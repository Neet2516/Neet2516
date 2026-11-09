#!/usr/bin/env python3
import base64
import os
import xml.etree.ElementTree as ET

# Load optimized badge images
def load_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

B64_COMPLETIONIST = load_b64("assets/badges/hacktoberfest-completionist-opt.png")
B64_CHALLENGE = load_b64("assets/badges/hacktoberfest-challenge-opt.png")
B64_ATTENDEE = load_b64("assets/badges/hacktoberfest-attendee-opt.png")
B64_DEBUT = load_b64("assets/badges/dev-writing-debut-opt.png")

def generate_community_badges():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="comm-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="comm-glow-left" cx="20%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="comm-glow-right" cx="80%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#F05033" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="comm-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.4"/>
    </linearGradient>

    <linearGradient id="comm-badge-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#991B1B" stop-opacity="0.2"/>
    </linearGradient>

    <pattern id="comm-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="11" cy="11" r="0.75" fill="#F05033" fill-opacity="0.1"/>
    </pattern>

    <filter id="comm-badge-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#DC2626" flood-opacity="0.4"/>
    </filter>
  </defs>

  <style>
    .comm-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .comm-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes comm-pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.35; }}
    }}
    @keyframes comm-badge-hover {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-3px); }}
    }}

    .comm-beacon {{ animation: comm-pulse 2s infinite ease-in-out; }}
    .comm-float-1 {{ animation: comm-badge-hover 3s infinite ease-in-out; }}
    .comm-float-2 {{ animation: comm-badge-hover 3s infinite ease-in-out 0.5s; }}
    .comm-float-3 {{ animation: comm-badge-hover 3s infinite ease-in-out 1s; }}
    .comm-float-4 {{ animation: comm-badge-hover 3s infinite ease-in-out 1.5s; }}
  </style>

  <!-- Background -->
  <rect width="940" height="480" rx="20" fill="url(#comm-bg-grad)"/>
  <rect width="940" height="480" rx="20" fill="url(#comm-glow-left)"/>
  <rect width="940" height="480" rx="20" fill="url(#comm-glow-right)"/>
  <rect width="940" height="480" rx="20" fill="url(#comm-dots)"/>
  <rect x="1" y="1" width="938" height="478" rx="19" fill="none" stroke="url(#comm-border-grad)" stroke-width="1.5"/>

  <!-- Section Header -->
  <g transform="translate(36, 32)">
    <rect x="0" y="0" width="220" height="22" rx="5" fill="#14141E" stroke="#DC2626" stroke-opacity="0.3" stroke-width="1"/>
    <circle cx="10" cy="11" r="3.5" fill="#DC2626"/>
    <text x="20" y="14.5" fill="#F05033" class="comm-font-mono" font-size="9" font-weight="700" letter-spacing="1">DEV COMMUNITY &amp; HACKTOBERFEST</text>

    <text x="0" y="44" fill="#F8FAFC" class="comm-font-display" font-size="20" font-weight="800" letter-spacing="-0.4">OPEN SOURCE BADGES &amp; WRITING</text>
    <text x="385" y="44" fill="#A1A1AA" class="comm-font-mono" font-size="11.5">// VERIFIED CONTRIBUTOR MILESTONES</text>
  </g>

  <!-- ================= LEFT: 4 HACKTOBERFEST & DEV BADGES ================= -->
  <g transform="translate(30, 88)">
    <rect width="425" height="364" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#comm-border-grad)" stroke-width="1.2"/>

    <!-- Header inside card -->
    <g transform="translate(20, 22)">
      <circle class="comm-beacon" cx="4" cy="4" r="3.5" fill="#DC2626"/>
      <text x="14" y="7" fill="#F05033" class="comm-font-mono" font-size="10" font-weight="700">VERIFIED BADGES // DIGITALOCEAN &amp; DEV.TO</text>
      <text x="0" y="24" fill="#F8FAFC" class="comm-font-display" font-size="14" font-weight="700">Hacktoberfest 2026 Honors</text>
    </g>
    <line x1="20" y1="54" x2="405" y2="54" stroke="#1B1922" stroke-width="1"/>

    <!-- 2x2 Grid of Badges -->
    <!-- Badge 1: Completionist (Top Left) -->
    <g class="comm-float-1" transform="translate(20, 68)" filter="url(#comm-badge-glow)">
      <rect width="186" height="106" rx="10" fill="#1B1922" stroke="url(#comm-badge-card-border)" stroke-width="1"/>
      <image href="data:image/png;base64,{B64_COMPLETIONIST}" x="12" y="14" width="56" height="66" preserveAspectRatio="xMidYMid meet"/>
      <text x="76" y="34" fill="#F8FAFC" class="comm-font-display" font-size="11.5" font-weight="700">Hacktoberfest</text>
      <text x="76" y="50" fill="#F05033" class="comm-font-mono" font-size="10" font-weight="700">Completionist</text>
      <text x="76" y="68" fill="#A1A1AA" class="comm-font-mono" font-size="8.5">Official Milestone</text>
      <rect x="76" y="76" width="62" height="16" rx="3" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.4" stroke-width="0.8"/>
      <text x="82" y="87" fill="#DC2626" class="comm-font-mono" font-size="8" font-weight="700">VERIFIED ✓</text>
    </g>

    <!-- Badge 2: Challenge Completion (Top Right) -->
    <g class="comm-float-2" transform="translate(218, 68)" filter="url(#comm-badge-glow)">
      <rect width="186" height="106" rx="10" fill="#1B1922" stroke="url(#comm-badge-card-border)" stroke-width="1"/>
      <image href="data:image/png;base64,{B64_CHALLENGE}" x="12" y="18" width="56" height="56" preserveAspectRatio="xMidYMid meet"/>
      <text x="76" y="34" fill="#F8FAFC" class="comm-font-display" font-size="11.5" font-weight="700">Challenge 2026</text>
      <text x="76" y="50" fill="#F05033" class="comm-font-mono" font-size="10" font-weight="700">Completion</text>
      <text x="76" y="68" fill="#A1A1AA" class="comm-font-mono" font-size="8.5">DEV × Hacktober</text>
      <rect x="76" y="76" width="62" height="16" rx="3" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.4" stroke-width="0.8"/>
      <text x="82" y="87" fill="#DC2626" class="comm-font-mono" font-size="8" font-weight="700">AWARDED 🏆</text>
    </g>

    <!-- Badge 3: Fest Attendee (Bottom Left) -->
    <g class="comm-float-3" transform="translate(20, 186)" filter="url(#comm-badge-glow)">
      <rect width="186" height="106" rx="10" fill="#1B1922" stroke="url(#comm-badge-card-border)" stroke-width="1"/>
      <image href="data:image/png;base64,{B64_ATTENDEE}" x="12" y="14" width="56" height="66" preserveAspectRatio="xMidYMid meet"/>
      <text x="76" y="34" fill="#F8FAFC" class="comm-font-display" font-size="11.5" font-weight="700">Fest Attendee</text>
      <text x="76" y="50" fill="#F05033" class="comm-font-mono" font-size="10" font-weight="700">Hacktoberfest</text>
      <text x="76" y="68" fill="#A1A1AA" class="comm-font-mono" font-size="8.5">Global Contributor</text>
      <rect x="76" y="76" width="62" height="16" rx="3" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.4" stroke-width="0.8"/>
      <text x="82" y="87" fill="#DC2626" class="comm-font-mono" font-size="8" font-weight="700">ATTENDEE 🎖️</text>
    </g>

    <!-- Badge 4: Writing Debut (Bottom Right) -->
    <g class="comm-float-4" transform="translate(218, 186)" filter="url(#comm-badge-glow)">
      <rect width="186" height="106" rx="10" fill="#1B1922" stroke="url(#comm-badge-card-border)" stroke-width="1"/>
      <image href="data:image/png;base64,{B64_DEBUT}" x="12" y="18" width="56" height="56" preserveAspectRatio="xMidYMid meet"/>
      <text x="76" y="34" fill="#F8FAFC" class="comm-font-display" font-size="11.5" font-weight="700">Writing Debut</text>
      <text x="76" y="50" fill="#F05033" class="comm-font-mono" font-size="10" font-weight="700">DEV.to Author</text>
      <text x="76" y="68" fill="#A1A1AA" class="comm-font-mono" font-size="8.5">Technical Writing</text>
      <rect x="76" y="76" width="62" height="16" rx="3" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.4" stroke-width="0.8"/>
      <text x="82" y="87" fill="#DC2626" class="comm-font-mono" font-size="8" font-weight="700">AUTHOR ✍️</text>
    </g>

    <!-- Milestone Repo Callout at Bottom -->
    <g transform="translate(20, 304)">
      <rect width="384" height="42" rx="8" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.3" stroke-width="1"/>
      <a href="https://github.com/Neet2516/hacktoberfest-dev-4" target="_blank">
        <text x="14" y="18" fill="#F8FAFC" class="comm-font-mono" font-size="10" font-weight="700">Neet2516/hacktoberfest-dev-4 ↗</text>
      </a>
      <text x="14" y="32" fill="#A1A1AA" class="comm-font-mono" font-size="8.5">Dedicated milestone repository for Hacktoberfest open-source tasks</text>
      <text x="325" y="24" fill="#F05033" class="comm-font-mono" font-size="9" font-weight="700">[ PR VERIFIED ]</text>
    </g>
  </g>

  <!-- ================= RIGHT: DEV COMMUNITY DISPATCH & ARTICLES ================= -->
  <g transform="translate(485, 88)">
    <rect width="425" height="364" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#comm-border-grad)" stroke-width="1.2"/>

    <!-- DEV Author Identity -->
    <g transform="translate(20, 20)">
      <!-- DEV Badge -->
      <rect width="42" height="26" rx="4" fill="#0D0E16" stroke="#DC2626" stroke-width="1.2"/>
      <text x="8" y="18" fill="#FFFFFF" class="comm-font-mono" font-size="11" font-weight="800">DEV</text>

      <!-- Author Handle -->
      <text x="52" y="12" fill="#F8FAFC" class="comm-font-display" font-size="13" font-weight="700">Navneet Sinha</text>
      <a href="https://dev.to/navneet_sinha" target="_blank">
        <text x="52" y="25" fill="#F05033" class="comm-font-mono" font-size="9.5">@navneet_sinha · dev.to/navneet_sinha ↗</text>
      </a>

      <!-- Bio / Message -->
      <text x="0" y="44" fill="#A1A1AA" class="comm-font-display" font-size="10.5">
        "Software Developer passionate about open source and web technologies."
      </text>
    </g>
    <line x1="20" y1="74" x2="405" y2="74" stroke="#1B1922" stroke-width="1"/>

    <!-- Featured DEV Articles (4 Publications) -->
    <g transform="translate(20, 86)">
      <text x="0" y="0" fill="#DC2626" class="comm-font-mono" font-size="9" font-weight="700" letter-spacing="1">FEATURED TECHNICAL ESSAYS // DEV.TO</text>

      <!-- Article 1: SPECTER -->
      <g transform="translate(0, 10)">
        <rect width="385" height="52" rx="6" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.2" stroke-width="0.8"/>
        <text x="10" y="16" fill="#F8FAFC" class="comm-font-display" font-size="10.5" font-weight="700">SPECTER 👻: The Ghost Maintainer</text>
        <text x="10" y="30" fill="#A1A1AA" class="comm-font-display" font-size="9">Autonomous multi-agent AI system resurrecting abandoned repos.</text>
        <a href="https://dev.to/navneet_sinha/specter-the-ghost-maintainer-autonomous-multi-agent-ai-system-resurrecting-abandoned-170n" target="_blank">
          <text x="10" y="44" fill="#F05033" class="comm-font-mono" font-size="8.5">dev.to/navneet_sinha/specter... ↗</text>
        </a>
        <text x="315" y="30" fill="#DC2626" class="comm-font-mono" font-size="8.5" font-weight="700">[ MULTI-AGENT ]</text>
      </g>

      <!-- Article 2: PatchGarden -->
      <g transform="translate(0, 68)">
        <rect width="385" height="52" rx="6" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.2" stroke-width="0.8"/>
        <text x="10" y="16" fill="#F8FAFC" class="comm-font-display" font-size="10.5" font-weight="700">PatchGarden 🌱: AI Maintenance Engineer</text>
        <text x="10" y="30" fill="#A1A1AA" class="comm-font-display" font-size="9">Built an AI maintenance engineer that doesn't trust its own patches.</text>
        <a href="https://dev.to/navneet_sinha/patchgarden-i-built-an-ai-maintenance-engineer-that-doesnt-trust-its-own-patches-3jj9" target="_blank">
          <text x="10" y="44" fill="#F05033" class="comm-font-mono" font-size="8.5">dev.to/navneet_sinha/patchgarden... ↗</text>
        </a>
        <text x="325" y="30" fill="#DC2626" class="comm-font-mono" font-size="8.5" font-weight="700">[ ZERO-TRUST ]</text>
      </g>

      <!-- Article 3: ZeroTrace -->
      <g transform="translate(0, 126)">
        <rect width="385" height="52" rx="6" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.2" stroke-width="0.8"/>
        <text x="10" y="16" fill="#F8FAFC" class="comm-font-display" font-size="10.5" font-weight="700">ZeroTrace: Air-Gapped Zero-Day SOC Copilot</text>
        <text x="10" y="30" fill="#A1A1AA" class="comm-font-display" font-size="9">Air-gapped behavioral anomaly detection for novel zero-day attacks.</text>
        <a href="https://dev.to/navneet_sinha/zerotrace-an-air-gapped-zero-day-behavioral-soc-copilot-db2" target="_blank">
          <text x="10" y="44" fill="#F05033" class="comm-font-mono" font-size="8.5">dev.to/navneet_sinha/zerotrace... ↗</text>
        </a>
        <text x="325" y="30" fill="#DC2626" class="comm-font-mono" font-size="8.5" font-weight="700">[ AIR-GAPPED ]</text>
      </g>

      <!-- Article 4: Ghost-Hunter -->
      <g transform="translate(0, 184)">
        <rect width="385" height="52" rx="6" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.2" stroke-width="0.8"/>
        <text x="10" y="16" fill="#F8FAFC" class="comm-font-display" font-size="10.5" font-weight="700">Ghost-Hunter: Temporal Sentinel (Local Gemma 3)</text>
        <text x="10" y="30" fill="#A1A1AA" class="comm-font-display" font-size="9">Temporal-powered follow-up sentinel using local on-device Gemma 3.</text>
        <a href="https://dev.to/navneet_sinha/ghost-hunter-an-air-gapped-temporal-powered-follow-up-sentinel-with-local-gemma-3-4ok0" target="_blank">
          <text x="10" y="44" fill="#F05033" class="comm-font-mono" font-size="8.5">dev.to/navneet_sinha/ghost-hunter... ↗</text>
        </a>
        <text x="325" y="30" fill="#DC2626" class="comm-font-mono" font-size="8.5" font-weight="700">[ LOCAL LLM ]</text>
      </g>
    </g>

    <!-- Footer link -->
    <g transform="translate(20, 334)">
      <a href="https://dev.to/navneet_sinha" target="_blank">
        <text x="0" y="0" fill="#FFFFFF" class="comm-font-mono" font-size="9.5" font-weight="700" text-decoration="underline">Read all technical articles on DEV.to (@navneet_sinha) ↗</text>
      </a>
    </g>
  </g>
</svg>"""

content = generate_community_badges()
ET.fromstring(content)
with open("svg/community-badges.svg", "w", encoding="utf-8") as f:
    f.write(content)
print(f"✓ Valid XML & Saved svg/community-badges.svg ({len(content)} bytes)")
