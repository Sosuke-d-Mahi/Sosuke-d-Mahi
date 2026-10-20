import base64
import os

with open('G:/HYML/Sushmitadasari/assets/avatar.png', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

# 1. assets/hero-portrait.svg
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="1200" height="440" role="img" aria-label="Easir Iqbal Mahi — Full-stack Software Developer &amp; Founder @ Lagbeto">
  <defs>
    <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1E0D17"/>
      <stop offset="50%" stop-color="#140910"/>
      <stop offset="100%" stop-color="#0E050B"/>
    </linearGradient>
    <radialGradient id="hero-glow" cx="80%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#941F4D" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#701A3D" stop-opacity="0"/>
    </radialGradient>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
      .t-white {{ fill: #FFFFFF; }}
      .t-accent {{ fill: #E5B5C7; }}
      .pill-tag {{ fill: #240F1D; stroke: #701A3D; stroke-width: 1.4; rx: 10; }}
      .pill-txt {{ font-family: system-ui, sans-serif; font-size: 14px; font-weight: 700; fill: #FFFFFF; }}
    </style>
  </defs>

  <!-- Background -->
  <rect x="10" y="10" width="1180" height="420" rx="24" fill="url(#hero-bg)" stroke="#701A3D" stroke-width="2.5"/>
  <rect x="10" y="10" width="1180" height="420" rx="24" fill="url(#hero-glow)"/>

  <!-- Left Info Column -->
  <g transform="translate(56, 50)">
    <!-- Eyebrow -->
    <g>
      <circle cx="6" cy="6" r="5" fill="#E5B5C7"/>
      <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#E5B5C7">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>
    </g>

    <!-- Main Title -->
    <text class="t-bold t-white" x="0" y="70" font-size="52">Easir Iqbal</text>
    <text class="t-bold" x="0" y="126" font-size="52" fill="#FFFFFF">Mahi<tspan fill="#E5B5C7">.</tspan></text>

    <!-- Stack Subtitle -->
    <rect x="0" y="152" width="710" height="40" rx="10" fill="#240F1D" stroke="#701A3D" stroke-width="1.2"/>
    <text class="t-mono" x="20" y="177" font-size="14.5" fill="#FFFFFF">TypeScript • Python • Go • Nodejs • JavaScript • Java • Flutter • Kotlin</text>

    <!-- Quote -->
    <g transform="translate(0, 214)">
      <rect x="0" y="0" width="710" height="66" rx="14" fill="#1A0A14" stroke="#941F4D" stroke-width="1.4"/>
      <text class="t-bold" x="20" y="28" font-size="16.5" fill="#E5B5C7">“I don’t seek approval, I seek superiority</text>
      <text class="t-bold t-white" x="20" y="52" font-size="16.5">then I build until reality has no choice but to agree.”</text>
    </g>

    <!-- Quick highlights -->
    <g transform="translate(0, 302)">
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

  <!-- Right Avatar Card -->
  <g transform="translate(830, 48)">
    <rect x="0" y="0" width="314" height="344" rx="20" fill="#1A0B15" stroke="#701A3D" stroke-width="2"/>
    <!-- Photo Frame -->
    <clipPath id="avatar-clip">
      <rect x="18" y="18" width="278" height="250" rx="14"/>
    </clipPath>
    <image href="data:image/png;base64,{avatar_b64}" x="18" y="18" width="278" height="250" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>
    <rect x="18" y="18" width="278" height="250" rx="14" fill="none" stroke="#941F4D" stroke-width="1.5"/>

    <!-- Bottom label -->
    <rect x="18" y="282" width="278" height="44" rx="10" fill="#291120" stroke="#701A3D" stroke-width="1.2"/>
    <text class="t-bold t-white" x="157" y="309" text-anchor="middle" font-size="15">Easir Iqbal Mahi · Founder</text>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/hero-portrait.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
print('Wrote assets/hero-portrait.svg')

# 2. assets/about-card.svg
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" role="img" aria-label="About Easir Iqbal Mahi">
  <defs>
    <linearGradient id="card-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1A0C16"/>
      <stop offset="100%" stop-color="#10070D"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .box-dark { fill: #220F1D; stroke: #701A3D; stroke-width: 1.5; rx: 16; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="380" rx="24" fill="url(#card-bg)" stroke="#701A3D" stroke-width="2.5"/>

  <!-- Header -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#E5B5C7"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#E5B5C7">01 / ABOUT ME &amp; VENTURE</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Currently Building &amp; <tspan fill="#E5B5C7">Exploring.</tspan></text>
  </g>

  <!-- 4 Grid Blocks -->
  <g transform="translate(56, 126)">
    <!-- Box 1 -->
    <g>
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#E5B5C7">CURRENTLY WORKING AT</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Founder of my own Startup called Lagbeto</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#C77B9B">Leading platform engineering &amp; mobile development</text>
    </g>

    <!-- Box 2 -->
    <g transform="translate(560, 0)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#E5B5C7">LEARNING</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Talking face to face skill :)</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#C77B9B">Interpersonal communication &amp; live tech discussions</text>
    </g>

    <!-- Box 3 -->
    <g transform="translate(0, 124)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#E5B5C7">LOOKING TO COLLABORATE ON</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Pro Full-stack Developers</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#C77B9B">Partnering with elite devs on scalable systems</text>
    </g>

    <!-- Box 4 -->
    <g transform="translate(560, 124)">
      <rect class="box-dark" x="0" y="0" width="525" height="106"/>
      <text class="t-mono" x="24" y="32" font-size="13" letter-spacing="1.5" fill="#E5B5C7">IN MY FREE TIME</text>
      <text class="t-bold" x="24" y="66" font-size="19" fill="#FFFFFF">Love playing games and modding those games ^_~</text>
      <text class="t-bold" x="24" y="90" font-size="14" fill="#C77B9B">Engine reverse engineering &amp; memory hooking</text>
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
      <stop offset="0%" stop-color="#1A0C16"/>
      <stop offset="100%" stop-color="#10070D"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .proj-box { fill: #200E1B; stroke: #701A3D; stroke-width: 1.6; rx: 18; }
      .tag-pill { fill: #311328; stroke: #941F4D; stroke-width: 1.2; rx: 8; }
      .tag-txt { font-family: system-ui, sans-serif; font-size: 13.5px; font-weight: 700; fill: #FFFFFF; }
      .badge-bg { fill: #941F4D; rx: 6; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="400" rx="24" fill="url(#proj-bg)" stroke="#701A3D" stroke-width="2.5"/>

  <!-- Header -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#E5B5C7"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#E5B5C7">02 / FEATURED WORK &amp; VENTURE</text>
    <text class="t-bold" x="0" y="52" font-size="34" fill="#FFFFFF">Products, not <tspan fill="#E5B5C7">assignments.</tspan></text>
  </g>

  <!-- 2 Project Cards Side-by-Side -->
  <g transform="translate(56, 126)">
    <!-- Project 1: api-docs -->
    <g>
      <rect class="proj-box" x="0" y="0" width="525" height="234"/>
      <!-- Badge -->
      <rect class="badge-bg" x="24" y="24" width="144" height="26"/>
      <text class="t-mono" x="96" y="41.5" text-anchor="middle" font-size="12" fill="#FFFFFF">FEATURED PROJECT</text>
      
      <text class="t-bold" x="24" y="86" font-size="28" fill="#FFFFFF">api-docs</text>
      <text class="t-mono" x="24" y="112" font-size="13" fill="#E5B5C7">https://github.com/Sosuke-d-Mahi/api-docs.git</text>
      
      <text class="t-bold" x="24" y="146" font-size="15.5" fill="#F8F0F3">Interactive developer documentation engine &amp; sandbox</text>
      <text class="t-bold" x="24" y="170" font-size="14" fill="#C77B9B">Real-time schema testing, automated spec parsing, zero-friction docs.</text>

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
      <text class="t-mono" x="24" y="112" font-size="13" fill="#E5B5C7">Founder &amp; Platform Architecture</text>
      
      <text class="t-bold" x="24" y="146" font-size="15.5" fill="#F8F0F3">Multi-service backend platform &amp; Flutter mobile app</text>
      <text class="t-bold" x="24" y="170" font-size="14" fill="#C77B9B">High-concurrency Go services, PostgreSQL, and cross-platform mobile client.</text>

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
      <stop offset="0%" stop-color="#1A0C16"/>
      <stop offset="100%" stop-color="#10070D"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
      .cat-lbl { font-family: "JetBrains Mono", monospace; font-size: 13.5px; font-weight: 700; fill: #E5B5C7; letter-spacing: 1.5px; }
      .pill-primary { fill: #38122B; stroke: #941F4D; stroke-width: 1.5; rx: 9; }
      .pill-sub { fill: #200E1C; stroke: #701A3D; stroke-width: 1.2; rx: 9; }
      .pill-lbl { font-family: system-ui, sans-serif; font-size: 14.5px; font-weight: 700; fill: #FFFFFF; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="410" rx="24" fill="url(#tech-bg)" stroke="#701A3D" stroke-width="2.5"/>

  <!-- Header -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#E5B5C7"/>
    <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#E5B5C7">03 / TECH STACK &amp; TOOLKIT</text>
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
      <stop offset="0%" stop-color="#1A0C16"/>
      <stop offset="100%" stop-color="#10070D"/>
    </linearGradient>
    <style>
      .t-bold { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
      .t-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
    </style>
  </defs>

  <rect x="10" y="10" width="1180" height="220" rx="24" fill="url(#foot-bg)" stroke="#701A3D" stroke-width="2.5"/>

  <g transform="translate(0, 36)" text-anchor="middle">
    <!-- Signature -->
    <text class="t-bold" x="600" y="56" font-size="52" fill="#FFFFFF">Easir<tspan fill="#E5B5C7">.</tspan></text>
    
    <!-- Tagline -->
    <text class="t-mono" x="600" y="96" font-size="14.5" letter-spacing="2.5" fill="#E5B5C7">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>

    <!-- Quote -->
    <text class="t-bold" x="600" y="142" font-size="17" fill="#FFFFFF">“I don’t seek approval, I seek superiority then I build until reality has no choice but to agree.”</text>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/footer-card.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
print('Wrote assets/footer-card.svg')
