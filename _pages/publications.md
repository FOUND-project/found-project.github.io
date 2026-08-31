---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FOUND — Publications</title>

  <style>
    :root {
      --primary-green: #1b4d3e;
      --primary-green-rgb: 27, 77, 62;
      --primary-green-dark: #0f3a26;
      --primary-green-light: #2d7a52;
      --primary-green-soft: #e8f5ef;
      --secondary-green: #4a8c73;
      --accent-green: #6bbf9a;
      --gold-accent: #d4af37;
      --white: #ffffff;
      --off-white: #fafdfa;
      --gray-50: #f8faf9;
      --gray-100: #f1f5f3;
      --gray-200: #e5ece8;
      --gray-700: #37423d;
      --gray-900: #121615;
      --shadow-sm: 0 2px 8px rgba(15, 41, 31, 0.08);
      --shadow-lg: 0 12px 32px rgba(15, 41, 31, 0.18);
      --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* make page full-width like News */
    .page, #main, .initial-content, .page__inner-wrap, .page__content, .archive {
      max-width: none !important;
      width: 100% !important;
    }

    /* ocultar el título por defecto del tema en esta página */
    .page__title {
      display: none !important;
    }

    /* nuevo título encima del logo, como en News */
  .pub-sidebar-title{
  position:absolute;
  top:72px;    /* moved down */
  left:86px;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,system-ui,sans-serif;
  font-size:1.9rem;
  font-weight:800;
  letter-spacing:-0.03em;
  color:#111827;
  z-index:30;
}

    /* CONTENEDOR PRINCIPAL */
    .pub-shell {
      max-width: var(--shell-max);
      margin: 0 auto 4rem;
      padding: 2rem var(--shell-pad);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif;
      background: linear-gradient(135deg, var(--gray-50) 0%, var(--off-white) 100%);
      min-height: 100vh;
      position: relative;
      overflow-x: hidden;
    }

    .pub-shell::before {
      content: '';
      position: fixed;
      inset: 0;
      background:
        radial-gradient(circle at 10% 20%, rgba(var(--primary-green-rgb), 0.04) 0%, transparent 50%),
        radial-gradient(circle at 90% 80%, rgba(212, 175, 55, 0.03) 0%, transparent 50%);
      pointer-events: none;
      z-index: -1;
    }

    /* LANGUAGE TOGGLE */
    .lang-toggle {
      display: flex;
      justify-content: flex-end;
      gap: 0.5rem;
      margin-bottom: 2.5rem;
      padding-right: 1.75rem;
      position: relative;
    }

    .lang-btn {
      padding: 0.5rem 1.25rem;
      border: 1px solid var(--gray-200);
      background: var(--white);
      color: var(--gray-700);
      font-size: 0.875rem;
      font-weight: 600;
      border-radius: 9999px;
      cursor: pointer;
      transition: all var(--transition-base);
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .lang-btn:hover {
      background: var(--gray-100);
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }

    .lang-btn.active {
      background: var(--primary-green);
      color: var(--white);
      border-color: var(--primary-green);
      box-shadow: var(--shadow-sm);
    }

    /* SECTION HEADERS */
    .pub-section {
      margin-bottom: 3.5rem;
      position: relative;
    }

    .pub-section-header {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1.75rem;
    }

    .pub-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      border: 1px solid rgba(27, 77, 62, 0.3);
      background: rgba(27, 77, 62, 0.1);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--primary-green);
      backdrop-filter: blur(8px);
    }

    .pub-pill::before {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--primary-green);
    }

    .pub-title {
      font-size: clamp(1.75rem, 3vw, 2.25rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--primary-green-dark);
      line-height: 1.2;
      position: relative;
      padding-bottom: 0.75rem;
    }

    .pub-title::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 60px;
      height: 3px;
      background: linear-gradient(90deg, var(--primary-green) 0%, var(--accent-green) 100%);
      border-radius: 9999px;
    }

    /* GRID & CARDS */
    .pub-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 350px), 1fr));
      gap: 2rem;
    }

    .pub-card {
      background: var(--white);
      border-radius: 20px;
      padding: 1.75rem;
      border: 1px solid var(--gray-200);
      box-shadow: var(--shadow-sm);
      transition: all var(--transition-base);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 100%;
    }

    .pub-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--primary-green) 0%, var(--accent-green) 100%);
      transform: scaleX(0);
      transform-origin: left;
      transition: transform var(--transition-base);
    }

    .pub-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-lg);
      border-color: var(--primary-green-light);
    }

    .pub-card:hover::before {
      transform: scaleX(1);
    }

    .pub-card-featured {
      grid-column: 1 / -1;
      background: linear-gradient(135deg, rgba(232, 245, 239, 0.5) 0%, rgba(255, 255, 255, 0.9) 100%);
      border: 1px solid rgba(27, 77, 62, 0.15);
      position: relative;
    }

    .pub-card-featured::after {
      content: '';
      position: absolute;
      inset: -1px;
      background: linear-gradient(120deg, rgba(255, 255, 255, 0.45), transparent 40%, transparent 60%, rgba(212, 175, 55, 0.25));
      mix-blend-mode: soft-light;
      opacity: 0.9;
      pointer-events: none;
      border-radius: 20px;
    }

    .pub-card-inner {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 2.5rem;
      align-items: start;
    }

    .pub-card-topline {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    .pub-emoji {
      font-size: 1.5rem;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
    }

    .pub-badge {
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 0.375rem 0.875rem;
      border-radius: 9999px;
      border: 1px solid rgba(27, 77, 62, 0.25);
      background: rgba(27, 77, 62, 0.08);
      color: var(--primary-green);
      transition: all var(--transition-base);
    }

    .pub-card:hover .pub-badge {
      background: rgba(27, 77, 62, 0.12);
      transform: scale(1.05);
    }

    .pub-item-title {
      margin: 0 0 0.75rem;
      font-size: 1.125rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--gray-900);
    }

    .pub-item-title a {
      color: inherit;
      text-decoration: none;
      transition: color var(--transition-base);
      position: relative;
    }

    .pub-item-title a:hover {
      color: var(--primary-green);
    }

    .pub-meta {
      font-size: 0.875rem;
      color: var(--gray-700);
      margin: 0 0 1rem;
    }

    .pub-desc {
      font-size: 0.9375rem;
      color: var(--gray-700);
      line-height: 1.6;
      margin: 0.5rem 0 0;
    }

    /* MEDIA */
    .pub-card-media {
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      border: 1px solid rgba(27, 77, 62, 0.1);
      background: var(--white);
      width: 200px;
      height: 280px;
      flex-shrink: 0;
    }

    .pub-card-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .pub-card:hover .pub-card-media img {
      transform: scale(1.05);
    }

    /* small loading helper */
    .loading { opacity: 0; }

    @media (max-width:1024px){
      .pub-card-inner{
        grid-template-columns:1fr;
        gap:1.5rem;
      }
      .pub-card-media{
        width:100%;
        height:200px;
        order:-1;
      }
    }

    @media (max-width:768px){
      .pub-shell{
        padding:1.5rem 1.25rem 3rem;
        margin-left:0;
      }
      .pub-sidebar-title{
        position:static;
        margin:0 0 1rem;
        padding:0 1.25rem;
        font-size:1.6rem;
      }
      .pub-grid{
        grid-template-columns:1fr;
      }
      .lang-toggle{
        justify-content:center;
        margin-bottom:2rem;
      }
    }

    @media (max-width:480px){
      .pub-title{font-size:1.5rem;}
      .pub-card-media{height:180px;}
    }

    /* ===== Volume 1 — index & chapter downloads ===== */
    .bk-intro{max-width:70ch;color:#4b5563;font-size:1rem;line-height:1.65;margin:0 0 1.4rem}
    .bk-bar{display:flex;flex-wrap:wrap;align-items:center;gap:.75rem;padding:.9rem 1.05rem;margin-bottom:1.25rem;
      background:linear-gradient(135deg,var(--primary-green) 0%,var(--primary-green-dark) 100%);
      border-radius:14px;box-shadow:var(--shadow-sm)}
    .bk-stats{color:#eaf6ef;font-size:.82rem;font-weight:600;
      letter-spacing:.02em;margin-right:auto}
    .bk-stats b{color:var(--gold-accent);font-weight:800}
    .bk-btn{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem .9rem;border-radius:9px;
      font-size:.8rem;font-weight:700;letter-spacing:.01em;text-decoration:none;border:1px solid transparent;
      cursor:pointer;transition:all var(--transition-base);white-space:nowrap;font-family:inherit;line-height:1.2}
    .bk-btn svg{width:14px;height:14px;flex:0 0 14px}
    .archive a.bk-btn,.archive a.bk-btn:hover,
    .page__content a.bk-btn,.page__content a.bk-btn:hover{text-decoration:none}
    .bk-bar .bk-btn{background:rgba(255,255,255,.12);color:#fff;border-color:rgba(255,255,255,.28)}
    .bk-bar .bk-btn:hover{background:rgba(255,255,255,.22);transform:translateY(-1px)}
    .bk-bar .bk-btn-gold{background:var(--gold-accent);color:#2b2000;border-color:var(--gold-accent)}
    .bk-bar .bk-btn-gold:hover{background:#e3c355;border-color:#e3c355}

    .bk-tools{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin-bottom:1rem}
    .bk-search-wrap{position:relative;flex:1 1 260px;max-width:420px}
    input[type="search"].bk-search{box-sizing:border-box}
    .bk-search{width:100%;padding:.58rem .8rem .58rem 2.1rem;border:1px solid var(--gray-200);border-radius:9px;
      font-size:.85rem;font-family:inherit;color:var(--gray-900);background:var(--white);
      transition:border-color var(--transition-base),box-shadow var(--transition-base)}
    .bk-search:focus{outline:none;border-color:var(--secondary-green);
      box-shadow:0 0 0 3px rgba(var(--primary-green-rgb),.12)}
    .bk-search-ico{position:absolute;left:.72rem;top:50%;transform:translateY(-50%);width:14px;height:14px;
      color:#9aa5a0;pointer-events:none}
    .bk-toggle-all{background:var(--white);border:1px solid var(--gray-200);color:var(--primary-green)}
    .bk-toggle-all:hover{background:var(--primary-green-soft);border-color:var(--secondary-green)}
    .bk-count{font-size:.78rem;color:#6b7280;margin-left:auto;font-weight:600}

    .bk-part{margin:1.5rem 0 .6rem;display:flex;align-items:center;gap:.7rem}
    .bk-part:first-of-type{margin-top:0}
    .bk-part-name{font-size:.72rem;font-weight:800;letter-spacing:.11em;text-transform:uppercase;
      color:var(--primary-green);white-space:nowrap}
    .bk-part-rule{flex:1;height:1px;background:linear-gradient(90deg,rgba(var(--primary-green-rgb),.28),rgba(var(--primary-green-rgb),0))}

    .bk-ch{background:var(--white);border:1px solid var(--gray-200);border-radius:12px;margin-bottom:.5rem;
      overflow:hidden;transition:border-color var(--transition-base),box-shadow var(--transition-base)}
    .bk-ch:hover{border-color:rgba(var(--primary-green-rgb),.32);box-shadow:var(--shadow-sm)}
    .bk-ch.is-open{border-color:rgba(var(--primary-green-rgb),.45);box-shadow:var(--shadow-sm)}
    .bk-ch-head{display:flex;align-items:flex-start;gap:.85rem;width:100%;padding:.85rem 1rem;background:none;
      border:0;text-align:left;cursor:pointer;font-family:inherit}
    .bk-ch-head:focus-visible{outline:2px solid var(--secondary-green);outline-offset:-2px}
    .bk-num{flex:0 0 auto;min-width:2rem;height:2rem;display:grid;place-items:center;border-radius:8px;
      background:var(--primary-green-soft);color:var(--primary-green);font-size:.8rem;font-weight:800;
      font-variant-numeric:tabular-nums;transition:all var(--transition-base)}
    .bk-ch.is-open .bk-num{background:var(--primary-green);color:var(--gold-accent)}
    .bk-ch-main{flex:1 1 auto;min-width:0}
    .bk-ch-title{display:block;font-size:.94rem;font-weight:700;line-height:1.4;color:var(--gray-900);
      margin-bottom:.2rem}
    .bk-ch-who{display:block;font-size:.78rem;line-height:1.45;color:#6b7280}
    .bk-ch-side{flex:0 0 auto;display:flex;align-items:center;gap:.7rem;padding-top:.25rem}
    .bk-ch-meta{font-size:.72rem;color:#8a938e;font-variant-numeric:tabular-nums;white-space:nowrap;text-align:right}
    .bk-chev{width:16px;height:16px;color:var(--secondary-green);transition:transform var(--transition-base);flex:0 0 16px}
    .bk-ch.is-open .bk-chev{transform:rotate(180deg)}

    .bk-ch-body{display:none;padding:0 1rem 1rem calc(1rem + 2rem + .85rem);border-top:1px solid var(--gray-100)}
    .bk-ch.is-open .bk-ch-body{display:block;animation:bkIn .22s ease}
    @keyframes bkIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}
    .bk-alt{font-size:.82rem;line-height:1.5;color:#4b5563;font-style:italic;margin:.85rem 0 0}
    .bk-acts{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.9rem}
    .bk-btn-dl{background:var(--primary-green);color:#fff;border-color:var(--primary-green)}
    .bk-btn-dl:hover{background:var(--primary-green-dark);border-color:var(--primary-green-dark);transform:translateY(-1px)}
    .bk-btn-ghost{background:var(--white);color:var(--primary-green);border-color:var(--gray-200)}
    .bk-btn-ghost:hover{background:var(--primary-green-soft);border-color:var(--secondary-green)}

    .bk-cite{margin-top:.9rem;background:var(--gray-50);border:1px solid var(--gray-100);border-left:3px solid var(--gold-accent);
      border-radius:0 10px 10px 0;padding:.75rem .9rem}
    .bk-cite-label{display:flex;align-items:center;justify-content:space-between;gap:.75rem;
      font-size:.68rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--primary-green);
      margin-bottom:.45rem}
    .bk-copy{background:var(--white);border:1px solid var(--gray-200);color:var(--primary-green);
      padding:.28rem .6rem;border-radius:7px;font-size:.68rem;font-weight:700;cursor:pointer;font-family:inherit;
      letter-spacing:.04em;transition:all var(--transition-base);white-space:nowrap}
    .bk-copy:hover{background:var(--primary-green-soft);border-color:var(--secondary-green)}
    .bk-copy.is-done{background:var(--primary-green);color:#fff;border-color:var(--primary-green)}
    .bk-cite-text{margin:0;font-size:.78rem;line-height:1.6;color:var(--gray-700);word-break:break-word}

    .bk-empty{padding:2rem 1rem;text-align:center;color:#8a938e;font-size:.88rem}

    .bk-how{margin-top:1.8rem;background:var(--white);border:1px solid var(--gray-200);border-radius:14px;
      padding:1.2rem 1.3rem;box-shadow:var(--shadow-sm)}
    .bk-how-title{display:flex;align-items:center;gap:.55rem;font-size:1.02rem;font-weight:800;
      color:var(--gray-900);margin:0 0 .5rem}
    .bk-how-title svg{width:17px;height:17px;color:var(--gold-accent);flex:0 0 17px}
    .bk-how-note{font-size:.83rem;line-height:1.6;color:#4b5563;margin:0 0 1rem;max-width:80ch}
    .bk-how-grid{display:grid;gap:.75rem}
    .bk-how-item{background:var(--gray-50);border:1px solid var(--gray-100);border-left:3px solid var(--primary-green);
      border-radius:0 10px 10px 0;padding:.75rem .9rem}
    .bk-how-item .bk-cite-label{color:var(--primary-green)}
    .bk-how-tpl{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.72rem;line-height:1.65;
      color:var(--gray-700);word-break:break-word;margin:0}
    .bk-how-tpl em{color:var(--primary-green);font-style:normal;font-weight:700}

    @media (max-width:860px){
      .bk-ch-head{flex-wrap:wrap;gap:.6rem .75rem;padding:.8rem .85rem}
      .bk-ch-main{flex:1 1 0}
      .bk-ch-side{width:100%;justify-content:space-between;padding-top:0;padding-left:calc(2rem + .75rem)}
      .bk-ch-title{font-size:.9rem}
      .bk-ch-body{padding:0 .85rem .95rem .85rem}
      .bk-bar{flex-direction:column;align-items:stretch}
      .bk-stats{margin-right:0;justify-content:center;text-align:center}
      .bk-bar .bk-btn{justify-content:center}
      .bk-count{margin-left:0;width:100%}
      .bk-acts .bk-btn{flex:1 1 auto;justify-content:center}
    }

  </style>
</head>

<body>
  <!-- nuevo título tipo “News” -->
  <div class="pub-sidebar-title">Publications</div>

  <div class="pub-shell">

    <!-- LANGUAGE TOGGLE -->
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
    </div>

    <!-- BOOK -->
    <section class="pub-section">
      <div class="pub-section-header">
        <span class="pub-pill" id="pill-book">BOOK</span>
        <h2 class="pub-title" id="title-book">The Book</h2>
      </div>

      <div class="pub-grid">
        <article class="pub-card pub-card-featured">
          <div class="pub-card-inner">
            <div class="pub-card-text">
              <div class="pub-card-topline">
                <span class="pub-emoji">📘</span>
                <span class="pub-badge" id="book-badge">Free download</span>
              </div>

              <h3 class="pub-item-title" id="book-title">
                <a href="https://www.centrogeo.org.mx/archivo/archivo-publicaciones/publicaciones-libros/3804-interpretar-la-naturaleza-para-encontrar-a-quienes-nos-faltan/file" target="_blank" rel="noopener noreferrer">
                  Interpreting Nature to Locate Those We Are Missing, Volume 1 
                </a>
              </h3>

              <p class="pub-meta" id="book-meta">
                CentroGeo &amp; SECIHTI (2024) · ISBN: 978-607-59992
              </p>

              <p class="pub-desc" id="book-desc">
                This volume brings together biological, physical, and earth sciences to design and test methods for detecting clandestine graves. Volume 2 will be presented in December 2026.
              </p>
            </div>

            <div class="pub-card-media">
              <img src="/images/the%20book.png" alt="FOUND book cover" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
          </div>
        </article>
      </div>
    </section>


    <!-- VOLUME 1 — INDEX & CHAPTER DOWNLOADS -->
    <section class="pub-section" id="volume-1">
      <div class="pub-section-header">
        <span class="pub-pill" id="bk-pill">VOLUME 1 &middot; CHAPTERS</span>
        <h2 class="pub-title" id="bk-heading">Index &amp; chapter downloads</h2>
      </div>

      <p class="bk-intro" id="bk-intro"></p>

      <div class="bk-bar">
        <div class="bk-stats" id="bk-stats"></div>
        <a class="bk-btn bk-btn-gold" id="bk-full"
           href="https://www.centrogeo.org.mx/archivo/archivo-publicaciones/publicaciones-libros/3804-interpretar-la-naturaleza-para-encontrar-a-quienes-nos-faltan/file"
           target="_blank" rel="noopener noreferrer">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          <span>Download the full volume</span>
        </a>
        <a class="bk-btn" id="bk-index-pdf" href="/files/libro-vol1/indice-capitulos.pdf" target="_blank" rel="noopener noreferrer">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
          <span>Index (PDF)</span>
        </a>
      </div>

      <div class="bk-tools">
        <div class="bk-search-wrap">
          <svg class="bk-search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="search" class="bk-search" id="bk-search" autocomplete="off">
        </div>
        <button type="button" class="bk-btn bk-toggle-all" id="bk-toggle-all"></button>
        <span class="bk-count" id="bk-count"></span>
      </div>

      <div id="bk-list"></div>

      <div class="bk-how">
        <h3 class="bk-how-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21c3-4 6-2 9-6"/><path d="M9 9h6"/><path d="M9 13h4"/><path d="M5 3h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8l-4 3V5a2 2 0 0 1 1-2z"/></svg>
          <span id="bk-how-title">How to cite</span>
        </h3>
        <p class="bk-how-note" id="bk-how-note"></p>
        <div class="bk-how-grid">
          <div class="bk-how-item">
            <div class="bk-cite-label">
              <span id="bk-how-whole-label">The whole volume</span>
              <button type="button" class="bk-copy" data-copy="whole"></button>
            </div>
            <p class="bk-cite-text" id="bk-how-whole"></p>
          </div>
          <div class="bk-how-item">
            <div class="bk-cite-label"><span id="bk-how-tpl-label">A single chapter</span></div>
            <p class="bk-how-tpl" id="bk-how-tpl"></p>
          </div>
        </div>
      </div>
    </section>

    <!-- ARTICLES -->
    <section class="pub-section">
      <div class="pub-section-header">
        <span class="pub-pill" id="pill-articles">ARTICLES</span>
        <h2 class="pub-title" id="title-articles">Articles</h2>
      </div>

<div class="pub-grid">
        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📑</span>
            <span class="pub-badge" id="a0-badge">Interview</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://www.ifcc-research.org/_files/ugd/00540a_4f9ed0d5f6444a4badcd1c8cc110dea0.pdf" target="_blank" rel="noopener noreferrer" id="a0-title">
              Interpreting the Earth: Technology, Testimony, and the Search for the Disappeared. Interview with Miguel Moctezuma.
            </a>
          </h3>
          <p class="pub-meta" id="a0-meta">
            Moctezuma, M. and Green, M. (2025) Aesthetics of the Unseen, 1(3). Florence: Istituto Fiorentino di Critica Culturale (IFCC). DOI: 10.17605/OSF.IO/75KV4
          </p>
        </article>

        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📑</span>
            <span class="pub-badge" id="a1-badge">Peer-reviewed</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://www.sciencedirect.com/science/article/abs/pii/S2352938525002289" target="_blank" rel="noopener noreferrer" id="a1-title">
              Design of spectral indices for the detection of soil pollutants associated with the disappearance of persons
            </a>
          </h3>
          <p class="pub-meta" id="a1-meta">
            J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, J.M. Madrigal-Gómez, C. Silva-Arias (2025)
          </p>
        </article>

        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📑</span>
            <span class="pub-badge" id="a2-badge">Peer-reviewed</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://www.sciencedirect.com/science/article/abs/pii/S0379073824001956" target="_blank" rel="noopener noreferrer" id="a2-title">
              Assessing Geospatial Models to Explain the Occurrence of Clandestine Graves in Mexico
            </a>
          </h3>
          <p class="pub-meta" id="a2-meta">
            J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, C. Silva-Arias (2024)
          </p>
        </article>

        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📑</span>
            <span class="pub-badge" id="a3-badge">Book chapter</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://link.springer.com/chapter/10.1007/978-3-031-61440-8_14" target="_blank" rel="noopener noreferrer" id="a3-title">
              Espacio Clandestino: A Nationwide Platform to Support Clandestine Graves Search in Mexico
            </a>
          </h3>
          <p class="pub-meta" id="a3-meta">
            J.L. Silván-Cárdenas, A.J. Alegre-Mondragón (2024)
          </p>
        </article>
      </div>
    </section>

    <!-- BLOGS -->
    <section class="pub-section">
      <div class="pub-section-header">
        <span class="pub-pill" id="pill-blogs">BLOGS &amp; INSIGHTS</span>
        <h2 class="pub-title" id="title-blogs">Blogs</h2>
      </div>

      <div class="pub-grid">
        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📝</span>
            <span class="pub-badge" id="b1-badge">Blog</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://www.frontiertechhub.org/insights/technological-responses-to-disappearance" target="_blank" rel="noopener noreferrer" id="b1-title">
              On the Frontier of Finding Peace
            </a>
          </h3>
          <p class="pub-meta" id="b1-meta">
            Mariela Garfias &amp; Frontier Tech Hub (2025)
          </p>
        </article>

        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📝</span>
            <span class="pub-badge" id="b2-badge">News story</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://www.uwe.ac.uk/news/mexico-project" target="_blank" rel="noopener noreferrer" id="b2-title">
              Academic playing role in project to find hidden graves in Mexico using drone technology
            </a>
          </h3>
          <p class="pub-meta" id="b2-meta">
            University of the West of England – Bristol (2025)
          </p>
        </article>

        <article class="pub-card">
          <div class="pub-card-topline">
            <span class="pub-emoji">📝</span>
            <span class="pub-badge" id="b3-badge">Op-ed</span>
          </div>
          <h3 class="pub-item-title">
            <a href="https://www.justsecurity.org/105181/drones-graves-mexicos-disappeared/" target="_blank" rel="noopener noreferrer" id="b3-title">
              Camera-Fitted Drones May Help Locate Graves of Mexico's Disappeared
            </a>
          </h3>
          <p class="pub-meta" id="b3-meta">
            Karina García-Reyes &amp; Miguel Moctezuma (2024)
          </p>
        </article>
      </div>
    </section>

  </div>

  <script>
    (function(){
      const STORAGE_KEY = 'found-lang';
      const LEGACY_KEY  = 'found-lang-pubs';

      const translations = {
        en: {
          'pill-book': 'BOOK',
          'title-book': 'The Book',
          'book-badge': 'Free download',
          'book-desc': 'This volume brings together biological, physical, and earth sciences to design and test methods for detecting clandestine graves. Volume 2 will be presented in December 2026.',
          'pill-articles': 'ARTICLES',
          'title-articles': 'Articles',
          'a1-badge': 'Peer-reviewed',
          'a2-badge': 'Peer-reviewed',
          'a3-badge': 'Book chapter',
          'a1-title': 'Design of spectral indices for the detection of soil pollutants associated with the disappearance of persons',
          'a1-meta': 'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, J.M. Madrigal-Gómez, C. Silva-Arias (2025)',
          'a2-title': 'Assessing Geospatial Models to Explain the Occurrence of Clandestine Graves in Mexico',
          'a2-meta': 'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, C. Silva-Arias (2024)',
          'a3-title': 'Espacio Clandestino: A Nationwide Platform to Support Clandestine Graves Search in Mexico',
          'a3-meta': 'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón (2024)',
          'pill-blogs': 'BLOGS &amp; INSIGHTS',
          'title-blogs': 'Blogs',
          'b1-badge': 'Blog',
          'b2-badge': 'News story',
          'b3-badge': 'Op-ed',
          'b1-title': 'On the Frontier of Finding Peace',
          'b1-meta': 'Mariela Garfias &amp; Frontier Tech Hub (2025)',
          'b2-title': 'Academic playing role in project to find hidden graves in Mexico using drone technology',
          'b2-meta': 'University of the West of England – Bristol (2025)',
          'b3-title': 'Camera-Fitted Drones May Help Locate Graves of Mexico\'s Disappeared',
          'b3-meta': 'Karina García-Reyes &amp; Miguel Moctezuma (2024)'
        },
        es: {
          'pill-book': 'LIBRO',
          'title-book': 'El libro',
          'book-badge': 'Arbitraje científico de capítulos; Descarga gratuita',
          'book-desc': 'Este volumen reúne ciencias biológicas, físicas y de la Tierra para diseñar y probar métodos de detección de fosas clandestinas. El Volumen 2 será presentado en diciembre de 2026.',
          'pill-articles': 'ARTÍCULOS',
          'title-articles': 'Artículos',
          'a1-badge': 'Revisado por pares',
          'a2-badge': 'Revisado por pares',
          'a3-badge': 'Capítulo de libro',
          'a1-title': 'Diseño de índices espectrales para detectar contaminantes del suelo asociados con la desaparición de personas',
          'a1-meta': 'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, J.M. Madrigal-Gómez, C. Silva-Arias (2025)',
          'a2-title': 'Evaluación de modelos geoespaciales para explicar la ocurrencia de fosas clandestinas en México',
          'a2-meta': 'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, C. Silva-Arias (2024)',
          'a3-title': 'Espacio Clandestino: una plataforma nacional para apoyar la búsqueda de fosas clandestinas en México',
          'a3-meta': 'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón (2024)',
          'pill-blogs': 'BLOGS Y REFLEXIONES',
          'title-blogs': 'Blogs',
          'b1-badge': 'Blog',
          'b2-badge': 'Nota informativa',
          'b3-badge': 'Artículo de opinión',
          'b1-title': 'En la frontera de encontrar la paz',
          'b1-meta': 'Mariela Garfias &amp; Frontier Tech Hub (2025)',
          'b2-title': 'Académica participa en proyecto para encontrar fosas ocultas en México mediante tecnología de drones',
          'b2-meta': 'University of the West of England – Bristol (2025)',
          'b3-title': 'Drones con cámara pueden ayudar a localizar fosas de personas desaparecidas en México',
          'b3-meta': 'Karina García-Reyes &amp; Miguel Moctezuma (2024)'
        }
      };

      const ids = [
        'pill-book','title-book','book-badge','book-desc',
        'pill-articles','title-articles',
        'a1-badge','a2-badge','a3-badge',
        'a1-title','a1-meta','a2-title','a2-meta','a3-title','a3-meta',
        'pill-blogs','title-blogs',
        'b1-badge','b2-badge','b3-badge',
        'b1-title','b1-meta','b2-title','b2-meta','b3-title','b3-meta'
      ];

      function setLanguage(lang){
        const dict = translations[lang] || translations.en;

        ids.forEach(id=>{
          const el = document.getElementById(id);
          if(el && dict[id] !== undefined){
            el.innerHTML = dict[id];
          }
        });

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        document.documentElement.setAttribute(
          'lang',
          lang === 'es' ? 'es' : 'en'
        );

        try{ localStorage.setItem(STORAGE_KEY, lang); }catch(e){}
      }

      document.addEventListener('DOMContentLoaded', function(){
        let saved = 'en';
        try{
          const stored = localStorage.getItem(STORAGE_KEY) || localStorage.getItem(LEGACY_KEY);
          if(stored && ['en','es'].includes(stored)) saved = stored;
        }catch(e){}

        setLanguage(saved);

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.addEventListener('click', function(){
            setLanguage(this.dataset.lang);
          });
        });
      });
    })();
  </script>
{% raw %}

  <script>
  (function(){
    var CH    = [{"n":1,"f":"cap-01-interpretando-senales-naturaleza.pdf","pg":"63–106","np":38,"mb":0.9,"es":"Interpretando señales en la naturaleza: los saberes de mujeres buscadoras influenciando las prácticas de búsqueda en Jalisco","en":"Interpreting signals in nature: buscadoras’ knowledge shaping search practices in Jalisco","who":["Miguel Moctezuma Barraza","Karina G. García Reyes"],"cite":"Moctezuma Barraza, M. and García Reyes, K. G."},{"n":2,"f":"cap-02-saberes-nacidos-del-dolor.pdf","pg":"107–132","np":26,"mb":1.3,"es":"Saberes nacidos del dolor: testimonios y propuestas de las madres buscadoras","en":"Knowledge born of pain: testimonies and proposals of the searching mothers","who":["José Darío Pereira Benítez","Eduardo Santana Castellón","Tunuari Roberto Chávez González","Lourdes Andrea Linton Padilla","Gabriel Aquiles González Ruiz"],"cite":"Pereira Benítez, J. D., Santana Castellón, E., Chávez González, T. R., Linton Padilla, L. A. and González Ruiz, G. A."},{"n":3,"f":"cap-03-madres-buscadoras-ciencia-ciudadana.pdf","pg":"133–172","np":40,"mb":2.2,"es":"Las madres buscadoras hacen ciencia ciudadana","en":"Searching mothers (madres buscadoras) do citizen science","who":["Eduardo Santana","Tunuari Roberto Chávez González","Lourdes Andrea Linton Padilla","Gabriel Aquiles González Ruiz"],"cite":"Santana, E., Chávez González, T. R., Linton Padilla, L. A. and González Ruiz, G. A."},{"n":4,"f":"cap-04-experimentacion-forense-historia-proyecto.pdf","pg":"173–196","np":24,"mb":3.5,"es":"Experimentación forense: la historia de un proyecto","en":"Forensic experimentation: the story of a project","who":["COBUPEJ"],"cite":"Comisión de Búsqueda de Personas del Estado de Jalisco (COBUPEJ)"},{"n":5,"f":"cap-05-sentir-el-viento-mirar-al-cielo.pdf","pg":"197–228","np":32,"mb":2.0,"es":"Sentir el viento y mirar al cielo para encontrarte en tierra: la lectura de condiciones climato-meteorológicas y de otros aspectos naturales como herramienta para la búsqueda en campo y la identificación de personas desaparecidas","en":"Feeling the wind and looking at the sky to find you on the ground: reading climatic-meteorological conditions and other natural features as a tool for field search and the identification of disappeared persons","who":["José Darío Pereira Benítez","Luz Adriana Vizcaíno Rodríguez"],"cite":"Pereira Benítez, J. D. and Vizcaíno Rodríguez, L. A."},{"n":6,"f":"cap-06-observacion-forense-experimental-geofisica.pdf","pg":"229–268","np":40,"mb":2.1,"es":"Observación forense experimental utilizando técnicas de prospección geofísica de alta resolución","en":"Experimental forensic observation using high-resolution geophysical prospecting techniques","who":["Anna Caccavari Garza","Martín Cárdenas Soto","Gerardo Cifuentes Nava","David Escobedo Zenil","José Antonio Martínez González","Jesús Sánchez González"],"cite":"Caccavari Garza, A., Cárdenas Soto, M., Cifuentes Nava, G., Escobedo Zenil, D., Martínez González, J. A. and Sánchez González, J."},{"n":7,"f":"cap-07-descarga-electrica-geofisica-aplicada.pdf","pg":"269–288","np":20,"mb":1.9,"es":"Una descarga eléctrica te puede revivir, creemos que también te puede encontrar. Geofísica aplicada","en":"An electric shock can revive you; we believe it can also find you. Applied geophysics","who":["Uriel Gutiérrez Mendiola","Adán González Nisino","Ciclos GIP"],"cite":"Gutiérrez Mendiola, U., González Nisino, A. and Ciclos GIP"},{"n":8,"f":"cap-08-reflejos-de-una-busqueda-gpr.pdf","pg":"289–322","np":34,"mb":3.4,"es":"Reflejos de una búsqueda: el uso del Radar de Penetración Terrestre (GPR) para la detección de inhumaciones clandestinas","en":"Reflections of a search: the use of Ground-Penetrating Radar (GPR) for the detection of clandestine burials","who":["Melina Gil Meza","Uriel Gutiérrez Mendiola","Dorian Quezada Esparza"],"cite":"Gil Meza, M., Gutiérrez Mendiola, U. and Quezada Esparza, D."},{"n":9,"f":"cap-09-morfologia-terreno-fotogrametria-drones.pdf","pg":"323–354","np":32,"mb":3.8,"es":"Morfología del terreno mediante fotogrametría con drones: oportunidades y limitaciones para la detección de fosas clandestinas","en":"Terrain morphology through drone photogrammetry: opportunities and limitations for the detection of clandestine graves","who":["Ana Josselinne Alegre Mondragón","José Luis Silván Cárdenas"],"cite":"Alegre Mondragón, A. J. and Silván Cárdenas, J. L."},{"n":10,"f":"cap-10-indices-espectrales-deteccion-fosas.pdf","pg":"355–392","np":38,"mb":2.3,"es":"Diseño y aplicación de índices espectrales para la detección de fosas clandestinas","en":"Design and application of spectral indices for the detection of clandestine graves","who":["José Luis Silván Cárdenas","Anna Josselinne Alegre Mondragón","Edgar Daniel Ramírez Aceves","David Rogelio Campos Cornejo","Maximiano Bautista Andalón"],"cite":"Silván Cárdenas, J. L., Alegre Mondragón, A. J., Ramírez Aceves, E. D., Campos Cornejo, D. R. and Bautista Andalón, M."},{"n":11,"f":"cap-11-calor-personas-que-nos-faltan-termografia.pdf","pg":"393–430","np":38,"mb":3.9,"es":"El calor de las personas que nos faltan: búsqueda de fosas clandestinas con apoyo de drones equipados con cámara termográfica","en":"The warmth of the people we are missing: searching for clandestine graves with drones equipped with a thermographic camera","who":["Sergio Alberto Quezada Godinez","Andrea Ponce Chávez","José Luis Silván Cárdenas","Tunuari Roberto Chávez González"],"cite":"Quezada Godinez, S. A., Ponce Chávez, A., Silván Cárdenas, J. L. and Chávez González, T. R."},{"n":12,"f":"cap-12-desenterrando-la-verdad-firma-quimica-suelo.pdf","pg":"431–490","np":60,"mb":6.4,"es":"Desenterrando la verdad: análisis de cambios en la firma química y características del suelo en sitios de inhumación clandestina","en":"Unearthing the truth: analysis of changes in the chemical signature and soil characteristics at clandestine burial sites","who":["Enrique Martin Ortega Higareda","Sonia Citlalli Saucedo Aguilar","Tunuari Roberto Chávez González","Luis Manuel Martínez Rivera"],"cite":"Ortega Higareda, E. M., Saucedo Aguilar, S. C., Chávez González, T. R. and Martínez Rivera, L. M."},{"n":13,"f":"cap-13-vida-despues-de-la-vida-botanica-forense.pdf","pg":"491–536","np":46,"mb":2.7,"es":"La vida después de la vida: botánica forense aplicada al estudio y detección de fosas clandestinas","en":"Life after life: forensic botany applied to the study and detection of clandestine graves","who":["Ramón Cuevas Guzmán","María L. Baca Cruz","José Guadalupe Robles Estrada","Fátima Yazmin Salcedo García","Melina Gil Meza"],"cite":"Cuevas Guzmán, R., Baca Cruz, M. L., Robles Estrada, J. G., Salcedo García, F. Y. and Gil Meza, M."},{"n":14,"f":"cap-14-entomologia-forense-insectos-fosas.pdf","pg":"537–576","np":40,"mb":1.5,"es":"¿Quiénes son los primeros en detectar una inhumación clandestina? Entomología forense: los insectos y su relación con las fosas clandestinas","en":"Who are the first to detect a clandestine burial? Forensic entomology: insects and their relationship with clandestine graves","who":["Jessica Berenice López Caro","Lizbeth G. Romero Aguilar","José L. Navarrete Heredia","María L. Baca Cruz"],"cite":"López Caro, J. B., Romero Aguilar, L. G., Navarrete Heredia, J. L. and Baca Cruz, M. L."},{"n":15,"f":"cap-15-analisis-tafonomico-comparativo.pdf","pg":"577–600","np":24,"mb":3.5,"es":"Análisis tafonómico comparativo: la deposición y su relación con la estimación del intervalo post mortem","en":"Comparative taphonomic analysis: deposition and its relationship with the estimation of the post-mortem interval","who":["Dalia Nonatzin Miranda Díaz"],"cite":"Miranda Díaz, D. N."},{"n":16,"f":"cap-16-simulacion-fosas-educacion-forense.pdf","pg":"601–632","np":32,"mb":1.9,"es":"Simulación de fosas clandestinas como estrategia didáctica en la formación del científico forense: participación del estudiantado de la Licenciatura en Ciencias Forenses en el proyecto de vinculación entre la COBUPEJ y la Universidad de Guadalajara","en":"Simulation of clandestine graves as a teaching strategy in the training of forensic scientists: participation of Forensic Science undergraduate students in the collaboration project between COBUPEJ and the University of Guadalajara","who":["Denisse Ayala Hernández","Alma Cristina Padilla de Anda","Teresita de Jesús Bustamante Flores"],"cite":"Ayala Hernández, D., Padilla de Anda, A. C. and Bustamante Flores, T. de J."},{"n":17,"f":"cap-17-interpretar-la-naturaleza-sintesis.pdf","pg":"633–666","np":36,"mb":1.3,"es":"Interpretar la naturaleza para encontrar a quienes nos faltan: integración de un estudio multidisciplinario y perspectivas","en":"Interpreting nature to find those who are missing: integration of a multidisciplinary study and perspectives","who":["Tunuari Roberto Chávez González","Enrique José Jardel Peláez","Sergio Alberto Quezada Godinez"],"cite":"Chávez González, T. R., Jardel Peláez, E. J. and Quezada Godinez, S. A."}];
    var PARTS = [{"id":"p1","es":"Madres buscadoras y ciencia ciudadana","en":"Searching mothers and citizen science","ch":[1,2,3]},{"id":"p2","es":"Planteamiento general","en":"General framing","ch":[4]},{"id":"p3","es":"Clima","en":"Climate","ch":[5]},{"id":"p4","es":"Geofísica","en":"Geophysics","ch":[6,7,8]},{"id":"p5","es":"Percepción remota","en":"Remote sensing","ch":[9,10,11]},{"id":"p6","es":"Química y biología","en":"Chemistry and biology","ch":[12,13,14]},{"id":"p7","es":"Tafonomía","en":"Taphonomy","ch":[15]},{"id":"p8","es":"Educación forense","en":"Forensic education","ch":[16]},{"id":"p9","es":"Síntesis","en":"Synthesis","ch":[17]}];
    var BOOK  = {"base":"/files/libro-vol1/","title":"Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas","editors":"V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas","imprint":"Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco","wholeCite":"Ávila Barrientos, V. H., Chávez González, T. R. and Silván Cárdenas, J. L. (eds.) (2024) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco."};
    var STR   = {"en":{"pill":"VOLUME 1 · CHAPTERS","heading":"Index & chapter downloads","intro":"The complete index of Volume 1. Every chapter can be opened in the browser or downloaded as a PDF, and each one carries its own reference in Harvard style. Chapters run from page 63 of the printed volume.","stats":"<b>17</b>&nbsp;chapters &middot; <b>600</b>&nbsp;pages &middot; free download","full":"Download the full volume","indexPdf":"Index (PDF)","search":"Filter by title, author or topic…","expandAll":"Expand all","collapseAll":"Collapse all","count":"%s of 17 shown","pp":"pp","dl":"Download PDF","openTab":"Open in browser","citeCh":"Cite this chapter (Harvard)","copy":"Copy","copied":"Copied","empty":"No chapters match that search.","howTitle":"How to cite","howNote":"References follow Harvard style. Each chapter entry gives the original Spanish title followed by an English translation in square brackets, matching the style used in FOUND's academic references. Open any chapter above to copy its full reference.","whole":"The whole volume","single":"A single chapter","tpl":"<em>Author(s)</em> (2024) &lsquo;<em>Spanish title</em>&rsquo; [<em>English title</em>], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. <em>page range</em>."},"es":{"pill":"VOLUMEN 1 · CAPÍTULOS","heading":"Índice y descarga de capítulos","intro":"El índice completo del Volumen 1. Cada capítulo puede abrirse en el navegador o descargarse en PDF, y cada uno incluye su referencia en formato Harvard. Los capítulos comienzan en la página 63 del volumen impreso.","stats":"<b>17</b>&nbsp;capítulos &middot; <b>600</b>&nbsp;páginas &middot; descarga gratuita","full":"Descargar el volumen completo","indexPdf":"Índice (PDF)","search":"Filtrar por título, autoría o tema…","expandAll":"Abrir todo","collapseAll":"Cerrar todo","count":"%s de 17 visibles","pp":"págs.","dl":"Descargar PDF","openTab":"Abrir en el navegador","citeCh":"Cómo citar este capítulo (Harvard)","copy":"Copiar","copied":"Copiado","empty":"Ningún capítulo coincide con esa búsqueda.","howTitle":"Cómo citar","howNote":"Las referencias siguen el formato Harvard. Cada entrada ofrece el título original en español seguido de su traducción al inglés entre corchetes, siguiendo el estilo empleado en las referencias académicas de FOUND. Abre cualquier capítulo para copiar su referencia completa.","whole":"El volumen completo","single":"Un capítulo","tpl":"<em>Autoría</em> (2024) &lsquo;<em>Título en español</em>&rsquo; [<em>Título en inglés</em>], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. <em>páginas</em>."}};

    var open = {};              // chapter number -> open?
    var lang = 'en';
    var listEl, searchEl, countEl, toggleEl;

    function esc(s){
      return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
                      .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
    }
    function names(who, lg){
      if(who.length === 1) return who[0];
      var last = who[who.length-1], head = who.slice(0,-1).join(', ');
      return head + (lg === 'es' ? ' y ' : ' and ') + last;
    }
    function citeOf(c){
      return c.cite + " (2024) '" + c.es + "' [" + c.en + "], in " + BOOK.editors +
             " (eds.) " + BOOK.title + ". " + BOOK.imprint + ", pp. " + c.pg + ".";
    }
    function title(c){ return lang === 'es' ? c.es : c.en; }
    function alt(c){   return lang === 'es' ? c.en : c.es; }

    var ICON_DL   = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';
    var ICON_OPEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>';
    var ICON_CHEV = '<svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>';

    function chapterHTML(c){
      var t = STR[lang];
      var isOpen = !!open[c.n];
      var url = BOOK.base + c.f;
      return '<article class="bk-ch' + (isOpen ? ' is-open' : '') + '" data-n="' + c.n + '" ' +
               'data-find="' + esc((c.es + ' ' + c.en + ' ' + c.who.join(' ')).toLowerCase()) + '">' +
          '<button type="button" class="bk-ch-head" aria-expanded="' + isOpen + '">' +
            '<span class="bk-num">' + (c.n < 10 ? '0' + c.n : c.n) + '</span>' +
            '<span class="bk-ch-main">' +
              '<span class="bk-ch-title">' + esc(title(c)) + '</span>' +
              '<span class="bk-ch-who">' + esc(names(c.who, lang)) + '</span>' +
            '</span>' +
            '<span class="bk-ch-side">' +
              '<span class="bk-ch-meta">pp. ' + c.pg + '<br>' + c.np + ' ' + t.pp + ' &middot; ' + c.mb.toFixed(1) + ' MB</span>' +
              ICON_CHEV +
            '</span>' +
          '</button>' +
          '<div class="bk-ch-body">' +
            '<p class="bk-alt">' + esc(alt(c)) + '</p>' +
            '<div class="bk-acts">' +
              '<a class="bk-btn bk-btn-dl" href="' + url + '" download>' + ICON_DL + '<span>' + t.dl + '</span></a>' +
              '<a class="bk-btn bk-btn-ghost" href="' + url + '" target="_blank" rel="noopener noreferrer">' + ICON_OPEN + '<span>' + t.openTab + '</span></a>' +
            '</div>' +
            '<div class="bk-cite">' +
              '<div class="bk-cite-label"><span>' + t.citeCh + '</span>' +
                '<button type="button" class="bk-copy" data-copy="' + c.n + '">' + t.copy + '</button></div>' +
              '<p class="bk-cite-text">' + esc(citeOf(c)) + '</p>' +
            '</div>' +
          '</div>' +
        '</article>';
    }

    function render(){
      var t = STR[lang], html = '';
      PARTS.forEach(function(p){
        html += '<div class="bk-part" data-part="' + p.id + '">' +
                  '<span class="bk-part-name">' + esc(lang === 'es' ? p.es : p.en) + '</span>' +
                  '<span class="bk-part-rule"></span></div>';
        p.ch.forEach(function(n){
          var c = CH.filter(function(x){ return x.n === n; })[0];
          if(c) html += chapterHTML(c);
        });
      });
      listEl.innerHTML = html + '<div class="bk-empty" id="bk-empty" style="display:none">' + t.empty + '</div>';

      document.getElementById('bk-pill').textContent        = t.pill;
      document.getElementById('bk-heading').textContent     = t.heading;
      document.getElementById('bk-intro').textContent       = t.intro;
      document.getElementById('bk-stats').innerHTML         = t.stats;
      document.querySelector('#bk-full span').textContent   = t.full;
      document.querySelector('#bk-index-pdf span').textContent = t.indexPdf;
      searchEl.placeholder                                  = t.search;
      searchEl.setAttribute('aria-label', t.search);
      document.getElementById('bk-how-title').textContent   = t.howTitle;
      document.getElementById('bk-how-note').textContent    = t.howNote;
      document.getElementById('bk-how-whole-label').textContent = t.whole;
      document.getElementById('bk-how-whole').textContent   = BOOK.wholeCite;
      document.getElementById('bk-how-tpl-label').textContent = t.single;
      document.getElementById('bk-how-tpl').innerHTML       = t.tpl;
      document.querySelector('[data-copy="whole"]').textContent = t.copy;

      filter();
      syncToggleAll();
    }

    function filter(){
      var q = (searchEl.value || '').trim().toLowerCase();
      var shown = 0;
      PARTS.forEach(function(p){
        var head = listEl.querySelector('[data-part="' + p.id + '"]');
        var any = false;
        p.ch.forEach(function(n){
          var el = listEl.querySelector('.bk-ch[data-n="' + n + '"]');
          if(!el) return;
          var hit = !q || el.getAttribute('data-find').indexOf(q) !== -1;
          el.style.display = hit ? '' : 'none';
          if(hit){ any = true; shown++; }
        });
        if(head) head.style.display = any ? '' : 'none';
      });
      var empty = document.getElementById('bk-empty');
      if(empty) empty.style.display = shown ? 'none' : '';
      countEl.textContent = STR[lang].count.replace('%s', shown);
    }

    function allOpen(){
      var vis = [].slice.call(listEl.querySelectorAll('.bk-ch')).filter(function(e){
        return e.style.display !== 'none';
      });
      return vis.length > 0 && vis.every(function(e){ return e.classList.contains('is-open'); });
    }
    function syncToggleAll(){
      toggleEl.textContent = allOpen() ? STR[lang].collapseAll : STR[lang].expandAll;
    }

    function copyText(txt, btn){
      var done = function(){
        var old = btn.textContent;
        btn.textContent = STR[lang].copied;
        btn.classList.add('is-done');
        setTimeout(function(){ btn.textContent = old; btn.classList.remove('is-done'); }, 1600);
      };
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(txt).then(done, function(){ fallback(txt, done); });
      } else { fallback(txt, done); }
    }
    function fallback(txt, done){
      var ta = document.createElement('textarea');
      ta.value = txt;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:absolute;left:-9999px;top:0';
      document.body.appendChild(ta);
      ta.select();
      try{ document.execCommand('copy'); done(); }catch(e){}
      document.body.removeChild(ta);
    }

    function boot(){
      listEl   = document.getElementById('bk-list');
      searchEl = document.getElementById('bk-search');
      countEl  = document.getElementById('bk-count');
      toggleEl = document.getElementById('bk-toggle-all');
      if(!listEl) return;

      try{
        var s = localStorage.getItem('found-lang') || localStorage.getItem('found-lang-pubs');
        if(s === 'es' || s === 'en') lang = s;
      }catch(e){}

      render();

      listEl.addEventListener('click', function(ev){
        var copy = ev.target.closest('.bk-copy');
        if(copy){
          ev.preventDefault(); ev.stopPropagation();
          var c = CH.filter(function(x){ return x.n === +copy.getAttribute('data-copy'); })[0];
          if(c) copyText(citeOf(c), copy);
          return;
        }
        var head = ev.target.closest('.bk-ch-head');
        if(!head) return;
        var art = head.closest('.bk-ch');
        var n = +art.getAttribute('data-n');
        open[n] = !art.classList.contains('is-open');
        art.classList.toggle('is-open', open[n]);
        head.setAttribute('aria-expanded', String(open[n]));
        syncToggleAll();
      });

      var wholeBtn = document.querySelector('[data-copy="whole"]');
      if(wholeBtn) wholeBtn.addEventListener('click', function(){ copyText(BOOK.wholeCite, wholeBtn); });

      searchEl.addEventListener('input', function(){ filter(); syncToggleAll(); });

      toggleEl.addEventListener('click', function(){
        var target = !allOpen();
        [].slice.call(listEl.querySelectorAll('.bk-ch')).forEach(function(el){
          if(el.style.display === 'none') return;
          var n = +el.getAttribute('data-n');
          open[n] = target;
          el.classList.toggle('is-open', target);
          var h = el.querySelector('.bk-ch-head');
          if(h) h.setAttribute('aria-expanded', String(target));
        });
        syncToggleAll();
      });

      document.querySelectorAll('.lang-btn').forEach(function(btn){
        btn.addEventListener('click', function(){
          var l = this.dataset.lang;
          if(l !== 'en' && l !== 'es') return;
          lang = l;
          render();
        });
      });
    }

    if(document.readyState === 'loading'){
      document.addEventListener('DOMContentLoaded', boot);
    } else { boot(); }
  })();
  </script>

{% endraw %}
</body>
</html>
