#!/usr/bin/env python3
"""Validate the exported static site using Python's standard library and Node.js."""
from pathlib import Path
from html.parser import HTMLParser
import base64
import json
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "dist"
HTML = (PUBLIC / "index.html").read_text(encoding="utf-8")

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.anchors = []
        self.controls = []
        self.images = []
        self.scripts = []
        self.h1_count = 0
        self.stack = []
        self.in_script = False
        self.current_script = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(tag)
        if "id" in values:
            self.ids.append(values["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "a" and values.get("href", "").startswith("#"):
            self.anchors.append(values["href"][1:])
        if "aria-controls" in values:
            self.controls.extend(values["aria-controls"].split())
        if tag == "img":
            self.images.append(values)
        if tag == "script":
            self.in_script = True
            self.current_script = []

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f"Unbalanced HTML: {tag}"
        self.stack.pop()
        if tag == "script":
            self.in_script = False
            self.scripts.append("".join(self.current_script))

    def handle_data(self, data):
        if self.in_script:
            self.current_script.append(data)

page = Inspect()
page.feed(HTML)
page.close()
assert not page.stack, "Unclosed HTML elements"
assert page.h1_count == 1, "Expected one primary heading"
assert len(page.ids) == len(set(page.ids)), "Duplicate element IDs"
assert all(x in page.ids for x in page.anchors), "Missing anchor target"
assert all(x in page.ids for x in page.controls), "Missing accessible control target"
assert len(page.images) == 2, "Unexpected image count"
for image in page.images:
    assert image.get("alt"), "Missing image alt text"
    src = image["src"]
    if src.startswith("data:image/jpeg;base64,"):
        data = base64.b64decode(src.split(",", 1)[1], validate=True)
        assert data.startswith(b"\xff\xd8") and data.endswith(b"\xff\xd9"), "Invalid embedded JPEG envelope"
    else:
        asset = (PUBLIC / src).resolve()
        assert asset.is_relative_to(PUBLIC.resolve()), "Asset outside public directory"
        assert asset.is_file() and asset.stat().st_size > 0, f"Missing asset: {src}"
assert "height:auto" in HTML, "Responsive image sizing missing"
config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
assert config["outputDirectory"] == "dist", "Unexpected deployment directory"
node = shutil.which("node")
assert node, "Node.js is required for JavaScript syntax validation"
with tempfile.TemporaryDirectory() as tmp:
    for i, script in enumerate(page.scripts):
        path = Path(tmp) / f"inline-{i}.js"
        path.write_text(script, encoding="utf-8")
        subprocess.run([node, "--check", str(path)], check=True, capture_output=True, text=True)
print("OK: HTML structure, headings, anchors, accessible targets, images, deployment configuration and JavaScript syntax.")
print("Visual testing and live contact flows must be reviewed separately before client launch.")
