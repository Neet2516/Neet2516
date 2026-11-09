#!/usr/bin/env python3
import base64
import os
import xml.etree.ElementTree as ET

os.makedirs("svg", exist_ok=True)

# Load optimized images
with open("assets/character-portrait-opt.png", "rb") as f:
    PORTRAIT_B64 = base64.b64encode(f.read()).decode("utf-8")

with open("assets/character-pointing-sticker.png", "rb") as f:
    POINTING_B64 = base64.b64encode(f.read()).decode("utf-8")

print(f"Loaded assets: portrait {len(PORTRAIT_B64)} chars, pointing {len(POINTING_B64)} chars")

def validate_and_save(filename, svg_content):
    try:
        ET.fromstring(svg_content)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"✓ Valid XML & Saved: {filename} ({len(svg_content)} bytes)")
    except Exception as e:
        print(f"✗ XML Validation Error in {filename}: {e}")
        raise e

# -------------------------------------------------------------------
# 1. HERO.SVG
# -------------------------------------------------------------------
def generate_hero():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="hero-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="hero-glow-left" cx="20%" cy="30%" r="50%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="hero-glow-right" cx="80%" cy="50%" r="55%">
      <stop offset="0%" stop-color="#F05033" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="hero-text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="45%" stop-color="#F8FAFC"/>
      <stop offset="80%" stop-color="#F05033"/>
      <stop offset="100%" stop-color="#DC2626"/>
    </linearGradient>

    <linearGradient id="hero-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.65"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.5"/>
    </linearGradient>

    <pattern id="hero-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r="0.75" fill="#F05033" fill-opacity="0.12"/>
    </pattern>

    <clipPath id="hero-avatar-clip">
      <rect x="600" y="80" width="280" height="270" rx="14"/>
    </clipPath>

    <filter id="hero-neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .hero-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .hero-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes hero-pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.35; transform: scale(0.92); }}
    }}
    @keyframes hero-rec-blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0.15; }}
    }}
    @keyframes hero-scanline {{
      0% {{ transform: translateY(0); opacity: 0; }}
      10% {{ opacity: 0.85; }}
      90% {{ opacity: 0.85; }}
      100% {{ transform: translateY(260px); opacity: 0; }}
    }}
    @keyframes hero-role-cycle {{
      0%, 16% {{ opacity: 1; transform: translateY(0); }}
      20%, 36% {{ opacity: 0; transform: translateY(-8px); }}
      40%, 56% {{ opacity: 0; transform: translateY(-8px); }}
      60%, 76% {{ opacity: 0; transform: translateY(-8px); }}
      80%, 96% {{ opacity: 0; transform: translateY(-8px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes hero-role-2 {{
      0%, 16% {{ opacity: 0; transform: translateY(8px); }}
      20%, 36% {{ opacity: 1; transform: translateY(0); }}
      40%, 100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    @keyframes hero-role-3 {{
      0%, 36% {{ opacity: 0; transform: translateY(8px); }}
      40%, 56% {{ opacity: 1; transform: translateY(0); }}
      60%, 100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    @keyframes hero-role-4 {{
      0%, 56% {{ opacity: 0; transform: translateY(8px); }}
      60%, 76% {{ opacity: 1; transform: translateY(0); }}
      80%, 100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    @keyframes hero-role-5 {{
      0%, 76% {{ opacity: 0; transform: translateY(8px); }}
      80%, 96% {{ opacity: 1; transform: translateY(0); }}
      100% {{ opacity: 0; transform: translateY(-8px); }}
    }}
    @keyframes hero-float {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-4px); }}
    }}

    .hero-rec {{ animation: hero-rec-blink 1.4s infinite; }}
    .hero-beacon {{ animation: hero-pulse 2s infinite ease-in-out; transform-origin: 16px 14px; }}
    .hero-scan {{ animation: hero-scanline 3.5s infinite linear; }}
    .hero-hud-float {{ animation: hero-float 5s infinite ease-in-out; }}
    .role-1 {{ animation: hero-role-cycle 12s infinite; }}
    .role-2 {{ animation: hero-role-2 12s infinite; }}
    .role-3 {{ animation: hero-role-3 12s infinite; }}
    .role-4 {{ animation: hero-role-4 12s infinite; }}
    .role-5 {{ animation: hero-role-5 12s infinite; }}
  </style>

  <!-- Base background -->
  <rect width="940" height="480" rx="20" fill="url(#hero-bg-grad)"/>
  <rect width="940" height="480" rx="20" fill="url(#hero-glow-left)"/>
  <rect width="940" height="480" rx="20" fill="url(#hero-glow-right)"/>
  <rect width="940" height="480" rx="20" fill="url(#hero-grid)"/>

  <!-- Outer Glass Border -->
  <rect x="1" y="1" width="938" height="478" rx="19" fill="none" stroke="url(#hero-border-grad)" stroke-width="1.5"/>

  <!-- Left Column: Introduction & Metadata -->
  <g transform="translate(48, 46)">
    <!-- Collaboration Badge -->
    <rect x="0" y="0" width="248" height="28" rx="14" fill="#14141E" stroke="#DC2626" stroke-opacity="0.4" stroke-width="1"/>
    <circle class="hero-beacon" cx="16" cy="14" r="4.5" fill="#DC2626"/>
    <circle cx="16" cy="14" r="2" fill="#FFFFFF"/>
    <text x="28" y="18" fill="#F05033" class="hero-font-mono" font-size="10.5" font-weight="600" letter-spacing="1.2">OPEN TO COLLABORATION</text>

    <!-- Greeting -->
    <text x="0" y="62" fill="#A1A1AA" class="hero-font-display" font-size="16" font-weight="400" letter-spacing="0.5">Hi there, I'm</text>

    <!-- Large Name Typography -->
    <text x="0" y="108" fill="url(#hero-text-grad)" class="hero-font-display" font-size="44" font-weight="800" letter-spacing="-0.5">NAVNEET SINHA</text>

    <!-- Tagline -->
    <text x="0" y="136" fill="#F05033" class="hero-font-mono" font-size="12" font-weight="700" letter-spacing="2">// BUILDING BEYOND THE CODE.</text>

    <!-- Cycling Roles Container -->
    <g transform="translate(0, 172)">
      <rect x="0" y="-18" width="310" height="32" rx="6" fill="#1B1922" fill-opacity="0.8" stroke="#DC2626" stroke-opacity="0.25" stroke-width="1"/>
      <text x="12" y="3" fill="#DC2626" class="hero-font-mono" font-size="13" font-weight="700">&gt;</text>
      
      <!-- Role 1 (Fallback visible) -->
      <g class="role-1">
        <text x="28" y="3" fill="#F8FAFC" class="hero-font-mono" font-size="13" font-weight="600">Full Stack Developer</text>
      </g>
      <!-- Role 2 -->
      <g class="role-2">
        <text x="28" y="3" fill="#F8FAFC" class="hero-font-mono" font-size="13" font-weight="600">Software Engineer</text>
      </g>
      <!-- Role 3 -->
      <g class="role-3">
        <text x="28" y="3" fill="#F8FAFC" class="hero-font-mono" font-size="13" font-weight="600">Open Source Contributor</text>
      </g>
      <!-- Role 4 -->
      <g class="role-4">
        <text x="28" y="3" fill="#F8FAFC" class="hero-font-mono" font-size="13" font-weight="600">Backend Explorer</text>
      </g>
      <!-- Role 5 -->
      <g class="role-5">
        <text x="28" y="3" fill="#F8FAFC" class="hero-font-mono" font-size="13" font-weight="600">AI-Integrated Developer</text>
      </g>
    </g>

    <!-- Short Intro -->
    <text x="0" y="232" fill="#A1A1AA" class="hero-font-display" font-size="14.5">
      <tspan x="0" dy="0">Building scalable digital experiences, exploring systems engineering,</tspan>
      <tspan x="0" dy="22">and turning ideas into production-ready software.</tspan>
    </text>

    <!-- Telemetry Metadata Badges -->
    <g transform="translate(0, 290)">
      <!-- Location -->
      <g transform="translate(0, 0)">
        <rect width="138" height="26" rx="6" fill="#14141E" stroke="#991B1B" stroke-opacity="0.4" stroke-width="1"/>
        <path d="M12 7 C9.8 7 8 8.8 8 11 C8 14 12 18 12 18 C12 18 16 14 16 11 C16 8.8 14.2 7 12 7 Z M12 12.2 C11.3 12.2 10.8 11.7 10.8 11 C10.8 10.3 11.3 9.8 12 9.8 C12.7 9.8 13.2 10.3 13.2 11 C13.2 11.7 12.7 12.2 12 12.2 Z" fill="#F05033"/>
        <text x="22" y="17" fill="#F8FAFC" class="hero-font-mono" font-size="10.5">Ghaziabad, IN</text>
      </g>

      <!-- GitHub Handle -->
      <g transform="translate(148, 0)">
        <rect width="128" height="26" rx="6" fill="#14141E" stroke="#991B1B" stroke-opacity="0.4" stroke-width="1"/>
        <path d="M10 8 C7.8 8 6 9.8 6 12 C6 13.8 7.2 15.3 8.8 15.8 C9.1 15.9 9.2 15.7 9.2 15.5 C9.2 15.3 9.2 14.8 9.2 14.2 C8.1 14.4 7.8 13.7 7.8 13.7 C7.6 13.2 7.3 13.1 7.3 13.1 C6.9 12.8 7.3 12.8 7.3 12.8 C7.7 12.8 8 13.2 8 13.2 C8.4 13.8 9 13.6 9.2 13.5 C9.2 13.2 9.3 13 9.5 12.9 C8.6 12.8 7.7 12.5 7.7 11 C7.7 10.6 7.8 10.2 8.1 9.9 C8.1 9.8 7.9 9.4 8.1 8.9 C8.1 8.9 8.4 8.8 9.2 9.3 C9.5 9.2 9.8 9.2 10.1 9.2 C10.4 9.2 10.7 9.2 11 9.3 C11.8 8.8 12.1 8.9 12.1 8.9 C12.3 9.4 12.1 9.8 12.1 9.9 C12.4 10.2 12.5 10.6 12.5 11 C12.5 12.5 11.6 12.8 10.7 12.9 C10.9 13.1 11 13.4 11 13.8 C11 14.4 11 15.3 11 15.5 C11 15.7 11.1 15.9 11.4 15.8 C13 15.3 14.2 13.8 14.2 12 C14.2 9.8 12.4 8 10 8 Z" fill="#F05033"/>
        <text x="22" y="17" fill="#F8FAFC" class="hero-font-mono" font-size="10.5">@Neet2516</text>
      </g>

      <!-- Architecture pill -->
      <g transform="translate(286, 0)">
        <rect width="194" height="26" rx="6" fill="#14141E" stroke="#991B1B" stroke-opacity="0.4" stroke-width="1"/>
        <circle cx="10" cy="13" r="3" fill="#DC2626"/>
        <text x="18" y="17" fill="#F8FAFC" class="hero-font-mono" font-size="10.5">Rust · Systems · AI</text>
      </g>
    </g>

    <!-- Activity Line -->
    <g transform="translate(0, 335)">
      <line x1="0" y1="0" x2="480" y2="0" stroke="#1B1922" stroke-width="1"/>
      <line x1="0" y1="0" x2="160" y2="0" stroke="#DC2626" stroke-width="1.5"/>
      <text x="0" y="24" fill="#A1A1AA" class="hero-font-mono" font-size="10">SYS_STATUS: ONLINE</text>
      <text x="160" y="24" fill="#A1A1AA" class="hero-font-mono" font-size="10">NODE: GHAZIABAD.IN</text>
      <text x="340" y="24" fill="#DC2626" class="hero-font-mono" font-size="10" font-weight="600">UPTIME: 99.98%</text>
    </g>
  </g>

  <!-- Right Column: Futuristic Camera Viewfinder HUD -->
  <g class="hero-hud-float">
    <!-- Outer Viewfinder Frame -->
    <rect x="580" y="38" width="320" height="394" rx="16" fill="#14141E" fill-opacity="0.9" stroke="url(#hero-border-grad)" stroke-width="1.5"/>

    <!-- HUD Top Bar -->
    <g transform="translate(600, 58)">
      <!-- REC indicator -->
      <circle class="hero-rec" cx="6" cy="6" r="5" fill="#DC2626"/>
      <text class="hero-rec hero-font-mono" x="16" y="10" fill="#DC2626" font-size="11" font-weight="700" letter-spacing="1">REC</text>

      <!-- Camera Title -->
      <text x="95" y="10" fill="#A1A1AA" class="hero-font-mono" font-size="10.5">CAM_01 // ACTIVE</text>

      <!-- Frame rate -->
      <text x="240" y="10" fill="#F05033" class="hero-font-mono" font-size="10.5" font-weight="600">60 FPS</text>
    </g>

    <!-- Viewfinder Inner Window with Portrait -->
    <g>
      <!-- Base photo clipped -->
      <image href="data:image/png;base64,{PORTRAIT_B64}" x="600" y="80" width="280" height="270" preserveAspectRatio="xMidYMid slice" clip-path="url(#hero-avatar-clip)"/>

      <!-- Viewfinder Overlay Elements -->
      <!-- Scanning Laser Line -->
      <g clip-path="url(#hero-avatar-clip)">
        <g class="hero-scan">
          <line x1="600" y1="85" x2="880" y2="85" stroke="#DC2626" stroke-width="2.5" filter="url(#hero-neon-glow)"/>
          <line x1="600" y1="84" x2="880" y2="84" stroke="#FFFFFF" stroke-width="1" opacity="0.6"/>
        </g>
      </g>

      <!-- Viewfinder Reticles (Corners) -->
      <!-- Top Left -->
      <path d="M 608 100 L 608 90 L 618 90" fill="none" stroke="#DC2626" stroke-width="2.5"/>
      <!-- Top Right -->
      <path d="M 862 90 L 872 90 L 872 100" fill="none" stroke="#DC2626" stroke-width="2.5"/>
      <!-- Bottom Left -->
      <path d="M 608 335 L 608 345 L 618 345" fill="none" stroke="#DC2626" stroke-width="2.5"/>
      <!-- Bottom Right -->
      <path d="M 862 345 L 872 345 L 872 335" fill="none" stroke="#DC2626" stroke-width="2.5"/>

      <!-- Center Crosshair Target -->
      <g opacity="0.5">
        <line x1="730" y1="215" x2="750" y2="215" stroke="#DC2626" stroke-width="1"/>
        <line x1="740" y1="205" x2="740" y2="225" stroke="#DC2626" stroke-width="1"/>
        <circle cx="740" cy="215" r="12" fill="none" stroke="#DC2626" stroke-width="0.8" stroke-dasharray="2,2"/>
      </g>

      <!-- Sub-frame Border -->
      <rect x="600" y="80" width="280" height="270" rx="14" fill="none" stroke="#DC2626" stroke-opacity="0.3" stroke-width="1"/>
    </g>

    <!-- Telemetry Readout Bottom Bar -->
    <g transform="translate(600, 370)">
      <rect x="0" y="0" width="280" height="48" rx="8" fill="#0D0E16" stroke="#1B1922" stroke-width="1"/>
      <text x="12" y="18" fill="#F8FAFC" class="hero-font-mono" font-size="10.5" font-weight="700">SYS.VER: 2.5.16</text>
      <text x="180" y="18" fill="#F05033" class="hero-font-mono" font-size="10">AUTH: VERIFIED</text>
      <text x="12" y="36" fill="#A1A1AA" class="hero-font-mono" font-size="9.5">LAT: 28.67° N  LON: 77.45° E</text>
      <text x="180" y="36" fill="#A1A1AA" class="hero-font-mono" font-size="9.5">BAT: 99.4% [■■■]</text>
    </g>
  </g>
</svg>"""

validate_and_save("svg/hero.svg", generate_hero())

# -------------------------------------------------------------------
# 2. ABOUT-LIFE.SVG
# -------------------------------------------------------------------
def generate_about():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="about-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="about-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="about-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.3"/>
    </linearGradient>

    <linearGradient id="about-ring-grad-1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F05033"/>
      <stop offset="100%" stop-color="#DC2626"/>
    </linearGradient>

    <linearGradient id="about-ring-grad-2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#991B1B"/>
    </linearGradient>

    <linearGradient id="about-ring-grad-3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991B1B"/>
      <stop offset="100%" stop-color="#450A0A"/>
    </linearGradient>

    <pattern id="about-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="0.7" fill="#F05033" fill-opacity="0.1"/>
    </pattern>
  </defs>

  <style>
    .about-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .about-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes about-cursor-blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    @keyframes about-progress-glow {{
      0%, 100% {{ opacity: 0.8; }}
      50% {{ opacity: 1; }}
    }}
    @keyframes about-ring-rotate {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}

    .about-cursor {{ animation: about-cursor-blink 1s infinite; }}
    .about-progress {{ animation: about-progress-glow 2.5s infinite ease-in-out; }}
  </style>

  <!-- Background -->
  <rect width="940" height="480" rx="20" fill="url(#about-bg-grad)"/>
  <rect width="940" height="480" rx="20" fill="url(#about-glow)"/>
  <rect width="940" height="480" rx="20" fill="url(#about-dots)"/>
  <rect x="1" y="1" width="938" height="478" rx="19" fill="none" stroke="url(#about-card-border)" stroke-width="1.5"/>

  <!-- ================= CARD 1: WHAT I BUILD (LEFT) ================= -->
  <g transform="translate(30, 24)">
    <!-- Glass Card Base -->
    <rect width="425" height="432" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#about-card-border)" stroke-width="1.2"/>

    <!-- Terminal Header -->
    <rect width="425" height="38" rx="16" fill="#1B1922"/>
    <rect y="26" width="425" height="12" fill="#1B1922"/>
    
    <!-- Window Control Dots -->
    <circle cx="24" cy="19" r="5" fill="#F05033"/>
    <circle cx="40" cy="19" r="5" fill="#991B1B"/>
    <circle cx="56" cy="19" r="5" fill="#450A0A"/>

    <!-- Terminal Title -->
    <text x="80" y="23" fill="#A1A1AA" class="about-font-mono" font-size="11">neet@kernel:~/manifesto.sh</text>

    <!-- Shell Prompt -->
    <g transform="translate(24, 60)">
      <text x="0" y="0" fill="#DC2626" class="about-font-mono" font-size="12" font-weight="700">$</text>
      <text x="14" y="0" fill="#F8FAFC" class="about-font-mono" font-size="12">./display_core_focus.sh</text>
      <rect class="about-cursor" x="180" y="-10" width="7" height="13" fill="#F05033"/>
    </g>

    <!-- Card Title -->
    <text x="24" y="98" fill="#F8FAFC" class="about-font-display" font-size="18" font-weight="700" letter-spacing="-0.3">WHAT I BUILD</text>
    <line x1="24" y1="108" x2="400" y2="108" stroke="#1B1922" stroke-width="1"/>
    <line x1="24" y1="108" x2="120" y2="108" stroke="#DC2626" stroke-width="1.5"/>

    <!-- Section 1: Full Stack Development -->
    <g transform="translate(24, 126)">
      <rect width="377" height="74" rx="8" fill="#1B1922" fill-opacity="0.6" stroke="#DC2626" stroke-opacity="0.2" stroke-width="1"/>
      <circle cx="20" cy="22" r="7" fill="#DC2626" fill-opacity="0.2"/>
      <circle cx="20" cy="22" r="3.5" fill="#F05033"/>
      <text x="36" y="26" fill="#F8FAFC" class="about-font-display" font-size="13.5" font-weight="700">Full Stack Development</text>
      <text x="36" y="44" fill="#A1A1AA" class="about-font-display" font-size="11.5">
        <tspan x="36" dy="0">Modern web applications using React, Next.js, TypeScript,</tspan>
        <tspan x="36" dy="16">and Node.js. Fluid interfaces backed by robust architectures.</tspan>
      </text>
    </g>

    <!-- Section 2: Backend & Systems -->
    <g transform="translate(24, 212)">
      <rect width="377" height="74" rx="8" fill="#1B1922" fill-opacity="0.6" stroke="#DC2626" stroke-opacity="0.2" stroke-width="1"/>
      <circle cx="20" cy="22" r="7" fill="#DC2626" fill-opacity="0.2"/>
      <circle cx="20" cy="22" r="3.5" fill="#F05033"/>
      <text x="36" y="26" fill="#F8FAFC" class="about-font-display" font-size="13.5" font-weight="700">Backend &amp; Systems Engineering</text>
      <text x="36" y="44" fill="#A1A1AA" class="about-font-display" font-size="11.5">
        <tspan x="36" dy="0">Exploring Rust, APIs, databases, distributed systems,</tspan>
        <tspan x="36" dy="16">and scalable architectures with Axum, Tokio, and Redis.</tspan>
      </text>
    </g>

    <!-- Section 3: AI & Automation -->
    <g transform="translate(24, 298)">
      <rect width="377" height="74" rx="8" fill="#1B1922" fill-opacity="0.6" stroke="#DC2626" stroke-opacity="0.2" stroke-width="1"/>
      <circle cx="20" cy="22" r="7" fill="#DC2626" fill-opacity="0.2"/>
      <circle cx="20" cy="22" r="3.5" fill="#F05033"/>
      <text x="36" y="26" fill="#F8FAFC" class="about-font-display" font-size="13.5" font-weight="700">AI &amp; Workflow Automation</text>
      <text x="36" y="44" fill="#A1A1AA" class="about-font-display" font-size="11.5">
        <tspan x="36" dy="0">Building intelligent pipelines, autonomous AI agents,</tspan>
        <tspan x="36" dy="16">N8N orchestrations, and LLM-assisted developer tooling.</tspan>
      </text>
    </g>

    <!-- Architecture Badges -->
    <g transform="translate(24, 390)">
      <rect width="112" height="22" rx="4" fill="#0D0E16" stroke="#991B1B" stroke-width="0.8"/>
      <text x="10" y="15" fill="#F05033" class="about-font-mono" font-size="9" font-weight="600">[ CRDT-ENABLED ]</text>

      <rect x="120" width="124" height="22" rx="4" fill="#0D0E16" stroke="#991B1B" stroke-width="0.8"/>
      <text x="130" y="15" fill="#F05033" class="about-font-mono" font-size="9" font-weight="600">[ ASYNC-STREAMING ]</text>

      <rect x="252" width="124" height="22" rx="4" fill="#0D0E16" stroke="#991B1B" stroke-width="0.8"/>
      <text x="262" y="15" fill="#F05033" class="about-font-mono" font-size="9" font-weight="600">[ ZERO-LATENCY ]</text>
    </g>
  </g>

  <!-- ================= CARD 2: BEYOND CODE (RIGHT) ================= -->
  <g transform="translate(485, 24)">
    <!-- Glass Card Base -->
    <rect width="425" height="432" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#about-card-border)" stroke-width="1.2"/>

    <!-- Story Progress Bars (Instagram Style) -->
    <g transform="translate(24, 16)" class="about-progress">
      <rect x="0" y="0" width="58" height="3" rx="1.5" fill="#F05033"/>
      <rect x="63" y="0" width="58" height="3" rx="1.5" fill="#DC2626"/>
      <rect x="126" y="0" width="58" height="3" rx="1.5" fill="#DC2626"/>
      <rect x="189" y="0" width="58" height="3" rx="1.5" fill="#991B1B"/>
      <rect x="252" y="0" width="58" height="3" rx="1.5" fill="#991B1B"/>
      <rect x="315" y="0" width="62" height="3" rx="1.5" fill="#450A0A"/>
    </g>

    <!-- Header -->
    <g transform="translate(24, 40)">
      <text x="0" y="0" fill="#F05033" class="about-font-mono" font-size="10.5" font-weight="700" letter-spacing="1.5">ENGINEER DISPATCH // STORY MODE</text>
      <text x="0" y="24" fill="#F8FAFC" class="about-font-display" font-size="18" font-weight="700" letter-spacing="-0.3">BEYOND THE TERMINAL</text>
    </g>
    <line x1="24" y1="78" x2="400" y2="78" stroke="#1B1922" stroke-width="1"/>
    <line x1="24" y1="78" x2="140" y2="78" stroke="#DC2626" stroke-width="1.5"/>

    <!-- 6 Curated Highlights -->
    <g transform="translate(24, 94)">
      <!-- Item 1 -->
      <g transform="translate(0, 0)">
        <circle cx="6" cy="7" r="3" fill="#DC2626"/>
        <text x="18" y="10" fill="#F8FAFC" class="about-font-display" font-size="12" font-weight="600">Open-source contributions</text>
        <text x="18" y="24" fill="#A1A1AA" class="about-font-display" font-size="10.5">Contributing to developer tooling and community ecosystems.</text>
      </g>
      <!-- Item 2 -->
      <g transform="translate(0, 38)">
        <circle cx="6" cy="7" r="3" fill="#DC2626"/>
        <text x="18" y="10" fill="#F8FAFC" class="about-font-display" font-size="12" font-weight="600">Hackathons &amp; High-Pressure Sprints</text>
        <text x="18" y="24" fill="#A1A1AA" class="about-font-display" font-size="10.5">Building rapid prototypes, competing, and validating architectures.</text>
      </g>
      <!-- Item 3 -->
      <g transform="translate(0, 76)">
        <circle cx="6" cy="7" r="3" fill="#DC2626"/>
        <text x="18" y="10" fill="#F8FAFC" class="about-font-display" font-size="12" font-weight="600">Exploring New Technologies</text>
        <text x="18" y="24" fill="#A1A1AA" class="about-font-display" font-size="10.5">Deep diving into Rust, Axum, Tokio, and emerging distributed primitives.</text>
      </g>
      <!-- Item 4 -->
      <g transform="translate(0, 114)">
        <circle cx="6" cy="7" r="3" fill="#DC2626"/>
        <text x="18" y="10" fill="#F8FAFC" class="about-font-display" font-size="12" font-weight="600">Building Real-World Side Projects</text>
        <text x="18" y="24" fill="#A1A1AA" class="about-font-display" font-size="10.5">Turning developer bottlenecks into clean open-source software.</text>
      </g>
      <!-- Item 5 -->
      <g transform="translate(0, 152)">
        <circle cx="6" cy="7" r="3" fill="#DC2626"/>
        <text x="18" y="10" fill="#F8FAFC" class="about-font-display" font-size="12" font-weight="600">Learning System Design</text>
        <text x="18" y="24" fill="#A1A1AA" class="about-font-display" font-size="10.5">Studying fault tolerance, CRDTs, consensus, and horizontal scaling.</text>
      </g>
      <!-- Item 6 -->
      <g transform="translate(0, 190)">
        <circle cx="6" cy="7" r="3" fill="#DC2626"/>
        <text x="18" y="10" fill="#F8FAFC" class="about-font-display" font-size="12" font-weight="600">Linux &amp; Developer Tooling</text>
        <text x="18" y="24" fill="#A1A1AA" class="about-font-display" font-size="10.5">Custom CLI environments, shell scripting, automation, and dotfiles.</text>
      </g>
    </g>

    <!-- Activity Rings Section -->
    <g transform="translate(24, 326)">
      <rect width="377" height="92" rx="10" fill="#0D0E16" stroke="#1B1922" stroke-width="1"/>
      
      <!-- Concentric Activity Rings -->
      <g transform="translate(56, 46)">
        <!-- Outer Track & Ring (Code & Systems - 94%) -->
        <circle cx="0" cy="0" r="36" fill="none" stroke="#1B1922" stroke-width="5"/>
        <circle cx="0" cy="0" r="36" fill="none" stroke="url(#about-ring-grad-1)" stroke-width="5" stroke-dasharray="226" stroke-dashoffset="14" stroke-linecap="round"/>
        
        <!-- Mid Track & Ring (Open Source - 88%) -->
        <circle cx="0" cy="0" r="27" fill="none" stroke="#1B1922" stroke-width="5"/>
        <circle cx="0" cy="0" r="27" fill="none" stroke="url(#about-ring-grad-2)" stroke-width="5" stroke-dasharray="170" stroke-dashoffset="20" stroke-linecap="round"/>

        <!-- Inner Track & Ring (Architecture - 82%) -->
        <circle cx="0" cy="0" r="18" fill="none" stroke="#1B1922" stroke-width="5"/>
        <circle cx="0" cy="0" r="18" fill="none" stroke="url(#about-ring-grad-3)" stroke-width="5" stroke-dasharray="113" stroke-dashoffset="20" stroke-linecap="round"/>
      </g>

      <!-- Rings Legend -->
      <g transform="translate(120, 22)">
        <circle cx="6" cy="6" r="4" fill="#F05033"/>
        <text x="16" y="9" fill="#F8FAFC" class="about-font-mono" font-size="9.5" font-weight="600">SYSTEMS &amp; CORE CODE</text>
        <text x="195" y="9" fill="#F05033" class="about-font-mono" font-size="9.5" font-weight="700">94%</text>

        <circle cx="6" cy="24" r="4" fill="#DC2626"/>
        <text x="16" y="27" fill="#F8FAFC" class="about-font-mono" font-size="9.5" font-weight="600">OPEN SOURCE &amp; LABS</text>
        <text x="195" y="27" fill="#DC2626" class="about-font-mono" font-size="9.5" font-weight="700">88%</text>

        <circle cx="6" cy="42" r="4" fill="#991B1B"/>
        <text x="16" y="45" fill="#F8FAFC" class="about-font-mono" font-size="9.5" font-weight="600">RESEARCH &amp; DESIGN</text>
        <text x="195" y="45" fill="#991B1B" class="about-font-mono" font-size="9.5" font-weight="700">82%</text>
      </g>
    </g>
  </g>
</svg>"""

validate_and_save("svg/about-life.svg", generate_about())

# -------------------------------------------------------------------
# 3. STACK.SVG (ORBITAL TECH UNIVERSE)
# -------------------------------------------------------------------
def generate_stack():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 560" width="100%" height="100%">
  <defs>
    <linearGradient id="stack-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="stack-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.35"/>
      <stop offset="40%" stop-color="#991B1B" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="stack-center-core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#DC2626"/>
      <stop offset="60%" stop-color="#991B1B"/>
      <stop offset="100%" stop-color="#450A0A"/>
    </radialGradient>

    <linearGradient id="stack-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.3"/>
    </linearGradient>

    <pattern id="stack-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r="0.75" fill="#F05033" fill-opacity="0.12"/>
    </pattern>

    <filter id="stack-node-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <style>
    .stack-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .stack-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes stack-spin-cw {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    @keyframes stack-spin-ccw {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(-360deg); }}
    }}
    @keyframes stack-core-pulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.9; }}
      50% {{ transform: scale(1.06); opacity: 1; }}
    }}
    @keyframes stack-orbit-glow {{
      0%, 100% {{ opacity: 0.35; }}
      50% {{ opacity: 0.65; }}
    }}

    .stack-core {{ animation: stack-core-pulse 3s infinite ease-in-out; transform-origin: 470px 245px; }}
    .stack-corona {{ animation: stack-spin-cw 24s infinite linear; transform-origin: 470px 245px; }}
    .stack-orbit-line {{ animation: stack-orbit-glow 4s infinite ease-in-out; }}
  </style>

  <!-- Background -->
  <rect width="940" height="560" rx="20" fill="url(#stack-bg-grad)"/>
  <circle cx="470" cy="245" r="280" fill="url(#stack-core-glow)"/>
  <rect width="940" height="560" rx="20" fill="url(#stack-dots)"/>
  <rect x="1" y="1" width="938" height="558" rx="19" fill="none" stroke="url(#stack-border-grad)" stroke-width="1.5"/>

  <!-- Top Header -->
  <g transform="translate(48, 36)">
    <rect x="0" y="0" width="168" height="24" rx="6" fill="#14141E" stroke="#DC2626" stroke-opacity="0.3" stroke-width="1"/>
    <circle cx="12" cy="12" r="3.5" fill="#DC2626"/>
    <text x="24" y="15.5" fill="#F05033" class="stack-font-mono" font-size="9.5" font-weight="700" letter-spacing="1">ORBITAL ARCHITECTURE</text>

    <text x="0" y="46" fill="#F8FAFC" class="stack-font-display" font-size="20" font-weight="800" letter-spacing="-0.4">NEET2516 TECH UNIVERSE</text>
    <text x="280" y="46" fill="#A1A1AA" class="stack-font-mono" font-size="11.5">// 3 CONCENTRIC RUNTIME TIERS</text>
  </g>

  <!-- ================= ORBIT SYSTEM ================= -->
  <!-- Orbit 3 (Outer) -->
  <ellipse class="stack-orbit-line" cx="470" cy="245" rx="390" ry="175" fill="none" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="6,8"/>

  <!-- Orbit 2 (Middle) -->
  <ellipse class="stack-orbit-line" cx="470" cy="245" rx="285" ry="128" fill="none" stroke="#DC2626" stroke-width="1.4" stroke-dasharray="5,6"/>

  <!-- Orbit 1 (Inner) -->
  <ellipse class="stack-orbit-line" cx="470" cy="245" rx="180" ry="80" fill="none" stroke="#F05033" stroke-width="1.6" stroke-dasharray="4,4"/>

  <!-- Rotating Dashed Corona around core -->
  <circle class="stack-corona" cx="470" cy="245" r="74" fill="none" stroke="#F05033" stroke-width="1.2" stroke-dasharray="4,10" opacity="0.6"/>
  <circle cx="470" cy="245" r="64" fill="none" stroke="#DC2626" stroke-width="1" stroke-opacity="0.4"/>

  <!-- Central Core Reactor -->
  <g class="stack-core">
    <circle cx="470" cy="245" r="54" fill="url(#stack-center-core)" stroke="#F8FAFC" stroke-opacity="0.2" stroke-width="1.5"/>
    <circle cx="470" cy="245" r="48" fill="#14141E" fill-opacity="0.7"/>
    <text x="470" y="240" text-anchor="middle" fill="#FFFFFF" class="stack-font-display" font-size="13" font-weight="800" letter-spacing="1">NEET2516</text>
    <text x="470" y="255" text-anchor="middle" fill="#F05033" class="stack-font-mono" font-size="8.5" font-weight="700" letter-spacing="1.5">CORE RUNTIME</text>
  </g>

  <!-- ================= ORBIT 1 NODES (Core Languages & Frontend) ================= -->
  <!-- Node: Rust (Left) -->
  <g transform="translate(290, 245)" filter="url(#stack-node-shadow)">
    <rect x="-42" y="-14" width="84" height="28" rx="14" fill="#1B1922" stroke="#F05033" stroke-width="1.5"/>
    <circle cx="-26" cy="0" r="4" fill="#F05033"/>
    <text x="-16" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="11" font-weight="700">Rust</text>
  </g>

  <!-- Node: TypeScript (Top Left) -->
  <g transform="translate(370, 175)" filter="url(#stack-node-shadow)">
    <rect x="-50" y="-14" width="100" height="28" rx="14" fill="#1B1922" stroke="#3178C6" stroke-width="1.5"/>
    <rect x="-38" y="-7" width="14" height="14" rx="2" fill="#3178C6"/>
    <text x="-34" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="9" font-weight="800">TS</text>
    <text x="-18" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="10.5" font-weight="700">TypeScript</text>
  </g>

  <!-- Node: Node.js (Top Right) -->
  <g transform="translate(570, 175)" filter="url(#stack-node-shadow)">
    <rect x="-44" y="-14" width="88" height="28" rx="14" fill="#1B1922" stroke="#339933" stroke-width="1.5"/>
    <circle cx="-28" cy="0" r="4" fill="#339933"/>
    <text x="-18" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="11" font-weight="700">Node.js</text>
  </g>

  <!-- Node: React (Right) -->
  <g transform="translate(650, 245)" filter="url(#stack-node-shadow)">
    <rect x="-42" y="-14" width="84" height="28" rx="14" fill="#1B1922" stroke="#61DAFB" stroke-width="1.5"/>
    <circle cx="-26" cy="0" r="4" fill="#61DAFB"/>
    <text x="-16" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="11" font-weight="700">React</text>
  </g>

  <!-- Node: Next.js (Bottom Center) -->
  <g transform="translate(470, 325)" filter="url(#stack-node-shadow)">
    <rect x="-44" y="-14" width="88" height="28" rx="14" fill="#1B1922" stroke="#FFFFFF" stroke-width="1.2"/>
    <circle cx="-28" cy="0" r="4" fill="#FFFFFF"/>
    <text x="-18" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="11" font-weight="700">Next.js</text>
  </g>

  <!-- ================= ORBIT 2 NODES (Backend, APIs, Data) ================= -->
  <!-- Node: Axum (Far Left Mid) -->
  <g transform="translate(185, 245)" filter="url(#stack-node-shadow)">
    <rect x="-38" y="-13" width="76" height="26" rx="13" fill="#14141E" stroke="#DC2626" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#F8FAFC" class="stack-font-mono" font-size="10.5" font-weight="700">Axum</text>
  </g>

  <!-- Node: PostgreSQL (Upper Left) -->
  <g transform="translate(285, 130)" filter="url(#stack-node-shadow)">
    <rect x="-52" y="-13" width="104" height="26" rx="13" fill="#14141E" stroke="#4169E1" stroke-width="1.2"/>
    <circle cx="-38" cy="0" r="3.5" fill="#4169E1"/>
    <text x="-28" y="4" fill="#F8FAFC" class="stack-font-mono" font-size="10" font-weight="600">PostgreSQL</text>
  </g>

  <!-- Node: Redis (Upper Right) -->
  <g transform="translate(655, 130)" filter="url(#stack-node-shadow)">
    <rect x="-40" y="-13" width="80" height="26" rx="13" fill="#14141E" stroke="#DC382D" stroke-width="1.2"/>
    <circle cx="-26" cy="0" r="3.5" fill="#DC382D"/>
    <text x="-16" y="4" fill="#F8FAFC" class="stack-font-mono" font-size="10" font-weight="600">Redis</text>
  </g>

  <!-- Node: Docker (Far Right Mid) -->
  <g transform="translate(755, 245)" filter="url(#stack-node-shadow)">
    <rect x="-40" y="-13" width="80" height="26" rx="13" fill="#14141E" stroke="#2496ED" stroke-width="1.2"/>
    <circle cx="-26" cy="0" r="3.5" fill="#2496ED"/>
    <text x="-16" y="4" fill="#F8FAFC" class="stack-font-mono" font-size="10" font-weight="600">Docker</text>
  </g>

  <!-- Node: WebSockets (Lower Right) -->
  <g transform="translate(660, 360)" filter="url(#stack-node-shadow)">
    <rect x="-54" y="-13" width="108" height="26" rx="13" fill="#14141E" stroke="#F05033" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#F8FAFC" class="stack-font-mono" font-size="10" font-weight="600">WebSockets</text>
  </g>

  <!-- Node: MongoDB (Lower Left) -->
  <g transform="translate(280, 360)" filter="url(#stack-node-shadow)">
    <rect x="-48" y="-13" width="96" height="26" rx="13" fill="#14141E" stroke="#47A248" stroke-width="1.2"/>
    <circle cx="-34" cy="0" r="3.5" fill="#47A248"/>
    <text x="-24" y="4" fill="#F8FAFC" class="stack-font-mono" font-size="10" font-weight="600">MongoDB</text>
  </g>

  <!-- ================= ORBIT 3 NODES (Cloud, AI, DevOps) ================= -->
  <!-- Node: Tokio (Outer Top Left) -->
  <g transform="translate(190, 105)" filter="url(#stack-node-shadow)">
    <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#0D0E16" stroke="#DC2626" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#A1A1AA" class="stack-font-mono" font-size="9.5">Tokio</text>
  </g>

  <!-- Node: AI Agents (Outer Top Center) -->
  <g transform="translate(470, 70)" filter="url(#stack-node-shadow)">
    <rect x="-52" y="-13" width="104" height="26" rx="13" fill="#1B1922" stroke="#DC2626" stroke-width="1.4"/>
    <circle cx="-38" cy="0" r="3" fill="#DC2626"/>
    <text x="-28" y="4" fill="#FFFFFF" class="stack-font-mono" font-size="10" font-weight="700">AI Agents</text>
  </g>

  <!-- Node: AWS (Outer Top Right) -->
  <g transform="translate(750, 105)" filter="url(#stack-node-shadow)">
    <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#0D0E16" stroke="#FF9900" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#FF9900" class="stack-font-mono" font-size="9.5" font-weight="700">AWS</text>
  </g>

  <!-- Node: N8N (Outer Right) -->
  <g transform="translate(860, 245)" filter="url(#stack-node-shadow)">
    <rect x="-34" y="-12" width="68" height="24" rx="12" fill="#0D0E16" stroke="#EA4B71" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#EA4B71" class="stack-font-mono" font-size="9.5" font-weight="700">N8N</text>
  </g>

  <!-- Node: GitHub Actions (Outer Bottom Right) -->
  <g transform="translate(760, 390)" filter="url(#stack-node-shadow)">
    <rect x="-60" y="-12" width="120" height="24" rx="12" fill="#0D0E16" stroke="#2088FF" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#F8FAFC" class="stack-font-mono" font-size="9.5">CI/CD Actions</text>
  </g>

  <!-- Node: Linux (Outer Bottom Left) -->
  <g transform="translate(180, 390)" filter="url(#stack-node-shadow)">
    <rect x="-35" y="-12" width="70" height="24" rx="12" fill="#0D0E16" stroke="#FCC624" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#FCC624" class="stack-font-mono" font-size="9.5" font-weight="700">Linux</text>
  </g>

  <!-- Node: Express.js (Outer Left) -->
  <g transform="translate(80, 245)" filter="url(#stack-node-shadow)">
    <rect x="-42" y="-12" width="84" height="24" rx="12" fill="#0D0E16" stroke="#991B1B" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#A1A1AA" class="stack-font-mono" font-size="9.5">Express.js</text>
  </g>

  <!-- ================= BOTTOM ORGANIZED DOMAIN CHIPS ================= -->
  <g transform="translate(30, 440)">
    <!-- Card Base -->
    <rect width="880" height="95" rx="12" fill="#14141E" stroke="#1B1922" stroke-width="1"/>

    <!-- Column 1: Frontend -->
    <g transform="translate(20, 16)">
      <text x="0" y="0" fill="#F05033" class="stack-font-mono" font-size="9.5" font-weight="700">01 // FRONTEND</text>
      <text x="0" y="18" fill="#F8FAFC" class="stack-font-display" font-size="11" font-weight="600">React · Next.js · TS</text>
      <text x="0" y="34" fill="#A1A1AA" class="stack-font-display" font-size="10">Tailwind · GSAP · Three.js</text>
      <text x="0" y="48" fill="#A1A1AA" class="stack-font-display" font-size="10">Shadcn UI · Framer</text>
    </g>

    <line x1="185" y1="14" x2="185" y2="80" stroke="#1B1922" stroke-width="1"/>

    <!-- Column 2: Backend & Systems -->
    <g transform="translate(205, 16)">
      <text x="0" y="0" fill="#F05033" class="stack-font-mono" font-size="9.5" font-weight="700">02 // BACKEND</text>
      <text x="0" y="18" fill="#F8FAFC" class="stack-font-display" font-size="11" font-weight="600">Rust · Axum · Tokio</text>
      <text x="0" y="34" fill="#A1A1AA" class="stack-font-display" font-size="10">Node.js · Express.js</text>
      <text x="0" y="48" fill="#A1A1AA" class="stack-font-display" font-size="10">WebSockets · WebRTC</text>
    </g>

    <line x1="375" y1="14" x2="375" y2="80" stroke="#1B1922" stroke-width="1"/>

    <!-- Column 3: Database & Caching -->
    <g transform="translate(395, 16)">
      <text x="0" y="0" fill="#F05033" class="stack-font-mono" font-size="9.5" font-weight="700">03 // DATA &amp; STORAGE</text>
      <text x="0" y="18" fill="#F8FAFC" class="stack-font-display" font-size="11" font-weight="600">PostgreSQL · Redis</text>
      <text x="0" y="34" fill="#A1A1AA" class="stack-font-display" font-size="10">MongoDB · MySQL</text>
      <text x="0" y="48" fill="#A1A1AA" class="stack-font-display" font-size="10">LevelDB · BullMQ</text>
    </g>

    <line x1="565" y1="14" x2="565" y2="80" stroke="#1B1922" stroke-width="1"/>

    <!-- Column 4: DevOps & Cloud -->
    <g transform="translate(585, 16)">
      <text x="0" y="0" fill="#F05033" class="stack-font-mono" font-size="9.5" font-weight="700">04 // DEVOPS &amp; CLOUD</text>
      <text x="0" y="18" fill="#F8FAFC" class="stack-font-display" font-size="11" font-weight="600">Docker · AWS · Linux</text>
      <text x="0" y="34" fill="#A1A1AA" class="stack-font-display" font-size="10">GitHub Actions · CI/CD</text>
      <text x="0" y="48" fill="#A1A1AA" class="stack-font-display" font-size="10">Vercel · Netlify</text>
    </g>

    <line x1="745" y1="14" x2="745" y2="80" stroke="#1B1922" stroke-width="1"/>

    <!-- Column 5: AI & Automation -->
    <g transform="translate(765, 16)">
      <text x="0" y="0" fill="#F05033" class="stack-font-mono" font-size="9.5" font-weight="700">05 // AI &amp; WORKFLOW</text>
      <text x="0" y="18" fill="#F8FAFC" class="stack-font-display" font-size="11" font-weight="600">AI Agents · N8N</text>
      <text x="0" y="34" fill="#A1A1AA" class="stack-font-display" font-size="10">Hugging Face · Mistral</text>
      <text x="0" y="48" fill="#A1A1AA" class="stack-font-display" font-size="10">Automation DAGs</text>
    </g>
  </g>
</svg>"""

validate_and_save("svg/stack.svg", generate_stack())

# -------------------------------------------------------------------
# 4. ID-DASHBOARD.SVG
# -------------------------------------------------------------------
def generate_id_dashboard():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="dash-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="dash-glow-left" cx="20%" cy="40%" r="45%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="dash-glow-right" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F05033" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="dash-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.4"/>
    </linearGradient>

    <linearGradient id="dash-holo-shimmer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0"/>
      <stop offset="35%" stop-color="#DC2626" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.12"/>
      <stop offset="65%" stop-color="#F05033" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#DC2626" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="dash-bar-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#991B1B"/>
      <stop offset="60%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#F05033"/>
    </linearGradient>

    <clipPath id="dash-portrait-clip">
      <rect x="52" y="105" width="112" height="122" rx="10"/>
    </clipPath>

    <pattern id="dash-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="0.75" fill="#F05033" fill-opacity="0.1"/>
    </pattern>
  </defs>

  <style>
    .dash-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .dash-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes dash-holo-sweep {{
      0% {{ transform: translateX(-150px) rotate(25deg); }}
      50% {{ transform: translateX(350px) rotate(25deg); }}
      100% {{ transform: translateX(350px) rotate(25deg); }}
    }}
    @keyframes dash-scan-laser {{
      0%, 100% {{ transform: translateY(0); opacity: 0.2; }}
      50% {{ transform: translateY(28px); opacity: 0.9; }}
    }}
    @keyframes dash-beacon-pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.3; }}
    }}

    .dash-shimmer {{ animation: dash-holo-sweep 7s infinite ease-in-out; }}
    .dash-laser {{ animation: dash-scan-laser 2.5s infinite ease-in-out; }}
    .dash-beacon {{ animation: dash-beacon-pulse 1.8s infinite ease-in-out; }}
  </style>

  <!-- Background -->
  <rect width="940" height="480" rx="20" fill="url(#dash-bg-grad)"/>
  <rect width="940" height="480" rx="20" fill="url(#dash-glow-left)"/>
  <rect width="940" height="480" rx="20" fill="url(#dash-glow-right)"/>
  <rect width="940" height="480" rx="20" fill="url(#dash-dots)"/>
  <rect x="1" y="1" width="938" height="478" rx="19" fill="none" stroke="url(#dash-border-grad)" stroke-width="1.5"/>

  <!-- ================= LEFT: HOLOGRAPHIC ID CARD ================= -->
  <g transform="translate(30, 0)">
    <!-- Hanging Woven Lanyard Strap -->
    <path d="M 160 0 L 160 38 L 190 38 L 190 0 Z" fill="#991B1B"/>
    <path d="M 165 0 L 175 38 M 175 0 L 185 38" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="3,3"/>

    <!-- Metal Clasp -->
    <rect x="156" y="32" width="38" height="20" rx="4" fill="#3A3A48" stroke="#71717A" stroke-width="1"/>
    <rect x="165" y="44" width="20" height="6" rx="2" fill="#1B1922"/>

    <!-- ID Card Body -->
    <g transform="translate(0, 48)">
      <rect x="15" y="0" width="310" height="412" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#dash-border-grad)" stroke-width="1.5"/>

      <!-- Punch Slot for Clasp -->
      <rect x="155" y="10" width="30" height="6" rx="3" fill="#0D0E16" stroke="#1B1922" stroke-width="0.8"/>

      <!-- Top Header of ID -->
      <g transform="translate(34, 30)">
        <text x="0" y="0" fill="#DC2626" class="dash-font-mono" font-size="9" font-weight="700" letter-spacing="1.2">SYSTEMS ID // SPEC-04</text>
        <text x="210" y="0" fill="#A1A1AA" class="dash-font-mono" font-size="8.5">NEET2516</text>
        <line x1="0" y1="8" x2="272" y2="8" stroke="#1B1922" stroke-width="1"/>
      </g>

      <!-- Smart Card IC Chip (Gold/Crimson Contacts) -->
      <g transform="translate(34, 46)">
        <rect width="36" height="28" rx="4" fill="#2A1B16" stroke="#DC2626" stroke-opacity="0.5" stroke-width="1"/>
        <line x1="12" y1="0" x2="12" y2="28" stroke="#DC2626" stroke-opacity="0.4"/>
        <line x1="24" y1="0" x2="24" y2="28" stroke="#DC2626" stroke-opacity="0.4"/>
        <line x1="0" y1="14" x2="36" y2="14" stroke="#DC2626" stroke-opacity="0.4"/>
        <circle cx="18" cy="14" r="4" fill="#DC2626" fill-opacity="0.3"/>
      </g>

      <!-- Photo Frame & Portrait Image -->
      <g>
        <rect x="32" y="86" width="116" height="126" rx="12" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.4" stroke-width="1.2"/>
        <image href="data:image/png;base64,{PORTRAIT_B64}" x="34" y="88" width="112" height="122" preserveAspectRatio="xMidYMid slice" clip-path="url(#dash-portrait-clip)"/>
      </g>

      <!-- Beside Photo: ID Fields -->
      <g transform="translate(160, 92)">
        <circle class="dash-beacon" cx="4" cy="4" r="3.5" fill="#DC2626"/>
        <text x="14" y="7" fill="#F05033" class="dash-font-mono" font-size="9" font-weight="700">STATUS: ACTIVE</text>

        <text x="0" y="30" fill="#A1A1AA" class="dash-font-mono" font-size="8">CLEARANCE</text>
        <text x="0" y="44" fill="#F8FAFC" class="dash-font-mono" font-size="10" font-weight="700">LEVEL 04 // ROOT</text>

        <text x="0" y="66" fill="#A1A1AA" class="dash-font-mono" font-size="8">DIVISION</text>
        <text x="0" y="80" fill="#F8FAFC" class="dash-font-mono" font-size="10" font-weight="700">DISTRIBUTED SYS</text>

        <text x="0" y="102" fill="#A1A1AA" class="dash-font-mono" font-size="8">NODE LOCATION</text>
        <text x="0" y="116" fill="#F8FAFC" class="dash-font-mono" font-size="10" font-weight="700">GHAZIABAD, IN</text>
      </g>

      <!-- Developer Info -->
      <g transform="translate(34, 234)">
        <text x="0" y="0" fill="#F8FAFC" class="dash-font-display" font-size="18" font-weight="800" letter-spacing="-0.3">NAVNEET SINHA</text>
        <text x="0" y="18" fill="#F05033" class="dash-font-mono" font-size="11" font-weight="700">FULL STACK DEVELOPER</text>
        <text x="0" y="34" fill="#A1A1AA" class="dash-font-mono" font-size="9.5">ID: NEET2516-DEV-007 // OPEN SOURCE</text>
      </g>

      <!-- Barcode with Laser Line -->
      <g transform="translate(34, 290)">
        <rect width="272" height="42" rx="4" fill="#0D0E16" stroke="#1B1922" stroke-width="1"/>
        
        <!-- Barcode lines -->
        <g fill="#A1A1AA" opacity="0.8">
          <rect x="12" y="6" width="3" height="30"/>
          <rect x="18" y="6" width="1.5" height="30"/>
          <rect x="22" y="6" width="4" height="30"/>
          <rect x="29" y="6" width="2" height="30"/>
          <rect x="34" y="6" width="1.5" height="30"/>
          <rect x="39" y="6" width="5" height="30"/>
          <rect x="47" y="6" width="2" height="30"/>
          <rect x="52" y="6" width="3" height="30"/>
          <rect x="58" y="6" width="1.5" height="30"/>
          <rect x="63" y="6" width="4" height="30"/>
          <rect x="70" y="6" width="2.5" height="30"/>
          <rect x="76" y="6" width="1.5" height="30"/>
          <rect x="81" y="6" width="5" height="30"/>
          <rect x="89" y="6" width="2" height="30"/>
          <rect x="94" y="6" width="3.5" height="30"/>
          <rect x="101" y="6" width="1.5" height="30"/>
          <rect x="106" y="6" width="4" height="30"/>
          <rect x="113" y="6" width="2" height="30"/>
          <rect x="118" y="6" width="3" height="30"/>
          <rect x="124" y="6" width="1.5" height="30"/>
          <rect x="129" y="6" width="5" height="30"/>
          <rect x="137" y="6" width="2" height="30"/>
          <rect x="142" y="6" width="4" height="30"/>
          <rect x="149" y="6" width="1.5" height="30"/>
          <rect x="154" y="6" width="3" height="30"/>
          <rect x="160" y="6" width="2.5" height="30"/>
          <rect x="166" y="6" width="1.5" height="30"/>
          <rect x="171" y="6" width="4" height="30"/>
          <rect x="178" y="6" width="2" height="30"/>
          <rect x="183" y="6" width="3" height="30"/>
          <rect x="189" y="6" width="1.5" height="30"/>
          <rect x="194" y="6" width="5" height="30"/>
          <rect x="202" y="6" width="2" height="30"/>
          <rect x="207" y="6" width="3.5" height="30"/>
          <rect x="214" y="6" width="1.5" height="30"/>
          <rect x="219" y="6" width="4" height="30"/>
          <rect x="226" y="6" width="2" height="30"/>
          <rect x="231" y="6" width="3" height="30"/>
          <rect x="237" y="6" width="1.5" height="30"/>
          <rect x="242" y="6" width="5" height="30"/>
          <rect x="250" y="6" width="2" height="30"/>
          <rect x="255" y="6" width="4" height="30"/>
        </g>

        <!-- Laser Line over barcode -->
        <g class="dash-laser">
          <line x1="8" y1="6" x2="264" y2="6" stroke="#DC2626" stroke-width="1.8"/>
          <line x1="8" y1="5.5" x2="264" y2="5.5" stroke="#FFFFFF" stroke-width="0.8" opacity="0.6"/>
        </g>
      </g>

      <!-- ID Footer Tag -->
      <g transform="translate(34, 350)">
        <text x="0" y="0" fill="#DC2626" class="dash-font-mono" font-size="8.5" font-weight="700">AUTHENTICATED DEVELOPER BADGE</text>
        <text x="0" y="14" fill="#A1A1AA" class="dash-font-mono" font-size="7.5">ISSUED: 2024 // ACTIVE LIFETIME // NEET2516</text>
      </g>

      <!-- Holographic Foil Sheen Overlay (Clipped to card) -->
      <g clip-path="url(#dash-card-clip)">
        <rect class="dash-shimmer" x="0" y="0" width="120" height="420" fill="url(#dash-holo-shimmer)"/>
      </g>
    </g>
  </g>

  <!-- ================= RIGHT: GITHUB TELEMETRY DASHBOARD ================= -->
  <g transform="translate(365, 24)">
    <!-- Base Card -->
    <rect width="545" height="432" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#dash-border-grad)" stroke-width="1.2"/>

    <!-- Dashboard Header -->
    <g transform="translate(24, 28)">
      <circle cx="6" cy="6" r="4.5" fill="#DC2626"/>
      <text x="18" y="10" fill="#F8FAFC" class="dash-font-display" font-size="16" font-weight="700">GITHUB METRICS &amp; TELEMETRY</text>
      
      <rect x="365" y="-4" width="132" height="22" rx="11" fill="#0D0E16" stroke="#DC2626" stroke-opacity="0.4" stroke-width="1"/>
      <circle class="dash-beacon" cx="376" cy="7" r="3" fill="#DC2626"/>
      <text x="385" y="10.5" fill="#F05033" class="dash-font-mono" font-size="9" font-weight="700">SYNC: REAL-TIME</text>
    </g>
    <line x1="24" y1="52" x2="521" y2="52" stroke="#1B1922" stroke-width="1"/>

    <!-- 4 Counter Metric Boxes -->
    <g transform="translate(24, 66)">
      <!-- Metric 1: Repositories -->
      <g transform="translate(0, 0)">
        <rect width="116" height="64" rx="8" fill="#1B1922" fill-opacity="0.8" stroke="#DC2626" stroke-opacity="0.25" stroke-width="1"/>
        <text x="12" y="20" fill="#A1A1AA" class="dash-font-mono" font-size="9">PUBLIC REPOS</text>
        <text x="12" y="48" fill="#F8FAFC" class="dash-font-display" font-size="24" font-weight="800">32</text>
      </g>

      <!-- Metric 2: Stars -->
      <g transform="translate(126, 0)">
        <rect width="116" height="64" rx="8" fill="#1B1922" fill-opacity="0.8" stroke="#DC2626" stroke-opacity="0.25" stroke-width="1"/>
        <text x="12" y="20" fill="#A1A1AA" class="dash-font-mono" font-size="9">STARS EARNED</text>
        <text x="12" y="48" fill="#F05033" class="dash-font-display" font-size="24" font-weight="800">15 ★</text>
      </g>

      <!-- Metric 3: Followers -->
      <g transform="translate(252, 0)">
        <rect width="116" height="64" rx="8" fill="#1B1922" fill-opacity="0.8" stroke="#DC2626" stroke-opacity="0.25" stroke-width="1"/>
        <text x="12" y="20" fill="#A1A1AA" class="dash-font-mono" font-size="9">FOLLOWERS</text>
        <text x="12" y="48" fill="#F8FAFC" class="dash-font-display" font-size="24" font-weight="800">8</text>
      </g>

      <!-- Metric 4: Primary Stack -->
      <g transform="translate(378, 0)">
        <rect width="119" height="64" rx="8" fill="#1B1922" fill-opacity="0.8" stroke="#DC2626" stroke-opacity="0.25" stroke-width="1"/>
        <text x="12" y="20" fill="#A1A1AA" class="dash-font-mono" font-size="9">PRIMARY STACK</text>
        <text x="12" y="48" fill="#F8FAFC" class="dash-font-mono" font-size="16" font-weight="700">TS / Rust</text>
      </g>
    </g>

    <!-- Top Repositories Crimson Bar Chart -->
    <g transform="translate(24, 150)">
      <text x="0" y="0" fill="#F8FAFC" class="dash-font-display" font-size="13" font-weight="700">TOP REPOSITORIES BY STAR COUNT</text>
      <text x="360" y="0" fill="#A1A1AA" class="dash-font-mono" font-size="9.5">GITHUB API VERIFIED</text>

      <!-- Bar 1: DevFlow (12 stars - max bar) -->
      <g transform="translate(0, 16)">
        <text x="0" y="14" fill="#F8FAFC" class="dash-font-mono" font-size="11" font-weight="600">DevFlow</text>
        <rect x="130" y="4" width="310" height="13" rx="6.5" fill="#0D0E16"/>
        <rect x="130" y="4" width="290" height="13" rx="6.5" fill="url(#dash-bar-grad)"/>
        <text x="430" y="14" fill="#F05033" class="dash-font-mono" font-size="11" font-weight="700">12 ★</text>
      </g>

      <!-- Bar 2: octo-engine (1 star) -->
      <g transform="translate(0, 40)">
        <text x="0" y="14" fill="#A1A1AA" class="dash-font-mono" font-size="11">octo-engine</text>
        <rect x="130" y="4" width="310" height="13" rx="6.5" fill="#0D0E16"/>
        <rect x="130" y="4" width="35" height="13" rx="6.5" fill="url(#dash-bar-grad)"/>
        <text x="175" y="14" fill="#F05033" class="dash-font-mono" font-size="11" font-weight="700">1 ★</text>
      </g>

      <!-- Bar 3: SyncBoard (1 star) -->
      <g transform="translate(0, 64)">
        <text x="0" y="14" fill="#A1A1AA" class="dash-font-mono" font-size="11">SyncBoard</text>
        <rect x="130" y="4" width="310" height="13" rx="6.5" fill="#0D0E16"/>
        <rect x="130" y="4" width="35" height="13" rx="6.5" fill="url(#dash-bar-grad)"/>
        <text x="175" y="14" fill="#F05033" class="dash-font-mono" font-size="11" font-weight="700">1 ★</text>
      </g>

      <!-- Bar 4: system-design-notes (1 star) -->
      <g transform="translate(0, 88)">
        <text x="0" y="14" fill="#A1A1AA" class="dash-font-mono" font-size="11">system-design</text>
        <rect x="130" y="4" width="310" height="13" rx="6.5" fill="#0D0E16"/>
        <rect x="130" y="4" width="35" height="13" rx="6.5" fill="url(#dash-bar-grad)"/>
        <text x="175" y="14" fill="#F05033" class="dash-font-mono" font-size="11" font-weight="700">1 ★</text>
      </g>

      <!-- Bar 5: city-waste-command (Featured Hackathon) -->
      <g transform="translate(0, 112)">
        <text x="0" y="14" fill="#A1A1AA" class="dash-font-mono" font-size="11">city-waste-cmd</text>
        <rect x="130" y="4" width="310" height="13" rx="6.5" fill="#0D0E16"/>
        <rect x="130" y="4" width="70" height="13" rx="6.5" fill="url(#dash-bar-grad)"/>
        <text x="210" y="14" fill="#F05033" class="dash-font-mono" font-size="10.5">Top 1000 Hack</text>
      </g>
    </g>

    <!-- Telemetry Box: Currently Exploring -->
    <g transform="translate(24, 296)">
      <rect width="497" height="114" rx="10" fill="#0D0E16" stroke="#1B1922" stroke-width="1"/>

      <g transform="translate(16, 18)">
        <circle cx="4" cy="4" r="3.5" fill="#DC2626"/>
        <text x="14" y="7" fill="#F05033" class="dash-font-mono" font-size="10" font-weight="700">CURRENTLY EXPLORING &amp; ENGINEERING</text>
      </g>

      <g transform="translate(16, 40)">
        <text x="0" y="0" fill="#F8FAFC" class="dash-font-mono" font-size="11" font-weight="600">⚡ Rust &amp; Axum High-Performance Services</text>
        <text x="16" y="14" fill="#A1A1AA" class="dash-font-display" font-size="10">Tokio async runtime, low-latency API layers, and type-safe protocols.</text>

        <text x="0" y="38" fill="#F8FAFC" class="dash-font-mono" font-size="11" font-weight="600">⚡ Distributed Consensus, Yjs CRDTs &amp; Event Sinks</text>
        <text x="16" y="52" fill="#A1A1AA" class="dash-font-display" font-size="10">Multi-tenant real-time sync, conflict-free state, and distributed locks.</text>
      </g>
    </g>
  </g>
</svg>"""

validate_and_save("svg/id-dashboard.svg", generate_id_dashboard())

# -------------------------------------------------------------------
# 5. PROJECTS.SVG
# -------------------------------------------------------------------
def generate_projects():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 700" width="100%" height="100%">
  <defs>
    <linearGradient id="proj-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="proj-glow" cx="50%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="proj-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.3"/>
    </linearGradient>

    <linearGradient id="proj-flagship-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F05033"/>
      <stop offset="50%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#991B1B"/>
    </linearGradient>

    <pattern id="proj-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="11" cy="11" r="0.75" fill="#F05033" fill-opacity="0.1"/>
    </pattern>
  </defs>

  <style>
    .proj-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .proj-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes proj-pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.4; }}
    }}
    .proj-beacon {{ animation: proj-pulse 2s infinite ease-in-out; }}
  </style>

  <!-- Background -->
  <rect width="940" height="700" rx="20" fill="url(#proj-bg-grad)"/>
  <rect width="940" height="700" rx="20" fill="url(#proj-glow)"/>
  <rect width="940" height="700" rx="20" fill="url(#proj-dots)"/>
  <rect x="1" y="1" width="938" height="698" rx="19" fill="none" stroke="url(#proj-card-border)" stroke-width="1.5"/>

  <!-- Section Header -->
  <g transform="translate(36, 32)">
    <rect x="0" y="0" width="180" height="22" rx="5" fill="#14141E" stroke="#DC2626" stroke-opacity="0.3" stroke-width="1"/>
    <circle cx="10" cy="11" r="3.5" fill="#DC2626"/>
    <text x="20" y="14.5" fill="#F05033" class="proj-font-mono" font-size="9" font-weight="700" letter-spacing="1">SYSTEM SHOWCASE</text>

    <text x="0" y="44" fill="#F8FAFC" class="proj-font-display" font-size="20" font-weight="800" letter-spacing="-0.4">FEATURED ENGINEERING PROJECTS</text>
    <text x="350" y="44" fill="#A1A1AA" class="proj-font-mono" font-size="11.5">// 5 BESPOKE PRODUCTION BUILDS</text>
  </g>

  <!-- ================= ROW 1: CARDS 1 & 2 ================= -->
  <!-- CARD 1: SyncBoard -->
  <g transform="translate(30, 88)">
    <rect width="425" height="175" rx="14" fill="#14141E" stroke="url(#proj-card-border)" stroke-width="1.2"/>
    
    <g transform="translate(20, 24)">
      <!-- Title & Category -->
      <text x="0" y="0" fill="#F8FAFC" class="proj-font-display" font-size="16" font-weight="700">SyncBoard</text>
      <rect x="96" y="-12" width="124" height="18" rx="4" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.3" stroke-width="0.8"/>
      <text x="104" y="0.5" fill="#F05033" class="proj-font-mono" font-size="8.5" font-weight="600">COLLABORATIVE CANVAS</text>

      <!-- Subtitle -->
      <text x="0" y="20" fill="#F05033" class="proj-font-mono" font-size="10.5" font-weight="600">Real-Time Collaborative Workspace</text>

      <!-- Description -->
      <text x="0" y="38" fill="#A1A1AA" class="proj-font-display" font-size="11">
        <tspan x="0" dy="0">Collaborative infinite canvas with live CRDT synchronization,</tspan>
        <tspan x="0" dy="16">embedded rich text editing, and multi-tenant persistence.</tspan>
      </text>

      <!-- Stack Badges -->
      <g transform="translate(0, 78)">
        <rect width="385" height="22" rx="4" fill="#0D0E16" stroke="#1B1922" stroke-width="0.8"/>
        <text x="8" y="14.5" fill="#A1A1AA" class="proj-font-mono" font-size="9">React · TS · Node.js · WebSockets · Yjs · Redis · MongoDB</text>
      </g>

      <!-- Links & Star -->
      <g transform="translate(0, 114)">
        <text x="0" y="14" fill="#DC2626" class="proj-font-mono" font-size="10" font-weight="700">★ 1 Star</text>
        <text x="65" y="14" fill="#A1A1AA" class="proj-font-mono" font-size="10">|</text>
        <a href="https://github.com/Neet2516/SyncBoard" target="_blank">
          <text x="78" y="14" fill="#F8FAFC" class="proj-font-mono" font-size="10" text-decoration="underline">Source Code ↗</text>
        </a>
        <text x="175" y="14" fill="#A1A1AA" class="proj-font-mono" font-size="10">|</text>
        <a href="https://sync-board-client-lake.vercel.app/" target="_blank">
          <text x="188" y="14" fill="#F05033" class="proj-font-mono" font-size="10" text-decoration="underline">Live App ↗</text>
        </a>
      </g>
    </g>
  </g>

  <!-- CARD 2: Code Theft Auto -->
  <g transform="translate(485, 88)">
    <rect width="425" height="175" rx="14" fill="#14141E" stroke="url(#proj-card-border)" stroke-width="1.2"/>
    
    <g transform="translate(20, 24)">
      <!-- Title & Category -->
      <text x="0" y="0" fill="#F8FAFC" class="proj-font-display" font-size="16" font-weight="700">Code Theft Auto</text>
      <rect x="135" y="-12" width="112" height="18" rx="4" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.3" stroke-width="0.8"/>
      <text x="143" y="0.5" fill="#F05033" class="proj-font-mono" font-size="8.5" font-weight="600">GAMIFIED ARENA</text>

      <!-- Subtitle -->
      <text x="0" y="20" fill="#F05033" class="proj-font-mono" font-size="10.5" font-weight="600">Real-Time Coding Competition Platform</text>

      <!-- Description -->
      <text x="0" y="38" fill="#A1A1AA" class="proj-font-display" font-size="11">
        <tspan x="0" dy="0">Interactive gamified multiplayer competition platform with live</tspan>
        <tspan x="0" dy="16">problem evaluation, dynamic matchmaking, and scoring.</tspan>
      </text>

      <!-- Achievement Callout -->
      <g transform="translate(0, 78)">
        <rect width="385" height="22" rx="4" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.4" stroke-width="1"/>
        <text x="8" y="14.5" fill="#F05033" class="proj-font-mono" font-size="9" font-weight="700">🏆 IMPACT: Used by 130+ students across 40+ teams</text>
      </g>

      <!-- Stack Badges -->
      <g transform="translate(0, 114)">
        <text x="0" y="14" fill="#A1A1AA" class="proj-font-mono" font-size="10">Next.js · TypeScript · Node.js · MongoDB</text>
        <text x="320" y="14" fill="#DC2626" class="proj-font-mono" font-size="9" font-weight="700">[ COMPETITIVE ]</text>
      </g>
    </g>
  </g>

  <!-- ================= ROW 2: CARDS 3 & 4 ================= -->
  <!-- CARD 3: City Waste Command -->
  <g transform="translate(30, 278)">
    <rect width="425" height="175" rx="14" fill="#14141E" stroke="url(#proj-card-border)" stroke-width="1.2"/>
    
    <g transform="translate(20, 24)">
      <!-- Title & Category -->
      <text x="0" y="0" fill="#F8FAFC" class="proj-font-display" font-size="16" font-weight="700">City Waste Command</text>
      <rect x="175" y="-12" width="108" height="18" rx="4" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.3" stroke-width="0.8"/>
      <text x="183" y="0.5" fill="#F05033" class="proj-font-mono" font-size="8.5" font-weight="600">CIRCULAR AI OPS</text>

      <!-- Subtitle -->
      <text x="0" y="20" fill="#F05033" class="proj-font-mono" font-size="10.5" font-weight="600">AI-Driven Circular Waste Intelligence System</text>

      <!-- Description -->
      <text x="0" y="38" fill="#A1A1AA" class="proj-font-display" font-size="11">
        <tspan x="0" dy="0">Geospatial municipal monitoring system coordinating sensor</tspan>
        <tspan x="0" dy="16">telemetry, collection logistics, and circular analytics.</tspan>
      </text>

      <!-- Achievement Callout -->
      <g transform="translate(0, 78)">
        <rect width="385" height="22" rx="4" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.4" stroke-width="1"/>
        <text x="8" y="14.5" fill="#F05033" class="proj-font-mono" font-size="9" font-weight="700">🎖️ AWARD: Selected among Top 1000 teams in national hackathon</text>
      </g>

      <!-- Stack & Link -->
      <g transform="translate(0, 114)">
        <text x="0" y="14" fill="#A1A1AA" class="proj-font-mono" font-size="9.5">React · TS · Express · Tailwind · Shadcn · Recharts · Leaflet</text>
        <a href="https://github.com/Neet2516/city-waste-command" target="_blank">
          <text x="345" y="14" fill="#F8FAFC" class="proj-font-mono" font-size="10" text-decoration="underline">Repo ↗</text>
        </a>
      </g>
    </g>
  </g>

  <!-- CARD 4: Rust CRM -->
  <g transform="translate(485, 278)">
    <rect width="425" height="175" rx="14" fill="#14141E" stroke="url(#proj-card-border)" stroke-width="1.2"/>
    
    <g transform="translate(20, 24)">
      <!-- Title & Category -->
      <text x="0" y="0" fill="#F8FAFC" class="proj-font-display" font-size="16" font-weight="700">Rust CRM</text>
      <rect x="88" y="-12" width="112" height="18" rx="4" fill="#1B1922" stroke="#DC2626" stroke-opacity="0.3" stroke-width="0.8"/>
      <text x="96" y="0.5" fill="#F05033" class="proj-font-mono" font-size="8.5" font-weight="600">HIGH-PERF RUST</text>

      <!-- Subtitle -->
      <text x="0" y="20" fill="#F05033" class="proj-font-mono" font-size="10.5" font-weight="600">Client Lead Management System</text>

      <!-- Description -->
      <text x="0" y="38" fill="#A1A1AA" class="proj-font-display" font-size="11">
        <tspan x="0" dy="0">High-concurrency CRM service built with Rust backend for</tspan>
        <tspan x="0" dy="16">memory safety and microsecond-level query throughput.</tspan>
      </text>

      <!-- Stack Badges -->
      <g transform="translate(0, 78)">
        <rect width="385" height="22" rx="4" fill="#0D0E16" stroke="#1B1922" stroke-width="0.8"/>
        <text x="8" y="14.5" fill="#A1A1AA" class="proj-font-mono" font-size="9">Rust Backend · React Client · TypeScript · REST APIs</text>
      </g>

      <!-- Links -->
      <g transform="translate(0, 114)">
        <a href="https://github.com/Neet2516/FUTURE_FS_02" target="_blank">
          <text x="0" y="14" fill="#F8FAFC" class="proj-font-mono" font-size="10" text-decoration="underline">Source Code (FUTURE_FS_02) ↗</text>
        </a>
        <text x="215" y="14" fill="#A1A1AA" class="proj-font-mono" font-size="10">|</text>
        <a href="https://rust-crm-six.vercel.app/" target="_blank">
          <text x="230" y="14" fill="#F05033" class="proj-font-mono" font-size="10" text-decoration="underline">Live Production App ↗</text>
        </a>
      </g>
    </g>
  </g>

  <!-- ================= ROW 3: FLAGSHIP CARD (DevFlow) ================= -->
  <g transform="translate(30, 468)">
    <rect width="880" height="195" rx="16" fill="#14141E" fill-opacity="0.95" stroke="url(#proj-flagship-border)" stroke-width="1.8"/>

    <g transform="translate(28, 28)">
      <!-- Flagship Badge & Stars -->
      <g transform="translate(0, -6)">
        <rect width="138" height="22" rx="5" fill="#991B1B" fill-opacity="0.3" stroke="#DC2626" stroke-width="1"/>
        <circle class="proj-beacon" cx="10" cy="11" r="3.5" fill="#DC2626"/>
        <text x="18" y="14.5" fill="#FFFFFF" class="proj-font-mono" font-size="9" font-weight="700">★ FLAGSHIP ENGINE</text>

        <rect x="146" width="94" height="22" rx="5" fill="#0D0E16" stroke="#F05033" stroke-width="1"/>
        <text x="156" y="14.5" fill="#F05033" class="proj-font-mono" font-size="9.5" font-weight="700">12 GITHUB ★</text>
      </g>

      <!-- Project Name -->
      <text x="0" y="44" fill="#F8FAFC" class="proj-font-display" font-size="22" font-weight="800" letter-spacing="-0.4">DevFlow</text>
      <text x="110" y="42" fill="#F05033" class="proj-font-mono" font-size="12" font-weight="600">// Distributed Workflow Automation &amp; CI/CD Engine</text>

      <!-- Description -->
      <text x="0" y="68" fill="#A1A1AA" class="proj-font-display" font-size="12" line-height="20">
        <tspan x="0" dy="0">Distributed CI/CD workflow engine for validating and scheduling DAG-based pipelines, coordinating</tspan>
        <tspan x="0" dy="18">specialized worker pools, and streaming live execution telemetry with automatic failure recovery.</tspan>
      </text>

      <!-- Stack Badges Bar -->
      <g transform="translate(0, 104)">
        <rect width="824" height="26" rx="6" fill="#0D0E16" stroke="#1B1922" stroke-width="1"/>
        <text x="12" y="17" fill="#F8FAFC" class="proj-font-mono" font-size="10">Node.js · TypeScript · Express · BullMQ · Redis Streams · PostgreSQL · React · Vite · Docker</text>
      </g>

      <!-- Links & Docs -->
      <g transform="translate(0, 146)">
        <a href="https://github.com/Neet2516/Devflow" target="_blank">
          <text x="0" y="0" fill="#FFFFFF" class="proj-font-mono" font-size="11" font-weight="700" text-decoration="underline">GitHub Repository (github.com/Neet2516/Devflow) ↗</text>
        </a>
        <text x="420" y="0" fill="#A1A1AA" class="proj-font-mono" font-size="11">|</text>
        <a href="https://docs-devflow.vercel.app" target="_blank">
          <text x="435" y="0" fill="#F05033" class="proj-font-mono" font-size="11" font-weight="700" text-decoration="underline">Official Documentation (docs-devflow.vercel.app) ↗</text>
        </a>
      </g>
    </g>
  </g>
