import base64
import os

with open('G:/HYML/Sushmitadasari/assets/avatar.png', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

RADAR_PULSE = '''
    <circle cx="6" cy="6" r="4" fill="#DC2626"/>
    <circle cx="6" cy="6" r="4" fill="none" stroke="#DC2626" stroke-width="1.5">
      <animate attributeName="r" values="4;10;4" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0.8" dur="2.4s" repeatCount="indefinite"/>
    </circle>
'''

# -------------------------------------------------------------
# 1. assets/hero-portrait.svg
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 470" width="1200" height="470" role="img" aria-label="Easir Iqbal Mahi — Full-stack Software Developer &amp; Founder @ Lagbeto">
  <defs>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-semi {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 600; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
    </style>
  </defs>

  <!-- Charcoal Card Canvas -->
  <rect x="8" y="8" width="1184" height="454" rx="20" fill="#0C0D11" stroke="#222329" stroke-width="1.5"/>

  <!-- Top Header Bar -->
  <g transform="translate(48, 42)">
    <!-- Left: Live pulse + Tagline -->
    <g transform="translate(0, 0)">
      {RADAR_PULSE}
      <text class="t-mono" x="22" y="10" font-size="12.5" letter-spacing="1.8" fill="#E4E4E7">BUILD · CREATE · IMPROVE</text>
    </g>

    <!-- Right: Location -->
    <g transform="translate(940, 0)">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" fill="#DC2626" transform="translate(0, -3) scale(0.7)"/>
      <text class="t-mono" x="20" y="10" font-size="12.5" letter-spacing="1.5" fill="#A1A1AA">RAJSHAHI, BD</text>
    </g>
  </g>

  <!-- Left Content Column -->
  <g transform="translate(48, 92)">
    <!-- Main Display Typography -->
    <text class="t-bold" x="0" y="52" font-size="56" fill="#FFFFFF" letter-spacing="-0.5">Easir Iqbal</text>
    <text class="t-bold" x="0" y="112" font-size="56" fill="#DC2626" letter-spacing="-0.5">Mahi<tspan fill="#FFFFFF">.</tspan></text>

    <!-- Subtitle Role -->
    <text class="t-mono" x="0" y="142" font-size="12.5" letter-spacing="1.6" fill="#A1A1AA">FULL-STACK SOFTWARE DEVELOPER  •  FOUNDER @ LAGBETO</text>

    <!-- Editorial Quote with Left Red Accent Bar -->
    <g transform="translate(0, 168)">
      <line x1="0" y1="4" x2="0" y2="46" stroke="#DC2626" stroke-width="3" stroke-linecap="round"/>
      <text class="t-bold" x="16" y="23" font-size="16" fill="#FFFFFF">I don’t seek approval. I seek superiority,</text>
      <text class="t-semi" x="16" y="45" font-size="16" fill="#A1A1AA">then I build until reality agrees.</text>
    </g>

    <!-- Tech Strip -->
    <g transform="translate(0, 240)">
      <rect x="0" y="0" width="726" height="36" rx="8" fill="#14151B" stroke="#222329" stroke-width="1.2"/>
      <text class="t-mono" x="20" y="23" font-size="12" letter-spacing="1.6" fill="#D4D4D8">TYPESCRIPT   PYTHON   GO   NODE.JS   JAVASCRIPT   JAVA   FLUTTER   KOTLIN</text>
    </g>

    <!-- 3 Action Buttons -->
    <g transform="translate(0, 296)">
      <!-- Portfolio Button -->
      <g>
        <rect x="0" y="0" width="170" height="42" rx="8" fill="#881D2D" stroke="#A82337" stroke-width="1.2"/>
        <text class="t-mono" x="22" y="26" font-size="13" letter-spacing="1.2" fill="#FFFFFF">PORTFOLIO</text>
        <text class="t-mono" x="142" y="26" font-size="14" fill="#FFFFFF">↗</text>
      </g>

      <!-- GitHub Button -->
      <g transform="translate(182, 0)">
        <rect x="0" y="0" width="160" height="42" rx="8" fill="#14151B" stroke="#262730" stroke-width="1.2"/>
        <!-- GitHub icon -->
        <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="#FFFFFF" transform="translate(18, 12) scale(0.75)"/>
        <text class="t-mono" x="46" y="26" font-size="13" letter-spacing="1.2" fill="#FFFFFF">GITHUB</text>
        <text class="t-mono" x="134" y="26" font-size="14" fill="#FFFFFF">↗</text>
      </g>

      <!-- Email Button -->
      <g transform="translate(354, 0)">
        <rect x="0" y="0" width="160" height="42" rx="8" fill="#14151B" stroke="#262730" stroke-width="1.2"/>
        <!-- Mail icon -->
        <path d="M3 4h18a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm0 2v.511l9 5.625 9-5.625V6H3zm18 3.314-8.47 5.294a1 1 0 0 1-1.06 0L3 9.314V18h18V9.314z" fill="#FFFFFF" transform="translate(18, 12) scale(0.75)"/>
        <text class="t-mono" x="46" y="26" font-size="13" letter-spacing="1.2" fill="#FFFFFF">EMAIL</text>
        <text class="t-mono" x="134" y="26" font-size="14" fill="#FFFFFF">↗</text>
      </g>
    </g>
  </g>

  <!-- Right Avatar Frame (Clean Editorial Rect) -->
  <g transform="translate(826, 42)">
    <rect x="0" y="0" width="326" height="386" rx="16" fill="#121318" stroke="#23242B" stroke-width="1.5"/>
    <clipPath id="avatar-clip">
      <rect x="14" y="14" width="298" height="358" rx="12"/>
    </clipPath>
    <image href="data:image/png;base64,{avatar_b64}" x="14" y="14" width="298" height="358" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>
    <rect x="14" y="14" width="298" height="358" rx="12" fill="none" stroke="#2B2C35" stroke-width="1"/>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/hero-portrait.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
print('Wrote assets/hero-portrait.svg')

# -------------------------------------------------------------
# 2. assets/about-card.svg
# -------------------------------------------------------------
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="1200" height="450" role="img" aria-label="About Easir Iqbal Mahi">
  <defs>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-semi {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 600; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
    </style>
  </defs>

  <rect x="8" y="8" width="1184" height="434" rx="20" fill="#0C0D11" stroke="#222329" stroke-width="1.5"/>

  <!-- Top Header Bar -->
  <g transform="translate(48, 42)">
    <g transform="translate(0, 0)">
      {RADAR_PULSE}
      <text class="t-mono" x="22" y="10" font-size="12.5" letter-spacing="1.8" fill="#E4E4E7">01 · ABOUT ME &amp; VENTURE</text>
    </g>
    <text class="t-mono" x="1104" y="10" text-anchor="end" font-size="12.5" letter-spacing="1.8" fill="#71717A">FOCUS · BUILD · LEARN · PLAY</text>
  </g>

  <!-- Big Display Title -->
  <g transform="translate(48, 98)">
    <text class="t-bold" x="0" y="0" font-size="34" fill="#FFFFFF">Currently Building &amp; <tspan fill="#DC2626">Exploring.</tspan></text>
  </g>

  <!-- 4 Editorial Bento Blocks (2x2) -->
  <g transform="translate(48, 128)">
    <!-- Box 1: Founder @ Lagbeto -->
    <g>
      <rect x="0" y="0" width="536" height="108" rx="12" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Rocket Icon -->
      <g transform="translate(24, 28)">
        <circle cx="20" cy="20" r="18" fill="#1E2028"/>
        <path d="M19 5s-.5 2-2 3.5-3.5 2-3.5 2l-2-2 1.5-1.5L10 4 7 7l3 3-1.5 1.5-2-2s-.5 2-2 3.5S1 19 1 19s3.5-.5 5-2 2-3.5 2-3.5l-2-2 1.5-1.5L13 13l3-3-3-3 1.5-1.5 2 2s2-.5 3.5-2S19 5 19 5z" fill="#DC2626" transform="translate(10, 10) scale(0.9)"/>
      </g>
      <g transform="translate(80, 24)">
        <text class="t-mono" x="0" y="14" font-size="11.5" letter-spacing="1.4" fill="#DC2626">FOUNDER @ LAGBETO</text>
        <text class="t-bold" x="0" y="38" font-size="17" fill="#FFFFFF">Building a multi-service platform</text>
        <text class="t-semi" x="0" y="60" font-size="13.5" fill="#A1A1AA">Go backends, scalable systems &amp; Flutter mobile app.</text>
      </g>
    </g>

    <!-- Box 2: Game Modding & Internals -->
    <g transform="translate(568, 0)">
      <rect x="0" y="0" width="536" height="108" rx="12" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Gamepad Icon -->
      <g transform="translate(24, 28)">
        <circle cx="20" cy="20" r="18" fill="#1E2028"/>
        <path d="M21 6H3c-1.1 0-2 .9-2 2v8c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-10 7H8v3H6v-3H3v-2h3V8h2v3h3v2zm4.5 2c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm3-3c-.83 0-1.5-.67-1.5-1.5S17.67 9 18.5 9s1.5.67 1.5 1.5-.67 1.5-1.5 1.5z" fill="#DC2626" transform="translate(8, 10) scale(0.8)"/>
      </g>
      <g transform="translate(80, 24)">
        <text class="t-mono" x="0" y="14" font-size="11.5" letter-spacing="1.4" fill="#DC2626">GAME MODDING &amp; INTERNALS</text>
        <text class="t-bold" x="0" y="38" font-size="17" fill="#FFFFFF">Exploring game engine internals</text>
        <text class="t-semi" x="0" y="60" font-size="13.5" fill="#A1A1AA">Memory inspection, runtime patchers, and custom hooks.</text>
      </g>
    </g>

    <!-- Box 3: Collaboration -->
    <g transform="translate(0, 122)">
      <rect x="0" y="0" width="536" height="108" rx="12" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Users Icon -->
      <g transform="translate(24, 28)">
        <circle cx="20" cy="20" r="18" fill="#1E2028"/>
        <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z" fill="#DC2626" transform="translate(8, 10) scale(0.8)"/>
      </g>
      <g transform="translate(80, 24)">
        <text class="t-mono" x="0" y="14" font-size="11.5" letter-spacing="1.4" fill="#DC2626">COLLABORATION</text>
        <text class="t-bold" x="0" y="38" font-size="17" fill="#FFFFFF">Working with talented developers</text>
        <text class="t-semi" x="0" y="60" font-size="13.5" fill="#A1A1AA">Partnering on scalable products and open source tools.</text>
      </g>
    </g>

    <!-- Box 4: Learning -->
    <g transform="translate(568, 122)">
      <rect x="0" y="0" width="536" height="108" rx="12" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Book Icon -->
      <g transform="translate(24, 28)">
        <circle cx="20" cy="20" r="18" fill="#1E2028"/>
        <path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z" fill="#DC2626" transform="translate(10, 10) scale(0.8)"/>
      </g>
      <g transform="translate(80, 24)">
        <text class="t-mono" x="0" y="14" font-size="11.5" letter-spacing="1.4" fill="#DC2626">LEARNING</text>
        <text class="t-bold" x="0" y="38" font-size="17" fill="#FFFFFF">Constantly learning &amp; experimenting</text>
        <text class="t-semi" x="0" y="60" font-size="13.5" fill="#A1A1AA">New technologies, system design, and low-level concepts.</text>
      </g>
    </g>
  </g>

  <!-- Bottom Featured Badge Center -->
  <g transform="translate(440, 382)">
    <rect x="0" y="0" width="180" height="34" rx="8" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
    <text class="t-mono" x="20" y="22" font-size="11.5" letter-spacing="1.4" fill="#A1A1AA">📁 FEATURED PROJECT</text>
    
    <g transform="translate(190, 0)">
      <rect x="0" y="0" width="130" height="34" rx="8" fill="#881D2D" stroke="#A82337" stroke-width="1.2"/>
      <text class="t-mono" x="18" y="22" font-size="12" letter-spacing="1.2" fill="#FFFFFF">API-DOCS</text>
      <text class="t-mono" x="104" y="22" font-size="13" fill="#FFFFFF">↗</text>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/about-card.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)
print('Wrote assets/about-card.svg')

# -------------------------------------------------------------
# 3. assets/projects-card.svg
# -------------------------------------------------------------
projects_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-label="Featured Projects of Easir Iqbal Mahi">
  <defs>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-semi {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 600; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
      .pill-t {{ fill: #1E2028; rx: 6; }}
      .pill-lbl {{ font-family: system-ui, sans-serif; font-size: 12.5px; font-weight: 700; fill: #D4D4D8; }}
    </style>
  </defs>

  <rect x="8" y="8" width="1184" height="404" rx="20" fill="#0C0D11" stroke="#222329" stroke-width="1.5"/>

  <!-- Top Header Bar -->
  <g transform="translate(48, 42)">
    <g transform="translate(0, 0)">
      {RADAR_PULSE}
      <text class="t-mono" x="22" y="10" font-size="12.5" letter-spacing="1.8" fill="#E4E4E7">02 · SELECTED WORK &amp; SYSTEMS</text>
    </g>
    <text class="t-mono" x="1104" y="10" text-anchor="end" font-size="12.5" letter-spacing="1.8" fill="#71717A">PRODUCTS, NOT ASSIGNMENTS</text>
  </g>

  <!-- Title -->
  <g transform="translate(48, 98)">
    <text class="t-bold" x="0" y="0" font-size="34" fill="#FFFFFF">Built for <tspan fill="#DC2626">Scale</tspan>, Performance &amp; Precision.</text>
  </g>

  <!-- 3 Project Columns Side-by-Side -->
  <g transform="translate(48, 126)">
    <!-- Card 1: Lagbeto Platform -->
    <g>
      <rect x="0" y="0" width="348" height="240" rx="14" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Square Logo [ L ] -->
      <rect x="22" y="22" width="40" height="40" rx="8" fill="#881D2D"/>
      <text class="t-bold" x="42" y="48" text-anchor="middle" font-size="20" fill="#FFFFFF">L</text>
      
      <text class="t-bold" x="74" y="42" font-size="20" fill="#FFFFFF">Lagbeto</text>
      <text class="t-mono" x="312" y="42" text-anchor="end" font-size="16" fill="#A1A1AA">↗</text>

      <text class="t-semi" x="22" y="94" font-size="14.5" fill="#A1A1AA">Multi-service platform with Go backend and Flutter mobile app.</text>
      
      <!-- Tech Pills -->
      <g transform="translate(22, 178)">
        <rect class="pill-t" x="0" y="0" width="48" height="28"/><text class="pill-lbl" x="24" y="18.5" text-anchor="middle">Go</text>
        <rect class="pill-t" x="56" y="0" width="66" height="28"/><text class="pill-lbl" x="89" y="18.5" text-anchor="middle">Flutter</text>
        <rect class="pill-t" x="130" y="0" width="96" height="28"/><text class="pill-lbl" x="178" y="18.5" text-anchor="middle">PostgreSQL</text>
      </g>
    </g>

    <!-- Card 2: API Docs -->
    <g transform="translate(378, 0)">
      <rect x="0" y="0" width="348" height="240" rx="14" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Square Logo [ </> ] -->
      <rect x="22" y="22" width="40" height="40" rx="8" fill="#1E2028" stroke="#881D2D" stroke-width="1.5"/>
      <text class="t-mono" x="42" y="47" text-anchor="middle" font-size="16" fill="#DC2626">&lt;/&gt;</text>
      
      <text class="t-bold" x="74" y="42" font-size="20" fill="#FFFFFF">API Docs</text>
      <text class="t-mono" x="312" y="42" text-anchor="end" font-size="16" fill="#A1A1AA">↗</text>

      <text class="t-semi" x="22" y="94" font-size="14.5" fill="#A1A1AA">Clean and developer-friendly interactive API documentation.</text>

      <!-- Tech Pills -->
      <g transform="translate(22, 178)">
        <rect class="pill-t" x="0" y="0" width="70" height="28"/><text class="pill-lbl" x="35" y="18.5" text-anchor="middle">Next.js</text>
        <rect class="pill-t" x="78" y="0" width="94" height="28"/><text class="pill-lbl" x="125" y="18.5" text-anchor="middle">TypeScript</text>
        <rect class="pill-t" x="180" y="0" width="102" height="28"/><text class="pill-lbl" x="231" y="18.5" text-anchor="middle">Tailwind CSS</text>
      </g>
    </g>

    <!-- Card 3: Game Modding & Internals -->
    <g transform="translate(756, 0)">
      <rect x="0" y="0" width="348" height="240" rx="14" fill="#14151B" stroke="#23242B" stroke-width="1.2"/>
      <!-- Square Logo [ ⚙ ] -->
      <rect x="22" y="22" width="40" height="40" rx="8" fill="#881D2D"/>
      <text class="t-mono" x="42" y="47" text-anchor="middle" font-size="18" fill="#FFFFFF">⚙</text>
      
      <text class="t-bold" x="74" y="42" font-size="20" fill="#FFFFFF">Game Modding</text>
      <text class="t-mono" x="312" y="42" text-anchor="end" font-size="16" fill="#A1A1AA">↗</text>

      <text class="t-semi" x="22" y="94" font-size="14.5" fill="#A1A1AA">Low-level gameplay modding, runtime memory hooks and scripting.</text>

      <!-- Tech Pills -->
      <g transform="translate(22, 178)">
        <rect class="pill-t" x="0" y="0" width="56" height="28"/><text class="pill-lbl" x="28" y="18.5" text-anchor="middle">C++</text>
        <rect class="pill-t" x="64" y="0" width="68" height="28"/><text class="pill-lbl" x="98" y="18.5" text-anchor="middle">Python</text>
        <rect class="pill-t" x="140" y="0" width="84" height="28"/><text class="pill-lbl" x="182" y="18.5" text-anchor="middle">Assembly</text>
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
tech_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 380" width="1200" height="380" role="img" aria-label="Tech Stack of Easir Iqbal Mahi">
  <defs>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
      .cat-lbl {{ font-family: "JetBrains Mono", monospace; font-size: 13px; font-weight: 700; fill: #DC2626; letter-spacing: 1.5px; }}
      .pill-p {{ fill: #1A1C24; stroke: #2D303C; stroke-width: 1.2; rx: 8; }}
      .pill-l {{ font-family: system-ui, sans-serif; font-size: 13.5px; font-weight: 700; fill: #FFFFFF; }}
    </style>
  </defs>

  <rect x="8" y="8" width="1184" height="364" rx="20" fill="#0C0D11" stroke="#222329" stroke-width="1.5"/>

  <!-- Top Header Bar -->
  <g transform="translate(48, 42)">
    <g transform="translate(0, 0)">
      {RADAR_PULSE}
      <text class="t-mono" x="22" y="10" font-size="12.5" letter-spacing="1.8" fill="#E4E4E7">03 · TECHNICAL ARSENAL</text>
    </g>
    <text class="t-mono" x="1104" y="10" text-anchor="end" font-size="12.5" letter-spacing="1.8" fill="#71717A">LANGUAGES · WEB · DATA · CLOUD</text>
  </g>

  <!-- Title -->
  <g transform="translate(48, 98)">
    <text class="t-bold" x="0" y="0" font-size="34" fill="#FFFFFF">Production-Tested <tspan fill="#DC2626">Technologies.</tspan></text>
  </g>

  <!-- 4 Skill Rows -->
  <g transform="translate(48, 128)">
    <!-- Row 1: Languages -->
    <g transform="translate(0, 0)">
      <text class="cat-lbl" x="0" y="23">LANGUAGES</text>
      <g transform="translate(190, 0)">
        <rect class="pill-p" x="0" y="0" width="102" height="34"/><text class="pill-l" x="51" y="22" text-anchor="middle">TypeScript</text>
        <rect class="pill-p" x="112" y="0" width="78" height="34"/><text class="pill-l" x="151" y="22" text-anchor="middle">Python</text>
        <rect class="pill-p" x="200" y="0" width="54" height="34"/><text class="pill-l" x="227" y="22" text-anchor="middle">Go</text>
        <rect class="pill-p" x="264" y="0" width="84" height="34"/><text class="pill-l" x="306" y="22" text-anchor="middle">Node.js</text>
        <rect class="pill-p" x="358" y="0" width="98" height="34"/><text class="pill-l" x="407" y="22" text-anchor="middle">JavaScript</text>
        <rect class="pill-p" x="466" y="0" width="60" height="34"/><text class="pill-l" x="496" y="22" text-anchor="middle">Java</text>
        <rect class="pill-p" x="536" y="0" width="68" height="34"/><text class="pill-l" x="570" y="22" text-anchor="middle">Kotlin</text>
        <rect class="pill-p" x="614" y="0" width="60" height="34"/><text class="pill-l" x="644" y="22" text-anchor="middle">Dart</text>
        <rect class="pill-p" x="684" y="0" width="78" height="34"/><text class="pill-l" x="723" y="22" text-anchor="middle">C, C++</text>
      </g>
    </g>

    <!-- Row 2: Frontend & UI -->
    <g transform="translate(0, 56)">
      <text class="cat-lbl" x="0" y="23">FRONTEND &amp; UI</text>
      <g transform="translate(190, 0)">
        <rect class="pill-p" x="0" y="0" width="70" height="34"/><text class="pill-l" x="35" y="22" text-anchor="middle">React</text>
        <rect class="pill-p" x="80" y="0" width="80" height="34"/><text class="pill-l" x="120" y="22" text-anchor="middle">Next.js</text>
        <rect class="pill-p" x="170" y="0" width="74" height="34"/><text class="pill-l" x="207" y="22" text-anchor="middle">Flutter</text>
        <rect class="pill-p" x="254" y="0" width="108" height="34"/><text class="pill-l" x="308" y="22" text-anchor="middle">TailwindCSS</text>
        <rect class="pill-p" x="372" y="0" width="76" height="34"/><text class="pill-l" x="410" y="22" text-anchor="middle">Vue.js</text>
        <rect class="pill-p" x="458" y="0" width="82" height="34"/><text class="pill-l" x="499" y="22" text-anchor="middle">Angular</text>
        <rect class="pill-p" x="550" y="0" width="66" height="34"/><text class="pill-l" x="583" y="22" text-anchor="middle">Astro</text>
        <rect class="pill-p" x="626" y="0" width="94" height="34"/><text class="pill-l" x="673" y="22" text-anchor="middle">Bootstrap</text>
      </g>
    </g>

    <!-- Row 3: Backend & Data -->
    <g transform="translate(0, 112)">
      <text class="cat-lbl" x="0" y="23">BACKEND &amp; DATA</text>
      <g transform="translate(190, 0)">
        <rect class="pill-p" x="0" y="0" width="106" height="34"/><text class="pill-l" x="53" y="22" text-anchor="middle">PostgreSQL</text>
        <rect class="pill-p" x="116" y="0" width="68" height="34"/><text class="pill-l" x="150" y="22" text-anchor="middle">Redis</text>
        <rect class="pill-p" x="194" y="0" width="80" height="34"/><text class="pill-l" x="234" y="22" text-anchor="middle">Docker</text>
        <rect class="pill-p" x="284" y="0" width="96" height="34"/><text class="pill-l" x="332" y="22" text-anchor="middle">Supabase</text>
        <rect class="pill-p" x="390" y="0" width="94" height="34"/><text class="pill-l" x="437" y="22" text-anchor="middle">MongoDB</text>
        <rect class="pill-p" x="494" y="0" width="78" height="34"/><text class="pill-l" x="533" y="22" text-anchor="middle">FastAPI</text>
        <rect class="pill-p" x="582" y="0" width="78" height="34"/><text class="pill-l" x="621" y="22" text-anchor="middle">Django</text>
        <rect class="pill-p" x="670" y="0" width="76" height="34"/><text class="pill-l" x="708" y="22" text-anchor="middle">MySQL</text>
      </g>
    </g>

    <!-- Row 4: AI & Cloud -->
    <g transform="translate(0, 168)">
      <text class="cat-lbl" x="0" y="23">AI &amp; CLOUD</text>
      <g transform="translate(190, 0)">
        <rect class="pill-p" x="0" y="0" width="114" height="34"/><text class="pill-l" x="57" y="22" text-anchor="middle">Claude Code</text>
        <rect class="pill-p" x="124" y="0" width="96" height="34"/><text class="pill-l" x="172" y="22" text-anchor="middle">Cursor AI</text>
        <rect class="pill-p" x="230" y="0" width="84" height="34"/><text class="pill-l" x="272" y="22" text-anchor="middle">OpenAI</text>
        <rect class="pill-p" x="324" y="0" width="82" height="34"/><text class="pill-l" x="365" y="22" text-anchor="middle">Gemini</text>
        <rect class="pill-p" x="416" y="0" width="54" height="34"/><text class="pill-l" x="443" y="22" text-anchor="middle">Git</text>
        <rect class="pill-p" x="480" y="0" width="86" height="34"/><text class="pill-l" x="523" y="22" text-anchor="middle">Postman</text>
        <rect class="pill-p" x="576" y="0" width="56" height="34"/><text class="pill-l" x="604" y="22" text-anchor="middle">Vite</text>
        <rect class="pill-p" x="642" y="0" width="80" height="34"/><text class="pill-l" x="682" y="22" text-anchor="middle">Railway</text>
        <rect class="pill-p" x="732" y="0" width="74" height="34"/><text class="pill-l" x="769" y="22" text-anchor="middle">Vercel</text>
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
footer_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 220" width="1200" height="220" role="img" aria-label="Easir Iqbal Mahi — Signature">
  <defs>
    <style>
      .t-bold {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }}
      .t-mono {{ font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }}
      .t-semi {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 600; }}
    </style>
  </defs>

  <rect x="8" y="8" width="1184" height="204" rx="20" fill="#0C0D11" stroke="#222329" stroke-width="1.5"/>

  <g transform="translate(0, 36)" text-anchor="middle">
    <!-- Signature -->
    <text class="t-bold" x="600" y="46" font-size="46" fill="#FFFFFF">Easir<tspan fill="#DC2626">.</tspan></text>
    
    <!-- Tagline -->
    <text class="t-mono" x="600" y="82" font-size="13" letter-spacing="2.2" fill="#DC2626">FULL-STACK SOFTWARE DEVELOPER · FOUNDER @ LAGBETO</text>

    <!-- Footer Links Strip -->
    <g transform="translate(0, 124)">
      <text class="t-mono" x="600" y="0" font-size="13.5" letter-spacing="1.2" fill="#A1A1AA">
        www.easirmahi.top   ·   github.com/Sosuke-d-Mahi   ·   easiriqbalmahi@gmail.com
      </text>
    </g>
  </g>
</svg>'''

with open('G:/HYML/Sushmitadasari/assets/footer-card.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
print('Wrote assets/footer-card.svg')
