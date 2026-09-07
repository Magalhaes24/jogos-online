"""Montagem do EPUB. Só zipfile — o formato é simples demais para justificar
uma dependência."""
import datetime
import pathlib
import uuid
import zipfile

from . import mdlite

CONTAINER = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""

OPF = """<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid"
         xml:lang="pt-PT">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:%(uuid)s</dc:identifier>
    <dc:title>%(title)s</dc:title>
    <dc:creator>%(creator)s</dc:creator>
    <dc:language>pt-PT</dc:language>
    <dc:description>%(desc)s</dc:description>
    <dc:date>%(date)s</dc:date>
    <meta property="dcterms:modified">%(modified)s</meta>
  </metadata>
  <manifest>
%(manifest)s
  </manifest>
  <spine toc="ncx">
%(spine)s
  </spine>
</package>
"""

NCX = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN"
  "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="pt-PT">
  <head>
    <meta name="dtb:uid" content="urn:uuid:%(uuid)s"/>
    <meta name="dtb:depth" content="2"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>%(title)s</text></docTitle>
  <navMap>
%(navpoints)s
  </navMap>
</ncx>
"""

NAV = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"
      xml:lang="pt-PT" lang="pt-PT">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>Índice</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
<nav epub:type="toc" id="toc">
<h1 class="block">Índice</h1>
%s
</nav>
</body>
</html>
"""


class Book:
    """Acumula ficheiros e a árvore do índice, e escreve o .epub no fim."""

    def __init__(self, title: str, creator: str, description: str):
        self.title = title
        self.creator = creator
        self.description = description
        self.uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, "pocket-problem-book/" + title))
        self.docs: list[tuple[str, str]] = []      # (nome, conteúdo)
        self.spine: list[str] = []                 # nomes por ordem de leitura
        self.toc: list[dict] = []                  # {label, href, children:[...]}

    def add(self, name: str, content: str, spine: bool = True) -> None:
        self.docs.append((name, content))
        if spine:
            self.spine.append(name)

    def toc_entry(self, label: str, href: str, children: list | None = None) -> None:
        self.toc.append({"label": label, "href": href, "children": children or []})

    # ── escrita ────────────────────────────────────────────────────────
    def write(self, path: pathlib.Path, css: str) -> pathlib.Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        manifest, spine = self._manifest_and_spine()
        now = datetime.datetime.now(datetime.timezone.utc)
        fields = dict(uuid=self.uuid, title=mdlite.esc(self.title),
                      creator=mdlite.esc(self.creator), desc=mdlite.esc(self.description),
                      date=now.strftime("%Y-%m-%d"),
                      modified=now.strftime("%Y-%m-%dT%H:%M:%SZ"),
                      manifest=manifest, spine=spine)

        with zipfile.ZipFile(path, "w") as z:
            # o mimetype tem de ser o primeiro e sem compressão
            z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
                       compress_type=zipfile.ZIP_STORED)
            z.writestr("META-INF/container.xml", CONTAINER, zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/content.opf", OPF % fields, zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/toc.ncx", NCX % dict(uuid=self.uuid,
                                                   title=mdlite.esc(self.title),
                                                   navpoints=self._navpoints()),
                       zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/nav.xhtml", NAV % self._nav_list(), zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/style.css", css, zipfile.ZIP_DEFLATED)
            for name, content in self.docs:
                z.writestr("OEBPS/" + name, content, zipfile.ZIP_DEFLATED)
        return path

    def _manifest_and_spine(self) -> tuple[str, str]:
        items = ['    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                 '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" '
                 'properties="nav"/>',
                 '    <item id="css" href="style.css" media-type="text/css"/>']
        for i, (name, _) in enumerate(self.docs):
            items.append('    <item id="d%d" href="%s" media-type="application/xhtml+xml"/>'
                         % (i, name))
        index = {name: "d%d" % i for i, (name, _) in enumerate(self.docs)}
        spine = ["    <itemref idref=\"%s\"/>" % index[n] for n in self.spine]
        return "\n".join(items), "\n".join(spine)

    def _navpoints(self) -> str:
        out, counter = [], [0]

        def emit(entries, depth):
            for e in entries:
                counter[0] += 1
                n = counter[0]
                out.append('%s<navPoint id="n%d" playOrder="%d">' % ("  " * depth, n, n))
                out.append('%s  <navLabel><text>%s</text></navLabel>'
                           % ("  " * depth, mdlite.esc(e["label"])))
                out.append('%s  <content src="%s"/>' % ("  " * depth, e["href"]))
                emit(e["children"], depth + 1)
                out.append("%s</navPoint>" % ("  " * depth))

        emit(self.toc, 2)
        return "\n".join(out)

    def _nav_list(self) -> str:
        def build(entries):
            lis = []
            for e in entries:
                inner = '<a href="%s">%s</a>' % (e["href"], mdlite.esc(e["label"]))
                if e["children"]:
                    inner += build(e["children"])
                lis.append("<li>%s</li>" % inner)
            return "<ol>%s</ol>" % "".join(lis)

        return build(self.toc)
