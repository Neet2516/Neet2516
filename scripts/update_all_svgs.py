#!/usr/bin/env python3
import base64
import os
import xml.etree.ElementTree as ET

# Helper to load b64
def b64_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

PORTRAIT_B64 = b64_file("assets/character-portrait-opt.png")
POINTING_B64 = b64_file("assets/character-pointing-sticker.png")
B64_COMPLETIONIST = b64_file("assets/badges/hacktoberfest-completionist-opt.png")
B64_CHALLENGE = b64_file("assets/badges/hacktoberfest-challenge-opt.png")
B64_ATTENDEE = b64_file("assets/badges/hacktoberfest-attendee-opt.png")
B64_DEBUT = b64_file("assets/badges/dev-writing-debut-opt.png")

# -------------------------------------------------------------
# 1. UPDATE CONNECT.SVG (INCLUDE DEV.TO CARD)
# -------------------------------------------------------------
def build_connect():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 500" width="100%" height="100%">
  <defs>
    <linearGradient id="conn-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="conn-glow-left" cx="25%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="conn-glow-right" cx="75%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#F05033" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="conn-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.4"/>
    </linearGradient>

    <linearGradient id="conn-neon-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="#F05033"/>
      <stop offset="100%" stop-color="#DC2626"/>
    </linearGradient>

    <linearGradient id="conn-manifesto-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="50%" stop-color="#F05033"/>
      <stop offset="100%" stop-color="#DC2626"/>
    </linearGradient>

    <filter id="conn-neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur1"/>
      <feGaussianBlur stdDeviation="8" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="conn-sticker-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#DC2626" flood-opacity="0.4"/>
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000000" flood-opacity="0.7"/>
    </filter>

    <pattern id="conn-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="11" cy="11" r="0.75" fill="#F05033" fill-opacity="0.1"/>
    </pattern>
  </defs>

  <style>
    .conn-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .conn-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes conn-flicker {{
      0%, 100% {{ opacity: 1; }}
      92% {{ opacity: 1; }}
      93% {{ opacity: 0.65; }}
      94% {{ opacity: 1; }}
      96% {{ opacity: 0.8; }}
      97% {{ opacity: 1; }}
    }}
    @keyframes conn-sparkle-float {{
      0%, 100% {{ transform: translateY(0) scale(1); opacity: 0.9; }}
      50% {{ transform: translateY(-8px) scale(1.2); opacity: 0.4; }}
    }}
    @keyframes conn-heart-pulse {{
      0%, 100% {{ transform: scale(1) translateY(0); opacity: 0.8; }}
      50% {{ transform: scale(1.15) translateY(-5px); opacity: 1; }}
    }}
    @keyframes conn-chevron-shift {{
      0% {{ transform: translateX(0); opacity: 0.3; }}
      50% {{ opacity: 1; }}
      100% {{ transform: translateX(12px); opacity: 0.3; }}
    }}
    @keyframes conn-char-sway {{
      0%, 100% {{ transform: translateY(0) rotate(0deg); }}
      50% {{ transform: translateY(-4px) rotate(0.5deg); }}
    }}

    .conn-neon {{ animation: conn-flicker 4s infinite; }}
    .conn-sparkle-1 {{ animation: conn-sparkle-float 3s infinite ease-in-out; }}
    .conn-sparkle-2 {{ animation: conn-sparkle-float 2.5s infinite ease-in-out 1s; }}
    .conn-sparkle-3 {{ animation: conn-sparkle-float 3.5s infinite ease-in-out 0.5s; }}
    .conn-heart-1 {{ animation: conn-heart-pulse 2.2s infinite ease-in-out; }}
    .conn-heart-2 {{ animation: conn-heart-pulse 2.8s infinite ease-in-out 0.8s; }}
    .conn-arrow {{ animation: conn-chevron-shift 1.6s infinite ease-in-out; }}
    .conn-character {{ animation: conn-char-sway 4s infinite ease-in-out; transform-origin: 190px 440px; }}
  </style>

  <!-- Background -->
  <rect width="940" height="500" rx="20" fill="url(#conn-bg-grad)"/>
  <rect width="940" height="500" rx="20" fill="url(#conn-glow-left)"/>
  <rect width="940" height="500" rx="20" fill="url(#conn-glow-right)"/>
  <rect width="940" height="500" rx="20" fill="url(#conn-dots)"/>
  <rect x="1" y="1" width="938" height="498" rx="19" fill="none" stroke="url(#conn-border-grad)" stroke-width="1.5"/>

  <!-- Pedestal glow -->
  <ellipse cx="200" cy="445" rx="130" ry="24" fill="#DC2626" fill-opacity="0.14"/>
  <ellipse cx="200" cy="445" rx="80" ry="14" fill="#F05033" fill-opacity="0.2"/>

  <!-- Character Group -->
  <g class="conn-character" filter="url(#conn-sticker-glow)">
    <image href="data:image/png;base64,{POINTING_B64}" x="40" y="52" width="310" height="385" preserveAspectRatio="xMidYMid meet"/>
  </g>

  <!-- Floating Sparkles (✦) -->
  <g class="conn-sparkle-1" transform="translate(68, 70)">
    <path d="M 0 -8 Q 0 0 8 0 Q 0 0 0 8 Q 0 0 -8 0 Q 0 0 0 -8 Z" fill="#FFFFFF"/>
    <circle cx="0" cy="0" r="2" fill="#F05033"/>
  </g>
  <g class="conn-sparkle-2" transform="translate(48, 230)">
    <path d="M 0 -6 Q 0 0 6 0 Q 0 0 0 6 Q 0 0 -6 0 Q 0 0 0 -6 Z" fill="#F05033"/>
  </g>
  <g class="conn-sparkle-3" transform="translate(330, 150)">
    <path d="M 0 -9 Q 0 0 9 0 Q 0 0 0 9 Q 0 0 -9 0 Q 0 0 0 -9 Z" fill="#DC2626"/>
    <circle cx="0" cy="0" r="2.5" fill="#FFFFFF"/>
  </g>

  <!-- Floating Glowing Hearts (♥) -->
  <g class="conn-heart-1" transform="translate(315, 80) scale(0.9)">
    <path d="M 10,3.5 C 10,2 8.5,0 6,0 C 3,0 1,2.5 1,5 C 1,8.5 7,13 10,15 C 13,13 19,8.5 19,5 C 19,2.5 17,0 14,0 C 11.5,0 10,2 10,3.5 Z" fill="#DC2626" opacity="0.85"/>
  </g>
  <g class="conn-heart-2" transform="translate(75, 140) scale(0.7)">
    <path d="M 10,3.5 C 10,2 8.5,0 6,0 C 3,0 1,2.5 1,5 C 1,8.5 7,13 10,15 C 13,13 19,8.5 19,5 C 19,2.5 17,0 14,0 C 11.5,0 10,2 10,3.5 Z" fill="#F05033" opacity="0.75"/>
  </g>

  <!-- Pointing Chevrons -->
  <g class="conn-arrow" transform="translate(325, 220)">
    <path d="M 0 0 L 8 8 L 0 16" fill="none" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 10 0 L 18 8 L 10 16" fill="none" stroke="#F05033" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 20 0 L 28 8 L 20 16" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>
  </g>

  <!-- ================= RIGHT: NEON SIGN & 5 SOCIAL CARDS ================= -->
  <g transform="translate(385, 24)">
    <!-- Neon Sign -->
    <g class="conn-neon">
      <rect x="0" y="0" width="220" height="36" rx="8" fill="#14141E" stroke="#DC2626" stroke-width="1.8" filter="url(#conn-neon-glow)"/>
      <rect x="0" y="0" width="220" height="36" rx="8" fill="#14141E" stroke="#FFFFFF" stroke-opacity="0.3" stroke-width="1"/>
      <circle cx="16" cy="18" r="4.5" fill="#DC2626"/>
      <text x="28" y="24" fill="url(#conn-neon-grad)" class="conn-font-display" font-size="19" font-weight="800" letter-spacing="3">NEET2516</text>
    </g>

    <g transform="translate(235, 6)">
      <text x="0" y="14" fill="#F05033" class="conn-font-mono" font-size="10.5" font-weight="700" letter-spacing="1.2">// INITIATE CONNECTION</text>
      <text x="0" y="26" fill="#A1A1AA" class="conn-font-mono" font-size="8.5">GITHUB · DEV.TO · LINKEDIN · EMAIL</text>
    </g>

    <!-- 5 Social Connection Cards -->
    <g transform="translate(0, 48)">
      <!-- 1. GitHub -->
      <a href="https://github.com/Neet2516" target="_blank">
        <g transform="translate(0, 0)">
          <rect width="520" height="44" rx="8" fill="#14141E" stroke="#1B1922" stroke-width="1"/>
          <rect x="1" y="1" width="518" height="42" rx="7" fill="none" stroke="#DC2626" stroke-opacity="0.2"/>
          <circle cx="24" cy="22" r="12" fill="#1B1922"/>
          <path d="M24 14 C19.6 14 16 17.6 16 22 C16 25.5 18.3 28.5 21.4 29.5 C21.8 29.6 22 29.4 22 29.1 C22 28.9 22 28 22 27 C19.8 27.5 19.3 26.1 19.3 26.1 C19 25.2 18.4 24.9 18.4 24.9 C17.7 24.4 18.5 24.4 18.5 24.4 C19.3 24.5 19.7 25.3 19.7 25.3 C20.4 26.5 21.5 26.2 22 25.9 C22.1 25.3 22.2 25 22.5 24.8 C20.7 24.6 18.9 23.9 18.9 20.8 C18.9 19.9 19.2 19.2 19.7 18.6 C19.6 18.4 19.4 17.6 19.8 16.6 C19.8 16.6 20.5 16.3 22 17.4 C22.6 17.2 23.3 17.1 24 17.1 C24.7 17.1 25.4 17.2 26 17.4 C27.5 16.3 28.2 16.6 28.2 16.6 C28.6 17.6 28.4 18.4 28.3 18.6 C28.8 19.2 29.1 19.9 29.1 20.8 C29.1 23.9 27.3 24.6 25.5 24.8 C25.8 25.1 26 25.7 26 26.6 C26 27.8 26 28.8 26 29.1 C26 29.4 26.2 29.6 26.6 29.5 C29.7 28.5 32 25.5 32 22 C32 17.6 28.4 14 24 14 Z" fill="#F05033"/>
          <text x="48" y="21" fill="#F8FAFC" class="conn-font-display" font-size="12" font-weight="700">GitHub</text>
          <text x="48" y="33" fill="#A1A1AA" class="conn-font-mono" font-size="9.5">https://github.com/Neet2516</text>
          <text x="445" y="26" fill="#F05033" class="conn-font-mono" font-size="10" font-weight="700">Follow ↗</text>
        </g>
      </a>

      <!-- 2. DEV Community -->
      <a href="https://dev.to/navneet_sinha" target="_blank">
        <g transform="translate(0, 50)">
          <rect width="520" height="44" rx="8" fill="#14141E" stroke="#1B1922" stroke-width="1"/>
          <rect x="1" y="1" width="518" height="42" rx="7" fill="none" stroke="#DC2626" stroke-opacity="0.2"/>
          <circle cx="24" cy="22" r="12" fill="#0D0E16"/>
          <text x="14" y="26" fill="#FFFFFF" class="conn-font-mono" font-size="9.5" font-weight="800">DEV</text>
          <text x="48" y="21" fill="#F8FAFC" class="conn-font-display" font-size="12" font-weight="700">DEV Community</text>
          <text x="48" y="33" fill="#A1A1AA" class="conn-font-mono" font-size="9.5">https://dev.to/navneet_sinha</text>
          <text x="445" y="26" fill="#DC2626" class="conn-font-mono" font-size="10" font-weight="700">Articles ↗</text>
        </g>
      </a>

      <!-- 3. LinkedIn -->
      <a href="https://www.linkedin.com/in/sinha-navneet/" target="_blank">
        <g transform="translate(0, 100)">
          <rect width="520" height="44" rx="8" fill="#14141E" stroke="#1B1922" stroke-width="1"/>
          <rect x="1" y="1" width="518" height="42" rx="7" fill="none" stroke="#DC2626" stroke-opacity="0.2"/>
          <circle cx="24" cy="22" r="12" fill="#1B1922"/>
          <rect x="18" y="18" width="2.5" height="8" fill="#0A66C2"/>
          <circle cx="19.2" cy="15.5" r="1.3" fill="#0A66C2"/>
          <path d="M 22.5 18 L 24.8 18 L 24.8 19.3 C 25.2 18.5 26.2 17.8 27.5 17.8 C 29.5 17.8 30 19.1 30 21.2 L 30 26 L 27.6 26 L 27.6 22.4 C 27.6 21.3 27.3 20.5 26.2 20.5 C 25.1 20.5 24.8 21.3 24.8 22.4 L 24.8 26 L 22.5 26 Z" fill="#0A66C2"/>
          <text x="48" y="21" fill="#F8FAFC" class="conn-font-display" font-size="12" font-weight="700">LinkedIn</text>
          <text x="48" y="33" fill="#A1A1AA" class="conn-font-mono" font-size="9.5">linkedin.com/in/sinha-navneet/</text>
          <text x="435" y="26" fill="#0A66C2" class="conn-font-mono" font-size="10" font-weight="700">Connect ↗</text>
        </g>
      </a>

      <!-- 4. Portfolio -->
      <a href="https://portfolio-1-tofl.onrender.com/" target="_blank">
        <g transform="translate(0, 150)">
          <rect width="520" height="44" rx="8" fill="#14141E" stroke="#1B1922" stroke-width="1"/>
          <rect x="1" y="1" width="518" height="42" rx="7" fill="none" stroke="#DC2626" stroke-opacity="0.2"/>
          <circle cx="24" cy="22" r="12" fill="#1B1922"/>
          <circle cx="24" cy="22" r="6" fill="none" stroke="#F05033" stroke-width="1"/>
          <ellipse cx="24" cy="22" rx="3" ry="6" fill="none" stroke="#F05033" stroke-width="0.8"/>
          <line x1="18" y1="22" x2="30" y2="22" stroke="#F05033" stroke-width="0.8"/>
          <text x="48" y="21" fill="#F8FAFC" class="conn-font-display" font-size="12" font-weight="700">Personal Portfolio</text>
          <text x="48" y="33" fill="#A1A1AA" class="conn-font-mono" font-size="9.5">portfolio-1-tofl.onrender.com</text>
          <text x="445" y="26" fill="#F05033" class="conn-font-mono" font-size="10" font-weight="700">Visit ↗</text>
        </g>
      </a>

      <!-- 5. Email -->
      <a href="mailto:getneet.25@gmail.com">
        <g transform="translate(0, 200)">
          <rect width="520" height="44" rx="8" fill="#14141E" stroke="#1B1922" stroke-width="1"/>
          <rect x="1" y="1" width="518" height="42" rx="7" fill="none" stroke="#DC2626" stroke-opacity="0.2"/>
          <circle cx="24" cy="22" r="12" fill="#1B1922"/>
          <rect x="17" y="17" width="14" height="10" rx="1.5" fill="none" stroke="#DC2626" stroke-width="1"/>
          <path d="M 17 18 L 24 23 L 31 18" fill="none" stroke="#DC2626" stroke-width="1"/>
          <text x="48" y="21" fill="#F8FAFC" class="conn-font-display" font-size="12" font-weight="700">Direct Email</text>
          <text x="48" y="33" fill="#A1A1AA" class="conn-font-mono" font-size="9.5">getneet.25@gmail.com</text>
          <text x="445" y="26" fill="#DC2626" class="conn-font-mono" font-size="10" font-weight="700">Write ↗</text>
        </g>
      </a>
    </g>

    <!-- Manifesto Footer -->
    <g transform="translate(0, 302)">
      <rect width="520" height="74" rx="10" fill="#1B1922" stroke="url(#conn-border-grad)" stroke-width="1.2"/>
      <text x="20" y="26" fill="url(#conn-manifesto-grad)" class="conn-font-display" font-size="14.5" font-weight="800" letter-spacing="1.5">BUILD. BREAK. LEARN. REPEAT.</text>
      <text x="20" y="46" fill="#A1A1AA" class="conn-font-display" font-size="10.5">
        Thanks for visiting my corner of the internet. Let's engineer something extraordinary together.
      </text>
      <circle cx="480" cy="37" r="16" fill="#14141E" stroke="#DC2626" stroke-width="1"/>
      <text x="480" y="42" text-anchor="middle" fill="#F05033" class="conn-font-mono" font-size="13" font-weight="700">∞</text>
    </g>
  </g>
</svg>"""

with open("svg/connect.svg", "w", encoding="utf-8") as f:
    f.write(build_connect())
ET.fromstring(build_connect())
print("✓ Valid XML & Saved svg/connect.svg")
