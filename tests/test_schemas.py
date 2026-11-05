import copy
import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate_schemas  # noqa: E402


def _validator(name):
    return Draft202012Validator(json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8")))


def _sample():
    path = ROOT / "examples" / "gideon" / "storyboard.json"
    return json.loads(path.read_text(encoding="utf-8"))


def test_repo_validates_clean():
    assert validate_schemas.validate_all() == []


def test_gideon_has_no_hand_set_duration():
    assert all("duration_s" not in s for s in _sample()["scenes"])


@pytest.mark.parametrize("missing", ["no text", "no lettering", "no watermark"])
def test_image_prompt_must_forbid_text(missing):
    sb = copy.deepcopy(_sample())
    sb["scenes"][0]["image"]["prompt"] = sb["scenes"][0]["image"]["prompt"].replace(missing, "")
    assert list(_validator("storyboard.v1.json").iter_errors(sb))


def test_bad_translation_rejected():
    sb = copy.deepcopy(_sample())
    sb["meta"]["translation"] = "NIV"
    assert list(_validator("storyboard.v1.json").iter_errors(sb))


def test_semantic_checks_catch_bad_order_and_text_window():
    sb = copy.deepcopy(_sample())
    sb["scenes"][1]["order"] = 5
    sb["scenes"][0]["onscreen_text"][0]["end_s"] = 0.1
    errs = validate_schemas.storyboard_semantic_errors(sb)
    assert any("order" in e for e in errs)
    assert any("end_s" in e for e in errs)


def test_tier0_profile_is_tier_zero():
    p = json.loads((ROOT / "examples" / "hardware_profile.tier0.json").read_text(encoding="utf-8"))
    assert p["tier"] == 0 and p["ram_gb"] == 16 and p["gpus"][0]["vram_gb"] == 2
