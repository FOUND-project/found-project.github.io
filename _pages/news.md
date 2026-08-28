---
layout: archive
title: "News"
permalink: /news/
author_profile: false
---
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200">
  <title>FOUND — News & Updates</title>
  <!-- ═══════════════════════════════════════════════════════
       OPEN GRAPH — dynamic per-card when shared via #card-id
       ═══════════════════════════════════════════════════════ -->
  <meta property="og:type"         content="article">
  <meta property="og:site_name"    content="FOUND Project">
  <meta property="og:title"        content="FOUND — News &amp; Updates" id="og-title">
  <meta property="og:description"  content="Latest developments on our work across Mexico, Colombia, and beyond." id="og-description">
  <meta property="og:image"        content="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true" id="og-image">
  <meta property="og:url"          content="https://found-project.org/news/" id="og-url">
  <meta name="twitter:card"        content="summary_large_image">
  <meta name="twitter:title"       content="FOUND — News &amp; Updates" id="tw-title">
  <meta name="twitter:description" content="Latest developments on our work across Mexico, Colombia, and beyond." id="tw-description">
  <meta name="twitter:image"       content="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true" id="tw-image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    /* ═══════════════════════════════════════════════════════
       RESET & DESIGN TOKENS
       ═══════════════════════════════════════════════════════ */
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    :root {
      --green-900: #0f2d22;
      --green-800: #1e4034;
      --green-700: #2d5f4d;
      --green-500: #4a8c73;
      --green-200: #c6e2d8;
      --green-50:  #f4faf7;
      --gold:      #d4af37;
      --gold-pale: rgba(212,175,55,.12);
      --text-dark:   #111827;
      --text-medium: #374151;
      --text-light:  #6b7280;
      --white:     #ffffff;
      --shadow-xs: 0 2px 8px  rgba(15,23,42,.06);
      --shadow-sm: 0 4px 16px rgba(15,23,42,.08);
      --shadow-md: 0 10px 28px rgba(15,23,42,.12);
      --shadow-lg: 0 24px 56px rgba(15,23,42,.18);
      --shadow-xl: 0 40px 80px rgba(15,23,42,.22);
      --radius-xl: 26px;
      --radius-lg: 20px;
      --radius-md: 14px;
      --radius-sm: 10px;
      --radius-pill: 999px;
      --ease: cubic-bezier(.4,0,.2,1);
      --ease-spring: cubic-bezier(.34,1.56,.64,1);
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
    }
    html { scroll-behavior: smooth; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif;
      background: radial-gradient(ellipse 1400px 700px at 5% -5%, rgba(212,175,55,.10) 0%, transparent 55%), radial-gradient(ellipse 1000px 600px at 90% 10%, rgba(198,226,216,.60) 0%, transparent 55%), linear-gradient(160deg, #f7fbfa 0%, #eef4f1 45%, #f9fbff 100%);
      min-height: 100vh;
      color: var(--text-dark);
      -webkit-font-smoothing: antialiased;
      padding: clamp(1.5rem,3vw,2.5rem) clamp(1rem,4vw,3rem);
    }
    .page, #main, .initial-content, .page__inner-wrap, .page__content, .archive { max-width: none !important; width: 100% !important; }
    *:focus-visible { outline: 3px solid rgba(74,140,115,.55); outline-offset: 3px; border-radius: var(--radius-sm); }
    .news-shell { max-width: var(--shell-max); margin: 0 auto; padding: 0 var(--shell-pad); position: relative; }
    .lang-toggle { position: absolute; top: .25rem; right: 0; display: inline-flex; gap: .45rem; z-index: 10; }
    .lang-btn { border: 1px solid rgba(15,23,42,.09); background: rgba(255,255,255,.88); color: var(--green-800); padding: .28rem .75rem; border-radius: var(--radius-pill); font-size: .72rem; font-weight: 700; letter-spacing: .09em; text-transform: uppercase; cursor: pointer; backdrop-filter: blur(10px); box-shadow: 0 3px 12px rgba(15,23,42,.07); transition: transform .2s var(--ease), background .2s var(--ease), box-shadow .2s var(--ease), color .2s var(--ease), border-color .2s var(--ease); }
    .lang-btn:hover { background:#fff; transform:translateY(-1px); box-shadow:0 7px 20px rgba(15,23,42,.14); }
    .lang-btn.active { background:var(--green-800); color:#fff; border-color:var(--green-800); }
    .news-header { position: relative; margin: 1.75rem 0 3rem; border-radius: var(--radius-xl); overflow: hidden; background: var(--white); box-shadow: var(--shadow-md); border: 1px solid rgba(15,23,42,.055); display: flex; align-items: stretch; }
    .news-header::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 5px; background: linear-gradient(180deg, var(--gold) 0%, rgba(212,175,55,.3) 100%); border-radius: var(--radius-xl) 0 0 var(--radius-xl); }
    .news-header::after { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 600px 300px at -5% 0%, rgba(212,175,55,.13) 0%, transparent 60%), radial-gradient(ellipse 500px 300px at 110% 100%, rgba(198,226,216,.5) 0%, transparent 60%); pointer-events: none; }
    .news-header-logo { flex: 0 0 auto; display: flex; align-items: center; padding: 2.2rem 2rem 2.2rem 2.8rem; position: relative; z-index: 1; }
    .news-header-logo img { width: 88px; height: 88px; border-radius: 20px; object-fit: cover; box-shadow: 0 12px 32px rgba(15,23,42,.22); border: 3px solid rgba(255,255,255,.95); background: #fff; }
    .news-header-divider { width: 1px; background: linear-gradient(180deg, transparent, rgba(15,23,42,.08), transparent); margin: 2rem 0; flex-shrink: 0; }
    .news-header-body { flex: 1; padding: 2.2rem 2.8rem 2.2rem 2.4rem; position: relative; z-index: 1; display: flex; flex-direction: column; justify-content: center; }
    .news-eyebrow { display: inline-flex; align-items: center; gap: .5rem; margin-bottom: .65rem; }
    .news-eyebrow-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--gold); box-shadow: 0 0 0 3px rgba(212,175,55,.2); }
    .news-eyebrow-text { font-size: .7rem; font-weight: 800; letter-spacing: .2em; text-transform: uppercase; color: var(--green-700); }
    #news-title { font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 900; color: var(--green-900); letter-spacing: -.035em; line-height: 1.15; margin-bottom: .5rem; }
    #news-subtitle { font-size: clamp(.95rem, 1.3vw, 1.1rem); color: var(--text-medium); line-height: 1.75; max-width: 680px; }
    .news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: clamp(1.2rem, 2vw, 1.8rem); margin-bottom: 2rem; --stagger: 60ms; }
    .news-card { background: var(--white); border-radius: var(--radius-lg); border: 1px solid rgba(15,23,42,.055); box-shadow: var(--shadow-sm); overflow: hidden; cursor: pointer; display: flex; flex-direction: column; position: relative; transition: transform .28s var(--ease), box-shadow .28s var(--ease), border-color .28s var(--ease); animation: cardIn .55s var(--ease) both; }
    .news-card:nth-child(1) { animation-delay: calc(1 * var(--stagger)); }
    .news-card:nth-child(2) { animation-delay: calc(2 * var(--stagger)); }
    .news-card:nth-child(3) { animation-delay: calc(3 * var(--stagger)); }
    .news-card:nth-child(4) { animation-delay: calc(4 * var(--stagger)); }
    .news-card:nth-child(5) { animation-delay: calc(5 * var(--stagger)); }
    .news-card:nth-child(6) { animation-delay: calc(6 * var(--stagger)); }
    @keyframes cardIn { from { opacity:0; transform:translateY(18px); } to { opacity:1; transform:translateY(0); } }
    .news-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); border-color: rgba(45,95,77,.22); }
    .news-card.featured { border-top: 3px solid var(--gold); }
    .card-banner { width: 100%; height: 160px; position: relative; overflow: hidden; flex-shrink: 0; }
    .card-banner img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform .55s var(--ease); }
    .news-card:hover .card-banner img { transform: scale(1.05); }
    .card-banner.no-photo { background: var(--banner-bg, linear-gradient(135deg, #1e4034 0%, #2d5f4d 100%)); display: flex; align-items: center; justify-content: center; }
    .card-banner-icon { width: 52px; height: 52px; opacity: .22; color: #fff; }
    .card-banner-icon svg { width: 100%; height: 100%; fill: currentColor; }
    .card-banner-watermark { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; gap: .5rem; }
    .card-banner-logo { width: 48px; height: 48px; border-radius: 12px; object-fit: cover; opacity: .32; border: 2px solid rgba(255,255,255,.25); }
    .card-banner-label { font-size: .62rem; font-weight: 800; letter-spacing: .22em; text-transform: uppercase; color: rgba(255,255,255,.45); }
    .card-banner.logo-contain { background: var(--banner-bg, linear-gradient(135deg, #2e1065 0%, #4c1d95 60%, #6d28d9 100%)); }
    .card-banner.logo-contain img { object-fit: contain; padding: 1.4rem; }
    .news-card:hover .card-banner.logo-contain img { transform: scale(1.03); }
    .card-banner::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 40%, rgba(10,24,18,.42) 100%); pointer-events: none; }
    .card-banner.logo-contain::after { display: none; }
    .card-body { padding: 1.3rem 1.4rem 1.5rem; display: flex; flex-direction: column; flex: 1; gap: .5rem; }
    .card-meta { display: flex; align-items: center; justify-content: space-between; gap: .35rem .5rem; flex-wrap: wrap; }
    .card-badge { display: inline-flex; align-items: center; gap: .3rem; padding: .16rem .6rem; border-radius: var(--radius-pill); font-size: .66rem; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; background: var(--badge-bg, rgba(30,64,52,.07)); color: var(--badge-color, var(--green-800)); border: 1px solid var(--badge-border, rgba(30,64,52,.16)); }
    .card-badge::before { content: ''; width: 5px; height: 5px; border-radius: 50%; background: currentColor; opacity: .7; }
    .card-date { font-size: .68rem; font-weight: 600; color: var(--text-light); letter-spacing: .03em; white-space: nowrap; }
    .card-title { font-size: 1.06rem; font-weight: 800; color: var(--green-900); line-height: 1.42; letter-spacing: -.015em; flex: 1; }
    .card-cta { display: flex; align-items: center; justify-content: space-between; margin-top: .4rem; padding-top: .9rem; border-top: 1px solid rgba(15,23,42,.055); }
    .card-read-more { font-size: .76rem; font-weight: 700; color: var(--green-700); letter-spacing: .04em; }
    .card-arrow { width: 28px; height: 28px; border-radius: 50%; background: var(--green-50); border: 1px solid rgba(45,95,77,.14); display: flex; align-items: center; justify-content: center; transition: background .2s var(--ease), transform .2s var(--ease-spring), box-shadow .2s var(--ease); flex-shrink: 0; }
    .card-arrow svg { width: 13px; height: 13px; stroke: var(--green-700); fill: none; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; transition: stroke .2s; }
    .news-card:hover .card-arrow { background: var(--green-800); transform: translateX(3px); box-shadow: 0 6px 16px rgba(30,64,52,.3); }
    .news-card:hover .card-arrow svg { stroke: #fff; }
    .modal-overlay { position: fixed; inset: 0; z-index: 9999; background: rgba(6,18,14,.62); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); display: flex; align-items: center; justify-content: center; padding: 1.5rem; opacity: 0; visibility: hidden; transition: opacity .32s var(--ease), visibility .32s var(--ease); }
    .modal-overlay.active { opacity: 1; visibility: visible; }
    .modal-panel { background: var(--white); border-radius: var(--radius-xl); max-width: 800px; width: 100%; max-height: 90vh; overflow-y: auto; overflow-x: hidden; box-shadow: var(--shadow-xl), 0 0 0 1px rgba(15,23,42,.06); transform: translateY(22px) scale(.965); transition: transform .35s var(--ease-spring); scrollbar-width: thin; scrollbar-color: var(--green-200) transparent; position: relative; }
    .modal-overlay.active .modal-panel { transform: translateY(0) scale(1); }
    .modal-panel::-webkit-scrollbar { width: 5px; }
    .modal-panel::-webkit-scrollbar-track { background: transparent; }
    .modal-panel::-webkit-scrollbar-thumb { background: var(--green-200); border-radius: 10px; }
    .modal-hero { position: relative; min-height: 200px; overflow: hidden; }
    .modal-hero-img { width: 100%; display: block; max-height: 340px; object-fit: cover; }
    .modal-hero.logo-contain { background: var(--hero-bg, linear-gradient(135deg, #2e1065 0%, #4c1d95 60%, #6d28d9 100%)); display: flex; align-items: center; justify-content: center; min-height: 240px; }
    .modal-hero.logo-contain .modal-hero-img { max-height: 220px; width: auto; max-width: 80%; object-fit: contain; padding: 1.5rem; }
    .modal-hero.logo-contain::after { display: none; }
    .modal-hero.full-image { background: #0b1c16; text-align: center; }
    .modal-hero.full-image .modal-hero-img { max-height: 80vh; width: auto; max-width: 100%; object-fit: contain; margin: 0 auto; }
    .modal-hero.full-image::after { display: none; }
    .modal-hero-gradient { min-height: 160px; background: var(--hero-bg, linear-gradient(135deg, #1e4034 0%, #2d5f4d 60%, #4a8c73 100%)); display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    .modal-hero-gradient::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 80% 60% at 15% -10%, rgba(212,175,55,.22) 0%, transparent 60%), radial-gradient(ellipse 60% 80% at 90% 110%, rgba(255,255,255,.07) 0%, transparent 60%); }
    .modal-hero-wm { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; gap: .65rem; }
    .modal-hero-logo { width: 56px; height: 56px; border-radius: 14px; object-fit: cover; opacity: .55; border: 2px solid rgba(255,255,255,.3); box-shadow: 0 8px 24px rgba(0,0,0,.25); }
    .modal-hero-news-label { font-size: .65rem; font-weight: 800; letter-spacing: .25em; text-transform: uppercase; color: rgba(255,255,255,.55); }
    .modal-hero::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 30%, rgba(10,24,18,.5) 100%); pointer-events: none; }
    .modal-img-wm { position: absolute; bottom: 1.1rem; right: 1.2rem; z-index: 2; width: 38px; height: 38px; border-radius: 10px; object-fit: cover; opacity: .55; border: 2px solid rgba(255,255,255,.4); box-shadow: 0 4px 14px rgba(0,0,0,.3); }
    .modal-close { position: absolute; top: 1rem; right: 1rem; z-index: 10; width: 38px; height: 38px; border-radius: 50%; border: none; background: rgba(255,255,255,.9); backdrop-filter: blur(10px); box-shadow: 0 4px 16px rgba(15,23,42,.18); display: flex; align-items: center; justify-content: center; cursor: pointer; color: var(--green-800); transition: transform .2s var(--ease-spring), box-shadow .2s var(--ease), background .2s; }
    .modal-close:hover { transform: scale(1.1); box-shadow: 0 8px 24px rgba(15,23,42,.24); background: #fff; }
    .modal-close svg { width: 16px; height: 16px; stroke: currentColor; fill: none; stroke-width: 2.5; stroke-linecap: round; }
    .modal-content { padding: 2rem 2.5rem 1.6rem; }
    .modal-meta { display: flex; align-items: center; gap: .65rem; margin-bottom: .9rem; flex-wrap: wrap; }
    .modal-badge { display: inline-flex; align-items: center; gap: .3rem; padding: .18rem .65rem; border-radius: var(--radius-pill); font-size: .68rem; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; background: var(--badge-bg, rgba(30,64,52,.07)); color: var(--badge-color, var(--green-800)); border: 1px solid var(--badge-border, rgba(30,64,52,.16)); }
    .modal-badge::before { content: ''; width: 5px; height: 5px; border-radius: 50%; background: currentColor; opacity: .7; }
    .modal-date { font-size: .72rem; font-weight: 600; color: var(--text-light); }
    .modal-title { font-size: clamp(1.3rem, 2.4vw, 1.75rem); font-weight: 900; color: var(--green-900); line-height: 1.3; letter-spacing: -.025em; margin-bottom: 1.5rem; }
    .modal-divider { height: 1px; background: linear-gradient(90deg, var(--green-200), transparent); margin-bottom: 1.5rem; }
    .modal-body { color: var(--text-medium); line-height: 1.82; }
    .modal-body p { margin-bottom: 1rem; font-size: .97rem; }
    .modal-body strong { color: var(--green-900); font-weight: 700; }
    .modal-body em { font-style: italic; }
    .modal-body a { color: var(--green-700); text-decoration: none; font-weight: 650; border-bottom: 2px solid rgba(45,95,77,.3); padding-bottom: .05rem; transition: border-color .2s, color .2s; }
    .modal-body a:hover { border-bottom-color: var(--gold); color: var(--green-700); }
    .modal-body ul { margin: .8rem 0 1.1rem 1.4rem; }
    .modal-body ul li { margin-bottom: .5rem; font-size: .97rem; }
    .modal-body img { width: 100%; border-radius: var(--radius-md); margin: 1.2rem 0 1rem; box-shadow: var(--shadow-md); }
    .modal-body .li-embed { display: flex; justify-content: center; margin: 1.4rem 0 1rem; }
    .modal-body .li-embed iframe { border-radius: var(--radius-md); box-shadow: var(--shadow-md); max-width: 100%; background: #fff; }
    .modal-footer { display: flex; align-items: center; gap: .65rem; padding: 1.1rem 2.5rem 1.6rem; border-top: 1px solid rgba(15,23,42,.055); }
    .modal-share-label { font-size: .68rem; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; color: var(--text-light); margin-right: .2rem; }
    .share-btn { width: 36px; height: 36px; border-radius: 50%; border: 1px solid rgba(15,23,42,.1); background: var(--green-50); color: var(--green-800); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: transform .2s var(--ease-spring), box-shadow .2s var(--ease), background .2s, border-color .2s; }
    .share-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(30,64,52,.2); background:#fff; }
    .share-btn svg { width: 15px; height: 15px; fill: currentColor; }
    .share-btn.copied { background: var(--green-800); color:#fff; border-color: var(--green-800); }
    .copy-tooltip { font-size: .7rem; font-weight: 700; color: var(--green-700); opacity: 0; transition: opacity .25s; margin-left: .1rem; }
    .copy-tooltip.show { opacity: 1; }
    .badge-award { --badge-bg: rgba(212,175,55,.1); --badge-color:#8a6d00; --badge-border:rgba(212,175,55,.3); }
    .badge-media { --badge-bg: rgba(59,130,246,.08); --badge-color:#1d4ed8; --badge-border:rgba(59,130,246,.22); }
    .badge-field { --badge-bg: rgba(16,185,129,.08); --badge-color:#065f46; --badge-border:rgba(16,185,129,.22); }
    .badge-funding { --badge-bg: rgba(139,92,246,.08); --badge-color:#5b21b6; --badge-border:rgba(139,92,246,.22); }
    .badge-coverage { --badge-bg: rgba(239,68,68,.07); --badge-color:#991b1b; --badge-border:rgba(239,68,68,.2); }
    .banner-award { --banner-bg: linear-gradient(135deg, #3d2a00 0%, #6b4c00 60%, #8a6d00 100%); }
    .banner-media { --banner-bg: linear-gradient(135deg, #0f1f40 0%, #1e3a8a 60%, #2563eb 100%); }
    .banner-field { --banner-bg: linear-gradient(135deg, #052e16 0%, #14532d 60%, #166534 100%); }
    .banner-funding { --banner-bg: linear-gradient(135deg, #2e1065 0%, #4c1d95 60%, #6d28d9 100%); }
    .banner-coverage { --banner-bg: linear-gradient(135deg, #450a0a 0%, #7f1d1d 60%, #b91c1c 100%); }
    @media (max-width: 900px) {
      body { padding: 1.4rem 1rem; }
      .news-shell { margin-left: 0; }
      .lang-toggle { position: static; margin-bottom: .75rem; }
      .news-header { flex-direction: column; }
      .news-header-logo { padding: 1.6rem 1.6rem 0; }
      .news-header-divider { display: none; }
      .news-header-body { padding: 1rem 1.6rem 1.8rem; }
      #news-title { font-size: 1.65rem; }
      .news-grid { grid-template-columns: 1fr; }
      .modal-content { padding: 1.5rem 1.4rem 1.2rem; }
      .modal-footer { padding: .9rem 1.4rem 1.3rem; }
    }
    @media (max-width: 480px) {
      .news-card .card-body { padding: 1.1rem 1.1rem 1.3rem; }
      .modal-panel { border-radius: var(--radius-lg); }
    }
  </style>
</head>
<body>
  <div class="news-shell">
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
    </div>
        <header class="news-header">
      <div class="news-header-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true" alt="FOUND Logo">
      </div>
      <div class="news-header-divider"></div>
      <div class="news-header-body">
        <div class="news-eyebrow">
          <span class="news-eyebrow-dot"></span>
          <span class="news-eyebrow-text" id="news-pill">NEWS · IMPACT · MEDIA</span>
        </div>
        <h1 id="news-title">FOUND — News &amp; Updates</h1>
        <p id="news-subtitle">Latest developments on our work across Mexico, Colombia, and beyond.</p>
      </div>
    </header>
    <section class="news-grid" id="news-grid" aria-label="News articles"></section>
  </div>
  <div class="modal-overlay" id="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="modal-title-el">
    <div class="modal-panel" id="modal-panel">
      <button class="modal-close" id="modal-close" aria-label="Close">
        <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="modal-hero" id="modal-hero"></div>
      <div class="modal-content">
        <div class="modal-meta">
          <span class="modal-badge" id="modal-badge"></span>
          <span class="modal-date" id="modal-date"></span>
        </div>
        <h2 class="modal-title" id="modal-title-el"></h2>
        <div class="modal-divider"></div>
        <div class="modal-body" id="modal-body"></div>
      </div>
      <div class="modal-footer">
        <span class="modal-share-label" id="share-label">Share</span>
        <button class="share-btn" id="btn-copy" title="Copy link">
          <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
        </button>
        <span class="copy-tooltip" id="copy-tooltip">Copied!</span>
      </div>
    </div>
  </div>
  <script>
    (function(){
      'use strict';
      var LOGO = 'https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true';
      var BASE_URL = 'https://found-project.org/news/';
      var newsCards = [
{
  id: 'found-identia-oxford-event',
  date: '2026-06-19',
  image:'https://raw.githubusercontent.com/FOUND-project/found-project.github.io/eacdc8082a25251fa6f305e06b98b0f721e2857b/images/Esp_BSG_June26.jpeg',
  logoBanner: false,
  fullImage: true,
  link: 'https://www.bsg.ox.ac.uk/events/found-and-identia',
  featured: true,
  category: 'partnership',
  en: {
    badge: 'Event',
    title: 'Can AI help us find and identify our disappeared? FOUND and identIA at the University of Oxford, 26 June',
    body: '<p><strong>Can AI help us find and identify our disappeared?</strong></p><p>In Mexico and Colombia, more than <strong>250,000 people</strong> remain missing, leaving families trapped in grief and uncertainty. It is a crisis that touches millions. AI, remote sensing and soil science have the potential to accelerate results and transform how authorities search for and identify the disappeared.</p><p>But technology alone is not the answer. The families who search hold irreplaceable knowledge, and tools must be built with them. <strong>FOUND</strong> and <strong>identIA</strong> are grounded in that principle: co-producing knowledge with searching families, and keeping ethics at the centre of how technologies enter sensitive fields and are embedded in government.</p><p>On <strong>26 June</strong>, FOUND and identIA come together at the <strong>Blavatnik School of Government, University of Oxford</strong>, to share their results to date in Mexico and Colombia.</p><ul><li>🗓 Friday 26 June 2026, 14:00–15:00 (UK)</li><li>📍 In person at the Blavatnik School of Government · also online</li><li>🎟 Free and open to the public</li></ul><p><a href="https://www.bsg.ox.ac.uk/events/found-and-identia" target="_blank" rel="noopener noreferrer">Register here ↗</a></p>'
  },
  es: {
    badge: 'Evento',
    title: '¿Puede la IA ayudarnos a encontrar e identificar a nuestras personas desaparecidas? FOUND e identIA en la Universidad de Oxford, 26 de junio',
    body: '<p><strong>¿Puede la IA ayudarnos a encontrar e identificar a nuestras personas desaparecidas?</strong></p><p>En México y Colombia, más de <strong>250,000 personas</strong> continúan desaparecidas, dejando a las familias atrapadas en el duelo y la incertidumbre. Es una crisis que toca a millones. La IA, la percepción remota y la ciencia del suelo tienen el potencial de acelerar resultados y transformar la forma en que las autoridades buscan e identifican a las personas desaparecidas.</p><p>Pero la tecnología por sí sola no es la respuesta. Las familias que buscan poseen un conocimiento irremplazable, y las herramientas deben construirse con ellas. <strong>FOUND</strong> e <strong>identIA</strong> se sostienen en ese principio: coproducir conocimiento con las familias buscadoras, y mantener la ética en el centro de cómo las tecnologías entran en campos sensibles y se incorporan a los gobiernos.</p><p>El <strong>26 de junio</strong>, FOUND e identIA se reúnen en la <strong>Blavatnik School of Government de la Universidad de Oxford</strong> para compartir sus resultados a la fecha en México y Colombia.</p><ul><li>🗓 Viernes 26 de junio de 2026, 14:00–15:00 (Reino Unido)</li><li>📍 Presencial en la Blavatnik School of Government · también en línea</li><li>🎟 Gratuito y abierto al público</li></ul><p><a href="https://www.bsg.ox.ac.uk/events/found-and-identia" target="_blank" rel="noopener noreferrer">Regístrate aquí ↗</a></p>'
  }
},
{
  id: 'cnb-first-training',
  date: '2026-04-15',
  image: 'https://github.com/FOUND-project/found-project.github.io/blob/eef1d014b946530cf97009db1836ca88a43f25e1/images/1%20CNB%20Training%20by%20CentroGeo.jpeg?raw=true',
  logoBanner: false,
  link: 'https://www.linkedin.com/feed/update/urn:li:ugcPost:7464725884999073792',
  featured: true,
  category: 'funding',
  en: {
    badge: 'Training',
    title: 'FOUND delivers first round of training to 45 officials of Mexico’s National Search Commission',
    body: '<p>Following February’s MoU with <strong>Mexico’s National Search Commission (CNB)</strong>, we have completed the first round of training, delivered to <strong>45 CNB officials</strong>.</p><p><strong>CentroGeo</strong>, FOUND’s implementing partner, has developed two platforms that the CNB has now adopted as part of its official toolkit:</p><ul><li><strong>Global Index Mapper</strong> applies spectral indices to satellite and drone imagery to identify anomalies and substances associated with clandestine graves. It can detect not only the presence of anomalies, but the day they appeared.</li><li><strong>Espacio Clandestino</strong> uses machine learning to identify sites of forensic interest, drawing on patterns from clandestine graves documented to date.</li></ul><p>Global Index Mapper was tested in <strong>Colombia</strong> during our February knowledge exchange with the <em>Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)</em>, and successfully identified a site of forensic interest with the same precision documented across Mexican sites.</p><p>The second CNB cohort will take place in <strong>July</strong>, with the Commissioner herself participating. Together, we are shaping two streams of workshops to scale to Mexican states — one operational and one research-focused — along with user guides and video tutorials.</p><div class="li-embed"><iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7464725884999073792?compact=1" height="399" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe></div><p><a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7464725884999073792" target="_blank" rel="noopener noreferrer">View the post on LinkedIn ↗</a></p>'
  },
  es: {
    badge: 'Capacitación',
    title: 'FOUND imparte la primera ronda de capacitación a 45 funcionarias y funcionarios de la Comisión Nacional de Búsqueda de México',
    body: '<p>Tras el convenio (MoU) firmado en febrero con la <strong>Comisión Nacional de Búsqueda (CNB)</strong> de México, completamos la primera ronda de capacitación, impartida a <strong>45 funcionarias y funcionarios de la CNB</strong>.</p><p><strong>CentroGeo</strong>, socio implementador de FOUND, ha desarrollado dos plataformas que la CNB ha adoptado como parte de su caja de herramientas oficial:</p><ul><li><strong>Global Index Mapper</strong> aplica índices espectrales a imágenes satelitales y de dron para identificar anomalías y sustancias asociadas a fosas clandestinas. No solo detecta la presencia de anomalías, sino el día en que aparecieron.</li><li><strong>Espacio Clandestino</strong> usa aprendizaje automático para identificar sitios de interés forense, a partir de los patrones de fosas clandestinas documentadas hasta la fecha.</li></ul><p>Global Index Mapper se probó en <strong>Colombia</strong> durante nuestro intercambio de conocimiento de febrero con la <em>Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)</em>, e identificó con éxito un sitio de interés forense con la misma precisión documentada en los sitios mexicanos.</p><p>La segunda generación de la CNB se realizará en <strong>julio</strong>, con la participación de la propia Comisionada. Juntas y juntos estamos diseñando dos líneas de talleres para escalar hacia los estados de México — una operativa y otra centrada en investigación — junto con guías de usuario y tutoriales en video.</p><div class="li-embed"><iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7464725884999073792?compact=1" height="399" width="504" frameborder="0" allowfullscreen="" title="Publicación incrustada"></iframe></div><p><a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7464725884999073792" target="_blank" rel="noopener noreferrer">Ver la publicación en LinkedIn ↗</a></p>'
  }
},
{
  id: 'fcdo-renewed-funding',
  date: '2026-05-20',
  image: 'https://github.com/FOUND-project/found-project.github.io/blob/85aba9317a2a148a7a79cef400aed2709c7ce224/images/10%20logo%20FT%2Blogo_Primary%2Bversion_white%2Btext.png?raw=true',
  logoBanner: true,
  link: null,
  featured: true,
  category: 'funding',
  en: {
    badge: 'Funding',
    title: '2026: FOUND receives renewed support from the UK’s FCDO through the Frontier Tech Hub',
    body: '<p>🌱 Massive news — <strong>FOUND</strong> has just received confirmation of renewed support from the UK’s <strong>Foreign, Commonwealth and Development Office (FCDO)</strong> through the <strong>Frontier Tech Hub</strong>.</p><p>This new round of funding will let us develop, incorporate, and automate new layers into our spectral indices and machine-learning platforms — and scale them through our partnerships with 🇲🇽 <strong>Mexico’s National Search Commission</strong>, 🇨🇴 <strong>Colombia’s Search Unit</strong>, <strong>Locate International</strong>, and <strong>Human Rights Watch</strong>.</p><p>🔍 FOUND is guided by mothers’ search groups and researchers from Mexico and Colombia. Our mission is to drive systemic change in how missing persons are searched for.</p><p>🛰️ At FOUND we use advanced tools such as machine-learning models, hyperspectral cameras, satellite imagery, seismic instruments, and electrical resistivity to locate missing persons and bring families closer to answers.</p><p>📌 Alongside our partners at <strong>LAB-CO</strong>, we will present our results to date in <strong>Oxford on 26 June 2026</strong>. More details coming soon.</p><p><em>FOUND: Interpreting Nature to Locate Those We Are Missing.</em></p>'
  },
  es: {
    badge: 'Financiamiento',
    title: '2026: FOUND recibe apoyo financiero del FCDO del Reino Unido a través del Frontier Tech Hub',
    body: '<p>🌱 Gran noticia — <strong>FOUND</strong> acaba de recibir la confirmación del apoyo renovado del <strong>Foreign, Commonwealth and Development Office (FCDO)</strong> del Reino Unido, a través del <strong>Frontier Tech Hub</strong>.</p><p>Esta nueva ronda de financiamiento nos permitirá desarrollar, incorporar y automatizar nuevas capas en nuestras plataformas de índices espectrales y aprendizaje automático — y escalarlas a través de nuestras alianzas con 🇲🇽 la <strong>Comisión Nacional de Búsqueda de México</strong>, 🇨🇴 la <strong>Unidad de Búsqueda de Colombia</strong>, <strong>Locate International</strong> y <strong>Human Rights Watch</strong>.</p><p>🔍 FOUND está guiado por colectivos de madres buscadoras y por personas investigadoras de México y Colombia. Nuestra misión es impulsar un cambio sistémico en la forma de buscar a las personas desaparecidas.</p><p>🛰️ En FOUND usamos herramientas avanzadas como modelos de aprendizaje automático, cámaras hiperespectrales, imágenes satelitales, instrumentos sísmicos y resistividad eléctrica para localizar a personas desaparecidas y acercar a las familias a las respuestas.</p><p>📌 Junto con nuestras y nuestros aliados de <strong>LAB-CO</strong>, presentaremos nuestros resultados a la fecha en <strong>Oxford el 26 de junio de 2026</strong>. Pronto compartiremos más detalles.</p><p><em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em></p>'
  }
},
{
  id: 'colombia-ubpd-integration',
  date: '2026-02-16',
  image: 'https://github.com/FOUND-project/found-project.github.io/raw/c6e364287db0cf1e3afb28333b2c63f628212c8a/images/1772208968695.jpg?w=1200&h=630&fit=crop',
  link: 'https://www.linkedin.com/posts/miguelmoctezuma_updates-ugcPost-7439250842781831168-a57F?utm_source=share&utm_medium=member_desktop&rcm=ACoAAB_zGzMBBxcSdtDzNCGsySXIVWQmE2nBr-E',
  featured: true,
  category: 'field',
  en: {
    badge: 'Collaboration',
    title: 'FOUND integrates Global Index Mapper platform control with Colombia\'s Search Unit (UBPD)',
    body: '<p>We travelled to Colombia to work alongside the <strong>Search Unit (UBPD)</strong> team. The agency will now have full control of FOUND tools and the ability to incorporate new layers and settings.</p><p>The platforms, built by our core member <strong>CentroGeo</strong>, enable two critical capabilities:</p><p><strong>[1] Locating clandestine sites</strong> by cross-referencing AI, institutional data, and field evidence from our experimental sites in Mexico, narrowing where authorities need to search.</p><p><strong>[2] Detecting clandestine graves</strong> through spectral indices and satellite and drone imagery, reading the environmental traces left behind.</p><p>We have now integrated satellite imagery going back to the early 1980s. What drones cannot see today, satellites might have recorded. This approach has already proven effective in two cases, demonstrating the power of historical data in locating missing persons.</p><figure style="margin: 1.5em 0; text-align: center;"><img src="https://github.com/FOUND-project/found-project.github.io/raw/9d3b508af5c500046a0806cc047ff9a1b06dd5ab/images/IMG_20260217_165004.jpg?w=800" alt="FOUND team collaboration with Colombia UBPD" style="max-width: 100%; height: auto; border-radius: 8px; margin: 0.5em 0;"/></figure><figure style="margin: 1.5em 0; text-align: center;"><img src="https://github.com/FOUND-project/found-project.github.io/raw/9d3b508af5c500046a0806cc047ff9a1b06dd5ab/images/IMG_20260217_172823.jpg?w=800" alt="UBPD platform integration demonstration" style="max-width: 100%; height: auto; border-radius: 8px; margin: 0.5em 0;"/></figure><p><a href="https://www.linkedin.com/posts/miguelmoctezuma_updates-ugcPost-7439250842781831168-a57F?utm_source=share&utm_medium=member_desktop&rcm=ACoAAB_zGzMBBxcSdtDzNCGsySXIVWQmE2nBr-E" target="_blank" rel="noopener noreferrer">Read the full post on LinkedIn →</a></p>'
  },
  es: {
    badge: 'Colaboración',
    title: 'FOUND integra control de plataforma de índices espectrales con la Unidad de Búsqueda (UBPD) de Colombia',
    body: '<p>Viajamos a Colombia para trabajar junto al equipo de la <strong>Unidad de Búsqueda (UBPD)</strong>. La agencia ahora tendrá control total de las herramientas de FOUND y la capacidad de incorporar nuevas capas y configuraciones.</p><p>Las plataformas, construidas por nuestro miembro principal <strong>CentroGeo</strong>, habilitan dos capacidades críticas:</p><p><strong>[1] Localizar sitios clandestinos</strong> mediante la referencia cruzada de IA, datos institucionales y evidencia de campo de nuestros sitios experimentales en México, reduciendo dónde las autoridades necesitan buscar.</p><p><strong>[2] Detectar fosas clandestinas</strong> a través de índices espectrales e imágenes satelitales y de drones, leyendo los rastros ambientales dejados atrás.</p><p>Ahora hemos integrado imágenes satelitales desde principios de los años 1980. Lo que los drones no pueden ver hoy, los satélites podrían haber grabado. Este enfoque ya ha demostrado ser efectivo en dos casos, demostrando el poder de los datos históricos en la localización de personas desaparecidas.</p><figure style="margin: 1.5em 0; text-align: center;"><img src="https://github.com/FOUND-project/found-project.github.io/raw/9d3b508af5c500046a0806cc047ff9a1b06dd5ab/images/IMG_20260217_165004.jpg?w=800" alt="Colaboración del equipo FOUND con UBPD de Colombia" style="max-width: 100%; height: auto; border-radius: 8px; margin: 0.5em 0;"/></figure><figure style="margin: 1.5em 0; text-align: center;"><img src="https://github.com/FOUND-project/found-project.github.io/raw/9d3b508af5c500046a0806cc047ff9a1b06dd5ab/images/IMG_20260217_172823.jpg?w=800" alt="Demostración de integración de plataforma UBPD" style="max-width: 100%; height: auto; border-radius: 8px; margin: 0.5em 0;"/></figure><p><a href="https://www.linkedin.com/posts/miguelmoctezuma_updates-ugcPost-7439250842781831168-a57F?utm_source=share&utm_medium=member_desktop&rcm=ACoAAB_zGzMBBxcSdtDzNCGsySXIVWQmE2nBr-E" target="_blank" rel="noopener noreferrer">Leer la publicación completa en LinkedIn →</a></p>'
  }
},
        {
          id: 'cnb-agreement',
          date: '2026-03-23',
          image: 'https://github.com/FOUND-project/found-project.github.io/blob/8859fa47dfbaaabd7722b5849fe9bcfc62b2474f/images/firma%20Convenio%20CNB.jpg?raw=true',
          link: 'https://www.linkedin.com/posts/frontier-tech-hub_la-firma-del-acuerdo-entre-la-comisi%C3%B3n-nacional-activity-7444632239109332992-KOCM?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAB_zGzMBBxcSdtDzNCGsySXIVWQmE2nBr-E',
          featured: true,
          category: 'partnership',
          en: { badge: 'Partnership', title: 'FOUND signs agreement with Mexico\'s National Search Commission', body: '<p>FOUND has signed a landmark agreement with Mexico\'s <strong>National Search Commission</strong>, marking a significant step towards strengthening national search capacities.</p><p>Through this collaboration, authorities across the country will be trained in the use of FOUND\'s platforms to support the location of <strong>clandestine graves</strong> and the identification of <strong>substances linked to disappearances</strong>.</p><p>The training will integrate the use of <strong>satellite imagery</strong>, <strong>drone-based data collection</strong>, and <strong>artificial intelligence</strong>, combining cutting-edge technology with the knowledge of search communities.</p><p>This agreement represents a move towards institutionalising advanced search methodologies and scaling their impact nationwide.</p><p><a href="https://www.linkedin.com/posts/frontier-tech-hub_la-firma-del-acuerdo-entre-la-comisi%C3%B3n-nacional-activity-7444632239109332992-KOCM?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAB_zGzMBBxcSdtDzNCGsySXIVWQmE2nBr-E" target="_blank" rel="noopener noreferrer">Read the full post on LinkedIn →</a></p>' },
          es: { badge: 'Alianza', title: 'FOUND firma convenio con la Comisión Nacional de Búsqueda de México', body: '<p>FOUND firmó un convenio histórico con la <strong>Comisión Nacional de Búsqueda</strong>, marcando un paso clave para fortalecer las capacidades de búsqueda a nivel nacional.</p><p>A través de esta colaboración, autoridades en todo el país serán capacitadas en el uso de las plataformas de FOUND para apoyar la localización de <strong>fosas clandestinas</strong> y la identificación de <strong>sustancias vinculadas a desapariciones</strong>.</p><p>La capacitación integrará el uso de <strong>imágenes satelitales</strong>, <strong>recolección de datos mediante drones</strong> y <strong>inteligencia artificial</strong>, combinando tecnología de frontera con el conocimiento de las comunidades de búsqueda.</p><p>Este acuerdo representa un avance hacia la institucionalización de metodologías avanzadas de búsqueda y la ampliación de su impacto a nivel nacional.</p><p><a href="https://www.linkedin.com/posts/frontier-tech-hub_la-firma-del-acuerdo-entre-la-comisi%C3%B3n-nacional-activity-7444632239109332992-KOCM?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAB_zGzMBBxcSdtDzNCGsySXIVWQmE2nBr-E" target="_blank" rel="noopener noreferrer">Leer la publicación completa en LinkedIn →</a></p>' }
        },
        {
          id: 'mariela-award',
          date: '2026-01-15',
          image: 'https://github.com/FOUND-project/found-project.github.io/blob/f1d0e85892b4ab9e24779fdbc7ba7db2020a6679/images/Mariela_award.jpg?raw=true',
          link: 'https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh',
          featured: true,
          category: 'award',
          en: { badge: 'Award', title: 'FOUND\'s pioneer wins the UK FCDO\'s Sir Nicholas Browne Policy and Expertise Award', body: '<p>We are proud to share that <strong>Mariela Garfias</strong> has been awarded the <strong>Sir Nicholas Browne Policy and Expertise Award</strong>, a UK FCDO award recognising excellence in delivering policy objectives, selected from more than 200 nominations.</p><p>Mariela is FOUND\'s FCDO pioneer and one of the people most responsible for the project\'s impact.</p><p>Through FOUND, and with the support of incredible partners, we have located <strong>27 people</strong> who were victims of disappearance in Mexico, allowing families to move towards answers and a form of closure. Our work is now being embedded with local and national authorities, and has expanded to collaboration with the <strong>Colombian Search Unit</strong> and the Executive Office of the <strong>UN Secretary-General</strong>.</p><p>In her acceptance speech, Mariela shared words that capture the spirit of FOUND: "From my decomposed body, flowers shall grow, and I am in them. That is eternity." — Edvard Munch.</p><p>When searching for clandestine graves using technologies, nature often bears witness — through subtle changes in soil and vegetation. Memory persists. Our responsibility is to find it.</p><p>Mariela thanked those who carry this work with us: the British Embassy in Mexico City, our mentor <strong>Martin Johnston</strong>, the Frontier Tech Hub team, and above all the searching mothers, whose knowledge and strength remain our compass.</p><p><a href="https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh" target="_blank" rel="noopener noreferrer">Read the full post on LinkedIn ↗</a></p>' },
          es: { badge: 'Reconocimiento', title: 'La pioneer de FOUND recibe el Premio Sir Nicholas Browne de Política y Pericia del FCDO británico', body: '<p>Nos enorgullece compartir que <strong>Mariela Garfias</strong> ha recibido el <strong>Premio Sir Nicholas Browne de Política y Pericia</strong>, un reconocimiento del FCDO británico a la excelencia en la implementación de objetivos de política, seleccionado entre más de 200 nominaciones.</p><p>Mariela es la pionera de FOUND dentro del FCDO y una de las personas más responsables del impacto del proyecto.</p><p>A través de FOUND, y con el apoyo de aliadas y aliados extraordinarios, hemos localizado a <strong>27 personas</strong> víctimas de desaparición en México, permitiendo que sus familias avancen hacia respuestas y alguna forma de cierre. Nuestro trabajo se está incorporando a autoridades locales y nacionales, y se ha ampliado a una colaboración con la <strong>Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia</strong> y con la Oficina Ejecutiva del <strong>Secretario General de la ONU</strong>.</p><p>En su discurso de aceptación, Mariela compartió unas palabras que capturan el espíritu de FOUND: "De mi cuerpo descompuesto crecerán flores, y yo estoy en ellas. Eso es la eternidad". — Edvard Munch.</p><p>Al buscar fosas clandestinas con tecnologías, la naturaleza suele dar testimonio — a través de cambios sutiles en el suelo y la vegetación. La memoria persiste. Nuestra responsabilidad es encontrarla.</p><p>Mariela agradeció a quienes sostienen este trabajo con nosotras y nosotros: la Embajada Británica en Ciudad de México, nuestro mentor <strong>Martin Johnston</strong>, el equipo de Frontier Tech Hub y, sobre todo, las madres buscadoras, cuyo conocimiento y fuerza siguen siendo nuestra brújula.</p><p><a href="https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh" target="_blank" rel="noopener noreferrer">Leer la publicación completa en LinkedIn ↗</a></p>' }
        },
        {
          id: 'ubpd-visit',
          date: '2025-11-20',
          image: null,
          link: null,
          featured: false,
          category: 'field',
          en: { badge: 'Field visit', title: 'Second visit of Colombia\'s Search Unit for Missing Persons (UBPD) to FOUND\'s experimental sites in Jalisco', body: '<p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p><p>We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia\'s <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND\'s experimental sites in Jalisco.</p><p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND\'s experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p><p>It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p><p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND\'s detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD\'s team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND\'s partner states in Mexico.</p>' },
          es: { badge: 'Visita de campo', title: 'Segunda visita de la Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD) de Colombia a los sitios experimentales de FOUND en Jalisco', body: '<p>Agradecemos profundamente a <strong>CVM Cyber</strong> y a <strong>Ciaran Martin</strong> por su apoyo para hacer posible esta visita.</p><p>Recibimos a <strong>Héctor Javier Gómez</strong>, geofísico de la <em>Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)</em> de Colombia, para un despliegue conjunto en los sitios experimentales de FOUND en Jalisco.</p><p>La visita se centró en la obtención y el procesamiento de imágenes hiperespectrales mediante dron en los cinco sitios experimentales de FOUND — apenas la segunda vez que esta tecnología se utiliza en México con fines humanitarios.</p><p>Se trata de la continuación de la visita de octubre de 2025 de <strong>el Dr. Julián Arias</strong>, Director de Prospección, Recuperación e Identificación de la UBPD, que marcó el inicio formal de nuestra colaboración en metodologías de búsqueda e identificación.</p><p>Durante esta segunda visita, la UBPD compartió recomendaciones técnicas clave para reforzar las estrategias de FOUND para detectar fosas clandestinas. La colaboración continuará en enero de 2026, cuando el equipo de FOUND visitará a la UBPD en Colombia para intercambiar experiencias e integrar sus metodologías en los estados aliados de FOUND en México.</p>' }
        },
        {
          id: 'guardian-article',
          date: '2025-11-19',
          image: 'https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true',
          link: 'https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims',
          featured: false,
          category: 'media',
          en: { badge: 'Media', title: 'FOUND in The Guardian', body: '<img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND in The Guardian"><p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist\'s in-person visit to our experimental sites in Jalisco, Mexico.</p><p>We are deeply grateful for the care, depth, and commitment brought to this story after months spent listening to families, researchers, and officials.</p><p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener noreferrer">Read the article in The Guardian ↗</a></p>' },
          es: { badge: 'Medios', title: 'FOUND en The Guardian', body: '<img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND en The Guardian"><p>Este reportaje es el resultado de más de seis meses de correos electrónicos, mensajes de WhatsApp y la visita en terreno de la periodista a nuestros sitios experimentales en Jalisco, México.</p><p>Agradecemos profundamente el cuidado, la profundidad y el compromiso con el que se trabajó esta historia, tras meses escuchando a familias, personas investigadoras y autoridades.</p><p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener noreferrer">Leer el reportaje en The Guardian ↗</a></p>' }
        },
        {
          id: 'frontier-tech-funding',
          date: '2025-09-01',
          image: null,
          link: null,
          featured: false,
          category: 'funding',
          en: { badge: 'Funding', title: '2025: FOUND receives new support from the UK\'s FCDO through the Frontier Tech Hub', body: '<p>In the pitch, our team showcased FOUND\'s impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.</p><p><strong>🌱 Driven by families and research communities</strong><br>FOUND is guided and motivated by mothers\' search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.</p><p><strong>We are now working directly with:</strong></p><ul><li>Executive Office of the UN Secretary-General</li><li>UK\'s Foreign, Commonwealth &amp; Development Office (FCDO)</li><li>Local Search Commissions and Attorney\'s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li><li>Colombian Search Unit</li><li>Mexico\'s National Search Commission</li><li>Mexican Science and Technology Secretariat</li><li>British Embassy in Mexico City</li><li>British Association for Forensic Anthropology</li></ul><p><strong>Technology for memory, dignity, and closure</strong><br>We will continue developing — and embedding in official protocols — new ways to locate missing persons using advanced tools such as machine-learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.</p><p><em>FOUND: Interpreting Nature to Locate Those We Are Missing.</em></p>' },
          es: { badge: 'Financiamiento', title: '2025: FOUND recibe nuevo apoyo del FCDO del Reino Unido a través de Frontier Tech Hub', body: '<p>En la presentación, nuestro equipo mostró el impacto alcanzado por FOUND hasta la fecha, y recibimos una financiación que nos permitirá escalar nuestra misión: impulsar cambios sistémicos en la forma de buscar a las personas desaparecidas en México, Colombia y más allá.</p><p><strong>Impulsado por familias y comunidades de investigación</strong><br>FOUND está guiado y motivado por colectivos de madres buscadoras y por personas investigadoras de CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge y las Universidades Autónomas de Zacatecas y San Luis Potosí.</p><p><strong>Actualmente trabajamos directamente con:</strong></p><ul><li>Oficina Ejecutiva del Secretario General de la ONU</li><li>Foreign, Commonwealth &amp; Development Office (FCDO) del Reino Unido</li><li>Comisiones y Fiscalías de Búsqueda de Jalisco, Zacatecas, San Luis Potosí y Chihuahua (México)</li><li>Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia</li><li>Comisión Nacional de Búsqueda de Personas de México</li><li>Secretaría de Ciencia y Tecnología de México</li><li>Embajada Británica en México</li><li>British Association for Forensic Anthropology</li></ul><p><strong>Tecnología para la memoria, la dignidad y el cierre</strong><br>Continuaremos desarrollando — y ayudando a incorporar en los protocolos oficiales — nuevas formas de localizar a personas desaparecidas.</p><p><em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em></p>' }
        },
        {
          id: 'international-media',
          date: '2025-07-29',
          image: null,
          link: null,
          featured: false,
          category: 'coverage',
          en: { badge: 'Coverage', title: 'FOUND featured by Associated Press, The Independent, LA Times, VICE, and NBC', body: '<ul><li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li></ul>' },
          es: { badge: 'Cobertura', title: 'FOUND en Associated Press, The Independent, LA Times, VICE y NBC', body: '<ul><li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li></ul>' }
        }
      ];
      var UI = {
        en: { pill: 'NEWS · IMPACT · MEDIA', title: 'FOUND — News &amp; Updates', subtitle: 'Latest developments on our work across Mexico, Colombia, and beyond.', readMore: 'Read more', share: 'Share' },
        es: { pill: 'NOTICIAS · IMPACTO · MEDIOS', title: 'FOUND — Noticias y Actualizaciones', subtitle: 'Las novedades más recientes sobre nuestro trabajo en México, Colombia y más allá.', readMore: 'Leer más', share: 'Compartir' }
      };
      var lang = 'en';
      var activeCardId = null;
      function fmtDate(d, l) { try { var date = new Date(d + 'T00:00:00'); return date.toLocaleDateString(l === 'en' ? 'en-US' : 'es-MX', { year:'numeric', month:'long', day:'numeric' }); } catch(e) { return d; } }
      function cardById(id) { for (var i = 0; i < newsCards.length; i++) { if (newsCards[i].id === id) return newsCards[i]; } return null; }
      function setMeta(id, val) { var el = document.getElementById(id); if (el) el.setAttribute('content', val); }
      function badgeClass(cat) { var map = { award:'badge-award', media:'badge-media', field:'badge-field', funding:'badge-funding', coverage:'badge-coverage', partnership:'badge-field', training:'badge-funding' }; return map[cat] || 'badge-field'; }
      function bannerClass(cat) { var map = { award:'banner-award', media:'banner-media', field:'banner-field', funding:'banner-funding', coverage:'banner-coverage', partnership:'banner-field', training:'banner-funding' }; return map[cat] || 'banner-field'; }
      function renderGrid() {
        var grid = document.getElementById('news-grid');
        grid.innerHTML = '';
        var ui = UI[lang] || UI.en;
        newsCards.forEach(function(card) {
          var t = card[lang] || card.en;
          var article = document.createElement('article');
          article.className = 'news-card' + (card.featured ? ' featured' : '');
          article.setAttribute('role', 'button');
          article.setAttribute('tabindex', '0');
          article.setAttribute('aria-label', t.title);
          var bannerHtml;
          if (card.image && card.logoBanner) {
            bannerHtml = '<div class="card-banner logo-contain ' + bannerClass(card.category) + '"><img src="' + card.image + '" alt="" loading="lazy"></div>';
          } else if (card.image) {
            bannerHtml = '<div class="card-banner"><img src="' + card.image + '" alt="" loading="lazy"></div>';
          } else {
            bannerHtml = '<div class="card-banner no-photo ' + bannerClass(card.category) + '"><div class="card-banner-watermark"><img class="card-banner-logo" src="' + LOGO + '" alt=""><span class="card-banner-label">FOUND</span></div></div>';
          }
          article.innerHTML = bannerHtml + '<div class="card-body"><div class="card-meta"><span class="card-badge ' + badgeClass(card.category) + '">' + t.badge + '</span>' + (card.date ? '<span class="card-date">' + fmtDate(card.date, lang) + '</span>' : '') + '</div><span class="card-title">' + t.title + '</span><div class="card-cta"><span class="card-read-more">' + ui.readMore + '</span><span class="card-arrow"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></span></div></div>';
          article.addEventListener('click', function() { openModal(card.id); });
          article.addEventListener('keydown', function(e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(card.id); } });
          grid.appendChild(article);
        });
      }
      var overlay = document.getElementById('modal-overlay');
      var panel = document.getElementById('modal-panel');
      function openModal(id) {
        var card = cardById(id);
        if (!card) return;
        activeCardId = id;
        var t = card[lang] || card.en;
        var ui = UI[lang] || UI.en;
        var hero = document.getElementById('modal-hero');
        if (card.image && card.logoBanner) {
          hero.className = 'modal-hero logo-contain ' + bannerClass(card.category);
          hero.innerHTML = '<img class="modal-hero-img" src="' + card.image + '" alt="' + t.title.replace(/<[^>]*>/g,'') + '">';
        } else if (card.image) {
          hero.className = 'modal-hero' + (card.fullImage ? ' full-image' : '');
          hero.innerHTML = '<img class="modal-hero-img" src="' + card.image + '" alt="' + t.title.replace(/<[^>]*>/g,'') + '">' + (card.fullImage ? '' : '<img class="modal-img-wm" src="' + LOGO + '" alt="">');
        } else {
          hero.className = 'modal-hero';
          hero.innerHTML = '<div class="modal-hero-gradient ' + bannerClass(card.category) + '"><div class="modal-hero-wm"><img class="modal-hero-logo" src="' + LOGO + '" alt=""><span class="modal-hero-news-label">FOUND NEWS</span></div></div>';
        }
        var badge = document.getElementById('modal-badge');
        badge.className = 'modal-badge ' + badgeClass(card.category);
        badge.innerHTML = t.badge;
        document.getElementById('modal-date').textContent = card.date ? fmtDate(card.date, lang) : '';
        document.getElementById('modal-title-el').innerHTML = t.title;
        document.getElementById('modal-body').innerHTML = t.body;
        document.getElementById('share-label').textContent = ui.share;
        var plainTitle = t.title.replace(/<[^>]*>/g,'');
        setMeta('og-title', plainTitle);
        setMeta('og-description', plainTitle);
        setMeta('og-image', (card.image && !card.logoBanner) ? card.image : LOGO);
        setMeta('og-url', BASE_URL + 'cards/' + id);
        setMeta('tw-title', plainTitle);
        setMeta('tw-description', plainTitle);
        setMeta('tw-image', (card.image && !card.logoBanner) ? card.image : LOGO);
        history.replaceState(null, '', '#' + id);
        overlay.classList.add('active');
        panel.scrollTop = 0;
        document.body.style.overflow = 'hidden';
        document.getElementById('modal-close').focus();
      }
      function closeModal() {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
        activeCardId = null;
        history.replaceState(null, '', window.location.pathname);
      }
      document.getElementById('modal-close').addEventListener('click', closeModal);
      overlay.addEventListener('click', function(e) { if (e.target === overlay) closeModal(); });
      document.addEventListener('keydown', function(e) { if (e.key === 'Escape' && overlay.classList.contains('active')) closeModal(); });
      document.getElementById('btn-copy').addEventListener('click', function() {
        var url = BASE_URL + 'cards/' + (activeCardId || '');
        var btn = document.getElementById('btn-copy');
        var tip = document.getElementById('copy-tooltip');
        if (navigator.clipboard) {
          navigator.clipboard.writeText(url).then(function() {
            btn.classList.add('copied');
            tip.classList.add('show');
            setTimeout(function() { btn.classList.remove('copied'); tip.classList.remove('show'); }, 2200);
          });
        } else {
          var ta = document.createElement('textarea');
          ta.value = url;
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          btn.classList.add('copied');
          tip.classList.add('show');
          setTimeout(function() { btn.classList.remove('copied'); tip.classList.remove('show'); }, 2200);
        }
      });
      function setLang(l) {
        lang = l;
        var ui = UI[l] || UI.en;
        document.getElementById('news-pill').textContent = ui.pill;
        document.getElementById('news-title').innerHTML = ui.title;
        document.getElementById('news-subtitle').innerHTML = ui.subtitle;
        document.documentElement.lang = l === 'es' ? 'es' : 'en';
        document.querySelectorAll('.lang-btn').forEach(function(btn) { btn.classList.toggle('active', btn.dataset.lang === l); });
        renderGrid();
        if (activeCardId && overlay.classList.contains('active')) openModal(activeCardId);
        try { localStorage.setItem('found-lang', l); } catch(e) {}
      }
      document.addEventListener('DOMContentLoaded', function() {
        var saved = null;
        try { saved = localStorage.getItem('found-lang') || localStorage.getItem('found-lang-news'); } catch(e) {}
        var init = (saved === 'es' || saved === 'en') ? saved : 'en';
        document.querySelectorAll('.lang-btn').forEach(function(btn) { btn.addEventListener('click', function() { setLang(btn.dataset.lang); }); });
        setLang(init);
        var hash = window.location.hash.replace('#', '');
        if (hash && cardById(hash)) { setTimeout(function() { openModal(hash); }, 280); }
      });
      window.addEventListener('hashchange', function() {
        var hash = window.location.hash.replace('#', '');
        if (hash && cardById(hash)) openModal(hash);
        else closeModal();
      });
    })();
  </script>
</body>
</html>
