#!/usr/bin/env node
/**
 * Renders assets/contribution-snake.svg for the profile README from the
 * real contribution snapshot in site/data/contributions.json.
 * Pure static, luxury dark obsidian & true crimson theme.
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
const LEVELS = ["#140508", "#4A0C16", "#8B1226", "#DC2626", "#EF4444"];

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
const fetched = data.fetchedAt ? fmt(toDate(data.fetchedAt.slice(0, 10))) : fmt(last);

/* ---- Heatmap grid ---- */
const columns = [];
let col = [];
days.forEach((d) => {
  const dow = toDate(d.date).getUTCDay();
  if (dow === 0 && col.length) {
    columns.push(col);
    col = [];
  }
  col.push(d);
});
if (col.length) columns.push(col);

const cellsSvg = columns
  .map((week, w) => {
    return week
      .map((d) => {
        const dow = toDate(d.date).getUTCDay();
        const x = GRID_X + w * STEP;
        const y = GRID_Y + dow * STEP;
        const fill = LEVELS[Math.min(d.level, LEVELS.length - 1)];
        return `<rect class="hm-c" x="${x}" y="${y}" width="${CELL}" height="${CELL}" rx="3.5" fill="${fill}" data-date="${d.date}" data-count="${d.count}" stroke="#8B1226" stroke-opacity=".12" stroke-width=".5"/>`;
      })
      .join("");
  })
  .join("\n    ");

/* ---- Month headers ---- */
const monthLabels = [];
let lastM = -1;
columns.forEach((week, w) => {
  const d0 = toDate(week[0].date);
  const m = d0.getUTCMonth();
  if (m !== lastM && d0.getUTCDate() <= 14) {
    monthLabels.push({ text: MONTHS[m], x: GRID_X + w * STEP });
    lastM = m;
  }
});
const monthSvg = monthLabels
  .map((m) => `<text x="${m.x}" y="${GRID_Y - 12}">${m.text}</text>`)
  .join("");

/* ---- Streak callout ---- */
let streakSvg = "";
if (best >= 7 && bestStart >= 0) {
  const startDay = days[bestStart];
  const endDay = days[bestEnd];
  streakSvg = `<!-- Longest Streak: ${best} days -->`;
}

/* ---- Stats blocks ---- */
const stats = [
  ["TOTAL COMMITS", `${total}`, "past 12 months"],
  ["ACTIVE DAYS", `${active}`, `${Math.round((active / days.length) * 100)}% of year`],
  ["BEST STREAK", `${best}d`, "consecutive coding"],
  ["PEAK DAY", `${peak.count}`, fmt(toDate(peak.date))],
];
const statsSvg = stats
  .map(([label, value, sub], i) => {
    const x = 580 + i * 150;
    return `<g transform="translate(${x} 54)">
      <rect x="0" y="0" width="140" height="74" rx="14" fill="#120508" stroke="#8B1226" stroke-opacity=".25" stroke-width="1" />
      <text class="hm-mono" x="14" y="24" font-size="11" font-weight="700" letter-spacing="1.2" fill="#EF4444">${label}</text>
      <text class="hm-sans" x="14" y="52" font-size="26" font-weight="800" fill="#FFFFFF">${esc(value)}</text>
      <text class="hm-mono" x="14" y="66" font-size="10" font-weight="600" fill="#94A3B8">${esc(sub)}</text>
    </g>`;
  })
  .join("\n    ");

const legendX = W - 56 - 5 * 20 - 90;
const legend = LEVELS.map((c, i) => `<rect x="${legendX + 42 + i * 20}" y="369" width="14" height="14" rx="3.5" fill="${c}" stroke="#8B1226" stroke-opacity=".2"/>`).join("");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-labelledby="hm-title hm-desc">
  <title id="hm-title">GitHub contributions for @${esc(data.login)}</title>
  <desc id="hm-desc">${total} contributions from ${fmt(first)} to ${fmt(last)}: ${active} active days, longest streak ${best} days, busiest day ${peak.count} contributions on ${fmt(toDate(peak.date))}. Source: ${esc(data.method || "public GitHub contribution calendar")}, snapshot ${fetched}.</desc>
  <defs>
    <linearGradient id="hm-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#120508"/>
      <stop offset="100%" stop-color="#090305"/>
    </linearGradient>
  </defs>
  <style>
    .hm-sans { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Inter", sans-serif; font-weight: 800; }
    .hm-mono { font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; }
  </style>

  <!-- Dark Obsidian Card Background with delicate hairline border -->
  <rect x="10" y="10" width="${W - 20}" height="${H - 20}" rx="20" fill="url(#hm-bg)" stroke="#8B1226" stroke-opacity=".25" stroke-width="1.2"/>

  <!-- Top Header Bar (No slashes!) -->
  <g transform="translate(56, 46)">
    <circle cx="6" cy="6" r="5" fill="#EF4444" />
    <text class="hm-mono" x="22" y="11" font-size="13" letter-spacing="2" fill="#EF4444">05 · COMMIT LOG &amp; REAL ACTIVITY</text>
    <text class="hm-sans" x="0" y="58" font-size="32" fill="#FFFFFF">A year of building, <tspan fill="#EF4444">one square</tspan> at a time.</text>
    ${statsSvg}
  </g>

  <!-- Month & Day Labels -->
  <g class="hm-mono" font-size="12" fill="#94A3B8">${monthSvg}</g>
  <g class="hm-mono" font-size="11.5" fill="#94A3B8" text-anchor="end">
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
    <text class="hm-mono" x="56" y="380" font-size="12" fill="#94A3B8">Source: public GitHub contribution calendar for @${esc(data.login)} · snapshot ${fetched}</text>
    <text class="hm-mono" x="${legendX}" y="380" font-size="12" fill="#94A3B8">Less</text>
    ${legend}
    <text class="hm-mono" x="${legendX + 42 + 5 * 20 + 6}" y="380" font-size="12" fill="#94A3B8">More</text>
  </g>
</svg>
`;

const out = path.resolve(OUTPUT);
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, svg, "utf8");
console.log(`Wrote ${OUTPUT}: ${days.length} days, ${total} contributions (snapshot ${fetched}).`);
