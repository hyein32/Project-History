"""각 폴더의 project.json 을 읽어 README.md 의 프로젝트 표를 다시 만든다."""
import json
from pathlib import Path

START, END = "<!-- PROJECTS:START -->", "<!-- PROJECTS:END -->"
root = Path(__file__).resolve().parents[2]

rows = []
for f in sorted(root.glob("*/project.json")):
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"{f}: JSON 형식 오류 - {e}")
    folder = f.parent.name
    d.setdefault("title", folder)
    rows.append((folder, d))

rows.sort(key=lambda r: (r[1].get("semester", ""), r[0]), reverse=True)

def cell(v):
    return str(v).replace("|", "\\|").replace("\n", " ") if v else "-"

lines = ["| 프로젝트 | 설명 | 학년 | 수업 | 학기 | 기술 | 링크 |", "|---|---|---|---|---|---|---|"]
for folder, d in rows:
    tech = ", ".join(d.get("tech", [])) if isinstance(d.get("tech"), list) else d.get("tech")
    links = [f"[코드](./{folder.replace(' ', '%20')}/)"]
    if d.get("demo"):
        links.insert(0, f"[데모]({d['demo']})")
    lines.append("| " + " | ".join([
        cell(d["title"]), cell(d.get("summary")), cell(d.get("grade")),
        cell(d.get("course")), cell(d.get("semester")), cell(tech), " · ".join(links),
    ]) + " |")
table = "\n".join(lines)

readme = root / "README.md"
text = readme.read_text(encoding="utf-8")
block = f"{START}\n{table}\n{END}"
if START in text and END in text:
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    text = head + block + tail
else:
    text = text.rstrip("\n") + "\n\n## 프로젝트 목록\n\n" + block + "\n"
readme.write_text(text, encoding="utf-8")
