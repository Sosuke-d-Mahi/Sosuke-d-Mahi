import os

# -------------------------------------------------------------
# 1. assets/hero-portrait.svg (100% PURE VECTOR SVG - ZERO RASTER IMAGES)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="1200" height="440" role="img" aria-label="Easir Iqbal Mahi — Full-stack Software Developer &amp; Founder @ Lagbeto">
  <defs>
    <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#17060A"/>
      <stop offset="50%" stop-color="#0E0407"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#7F1D1D" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#EF4444" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#EF4444" stop-opacity="0"/>
    </radialGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .t-white { fill: #FFFFFF; }
      .t-red { fill: #EF4444; }
      .t-sub { fill: #FECACA; }
      .pill-tag { fill: #1F070C; stroke: #991B1B; stroke-width: 1.5; rx: 10; }
      .pill-txt { font-family: system-ui, sans-serif; font-size: 14px; font-weight: 700; fill: #FFFFFF; }
      .node-box { fill: #240A12; stroke: #991B1B; stroke-width: 1.2; rx: 8; }
      .node-lbl { font-family: "JetBrains Mono", monospace; font-size: 11px; font-weight: 700; fill: #FECACA; }
    </style>
  </defs>

  <!-- Background -->
  <rect x="10" y="10" width="1180" height="420" rx="24" fill="url(#hero-bg)" stroke="#991B1B" stroke-width="2.5"/>
  <rect x="10" y="10" width="1180" height="420" rx="24" fill="url(#hero-glow)"/>

  <!-- Left Info Column -->
  <g transform="translate(56, 44)">
    <!-- Eyebrow -->
    <g>
      <circle cx="6" cy="6" r="5" fill="#EF4444"/>
      <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#EF4444">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>
    </g>

    <!-- Main Title -->
    <text class="t-bold t-white" x="0" y="68" font-size="52">Easir Iqbal</text>
    <text class="t-bold" x="0" y="124" font-size="52" fill="#FFFFFF">Mahi<tspan fill="#EF4444">.</tspan></text>

    <!-- Stack Subtitle -->
    <rect x="0" y="150" width="700" height="40" rx="10" fill="#1C060B" stroke="#991B1B" stroke-width="1.2"/>
    <text class="t-mono" x="20" y="175" font-size="14" fill="#FFFFFF">TypeScript • Python • Go • Nodejs • JavaScript • Java • Flutter • Kotlin</text>

    <!-- Philosophy Quote -->
    <g transform="translate(0, 210)">
      <rect x="0" y="0" width="700" height="68" rx="14" fill="#170509" stroke="#DC2626" stroke-width="1.4"/>
      <text class="t-bold" x="22" y="28" font-size="16.5" fill="#EF4444">“I don’t seek approval, I seek superiority</text>
      <text class="t-bold t-white" x="22" y="53" font-size="16.5">then I build until reality has no choice but to agree.”</text>
    </g>

    <!-- Quick Highlights -->
    <g transform="translate(0, 298)">
      <g>
        <rect class="pill-tag" x="0" y="0" width="220" height="36"/>
        <text class="pill-txt" x="110" y="23" text-anchor="middle">Startup: Founder @ Lagbeto</text>
      </g>
      <g transform="translate(232, 0)">
        <rect class="pill-tag" x="0" y="0" width="220" height="36"/>
        <text class="pill-txt" x="110" y="23" text-anchor="middle">Featured: api-docs.git</text>
      </g>
      <g transform="translate(464, 0)">
        <rect class="pill-tag" x="0" y="0" width="236" height="36"/>
        <text class="pill-txt" x="118" y="23" text-anchor="middle">Passions: Game Modding</text>
      </g>
    </g>
  </g>

  <!-- Right Architecture Panel (Pure SVG Vector — Zero Raster Images) -->
  <g transform="translate(800, 44)">
    <rect x="0" y="0" width="344" height="352" rx="20" fill="#17060C" stroke="#991B1B" stroke-width="2"/>
    
    <!-- Top Console Header -->
    <path d="M0 20 C0 9 9 0 20 0 L324 0 C335 0 344 9 344 20 L344 40 L0 40 Z" fill="#240A13"/>
    <circle cx="20" cy="20" r="4.5" fill="#EF4444"/>
    <circle cx="34" cy="20" r="4.5" fill="#7F1D1D"/>
    <circle cx="48" cy="20" r="4.5" fill="#3D0B12"/>
    <text class="t-mono" x="190" y="25" text-anchor="middle" font-size="11.5" letter-spacing="1.5" fill="#FECACA">SYSTEM ARCHITECTURE</text>

    <!-- Center Technical Core -->
    <g transform="translate(172, 172)">
      <!-- Outer Orbit Ring -->
      <circle cx="0" cy="0" r="115" fill="none" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="5 7"/>
      <!-- Inner Orbit Ring -->
      <circle cx="0" cy="0" r="70" fill="none" stroke="#DC2626" stroke-width="1.4" stroke-opacity="0.6"/>
      
      <!-- Core Glow -->
      <circle cx="0" cy="0" r="44" fill="url(#core-glow)"/>
      <circle cx="0" cy="0" r="32" fill="#881326" stroke="#EF4444" stroke-width="1.8"/>
      <text class="t-bold" x="0" y="-4" text-anchor="middle" font-size="14" fill="#FFFFFF">LAGBETO</text>
      <text class="t-mono" x="0" y="14" text-anchor="middle" font-size="10" letter-spacing="1" fill="#FECACA">CORE</text>

      <!-- Node 1: Top (Backend) -->
      <g transform="translate(0, -96)">
        <rect class="node-box" x="-56" y="-15" width="112" height="30"/>
        <text class="node-lbl" x="0" y="5" text-anchor="middle">GO · NODE.JS</text>
      </g>

      <!-- Node 2: Right (Frontend) -->
      <g transform="translate(94, 0)">
        <rect class="node-box" x="-15" y="-15" width="112" height="30"/>
        <text class="node-lbl" x="41" y="5" text-anchor="middle">NEXT · FLUTTER</text>
      </g>

      <!-- Node 3: Bottom (Databases) -->
      <g transform="translate(0, 96)">
        <rect class="node-box" x="-56" y="-15" width="112" height="30"/>
        <text class="node-lbl" x="0" y="5" text-anchor="middle">POSTGRES · REDIS</text>
      </g>

      <!-- Node 4: Left (Systems & AI) -->
      <g transform="translate(-94, 0)">
        <rect class="node-box" x="-97" y="-15" width="112" height="30"/>
        <text class="node-lbl" x="-41" y="5" text-anchor="middle">DOCKER · TOOLS</text>
      </g>
    </g>

    <!-- Bottom Status Bar -->
    <g transform="translate(20, 308)">
      <rect x="0" y="0" width="304" height="32" rx="8" fill="#200810" stroke="#991B1B" stroke-width="1.2"/>
      <circle cx="16" cy="16" r="4" fill="#EF4444"/>
      <text class="t-mono" x="28" y="21" font-size="11.5" letter-spacing="1.2" fill="#FFFFFF">STATUS: ACTIVE DEVELOPER · 679 COMMITS</text>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/hero-portrait.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
print('Wrote assets/hero-portrait.svg (Pure SVG)')

# -------------------------------------------------------------
# 2. assets/about-card.svg
# -------------------------------------------------------------
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-label="About Easir Iqbal Mahi">
  <defs>
    <linearGradient id="card-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#17060A"/>
      <stop offset="100%" stop-color="#0A0205"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .box-dark { fill: #1D060C; stroke: #991B1B; stroke-width: 1.5; rx: 16; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="380" rx="24" fill="url(#card-bg)" stroke="#991B1B" stroke-width="2.5"/>

  <!-- Header -->
  <g transform="translate(56, 44)">
    <circle cx="6" cy="6" r="5" fill="#EF4444"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#EF4444">01 · ABOUT ME &amp; VENTURE</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Currently Building &amp; <tspan fill="#EF4444">Exploring.</tspan></text>
  </g>

  <!-- 4 Grid Blocks -->
  <g transform="translate(56, 126)">
    <!-- Box 1 -->
    <g>
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#EF4444">CURRENTLY WORKING AT</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Founder of my own Startup called Lagbeto</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#FECACA">Leading platform architecture &amp; cross-platform development</text>
    </g>

    <!-- Box 2 -->
    <g transform="translate(560, 0)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#EF4444">LEARNING</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Talking face to face skill :)</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#FECACA">High-impact communication &amp; live technical dialogues</text>
    </g>

    <!-- Box 3 -->
    <g transform="translate(0, 124)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#EF4444">LOOKING TO COLLABORATE ON</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Pro Full-stack Developers</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#FECACA">Partnering with talented engineers on scalable systems</text>
    </g>

    <!-- Box 4 -->
    <g transform="translate(560, 124)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#EF4444">IN MY FREE TIME</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Love playing games and modding those games ^_~</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#FECACA">Game engine reverse engineering &amp; memory hooking</text>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/about-card.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)
print('Wrote assets/about-card.svg')

# -------------------------------------------------------------
# 3. assets/projects-card.svg
# -------------------------------------------------------------
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-label="Featured Projects of Easir Iqbal Mahi">
  <defs>
    <linearGradient id="proj-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#17060A"/>
      <stop offset="100%" stop-color="#0A0205"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .proj-box { fill: #1D060C; stroke: #991B1B; stroke-width: 1.6; rx: 18; }
      .tag-pill { fill: #2C0913; stroke: #DC2626; stroke-width: 1.2; rx: 8; }
      .tag-txt { font-family: system-ui, sans-serif; font-size: 13.5px; font-weight: 700; fill: #FFFFFF; }
      .badge-bg { fill: #DC2626; rx: 6; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="400" rx="24" fill="url(#proj-bg)" stroke="#991B1B" stroke-width="2.5"/>

  <!-- Header -->
  <g transform="translate(56, 44)">
    <circle cx="6" cy="6" r="5" fill="#EF4444"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#EF4444">02 · FEATURED WORK &amp; VENTURE</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Products, not <tspan fill="#EF4444">assignments.</tspan></text>
  </g>

  <!-- 2 Project Cards Side-by-Side -->
  <g transform="translate(56, 126)">
    <!-- Project 1: api-docs -->
    <g>
      <rect class="proj-box" x="0" y="0" width="525" height="236"/>
      <!-- Badge -->
      <rect class="badge-bg" x="24" y="22" width="156" height="26"/>
      <text class="t-mono" x="102" y="39.5" text-anchor="middle" font-size="12" fill="#FFFFFF">FEATURED PROJECT</text>
      
      <text class="t-bold" x="24" y="84" font-size="28" fill="#FFFFFF">api-docs</text>
      <text class="t-mono" x="24" y="110" font-size="13" fill="#EF4444">github.com · Sosuke-d-Mahi · api-docs</text>
      
      <text class="t-bold" x="24" y="144" font-size="15.5" fill="#FFFFFF">Interactive developer documentation engine &amp; sandbox</text>
      <text class="t-bold" x="24" y="168" font-size="14" fill="#FECACA">Real-time schema testing, automated spec parsing, zero-friction docs.</text>

      <!-- Tags -->
      <g transform="translate(24, 186)">
        <rect class="tag-pill" x="0" y="0" width="100" height="28"/><text class="tag-txt" x="50" y="18.5" text-anchor="middle">TypeScript</text>
        <rect class="tag-pill" x="110" y="0" width="80" height="28"/><text class="tag-txt" x="150" y="18.5" text-anchor="middle">Node.js</text>
        <rect class="tag-pill" x="200" y="0" width="86" height="28"/><text class="tag-txt" x="243" y="18.5" text-anchor="middle">REST API</text>
        <rect class="tag-pill" x="296" y="0" width="84" height="28"/><text class="tag-txt" x="338" y="18.5" text-anchor="middle">OpenAPI</text>
      </g>
    </g>

    <!-- Project 2: Lagbeto -->
    <g transform="translate(560, 0)">
      <rect class="proj-box" x="0" y="0" width="525" height="236"/>
      <!-- Badge -->
      <rect class="badge-bg" x="24" y="22" width="144" height="26"/>
      <text class="t-mono" x="96" y="39.5" text-anchor="middle" font-size="12" fill="#FFFFFF">STARTUP VENTURE</text>
      
      <text class="t-bold" x="24" y="84" font-size="28" fill="#FFFFFF">Lagbeto Platform</text>
      <text class="t-mono" x="24" y="110" font-size="13" fill="#EF4444">Founder &amp; Platform Architecture</text>
      
      <text class="t-bold" x="24" y="144" font-size="15.5" fill="#FFFFFF">Multi-service backend platform &amp; Flutter mobile app</text>
      <text class="t-bold" x="24" y="168" font-size="14" fill="#FECACA">High-concurrency Go services, PostgreSQL, and cross-platform mobile client.</text>

      <!-- Tags -->
      <g transform="translate(24, 186)">
        <rect class="tag-pill" x="0" y="0" width="82" height="28"/><text class="tag-txt" x="41" y="18.5" text-anchor="middle">Next.js</text>
        <rect class="tag-pill" x="92" y="0" width="54" height="28"/><text class="tag-txt" x="119" y="18.5" text-anchor="middle">Go</text>
        <rect class="pill-tag" x="156" y="0" width="98" height="28"/><text class="tag-txt" x="205" y="18.5" text-anchor="middle">PostgreSQL</text>
        <rect class="tag-pill" x="264" y="0" width="68" height="28"/><text class="tag-txt" x="298" y="18.5" text-anchor="middle">Redis</text>
        <rect class="tag-pill" x="342" y="0" width="76" height="28"/><text class="tag-txt" x="380" y="18.5" text-anchor="middle">Flutter</text>
      </g>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/projects-card.svg', 'w', encoding='utf-8') as f:
    f.write(projects_svg)
print('Wrote assets/projects-card.svg')

# -------------------------------------------------------------
# 4. assets/tech-card.svg
# -------------------------------------------------------------
tech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-label="Tech Stack and Toolkit of Easir Iqbal Mahi">
  <defs>
    <linearGradient id="tech-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#17060A"/>
      <stop offset="100%" stop-color="#0A0205"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .cat-lbl { font-family: "JetBrains Mono", monospace; font-size: 13.5px; font-weight: 700; fill: #EF4444; letter-spacing: 1.5px; }
      .pill-primary { fill: #2C0913; stroke: #DC2626; stroke-width: 1.3; rx: 9; }
      .pill-sub { fill: #1D060C; stroke: #991B1B; stroke-width: 1.2; rx: 9; }
      .pill-lbl { font-family: system-ui, sans-serif; font-size: 14px; font-weight: 700; fill: #FFFFFF; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="350" rx="24" fill="url(#tech-bg)" stroke="#991B1B" stroke-width="2.5"/>

  <!-- Header -->
  <g transform="translate(56, 44)">
    <circle cx="6" cy="6" r="5" fill="#EF4444"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#EF4444">03 · TECHNICAL ARSENAL</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Production-Tested <tspan fill="#EF4444">Technologies.</tspan></text>
  </g>

  <!-- 4 Skill Rows -->
  <g transform="translate(56, 126)">
    <!-- Row 1: Languages -->
    <g transform="translate(0, 0)">
      <text class="cat-lbl" x="0" y="23">LANGUAGES</text>
      <g transform="translate(190, 0)">
        <rect class="pill-primary" x="0" y="0" width="105" height="34"/><text class="pill-lbl" x="52" y="22.5" text-anchor="middle">TypeScript</text>
        <rect class="pill-primary" x="115" y="0" width="80" height="34"/><text class="pill-lbl" x="155" y="22.5" text-anchor="middle">Python</text>
        <rect class="pill-primary" x="205" y="0" width="56" height="34"/><text class="pill-lbl" x="233" y="22.5" text-anchor="middle">Go</text>
        <rect class="pill-primary" x="271" y="0" width="88" height="34"/><text class="pill-lbl" x="315" y="22.5" text-anchor="middle">Node.js</text>
        <rect class="pill-sub" x="369" y="0" width="102" height="34"/><text class="pill-lbl" x="420" y="22.5" text-anchor="middle">JavaScript</text>
        <rect class="pill-sub" x="481" y="0" width="62" height="34"/><text class="pill-lbl" x="512" y="22.5" text-anchor="middle">Java</text>
        <rect class="pill-sub" x="553" y="0" width="70" height="34"/><text class="pill-lbl" x="588" y="22.5" text-anchor="middle">Kotlin</text>
        <rect class="pill-sub" x="633" y="0" width="60" height="34"/><text class="pill-lbl" x="663" y="22.5" text-anchor="middle">Dart</text>
        <rect class="pill-sub" x="703" y="0" width="78" height="34"/><text class="pill-lbl" x="742" y="22.5" text-anchor="middle">C, C++</text>
      </g>
    </g>

    <!-- Row 2: Frontend & Mobile -->
    <g transform="translate(0, 56)">
      <text class="cat-lbl" x="0" y="23">FRONTEND &amp; UI</text>
      <g transform="translate(190, 0)">
        <rect class="pill-primary" x="0" y="0" width="74" height="34"/><text class="pill-lbl" x="37" y="22.5" text-anchor="middle">React</text>
        <rect class="pill-primary" x="84" y="0" width="84" height="34"/><text class="pill-lbl" x="126" y="22.5" text-anchor="middle">Next.js</text>
        <rect class="pill-primary" x="178" y="0" width="76" height="34"/><text class="pill-lbl" x="216" y="22.5" text-anchor="middle">Flutter</text>
        <rect class="pill-primary" x="264" y="0" width="112" height="34"/><text class="pill-lbl" x="320" y="22.5" text-anchor="middle">TailwindCSS</text>
        <rect class="pill-sub" x="386" y="0" width="78" height="34"/><text class="pill-lbl" x="425" y="22.5" text-anchor="middle">Vue.js</text>
        <rect class="pill-sub" x="474" y="0" width="84" height="34"/><text class="pill-lbl" x="516" y="22.5" text-anchor="middle">Angular</text>
        <rect class="pill-sub" x="568" y="0" width="68" height="34"/><text class="pill-lbl" x="602" y="22.5" text-anchor="middle">Astro</text>
        <rect class="pill-sub" x="646" y="0" width="96" height="34"/><text class="pill-lbl" x="694" y="22.5" text-anchor="middle">Bootstrap</text>
      </g>
    </g>

    <!-- Row 3: Backend & Databases -->
    <g transform="translate(0, 112)">
      <text class="cat-lbl" x="0" y="23">BACKEND &amp; DATA</text>
      <g transform="translate(190, 0)">
        <rect class="pill-primary" x="0" y="0" width="112" height="34"/><text class="pill-lbl" x="56" y="22.5" text-anchor="middle">PostgreSQL</text>
        <rect class="pill-primary" x="122" y="0" width="70" height="34"/><text class="pill-lbl" x="157" y="22.5" text-anchor="middle">Redis</text>
        <rect class="pill-primary" x="202" y="0" width="86" height="34"/><text class="pill-lbl" x="245" y="22.5" text-anchor="middle">Docker</text>
        <rect class="pill-primary" x="298" y="0" width="100" height="34"/><text class="pill-lbl" x="348" y="22.5" text-anchor="middle">Supabase</text>
        <rect class="pill-sub" x="408" y="0" width="98" height="34"/><text class="pill-lbl" x="457" y="22.5" text-anchor="middle">MongoDB</text>
        <rect class="pill-sub" x="516" y="0" width="80" height="34"/><text class="pill-lbl" x="556" y="22.5" text-anchor="middle">FastAPI</text>
        <rect class="pill-sub" x="606" y="0" width="80" height="34"/><text class="pill-lbl" x="646" y="22.5" text-anchor="middle">Django</text>
        <rect class="pill-sub" x="696" y="0" width="76" height="34"/><text class="pill-lbl" x="734" y="22.5" text-anchor="middle">MySQL</text>
      </g>
    </g>

    <!-- Row 4: Cloud & AI Tooling -->
    <g transform="translate(0, 168)">
      <text class="cat-lbl" x="0" y="23">AI &amp; CLOUD</text>
      <g transform="translate(190, 0)">
        <rect class="pill-primary" x="0" y="0" width="120" height="34"/><text class="pill-lbl" x="60" y="22.5" text-anchor="middle">Claude Code</text>
        <rect class="pill-primary" x="130" y="0" width="102" height="34"/><text class="pill-lbl" x="181" y="22.5" text-anchor="middle">Cursor AI</text>
        <rect class="pill-primary" x="242" y="0" width="88" height="34"/><text class="pill-lbl" x="286" y="22.5" text-anchor="middle">OpenAI</text>
        <rect class="pill-primary" x="340" y="0" width="86" height="34"/><text class="pill-lbl" x="383" y="22.5" text-anchor="middle">Gemini</text>
        <rect class="pill-sub" x="436" y="0" width="58" height="34"/><text class="pill-lbl" x="465" y="22.5" text-anchor="middle">Git</text>
        <rect class="pill-sub" x="504" y="0" width="92" height="34"/><text class="pill-lbl" x="550" y="22.5" text-anchor="middle">Postman</text>
        <rect class="pill-sub" x="606" y="0" width="60" height="34"/><text class="pill-lbl" x="636" y="22.5" text-anchor="middle">Vite</text>
        <rect class="pill-sub" x="676" y="0" width="82" height="34"/><text class="pill-lbl" x="717" y="22.5" text-anchor="middle">Railway</text>
        <rect class="pill-sub" x="768" y="0" width="76" height="34"/><text class="pill-lbl" x="806" y="22.5" text-anchor="middle">Vercel</text>
      </g>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/tech-card.svg', 'w', encoding='utf-8') as f:
    f.write(tech_svg)
print('Wrote assets/tech-card.svg')

# -------------------------------------------------------------
# 5. assets/footer-card.svg
# -------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240" role="img" aria-label="Easir Iqbal Mahi — Signature">
  <defs>
    <linearGradient id="foot-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#17060A"/>
      <stop offset="100%" stop-color="#0A0205"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="220" rx="24" fill="url(#foot-bg)" stroke="#991B1B" stroke-width="2.5"/>

  <g transform="translate(0, 36)" text-anchor="middle">
    <!-- Signature -->
    <text class="t-bold" x="600" y="56" font-size="52" fill="#FFFFFF">Easir<tspan fill="#EF4444">.</tspan></text>
    
    <!-- Tagline -->
    <text class="t-mono" x="600" y="96" font-size="15" letter-spacing="2.5" fill="#EF4444">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>

    <!-- Quote -->
    <text class="t-bold" x="600" y="142" font-size="17" fill="#FFFFFF">“I don’t seek approval, I seek superiority then I build until reality has no choice but to agree.”</text>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/footer-card.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
print('Wrote assets/footer-card.svg')