</svg>"""

validate_and_save("svg/projects.svg", generate_projects())

# -------------------------------------------------------------------
# 6. CONNECT.SVG
# -------------------------------------------------------------------
def generate_connect():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
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
    .conn-character {{ animation: conn-char-sway 4s infinite ease-in-out; transform-origin: 190px 420px; }}
  </style>

  <!-- Background -->
  <rect width="940" height="480" rx="20" fill="url(#conn-bg-grad)"/>
  <rect width="940" height="480" rx="20" fill="url(#conn-glow-left)"/>
  <rect width="940" height="480" rx="20" fill="url(#conn-glow-right)"/>
  <rect width="940" height="480" rx="20" fill="url(#conn-dots)"/>
  <rect x="1" y="1" width="938" height="478" rx="19" fill="none" stroke="url(#conn-border-grad)" stroke-width="1.5"/>

  <!-- ================= LEFT: POINTING ANIME CHARACTER & STICKER ================= -->
  <!-- Ambient character pedestal glow -->
  <ellipse cx="200" cy="425" rx="130" ry="24" fill="#DC2626" fill-opacity="0.14"/>
  <ellipse cx="200" cy="425" rx="80" ry="14" fill="#F05033" fill-opacity="0.2"/>

  <!-- Character Group -->
  <g class="conn-character" filter="url(#conn-sticker-glow)">
    <!-- White Sticker Outline Backdrop for Character -->
    <image href="data:image/png;base64,{POINTING_B64}" x="40" y="42" width="310" height="375" preserveAspectRatio="xMidYMid meet"/>
  </g>

  <!-- Floating Sparkles (✦) -->
  <!-- Sparkle 1 (Top Left) -->
  <g class="conn-sparkle-1" transform="translate(68, 70)">
    <path d="M 0 -8 Q 0 0 8 0 Q 0 0 0 8 Q 0 0 -8 0 Q 0 0 0 -8 Z" fill="#FFFFFF"/>
    <circle cx="0" cy="0" r="2" fill="#F05033"/>
  </g>
  <!-- Sparkle 2 (Mid Left) -->
  <g class="conn-sparkle-2" transform="translate(48, 220)">
    <path d="M 0 -6 Q 0 0 6 0 Q 0 0 0 6 Q 0 0 -6 0 Q 0 0 0 -6 Z" fill="#F05033"/>
  </g>
  <!-- Sparkle 3 (Near Pointing Hand) -->
  <g class="conn-sparkle-3" transform="translate(330, 140)">
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

  <!-- Pointing Chevrons / Directional Arrows toward Links -->
  <g class="conn-arrow" transform="translate(325, 200)">
    <path d="M 0 0 L 8 8 L 0 16" fill="none" stroke="#DC2626" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 10 0 L 18 8 L 10 16" fill="none" stroke="#F05033" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 20 0 L 28 8 L 20 16" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>
  </g>

  <!-- ================= RIGHT: NEON SIGN & SOCIAL CARDS ================= -->
  <g transform="translate(385, 30)">
    <!-- Crimson Neon Sign Header: NEET2516 -->
    <g class="conn-neon">
      <rect x="0" y="0" width="220" height="38" rx="8" fill="#14141E" stroke="#DC2626" stroke-width="1.8" filter="url(#conn-neon-glow)"/>
      <rect x="0" y="0" width="220" height="38" rx="8" fill="#14141E" stroke="#FFFFFF" stroke-opacity="0.3" stroke-width="1"/>
      <circle cx="16" cy="19" r="4.5" fill="#DC2626"/>
      <text x="28" y="25" fill="url(#conn-neon-grad)" class="conn-font-display" font-size="19" font-weight="800" letter-spacing="3">NEET2516</text>
    </g>

    <!-- Subtitle Badge -->
    <g transform="translate(235, 8)">
      <text x="0" y="14" fill="#F05033" class="conn-font-mono" font-size="10.5" font-weight="700" letter-spacing="1.2">// INITIATE CONNECTION</text>
      <text x="0" y="27" fill="#A1A1AA" class="conn-font-mono" font-size="9">CHANNELS: ACTIVE &amp; RESPONSIVE</text>
    </g>

    <!-- Social Connection Cards (4 items) -->
    <g transform="translate(0, 52)">
      <!-- 1. GitHub -->
      <a href="https://github.com/Neet2516" target="_blank">
        <g transform="translate(0, 0)">
          <rect width="520" height="50" rx="10" fill="#14141E" stroke="#1B1922" stroke-width="1.2"/>
          <rect x="1" y="1" width="518" height="48" rx="9" fill="none" stroke="#DC2626" stroke-opacity="0.25"/>
          
          <!-- GitHub Icon -->
          <circle cx="28" cy="25" r="14" fill="#1B1922"/>
          <path d="M28 15 C22.5 15 18 19.5 18 25 C18 29.4 20.9 33.1 24.8 34.4 C25.3 34.5 25.5 34.2 25.5 33.9 C25.5 33.6 25.5 32.5 25.5 31.2 C22.7 31.8 22.1 30.1 22.1 30.1 C21.7 29 21 28.6 21 28.6 C20.1 28 21.1 28 21.1 28 C22.1 28.1 22.6 29.1 22.6 29.1 C23.5 30.6 24.9 30.2 25.5 29.9 C25.6 29.2 25.8 28.8 26.2 28.5 C23.9 28.2 21.6 27.4 21.6 23.5 C21.6 22.4 22 21.5 22.6 20.8 C22.5 20.5 22.2 19.5 22.7 18.2 C22.7 18.2 23.6 17.9 25.5 19.2 C26.3 19 27.2 18.9 28 18.9 C28.8 18.9 29.7 19 30.5 19.2 C32.4 17.9 33.3 18.2 33.3 18.2 C33.8 19.5 33.5 20.5 33.4 20.8 C34 21.5 34.4 22.4 34.4 23.5 C34.4 27.4 32.1 28.2 29.8 28.5 C30.2 28.9 30.5 29.6 30.5 30.7 C30.5 32.2 30.5 33.5 30.5 33.9 C30.5 34.2 30.7 34.5 31.2 34.4 C35.1 33.1 38 29.4 38 25 C38 19.5 33.5 15 28 15 Z" fill="#F05033"/>

          <text x="56" y="24" fill="#F8FAFC" class="conn-font-display" font-size="13" font-weight="700">GitHub</text>
          <text x="56" y="38" fill="#A1A1AA" class="conn-font-mono" font-size="10.5">https://github.com/Neet2516</text>

          <text x="440" y="30" fill="#F05033" class="conn-font-mono" font-size="11" font-weight="700">Follow ↗</text>
        </g>
      </a>

      <!-- 2. LinkedIn -->
      <a href="https://www.linkedin.com/in/sinha-navneet/" target="_blank">
        <g transform="translate(0, 58)">
          <rect width="520" height="50" rx="10" fill="#14141E" stroke="#1B1922" stroke-width="1.2"/>
          <rect x="1" y="1" width="518" height="48" rx="9" fill="none" stroke="#DC2626" stroke-opacity="0.25"/>

          <!-- LinkedIn Icon -->
          <circle cx="28" cy="25" r="14" fill="#1B1922"/>
          <rect x="21" y="21" width="3" height="9" fill="#0A66C2"/>
          <circle cx="22.5" cy="18" r="1.5" fill="#0A66C2"/>
          <path d="M 26 21 L 28.8 21 L 28.8 22.5 C 29.3 21.6 30.4 20.8 32 20.8 C 34.5 20.8 35 22.4 35 25 L 35 30 L 32.2 30 L 32.2 25.5 C 32.2 24.2 31.8 23.2 30.5 23.2 C 29.2 23.2 28.8 24.2 28.8 25.5 L 28.8 30 L 26 30 Z" fill="#0A66C2"/>

          <text x="56" y="24" fill="#F8FAFC" class="conn-font-display" font-size="13" font-weight="700">LinkedIn</text>
          <text x="56" y="38" fill="#A1A1AA" class="conn-font-mono" font-size="10.5">linkedin.com/in/sinha-navneet/</text>

          <text x="430" y="30" fill="#0A66C2" class="conn-font-mono" font-size="11" font-weight="700">Connect ↗</text>
        </g>
      </a>

      <!-- 3. Portfolio -->
      <a href="https://portfolio-1-tofl.onrender.com/" target="_blank">
        <g transform="translate(0, 116)">
          <rect width="520" height="50" rx="10" fill="#14141E" stroke="#1B1922" stroke-width="1.2"/>
          <rect x="1" y="1" width="518" height="48" rx="9" fill="none" stroke="#DC2626" stroke-opacity="0.25"/>

          <!-- Globe Icon -->
          <circle cx="28" cy="25" r="14" fill="#1B1922"/>
          <circle cx="28" cy="25" r="7.5" fill="none" stroke="#F05033" stroke-width="1.2"/>
          <ellipse cx="28" cy="25" rx="3.5" ry="7.5" fill="none" stroke="#F05033" stroke-width="1"/>
          <line x1="20.5" y1="25" x2="35.5" y2="25" stroke="#F05033" stroke-width="1"/>

          <text x="56" y="24" fill="#F8FAFC" class="conn-font-display" font-size="13" font-weight="700">Personal Portfolio</text>
          <text x="56" y="38" fill="#A1A1AA" class="conn-font-mono" font-size="10.5">portfolio-1-tofl.onrender.com</text>

          <text x="445" y="30" fill="#F05033" class="conn-font-mono" font-size="11" font-weight="700">Visit ↗</text>
        </g>
      </a>

      <!-- 4. Email -->
      <a href="mailto:getneet.25@gmail.com">
        <g transform="translate(0, 174)">
          <rect width="520" height="50" rx="10" fill="#14141E" stroke="#1B1922" stroke-width="1.2"/>
          <rect x="1" y="1" width="518" height="48" rx="9" fill="none" stroke="#DC2626" stroke-opacity="0.25"/>

          <!-- Mail Icon -->
          <circle cx="28" cy="25" r="14" fill="#1B1922"/>
          <rect x="20" y="19" width="16" height="12" rx="2" fill="none" stroke="#DC2626" stroke-width="1.2"/>
          <path d="M 20 20 L 28 26 L 36 20" fill="none" stroke="#DC2626" stroke-width="1.2"/>

          <text x="56" y="24" fill="#F8FAFC" class="conn-font-display" font-size="13" font-weight="700">Direct Dispatch Email</text>
          <text x="56" y="38" fill="#A1A1AA" class="conn-font-mono" font-size="10.5">getneet.25@gmail.com</text>

          <text x="445" y="30" fill="#DC2626" class="conn-font-mono" font-size="11" font-weight="700">Write ↗</text>
        </g>
      </a>
    </g>

    <!-- Closing Manifesto Banner -->
    <g transform="translate(0, 288)">
      <rect width="520" height="88" rx="12" fill="#1B1922" stroke="url(#conn-border-grad)" stroke-width="1.2"/>
      
      <!-- Top Motto -->
      <text x="24" y="30" fill="url(#conn-manifesto-grad)" class="conn-font-display" font-size="16" font-weight="800" letter-spacing="1.5">BUILD. BREAK. LEARN. REPEAT.</text>

      <!-- Subtext -->
      <text x="24" y="52" fill="#A1A1AA" class="conn-font-display" font-size="11.5">
        <tspan x="24" dy="0">Thanks for visiting my corner of the internet.</tspan>
        <tspan x="24" dy="18">Let's build something extraordinary together.</tspan>
      </text>

      <circle cx="475" cy="44" r="18" fill="#14141E" stroke="#DC2626" stroke-width="1"/>
      <text x="475" y="49" text-anchor="middle" fill="#F05033" class="conn-font-mono" font-size="14" font-weight="700">∞</text>
    </g>
  </g>
</svg>"""

