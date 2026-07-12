#!/usr/bin/env python3
"""Save a podcast Q&A session as a timestamped Obsidian note."""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def slugify(text: str) -> str:
    """Create a safe filename fragment from a title."""
    return re.sub(r"[\\/:*?\"<>|]", "", text).strip()


def build_frontmatter(show: str, episode: str, title: str, transcript: str, agent: str) -> str:
    """Generate Obsidian frontmatter for the Q&A note."""
    # Extract just the filename for wiki link if transcript is given as relative path
    transcript_name = Path(transcript).name if transcript else ""
    # Remove .md extension for wiki link
    link_target = transcript_name.removesuffix(".md") if transcript_name else ""
    display_title = title or f"{show} {episode}"

    source_line = f'source: "[[{link_target}|{display_title}]]"\n' if link_target else ""
    agent_line = f"agent: {agent}\n" if agent else ""

    return f"""---
title: {show} {episode} 问答：{title}
description: 基于《{display_title}》逐字稿的 AI 问答
tags:
  - podcast/{show}
  - podcast-qa
{source_line}{agent_line}is_diary: false
is_essay: true
is_wx_article: false
---

"""


def write_qa_note(vault: Path, show: str, episode: str, title: str, transcript: str, agent: str, content: str, timestamp: Optional[datetime] = None) -> Path:
    """Write the Q&A note to raw/inbox/."""
    inbox = vault / "raw" / "inbox"
    inbox.mkdir(parents=True, exist_ok=True)

    ts = timestamp or datetime.now()
    filename = f"{ts.strftime('%Y%m%d%H%M%S')}.md"
    note_path = inbox / filename

    # Avoid collision
    counter = 2
    original_path = note_path
    while note_path.exists():
        note_path = original_path.with_name(f"{original_path.stem}-{counter}.md")
        counter += 1

    frontmatter = build_frontmatter(show, episode, title, transcript, agent)
    note_path.write_text(frontmatter + content, encoding="utf-8")
    return note_path


def link_to_diary(vault: Path, note_path: Path, timestamp: Optional[datetime] = None) -> Optional[Path]:
    """Append a wiki link to today's diary note."""
    ts = timestamp or datetime.now()
    diary_dir = vault / "diary"
    diary_dir.mkdir(parents=True, exist_ok=True)
    diary_path = diary_dir / f"{ts.strftime('%Y%m%d')}.md"

    note_name = note_path.stem
    link = f"[[{note_name}]]"

    # Read existing diary frontmatter if present
    if diary_path.exists():
        existing = diary_path.read_text(encoding="utf-8")
        if link in existing:
            return diary_path
        new_content = existing.rstrip() + f"\n\n{link}\n"
    else:
        new_content = f"""---
title:
description:
tags:
is_diary: true
is_essay: false
is_wx_article: false
---

{link}
"""

    diary_path.write_text(new_content, encoding="utf-8")
    return diary_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Save podcast Q&A to Obsidian vault")
    parser.add_argument("--vault", required=True, help="Path to Obsidian vault root")
    parser.add_argument("--show", required=True, help="Podcast show name")
    parser.add_argument("--episode", required=True, help="Episode number or ID")
    parser.add_argument("--title", required=True, help="Episode title")
    parser.add_argument("--transcript", default="", help="Relative path to transcript note (e.g. raw/podcasts/...)")
    parser.add_argument("--agent", default="", help="AI agent name (e.g. 'Kimi Code', 'Claude Code'); leave empty if unknown")
    parser.add_argument("--content", default="", help="Q&A markdown content (inline)")
    parser.add_argument("--content-file", help="Path to file containing Q&A markdown content")
    parser.add_argument("--timestamp", help="Timestamp in YYYYMMDDHHMMSS format (default: now)")
    parser.add_argument("--link-diary", action="store_true", help="Also append wiki link to today's diary")

    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"ERROR: vault does not exist: {vault}", file=sys.stderr)
        return 1

    if args.content_file:
        content_path = Path(args.content_file).expanduser()
        if not content_path.is_file():
            print(f"ERROR: content file does not exist: {content_path}", file=sys.stderr)
            return 1
        content = content_path.read_text(encoding="utf-8")
    else:
        content = args.content

    if not content.strip():
        print("ERROR: content is empty", file=sys.stderr)
        return 1

    timestamp = None
    if args.timestamp:
        try:
            timestamp = datetime.strptime(args.timestamp, "%Y%m%d%H%M%S")
        except ValueError:
            print(f"ERROR: invalid timestamp format: {args.timestamp}", file=sys.stderr)
            return 1

    note_path = write_qa_note(
        vault=vault,
        show=args.show,
        episode=args.episode,
        title=args.title,
        transcript=args.transcript,
        agent=args.agent,
        content=content,
        timestamp=timestamp,
    )

    print(f"Wrote Q&A note: {note_path}")

    if args.link_diary:
        diary_path = link_to_diary(vault, note_path, timestamp)
        if diary_path:
            print(f"Linked in diary: {diary_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
