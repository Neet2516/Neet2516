#!/usr/bin/env python3
"""
scripts/build_svgs.py
Deterministic build engine for all Neet2516 Midnight Crimson SVGs.
Generates, validates XML, and saves all SVG components.
"""

import base64
import os
import xml.etree.ElementTree as ET

os.makedirs("svg", exist_ok=True)
os.makedirs("profile-3d-contrib", exist_ok=True)

def load_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

PORTRAIT_B64 = load_b64("assets/character-portrait-opt.png")
POINTING_B64 = load_b64("assets/character-pointing-sticker.png")
B64_COMPLETIONIST = load_b64("assets/badges/hacktoberfest-completionist-opt.png")
B64_CHALLENGE = load_b64("assets/badges/hacktoberfest-challenge-opt.png")
B64_ATTENDEE = load_b64("assets/badges/hacktoberfest-attendee-opt.png")
B64_DEBUT = load_b64("assets/badges/dev-writing-debut-opt.png")

def validate_and_save(filename, svg_content):
    try:
        ET.fromstring(svg_content)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"✓ Valid XML & Saved: {filename} ({len(svg_content)} bytes)")
    except Exception as e:
        print(f"✗ XML Validation Error in {filename}: {e}")
        raise e

# Read existing fixed SVGs to ensure exact preservation
print("Synchronizing all SVG components...")
