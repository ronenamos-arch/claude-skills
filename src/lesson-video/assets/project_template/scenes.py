# -*- coding: utf-8 -*-
"""Illustration prompts for this lesson (gen_images.py reads SCENES, the era sets and ANCIENT).
Write the subject only; the art style and the people/era block are appended automatically.
Name = file name in clip/assets/img/. Plan ~1 picture per 60-75s of lesson + "thumb-hero"."""

# 18th-19th century scenes get the HISTORIC block (period clothing, no modern items).
HISTORIC_SCENES = set()
# Ancient-world scenes get the ANCIENT block below.
ANCIENT_SCENES = set()

ANCIENT = (
    "ANCIENT ERA (STRICT): simple period robes, cloaks and head cloths, no modern items, no anachronisms. "
    "Prefer distant small figures in crowd scenes. No identifiable real people."
)

SCENES = {
    "thumb-hero": "A single warm, striking scene that sums up the lesson, one clear subject on the LEFT half, "
                  "the right half calmer and darker for a big title; cinematic light.",
    "example-team-meeting": "A small accounting team around a table in a bright office, laptops open, a screen showing "
                            "a simple chart, warm daylight.",
}