validate_and_save("svg/connect.svg", generate_connect())

# -------------------------------------------------------------------
# 7. CONTRIBUTION-CITY-PREVIEW.SVG (MIDNIGHT CRIMSON 3D SKYLINE)
# -------------------------------------------------------------------
def generate_city():
    # Generate isometric buildings with illuminated crimson windows
    import random
    random.seed(2516)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 380" width="100%" height="100%">
  <defs>
    <linearGradient id="city-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D0E16"/>
      <stop offset="50%" stop-color="#14141E"/>
      <stop offset="100%" stop-color="#0D0E16"/>
    </linearGradient>

    <radialGradient id="city-moon-glow" cx="50%" cy="10%" r="50%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.22"/>
      <stop offset="50%" stop-color="#991B1B" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#0D0E16" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="city-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#1B1922" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#F05033" stop-opacity="0.3"/>
    </linearGradient>

    <pattern id="city-dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="0.75" fill="#F05033" fill-opacity="0.08"/>
    </pattern>
  </defs>

  <style>
    .city-font-display {{
      font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    .city-font-mono {{
      font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}

    @keyframes city-window-flicker {{
      0%, 100% {{ opacity: 0.9; }}
      50% {{ opacity: 0.4; }}
    }}
    @keyframes city-beacon-blink {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.2; transform: scale(0.8); }}
    }}

    .city-window {{ animation: city-window-flicker 4s infinite ease-in-out; }}
    .city-beacon {{ animation: city-beacon-blink 2s infinite ease-in-out; }}
  </style>

  <!-- Background -->
  <rect width="940" height="380" rx="20" fill="url(#city-bg-grad)"/>
  <rect width="940" height="380" rx="20" fill="url(#city-moon-glow)"/>
  <rect width="940" height="380" rx="20" fill="url(#city-dots)"/>
  <rect x="1" y="1" width="938" height="378" rx="19" fill="none" stroke="url(#city-border-grad)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(36, 32)">
    <rect x="0" y="0" width="180" height="22" rx="5" fill="#14141E" stroke="#DC2626" stroke-opacity="0.3" stroke-width="1"/>
    <circle cx="10" cy="11" r="3.5" fill="#DC2626"/>
    <text x="20" y="14.5" fill="#F05033" class="city-font-mono" font-size="9" font-weight="700" letter-spacing="1">GITHUB ARCHITECTURE</text>

    <text x="0" y="44" fill="#F8FAFC" class="city-font-display" font-size="20" font-weight="800" letter-spacing="-0.4">GITHUB CONTRIBUTION CITY</text>
    <text x="310" y="44" fill="#A1A1AA" class="city-font-mono" font-size="11.5">// 3D CODE METROPOLIS · MIDNIGHT EDITION</text>
  </g>

  <!-- Ground Plane Isometric Grid -->
  <g transform="translate(0, 110)">
    <!-- Base horizontal ground glow -->
    <ellipse cx="470" cy="200" rx="420" ry="45" fill="#14141E" fill-opacity="0.8"/>
    <ellipse cx="470" cy="200" rx="350" ry="30" fill="#DC2626" fill-opacity="0.08"/>

    <!-- Isometric 3D Skyline Buildings -->
    <!-- Far Background Silhouettes -->
    <rect x="60" y="80" width="45" height="120" fill="#11121C" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="120" y="50" width="55" height="150" fill="#131422" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="190" y="100" width="40" height="100" fill="#11121C" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="245" y="30" width="60" height="170" fill="#161726" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="320" y="70" width="50" height="130" fill="#131422" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="385" y="20" width="70" height="180" fill="#18192A" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="470" y="10" width="80" height="190" fill="#1A1B2E" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="565" y="40" width="65" height="160" fill="#161726" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="645" y="80" width="50" height="120" fill="#131422" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="710" y="45" width="60" height="155" fill="#161726" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="785" y="90" width="45" height="110" fill="#11121C" stroke="#1B1922" stroke-width="0.8"/>
    <rect x="845" y="65" width="50" height="135" fill="#131422" stroke="#1B1922" stroke-width="0.8"/>

    <!-- Midground Towers with Crimson Windows -->
    <!-- Tower 1 -->
    <g transform="translate(130, 40)">
      <rect width="60" height="160" fill="#14141E" stroke="#991B1B" stroke-opacity="0.4" stroke-width="1"/>
      <circle class="city-beacon" cx="30" cy="0" r="2.5" fill="#DC2626"/>
      <!-- Window grid -->
      <g fill="#DC2626" opacity="0.75" class="city-window">
        <rect x="10" y="20" width="6" height="8" rx="1"/>
        <rect x="22" y="20" width="6" height="8" rx="1"/>
        <rect x="44" y="20" width="6" height="8" rx="1"/>
        <rect x="10" y="40" width="6" height="8" rx="1"/>
        <rect x="34" y="40" width="6" height="8" rx="1"/>
        <rect x="44" y="40" width="6" height="8" rx="1"/>
        <rect x="22" y="60" width="6" height="8" rx="1"/>
        <rect x="34" y="60" width="6" height="8" rx="1"/>
        <rect x="10" y="80" width="6" height="8" rx="1"/>
        <rect x="44" y="80" width="6" height="8" rx="1"/>
        <rect x="22" y="100" width="6" height="8" rx="1"/>
        <rect x="34" y="100" width="6" height="8" rx="1"/>
      </g>
    </g>

    <!-- Tower 2 (The Central Apex - DevFlow Tower) -->
    <g transform="translate(430, 0)">
      <rect width="80" height="200" fill="#1B1922" stroke="#DC2626" stroke-width="1.2"/>
      <!-- Rooftop Spire -->
      <line x1="40" y1="0" x2="40" y2="-25" stroke="#F05033" stroke-width="2"/>
      <circle class="city-beacon" cx="40" cy="-26" r="3.5" fill="#DC2626"/>
      
      <!-- Illuminated Windows -->
      <g fill="#F05033" opacity="0.85">
        <rect x="14" y="25" width="8" height="10" rx="1"/>
        <rect x="28" y="25" width="8" height="10" rx="1"/>
        <rect x="42" y="25" width="8" height="10" rx="1"/>
        <rect x="56" y="25" width="8" height="10" rx="1"/>

        <rect x="14" y="48" width="8" height="10" rx="1"/>
        <rect x="42" y="48" width="8" height="10" rx="1"/>
        <rect x="56" y="48" width="8" height="10" rx="1"/>

        <rect x="28" y="72" width="8" height="10" rx="1"/>
        <rect x="42" y="72" width="8" height="10" rx="1"/>

        <rect x="14" y="96" width="8" height="10" rx="1"/>
        <rect x="28" y="96" width="8" height="10" rx="1"/>
        <rect x="56" y="96" width="8" height="10" rx="1"/>

        <rect x="14" y="120" width="8" height="10" rx="1"/>
        <rect x="42" y="120" width="8" height="10" rx="1"/>
      </g>
    </g>

    <!-- Tower 3 (SyncBoard Tower) -->
    <g transform="translate(250, 30)">
      <rect width="65" height="170" fill="#14141E" stroke="#DC2626" stroke-opacity="0.5" stroke-width="1"/>
      <circle class="city-beacon" cx="32" cy="0" r="2.5" fill="#DC2626"/>
      <g fill="#DC2626" opacity="0.8">
        <rect x="12" y="30" width="7" height="9" rx="1"/>
        <rect x="26" y="30" width="7" height="9" rx="1"/>
        <rect x="44" y="30" width="7" height="9" rx="1"/>
        <rect x="26" y="55" width="7" height="9" rx="1"/>
        <rect x="44" y="55" width="7" height="9" rx="1"/>
        <rect x="12" y="80" width="7" height="9" rx="1"/>
        <rect x="26" y="80" width="7" height="9" rx="1"/>
        <rect x="12" y="105" width="7" height="9" rx="1"/>
        <rect x="44" y="105" width="7" height="9" rx="1"/>
      </g>
    </g>

    <!-- Tower 4 (Rust Tower) -->
    <g transform="translate(600, 20)">
      <rect width="70" height="180" fill="#14141E" stroke="#DC2626" stroke-opacity="0.5" stroke-width="1"/>
      <line x1="35" y1="0" x2="35" y2="-18" stroke="#DC2626" stroke-width="1.5"/>
      <circle class="city-beacon" cx="35" cy="-19" r="2.5" fill="#F05033"/>
      <g fill="#F05033" opacity="0.85">
        <rect x="14" y="24" width="7" height="9" rx="1"/>
        <rect x="30" y="24" width="7" height="9" rx="1"/>
        <rect x="46" y="24" width="7" height="9" rx="1"/>
        <rect x="14" y="48" width="7" height="9" rx="1"/>
        <rect x="46" y="48" width="7" height="9" rx="1"/>
        <rect x="30" y="72" width="7" height="9" rx="1"/>
        <rect x="46" y="72" width="7" height="9" rx="1"/>
        <rect x="14" y="96" width="7" height="9" rx="1"/>
        <rect x="30" y="96" width="7" height="9" rx="1"/>
      </g>
    </g>

    <!-- Tower 5 (Command Center) -->
    <g transform="translate(730, 50)">
      <rect width="60" height="150" fill="#14141E" stroke="#991B1B" stroke-opacity="0.4" stroke-width="1"/>
      <circle class="city-beacon" cx="30" cy="0" r="2" fill="#DC2626"/>
      <g fill="#DC2626" opacity="0.7">
        <rect x="10" y="20" width="6" height="8" rx="1"/>
        <rect x="32" y="20" width="6" height="8" rx="1"/>
        <rect x="44" y="20" width="6" height="8" rx="1"/>
        <rect x="20" y="45" width="6" height="8" rx="1"/>
        <rect x="32" y="45" width="6" height="8" rx="1"/>
        <rect x="10" y="70" width="6" height="8" rx="1"/>
        <rect x="44" y="70" width="6" height="8" rx="1"/>
      </g>
    </g>

    <!-- Foreground Highway & Telemetry Bar -->
    <line x1="40" y1="200" x2="900" y2="200" stroke="#DC2626" stroke-width="1.5" stroke-opacity="0.6"/>
    <line x1="40" y1="204" x2="900" y2="204" stroke="#F05033" stroke-width="0.8" stroke-dasharray="12,16"/>
  </g>

  <!-- Footer Telemetry -->
  <g transform="translate(36, 335)">
    <text x="0" y="16" fill="#F8FAFC" class="city-font-mono" font-size="10" font-weight="700">AUTONOMOUS DISPATCH // DAILY CRON ACTIVE</text>
    <text x="360" y="16" fill="#A1A1AA" class="city-font-mono" font-size="9.5">ACTION: yoshi389111/github-profile-3d-contrib</text>
    <text x="730" y="16" fill="#DC2626" class="city-font-mono" font-size="9.5" font-weight="700">SCHEDULE: 0 18 * * *</text>
  </g>
</svg>"""

validate_and_save("svg/contribution-city-preview.svg", generate_city())
print("All SVGs successfully created and verified!")
