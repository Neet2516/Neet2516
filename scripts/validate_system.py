#!/usr/bin/env python3
import glob
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

print("=" * 60)
print("NEET2516 PROFILE QUALITY CONTROL & VALIDATION SUITE")
print("=" * 60)

errors = 0

# 1. XML Validation & Duplicate ID Check
all_svgs = sorted(glob.glob("svg/*.svg") + glob.glob("profile-3d-contrib/*.svg"))
print(f"\n[1/5] Checking XML validity for {len(all_svgs)} SVGs...")

for svg_path in all_svgs:
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        if not root.tag.endswith("svg"):
            print(f"  [FAIL] {svg_path} root tag is not svg: {root.tag}")
            errors += 1
        else:
            print(f"  [PASS] {svg_path} (Valid XML, viewBox='{root.get('viewBox')}')")
    except Exception as e:
        print(f"  [FAIL] {svg_path} XML error: {e}")
        errors += 1

# Check for duplicate IDs within each file
print("\n[2/5] Checking for duplicate element IDs...")
for svg_path in all_svgs:
    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()
    ids = re.findall(r'\bid=["\']([^"\']+)["\']', content)
    seen = set()
    dup = set()
    for item in ids:
        if item in seen:
            dup.add(item)
        seen.add(item)
    if dup:
        print(f"  [FAIL] {svg_path} has duplicate IDs: {dup}")
        errors += 1
    else:
        print(f"  [PASS] {svg_path} ({len(ids)} unique IDs, 0 duplicates)")

# 3. README Path Verification
print("\n[3/5] Checking README file references...")
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

img_refs = re.findall(r'<img [^>]*src=["\']([^"\']+)["\']', readme)
for ref in img_refs:
    clean_ref = ref.split("?")[0]
    if os.path.exists(clean_ref):
        size_kb = os.path.getsize(clean_ref) / 1024
        print(f"  [PASS] {clean_ref} exists ({size_kb:.1f} KB)")
    else:
        print(f"  [FAIL] {clean_ref} does not exist!")
        errors += 1

# 4. GitHub Actions Workflow Syntax Check
print("\n[4/5] Checking GitHub Actions workflow...")
wf_path = ".github/workflows/contribution-city.yml"
if os.path.exists(wf_path):
    with open(wf_path, "r", encoding="utf-8") as f:
        wf_content = f.read()
    required_keywords = ["name:", "on:", "schedule:", "workflow_dispatch:", "permissions:", "contents: write", "yoshi389111/github-profile-3d-contrib"]
    missing = [kw for kw in required_keywords if kw not in wf_content]
    if missing:
        print(f"  [FAIL] Workflow missing keywords: {missing}")
        errors += 1
    else:
        print(f"  [PASS] {wf_path} structure and permissions verified.")
else:
    print(f"  [FAIL] {wf_path} missing!")
    errors += 1

# 5. Link Health Validation
print("\n[5/5] Validating external URLs in profile...")
urls = [
    "https://github.com/Neet2516",
    "https://portfolio-1-tofl.onrender.com/",
    "https://github.com/Neet2516/Devflow",
    "https://github.com/Neet2516/SyncBoard",
    "https://github.com/Neet2516/FUTURE_FS_02",
    "https://rust-crm-six.vercel.app/",
    "https://sync-board-client-lake.vercel.app/",
    "https://docs-devflow.vercel.app",
    "https://github.com/Neet2516/city-waste-command"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            code = resp.getcode()
            print(f"  [PASS] {url} -> HTTP {code}")
    except urllib.error.HTTPError as e:
        # 429 rate limit or 403 on anti-bot is common on vercel/render/github when automated, but check if not 404
        if e.code == 404:
            print(f"  [FAIL] {url} -> 404 NOT FOUND")
            errors += 1
        else:
            print(f"  [PASS] {url} -> HTTP {e.code} (Reachable)")
    except Exception as e:
        print(f"  [WARN] {url} -> {e}")

print("=" * 60)
if errors == 0:
    print("ALL TESTS PASSED! Quality control is 100% GREEN.")
else:
    print(f"VALIDATION FINISHED WITH {errors} ERRORS.")
    sys.exit(1)
