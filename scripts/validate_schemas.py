#!/usr/bin/env python3
"""Validate JSON Schemas and every example against its schema.

Checks:
- each schemas/*.json is a valid Draft 2020-12 schema
- examples/**/storyboard*.json, hardware_profile*.json, job_event*.json validate
- storyboard semantics: unique scene ids, orders 1..n, on-screen text end > start
- config/*.yaml parse (if present)
Exit code 1 on any failure.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent

EXAMPLE_MAP = {
    "storyboard": "storyboard.v1.json",
    "hardware_profile": "hardware_profile.v1.json",
    "job_event": "job_event.v1.json",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def storyboard_semantic_errors(sb: dict) -> list[str]:
    errors = []
    scenes = sb.get("scenes", [])
    ids = [s["id"] for s in scenes]
    if len(ids) != len(set(ids)):
        errors.append("duplicate scene ids")
    if [s["order"] for s in scenes] != list(range(1, len(scenes) + 1)):
        errors.append("scene order must be 1..n in sequence")
    for s in scenes:
        for t in s.get("onscreen_text", []):
            if t["end_s"] <= t["start_s"]:
                errors.append(f"{s['id']}/{t['text_id']}: end_s must be after start_s")
    return errors


def validate_all(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    validators = {}
    for schema_path in sorted((root / "schemas").glob("*.json")):
        schema = load(schema_path)
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{schema_path.name}: invalid schema: {exc}")
            continue
        validators[schema_path.name] = Draft202012Validator(schema)

    for example in sorted((root / "examples").rglob("*.json")):
        for prefix, schema_name in EXAMPLE_MAP.items():
            if example.name.startswith(prefix):
                validator = validators.get(schema_name)
                if validator is None:
                    errors.append(f"{example}: schema {schema_name} missing")
                    break
                data = load(example)
                for err in validator.iter_errors(data):
                    loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                    errors.append(f"{example.relative_to(root)}: {loc}: {err.message}")
                if prefix == "storyboard":
                    rel = example.relative_to(root)
                    errors += [f"{rel}: {e}" for e in storyboard_semantic_errors(data)]
                break

    for cfg in sorted((root / "config").glob("*.y*ml")):
        try:
            yaml.safe_load(cfg.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{cfg.name}: invalid YAML: {exc}")
    return errors


def main() -> int:
    errors = validate_all()
    if errors:
        print("Schema validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Schema validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
