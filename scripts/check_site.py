"""Check a Hugo build: python3 scripts/check_site.py /path/to/public."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids, self.papers = [], set(), []
        self.paper = None
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a': self.links.append(a.get('href', ''))
        if tag == 'article' and a.get('class') == 'paper':
            self.paper = {'bold': 0, 'text': ''}
            self.papers.append(self.paper)
        if tag == 'strong' and self.paper is not None:
            self.paper['bold'] += 1
    def handle_endtag(self, tag):
        if tag == 'article': self.paper = None
    def handle_data(self, text):
        if self.paper is not None: self.paper['text'] += text

root = Path(sys.argv[1])
pages = {p.relative_to(root).as_posix(): Page(p) for p in root.rglob('*.html')}
listing = pages['publications/index.html']
assert len(listing.papers) >= 9, 'Missing publications'
assert {'published', 'preprints'} <= listing.ids
assert len(pages['index.html'].papers) == 3
for name, page in pages.items():
    for paper in page.papers:
        assert paper['bold'] == 1, (name, 'Exactly one highlighted author required')
        assert 'Junxiang Huang' in paper['text']
    for href in page.links:
        u = urlsplit(href)
        if u.scheme or u.netloc: continue
        target = root / unquote(u.path.lstrip('/')) if u.path.startswith('/') else (root / name).parent / unquote(u.path)
        if not u.path: target = root / name
        if target.is_dir(): target /= 'index.html'
        assert target.exists(), (name, href)
        if u.fragment and target.suffix == '.html':
            assert unquote(u.fragment) in Page(target).ids, (name, href, 'missing anchor')
    text = (root / name).read_text()
    assert 'Presidential Scholarship' not in text and '校长奖学金' not in text
    assert '/authors/et-al/' not in text
assert {'education','experience','awards','teaching','talks','service'} <= pages['experience/index.html'].ids
assert (root / 'uploads/resume.pdf').read_bytes() == Path('static/uploads/resume.pdf').read_bytes()
print(f'PASS: {len(listing.papers)} papers, author highlighting, internal links/anchors, experience sections, unchanged CV.')
