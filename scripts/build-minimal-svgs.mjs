import fs from "node:fs";
import path from "node:path";

const root = path.resolve(".");
const assetsDir = path.join(root, "assets");

if (!fs.existsSync(assetsDir)) {
  fs.mkdirSync(assetsDir, { recursive: true });
}

// 1. card-about.svg
const cardAbout = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 390" width="1000" height="390" role="img" aria-label="About Easir Iqbal Mahi">
  <defs>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif; }
      .font-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .pill { fill: #FFFFFF; stroke: #E2E8F0; stroke-width: 1.5; rx: 10; }
      .pill-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13.5px; font-weight: 600; fill: #1E293B; }
    </style>
    <filter id="card-shadow" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.04" />
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="10" y="10" width="980" height="370" rx="24" fill="#F8F9FA" stroke="#E2E8F0" stroke-width="2" filter="url(#card-shadow)" />

  <!-- Top Metadata Bar -->
  <g transform="translate(44, 46)">
    <circle cx="5" cy="5" r="4.5" fill="#8B3A4A" />
    <text class="font-mono" x="18" y="9" font-size="13" font-weight="700" letter-spacing="2" fill="#8B3A4A">01 / ABOUT &amp; VENTURE</text>
    <text class="font-mono" x="912" y="9" text-anchor="end" font-size="12.5" font-weight="600" letter-spacing="1.5" fill="#64748B">📍 RAJSHAHI, BD</text>
  </g>

  <!-- Title & Quote -->
  <g transform="translate(44, 82)">
    <text class="font-sans" x="0" y="32" font-size="34" font-weight="800" fill="#0F172A">Founder &amp; Full-Stack <tspan fill="#8B3A4A">Architect.</tspan></text>
    
    <!-- Quote Bar -->
    <rect x="0" y="52" width="912" height="42" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" />
    <text class="font-sans" x="20" y="78" font-size="15.5" font-weight="700" fill="#8B3A4A">“I don’t seek approval. I seek superiority, then I build until reality agrees.”</text>
  </g>

  <!-- Content Columns -->
  <g transform="translate(44, 204)">
    <!-- Left Column: Startup & Philosophy -->
    <g>
      <rect x="0" y="0" width="440" height="110" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" />
      <text class="font-mono" x="20" y="28" font-size="12" font-weight="700" letter-spacing="1.5" fill="#8B3A4A">STARTUP VENTURE</text>
      <text class="font-sans" x="20" y="56" font-size="20" font-weight="700" fill="#0F172A">Founder @ Lagbeto</text>
      <text class="font-sans" x="20" y="82" font-size="14.5" font-weight="500" fill="#475569">Architecting multi-service Go backends &amp; Flutter mobile app.</text>
    </g>

    <!-- Right Column: Systems & Passion -->
    <g transform="translate(472, 0)">
      <rect x="0" y="0" width="440" height="110" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" />
      <text class="font-mono" x="20" y="28" font-size="12" font-weight="700" letter-spacing="1.5" fill="#8B3A4A">SYSTEMS &amp; REVERSE ENGINEERING</text>
      <text class="font-sans" x="20" y="56" font-size="20" font-weight="700" fill="#0F172A">Game Modding &amp; Internals</text>
      <text class="font-sans" x="20" y="82" font-size="14.5" font-weight="500" fill="#475569">Memory inspection, runtime patchers, and custom hook engines.</text>
    </g>
  </g>

  <!-- Bottom Stat Badges -->
  <g transform="translate(44, 342)">
    <text class="font-mono" x="0" y="15" font-size="13" font-weight="600" fill="#64748B">HIGHLIGHTS:</text>
    <g transform="translate(100, 0)">
      <rect class="pill" x="0" y="0" width="150" height="26" />
      <text class="pill-text" x="75" y="17.5" text-anchor="middle">3+ Years Experience</text>
    </g>
    <g transform="translate(262, 0)">
      <rect class="pill" x="0" y="0" width="145" height="26" />
      <text class="pill-text" x="72.5" y="17.5" text-anchor="middle">20+ Projects Built</text>
    </g>
    <g transform="translate(419, 0)">
      <rect class="pill" x="0" y="0" width="170" height="26" />
      <text class="pill-text" x="85" y="17.5" text-anchor="middle">679 GitHub Commits</text>
    </g>
    <g transform="translate(601, 0)">
      <rect class="pill" x="0" y="0" width="135" height="26" />
      <text class="pill-text" x="67.5" y="17.5" text-anchor="middle">∞ Keep Building</text>
    </g>
  </g>
</svg>`;

fs.writeFileSync(path.join(assetsDir, "card-about.svg"), cardAbout);
console.log("Wrote assets/card-about.svg");

// 2. card-projects.svg
const cardProjects = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 480" width="1000" height="480" role="img" aria-label="Featured Projects of Easir Iqbal Mahi">
  <defs>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif; }
      .font-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .tag { fill: #F1F5F9; stroke: #E2E8F0; stroke-width: 1; rx: 8; }
      .tag-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; font-weight: 600; fill: #334155; }
      .featured-badge { fill: #8B3A4A; rx: 6; }
      .badge-text { font-family: "JetBrains Mono", monospace; font-size: 11px; font-weight: 700; fill: #FFFFFF; }
    </style>
  </defs>

  <!-- Card Background -->
  <rect x="10" y="10" width="980" height="460" rx="24" fill="#F8F9FA" stroke="#E2E8F0" stroke-width="2" />

  <!-- Top Metadata Bar -->
  <g transform="translate(44, 46)">
    <circle cx="5" cy="5" r="4.5" fill="#8B3A4A" />
    <text class="font-mono" x="18" y="9" font-size="13" font-weight="700" letter-spacing="2" fill="#8B3A4A">02 / SELECTED WORK &amp; SYSTEMS</text>
    <text class="font-mono" x="912" y="9" text-anchor="end" font-size="12.5" font-weight="600" letter-spacing="1.5" fill="#64748B">PRODUCTS, NOT ASSIGNMENTS</text>
  </g>

  <!-- Title -->
  <g transform="translate(44, 82)">
    <text class="font-sans" x="0" y="30" font-size="32" font-weight="800" fill="#0F172A">Built for <tspan fill="#8B3A4A">Scale,</tspan> Performance &amp; Precision.</text>
  </g>

  <!-- 3 Project Rows -->
  <g transform="translate(44, 130)">
    <!-- Project 1: api-docs -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="912" height="96" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.4" />
      <rect class="featured-badge" x="22" y="20" width="82" height="22" />
      <text class="badge-text" x="63" y="35" text-anchor="middle">FEATURED</text>
      
      <text class="font-sans" x="116" y="38" font-size="22" font-weight="800" fill="#0F172A">api-docs</text>
      <text class="font-mono" x="225" y="36" font-size="13" font-weight="600" fill="#64748B">/ github.com/Sosuke-d-Mahi/api-docs</text>
      <text class="font-sans" x="22" y="72" font-size="15" font-weight="500" fill="#334155">Interactive documentation platform with real-time payload testing, sub-millisecond spec parsing &amp; OpenAPI validation.</text>
      
      <!-- Tags -->
      <g transform="translate(560, 18)">
        <rect class="tag" x="0" y="0" width="92" height="26" /><text class="tag-text" x="46" y="17.5" text-anchor="middle">TypeScript</text>
        <rect class="tag" x="98" y="0" width="76" height="26" /><text class="tag-text" x="136" y="17.5" text-anchor="middle">Node.js</text>
        <rect class="tag" x="180" y="0" width="82" height="26" /><text class="tag-text" x="221" y="17.5" text-anchor="middle">REST API</text>
        <rect class="tag" x="268" y="0" width="76" height="26" /><text class="tag-text" x="306" y="17.5" text-anchor="middle">OpenAPI</text>
      </g>
    </g>

    <!-- Project 2: Lagbeto Platform -->
    <g transform="translate(0, 108)">
      <rect x="0" y="0" width="912" height="96" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.4" />
      <rect class="featured-badge" x="22" y="20" width="74" height="22" fill="#0F172A" />
      <text class="badge-text" x="59" y="35" text-anchor="middle">STARTUP</text>
      
      <text class="font-sans" x="108" y="38" font-size="22" font-weight="800" fill="#0F172A">Lagbeto Platform</text>
      <text class="font-mono" x="305" y="36" font-size="13" font-weight="600" fill="#64748B">/ Distributed Platform &amp; Mobile</text>
      <text class="font-sans" x="22" y="72" font-size="15" font-weight="500" fill="#334155">High-availability microservice backend in Go &amp; Node.js, PostgreSQL persistence, and Flutter cross-platform mobile client.</text>
      
      <!-- Tags -->
      <g transform="translate(584, 18)">
        <rect class="tag" x="0" y="0" width="50" height="26" /><text class="tag-text" x="25" y="17.5" text-anchor="middle">Go</text>
        <rect class="tag" x="56" y="0" width="76" height="26" /><text class="tag-text" x="94" y="17.5" text-anchor="middle">Flutter</text>
        <rect class="tag" x="138" y="0" width="96" height="26" /><text class="tag-text" x="186" y="17.5" text-anchor="middle">PostgreSQL</text>
        <rect class="tag" x="240" y="0" width="80" height="26" /><text class="tag-text" x="280" y="17.5" text-anchor="middle">Docker</text>
      </g>
    </g>

    <!-- Project 3: Game Modding & Internals -->
    <g transform="translate(0, 216)">
      <rect x="0" y="0" width="912" height="96" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.4" />
      <rect class="featured-badge" x="22" y="20" width="74" height="22" fill="#475569" />
      <text class="badge-text" x="59" y="35" text-anchor="middle">SYSTEMS</text>
      
      <text class="font-sans" x="108" y="38" font-size="22" font-weight="800" fill="#0F172A">Game Modding &amp; Internals</text>
      <text class="font-mono" x="400" y="36" font-size="13" font-weight="600" fill="#64748B">/ Reverse Engineering &amp; Tooling</text>
      <text class="font-sans" x="22" y="72" font-size="15" font-weight="500" fill="#334155">Reverse engineering game binaries, disassembling execution logic, and building runtime memory injection hooks.</text>
      
      <!-- Tags -->
      <g transform="translate(560, 18)">
        <rect class="tag" x="0" y="0" width="60" height="26" /><text class="tag-text" x="30" y="17.5" text-anchor="middle">C++</text>
        <rect class="tag" x="66" y="0" width="76" height="26" /><text class="tag-text" x="104" y="17.5" text-anchor="middle">Python</text>
        <rect class="tag" x="148" y="0" width="84" height="26" /><text class="tag-text" x="190" y="17.5" text-anchor="middle">Assembly</text>
        <rect class="tag" x="238" y="0" width="82" height="26" /><text class="tag-text" x="279" y="17.5" text-anchor="middle">Reverse</text>
      </g>
    </g>
  </g>
</svg>`;

fs.writeFileSync(path.join(assetsDir, "card-projects.svg"), cardProjects);
console.log("Wrote assets/card-projects.svg");

// 3. card-tech.svg
const cardTech = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" role="img" aria-label="Tech Stack and Toolkit of Easir Iqbal Mahi">
  <defs>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif; }
      .font-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .pill-cat { font-family: "JetBrains Mono", monospace; font-size: 12.5px; font-weight: 700; fill: #8B3A4A; letter-spacing: 1.5px; }
      .tech-pill { fill: #FFFFFF; stroke: #CBD5E1; stroke-width: 1.3; rx: 9; }
      .tech-pill-primary { fill: #0F172A; rx: 9; }
      .tech-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14.5px; font-weight: 600; fill: #1E293B; }
      .tech-text-primary { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14.5px; font-weight: 700; fill: #FFFFFF; }
    </style>
  </defs>

  <!-- Card Background -->
  <rect x="10" y="10" width="980" height="430" rx="24" fill="#F8F9FA" stroke="#E2E8F0" stroke-width="2" />

  <!-- Top Metadata Bar -->
  <g transform="translate(44, 46)">
    <circle cx="5" cy="5" r="4.5" fill="#8B3A4A" />
    <text class="font-mono" x="18" y="9" font-size="13" font-weight="700" letter-spacing="2" fill="#8B3A4A">03 / TECH STACK &amp; TOOLKIT</text>
    <text class="font-mono" x="912" y="9" text-anchor="end" font-size="12.5" font-weight="600" letter-spacing="1.5" fill="#64748B">50+ PRODUCTION TOOLS</text>
  </g>

  <!-- Title -->
  <g transform="translate(44, 82)">
    <text class="font-sans" x="0" y="30" font-size="32" font-weight="800" fill="#0F172A">Tools I reach for, <tspan fill="#8B3A4A">and why.</tspan></text>
  </g>

  <!-- Categories -->
  <g transform="translate(44, 135)">
    <!-- Row 1: Core Languages -->
    <g transform="translate(0, 0)">
      <text class="pill-cat" x="0" y="21">CORE LANGUAGES</text>
      <g transform="translate(180, 0)">
        <rect class="tech-pill-primary" x="0" y="0" width="102" height="32" /><text class="tech-text-primary" x="51" y="21" text-anchor="middle">TypeScript</text>
        <rect class="tech-pill-primary" x="110" y="0" width="80" height="32" /><text class="tech-text-primary" x="150" y="21" text-anchor="middle">Python</text>
        <rect class="tech-pill-primary" x="198" y="0" width="50" height="32" /><text class="tech-text-primary" x="223" y="21" text-anchor="middle">Go</text>
        <rect class="tech-pill-primary" x="256" y="0" width="62" height="32" /><text class="tech-text-primary" x="287" y="21" text-anchor="middle">Dart</text>
        <rect class="tech-pill-primary" x="326" y="0" width="70" height="32" /><text class="tech-text-primary" x="361" y="21" text-anchor="middle">Kotlin</text>
        <rect class="tech-pill" x="404" y="0" width="60" height="32" /><text class="tech-text" x="434" y="21" text-anchor="middle">Java</text>
        <rect class="tech-pill" x="472" y="0" width="98" height="32" /><text class="tech-text" x="521" y="21" text-anchor="middle">JavaScript</text>
        <rect class="tech-pill" x="578" y="0" width="54" height="32" /><text class="tech-text" x="605" y="21" text-anchor="middle">C++</text>
        <rect class="tech-pill" x="640" y="0" width="46" height="32" /><text class="tech-text" x="663" y="21" text-anchor="middle">C</text>
        <rect class="tech-pill" x="694" y="0" width="48" height="32" /><text class="tech-text" x="718" y="21" text-anchor="middle">C#</text>
      </g>
    </g>

    <!-- Row 2: Mobile & Frontend -->
    <g transform="translate(0, 56)">
      <text class="pill-cat" x="0" y="21">MOBILE &amp; WEB</text>
      <g transform="translate(180, 0)">
        <rect class="tech-pill-primary" x="0" y="0" width="76" height="32" /><text class="tech-text-primary" x="38" y="21" text-anchor="middle">Flutter</text>
        <rect class="tech-pill" x="84" y="0" width="70" height="32" /><text class="tech-text" x="119" y="21" text-anchor="middle">React</text>
        <rect class="tech-pill" x="162" y="0" width="78" height="32" /><text class="tech-text" x="201" y="21" text-anchor="middle">Next.js</text>
        <rect class="tech-pill" x="248" y="0" width="102" height="32" /><text class="tech-text" x="299" y="21" text-anchor="middle">TailwindCSS</text>
        <rect class="tech-pill" x="358" y="0" width="76" height="32" /><text class="tech-text" x="396" y="21" text-anchor="middle">Vue.js</text>
        <rect class="tech-pill" x="442" y="0" width="80" height="32" /><text class="tech-text" x="482" y="21" text-anchor="middle">Angular</text>
        <rect class="tech-pill" x="530" y="0" width="66" height="32" /><text class="tech-text" x="563" y="21" text-anchor="middle">Astro</text>
      </g>
    </g>

    <!-- Row 3: Backend & Systems -->
    <g transform="translate(0, 112)">
      <text class="pill-cat" x="0" y="21">BACKEND &amp; CLOUD</text>
      <g transform="translate(180, 0)">
        <rect class="tech-pill-primary" x="0" y="0" width="82" height="32" /><text class="tech-text-primary" x="41" y="21" text-anchor="middle">Node.js</text>
        <rect class="tech-pill" x="90" y="0" width="86" height="32" /><text class="tech-text" x="133" y="21" text-anchor="middle">Express</text>
        <rect class="tech-pill" x="184" y="0" width="78" height="32" /><text class="tech-text" x="223" y="21" text-anchor="middle">FastAPI</text>
        <rect class="tech-pill" x="270" y="0" width="80" height="32" /><text class="tech-text" x="310" y="21" text-anchor="middle">Django</text>
        <rect class="tech-pill-primary" x="358" y="0" width="78" height="32" /><text class="tech-text-primary" x="397" y="21" text-anchor="middle">Docker</text>
        <rect class="tech-pill" x="444" y="0" width="66" height="32" /><text class="tech-text" x="477" y="21" text-anchor="middle">Nginx</text>
        <rect class="tech-pill" x="518" y="0" width="58" height="32" /><text class="tech-text" x="547" y="21" text-anchor="middle">GCP</text>
        <rect class="tech-pill" x="584" y="0" width="78" height="32" /><text class="tech-text" x="623" y="21" text-anchor="middle">Railway</text>
        <rect class="tech-pill" x="670" y="0" width="72" height="32" /><text class="tech-text" x="706" y="21" text-anchor="middle">Vercel</text>
      </g>
    </g>

    <!-- Row 4: Data & Cache -->
    <g transform="translate(0, 168)">
      <text class="pill-cat" x="0" y="21">DATA &amp; CACHE</text>
      <g transform="translate(180, 0)">
        <rect class="tech-pill-primary" x="0" y="0" width="106" height="32" /><text class="tech-text-primary" x="53" y="21" text-anchor="middle">PostgreSQL</text>
        <rect class="tech-pill-primary" x="114" y="0" width="64" height="32" /><text class="tech-text-primary" x="146" y="21" text-anchor="middle">Redis</text>
        <rect class="tech-pill" x="186" y="0" width="94" height="32" /><text class="tech-text" x="233" y="21" text-anchor="middle">MongoDB</text>
        <rect class="tech-pill" x="288" y="0" width="92" height="32" /><text class="tech-text" x="334" y="21" text-anchor="middle">Supabase</text>
        <rect class="tech-pill" x="388" y="0" width="72" height="32" /><text class="tech-text" x="424" y="21" text-anchor="middle">MySQL</text>
        <rect class="tech-pill" x="468" y="0" width="86" height="32" /><text class="tech-text" x="511" y="21" text-anchor="middle">Firestore</text>
        <rect class="tech-pill" x="562" y="0" width="102" height="32" /><text class="tech-text" x="613" y="21" text-anchor="middle">DynamoDB</text>
      </g>
    </g>

    <!-- Row 5: AI & Modern Workflow -->
    <g transform="translate(0, 224)">
      <text class="pill-cat" x="0" y="21">AI &amp; DEV TOOLS</text>
      <g transform="translate(180, 0)">
        <rect class="tech-pill-primary" x="0" y="0" width="112" height="32" /><text class="tech-text-primary" x="56" y="21" text-anchor="middle">Claude Code</text>
        <rect class="tech-pill-primary" x="120" y="0" width="92" height="32" /><text class="tech-text-primary" x="166" y="21" text-anchor="middle">Cursor AI</text>
        <rect class="tech-pill" x="220" y="0" width="80" height="32" /><text class="tech-text" x="260" y="21" text-anchor="middle">OpenAI</text>
        <rect class="tech-pill" x="308" y="0" width="78" height="32" /><text class="tech-text" x="347" y="21" text-anchor="middle">Gemini</text>
        <rect class="tech-pill" x="394" y="0" width="52" height="32" /><text class="tech-text" x="420" y="21" text-anchor="middle">Git</text>
        <rect class="tech-pill" x="454" y="0" width="84" height="32" /><text class="tech-text" x="496" y="21" text-anchor="middle">Postman</text>
        <rect class="tech-pill" x="546" y="0" width="54" height="32" /><text class="tech-text" x="573" y="21" text-anchor="middle">Vite</text>
      </g>
    </g>
  </g>
</svg>`;

fs.writeFileSync(path.join(assetsDir, "card-tech.svg"), cardTech);
console.log("Wrote assets/card-tech.svg");

// 4. card-stats.svg
const cardStats = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 280" width="1000" height="280" role="img" aria-label="Commit Log and Metrics of Easir Iqbal Mahi">
  <defs>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif; }
      .font-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .stat-card { fill: #FFFFFF; stroke: #E2E8F0; stroke-width: 1.4; rx: 16; }
    </style>
  </defs>

  <!-- Card Background -->
  <rect x="10" y="10" width="980" height="260" rx="24" fill="#F8F9FA" stroke="#E2E8F0" stroke-width="2" />

  <!-- Top Metadata Bar -->
  <g transform="translate(44, 46)">
    <circle cx="5" cy="5" r="4.5" fill="#8B3A4A" />
    <text class="font-mono" x="18" y="9" font-size="13" font-weight="700" letter-spacing="2" fill="#8B3A4A">04 / COMMIT LOG &amp; METRICS</text>
    <text class="font-mono" x="912" y="9" text-anchor="end" font-size="12.5" font-weight="600" letter-spacing="1.5" fill="#64748B">CONTINUOUS DELIVERY</text>
  </g>

  <!-- Title -->
  <g transform="translate(44, 82)">
    <text class="font-sans" x="0" y="30" font-size="32" font-weight="800" fill="#0F172A">679 Verified Contributions <tspan fill="#8B3A4A">Over the Past Year.</tspan></text>
  </g>

  <!-- Stat Columns -->
  <g transform="translate(44, 138)">
    <!-- Stat 1 -->
    <g transform="translate(0, 0)">
      <rect class="stat-card" x="0" y="0" width="212" height="106" />
      <text class="font-sans" x="22" y="44" font-size="38" font-weight="800" fill="#0F172A">679</text>
      <text class="font-sans" x="22" y="72" font-size="14" font-weight="700" fill="#8B3A4A">GitHub Commits</text>
      <text class="font-mono" x="22" y="92" font-size="12" font-weight="500" fill="#64748B">367 days recorded</text>
    </g>

    <!-- Stat 2 -->
    <g transform="translate(233, 0)">
      <rect class="stat-card" x="0" y="0" width="212" height="106" />
      <text class="font-sans" x="22" y="44" font-size="38" font-weight="800" fill="#0F172A">15+</text>
      <text class="font-sans" x="22" y="72" font-size="14" font-weight="700" fill="#8B3A4A">Production Frameworks</text>
      <text class="font-mono" x="22" y="92" font-size="12" font-weight="500" fill="#64748B">Web, mobile &amp; backend</text>
    </g>

    <!-- Stat 3 -->
    <g transform="translate(466, 0)">
      <rect class="stat-card" x="0" y="0" width="212" height="106" />
      <text class="font-sans" x="22" y="44" font-size="38" font-weight="800" fill="#0F172A">8+</text>
      <text class="font-sans" x="22" y="72" font-size="14" font-weight="700" fill="#8B3A4A">Core Languages</text>
      <text class="font-mono" x="22" y="92" font-size="12" font-weight="500" fill="#64748B">Polyglot proficiency</text>
    </g>

    <!-- Stat 4 -->
    <g transform="translate(700, 0)">
      <rect class="stat-card" x="0" y="0" width="212" height="106" />
      <text class="font-sans" x="22" y="44" font-size="38" font-weight="800" fill="#8B3A4A">∞</text>
      <text class="font-sans" x="22" y="72" font-size="14" font-weight="700" fill="#0F172A">Founder @ Lagbeto</text>
      <text class="font-mono" x="22" y="92" font-size="12" font-weight="500" fill="#64748B">Hands-on architecture</text>
    </g>
  </g>
</svg>`;

fs.writeFileSync(path.join(assetsDir, "card-stats.svg"), cardStats);
console.log("Wrote assets/card-stats.svg");

// 5. card-connect.svg
const cardConnect = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240" width="1000" height="240" role="img" aria-label="Connect with Easir Iqbal Mahi">
  <defs>
    <style>
      .font-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif; }
      .font-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .btn-pill { fill: #FFFFFF; stroke: #CBD5E1; stroke-width: 1.4; rx: 12; }
      .btn-pill-primary { fill: #8B3A4A; rx: 12; }
      .btn-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14.5px; font-weight: 700; fill: #0F172A; }
      .btn-text-primary { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14.5px; font-weight: 700; fill: #FFFFFF; }
    </style>
  </defs>

  <!-- Card Background -->
  <rect x="10" y="10" width="980" height="220" rx="24" fill="#F8F9FA" stroke="#E2E8F0" stroke-width="2" />

  <!-- Top Metadata Bar -->
  <g transform="translate(44, 46)">
    <circle cx="5" cy="5" r="4.5" fill="#8B3A4A" />
    <text class="font-mono" x="18" y="9" font-size="13" font-weight="700" letter-spacing="2" fill="#8B3A4A">05 / GET IN TOUCH</text>
    <text class="font-mono" x="912" y="9" text-anchor="end" font-size="12.5" font-weight="600" letter-spacing="1.5" fill="#64748B">MY INBOX IS OPEN</text>
  </g>

  <!-- Title & Lede -->
  <g transform="translate(44, 82)">
    <text class="font-sans" x="0" y="30" font-size="32" font-weight="800" fill="#0F172A">Let’s build something <tspan fill="#8B3A4A">worth explaining.</tspan></text>
    <text class="font-sans" x="0" y="60" font-size="15.5" font-weight="500" fill="#475569">Open for high-impact full-stack collaborations, venture engineering, and systems discussions.</text>
  </g>

  <!-- Action Links / Buttons -->
  <g transform="translate(44, 168)">
    <g>
      <rect class="btn-pill-primary" x="0" y="0" width="250" height="42" />
      <text class="btn-text-primary" x="125" y="26" text-anchor="middle">✉ easiriqbalmahi@gmail.com</text>
    </g>
    <g transform="translate(266, 0)">
      <rect class="btn-pill" x="0" y="0" width="200" height="42" />
      <text class="btn-text" x="100" y="26" text-anchor="middle">💼 in/easirmahi ↗</text>
    </g>
    <g transform="translate(482, 0)">
      <rect class="btn-pill" x="0" y="0" width="220" height="42" />
      <text class="btn-text" x="110" y="26" text-anchor="middle">🐙 @Sosuke-d-Mahi ↗</text>
    </g>
    <g transform="translate(718, 0)">
      <rect class="btn-pill" x="0" y="0" width="194" height="42" />
      <text class="btn-text" x="97" y="26" text-anchor="middle">🌐 easirmahi.top ↗</text>
    </g>
  </g>
</svg>`;

fs.writeFileSync(path.join(assetsDir, "card-connect.svg"), cardConnect);
console.log("Wrote assets/card-connect.svg");
