<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200">
  <title>FOUND — News & Updates</title>
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
  <style>
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    :root {
      --green-900: #0f2d22;
      --green-800: #1e4034;
      --green-700: #2d5f4d;
      --green-500: #4a8c73;
      --green-200: #c6e2d8;
      --green-50:  #f4faf7;
      --gold:      #d4af37;
      --text-dark:   #111827;
      --text-medium: #374151;
      --text-light:  #6b7280;
      --white:     #ffffff;
      --shadow-sm: 0 4px 16px rgba(15,23,42,.08);
      --shadow-md: 0 10px 28px rgba(15,23,42,.12);
      --shadow-lg: 0 24px 56px rgba(15,23,42,.18);
      --shadow-xl: 0 40px 80px rgba(15,23,42,.22);
      --radius-lg: 20px;
      --ease: cubic-bezier(.4,0,.2,1);
      --ease-spring: cubic-bezier(.34,1.56,.64,1);
    }
    html { scroll-behavior: smooth; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif;
      background: radial-gradient(ellipse 1400px 700px at 5% -5%,  rgba(212,175,55,.10) 0%, transparent 55%), radial-gradient(ellipse 1000px 600px at 90% 10%, rgba(198,226,216,.60) 0%, transparent 55%), linear-gradient(160deg, #f7fbfa 0%, #eef4f1 45%, #f9fbff 100%);
      min-height: 100vh;
      color: var(--text-dark);
      -webkit-font-smoothing: antialiased;
      padding: clamp(1.5rem,3vw,2.5rem) clamp(1rem,4vw,3rem);
    }
    .news-shell {
      max-width: 1320px;
      margin: 0 auto 0 5.6rem;
      position: relative;
    }
    .lang-toggle {
      position: absolute;
      top: .25rem; right: 0;
      display: inline-flex;
      gap: .45rem;
      z-index: 10;
    }
    .lang-btn {
      border: 1px solid rgba(15,23,42,.09);
      background: rgba(255,255,255,.88);
      color: var(--green-800);
      padding: .28rem .75rem;
      border-radius: 999px;
      font-size: .72rem;
      font-weight: 700;
      letter-spacing: .09em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(10px);
      box-shadow: 0 3px 12px rgba(15,23,42,.07);
      transition: transform .2s var(--ease), background .2s var(--ease), box-shadow .2s var(--ease);
    }
    .lang-btn:hover  { background:#fff; transform:translateY(-1px); box-shadow:0 7px 20px rgba(15,23,42,.14); }
    .lang-btn.active { background:var(--green-800); color:#fff; border-color:var(--green-800); }
    .news-header {
      position: relative;
      margin: 1.75rem 0 3rem;
      border-radius: var(--radius-lg);
      overflow: hidden;
      background: var(--white);
      box-shadow: var(--shadow-md);
      border: 1px solid rgba(15,23,42,.055);
      display: flex;
      align-items: stretch;
    }
    .news-header::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 5px;
      background: linear-gradient(180deg, var(--gold) 0%, rgba(212,175,55,.3) 100%);
    }
    .news-header::after {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(ellipse 600px 300px at -5% 0%, rgba(212,175,55,.13) 0%, transparent 60%), radial-gradient(ellipse 500px 300px at 110% 100%, rgba(198,226,216,.5) 0%, transparent 60%);
      pointer-events: none;
    }
    .news-header-logo {
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      padding: 2.2rem 2rem 2.2rem 2.8rem;
      position: relative;
      z-index: 1;
    }
    .news-header-logo img {
      width: 88px;
      height: 88px;
      border-radius: 20px;
      object-fit: cover;
      box-shadow: 0 12px 32px rgba(15,23,42,.22);
      border: 3px solid rgba(255,255,255,.95);
    }
    .news-header-divider {
      width: 1px;
      background: linear-gradient(180deg, transparent, rgba(15,23,42,.08), transparent);
      margin: 2rem 0;
      flex-shrink: 0;
    }
    .news-header-body {
      flex: 1;
      padding: 2.2rem 2.8rem 2.2rem 2.4rem;
      position: relative;
      z-index: 1;
    }
    .news-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: .5rem;
      margin-bottom: .65rem;
    }
    .news-eyebrow-dot {
      width: 7px; height: 7px;
      border-radius: 50%;
      background: var(--gold);
      box-shadow: 0 0 0 3px rgba(212,175,55,.2);
    }
    .news-eyebrow-text {
      font-size: .7rem;
      font-weight: 800;
      letter-spacing: .2em;
      text-transform: uppercase;
      color: var(--green-700);
    }
    #news-title {
      font-size: clamp(1.8rem, 3vw, 2.5rem);
      font-weight: 900;
      color: var(--green-900);
      letter-spacing: -.035em;
      line-height: 1.15;
      margin-bottom: .5rem;
    }
    #news-subtitle {
      font-size: clamp(.95rem, 1.3vw, 1.1rem);
      color: var(--text-medium);
      line-height: 1.75;
      max-width: 680px;
    }
    .news-stats {
      display: flex;
      gap: 2rem;
      margin-top: 1.4rem;
      padding-top: 1.2rem;
      border-top: 1px solid rgba(15,23,42,.06);
    }
    .news-stat {
      display: flex;
      flex-direction: column;
      gap: .1rem;
    }
    .news-stat-value {
      font-size: 1.35rem;
      font-weight: 900;
      color: var(--green-800);
    }
    .news-stat-label {
      font-size: .68rem;
      font-weight: 700;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--text-light);
    }
    .news-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: clamp(1.2rem, 2vw, 1.8rem);
      margin-bottom: 2rem;
      --stagger: 60ms;
    }
    .news-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      border: 1px solid rgba(15,23,42,.055);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      animation: cardIn .55s var(--ease) both;
      transition: transform .28s var(--ease), box-shadow .28s var(--ease);
    }
    .news-card:nth-child(1) { animation-delay: calc(1 * var(--stagger)); }
    .news-card:nth-child(2) { animation-delay: calc(2 * var(--stagger)); }
    .news-card:nth-child(3) { animation-delay: calc(3 * var(--stagger)); }
    .news-card:nth-child(4) { animation-delay: calc(4 * var(--stagger)); }
    .news-card:nth-child(5) { animation-delay: calc(5 * var(--stagger)); }
    .news-card:nth-child(6) { animation-delay: calc(6 * var(--stagger)); }
    @keyframes cardIn {
      from { opacity:0; transform:translateY(18px); }
      to   { opacity:1; transform:translateY(0); }
    }
    .news-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-lg);
    }
    .news-card.featured {
      border-top: 3px solid var(--gold);
    }
    .card-banner {
      width: 100%;
      height: 160px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .card-banner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform .55s var(--ease);
    }
    .news-card:hover .card-banner img {
      transform: scale(1.05);
    }
    .card-banner.no-photo {
      background: var(--banner-bg, linear-gradient(135deg, #1e4034 0%, #2d5f4d 100%));
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card-banner-watermark {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: .5rem;
    }
    .card-banner-logo {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      object-fit: cover;
      opacity: .32;
      border: 2px solid rgba(255,255,255,.25);
    }
    .card-banner-label {
      font-size: .62rem;
      font-weight: 800;
      letter-spacing: .22em;
      text-transform: uppercase;
      color: rgba(255,255,255,.45);
    }
    .card-banner::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, transparent 40%, rgba(10,24,18,.42) 100%);
      pointer-events: none;
    }
    .card-body {
      padding: 1.3rem 1.4rem 1.5rem;
      display: flex;
      flex-direction: column;
      flex: 1;
      gap: .5rem;
    }
    .card-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: .5rem;
    }
    .card-badge {
      display: inline-flex;
      align-items: center;
      gap: .3rem;
      padding: .16rem .6rem;
      border-radius: 999px;
      font-size: .66rem;
      font-weight: 800;
      letter-spacing: .13em;
      text-transform: uppercase;
      background: var(--badge-bg, rgba(30,64,52,.07));
      color: var(--badge-color, var(--green-800));
      border: 1px solid var(--badge-border, rgba(30,64,52,.16));
    }
    .card-date {
      font-size: .68rem;
      font-weight: 600;
      color: var(--text-light);
      letter-spacing: .03em;
      white-space: nowrap;
    }
    .card-title {
      font-size: 1.06rem;
      font-weight: 800;
      color: var(--green-900);
      line-height: 1.42;
      flex: 1;
    }
    .card-cta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: .4rem;
      padding-top: .9rem;
      border-top: 1px solid rgba(15,23,42,.055);
    }
    .card-read-more {
      font-size: .76rem;
      font-weight: 700;
      color: var(--green-700);
      letter-spacing: .04em;
    }
    .card-arrow {
      width: 28px; height: 28px;
      border-radius: 50%;
      background: var(--green-50);
      border: 1px solid rgba(45,95,77,.14);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background .2s var(--ease), transform .2s var(--ease-spring);
      flex-shrink: 0;
    }
    .card-arrow svg {
      width: 13px; height: 13px;
      stroke: var(--green-700);
      fill: none;
      stroke-width: 2.2;
      stroke-linecap: round;
    }
    .news-card:hover .card-arrow {
      background: var(--green-800);
      transform: translateX(3px);
    }
    .news-card:hover .card-arrow svg {
      stroke: #fff;
    }
    /* MODAL */
    .modal-overlay {
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: rgba(6,18,14,.62);
      backdrop-filter: blur(14px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      visibility: hidden;
      transition: opacity .32s var(--ease), visibility .32s var(--ease);
    }
    .modal-overlay.active {
      opacity: 1;
      visibility: visible;
    }
    .modal-panel {
      background: var(--white);
      border-radius: var(--radius-lg);
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: var(--shadow-xl);
      transform: translateY(22px) scale(.965);
      transition: transform .35s var(--ease-spring);
    }
    .modal-overlay.active .modal-panel {
      transform: translateY(0) scale(1);
    }
    .modal-hero {
      position: relative;
      min-height: 200px;
      overflow: hidden;
    }
    .modal-hero-img {
      width: 100%;
      display: block;
      max-height: 340px;
      object-fit: cover;
    }
    .modal-hero-gradient {
      min-height: 160px;
      background: var(--hero-bg, linear-gradient(135deg, #1e4034 0%, #2d5f4d 60%, #4a8c73 100%));
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .modal-hero-wm {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: .65rem;
    }
    .modal-hero-logo {
      width: 56px; height: 56px;
      border-radius: 14px;
      object-fit: cover;
      opacity: .55;
      border: 2px solid rgba(255,255,255,.3);
    }
    .modal-hero-news-label {
      font-size: .65rem;
      font-weight: 800;
      letter-spacing: .25em;
      text-transform: uppercase;
      color: rgba(255,255,255,.55);
    }
    .modal-img-wm {
      position: absolute;
      bottom: 1.1rem;
      right: 1.2rem;
      z-index: 2;
      width: 38px; height: 38px;
      border-radius: 10px;
      object-fit: cover;
      opacity: .55;
      border: 2px solid rgba(255,255,255,.4);
    }
    .modal-close {
      position: absolute;
      top: 1rem; right: 1rem;
      z-index: 10;
      width: 38px; height: 38px;
      border-radius: 50%;
      border: none;
      background: rgba(255,255,255,.9);
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--green-800);
      transition: transform .2s var(--ease-spring);
    }
    .modal-close:hover { transform: scale(1.1); background: #fff; }
    .modal-close svg {
      width: 16px; height: 16px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2.5;
    }
    .modal-content {
      padding: 2rem 2.5rem 1.6rem;
    }
    .modal-badge {
      display: inline-flex;
      align-items: center;
      gap: .3rem;
      padding: .18rem .65rem;
      border-radius: 999px;
      font-size: .68rem;
      font-weight: 800;
      text-transform: uppercase;
      background: var(--badge-bg, rgba(30,64,52,.07));
      color: var(--badge-color, var(--green-800));
      border: 1px solid var(--badge-border, rgba(30,64,52,.16));
    }
    .modal-date {
      font-size: .72rem;
      font-weight: 600;
      color: var(--text-light);
    }
    .modal-title {
      font-size: clamp(1.3rem, 2.4vw, 1.75rem);
      font-weight: 900;
      color: var(--green-900);
      line-height: 1.3;
      margin-bottom: 1.5rem;
      margin-top: 1rem;
    }
    .modal-divider {
      height: 1px;
      background: linear-gradient(90deg, var(--green-200), transparent);
      margin-bottom: 1.5rem;
    }
    .modal-body {
      color: var(--text-medium);
      line-height: 1.82;
    }
    .modal-body p { margin-bottom: 1rem; font-size: .97rem; }
    .modal-body a {
      color: var(--green-700);
      text-decoration: none;
      font-weight: 650;
      border-bottom: 2px solid rgba(45,95,77,.3);
    }
    .modal-body a:hover { border-bottom-color: var(--gold); }
    .modal-footer {
      display: flex;
      align-items: center;
      gap: .65rem;
      padding: 1.1rem 2.5rem 1.6rem;
      border-top: 1px solid rgba(15,23,42,.055);
    }
    .modal-share-label {
      font-size: .68rem;
      font-weight: 800;
      letter-spacing: .14em;
      text-transform: uppercase;
      color: var(--text-light);
      margin-right: .2rem;
    }
    .share-btn {
      width: 36px; height: 36px;
      border-radius: 50%;
      border: 1px solid rgba(15,23,42,.1);
      background: var(--green-50);
      color: var(--green-800);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: transform .2s var(--ease-spring);
    }
    .share-btn:hover { transform: translateY(-2px); background:#fff; }
    .share-btn svg { width: 15px; height: 15px; fill: currentColor; }
    .share-btn.copied { background: var(--green-800); color:#fff; }
    .copy-tooltip {
      font-size: .7rem;
      font-weight: 700;
      color: var(--green-700);
      opacity: 0;
      transition: opacity .25s;
      margin-left: .1rem;
    }
    .copy-tooltip.show { opacity: 1; }
    /* BADGE COLORS */
    .badge-award    { --badge-bg: rgba(212,175,55,.1); --badge-color:#8a6d00; --badge-border:rgba(212,175,55,.3); }
    .badge-media    { --badge-bg: rgba(59,130,246,.08); --badge-color:#1d4ed8; --badge-border:rgba(59,130,246,.22); }
    .badge-field    { --badge-bg: rgba(16,185,129,.08); --badge-color:#065f46; --badge-border:rgba(16,185,129,.22); }
    .badge-funding  { --badge-bg: rgba(139,92,246,.08); --badge-color:#5b21b6; --badge-border:rgba(139,92,246,.22); }
    .badge-coverage { --badge-bg: rgba(239,68,68,.07);  --badge-color:#991b1b; --badge-border:rgba(239,68,68,.2); }
    /* BANNER GRADIENTS */
    .banner-award    { --banner-bg: linear-gradient(135deg, #3d2a00 0%, #6b4c00 60%, #8a6d00 100%); }
    .banner-media    { --banner-bg: linear-gradient(135deg, #0f1f40 0%, #1e3a8a 60%, #2563eb 100%); }
    .banner-field    { --banner-bg: linear-gradient(135deg, #052e16 0%, #14532d 60%, #166534 100%); }
    .banner-funding  { --banner-bg: linear-gradient(135deg, #2e1065 0%, #4c1d95 60%, #6d28d9 100%); }
    .banner-coverage { --banner-bg: linear-gradient(135deg, #450a0a 0%, #7f1d1d 60%, #b91c1c 100%); }
    @media (max-width: 900px) {
      body { padding: 1.4rem 1rem; }
      .news-shell { margin-left: 0; }
      .news-header { flex-direction: column; }
      .news-header-divider { display: none; }
      .news-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <div class="news-shell">
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
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
        <div class="news-stats">
          <div class="news-stat">
            <span class="news-stat-value">27</span>
            <span class="news-stat-label" id="stat-label-located">Located</span>
          </div>
          <div class="news-stat">
            <span class="news-stat-value">5</span>
            <span class="news-stat-label" id="stat-label-states">Partner states</span>
          </div>
          <div class="news-stat">
            <span class="news-stat-value">3+</span>
            <span class="news-stat-label" id="stat-label-countries">Countries</span>
          </div>
        </div>
      </div>
    </header>
    <section class="news-grid" id="news-grid" aria-label="News articles"></section>
  </div>
  <!-- MODAL -->
  <div class="modal-overlay" id="modal-overlay" role="dialog" aria-modal="true">
    <div class="modal-panel" id="modal-panel">
      <button class="modal-close" id="modal-close" aria-label="Close">
        <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      <div class="modal-hero" id="modal-hero"></div>
      <div class="modal-content">
        <div style="display:flex; align-items:center; gap:.65rem; margin-bottom:.9rem; flex-wrap:wrap;">
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
    
      {id:'cnb-agreement',date:'2025-07-01',image:'https://github.com/FOUND-project/found-project.github.io/blob/8859fa47dfbaaabd7722b5849fe9bcfc62b2474f/images/firma%20Convenio%20CNB.jpg?raw=true',featured:true,category:'partnership',en:{badge:'Partnership',title:'FOUND signs agreement with Mexico\'s National Search Commission',body:'<p>FOUND has signed a landmark agreement with Mexico\'s <strong>National Search Commission</strong>, marking a significant step towards strengthening national search capacities.</p>'},es:{badge:'Alianza',title:'FOUND firma convenio con la Comisión Nacional de Búsqueda de México',body:'<p>FOUND firmó un convenio histórico con la <strong>Comisión Nacional de Búsqueda</strong>.</p>'},nah:{badge:'Tlasentilistli',title:'FOUND kichiwa convenio iuan Comisión Nacional de Búsqueda',body:'<p>FOUND okichij se hueyi convenio iuan Comisión Nacional de Búsqueda.</p>'}},
    
      {id:'mariela-award',date:'2025-06-15',image:null,featured:true,category:'award',en:{badge:'Award',title:'FOUND\'s pioneer wins the UK FCDO\'s Sir Nicholas Browne Award',body:'<p>We are proud to share that <strong>Mariela Garfias</strong> has been awarded the <strong>Sir Nicholas Browne Policy and Expertise Award</strong>.</p>'},es:{badge:'Reconocimiento',title:'La pioneer de FOUND recibe el Premio Sir Nicholas Browne',body:'<p>Nos enorgullece compartir que <strong>Mariela Garfias</strong> ha recibido el <strong>Premio Sir Nicholas Browne</strong>.</p>'},nah:{badge:'Tlatlepanitaliztli',title:'In pioneer de FOUND kiseli in Premio Sir Nicholas Browne',body:'<p>Tiquinechpoua ika pakilistli ke <strong>Mariela Garfias</strong> okiseli in <strong>Premio Sir Nicholas Browne</strong>.</p>'}},
     
      {id:'ubpd-visit',date:'2025-11-20',image:null,featured:false,category:'field',en:{badge:'Field visit',title:'Colombia\'s UBPD visits FOUND\'s experimental sites',body:'<p>We welcomed <strong>Héctor Javier Gómez</strong> from Colombia\'s UBPD for field deployment to FOUND\'s experimental sites in Jalisco.</p>'},es:{badge:'Visita de campo',title:'La UBPD de Colombia visita los sitios experimentales de FOUND',body:'<p>Recibimos a <strong>Héctor Javier Gómez</strong> de la UBPD de Colombia.</p>'},nah:{badge:'Tlayekoliztli',title:'UBPD de Colombia tlanpohuiliah sitios experimentales',body:'<p>Otikweltaskeh <strong>Héctor Javier Gómez</strong> de UBPD.</p>'}},
    
      {id:'guardian-article',date:'2025-11-19',image:'https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true',featured:false,category:'media',en:{badge:'Media',title:'FOUND featured in The Guardian',body:'<p>This piece is the result of months of research and field visits to our experimental sites in Jalisco.</p>'},es:{badge:'Medios',title:'FOUND en The Guardian',body:'<p>Este reportaje es resultado de meses de investigación.</p>'},nah:{badge:'Medios',title:'FOUND ipan The Guardian',body:'<p>Nin reportaje omochi ika metztli de investigación.</p>'}},
    
      {id:'frontier-tech',date:'2025-09-01',image:null,featured:false,category:'funding',en:{badge:'Funding',title:'FOUND receives new support from Frontier Tech Hub',body:'<p>We were awarded funding through the UK\'s FCDO Frontier Tech Hub programme.</p>'},es:{badge:'Financiación',title:'FOUND recibe apoyo del Frontier Tech Hub',body:'<p>Recibimos financiación del FCDO del Reino Unido.</p>'},nah:{badge:'Financiamiento',title:'FOUND kiselia tlapalehuiliztli de Frontier Tech Hub',body:'<p>Otikselijkeh se financiamiento.</p>'}},
     
      {id:'international-media',date:'2025-07-29',image:null,featured:false,category:'coverage',en:{badge:'Coverage',title:'FOUND featured internationally',body:'<p>Our work was featured in Associated Press, The Independent, LA Times, VICE, and NBC.</p>'},es:{badge:'Cobertura',title:'FOUND en medios internacionales',body:'<p>Nuestro trabajo fue reportado en medios internacionales.</p>'},nah:{badge:'Tlayekoliztli',title:'FOUND ipan medios internacionales',body:'<p>Nin tequitl okichihualoni ipan medios.</p>'}}
    ];
   
    var UI = {en:{pill:'NEWS · IMPACT · MEDIA',title:'FOUND — News &amp; Updates',subtitle:'Latest developments on our work across Mexico, Colombia, and beyond.',readMore:'Read more',share:'Share',statLocated:'Located',statStates:'Partner states',statCountries:'Countries'},es:{pill:'NOTICIAS · IMPACTO · MEDIOS',title:'FOUND — Noticias y Actualizaciones',subtitle:'Novedades de nuestro trabajo en México, Colombia y más allá.',readMore:'Leer más',share:'Compartir',statLocated:'Localizadas',statStates:'Estados aliados',statCountries:'Países'},nah:{pill:'TLATLAHCUILOLLI · TLAKAMEH · MEDIOS',title:'FOUND — Tlen mochihua huan tlen pano',subtitle:'Nuevas tlamantli tlen totlatequi.',readMore:'Xikpoua okachi',share:'Xiktemaka',statLocated:'Telnextijkeh',statStates:'Estados',statCountries:'Tlaltipaktli'}};
    var lang = 'en';
    var activeCardId = null;
    function fmtDate(d,l){try{var date=new Date(d+'T00:00:00');return date.toLocaleDateString(l==='en'?'en-US':'es-MX',{year:'numeric',month:'long',day:'numeric'})}catch(e){return d}}
    function cardById(id){for(var i=0;i<newsCards.length;i++){if(newsCards[i].id===id)return newsCards[i]}return null}
    function badgeClass(cat){var map={award:'badge-award',media:'badge-media',field:'badge-field',funding:'badge-funding',coverage:'badge-coverage'};return map[cat]||'badge-field'}
    function bannerClass(cat){var map={award:'banner-award',media:'banner-media',field:'banner-field',funding:'banner-funding',coverage:'banner-coverage'};return map[cat]||'banner-field'}
    function renderGrid(){
      var grid=document.getElementById('news-grid');
      grid.innerHTML='';
      var ui=UI[lang]||UI.en;
      newsCards.forEach(function(card){
        var t=card[lang]||card.en;
        var article=document.createElement('article');
        article.className='news-card'+(card.featured?' featured':'');
        article.setAttribute('role','button');
        article.setAttribute('tabindex','0');
        var bannerHtml=card.image?'<div class="card-banner"><img src="'+card.image+'" alt="" loading="lazy"></div>':'<div class="card-banner no-photo '+bannerClass(card.category)+'"><div class="card-banner-watermark"><img class="card-banner-logo" src="'+LOGO+'" alt=""><span class="card-banner-label">FOUND</span></div></div>';
        article.innerHTML=bannerHtml+'<div class="card-body"><div class="card-meta"><span class="card-badge '+badgeClass(card.category)+'">'+t.badge+'</span>'+(card.date?'<span class="card-date">'+fmtDate(card.date,lang)+'</span>':'')+' </div><span class="card-title">'+t.title+'</span><div class="card-cta"><span class="card-read-more">'+ui.readMore+'</span><span class="card-arrow"><svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg></span></div></div>';
        article.addEventListener('click',function(){openModal(card.id)});
        grid.appendChild(article);
      });
    }
    var overlay=document.getElementById('modal-overlay');
    var panel=document.getElementById('modal-panel');
    function openModal(id){
      var card=cardById(id);
      if(!card)return;
      activeCardId=id;
      var t=card[lang]||card.en;
      var ui=UI[lang]||UI.en;
      var hero=document.getElementById('modal-hero');
      if(card.image){hero.innerHTML='<img class="modal-hero-img" src="'+card.image+'" alt="'+t.title.replace(/<[^>]*>/g,'')+'"><img class="modal-img-wm" src="'+LOGO+'" alt="">';}else{hero.innerHTML='<div class="modal-hero-gradient '+bannerClass(card.category)+'"><div class="modal-hero-wm"><img class="modal-hero-logo" src="'+LOGO+'" alt=""><span class="modal-hero-news-label">FOUND NEWS</span></div></div>';}
      var badge=document.getElementById('modal-badge');
      badge.className='modal-badge '+badgeClass(card.category);
      badge.innerHTML=t.badge;
      document.getElementById('modal-date').textContent=card.date?fmtDate(card.date,lang):'';
      document.getElementById('modal-title-el').innerHTML=t.title;
      document.getElementById('modal-body').innerHTML=t.body;
      document.getElementById('share-label').textContent=ui.share;
      history.replaceState(null,'','#'+id);
      overlay.classList.add('active');
      panel.scrollTop=0;
      document.body.style.overflow='hidden';
    }
    function closeModal(){overlay.classList.remove('active');document.body.style.overflow='';activeCardId=null;history.replaceState(null,'',window.location.pathname);}
    document.getElementById('modal-close').addEventListener('click',closeModal);
    overlay.addEventListener('click',function(e){if(e.target===overlay)closeModal()});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&overlay.classList.contains('active'))closeModal()});
    document.getElementById('btn-copy').addEventListener('click',function(){
      var url=BASE_URL+'cards/'+(activeCardId||'');
      var btn=document.getElementById('btn-copy');
      var tip=document.getElementById('copy-tooltip');
      if(navigator.clipboard){navigator.clipboard.writeText(url).then(function(){btn.classList.add('copied');tip.classList.add('show');setTimeout(function(){btn.classList.remove('copied');tip.classList.remove('show')},2200)});}else{var ta=document.createElement('textarea');ta.value=url;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);btn.classList.add('copied');tip.classList.add('show');setTimeout(function(){btn.classList.remove('copied');tip.classList.remove('show')},2200);}
    });
    function setLang(l){
      lang=l;
      var ui=UI[l]||UI.en;
      document.getElementById('news-pill').textContent=ui.pill;
      document.getElementById('news-title').innerHTML=ui.title;
      document.getElementById('news-subtitle').innerHTML=ui.subtitle;
      document.getElementById('stat-label-located').textContent=ui.statLocated;
      document.getElementById('stat-label-states').textContent=ui.statStates;
      document.getElementById('stat-label-countries').textContent=ui.statCountries;
      document.documentElement.lang=l==='es'?'es':(l==='nah'?'nah':'en');
      document.querySelectorAll('.lang-btn').forEach(function(btn){btn.classList.toggle('active',btn.dataset.lang===l)});
      renderGrid();
      if(activeCardId&&overlay.classList.contains('active'))openModal(activeCardId);
      try{localStorage.setItem('found-lang-news',l);}catch(e){}
    }
    document.addEventListener('DOMContentLoaded',function(){
      var saved=null;
      try{saved=localStorage.getItem('found-lang-news');}catch(e){}
      var init=(saved==='es'||saved==='en'||saved==='nah')?saved:'en';
      document.querySelectorAll('.lang-btn').forEach(function(btn){btn.addEventListener('click',function(){setLang(btn.dataset.lang)})});
      setLang(init);
      var hash=window.location.hash.replace('#','');
      if(hash&&cardById(hash)){setTimeout(function(){openModal(hash)},280);}
    });
    window.addEventListener('hashchange',function(){var hash=window.location.hash.replace('#','');if(hash&&cardById(hash))openModal(hash);else closeModal()});
  })();
  </script>
</body>
</html>
