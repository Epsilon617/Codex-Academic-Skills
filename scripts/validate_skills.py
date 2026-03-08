#!/usr/bin/env python3

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "skills.csv"
EXPECTED_HEADERS = [
    "category_en",
    "category_zh",
    "skill_name",
    "description_en",
    "description_zh",
    "link",
    "host_repo",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_repo_from_link(link: str) -> str | None:
    parsed = urlparse(link)
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        return None

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    return f"{parts[0]}/{parts[1]}"


def main() -> None:
    if not CSV_PATH.exists():
        fail(f"missing file: {CSV_PATH}")

    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_HEADERS:
            fail(
                "unexpected CSV headers. "
                f"expected {EXPECTED_HEADERS}, got {reader.fieldnames}"
            )

        seen_rows: set[tuple[str, ...]] = set()
        seen_links: dict[str, tuple[str, str]] = {}
        category_pairs: dict[str, str] = {}

        for index, row in enumerate(reader, start=2):
            values = {key: (value or "").strip() for key, value in row.items()}

            missing = [key for key, value in values.items() if not value]
            if missing:
                fail(f"row {index} has empty fields: {', '.join(missing)}")

            row_key = tuple(values[key] for key in EXPECTED_HEADERS)
            if row_key in seen_rows:
                fail(f"row {index} duplicates an existing row")
            seen_rows.add(row_key)

            existing_link = seen_links.get(values["link"])
            if existing_link is None:
                seen_links[values["link"]] = (
                    values["skill_name"],
                    values["host_repo"],
                )
            elif existing_link != (values["skill_name"], values["host_repo"]):
                fail(
                    "row "
                    f"{index} reuses link {values['link']} for a different skill"
                )

            repo_from_link = parse_repo_from_link(values["link"])
            if repo_from_link is None:
                fail(
                    f"row {index} has an unsupported link format: {values['link']}"
                )

            if repo_from_link != values["host_repo"]:
                fail(
                    "row "
                    f"{index} has host_repo={values['host_repo']} but link points to "
                    f"{repo_from_link}"
                )

            mapped = category_pairs.setdefault(
                values["category_en"], values["category_zh"]
            )
            if mapped != values["category_zh"]:
                fail(
                    "row "
                    f"{index} maps category_en={values['category_en']} to "
                    f"multiple Chinese labels"
                )

    print(f"Validated {CSV_PATH.relative_to(ROOT)} successfully.")


if __name__ == "__main__":
    main()
