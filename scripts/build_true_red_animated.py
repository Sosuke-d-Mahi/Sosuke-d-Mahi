import base64
import os

with open('G:/HYML/Sushmitadasari/assets/avatar.png', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

# 1. assets/hero-portrait.svg with COOL ANIMATIONS & TRUE RED
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="1200" height="440" role="img" aria-label="Easir Iqbal Mahi — Full-stack Software Developer &amp; Founder @ Lagbeto">
  <defs>
    <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#18070B"/>
      <stop offset="50%" stop-color="#100507"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#FF2A42" stop-opacity="0.32">
        <animate attributeName="stop-opacity" values="0.2;0.42;0.2" dur="3.5s" repeatCount="indefinite" />
      </stop>
      <stop offset="60%" stop-color="#DC2626" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="laser-beam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#DC2626" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FF334B" stop-opacity="1"/>
      <stop offset="100%" stop-color="#DC2626" stop-opacity="0"/>
    </linearGradient>
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
      .t-white {{ fill: #FFFFFF; }}
      .t-red {{ fill: #FF334B; }}
      .pill-tag {{ fill: #20070C; stroke: #DC2626; stroke-width: 1.5; rx: 10; }}
      .pill-txt {{ font-family: system-ui, sans-serif; font-size: 14px; font-weight: 700; fill: #FFFFFF; }}
      
      @keyframes pulse-border {{
        0%, 100% {{ stroke-opacity: 0.65; }}
        50% {{ stroke-opacity: 1; stroke-width: 2.8px; }}
      }}
      .animated-border {{
        animation: pulse-border 3s ease-in-out infinite;
      }}
      @keyframes float-subtle {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-4px); }}
      }}
      .floating-card {{
        animation: float-subtle 4s ease-in-out infinite;
      }}
    </style>
  </defs>

  <!-- Background with ambient glow -->
  <rect x="10" y="10" width="1180" height="420" rx="24" fill="url(#hero-bg)" stroke="#DC2626" stroke-width="2" class="animated-border"/>
  <rect x="10" y="10" width="1180" height="420" rx="24" fill="url(#hero-glow)"/>

  <!-- Animated scanning light bar across top -->
  <rect x="40" y="12" width="180" height="2" fill="url(#laser-beam)">
    <animate attributeName="x" values="40;980;40" dur="6s" repeatCount="indefinite" ease="easeInOut"/>
  </rect>

  <!-- Left Info Column -->
  <g transform="translate(56, 50)">
    <!-- Eyebrow (No slashes!) -->
    <g>
      <circle cx="6" cy="6" r="5" fill="#FF334B" filter="url(#neon-glow)">
        <animate attributeName="r" values="4;6;4" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;0.6;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2.2" fill="#FF334B">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>
    </g>

    <!-- Main Title -->
    <text class="t-bold t-white" x="0" y="72" font-size="52">Easir Iqbal</text>
    <text class="t-bold" x="0" y="128" font-size="52" fill="#FFFFFF">Mahi<tspan fill="#FF334B" filter="url(#neon-glow)">.</tspan></text>

    <!-- Stack Subtitle -->
    <rect x="0" y="152" width="710" height="42" rx="10" fill="#1C060A" stroke="#DC2626" stroke-width="1.4"/>
    <text class="t-mono" x="20" y="178" font-size="14.5" fill="#FFFFFF">TypeScript • Python • Go • Nodejs • JavaScript • Java • Flutter • Kotlin</text>

    <!-- Quote Box -->
    <g transform="translate(0, 214)">
      <rect x="0" y="0" width="710" height="68" rx="14" fill="#170508" stroke="#FF334B" stroke-width="1.6"/>
      <text class="t-bold t-red" x="20" y="29" font-size="16.5">“I don’t seek approval, I seek superiority</text>
      <text class="t-bold t-white" x="20" y="53" font-size="16.5">then I build until reality has no choice but to agree.”</text>
    </g>

    <!-- Quick Highlights -->
    <g transform="translate(0, 304)">
      <g>
        <rect class="pill-tag" x="0" y="0" width="220" height="34"/>
        <text class="pill-txt" x="110" y="22" text-anchor="middle">Startup: Founder @ Lagbeto</text>
      </g>
      <g transform="translate(234, 0)">
        <rect class="pill-tag" x="0" y="0" width="220" height="34"/>
        <text class="pill-txt" x="110" y="22" text-anchor="middle">Featured: api-docs.git</text>
      </g>
      <g transform="translate(468, 0)">
        <rect class="pill-tag" x="0" y="0" width="242" height="34"/>
        <text class="pill-txt" x="121" y="22" text-anchor="middle">Passions: Game Modding</text>
      </g>
    </g>
  </g>

  <!-- Right Avatar Card (Floating Animation) -->
  <g transform="translate(830, 48)" class="floating-card">
    <rect x="0" y="0" width="314" height="344" rx="20" fill="#140508" stroke="#DC2626" stroke-width="2"/>
    
    <!-- Photo Frame -->
    <clipPath id="avatar-clip">
      <rect x="18" y="18" width="278" height="250" rx="14"/>
    </clipPath>
    <image href="data:image/png;base64,{avatar_b64}" x="18" y="18" width="278" height="250" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>
    <rect x="18" y="18" width="278" height="250" rx="14" fill="none" stroke="#FF334B" stroke-width="1.8"/>

    <!-- Bottom label with pulsing live indicator -->
    <rect x="18" y="282" width="278" height="44" rx="10" fill="#20070C" stroke="#DC2626" stroke-width="1.4"/>
    <circle cx="40" cy="304" r="4.5" fill="#FF334B">
      <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <text class="t-bold t-white" x="160" y="309" text-anchor="middle" font-size="15">Easir Iqbal Mahi · Founder</text>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/hero-portrait.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
print('Wrote assets/hero-portrait.svg')

# 2. assets/about-card.svg
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-label="About Easir Iqbal Mahi">
  <defs>
    <linearGradient id="card-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#18070B"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .box-dark { fill: #1D070C; stroke: #DC2626; stroke-width: 1.5; rx: 16; }
      .sub-silver { fill: #E2E8F0; }
      @keyframes pulse-dot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
      }
      .anim-dot { animation: pulse-dot 2s infinite ease-in-out; transform-origin: center; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="380" rx="24" fill="url(#card-bg)" stroke="#DC2626" stroke-width="2"/>

  <!-- Header (No slashes!) -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#FF334B" class="anim-dot"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#FF334B">ABOUT ME &amp; VENTURE</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Currently Building &amp; <tspan fill="#FF334B">Exploring.</tspan></text>
  </g>

  <!-- 4 Grid Blocks -->
  <g transform="translate(56, 126)">
    <!-- Box 1 -->
    <g>
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#FF334B">CURRENTLY WORKING AT</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Founder of my own Startup called Lagbeto</text>
      <text class="t-bold sub-silver" x="24" y="90" font-size="14">Leading platform engineering &amp; mobile development</text>
    </g>

    <!-- Box 2 -->
    <g transform="translate(560, 0)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#FF334B">LEARNING</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Talking face to face skill :)</text>
      <text class="t-bold sub-silver" x="24" y="90" font-size="14">Interpersonal communication &amp; live tech discussions</text>
    </g>

    <!-- Box 3 -->
    <g transform="translate(0, 124)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#FF334B">LOOKING TO COLLABORATE ON</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Pro Full-stack Developers</text>
      <text class="t-bold sub-silver" x="24" y="90" font-size="14">Partnering with elite devs on scalable systems</text>
    </g>

    <!-- Box 4 -->
    <g transform="translate(560, 124)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#FF334B">IN MY FREE TIME</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Love playing games and modding those games ^_~</text>
      <text class="t-bold sub-silver" x="24" y="90" font-size="14">Engine reverse engineering &amp; memory hooking</text>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/about-card.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)
print('Wrote assets/about-card.svg')

# 3. assets/projects-card.svg
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-label="Featured Projects of Easir Iqbal Mahi">
  <defs>
    <linearGradient id="proj-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#18070B"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .proj-box { fill: #1D070C; stroke: #DC2626; stroke-width: 1.6; rx: 18; }
      .tag-pill { fill: #2B0B13; stroke: #FF334B; stroke-width: 1.2; rx: 8; }
      .tag-txt { font-family: system-ui, sans-serif; font-size: 13.5px; font-weight: 700; fill: #FFFFFF; }
      .badge-bg { fill: #DC2626; rx: 6; }
      .sub-silver { fill: #E2E8F0; }
      @keyframes pulse-border {
        0%, 100% { stroke-opacity: 0.7; }
        50% { stroke-opacity: 1; stroke-width: 2.2px; }
      }
      .glow-box { animation: pulse-border 3s ease-in-out infinite; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="400" rx="24" fill="url(#proj-bg)" stroke="#DC2626" stroke-width="2"/>

  <!-- Header (No slashes!) -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#FF334B"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#FF334B">FEATURED WORK &amp; VENTURE</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Products, not <tspan fill="#FF334B">assignments.</tspan></text>
  </g>

  <!-- 2 Project Cards Side-by-Side -->
  <g transform="translate(56, 126)">
    <!-- Project 1: api-docs -->
    <g class="glow-box">
      <rect class="proj-box" x="0" y="0" width="525" height="234"/>
      <!-- Badge -->
      <rect class="badge-bg" x="24" y="24" width="144" height="26"/>
      <text class="t-mono" x="96" y="41.5" text-anchor="middle" font-size="12" fill="#FFFFFF">FEATURED PROJECT</text>
      
      <text class="t-bold" x="24" y="86" font-size="28" fill="#FFFFFF">api-docs</text>
      <text class="t-mono" x="24" y="112" font-size="13" fill="#FF334B">https://github.com/Sosuke-d-Mahi/api-docs.git</text>
      
      <text class="t-bold" x="24" y="146" font-size="15.5" fill="#FFFFFF">Interactive developer documentation engine &amp; sandbox</text>
      <text class="t-bold sub-silver" x="24" y="170" font-size="14">Real-time schema testing, automated spec parsing, zero-friction docs.</text>

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
      <rect class="proj-box" x="0" y="0" width="525" height="234"/>
      <!-- Badge -->
      <rect class="badge-bg" x="24" y="24" width="130" height="26"/>
      <text class="t-mono" x="89" y="41.5" text-anchor="middle" font-size="12" fill="#FFFFFF">STARTUP VENTURE</text>
      
      <text class="t-bold" x="24" y="86" font-size="28" fill="#FFFFFF">Lagbeto Platform</text>
      <text class="t-mono" x="24" y="112" font-size="13" fill="#FF334B">Founder &amp; Platform Architecture</text>
      
      <text class="t-bold" x="24" y="146" font-size="15.5" fill="#FFFFFF">Multi-service backend platform &amp; Flutter mobile app</text>
      <text class="t-bold sub-silver" x="24" y="170" font-size="14">High-concurrency Go services, PostgreSQL, and cross-platform mobile client.</text>

      <!-- Tags -->
      <g transform="translate(24, 186)">
        <rect class="tag-pill" x="0" y="0" width="54" height="28"/><text class="tag-txt" x="27" y="18.5" text-anchor="middle">Go</text>
        <rect class="tag-pill" x="64" y="0" width="80" height="28"/><text class="tag-txt" x="104" y="18.5" text-anchor="middle">Flutter</text>
        <rect class="tag-pill" x="154" y="0" width="102" height="28"/><text class="tag-txt" x="205" y="18.5" text-anchor="middle">PostgreSQL</text>
        <rect class="tag-pill" x="266" y="0" width="80" height="28"/><text class="tag-txt" x="306" y="18.5" text-anchor="middle">Docker</text>
      </g>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/projects-card.svg', 'w', encoding='utf-8') as f:
    f.write(projects_svg)
print('Wrote assets/projects-card.svg')

# 4. assets/tech-card.svg
tech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 430" width="1200" height="430" role="img" aria-label="Tech Stack of Easir Iqbal Mahi">
  <defs>
    <linearGradient id="tech-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#18070B"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .cat-lbl { font-family: "JetBrains Mono", monospace; font-size: 13.5px; font-weight: 700; fill: #FF334B; letter-spacing: 1.5px; }
      .pill-primary { fill: #2B0B13; stroke: #DC2626; stroke-width: 1.5; rx: 9; }
      .pill-sub { fill: #1C070C; stroke: #991B1B; stroke-width: 1.2; rx: 9; }
      .pill-lbl { font-family: system-ui, sans-serif; font-size: 14.5px; font-weight: 700; fill: #FFFFFF; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="410" rx="24" fill="url(#tech-bg)" stroke="#DC2626" stroke-width="2"/>

  <!-- Header (No slashes!) -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#FF334B"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#FF334B">TECH STACK &amp; TOOLKIT</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Languages &amp; Technologies I Build With</text>
  </g>

  <!-- Categories -->
  <g transform="translate(56, 126)">
    <!-- Row 1: Core Languages -->
    <g transform="translate(0, 0)">
      <text class="cat-lbl" x="0" y="23">CORE STACK</text>
      <g transform="translate(190, 0)">
        <rect class="pill-primary" x="0" y="0" width="110" height="34"/><text class="pill-lbl" x="55" y="22.5" text-anchor="middle">TypeScript</text>
        <rect class="pill-primary" x="120" y="0" width="86" height="34"/><text class="pill-lbl" x="163" y="22.5" text-anchor="middle">Python</text>
        <rect class="pill-primary" x="216" y="0" width="56" height="34"/><text class="pill-lbl" x="244" y="22.5" text-anchor="middle">Go</text>
        <rect class="pill-primary" x="282" y="0" width="88" height="34"/><text class="pill-lbl" x="326" y="22.5" text-anchor="middle">Node.js</text>
        <rect class="pill-primary" x="380" y="0" width="108" height="34"/><text class="pill-lbl" x="434" y="22.5" text-anchor="middle">JavaScript</text>
        <rect class="pill-primary" x="498" y="0" width="66" height="34"/><text class="pill-lbl" x="531" y="22.5" text-anchor="middle">Java</text>
        <rect class="pill-primary" x="574" y="0" width="82" height="34"/><text class="pill-lbl" x="615" y="22.5" text-anchor="middle">Flutter</text>
        <rect class="pill-primary" x="666" y="0" width="76" height="34"/><text class="pill-lbl" x="704" y="22.5" text-anchor="middle">Kotlin</text>
        <rect class="pill-sub" x="752" y="0" width="62" height="34"/><text class="pill-lbl" x="783" y="22.5" text-anchor="middle">Dart</text>
        <rect class="pill-sub" x="824" y="0" width="60" height="34"/><text class="pill-lbl" x="854" y="22.5" text-anchor="middle">C++</text>
      </g>
    </g>

    <!-- Row 2: Frontend & Mobile -->
    <g transform="translate(0, 56)">
      <text class="cat-lbl" x="0" y="23">FRONTEND &amp; UI</text>
      <g transform="translate(190, 0)">
        <rect class="pill-primary" x="0" y="0" width="76" height="34"/><text class="pill-lbl" x="38" y="22.5" text-anchor="middle">React</text>
        <rect class="pill-primary" x="86" y="0" width="86" height="34"/><text class="pill-lbl" x="129" y="22.5" text-anchor="middle">Next.js</text>
        <rect class="pill-primary" x="182" y="0" width="114" height="34"/><text class="pill-lbl" x="239" y="22.5" text-anchor="middle">TailwindCSS</text>
        <rect class="pill-sub" x="306" y="0" width="80" height="34"/><text class="pill-lbl" x="346" y="22.5" text-anchor="middle">Vue.js</text>
        <rect class="pill-sub" x="396" y="0" width="86" height="34"/><text class="pill-lbl" x="439" y="22.5" text-anchor="middle">Angular</text>
        <rect class="pill-sub" x="492" y="0" width="70" height="34"/><text class="pill-lbl" x="527" y="22.5" text-anchor="middle">Astro</text>
        <rect class="pill-sub" x="572" y="0" width="102" height="34"/><text class="pill-lbl" x="623" y="22.5" text-anchor="middle">Bootstrap</text>
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

# 5. assets/footer-card.svg
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240" role="img" aria-label="Easir Iqbal Mahi — Signature">
  <defs>
    <linearGradient id="foot-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#18070B"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      @keyframes neon-pulse {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; filter: drop-shadow(0 0 8px #FF334B); }
      }
      .anim-sig { animation: neon-pulse 3s infinite ease-in-out; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="220" rx="24" fill="url(#foot-bg)" stroke="#DC2626" stroke-width="2"/>

  <g transform="translate(0, 36)" text-anchor="middle">
    <!-- Signature -->
    <text class="t-bold anim-sig" x="600" y="56" font-size="52" fill="#FFFFFF">Easir<tspan fill="#FF334B">.</tspan></text>
    
    <!-- Tagline (No slashes!) -->
    <text class="t-mono" x="600" y="96" font-size="14.5" letter-spacing="2.5" fill="#FF334B">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>

    <!-- Quote -->
    <text class="t-bold" x="600" y="142" font-size="17" fill="#FFFFFF">“I don’t seek approval, I seek superiority then I build until reality has no choice but to agree.”</text>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/footer-card.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
print('Wrote assets/footer-card.svg')
