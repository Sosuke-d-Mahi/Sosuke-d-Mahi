import base64
import os

with open('G:/HYML/Sushmitadasari/assets/avatar.png', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

# -------------------------------------------------------------
# 1. assets/hero-portrait.svg
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450" role="img" aria-label="Easir Iqbal Mahi — Full-stack Software Developer &amp; Founder @ Lagbeto">
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
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
      .t-white {{ fill: #FFFFFF; }}
      .t-red {{ fill: #EF4444; }}
      .t-sub {{ fill: #FECACA; }}
      .pill-tag {{ fill: #1F070C; stroke: #991B1B; stroke-width: 1.5; rx: 10; }}
      .pill-txt {{ font-family: system-ui, sans-serif; font-size: 14.5px; font-weight: 700; fill: #FFFFFF; }}
    </style>
  </defs>

  <!-- Background -->
  <rect x="10" y="10" width="1180" height="430" rx="24" fill="url(#hero-bg)" stroke="#991B1B" stroke-width="2.5"/>
  <rect x="10" y="10" width="1180" height="430" rx="24" fill="url(#hero-glow)"/>

  <!-- Left Info Column -->
  <g transform="translate(56, 48)">
    <!-- Eyebrow -->
    <g>
      <circle cx="6" cy="6" r="5" fill="#EF4444"/>
      <text class="t-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#EF4444">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>
    </g>

    <!-- Main Title -->
    <text class="t-bold t-white" x="0" y="72" font-size="54">Easir Iqbal</text>
    <text class="t-bold" x="0" y="130" font-size="54" fill="#FFFFFF">Mahi<tspan fill="#EF4444">.</tspan></text>

    <!-- Stack Subtitle -->
    <rect x="0" y="156" width="710" height="42" rx="10" fill="#1C060B" stroke="#991B1B" stroke-width="1.2"/>
    <text class="t-mono" x="20" y="182" font-size="15" fill="#FFFFFF">TypeScript • Python • Go • Nodejs • JavaScript • Java • Flutter • Kotlin</text>

    <!-- Philosophy Quote -->
    <g transform="translate(0, 218)">
      <rect x="0" y="0" width="710" height="70" rx="14" fill="#170509" stroke="#DC2626" stroke-width="1.4"/>
      <text class="t-bold" x="22" y="29" font-size="17" fill="#EF4444">“I don’t seek approval, I seek superiority</text>
      <text class="t-bold t-white" x="22" y="55" font-size="17">then I build until reality has no choice but to agree.”</text>
    </g>

    <!-- Quick Highlights -->
    <g transform="translate(0, 308)">
      <g>
        <rect class="pill-tag" x="0" y="0" width="224" height="36"/>
        <text class="pill-txt" x="112" y="23" text-anchor="middle">Startup: Founder @ Lagbeto</text>
      </g>
      <g transform="translate(238, 0)">
        <rect class="pill-tag" x="0" y="0" width="224" height="36"/>
        <text class="pill-txt" x="112" y="23" text-anchor="middle">Featured: api-docs.git</text>
      </g>
      <g transform="translate(476, 0)">
        <rect class="pill-tag" x="0" y="0" width="234" height="36"/>
        <text class="pill-txt" x="117" y="23" text-anchor="middle">Passions: Game Modding</text>
      </g>
    </g>
  </g>

  <!-- Right Avatar Card -->
  <g transform="translate(830, 48)">
    <rect x="0" y="0" width="314" height="354" rx="20" fill="#1A070E" stroke="#991B1B" stroke-width="2"/>
    <!-- Photo Frame -->
    <clipPath id="avatar-clip">
      <rect x="18" y="18" width="278" height="260" rx="14"/>
    </clipPath>
    <image href="data:image/png;base64,{avatar_b64}" x="18" y="18" width="278" height="260" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>
    <rect x="18" y="18" width="278" height="260" rx="14" fill="none" stroke="#DC2626" stroke-width="1.5"/>

    <!-- Bottom label -->
    <rect x="18" y="292" width="278" height="44" rx="10" fill="#240A12" stroke="#991B1B" stroke-width="1.2"/>
    <text class="t-bold t-white" x="157" y="320" text-anchor="middle" font-size="16">Easir Iqbal Mahi · Founder</text>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/hero-portrait.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
print('Wrote assets/hero-portrait.svg')

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
        <rect class="tag-pill" x="156" y="0" width="98" height="28"/><text class="tag-txt" x="205" y="18.5" text-anchor="middle">PostgreSQL</text>
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
        <rect class="pill-sub" x="703" y="0" width="70" height="34"/><text class="pill-lbl" x="738" y="22.5" text-anchor="middle">C / C++</text>
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

# Wait, in Row 1: replace 'C / C++' with 'C, C++' so there is NO slash at all!
tech_svg = tech_svg.replace('>C / C++<', '>C, C++<')

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
