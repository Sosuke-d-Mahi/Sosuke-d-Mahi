#!/usr/bin/env node
/**
 * Renders assets/contribution-snake.svg for the profile README from the
 * real contribution snapshot in site/data/contributions.json.
 */

import fs from "node:fs";
import path from "node:path";

const INPUT = process.env.INPUT_PATH || "site/data/contributions.json";
const OUTPUT = process.env.OUTPUT_PATH || "assets/contribution-snake.svg";

const W = 1200;
const H = 410;
const CELL = 15;
const GAP = 4;
const STEP = CELL + GAP;
const GRID_X = 118;
const GRID_Y = 175;
const LEVELS = ["#1D070C", "#5A111F", "#991B1B", "#DC2626", "#FF334B"];

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const toDate = (iso) => new Date(`${iso}T00:00:00Z`);
const fmt = (d) => `${d.getUTCDate()} ${MONTHS[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

if (!fs.existsSync(INPUT)) {
  console.warn(`No snapshot at ${INPUT}; leaving ${OUTPUT} unchanged.`);
  process.exit(0);
}
const data = JSON.parse(fs.readFileSync(INPUT, "utf8"));
const days = data.days;
if (!Array.isArray(days) || days.length === 0) {
  console.warn("Snapshot has no days; leaving SVG unchanged.");
  process.exit(0);
}

/* ---- Stats ---- */
let total = 0, active = 0, run = 0, best = 0, bestEnd = -1, peak = days[0];
days.forEach((d, i) => {
  total += d.count;
  if (d.count > 0) {
    active++;
    if (++run > best) { best = run; bestEnd = i; }
    if (d.count > peak.count) peak = d;
  } else run = 0;
});
const bestStart = bestEnd - best + 1;
const first = toDate(days[0].date);
const last = toDate(days[days.length - 1].date);
const fetched = data.fetchedAt ? fmt(new Date(data.fetchedAt)) : fmt(last);

/* ---- Grid ---- */
const offset = first.getUTCDay();
const pos = (i) => {
  const week = Math.floor((i + offset) / 7);
  const dow = (i + offset) % 7;
  return { week, dow, x: GRID_X + week * STEP, y: GRID_Y + dow * STEP };
};
const label = (d) => `${d.count} contribution${d.count === 1 ? "" : "s"} · ${fmt(toDate(d.date))}`;

/* ---- Snake ---- */
const weeksCount = Math.floor((days.length - 1 + offset) / 7) + 1;
const center = (week, dow) => [GRID_X + week * STEP + CELL / 2, GRID_Y + dow * STEP + CELL / 2];
const route = [];
for (let w = 0; w < weeksCount; w++) {
  for (let r = 0; r < 7; r++) route.push(center(w, w % 2 === 0 ? r : 6 - r));
}
const [fx, fy] = route[0];
const [lx, ly] = route[route.length - 1];
route.unshift([fx, fy - STEP]);
route.push([lx + STEP, ly]);
const SNAKE_DT = 0.055;
const SNAKE_BEGIN = 2.4;
const runTime = (route.length - 1) * SNAKE_DT;
const loop = runTime + 3.5;
const runFrac = (runTime / loop).toFixed(4);
const routeD = "M" + route.map(([x, y]) => `${x.toFixed(1)} ${y.toFixed(1)}`).join(" L");

const routeIndex = (i) => {
  const { week, dow } = pos(i);
  return week * 7 + (week % 2 === 0 ? dow : 6 - dow) + 1;
};

const cellsSvg = days
  .map((d, i) => {
    const { week, dow, x, y } = pos(i);
    const delay = (0.3 + (week + dow * 1.6) * 0.018).toFixed(3);
    const color = LEVELS[d.level] ?? LEVELS[0];
    const eat = d.count > 0
      ? `<animate attributeName="fill" values="${color};${LEVELS[0]}" keyTimes="0;${((routeIndex(i) * SNAKE_DT) / loop).toFixed(4)}" calcMode="discrete" dur="${loop.toFixed(2)}s" begin="${SNAKE_BEGIN}s" repeatCount="indefinite"/>`
      : "";
    return `<rect class="hm-c" style="animation-delay:${delay}s" x="${x}" y="${y}" width="${CELL}" height="${CELL}" rx="3.5" fill="${color}"><title>${label(d)}</title>${eat}</rect>`;
  })
  .join("\n    ");

let streakSvg = "";
if (best > 1) {
  const startPos = pos(bestStart);
  const labelX = Math.min(startPos.x, W - 420);
  streakSvg = `<g class="hm-fade" style="animation-delay:2.6s">
      <path d="M${startPos.x + CELL / 2} ${GRID_Y + 7 * STEP - 2} V ${GRID_Y + 7 * STEP + 10}" stroke="#FF334B" stroke-width="1.8"/>
      <text class="hm-mono" x="${labelX}" y="${GRID_Y + 7 * STEP + 24}" font-size="12" font-weight="700" letter-spacing="1.2" fill="#FF334B">LONGEST STREAK · ${best} DAYS · ${fmt(toDate(days[bestStart].date)).toUpperCase()} – ${fmt(toDate(days[bestEnd].date)).toUpperCase()}</text>
    </g>`;
}

const SEGMENTS = 9;
const snakeSvg = Array.from({ length: SEGMENTS }, (_, k) => {
  const seg = SEGMENTS - 1 - k;
  const size = CELL - seg * 0.9;
  const fill = seg === 0 ? "#FFFFFF" : seg < 3 ? "#FF334B" : seg < 6 ? "#DC2626" : "#991B1B";
  const op = (1 - seg * 0.06).toFixed(2);
  const begin = (SNAKE_BEGIN + seg * SNAKE_DT).toFixed(3);
  const eyes = seg === 0 ? `<circle cx="${(size / 2 - 4).toFixed(1)}" cy="-2.5" r="1.3" fill="#18070B"/><circle cx="${(size / 2 - 4).toFixed(1)}" cy="2.5" r="1.3" fill="#18070B"/>` : "";
  return `<g opacity="0">
      <animateMotion path="${routeD}" rotate="auto" dur="${loop.toFixed(2)}s" begin="${begin}s" repeatCount="indefinite" calcMode="linear" keyPoints="0;1;1" keyTimes="0;${runFrac};1"/>
      <animate attributeName="opacity" values="${op};0" keyTimes="0;${runFrac}" calcMode="discrete" dur="${loop.toFixed(2)}s" begin="${begin}s" repeatCount="indefinite"/>
      <rect x="${(-size / 2).toFixed(1)}" y="${(-size / 2).toFixed(1)}" width="${size.toFixed(1)}" height="${size.toFixed(1)}" rx="${(size / 2.6).toFixed(1)}" fill="${fill}"/>${eyes}
    </g>`;
}).join("\n    ");

/* ---- Month labels ---- */
const labels = [];
let lastMonth = -1;
days.forEach((d, i) => {
  const m = toDate(d.date).getUTCMonth();
  if (m === lastMonth) return;
  lastMonth = m;
  labels.push({ col: Math.floor((i + offset) / 7), text: MONTHS[m] });
});
if (labels.length > 1 && labels[1].col - labels[0].col < 3) labels.shift();
const monthSvg = labels
  .map(({ col, text }) => `<text x="${GRID_X + col * STEP}" y="${GRID_Y - 14}">${text}</text>`)
  .join("");

const stats = [
  ["CONTRIBUTIONS", total.toLocaleString("en-US"), `${MONTHS[first.getUTCMonth()]} ${first.getUTCFullYear()} – ${MONTHS[last.getUTCMonth()]} ${last.getUTCFullYear()}`],
  ["ACTIVE DAYS", String(active), `of ${days.length} days`],
  ["LONGEST STREAK", String(best), "consecutive days"],
  ["BUSIEST DAY", String(peak.count), fmt(toDate(peak.date))],
];
const statsSvg = stats
  .map(([label, value, sub], i) => {
    const x = 580 + i * 150;
    return `<g transform="translate(${x} 54)">
      <rect x="0" y="0" width="140" height="74" rx="14" fill="#1D070C" stroke="#DC2626" stroke-width="1.4" />
      <text class="hm-mono" x="14" y="24" font-size="11" font-weight="700" letter-spacing="1.2" fill="#FF334B">${label}</text>
      <text class="hm-sans" x="14" y="52" font-size="26" font-weight="800" fill="#FFFFFF">${esc(value)}</text>
      <text class="hm-mono" x="14" y="66" font-size="10" font-weight="600" fill="#E2E8F0">${esc(sub)}</text>
    </g>`;
  })
  .join("\n    ");

const legendX = W - 56 - 5 * 20 - 90;
const legend = LEVELS.map((c, i) => `<rect x="${legendX + 42 + i * 20}" y="369" width="14" height="14" rx="3.5" fill="${c}"/>`).join("");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-labelledby="hm-title hm-desc">
  <title id="hm-title">GitHub contributions for @${esc(data.login)}</title>
  <desc id="hm-desc">${total} contributions from ${fmt(first)} to ${fmt(last)}: ${active} active days, longest streak ${best} days, busiest day ${peak.count} contributions on ${fmt(toDate(peak.date))}. Source: ${esc(data.method || "public GitHub contribution calendar")}, snapshot ${fetched}.</desc>
  <defs>
    <linearGradient id="hm-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#18070B"/>
      <stop offset="100%" stop-color="#080204"/>
    </linearGradient>
  </defs>
  <style>
    .hm-sans { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
    .hm-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
    .hm-c { transform-box: fill-box; transform-origin: center; animation: hm-in .8s cubic-bezier(.34,1.56,.64,1) both; }
    .hm-fade { animation: hm-fade 1.2s ease both; }
    @keyframes hm-in { from { opacity: 0; transform: scale(.2); } to { opacity: 1; transform: none; } }
    @keyframes hm-fade { from { opacity: 0; } to { opacity: 1; } }
    @media (prefers-reduced-motion: reduce) { .hm-c, .hm-fade { animation: none; } .hm-motion { display: none; } }
  </style>

  <!-- Dark True Red Card Background -->
  <rect x="10" y="10" width="${W - 20}" height="${H - 20}" rx="24" fill="url(#hm-bg)" stroke="#DC2626" stroke-width="2"/>

  <!-- Top Header Bar (No slashes!) -->
  <g class="hm-fade" transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#FF334B" />
    <text class="hm-mono" x="22" y="11" font-size="14" letter-spacing="2" fill="#FF334B">COMMIT LOG &amp; REAL ACTIVITY</text>
    <text class="hm-sans" x="0" y="58" font-size="32" fill="#FFFFFF">A year of building, <tspan fill="#FF334B">one square</tspan> at a time.</text>
    ${statsSvg}
  </g>

  <!-- Month & Day Labels -->
  <g class="hm-mono" font-size="12" fill="#FF334B">${monthSvg}</g>
  <g class="hm-mono" font-size="11.5" fill="#FF334B" text-anchor="end">
    <text x="${GRID_X - 14}" y="${GRID_Y + STEP + 11}">Mon</text>
    <text x="${GRID_X - 14}" y="${GRID_Y + 3 * STEP + 11}">Wed</text>
    <text x="${GRID_X - 14}" y="${GRID_Y + 5 * STEP + 11}">Fri</text>
  </g>

  <!-- Cells -->
  <g>
    ${cellsSvg}
  </g>

  <!-- Snake Motion -->
  <g class="hm-motion">
    ${snakeSvg}
  </g>

  ${streakSvg}

  <!-- Footer Legend -->
  <g class="hm-fade">
    <text class="hm-mono" x="56" y="380" font-size="12" fill="#E2E8F0">Source: public GitHub contribution calendar for @${esc(data.login)} · snapshot ${fetched}</text>
    <text class="hm-mono" x="${legendX}" y="380" font-size="12" fill="#FF334B">Less</text>
    ${legend}
    <text class="hm-mono" x="${legendX + 42 + 5 * 20 + 6}" y="380" font-size="12" fill="#FF334B">More</text>
  </g>
</svg>
`;

const out = path.resolve(OUTPUT);
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, svg, "utf8");
console.log(`Wrote ${OUTPUT}: ${days.length} days, ${total} contributions (snapshot ${fetched}).`);
