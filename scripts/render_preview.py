#!/usr/bin/env python3
"""Render one cognitive-first answer as standalone HTML and Markdown; stdlib only."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,24}$")
SUPPORTED = {"facts", "steps", "choice", "text", "callout", "details"}
INLINE = re.compile(r"\*\*(.+?)\*\*|==(.+?)==", re.DOTALL)

CSS = """
:root{color-scheme:light;--ink:#171717;--body:#303030;--muted:#686868;--surface:#f6f6f6;--line:#e8e8e8;--white:#fff;--content-width:720px;--r-card:14px;--s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:24px;--s6:32px;--s7:48px}
*{box-sizing:border-box}
html{font-size:16px}
body{margin:0;background:var(--white);color:var(--body);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:16px;line-height:1.75;-webkit-font-smoothing:antialiased}
main{width:min(calc(100% - 48px),var(--content-width));margin:60px auto 96px}
h1,h2,p{overflow-wrap:anywhere}
h1{color:var(--ink);font-size:clamp(22px,3vw,27px);line-height:1.35;letter-spacing:-.01em;margin:0 0 var(--s5);font-weight:660}
.lead{color:var(--ink);font-size:19px;font-weight:450;line-height:1.65;margin:0 0 var(--s4)}
strong{font-weight:680;color:var(--ink)}
mark{background:#ececec;color:inherit;border-radius:4px;padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.explain{font-size:16px;line-height:1.75;margin:0 0 var(--s5);white-space:pre-wrap}
section{margin:var(--s6) 0}
h2{color:var(--ink);font-size:17px;line-height:1.5;margin:0 0 var(--s3);font-weight:680;letter-spacing:0}
.card,.callout{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-card);padding:4px 18px}
.facts-row{display:grid;grid-template-columns:minmax(90px,28%) minmax(0,1fr);align-items:baseline;gap:var(--s4);padding:var(--s3) 0;border-bottom:1px solid #e6e6e6}
.facts-row:last-child{border-bottom:0}
.facts-label{color:var(--muted);font-size:13px;line-height:1.65}
.facts-value{font-size:16px;font-weight:550;line-height:1.7;overflow-wrap:anywhere}
.steps{list-style:none;margin:0;padding:0}
.step{display:grid;grid-template-columns:27px minmax(0,1fr);column-gap:var(--s3);padding:0 0 var(--s4)}
.step:last-child{padding-bottom:0}
.step-num{display:flex;align-items:center;justify-content:center;width:25px;height:25px;border-radius:50%;background:var(--surface);border:1px solid var(--line);color:var(--muted);font-size:12px;font-weight:650;line-height:1}
.step-title{color:var(--ink);font-size:16px;font-weight:650;line-height:1.6}
.step-detail{color:var(--muted);font-size:14px;line-height:1.7;margin-top:2px}
.paragraph{font-size:16px;line-height:1.8;white-space:pre-wrap;margin:0}
.callout{padding:var(--s4) 18px}
.callout-label{font-size:12px;line-height:1.6;color:var(--muted);margin:0 0 var(--s1)}
.callout-text{margin:0;font-size:16px;line-height:1.75}
.details{border-top:1px solid var(--line);padding-top:var(--s3)}
.details summary{cursor:pointer;font-size:14px;color:var(--muted);padding:var(--s2) 0}
.details p{margin:var(--s2) 0 0;font-size:15px;line-height:1.8;white-space:pre-wrap}
.quiz{border:1px solid var(--line);border-radius:var(--r-card);padding:18px;background:var(--white)}
.quiz-question{font-size:16px;line-height:1.75;font-weight:580;color:var(--ink);margin:0 0 var(--s3)}
fieldset{border:0;margin:0;padding:0;min-width:0}
legend{font-weight:450;color:var(--muted);font-size:13px;line-height:1.6;margin:0 0 var(--s2)}
.option{display:flex;align-items:flex-start;gap:var(--s3);min-height:44px;padding:10px 8px;border:1px solid transparent;border-radius:10px;cursor:pointer;font-size:15px;line-height:1.7}
.option:hover,.option.selected,.option:has(input:checked){background:var(--surface)}
.option.selected,.option:has(input:checked){border-color:var(--line)}
.option input{width:19px;height:19px;flex:none;margin:3px 0 0;accent-color:#171717}
.option span{flex:1;overflow-wrap:anywhere}
button{display:block;margin-top:var(--s4);min-height:44px;width:100%;border:0;background:#171717;color:#fff;border-radius:100px;padding:10px 18px;font-family:inherit;font-size:15px;font-weight:630;cursor:pointer}
button:disabled{background:#ebebeb;color:#777;cursor:not-allowed}
button:focus-visible,.option:focus-within,.details summary:focus-visible{outline:3px solid #266ab5;outline-offset:3px}
.feedback{margin-top:var(--s4);border:1px solid var(--line);border-radius:12px;padding:var(--s3) var(--s4);background:var(--surface);line-height:1.75;white-space:pre-wrap;font-size:15px}
.feedback[hidden]{display:none}
.next{padding:var(--s4) 18px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-card)}
.next-label{color:var(--muted);font-size:13px;margin:0 0 var(--s1)}
.next-text{font-size:16px;font-weight:550;margin:0;line-height:1.75}
@media(max-width:540px){main{width:min(calc(100% - 32px),var(--content-width));margin:32px auto 64px}h1{margin-bottom:20px}.lead{font-size:18px}.card{padding:4px 14px}.facts-row{grid-template-columns:85px minmax(0,1fr);gap:12px}.quiz{padding:14px}.option{font-size:15px}}
@media(prefers-reduced-motion:no-preference){button,.option{transition:background .14s ease}}
"""

JS = """
document.querySelectorAll('[data-choice-form]').forEach((form)=>{
  const submit=form.querySelector('button[type="submit"]');
  const feedback=form.querySelector('[data-feedback-box]');
  form.addEventListener('change',()=>{
    submit.disabled=!form.querySelector('input[type="radio"]:checked');
    form.querySelectorAll('.option').forEach((label)=>{
      label.classList.toggle('selected',!!label.querySelector('input:checked'));
    });
    feedback.hidden=true;
    feedback.textContent='';
  });
  form.addEventListener('submit',(event)=>{
    event.preventDefault();
    const checked=form.querySelector('input[type="radio"]:checked');
    if(!checked)return;
    feedback.textContent=checked.dataset.feedback||'已提交';
    feedback.hidden=false;
  });
});
"""


def require_text(value: Any, where: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{where} must be a non-empty string")
    return value.strip()


def require_list(value: Any, where: str, low: int, high: int) -> list[Any]:
    if not isinstance(value, list) or not low <= len(value) <= high:
        raise ValueError(f"{where} requires {low}–{high} entries")
    return value


def validate(doc: Any) -> dict[str, Any]:
    if not isinstance(doc, dict) or doc.get("schema_version") != 1:
        raise ValueError("schema_version must equal 1")
    for key in ("title", "lead"):
        require_text(doc.get(key), key)
    if "explanation" in doc:
        require_text(doc["explanation"], "explanation")
    if "next_action" in doc:
        require_text(doc["next_action"], "next_action")
    blocks = require_list(doc.get("blocks"), "blocks", 0, 12)
    choice_count = 0
    for n, block in enumerate(blocks):
        if not isinstance(block, dict):
            raise ValueError(f"blocks[{n}] must be an object")
        kind = block.get("type")
        if kind not in SUPPORTED:
            raise ValueError(f"blocks[{n}] unsupported type: {kind}")
        require_text(block.get("heading"), f"blocks[{n}].heading")
        if kind in {"facts", "steps"}:
            items = require_list(block.get("items"), f"blocks[{n}].items", 2, 5)
            for i, item in enumerate(items):
                if not isinstance(item, dict):
                    raise ValueError(f"blocks[{n}].items[{i}] must be an object")
                if kind == "facts":
                    require_text(item.get("label"), f"blocks[{n}].items[{i}].label")
                    require_text(item.get("value"), f"blocks[{n}].items[{i}].value")
                else:
                    require_text(item.get("title"), f"blocks[{n}].items[{i}].title")
                    require_text(item.get("detail"), f"blocks[{n}].items[{i}].detail")
        elif kind == "choice":
            choice_count += 1
            if choice_count > 1:
                raise ValueError("Only one diagnostic choice per answer")
            require_text(block.get("question"), f"blocks[{n}].question")
            options = require_list(block.get("options"), f"blocks[{n}].options", 2, 4)
            seen: set[str] = set()
            for i, option in enumerate(options):
                if not isinstance(option, dict):
                    raise ValueError(f"blocks[{n}].options[{i}] must be an object")
                option_id = require_text(option.get("id"), f"blocks[{n}].options[{i}].id")
                if not ID_PATTERN.fullmatch(option_id) or option_id in seen:
                    raise ValueError(f"Invalid or duplicate option id: {option_id}")
                seen.add(option_id)
                require_text(option.get("label"), f"blocks[{n}].options[{i}].label")
                require_text(option.get("feedback"), f"blocks[{n}].options[{i}].feedback")
        elif kind in {"callout", "details"}:
            require_text(block.get("body"), f"blocks[{n}].body")
            if kind == "details":
                require_text(block.get("summary"), f"blocks[{n}].summary")
            elif "eyebrow" in block:
                require_text(block["eyebrow"], f"blocks[{n}].eyebrow")
        else:
            require_text(block.get("body"), f"blocks[{n}].body")
    return doc


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rich(value: str) -> str:
    """Escape untrusted text, then render only **bold** and ==muted highlight==."""
    parts: list[str] = []
    offset = 0
    for match in INLINE.finditer(value):
        parts.append(esc(value[offset:match.start()]))
        if match.group(1) is not None:
            parts.append(f"<strong>{esc(match.group(1))}</strong>")
        else:
            parts.append(f"<mark>{esc(match.group(2))}</mark>")
        offset = match.end()
    parts.append(esc(value[offset:]))
    return "".join(parts)


def plain_markdown(value: str) -> str:
    """Portable fallback: highlights turn into GitHub-flavored bold."""
    return re.sub(r"==(.+?)==", r"**\1**", value, flags=re.DOTALL)


def render_block(block: dict[str, Any]) -> str:
    heading = f"<h2>{esc(block['heading'])}</h2>"
    kind = block["type"]
    if kind == "facts":
        rows = "".join(
            f'<div class="facts-row"><span class="facts-label">{esc(item["label"])}</span>'
            f'<span class="facts-value">{rich(item["value"])}</span></div>'
            for item in block["items"]
        )
        content = f'<div class="card">{rows}</div>'
    elif kind == "steps":
        stages = []
        for i, item in enumerate(block["items"]):
            stages.append(
                f'<li class="step"><span class="step-num" aria-hidden="true">{i+1}</span>'
                f'<div><div class="step-title">{rich(item["title"])}</div>'
                f'<div class="step-detail">{rich(item["detail"])}</div></div></li>'
            )
        content = f'<ol class="steps">{"".join(stages)}</ol>'
    elif kind == "text":
        content = f'<p class="paragraph">{rich(block["body"])}</p>'
    elif kind == "callout":
        eyebrow = (
            f'<p class="callout-label">{esc(block["eyebrow"])}</p>'
            if block.get("eyebrow") else ""
        )
        content = f'<div class="callout">{eyebrow}<p class="callout-text">{rich(block["body"])}</p></div>'
    elif kind == "details":
        content = (
            '<details class="details">'
            f'<summary>{esc(block["summary"])}</summary>'
            f'<p>{rich(block["body"])}</p></details>'
        )
    else:  # choice
        options = "".join(
            f'<label class="option"><input type="radio" name="answer" value="{esc(o["id"])}" '
            f'data-feedback="{esc(o["feedback"])}"><span>{esc(o["id"])}. {rich(o["label"])}</span></label>'
            for o in block["options"]
        )
        content = (
            f'<div class="quiz"><p class="quiz-question">{rich(block["question"])}</p>'
            '<form data-choice-form><fieldset><legend>请选择最符合你的选项</legend>'
            f'{options}</fieldset><button type="submit" disabled>提交我的情况</button>'
            '<div class="feedback" data-feedback-box role="status" aria-live="polite" hidden></div>'
            '</form></div>'
        )
    return f"<section>{heading}{content}</section>"


def render_html(doc: dict[str, Any]) -> str:
    blocks = "".join(render_block(block) for block in doc["blocks"])
    explain = f'<p class="explain">{rich(doc["explanation"])}</p>' if doc.get("explanation") else ""
    action = (
        '<section class="next"><p class="next-label">下一步</p>'
        f'<p class="next-text">{rich(doc["next_action"])}</p></section>'
        if doc.get("next_action") else ""
    )
    return (
        '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{esc(doc["title"])}</title><style>{CSS}</style></head><body>'
        f'<main><article><h1>{esc(doc["title"])}</h1><p class="lead">{rich(doc["lead"])}</p>'
        f'{explain}{blocks}{action}</article></main><script>{JS}</script></body></html>'
    )


def md_safe(s: str) -> str:
    return plain_markdown(s).replace("|", r"\|").replace("\n", " ")


def render_markdown(doc: dict[str, Any]) -> str:
    lines = [f'# {doc["title"]}', "", plain_markdown(doc["lead"]), ""]
    if doc.get("explanation"):
        lines += [plain_markdown(doc["explanation"]), ""]
    for block in doc["blocks"]:
        lines += [f'## {block["heading"]}', ""]
        if block["type"] == "facts":
            lines += ["| 信息槽 | 内容 |", "| --- | --- |"]
            lines += [
                f'| {md_safe(item["label"])} | {md_safe(item["value"])} |'
                for item in block["items"]
            ]
        elif block["type"] == "steps":
            lines += [
                f'{i+1}. **{plain_markdown(item["title"])}** — {plain_markdown(item["detail"])}'
                for i, item in enumerate(block["items"])
            ]
        elif block["type"] == "choice":
            lines += [plain_markdown(block["question"]), ""]
            lines += [f'- {o["id"]}. {plain_markdown(o["label"])}' for o in block["options"]]
            lines += ["", "回复对应选项即可继续；文字模式没有网页提交按钮。"]
        elif block["type"] == "callout":
            if block.get("eyebrow"):
                lines += [f'*{block["eyebrow"]}*', ""]
            lines += [f'> {plain_markdown(block["body"])}']
        elif block["type"] == "details":
            lines += [f'**{block["summary"]}**', "", plain_markdown(block["body"])]
        else:
            lines.append(plain_markdown(block["body"]))
        lines.append("")
    if doc.get("next_action"):
        lines += ["**下一步：** " + plain_markdown(doc["next_action"]), ""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON answer document")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for both outputs")
    parser.add_argument("--force", action="store_true", help="Replace the two generated files")
    args = parser.parse_args()
    try:
        doc = validate(json.loads(args.input.read_text(encoding="utf-8")))
        out = args.output_dir.resolve()
        out.mkdir(parents=True, exist_ok=True)
        html_path = out / (args.input.stem + ".html")
        md_path = out / (args.input.stem + ".md")
        for target in (html_path, md_path):
            if target.exists() and not args.force:
                raise FileExistsError(f"{target} already exists (use --force)")
        html_path.write_text(render_html(doc), encoding="utf-8")
        md_path.write_text(render_markdown(doc), encoding="utf-8")
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"render error: {exc}", file=sys.stderr)
        return 2
    print(f"HTML: {html_path}")
    print(f"Markdown: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
