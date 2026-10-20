#!/usr/bin/env node
/**
 * Renders assets/contribution-snake.svg with editorial charcoal & burgundy theme.
 * Clean, lightweight, native radar pulse on status dot, zero broken CSS animation.
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
const LEVELS = ["#14151B", "#4A121E", "#7F1D2D", "#DC2626", "#EF4444"];

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

/* ---- Heatmap Grid ---- */
const offset = first.getUTCDay();
const pos = (idx) => {
  const abs = idx + offset;
  const col = Math.floor(abs / 7);
  const row = abs % 7;
  return { x: GRID_X + col * STEP, y: GRID_Y + row * STEP };
};

const label = (d) =>
  d.count === 0
    ? `No contributions on ${fmt(toDate(d.date))}`
    : `${d.count} contribution${d.count === 1 ? "" : "s"} on ${fmt(toDate(d.date))}`;

const cellsSvg = days
  .map((d, i) => {
    const { x, y } = pos(i);
    const color = LEVELS[d.level] || LEVELS[0];
    return `<rect x="${x}" y="${y}" width="${CELL}" height="${CELL}" rx="3" fill="${color}"><title>${label(d)}</title></rect>`;
  })
  .join("\n    ");

let streakSvg = "";
if (best > 1) {
  const startPos = pos(bestStart);
  const labelX = Math.min(startPos.x, W - 420);
  streakSvg = `<g>
      <path d="M${startPos.x + CELL / 2} ${GRID_Y + 7 * STEP - 2} V ${GRID_Y + 7 * STEP + 10}" stroke="#DC2626" stroke-width="1.8"/>
      <text class="hm-mono" x="${labelX}" y="${GRID_Y + 7 * STEP + 24}" font-size="12" font-weight="700" letter-spacing="1.2" fill="#DC2626">LONGEST STREAK · ${best} DAYS · ${fmt(toDate(days[bestStart].date)).toUpperCase()} – ${fmt(toDate(days[bestEnd].date)).toUpperCase()}</text>
    </g>`;
}

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
  .map(([lbl, value, sub], i) => {
    const x = 580 + i * 150;
    return `<g transform="translate(${x} 54)">
      <rect x="0" y="0" width="140" height="74" rx="10" fill="#14151B" stroke="#23242B" stroke-width="1.2" />
      <text class="hm-mono" x="14" y="24" font-size="11" font-weight="700" letter-spacing="1.2" fill="#DC2626">${lbl}</text>
      <text class="hm-sans" x="14" y="52" font-size="26" font-weight="800" fill="#FFFFFF">${esc(value)}</text>
      <text class="hm-mono" x="14" y="66" font-size="10" font-weight="600" fill="#A1A1AA">${esc(sub)}</text>
    </g>`;
  })
  .join("\n    ");

const legendX = W - 56 - 5 * 20 - 90;
const legend = LEVELS.map((c, i) => `<rect x="${legendX + 42 + i * 20}" y="369" width="14" height="14" rx="3" fill="${c}"/>`).join("");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-labelledby="hm-title hm-desc">
  <title id="hm-title">GitHub contributions for @${esc(data.login)}</title>
  <desc id="hm-desc">${total} contributions from ${fmt(first)} to ${fmt(last)}: ${active} active days, longest streak ${best} days, busiest day ${peak.count} contributions on ${fmt(toDate(peak.date))}. Source: ${esc(data.method || "public GitHub contribution calendar")}, snapshot ${fetched}.</desc>
  <style>
    .hm-sans { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
    .hm-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-weight: 700; }
  </style>

  <rect x="8" y="8" width="${W - 16}" height="${H - 16}" rx="20" fill="#0C0D11" stroke="#222329" stroke-width="1.5"/>

  <!-- Top Header Bar -->
  <g transform="translate(48, 42)">
    <circle cx="6" cy="6" r="4" fill="#DC2626"/>
    <circle cx="6" cy="6" r="4" fill="none" stroke="#DC2626" stroke-width="1.5">
      <animate attributeName="r" values="4;10;4" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0.8" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text class="hm-mono" x="22" y="10" font-size="12.5" letter-spacing="1.8" fill="#E4E4E7">04 · COMMIT LOG &amp; REAL ACTIVITY</text>
    <text class="hm-sans" x="0" y="58" font-size="32" fill="#FFFFFF">A year of building, <tspan fill="#DC2626">one square</tspan> at a time.</text>
    ${statsSvg}
  </g>

  <!-- Month & Day Labels -->
  <g class="hm-mono" font-size="12" fill="#A1A1AA">${monthSvg}</g>
  <g class="hm-mono" font-size="11.5" fill="#71717A" text-anchor="end">
    <text x="${GRID_X - 14}" y="${GRID_Y + STEP + 11}">Mon</text>
    <text x="${GRID_X - 14}" y="${GRID_Y + 3 * STEP + 11}">Wed</text>
    <text x="${GRID_X - 14}" y="${GRID_Y + 5 * STEP + 11}">Fri</text>
  </g>

  <!-- Cells -->
  <g>
    ${cellsSvg}
  </g>

  ${streakSvg}

  <!-- Footer Legend -->
  <g>
    <text class="hm-mono" x="48" y="380" font-size="12" fill="#71717A">Source: public GitHub contribution calendar for @${esc(data.login)} · snapshot ${fetched}</text>
    <text class="hm-mono" x="${legendX}" y="380" font-size="12" fill="#A1A1AA">Less</text>
    ${legend}
    <text class="hm-mono" x="${legendX + 42 + 5 * 20 + 6}" y="380" font-size="12" fill="#A1A1AA">More</text>
  </g>
</svg>
`;

const out = path.resolve(OUTPUT);
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, svg, "utf8");
console.log(`Wrote ${OUTPUT}: ${days.length} days, ${total} contributions (snapshot ${fetched}).`);
