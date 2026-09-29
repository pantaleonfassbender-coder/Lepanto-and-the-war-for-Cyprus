/* Lepanto 1570–1573 — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, texts: {} };
const SIDES = { ottoman: "Ottoman", venice: "Venice", papacy: "Papacy", spain: "Spain", league: "The League", reception: "Reception" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("lepanto_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json"].map(getJSON));
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  const dj = plateOf("venier");
  view.innerHTML = `
  <div class="hero">
    <div>
      <span class="tag">1570–1573 · Cyprus · the Holy League · Lepanto</span>
      <h1>A battle won, and a war lost</h1>
      <p class="lede">On 7 October 1571 the fleet of the Holy League destroyed the Ottoman fleet at the mouth of the Gulf of Patras.
      Two months earlier Famagusta, the last Venetian fortress on Cyprus, had surrendered, and its commanders had been killed after the surrender.
      Within a year the Ottomans had a new fleet; within eighteen months Venice had made a separate peace and given up Cyprus.</p>
      <p class="readable">This apparatus follows the war through the documents of the people who fought it, lost it, translated it and remembered it.
      Every text is public domain and carried in full or in whole sections, with the original beside the English where there is one, a timeline that links into the texts, and plates from the prints of the time.</p>
      <p class="quote">"… namely, Letters … committed to Printers presses … By the which benefit of letters (now reduced into print) we see how easie a thing it is … to live for ever."
      <br><span class="fine">William Malim, dedicating his translation of the Famagusta report, London, 1572 ·
      <a href="#/text/famagusta/dedication/4">Fam. Ded. [4]</a></span></p>
    </div>
    <figure><img src="assets/plates/${dj.id}.jpg" alt="${esc(dj.titel)}">
      <figcaption>${esc(dj.caption)} <a href="#/plates">All plates →</a></figcaption></figure>
  </div>

  <h2>What the apparatus carries</h2>
  <div class="grid g2">${D.mods.shipped.map(card).join("")}</div>

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>What did the victory buy?</h3>
      <p>The captive of <em>Don Quixote</em> calls it the day the world learned the Turks were not invincible at sea, and then tells how the chance was lost at Navarino, how Venice made its peace, how La Goleta fell. <a href="#/text/cervantes/captive">DQ I.39</a></p></div>
    <div class="panel"><h3>Who writes the war?</h3>
      <p>A Venetian officer who sold himself as a slave to survive; an English protestant who translated him for the Earl of Leicester; a Spanish veteran writing fiction; an Edwardian balladeer. The Ottoman side speaks here only through them, a gap the <a href="#/sources">sources page</a> names.</p></div>
    <div class="panel"><h3>What outlasts it?</h3>
      <p>Malim thinks letters outlast pyramids. Cervantes thinks a fortress's stones are not needed to keep a memory alive. A game built on these texts is in preparation: its accounting asks what the League's victory actually secured.</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">Shipped modules can be read in full. Planned modules name their sources and wait their turn.</p>
    <h2>Shipped</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>
    <h2>Planned</h2><div class="grid g2">${D.mods.planned.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">planned</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const origName = { la: "Latin", es: "Spanish", it: "Italian" }[t.orig_sprache] || "Original";
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + English`], ["orig", origName], ["en", "English"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units" class="${t.verse ? "verse" : ""}"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", u.label ? "label" : "", u.list ? "list" : "", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a></div>
        <div>${u.titel ? `<h4>${esc(u.titel)}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="orig" lang="${esc(t.orig_sprache)}">${esc(u.orig)}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("lepanto_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>1566–1911</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>The faces of the war</h1>
    <p class="lede">Portraits, a victory print and a medal from both sides of the war, as the nineteenth century reproduced them from sixteenth-century originals.</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing or a transcription that is out of copyright, and its source is named on its page. Modern editions and translations that are in copyright are not used.</p>
    <p><b>OCR repaired against the page.</b> Texts come from digitised books. Where the machine reading fails, the text is corrected against the page image: the Latin of Malim's prayer was transcribed by eye, and where two scans of the same book differ, the cleaner one is used and the choice recorded in the build script.</p>
    <p><b>Spelling as printed.</b> Early modern English is left as the printing has it ("Iland", "souldiours"), and Latin keeps its printer's ligatures and accents.</p>
    <p><b>Working translations.</b> Where no public-domain English exists, the site gives its own working translation, marked as such and dedicated to the public domain (CC0). It is an aid to reading, not a critical translation.</p>
    <p><b>The known imbalance.</b> The Ottoman side of this war has no public-domain English sources. Until that gap is filled, the Ottomans speak here only through Venetian, Spanish and English writers, whose hostility is part of the evidence. The Texts page names the options.</p>
    <p><b>Dates.</b> The documents are followed; where modern accounts differ (the Famagusta dates are the main case), the timeline says so. England reckoned the new year from 25 March in 1572, as Malim notes in the margin of the report.</p>
    </div>
    <h2>Sources carried</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>
    <h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });
