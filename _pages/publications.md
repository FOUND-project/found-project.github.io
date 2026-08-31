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
    .bk-bar{display:flex;flex-wrap:wrap;align-items:baseline;gap:.4rem 1rem;padding:.9rem 1.15rem;margin-bottom:1.25rem;
      background:linear-gradient(135deg,var(--primary-green) 0%,var(--primary-green-dark) 100%);
      border-radius:14px;box-shadow:var(--shadow-sm)}
    .bk-bar-title{color:var(--gold-accent);font-size:1.02rem;font-weight:800;letter-spacing:.01em}
    .bk-stats{color:#cfe3d6;font-size:.82rem;font-weight:600;letter-spacing:.02em}
    .bk-btn{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem .9rem;border-radius:9px;
      font-size:.8rem;font-weight:700;letter-spacing:.01em;text-decoration:none;border:1px solid transparent;
      cursor:pointer;transition:all var(--transition-base);white-space:nowrap;font-family:inherit;line-height:1.2}
    .bk-btn svg{width:14px;height:14px;flex:0 0 14px}
    .archive a.bk-btn,.archive a.bk-btn:hover,
    .page__content a.bk-btn,.page__content a.bk-btn:hover{text-decoration:none}
    .bk-tools{display:none;flex-wrap:wrap;gap:.6rem;align-items:center;margin-bottom:1rem}
    .bk-js .bk-tools{display:flex}
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
    /* native <details> so the list works with no JS at all */
    .bk-ch{background:var(--white);border:1px solid var(--gray-200);border-radius:12px;margin-bottom:.5rem;
      overflow:hidden;transition:border-color var(--transition-base),box-shadow var(--transition-base)}
    .bk-ch:hover{border-color:rgba(var(--primary-green-rgb),.32);box-shadow:var(--shadow-sm)}
    .bk-ch[open]{border-color:rgba(var(--primary-green-rgb),.45);box-shadow:var(--shadow-sm)}
    .bk-ch-head{display:flex;align-items:flex-start;gap:.85rem;width:100%;padding:.85rem 1rem;
      text-align:left;cursor:pointer;font-family:inherit;list-style:none}
    .bk-ch-head::-webkit-details-marker{display:none}
    .bk-ch-head::marker{content:""}
    .bk-ch-head:focus-visible{outline:2px solid var(--secondary-green);outline-offset:-2px}
    .bk-num{flex:0 0 auto;min-width:2rem;height:2rem;display:grid;place-items:center;border-radius:8px;
      background:var(--primary-green-soft);color:var(--primary-green);font-size:.8rem;font-weight:800;
      font-variant-numeric:tabular-nums;transition:all var(--transition-base)}
    .bk-ch[open] .bk-num{background:var(--primary-green);color:var(--gold-accent)}
    .bk-ch-main{flex:1 1 auto;min-width:0}
    .bk-ch-title{display:block;font-size:.94rem;font-weight:700;line-height:1.4;color:var(--gray-900);
      margin-bottom:.2rem}
    .bk-ch-who{display:block;font-size:.78rem;line-height:1.45;color:#6b7280}
    .bk-ch-side{flex:0 0 auto;display:flex;align-items:center;gap:.7rem;padding-top:.25rem}
    .bk-ch-meta{font-size:.72rem;color:#8a938e;font-variant-numeric:tabular-nums;white-space:nowrap;text-align:right}
    .bk-ch-pages{display:block}
    .bk-ch-size{display:block}
    .bk-chev{width:16px;height:16px;color:var(--secondary-green);transition:transform var(--transition-base);flex:0 0 16px}
    .bk-ch[open] .bk-chev{transform:rotate(180deg)}
    .bk-ch-body{padding:0 1rem 1rem calc(1rem + 2rem + .85rem);border-top:1px solid var(--gray-100);
      animation:bkIn .22s ease}
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
    .bk-copy{display:none;background:var(--white);border:1px solid var(--gray-200);color:var(--primary-green);
      padding:.28rem .6rem;border-radius:7px;font-size:.68rem;font-weight:700;cursor:pointer;font-family:inherit;
      letter-spacing:.04em;transition:all var(--transition-base);white-space:nowrap}
    .bk-js .bk-copy{display:inline-block}
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
                CentroGeo &amp; SECIHTI · ISBN: 978-607-59992
              </p>

              <p class="pub-desc" id="book-desc">
                This volume brings together biological, physical, and earth sciences to design and test methods for detecting clandestine graves. Volume 2 and Volume 3 will be presented in December 2026.
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
        <span class="pub-pill" data-en="VOLUME 1 · CHAPTERS" data-es="VOLUMEN 1 · CAPÍTULOS">VOLUME 1 · CHAPTERS</span>
        <h2 class="pub-title" data-en="Index &amp; chapter downloads" data-es="Índice y descarga de capítulos">Index &amp; chapter downloads</h2>
      </div>

      <p class="bk-intro" data-en="The complete index of Volume 1. Every chapter can be opened in the browser or downloaded as a PDF, and each one carries its own reference in Harvard style. Chapters run from page 63 of the printed volume." data-es="El índice completo del Volumen 1. Cada capítulo puede abrirse en el navegador o descargarse en PDF, y cada uno incluye su referencia en formato Harvard. Los capítulos comienzan en la página 63 del volumen impreso.">The complete index of Volume 1. Every chapter can be opened in the browser or downloaded as a PDF, and each one carries its own reference in Harvard style. Chapters run from page 63 of the printed volume.</p>

      <div class="bk-bar">
        <div class="bk-bar-title" data-en="Chapter downloads" data-es="Descarga de capítulos">Chapter downloads</div>
        <div class="bk-stats" data-en="17 chapters · 600 pages · free download" data-es="17 capítulos · 600 páginas · descarga gratuita">17 chapters · 600 pages · free download</div>
      </div>

      <div class="bk-tools">
        <div class="bk-search-wrap">
          <svg class="bk-search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="search" class="bk-search" id="bk-search" autocomplete="off" data-ph-en="Filter by title, author or topic…" data-ph-es="Filtrar por título, autoría o tema…">
        </div>
        <button type="button" class="bk-btn bk-toggle-all" id="bk-toggle-all" data-en="Expand all" data-es="Abrir todo">Expand all</button>
        <span class="bk-count" id="bk-count"></span>
      </div>

      <div id="bk-list">
      <div class="bk-part" data-part="p1"><span class="bk-part-name" data-en="Searching mothers and citizen science" data-es="Madres buscadoras y ciencia ciudadana">Searching mothers and citizen science</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="1" data-find="interpretando señales en la naturaleza: los saberes de mujeres buscadoras influenciando las prácticas de búsqueda en jalisco interpreting signals in nature: buscadoras’ knowledge shaping search practices in jalisco miguel moctezuma barraza karina g. garcía reyes">
        <summary class="bk-ch-head">
          <span class="bk-num">01</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Interpreting signals in nature: buscadoras’ knowledge shaping search practices in Jalisco" data-es="Interpretando señales en la naturaleza: los saberes de mujeres buscadoras influenciando las prácticas de búsqueda en Jalisco">Interpreting signals in nature: buscadoras’ knowledge shaping search practices in Jalisco</span><span class="bk-ch-who" data-en="Miguel Moctezuma Barraza and Karina G. García Reyes" data-es="Miguel Moctezuma Barraza y Karina G. García Reyes">Miguel Moctezuma Barraza and Karina G. García Reyes</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 63–106</span><span class="bk-ch-size" data-en="38 pp · 0.9 MB" data-es="38 págs. · 0.9 MB">38 pp · 0.9 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Interpretando señales en la naturaleza: los saberes de mujeres buscadoras influenciando las prácticas de búsqueda en Jalisco" data-es="Interpreting signals in nature: buscadoras’ knowledge shaping search practices in Jalisco">Interpretando señales en la naturaleza: los saberes de mujeres buscadoras influenciando las prácticas de búsqueda en Jalisco</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-01-interpretando-senales-naturaleza.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-01-interpretando-senales-naturaleza.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Moctezuma Barraza, M. and García Reyes, K. G. (2024) 'Interpretando señales en la naturaleza: los saberes de mujeres buscadoras influenciando las prácticas de búsqueda en Jalisco' [Interpreting signals in nature: buscadoras’ knowledge shaping search practices in Jalisco], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 63–106.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="2" data-find="saberes nacidos del dolor: testimonios y propuestas de las madres buscadoras knowledge born of pain: testimonies and proposals of the searching mothers josé darío pereira benítez eduardo santana castellón tunuari roberto chávez gonzález lourdes andrea linton padilla gabriel aquiles gonzález ruiz">
        <summary class="bk-ch-head">
          <span class="bk-num">02</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Knowledge born of pain: testimonies and proposals of the searching mothers" data-es="Saberes nacidos del dolor: testimonios y propuestas de las madres buscadoras">Knowledge born of pain: testimonies and proposals of the searching mothers</span><span class="bk-ch-who" data-en="José Darío Pereira Benítez, Eduardo Santana Castellón, Tunuari Roberto Chávez González, Lourdes Andrea Linton Padilla and Gabriel Aquiles González Ruiz" data-es="José Darío Pereira Benítez, Eduardo Santana Castellón, Tunuari Roberto Chávez González, Lourdes Andrea Linton Padilla y Gabriel Aquiles González Ruiz">José Darío Pereira Benítez, Eduardo Santana Castellón, Tunuari Roberto Chávez González, Lourdes Andrea Linton Padilla and Gabriel Aquiles González Ruiz</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 107–132</span><span class="bk-ch-size" data-en="26 pp · 1.3 MB" data-es="26 págs. · 1.3 MB">26 pp · 1.3 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Saberes nacidos del dolor: testimonios y propuestas de las madres buscadoras" data-es="Knowledge born of pain: testimonies and proposals of the searching mothers">Saberes nacidos del dolor: testimonios y propuestas de las madres buscadoras</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-02-saberes-nacidos-del-dolor.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-02-saberes-nacidos-del-dolor.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Pereira Benítez, J. D., Santana Castellón, E., Chávez González, T. R., Linton Padilla, L. A. and González Ruiz, G. A. (2024) 'Saberes nacidos del dolor: testimonios y propuestas de las madres buscadoras' [Knowledge born of pain: testimonies and proposals of the searching mothers], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 107–132.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="3" data-find="las madres buscadoras hacen ciencia ciudadana searching mothers (madres buscadoras) do citizen science eduardo santana tunuari roberto chávez gonzález lourdes andrea linton padilla gabriel aquiles gonzález ruiz">
        <summary class="bk-ch-head">
          <span class="bk-num">03</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Searching mothers (madres buscadoras) do citizen science" data-es="Las madres buscadoras hacen ciencia ciudadana">Searching mothers (madres buscadoras) do citizen science</span><span class="bk-ch-who" data-en="Eduardo Santana, Tunuari Roberto Chávez González, Lourdes Andrea Linton Padilla and Gabriel Aquiles González Ruiz" data-es="Eduardo Santana, Tunuari Roberto Chávez González, Lourdes Andrea Linton Padilla y Gabriel Aquiles González Ruiz">Eduardo Santana, Tunuari Roberto Chávez González, Lourdes Andrea Linton Padilla and Gabriel Aquiles González Ruiz</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 133–172</span><span class="bk-ch-size" data-en="40 pp · 2.2 MB" data-es="40 págs. · 2.2 MB">40 pp · 2.2 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Las madres buscadoras hacen ciencia ciudadana" data-es="Searching mothers (madres buscadoras) do citizen science">Las madres buscadoras hacen ciencia ciudadana</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-03-madres-buscadoras-ciencia-ciudadana.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-03-madres-buscadoras-ciencia-ciudadana.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Santana, E., Chávez González, T. R., Linton Padilla, L. A. and González Ruiz, G. A. (2024) 'Las madres buscadoras hacen ciencia ciudadana' [Searching mothers (madres buscadoras) do citizen science], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 133–172.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p2"><span class="bk-part-name" data-en="General framing" data-es="Planteamiento general">General framing</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="4" data-find="experimentación forense: la historia de un proyecto forensic experimentation: the story of a project cobupej">
        <summary class="bk-ch-head">
          <span class="bk-num">04</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Forensic experimentation: the story of a project" data-es="Experimentación forense: la historia de un proyecto">Forensic experimentation: the story of a project</span><span class="bk-ch-who" data-en="COBUPEJ" data-es="COBUPEJ">COBUPEJ</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 173–196</span><span class="bk-ch-size" data-en="24 pp · 3.5 MB" data-es="24 págs. · 3.5 MB">24 pp · 3.5 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Experimentación forense: la historia de un proyecto" data-es="Forensic experimentation: the story of a project">Experimentación forense: la historia de un proyecto</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-04-experimentacion-forense-historia-proyecto.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-04-experimentacion-forense-historia-proyecto.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Comisión de Búsqueda de Personas del Estado de Jalisco (COBUPEJ) (2024) 'Experimentación forense: la historia de un proyecto' [Forensic experimentation: the story of a project], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 173–196.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p3"><span class="bk-part-name" data-en="Climate" data-es="Clima">Climate</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="5" data-find="sentir el viento y mirar al cielo para encontrarte en tierra: la lectura de condiciones climato-meteorológicas y de otros aspectos naturales como herramienta para la búsqueda en campo y la identificación de personas desaparecidas feeling the wind and looking at the sky to find you on the ground: reading climatic-meteorological conditions and other natural features as a tool for field search and the identification of disappeared persons josé darío pereira benítez luz adriana vizcaíno rodríguez">
        <summary class="bk-ch-head">
          <span class="bk-num">05</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Feeling the wind and looking at the sky to find you on the ground: reading climatic-meteorological conditions and other natural features as a tool for field search and the identification of disappeared persons" data-es="Sentir el viento y mirar al cielo para encontrarte en tierra: la lectura de condiciones climato-meteorológicas y de otros aspectos naturales como herramienta para la búsqueda en campo y la identificación de personas desaparecidas">Feeling the wind and looking at the sky to find you on the ground: reading climatic-meteorological conditions and other natural features as a tool for field search and the identification of disappeared persons</span><span class="bk-ch-who" data-en="José Darío Pereira Benítez and Luz Adriana Vizcaíno Rodríguez" data-es="José Darío Pereira Benítez y Luz Adriana Vizcaíno Rodríguez">José Darío Pereira Benítez and Luz Adriana Vizcaíno Rodríguez</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 197–228</span><span class="bk-ch-size" data-en="32 pp · 2.0 MB" data-es="32 págs. · 2.0 MB">32 pp · 2.0 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Sentir el viento y mirar al cielo para encontrarte en tierra: la lectura de condiciones climato-meteorológicas y de otros aspectos naturales como herramienta para la búsqueda en campo y la identificación de personas desaparecidas" data-es="Feeling the wind and looking at the sky to find you on the ground: reading climatic-meteorological conditions and other natural features as a tool for field search and the identification of disappeared persons">Sentir el viento y mirar al cielo para encontrarte en tierra: la lectura de condiciones climato-meteorológicas y de otros aspectos naturales como herramienta para la búsqueda en campo y la identificación de personas desaparecidas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-05-sentir-el-viento-mirar-al-cielo.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-05-sentir-el-viento-mirar-al-cielo.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Pereira Benítez, J. D. and Vizcaíno Rodríguez, L. A. (2024) 'Sentir el viento y mirar al cielo para encontrarte en tierra: la lectura de condiciones climato-meteorológicas y de otros aspectos naturales como herramienta para la búsqueda en campo y la identificación de personas desaparecidas' [Feeling the wind and looking at the sky to find you on the ground: reading climatic-meteorological conditions and other natural features as a tool for field search and the identification of disappeared persons], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 197–228.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p4"><span class="bk-part-name" data-en="Geophysics" data-es="Geofísica">Geophysics</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="6" data-find="observación forense experimental utilizando técnicas de prospección geofísica de alta resolución experimental forensic observation using high-resolution geophysical prospecting techniques anna caccavari garza martín cárdenas soto gerardo cifuentes nava david escobedo zenil josé antonio martínez gonzález jesús sánchez gonzález">
        <summary class="bk-ch-head">
          <span class="bk-num">06</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Experimental forensic observation using high-resolution geophysical prospecting techniques" data-es="Observación forense experimental utilizando técnicas de prospección geofísica de alta resolución">Experimental forensic observation using high-resolution geophysical prospecting techniques</span><span class="bk-ch-who" data-en="Anna Caccavari Garza, Martín Cárdenas Soto, Gerardo Cifuentes Nava, David Escobedo Zenil, José Antonio Martínez González and Jesús Sánchez González" data-es="Anna Caccavari Garza, Martín Cárdenas Soto, Gerardo Cifuentes Nava, David Escobedo Zenil, José Antonio Martínez González y Jesús Sánchez González">Anna Caccavari Garza, Martín Cárdenas Soto, Gerardo Cifuentes Nava, David Escobedo Zenil, José Antonio Martínez González and Jesús Sánchez González</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 229–268</span><span class="bk-ch-size" data-en="40 pp · 2.1 MB" data-es="40 págs. · 2.1 MB">40 pp · 2.1 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Observación forense experimental utilizando técnicas de prospección geofísica de alta resolución" data-es="Experimental forensic observation using high-resolution geophysical prospecting techniques">Observación forense experimental utilizando técnicas de prospección geofísica de alta resolución</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-06-observacion-forense-experimental-geofisica.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-06-observacion-forense-experimental-geofisica.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Caccavari Garza, A., Cárdenas Soto, M., Cifuentes Nava, G., Escobedo Zenil, D., Martínez González, J. A. and Sánchez González, J. (2024) 'Observación forense experimental utilizando técnicas de prospección geofísica de alta resolución' [Experimental forensic observation using high-resolution geophysical prospecting techniques], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 229–268.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="7" data-find="una descarga eléctrica te puede revivir, creemos que también te puede encontrar. geofísica aplicada an electric shock can revive you; we believe it can also find you. applied geophysics uriel gutiérrez mendiola adán gonzález nisino ciclos gip">
        <summary class="bk-ch-head">
          <span class="bk-num">07</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="An electric shock can revive you; we believe it can also find you. Applied geophysics" data-es="Una descarga eléctrica te puede revivir, creemos que también te puede encontrar. Geofísica aplicada">An electric shock can revive you; we believe it can also find you. Applied geophysics</span><span class="bk-ch-who" data-en="Uriel Gutiérrez Mendiola, Adán González Nisino and Ciclos GIP" data-es="Uriel Gutiérrez Mendiola, Adán González Nisino y Ciclos GIP">Uriel Gutiérrez Mendiola, Adán González Nisino and Ciclos GIP</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 269–288</span><span class="bk-ch-size" data-en="20 pp · 1.9 MB" data-es="20 págs. · 1.9 MB">20 pp · 1.9 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Una descarga eléctrica te puede revivir, creemos que también te puede encontrar. Geofísica aplicada" data-es="An electric shock can revive you; we believe it can also find you. Applied geophysics">Una descarga eléctrica te puede revivir, creemos que también te puede encontrar. Geofísica aplicada</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-07-descarga-electrica-geofisica-aplicada.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-07-descarga-electrica-geofisica-aplicada.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Gutiérrez Mendiola, U., González Nisino, A. and Ciclos GIP (2024) 'Una descarga eléctrica te puede revivir, creemos que también te puede encontrar. Geofísica aplicada' [An electric shock can revive you; we believe it can also find you. Applied geophysics], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 269–288.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="8" data-find="reflejos de una búsqueda: el uso del radar de penetración terrestre (gpr) para la detección de inhumaciones clandestinas reflections of a search: the use of ground-penetrating radar (gpr) for the detection of clandestine burials melina gil meza uriel gutiérrez mendiola dorian quezada esparza">
        <summary class="bk-ch-head">
          <span class="bk-num">08</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Reflections of a search: the use of Ground-Penetrating Radar (GPR) for the detection of clandestine burials" data-es="Reflejos de una búsqueda: el uso del Radar de Penetración Terrestre (GPR) para la detección de inhumaciones clandestinas">Reflections of a search: the use of Ground-Penetrating Radar (GPR) for the detection of clandestine burials</span><span class="bk-ch-who" data-en="Melina Gil Meza, Uriel Gutiérrez Mendiola and Dorian Quezada Esparza" data-es="Melina Gil Meza, Uriel Gutiérrez Mendiola y Dorian Quezada Esparza">Melina Gil Meza, Uriel Gutiérrez Mendiola and Dorian Quezada Esparza</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 289–322</span><span class="bk-ch-size" data-en="34 pp · 3.4 MB" data-es="34 págs. · 3.4 MB">34 pp · 3.4 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Reflejos de una búsqueda: el uso del Radar de Penetración Terrestre (GPR) para la detección de inhumaciones clandestinas" data-es="Reflections of a search: the use of Ground-Penetrating Radar (GPR) for the detection of clandestine burials">Reflejos de una búsqueda: el uso del Radar de Penetración Terrestre (GPR) para la detección de inhumaciones clandestinas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-08-reflejos-de-una-busqueda-gpr.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-08-reflejos-de-una-busqueda-gpr.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Gil Meza, M., Gutiérrez Mendiola, U. and Quezada Esparza, D. (2024) 'Reflejos de una búsqueda: el uso del Radar de Penetración Terrestre (GPR) para la detección de inhumaciones clandestinas' [Reflections of a search: the use of Ground-Penetrating Radar (GPR) for the detection of clandestine burials], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 289–322.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p5"><span class="bk-part-name" data-en="Remote sensing" data-es="Percepción remota">Remote sensing</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="9" data-find="morfología del terreno mediante fotogrametría con drones: oportunidades y limitaciones para la detección de fosas clandestinas terrain morphology through drone photogrammetry: opportunities and limitations for the detection of clandestine graves ana josselinne alegre mondragón josé luis silván cárdenas">
        <summary class="bk-ch-head">
          <span class="bk-num">09</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Terrain morphology through drone photogrammetry: opportunities and limitations for the detection of clandestine graves" data-es="Morfología del terreno mediante fotogrametría con drones: oportunidades y limitaciones para la detección de fosas clandestinas">Terrain morphology through drone photogrammetry: opportunities and limitations for the detection of clandestine graves</span><span class="bk-ch-who" data-en="Ana Josselinne Alegre Mondragón and José Luis Silván Cárdenas" data-es="Ana Josselinne Alegre Mondragón y José Luis Silván Cárdenas">Ana Josselinne Alegre Mondragón and José Luis Silván Cárdenas</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 323–354</span><span class="bk-ch-size" data-en="32 pp · 3.8 MB" data-es="32 págs. · 3.8 MB">32 pp · 3.8 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Morfología del terreno mediante fotogrametría con drones: oportunidades y limitaciones para la detección de fosas clandestinas" data-es="Terrain morphology through drone photogrammetry: opportunities and limitations for the detection of clandestine graves">Morfología del terreno mediante fotogrametría con drones: oportunidades y limitaciones para la detección de fosas clandestinas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-09-morfologia-terreno-fotogrametria-drones.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-09-morfologia-terreno-fotogrametria-drones.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Alegre Mondragón, A. J. and Silván Cárdenas, J. L. (2024) 'Morfología del terreno mediante fotogrametría con drones: oportunidades y limitaciones para la detección de fosas clandestinas' [Terrain morphology through drone photogrammetry: opportunities and limitations for the detection of clandestine graves], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 323–354.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="10" data-find="diseño y aplicación de índices espectrales para la detección de fosas clandestinas design and application of spectral indices for the detection of clandestine graves josé luis silván cárdenas anna josselinne alegre mondragón edgar daniel ramírez aceves david rogelio campos cornejo maximiano bautista andalón">
        <summary class="bk-ch-head">
          <span class="bk-num">10</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Design and application of spectral indices for the detection of clandestine graves" data-es="Diseño y aplicación de índices espectrales para la detección de fosas clandestinas">Design and application of spectral indices for the detection of clandestine graves</span><span class="bk-ch-who" data-en="José Luis Silván Cárdenas, Anna Josselinne Alegre Mondragón, Edgar Daniel Ramírez Aceves, David Rogelio Campos Cornejo and Maximiano Bautista Andalón" data-es="José Luis Silván Cárdenas, Anna Josselinne Alegre Mondragón, Edgar Daniel Ramírez Aceves, David Rogelio Campos Cornejo y Maximiano Bautista Andalón">José Luis Silván Cárdenas, Anna Josselinne Alegre Mondragón, Edgar Daniel Ramírez Aceves, David Rogelio Campos Cornejo and Maximiano Bautista Andalón</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 355–392</span><span class="bk-ch-size" data-en="38 pp · 2.3 MB" data-es="38 págs. · 2.3 MB">38 pp · 2.3 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Diseño y aplicación de índices espectrales para la detección de fosas clandestinas" data-es="Design and application of spectral indices for the detection of clandestine graves">Diseño y aplicación de índices espectrales para la detección de fosas clandestinas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-10-indices-espectrales-deteccion-fosas.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-10-indices-espectrales-deteccion-fosas.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Silván Cárdenas, J. L., Alegre Mondragón, A. J., Ramírez Aceves, E. D., Campos Cornejo, D. R. and Bautista Andalón, M. (2024) 'Diseño y aplicación de índices espectrales para la detección de fosas clandestinas' [Design and application of spectral indices for the detection of clandestine graves], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 355–392.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="11" data-find="el calor de las personas que nos faltan: búsqueda de fosas clandestinas con apoyo de drones equipados con cámara termográfica the warmth of the people we are missing: searching for clandestine graves with drones equipped with a thermographic camera sergio alberto quezada godinez andrea ponce chávez josé luis silván cárdenas tunuari roberto chávez gonzález">
        <summary class="bk-ch-head">
          <span class="bk-num">11</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="The warmth of the people we are missing: searching for clandestine graves with drones equipped with a thermographic camera" data-es="El calor de las personas que nos faltan: búsqueda de fosas clandestinas con apoyo de drones equipados con cámara termográfica">The warmth of the people we are missing: searching for clandestine graves with drones equipped with a thermographic camera</span><span class="bk-ch-who" data-en="Sergio Alberto Quezada Godinez, Andrea Ponce Chávez, José Luis Silván Cárdenas and Tunuari Roberto Chávez González" data-es="Sergio Alberto Quezada Godinez, Andrea Ponce Chávez, José Luis Silván Cárdenas y Tunuari Roberto Chávez González">Sergio Alberto Quezada Godinez, Andrea Ponce Chávez, José Luis Silván Cárdenas and Tunuari Roberto Chávez González</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 393–430</span><span class="bk-ch-size" data-en="38 pp · 3.9 MB" data-es="38 págs. · 3.9 MB">38 pp · 3.9 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="El calor de las personas que nos faltan: búsqueda de fosas clandestinas con apoyo de drones equipados con cámara termográfica" data-es="The warmth of the people we are missing: searching for clandestine graves with drones equipped with a thermographic camera">El calor de las personas que nos faltan: búsqueda de fosas clandestinas con apoyo de drones equipados con cámara termográfica</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-11-calor-personas-que-nos-faltan-termografia.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-11-calor-personas-que-nos-faltan-termografia.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Quezada Godinez, S. A., Ponce Chávez, A., Silván Cárdenas, J. L. and Chávez González, T. R. (2024) 'El calor de las personas que nos faltan: búsqueda de fosas clandestinas con apoyo de drones equipados con cámara termográfica' [The warmth of the people we are missing: searching for clandestine graves with drones equipped with a thermographic camera], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 393–430.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p6"><span class="bk-part-name" data-en="Chemistry and biology" data-es="Química y biología">Chemistry and biology</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="12" data-find="desenterrando la verdad: análisis de cambios en la firma química y características del suelo en sitios de inhumación clandestina unearthing the truth: analysis of changes in the chemical signature and soil characteristics at clandestine burial sites enrique martin ortega higareda sonia citlalli saucedo aguilar tunuari roberto chávez gonzález luis manuel martínez rivera">
        <summary class="bk-ch-head">
          <span class="bk-num">12</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Unearthing the truth: analysis of changes in the chemical signature and soil characteristics at clandestine burial sites" data-es="Desenterrando la verdad: análisis de cambios en la firma química y características del suelo en sitios de inhumación clandestina">Unearthing the truth: analysis of changes in the chemical signature and soil characteristics at clandestine burial sites</span><span class="bk-ch-who" data-en="Enrique Martin Ortega Higareda, Sonia Citlalli Saucedo Aguilar, Tunuari Roberto Chávez González and Luis Manuel Martínez Rivera" data-es="Enrique Martin Ortega Higareda, Sonia Citlalli Saucedo Aguilar, Tunuari Roberto Chávez González y Luis Manuel Martínez Rivera">Enrique Martin Ortega Higareda, Sonia Citlalli Saucedo Aguilar, Tunuari Roberto Chávez González and Luis Manuel Martínez Rivera</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 431–490</span><span class="bk-ch-size" data-en="60 pp · 6.4 MB" data-es="60 págs. · 6.4 MB">60 pp · 6.4 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Desenterrando la verdad: análisis de cambios en la firma química y características del suelo en sitios de inhumación clandestina" data-es="Unearthing the truth: analysis of changes in the chemical signature and soil characteristics at clandestine burial sites">Desenterrando la verdad: análisis de cambios en la firma química y características del suelo en sitios de inhumación clandestina</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-12-desenterrando-la-verdad-firma-quimica-suelo.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-12-desenterrando-la-verdad-firma-quimica-suelo.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Ortega Higareda, E. M., Saucedo Aguilar, S. C., Chávez González, T. R. and Martínez Rivera, L. M. (2024) 'Desenterrando la verdad: análisis de cambios en la firma química y características del suelo en sitios de inhumación clandestina' [Unearthing the truth: analysis of changes in the chemical signature and soil characteristics at clandestine burial sites], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 431–490.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="13" data-find="la vida después de la vida: botánica forense aplicada al estudio y detección de fosas clandestinas life after life: forensic botany applied to the study and detection of clandestine graves ramón cuevas guzmán maría l. baca cruz josé guadalupe robles estrada fátima yazmin salcedo garcía melina gil meza">
        <summary class="bk-ch-head">
          <span class="bk-num">13</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Life after life: forensic botany applied to the study and detection of clandestine graves" data-es="La vida después de la vida: botánica forense aplicada al estudio y detección de fosas clandestinas">Life after life: forensic botany applied to the study and detection of clandestine graves</span><span class="bk-ch-who" data-en="Ramón Cuevas Guzmán, María L. Baca Cruz, José Guadalupe Robles Estrada, Fátima Yazmin Salcedo García and Melina Gil Meza" data-es="Ramón Cuevas Guzmán, María L. Baca Cruz, José Guadalupe Robles Estrada, Fátima Yazmin Salcedo García y Melina Gil Meza">Ramón Cuevas Guzmán, María L. Baca Cruz, José Guadalupe Robles Estrada, Fátima Yazmin Salcedo García and Melina Gil Meza</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 491–536</span><span class="bk-ch-size" data-en="46 pp · 2.7 MB" data-es="46 págs. · 2.7 MB">46 pp · 2.7 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="La vida después de la vida: botánica forense aplicada al estudio y detección de fosas clandestinas" data-es="Life after life: forensic botany applied to the study and detection of clandestine graves">La vida después de la vida: botánica forense aplicada al estudio y detección de fosas clandestinas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-13-vida-despues-de-la-vida-botanica-forense.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-13-vida-despues-de-la-vida-botanica-forense.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Cuevas Guzmán, R., Baca Cruz, M. L., Robles Estrada, J. G., Salcedo García, F. Y. and Gil Meza, M. (2024) 'La vida después de la vida: botánica forense aplicada al estudio y detección de fosas clandestinas' [Life after life: forensic botany applied to the study and detection of clandestine graves], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 491–536.</p>
          </div>
        </div>
      </details>
      <details class="bk-ch" data-n="14" data-find="¿quiénes son los primeros en detectar una inhumación clandestina? entomología forense: los insectos y su relación con las fosas clandestinas who are the first to detect a clandestine burial? forensic entomology: insects and their relationship with clandestine graves jessica berenice lópez caro lizbeth g. romero aguilar josé l. navarrete heredia maría l. baca cruz">
        <summary class="bk-ch-head">
          <span class="bk-num">14</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Who are the first to detect a clandestine burial? Forensic entomology: insects and their relationship with clandestine graves" data-es="¿Quiénes son los primeros en detectar una inhumación clandestina? Entomología forense: los insectos y su relación con las fosas clandestinas">Who are the first to detect a clandestine burial? Forensic entomology: insects and their relationship with clandestine graves</span><span class="bk-ch-who" data-en="Jessica Berenice López Caro, Lizbeth G. Romero Aguilar, José L. Navarrete Heredia and María L. Baca Cruz" data-es="Jessica Berenice López Caro, Lizbeth G. Romero Aguilar, José L. Navarrete Heredia y María L. Baca Cruz">Jessica Berenice López Caro, Lizbeth G. Romero Aguilar, José L. Navarrete Heredia and María L. Baca Cruz</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 537–576</span><span class="bk-ch-size" data-en="40 pp · 1.5 MB" data-es="40 págs. · 1.5 MB">40 pp · 1.5 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="¿Quiénes son los primeros en detectar una inhumación clandestina? Entomología forense: los insectos y su relación con las fosas clandestinas" data-es="Who are the first to detect a clandestine burial? Forensic entomology: insects and their relationship with clandestine graves">¿Quiénes son los primeros en detectar una inhumación clandestina? Entomología forense: los insectos y su relación con las fosas clandestinas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-14-entomologia-forense-insectos-fosas.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-14-entomologia-forense-insectos-fosas.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">López Caro, J. B., Romero Aguilar, L. G., Navarrete Heredia, J. L. and Baca Cruz, M. L. (2024) '¿Quiénes son los primeros en detectar una inhumación clandestina? Entomología forense: los insectos y su relación con las fosas clandestinas' [Who are the first to detect a clandestine burial? Forensic entomology: insects and their relationship with clandestine graves], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 537–576.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p7"><span class="bk-part-name" data-en="Taphonomy" data-es="Tafonomía">Taphonomy</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="15" data-find="análisis tafonómico comparativo: la deposición y su relación con la estimación del intervalo post mortem comparative taphonomic analysis: deposition and its relationship with the estimation of the post-mortem interval dalia nonatzin miranda díaz">
        <summary class="bk-ch-head">
          <span class="bk-num">15</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Comparative taphonomic analysis: deposition and its relationship with the estimation of the post-mortem interval" data-es="Análisis tafonómico comparativo: la deposición y su relación con la estimación del intervalo post mortem">Comparative taphonomic analysis: deposition and its relationship with the estimation of the post-mortem interval</span><span class="bk-ch-who" data-en="Dalia Nonatzin Miranda Díaz" data-es="Dalia Nonatzin Miranda Díaz">Dalia Nonatzin Miranda Díaz</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 577–600</span><span class="bk-ch-size" data-en="24 pp · 3.5 MB" data-es="24 págs. · 3.5 MB">24 pp · 3.5 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Análisis tafonómico comparativo: la deposición y su relación con la estimación del intervalo post mortem" data-es="Comparative taphonomic analysis: deposition and its relationship with the estimation of the post-mortem interval">Análisis tafonómico comparativo: la deposición y su relación con la estimación del intervalo post mortem</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-15-analisis-tafonomico-comparativo.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-15-analisis-tafonomico-comparativo.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Miranda Díaz, D. N. (2024) 'Análisis tafonómico comparativo: la deposición y su relación con la estimación del intervalo post mortem' [Comparative taphonomic analysis: deposition and its relationship with the estimation of the post-mortem interval], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 577–600.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p8"><span class="bk-part-name" data-en="Forensic education" data-es="Educación forense">Forensic education</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="16" data-find="simulación de fosas clandestinas como estrategia didáctica en la formación del científico forense: participación del estudiantado de la licenciatura en ciencias forenses en el proyecto de vinculación entre la cobupej y la universidad de guadalajara simulation of clandestine graves as a teaching strategy in the training of forensic scientists: participation of forensic science undergraduate students in the collaboration project between cobupej and the university of guadalajara denisse ayala hernández alma cristina padilla de anda teresita de jesús bustamante flores">
        <summary class="bk-ch-head">
          <span class="bk-num">16</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Simulation of clandestine graves as a teaching strategy in the training of forensic scientists: participation of Forensic Science undergraduate students in the collaboration project between COBUPEJ and the University of Guadalajara" data-es="Simulación de fosas clandestinas como estrategia didáctica en la formación del científico forense: participación del estudiantado de la Licenciatura en Ciencias Forenses en el proyecto de vinculación entre la COBUPEJ y la Universidad de Guadalajara">Simulation of clandestine graves as a teaching strategy in the training of forensic scientists: participation of Forensic Science undergraduate students in the collaboration project between COBUPEJ and the University of Guadalajara</span><span class="bk-ch-who" data-en="Denisse Ayala Hernández, Alma Cristina Padilla de Anda and Teresita de Jesús Bustamante Flores" data-es="Denisse Ayala Hernández, Alma Cristina Padilla de Anda y Teresita de Jesús Bustamante Flores">Denisse Ayala Hernández, Alma Cristina Padilla de Anda and Teresita de Jesús Bustamante Flores</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 601–632</span><span class="bk-ch-size" data-en="32 pp · 1.9 MB" data-es="32 págs. · 1.9 MB">32 pp · 1.9 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Simulación de fosas clandestinas como estrategia didáctica en la formación del científico forense: participación del estudiantado de la Licenciatura en Ciencias Forenses en el proyecto de vinculación entre la COBUPEJ y la Universidad de Guadalajara" data-es="Simulation of clandestine graves as a teaching strategy in the training of forensic scientists: participation of Forensic Science undergraduate students in the collaboration project between COBUPEJ and the University of Guadalajara">Simulación de fosas clandestinas como estrategia didáctica en la formación del científico forense: participación del estudiantado de la Licenciatura en Ciencias Forenses en el proyecto de vinculación entre la COBUPEJ y la Universidad de Guadalajara</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-16-simulacion-fosas-educacion-forense.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-16-simulacion-fosas-educacion-forense.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Ayala Hernández, D., Padilla de Anda, A. C. and Bustamante Flores, T. de J. (2024) 'Simulación de fosas clandestinas como estrategia didáctica en la formación del científico forense: participación del estudiantado de la Licenciatura en Ciencias Forenses en el proyecto de vinculación entre la COBUPEJ y la Universidad de Guadalajara' [Simulation of clandestine graves as a teaching strategy in the training of forensic scientists: participation of Forensic Science undergraduate students in the collaboration project between COBUPEJ and the University of Guadalajara], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 601–632.</p>
          </div>
        </div>
      </details>
      <div class="bk-part" data-part="p9"><span class="bk-part-name" data-en="Synthesis" data-es="Síntesis">Synthesis</span><span class="bk-part-rule"></span></div>
      <details class="bk-ch" data-n="17" data-find="interpretar la naturaleza para encontrar a quienes nos faltan: integración de un estudio multidisciplinario y perspectivas interpreting nature to find those who are missing: integration of a multidisciplinary study and perspectives tunuari roberto chávez gonzález enrique josé jardel peláez sergio alberto quezada godinez">
        <summary class="bk-ch-head">
          <span class="bk-num">17</span>
          <span class="bk-ch-main"><span class="bk-ch-title" data-en="Interpreting nature to find those who are missing: integration of a multidisciplinary study and perspectives" data-es="Interpretar la naturaleza para encontrar a quienes nos faltan: integración de un estudio multidisciplinario y perspectivas">Interpreting nature to find those who are missing: integration of a multidisciplinary study and perspectives</span><span class="bk-ch-who" data-en="Tunuari Roberto Chávez González, Enrique José Jardel Peláez and Sergio Alberto Quezada Godinez" data-es="Tunuari Roberto Chávez González, Enrique José Jardel Peláez y Sergio Alberto Quezada Godinez">Tunuari Roberto Chávez González, Enrique José Jardel Peláez and Sergio Alberto Quezada Godinez</span></span>
          <span class="bk-ch-side"><span class="bk-ch-meta"><span class="bk-ch-pages">pp. 633–666</span><span class="bk-ch-size" data-en="36 pp · 1.3 MB" data-es="36 págs. · 1.3 MB">36 pp · 1.3 MB</span></span><svg class="bk-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></span>
        </summary>
        <div class="bk-ch-body">
          <p class="bk-alt" data-en="Interpretar la naturaleza para encontrar a quienes nos faltan: integración de un estudio multidisciplinario y perspectivas" data-es="Interpreting nature to find those who are missing: integration of a multidisciplinary study and perspectives">Interpretar la naturaleza para encontrar a quienes nos faltan: integración de un estudio multidisciplinario y perspectivas</p>
          <div class="bk-acts">
            <a class="bk-btn bk-btn-dl" href="/files/libro-vol1/cap-17-interpretar-la-naturaleza-sintesis.pdf" download><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span class="" data-en="Download PDF" data-es="Descargar PDF">Download PDF</span></a>
            <a class="bk-btn bk-btn-ghost" href="/files/libro-vol1/cap-17-interpretar-la-naturaleza-sintesis.pdf" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg><span class="" data-en="Open in browser" data-es="Abrir en el navegador">Open in browser</span></a>
          </div>
          <div class="bk-cite">
            <div class="bk-cite-label"><span class="" data-en="Cite this chapter (Harvard)" data-es="Cómo citar este capítulo (Harvard)">Cite this chapter (Harvard)</span><button type="button" class="bk-copy" data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text">Chávez González, T. R., Jardel Peláez, E. J. and Quezada Godinez, S. A. (2024) 'Interpretar la naturaleza para encontrar a quienes nos faltan: integración de un estudio multidisciplinario y perspectivas' [Interpreting nature to find those who are missing: integration of a multidisciplinary study and perspectives], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. 633–666.</p>
          </div>
        </div>
      </details>
        <div class="bk-empty" id="bk-empty" hidden data-en="No chapters match that search." data-es="Ningún capítulo coincide con esa búsqueda.">No chapters match that search.</div>
      </div>

      <div class="bk-how">
        <h3 class="bk-how-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21c3-4 6-2 9-6"/><path d="M9 9h6"/><path d="M9 13h4"/><path d="M5 3h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8l-4 3V5a2 2 0 0 1 1-2z"/></svg>
          <span class="" data-en="How to cite" data-es="Cómo citar">How to cite</span>
        </h3>
        <p class="bk-how-note" data-en="References follow Harvard style. Each chapter entry gives the original Spanish title followed by an English translation in square brackets, matching the style used in FOUND's academic references. Open any chapter above to copy its full reference." data-es="Las referencias siguen el formato Harvard. Cada entrada ofrece el título original en español seguido de su traducción al inglés entre corchetes, siguiendo el estilo empleado en las referencias académicas de FOUND. Abre cualquier capítulo para copiar su referencia completa.">References follow Harvard style. Each chapter entry gives the original Spanish title followed by an English translation in square brackets, matching the style used in FOUND's academic references. Open any chapter above to copy its full reference.</p>
        <div class="bk-how-grid">
          <div class="bk-how-item">
            <div class="bk-cite-label"><span class="" data-en="The whole volume" data-es="El volumen completo">The whole volume</span><button type="button" class="bk-copy" data-copy-whole data-en="Copy" data-es="Copiar">Copy</button></div>
            <p class="bk-cite-text" id="bk-whole-cite">Ávila Barrientos, V. H., Chávez González, T. R. and Silván Cárdenas, J. L. (eds.) (2024) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco.</p>
          </div>
          <div class="bk-how-item">
            <div class="bk-cite-label"><span class="" data-en="A single chapter" data-es="Un capítulo">A single chapter</span></div>
            <p class="bk-how-tpl" data-html-en="&lt;em&gt;Author(s)&lt;/em&gt; (2024) &amp;lsquo;&lt;em&gt;Spanish title&lt;/em&gt;&amp;rsquo; [&lt;em&gt;English title&lt;/em&gt;], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. &lt;em&gt;page range&lt;/em&gt;." data-html-es="&lt;em&gt;Autoría&lt;/em&gt; (2024) &amp;lsquo;&lt;em&gt;Título en español&lt;/em&gt;&amp;rsquo; [&lt;em&gt;Título en inglés&lt;/em&gt;], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. &lt;em&gt;páginas&lt;/em&gt;."><em>Author(s)</em> (2024) &lsquo;<em>Spanish title</em>&rsquo; [<em>English title</em>], in V. H. Ávila Barrientos, T. R. Chávez González and J. L. Silván Cárdenas (eds.) Interpretar la naturaleza para encontrar a quienes nos faltan: ciencias biológicas, físicas y de la tierra aplicadas a la detección de inhumaciones clandestinas. Ciudad de México: CentroGeo / Gobierno del Estado de Jalisco, pp. <em>page range</em>.</p>
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
          'title-book': 'The Book',
          'book-badge': 'Free download',
          'book-desc': 'This volume brings together biological, physical, and earth sciences to design and test methods for detecting clandestine graves. Volume 2 and Volume 3 will be presented in December 2026.',
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
          'title-book': 'El libro',
          'book-badge': 'Arbitraje científico de capítulos; Descarga gratuita',
          'book-desc': 'Este volumen reúne ciencias biológicas, físicas y de la Tierra para diseñar y probar métodos de detección de fosas clandestinas. El Volumen 2 y el Volumen 3 serán presentados en diciembre de 2026.',
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
        'title-book','book-badge','book-desc',
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
    var sec = document.getElementById('volume-1');
    if(!sec) return;
    var list = document.getElementById('bk-list');
    var search = document.getElementById('bk-search');
    var toggle = document.getElementById('bk-toggle-all');
    var count = document.getElementById('bk-count');
    var empty = document.getElementById('bk-empty');
    var lang = 'en';
    var COUNT = {en:'%s of 17 shown', es:'%s de 17 visibles'};
    var DONE  = {en:'Copied', es:'Copiado'};

    function chapters(){ return [].slice.call(list.querySelectorAll('.bk-ch')); }
    function visible(){ return chapters().filter(function(e){ return e.style.display !== 'none'; }); }

    function setLang(l){
      lang = (l === 'es') ? 'es' : 'en';
      var nodes = sec.querySelectorAll('[data-en],[data-html-en],[data-ph-en]');
      [].slice.call(nodes).forEach(function(el){
        var html = el.getAttribute('data-html-' + lang);
        if(html !== null){ el.innerHTML = html; return; }
        var ph = el.getAttribute('data-ph-' + lang);
        if(ph !== null){ el.placeholder = ph; el.setAttribute('aria-label', ph); return; }
        var txt = el.getAttribute('data-' + lang);
        if(txt !== null) el.textContent = txt;
      });
      syncToggle();
      updateCount();
    }

    function updateCount(){
      count.textContent = COUNT[lang].replace('%s', visible().length);
    }

    function filter(){
      var q = (search.value || '').trim().toLowerCase();
      var shown = 0;
      chapters().forEach(function(el){
        var hit = !q || el.getAttribute('data-find').indexOf(q) !== -1;
        el.style.display = hit ? '' : 'none';
        if(hit) shown++;
      });
      [].slice.call(sec.querySelectorAll('.bk-part')).forEach(function(head){
        var any = false, n = head.nextElementSibling;
        while(n && n.classList.contains('bk-ch')){
          if(n.style.display !== 'none') any = true;
          n = n.nextElementSibling;
        }
        head.style.display = any ? '' : 'none';
      });
      empty.hidden = shown > 0;
      updateCount();
      syncToggle();
    }

    function allOpen(){
      var v = visible();
      return v.length > 0 && v.every(function(e){ return e.open; });
    }
    function syncToggle(){
      toggle.textContent = allOpen()
        ? (lang === 'es' ? 'Cerrar todo' : 'Collapse all')
        : (lang === 'es' ? 'Abrir todo'  : 'Expand all');
    }

    function copy(text, btn){
      var restore = btn.getAttribute('data-' + lang) || btn.textContent;
      var ok = function(){
        btn.textContent = DONE[lang];
        btn.classList.add('is-done');
        setTimeout(function(){ btn.textContent = restore; btn.classList.remove('is-done'); }, 1600);
      };
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(text).then(ok, function(){ legacy(text, ok); });
      } else { legacy(text, ok); }
    }
    function legacy(text, ok){
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly','');
      ta.style.cssText = 'position:absolute;left:-9999px;top:0';
      document.body.appendChild(ta); ta.select();
      try{ document.execCommand('copy'); ok(); }catch(e){}
      document.body.removeChild(ta);
    }

    sec.addEventListener('click', function(ev){
      var btn = ev.target.closest ? ev.target.closest('.bk-copy') : null;
      if(!btn) return;
      ev.preventDefault();
      var box = btn.closest('.bk-cite') || btn.closest('.bk-how-item');
      var text = box ? box.querySelector('.bk-cite-text') : null;
      if(text) copy(text.textContent.trim(), btn);
    });
    sec.addEventListener('toggle', function(){ syncToggle(); }, true);
    search.addEventListener('input', filter);
    toggle.addEventListener('click', function(){
      var target = !allOpen();
      visible().forEach(function(e){ e.open = target; });
      syncToggle();
    });
    document.querySelectorAll('.lang-btn').forEach(function(b){
      b.addEventListener('click', function(){ setLang(this.dataset.lang); });
    });

    sec.classList.add('bk-js');
    try{
      var saved = localStorage.getItem('found-lang') || localStorage.getItem('found-lang-pubs');
      if(saved === 'es' || saved === 'en') lang = saved;
    }catch(e){}
    setLang(lang);
  })();
  </script>
{% endraw %}
</body>
</html>
