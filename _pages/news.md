---
layout: archive
title: "News"
permalink: /news/
author_profile: true
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
      *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
      }
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, system-ui, sans-serif;
      background:
        radial-gradient(ellipse 1400px 700px at 5% -5%,  rgba(212,175,55,.10) 0%, transparent 55%),
        radial-gradient(ellipse 1000px 600px at 90% 10%, rgba(198,226,216,.60) 0%, transparent 55%),
        linear-gradient(160deg, #f7fbfa 0%, #eef4f1 45%, #f9fbff 100%);
      min-height: 100vh;
      color: var(--text-dark);
      -webkit-font-smoothing: antialiased;
      padding: clamp(1.5rem,3vw,2.5rem) clamp(1rem,4vw,3rem);
    }

    /* Full-width override for Minimal Mistakes */
    .page, #main, .initial-content, .page__inner-wrap, .page__content, .archive {
      max-width: none !important;
      width: 100% !important;
    }

    *:focus-visible {
      outline: 3px solid rgba(74,140,115,.55);
      outline-offset: 3px;
      border-radius: var(--radius-sm);
    }

    /* ═══════════════════════════════════════════════════════
       SHELL
       ═══════════════════════════════════════════════════════ */
    .news-shell {
      max-width: 1320px;
      margin: 0 auto 0 5.6rem;
      position: relative;
    }

    /* ── Language toggle ── */
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
      border-radius: var(--radius-pill);
      font-size: .72rem;
      font-weight: 700;
      letter-spacing: .09em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(10px);
      box-shadow: 0 3px 12px rgba(15,23,42,.07);
      transition: transform .2s var(--ease), background .2s var(--ease),
                  box-shadow .2s var(--ease), color .2s var(--ease),
                  border-color .2s var(--ease);
    }
    .lang-btn:hover  { background:#fff; transform:translateY(-1px); box-shadow:0 7px 20px rgba(15,23,42,.14); }
    .lang-btn.active { background:var(--green-800); color:#fff; border-color:var(--green-800); }

    /* ═══════════════════════════════════════════════════════
       PAGE HEADER — rich editorial banner
       ═══════════════════════════════════════════════════════ */
    .news-header {
      position: relative;
      margin: 1.75rem 0 3rem;
      border-radius: var(--radius-xl);
      overflow: hidden;
      background: var(--white);
      box-shadow: var(--shadow-md);
      border: 1px solid rgba(15,23,42,.055);
      display: flex;
      align-items: stretch;
    }

    /* Gold left stripe */
    .news-header::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 5px;
      background: linear-gradient(180deg, var(--gold) 0%, rgba(212,175,55,.3) 100%);
      border-radius: var(--radius-xl) 0 0 var(--radius-xl);
    }

    /* Radial glow */
    .news-header::after {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 600px 300px at -5% 0%, rgba(212,175,55,.13) 0%, transparent 60%),
        radial-gradient(ellipse 500px 300px at 110% 100%, rgba(198,226,216,.5) 0%, transparent 60%);
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
      background: #fff;
    }

    /* Subtle divider */
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
      display: flex;
      flex-direction: column;
      justify-content: center;
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

    /* Stats row */
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
      letter-spacing: -.03em;
    }
    .news-stat-label {
      font-size: .68rem;
      font-weight: 700;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--text-light);
    }

    /* ═══════════════════════════════════════════════════════
       CARD GRID
       ═══════════════════════════════════════════════════════ */
    .news-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: clamp(1.2rem, 2vw, 1.8rem);
      margin-bottom: 2rem;
      /* Stagger animation */
      --stagger: 60ms;
    }

    /* ── Individual card ── */
    .news-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      border: 1px solid rgba(15,23,42,.055);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      position: relative;
      transition:
        transform   .28s var(--ease),
        box-shadow  .28s var(--ease),
        border-color .28s var(--ease);

      /* Entrance animation */
      animation: cardIn .55s var(--ease) both;
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
      border-color: rgba(45,95,77,.22);
    }

    /* Gold accent for featured card */
    .news-card.featured {
      border-top: 3px solid var(--gold);
    }

    /* ── Card visual banner ── */
    .card-banner {
      width: 100%;
      height: 160px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }

    /* Photo variant */
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

    /* No-photo: gradient pattern variant */
    .card-banner.no-photo {
      background: var(--banner-bg, linear-gradient(135deg, #1e4034 0%, #2d5f4d 100%));
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* SVG icon inside no-photo banner */
    .card-banner-icon {
      width: 52px;
      height: 52px;
      opacity: .22;
      color: #fff;
    }
    .card-banner-icon svg {
      width: 100%;
      height: 100%;
      fill: currentColor;
    }

    /* FOUND watermark in no-photo banner */
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

    /* Gradient overlay on photo banners */
    .card-banner::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, transparent 40%, rgba(10,24,18,.42) 100%);
      pointer-events: none;
    }

    /* ── Card body ── */
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
      border-radius: var(--radius-pill);
      font-size: .66rem;
      font-weight: 800;
      letter-spacing: .13em;
      text-transform: uppercase;
      background: var(--badge-bg, rgba(30,64,52,.07));
      color: var(--badge-color, var(--green-800));
      border: 1px solid var(--badge-border, rgba(30,64,52,.16));
    }
    .card-badge::before {
      content: '';
      width: 5px; height: 5px;
      border-radius: 50%;
      background: currentColor;
      opacity: .7;
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
      letter-spacing: -.015em;
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
      transition: background .2s var(--ease), transform .2s var(--ease-spring), box-shadow .2s var(--ease);
      flex-shrink: 0;
    }
    .card-arrow svg {
      width: 13px; height: 13px;
      stroke: var(--green-700);
      fill: none;
      stroke-width: 2.2;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: stroke .2s;
    }
    .news-card:hover .card-arrow {
      background: var(--green-800);
      transform: translateX(3px);
      box-shadow: 0 6px 16px rgba(30,64,52,.3);
    }
    .news-card:hover .card-arrow svg {
      stroke: #fff;
    }

    /* ═══════════════════════════════════════════════════════
       MODAL
       ═══════════════════════════════════════════════════════ */
    .modal-overlay {
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: rgba(6,18,14,.62);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
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
      border-radius: var(--radius-xl);
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      overflow-x: hidden;
      box-shadow: var(--shadow-xl), 0 0 0 1px rgba(15,23,42,.06);
      transform: translateY(22px) scale(.965);
      transition: transform .35s var(--ease-spring);
      scrollbar-width: thin;
      scrollbar-color: var(--green-200) transparent;
      position: relative;
    }
    .modal-overlay.active .modal-panel {
      transform: translateY(0) scale(1);
    }
    .modal-panel::-webkit-scrollbar { width: 5px; }
    .modal-panel::-webkit-scrollbar-track { background: transparent; }
    .modal-panel::-webkit-scrollbar-thumb { background: var(--green-200); border-radius: 10px; }

    /* Modal hero / image area */
    .modal-hero {
      position: relative;
      min-height: 200px;
      overflow: hidden;
    }

    /* Hero with image */
    .modal-hero-img {
      width: 100%;
      display: block;
      max-height: 340px;
      object-fit: cover;
    }

    /* Hero without image — gradient banner */
    .modal-hero-gradient {
      min-height: 160px;
      background: var(--hero-bg, linear-gradient(135deg, #1e4034 0%, #2d5f4d 60%, #4a8c73 100%));
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }
    /* Subtle noise texture overlay */
    .modal-hero-gradient::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 80% 60% at 15% -10%, rgba(212,175,55,.22) 0%, transparent 60%),
        radial-gradient(ellipse 60% 80% at 90% 110%, rgba(255,255,255,.07) 0%, transparent 60%);
    }
    .modal-hero-wm {
      position: relative;
      z-index: 1;
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
      box-shadow: 0 8px 24px rgba(0,0,0,.25);
    }
    .modal-hero-news-label {
      font-size: .65rem;
      font-weight: 800;
      letter-spacing: .25em;
      text-transform: uppercase;
      color: rgba(255,255,255,.55);
    }

    /* Gradient overlay on image hero */
    .modal-hero::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, transparent 30%, rgba(10,24,18,.5) 100%);
      pointer-events: none;
    }

    /* Watermark logo overlaid on image */
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
      box-shadow: 0 4px 14px rgba(0,0,0,.3);
    }

    /* Close button */
    .modal-close {
      position: absolute;
      top: 1rem; right: 1rem;
      z-index: 10;
      width: 38px; height: 38px;
      border-radius: 50%;
      border: none;
      background: rgba(255,255,255,.9);
      backdrop-filter: blur(10px);
      box-shadow: 0 4px 16px rgba(15,23,42,.18);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--green-800);
      transition: transform .2s var(--ease-spring), box-shadow .2s var(--ease), background .2s;
    }
    .modal-close:hover {
      transform: scale(1.1);
      box-shadow: 0 8px 24px rgba(15,23,42,.24);
      background: #fff;
    }
    .modal-close svg {
      width: 16px; height: 16px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2.5;
      stroke-linecap: round;
    }

    /* Modal content area */
    .modal-content {
      padding: 2rem 2.5rem 1.6rem;
    }

    .modal-meta {
      display: flex;
      align-items: center;
      gap: .65rem;
      margin-bottom: .9rem;
      flex-wrap: wrap;
    }

    .modal-badge {
      display: inline-flex;
      align-items: center;
      gap: .3rem;
      padding: .18rem .65rem;
      border-radius: var(--radius-pill);
      font-size: .68rem;
      font-weight: 800;
      letter-spacing: .14em;
      text-transform: uppercase;
      background: var(--badge-bg, rgba(30,64,52,.07));
      color: var(--badge-color, var(--green-800));
      border: 1px solid var(--badge-border, rgba(30,64,52,.16));
    }
    .modal-badge::before {
      content: '';
      width: 5px; height: 5px;
      border-radius: 50%;
      background: currentColor;
      opacity: .7;
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
      letter-spacing: -.025em;
      margin-bottom: 1.5rem;
    }

    /* Divider */
    .modal-divider {
      height: 1px;
      background: linear-gradient(90deg, var(--green-200), transparent);
      margin-bottom: 1.5rem;
    }

    /* Body text */
    .modal-body {
      color: var(--text-medium);
      line-height: 1.82;
    }
    .modal-body p   { margin-bottom: 1rem; font-size: .97rem; }
    .modal-body strong { color: var(--green-900); font-weight: 700; }
    .modal-body em  { font-style: italic; }
    .modal-body a {
      color: var(--green-700);
      text-decoration: none;
      font-weight: 650;
      border-bottom: 2px solid rgba(45,95,77,.3);
      padding-bottom: .05rem;
      transition: border-color .2s, color .2s;
    }
    .modal-body a:hover { border-bottom-color: var(--gold); color: var(--green-700); }
    .modal-body ul { margin: .8rem 0 1.1rem 1.4rem; }
    .modal-body ul li { margin-bottom: .5rem; font-size: .97rem; }
    .modal-body img {
      width: 100%;
      border-radius: var(--radius-md);
      margin: 1.2rem 0 1rem;
      box-shadow: var(--shadow-md);
    }

    /* Share footer */
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
      transition: transform .2s var(--ease-spring), box-shadow .2s var(--ease), background .2s, border-color .2s;
    }
    .share-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(30,64,52,.2); background:#fff; }
    .share-btn svg { width: 15px; height: 15px; fill: currentColor; }
    .share-btn.copied { background: var(--green-800); color:#fff; border-color: var(--green-800); }

    .copy-tooltip {
      font-size: .7rem;
      font-weight: 700;
      color: var(--green-700);
      opacity: 0;
      transition: opacity .25s;
      margin-left: .1rem;
    }
    .copy-tooltip.show { opacity: 1; }

    /* ═══════════════════════════════════════════════════════
       BADGE COLOR THEMES (per category)
       ═══════════════════════════════════════════════════════ */
    .badge-award    { --badge-bg: rgba(212,175,55,.1); --badge-color:#8a6d00; --badge-border:rgba(212,175,55,.3); }
    .badge-media    { --badge-bg: rgba(59,130,246,.08); --badge-color:#1d4ed8; --badge-border:rgba(59,130,246,.22); }
    .badge-field    { --badge-bg: rgba(16,185,129,.08); --badge-color:#065f46; --badge-border:rgba(16,185,129,.22); }
    .badge-funding  { --badge-bg: rgba(139,92,246,.08); --badge-color:#5b21b6; --badge-border:rgba(139,92,246,.22); }
    .badge-coverage { --badge-bg: rgba(239,68,68,.07);  --badge-color:#991b1b; --badge-border:rgba(239,68,68,.2); }

    /* ═══════════════════════════════════════════════════════
       BANNER GRADIENT THEMES
       ═══════════════════════════════════════════════════════ */
    .banner-award    { --banner-bg: linear-gradient(135deg, #3d2a00 0%, #6b4c00 60%, #8a6d00 100%); }
    .banner-media    { --banner-bg: linear-gradient(135deg, #0f1f40 0%, #1e3a8a 60%, #2563eb 100%); }
    .banner-field    { --banner-bg: linear-gradient(135deg, #052e16 0%, #14532d 60%, #166534 100%); }
    .banner-funding  { --banner-bg: linear-gradient(135deg, #2e1065 0%, #4c1d95 60%, #6d28d9 100%); }
    .banner-coverage { --banner-bg: linear-gradient(135deg, #450a0a 0%, #7f1d1d 60%, #b91c1c 100%); }

    /* ═══════════════════════════════════════════════════════
       RESPONSIVE
       ═══════════════════════════════════════════════════════ */
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

    <!-- LANGUAGE TOGGLE -->
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
    </div>

    <!-- PAGE HEADER -->
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

    <!-- CARD GRID — auto-generated by JS -->
    <section class="news-grid" id="news-grid" aria-label="News articles"></section>

  </div><!-- /news-shell -->

  <!-- MODAL (single reusable) -->
  <div class="modal-overlay" id="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="modal-title-el">
    <div class="modal-panel" id="modal-panel">

      <button class="modal-close" id="modal-close" aria-label="Close">
        <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>

      <!-- Hero image / gradient banner -->
      <div class="modal-hero" id="modal-hero"></div>

      <!-- Title / meta -->
      <div class="modal-content">
        <div class="modal-meta">
          <span class="modal-badge" id="modal-badge"></span>
          <span class="modal-date"  id="modal-date"></span>
        </div>
        <h2 class="modal-title" id="modal-title-el"></h2>
        <div class="modal-divider"></div>
        <div class="modal-body"   id="modal-body"></div>
      </div>

      <!-- Share row -->
      <div class="modal-footer">
        <span class="modal-share-label" id="share-label">Share</span>
        <button class="share-btn" id="btn-copy" title="Copy link">
          <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
        </button>
        <span class="copy-tooltip" id="copy-tooltip">Copied!</span>
        <button class="share-btn" id="btn-twitter" title="Share on X / Twitter">
          <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </button>
        <button class="share-btn" id="btn-linkedin" title="Share on LinkedIn">
          <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        </button>
        <button class="share-btn" id="btn-facebook" title="Share on Facebook">
          <svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        </button>
      </div>

    </div>
  </div>

  <script>
  (function(){
    'use strict';

    var LOGO     = 'https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true';
    var BASE_URL = 'https://found-project.org/news/';

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       SVG ICONS (one per category — used in no-photo banners)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    var ICONS = {
      award:   '<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
      media:   '<svg viewBox="0 0 24 24"><path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>',
      field:   '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/></svg>',
      funding: '<svg viewBox="0 0 24 24"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/></svg>',
      coverage:'<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'
    };

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       NEWS CARDS DATA
       ─────────────────────────────────────────────────────
       TO ADD A NEW CARD:
       1. Copy any object below and append it to newsCards[]
       2. Give it a unique "id" (appears in the URL: #your-id)
       3. Fill in: date, image (URL or null), link (optional),
          featured (true = gold top border), category
          (award | media | field | funding | coverage)
       4. Add your text under en, es, nah — each needs:
          badge (short category label), title, body (HTML)
       5. Done — card & modal are auto-generated!
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    var newsCards = [

      /* ── 0: Mariela Award ─────────────────────────────── */
      {
        id: 'mariela-award',
        date: '2025-06-15',
        image: null,
        link: 'https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh',
        featured: true,
        category: 'award',
        en: {
          badge: 'Award',
          title: "FOUND\u2019s pioneer wins the UK FCDO\u2019s Sir Nicholas Browne Policy and Expertise Award",
          body: '<p>We are proud to share that <strong>Mariela Garfias</strong> has been awarded the <strong>Sir Nicholas Browne Policy and Expertise Award</strong>, a UK FCDO award recognising excellence in delivering policy objectives, selected from more than 200 nominations.</p><p>Mariela is FOUND\u2019s FCDO pioneer and one of the people most responsible for the project\u2019s impact.</p><p>Through FOUND, and with the support of incredible partners, we have located <strong>27 people</strong> who were victims of disappearance in Mexico, allowing families to move towards answers and a form of closure. Our work is now being embedded with local and national authorities, and has expanded to collaboration with the <strong>Colombian Search Unit</strong> and the Executive Office of the <strong>UN Secretary-General</strong>.</p><p>In her acceptance speech, Mariela shared words that capture the spirit of FOUND: \u201cFrom my decomposed body, flowers shall grow, and I am in them. That is eternity.\u201d \u2014 Edvard Munch.</p><p>When searching for clandestine graves using technologies, nature often bears witness \u2014 through subtle changes in soil and vegetation. Memory persists. Our responsibility is to find it.</p><p>Mariela thanked those who carry this work with us: the British Embassy in Mexico City, our mentor <strong>Martin Johnston</strong>, the Frontier Tech Hub team, and above all the searching mothers, whose knowledge and strength remain our compass.</p><p><a href="https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh" target="_blank" rel="noopener noreferrer">Read the full post on LinkedIn \u2197</a></p>'
        },
        es: {
          badge: 'Reconocimiento',
          title: 'La pionera de FOUND recibe el Premio Sir Nicholas Browne de Pol\u00edtica y Pericia del FCDO brit\u00e1nico',
          body: '<p>Nos enorgullece compartir que <strong>Mariela Garfias</strong> ha recibido el <strong>Premio Sir Nicholas Browne de Pol\u00edtica y Pericia</strong>, un reconocimiento del FCDO brit\u00e1nico a la excelencia en la implementaci\u00f3n de objetivos de pol\u00edtica, seleccionado entre m\u00e1s de 200 nominaciones.</p><p>Mariela es la pionera de FOUND dentro del FCDO y una de las personas m\u00e1s responsables del impacto del proyecto.</p><p>A trav\u00e9s de FOUND, y con el apoyo de aliadas y aliados extraordinarios, hemos localizado a <strong>27 personas</strong> v\u00edctimas de desaparici\u00f3n en M\u00e9xico, permitiendo que sus familias avancen hacia respuestas y alguna forma de cierre. Nuestro trabajo se est\u00e1 incorporando a autoridades locales y nacionales, y se ha ampliado a una colaboraci\u00f3n con la <strong>Unidad de B\u00fasqueda de Personas dadas por Desaparecidas de Colombia</strong> y con la Oficina Ejecutiva del <strong>Secretario General de la ONU</strong>.</p><p>En su discurso de aceptaci\u00f3n, Mariela comparti\u00f3 unas palabras que capturan el esp\u00edritu de FOUND: \u201cDe mi cuerpo descompuesto crecer\u00e1n flores, y yo estoy en ellas. Eso es la eternidad\u201d. \u2014 Edvard Munch.</p><p>Al buscar fosas clandestinas con tecnolog\u00edas, la naturaleza suele dar testimonio \u2014 a trav\u00e9s de cambios sutiles en el suelo y la vegetaci\u00f3n. La memoria persiste. Nuestra responsabilidad es encontrarla.</p><p>Mariela agradeci\u00f3 a quienes sostienen este trabajo con nosotras y nosotros: la Embajada Brit\u00e1nica en Ciudad de M\u00e9xico, nuestro mentor <strong>Martin Johnston</strong>, el equipo de Frontier Tech Hub y, sobre todo, las madres buscadoras, cuyo conocimiento y fuerza siguen siendo nuestra br\u00fajula.</p><p><a href="https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh" target="_blank" rel="noopener noreferrer">Leer la publicaci\u00f3n completa en LinkedIn \u2197</a></p>'
        },
        nah: {
          badge: 'Tlatlepanitaliztli',
          title: 'In pionera de FOUND kiseli in Premio Sir Nicholas Browne de Pol\u00edtica huan Pericia (FCDO)',
          body: '<p>Tiquinechpoua ika pakilistli ke <strong>Mariela Garfias</strong> okiseli in <strong>Premio Sir Nicholas Browne de Pol\u00edtica y Pericia</strong>, tlatlepanitaliztli de in FCDO brit\u00e1nico tlen kixnextia kualli tequitl ipan pol\u00edticas, tlaxtlahuilli tlen m\u00e1s de 200 propuestah.</p><p>Mariela yeto in pionera de FOUND dentro de in FCDO huan se de in tlacameh tlen okitmaka hueyi tlakameh inin proyecto.</p><p>Ika FOUND, huan ika tlatlapalehuiliztli de miek toknihuan, yotiknextijkeh kan okatkah <strong>27 tl\u0101cameh</strong> tlen polihuitkeh ipan M\u0113xihco, tlen kimpalehuiah in familias kiseliskeh tlanemilistli huan se tipo de cierre.</p><p>Ipan in tlajtohketl de kiselis in premio, Mariela okijtoua tlahtolli tlen kixkopina in esp\u00edritu de FOUND: \u201cDe mi cuerpo descompuesto crecer\u00e1n flores, y yo estoy en ellas. Eso es la eternidad\u201d. \u2014 Edvard Munch.</p><p>Ijkuak tiktlatemohuah fosas clandestinas ika tecnolog\u00edas, in tlalli huan xihuitl miek wel kitenextiah \u2014 ika tlapeyaliztli tlen tzintla o ipan xihuitl. In memoria amo polihui. Totekipano in tikajsikilis.</p><p>Mariela okimotlajkamat in tlen kualkanin kinyeknekiltiah nin tequitl: Embajada Brit\u00e1nica ipan Ciudad de M\u00e9xico, in tomentor <strong>Martin Johnston</strong>, in equipo de Frontier Tech Hub, huan, achtoyan, in nananmeh buscadoras.</p><p><a href="https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh" target="_blank" rel="noopener noreferrer">Xikmotlajkolti in tlatlatol ipan LinkedIn \u2197</a></p>'
        }
      },

      /* ── 1: UBPD Field Visit ───────────────────────────── */
      {
        id: 'ubpd-visit',
        date: '2025-11-20',
        image: null,
        link: null,
        featured: false,
        category: 'field',
        en: {
          badge: 'Field visit',
          title: "Second visit of Colombia\u2019s Search Unit for Missing Persons (UBPD) to FOUND\u2019s experimental sites in Jalisco",
          body: '<p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p><p>We welcomed <strong>H\u00e9ctor Javier G\u00f3mez</strong>, geophysicist from Colombia\u2019s <em>Unidad de B\u00fasqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND\u2019s experimental sites in Jalisco.</p><p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND\u2019s experimental sites \u2014 marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p><p>It follows the October 2025 visit by <strong>Dr Juli\u00e1n Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p><p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND\u2019s detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD\u2019s team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND\u2019s partner states in Mexico.</p>'
        },
        es: {
          badge: 'Visita de campo',
          title: 'Segunda visita de la Unidad de B\u00fasqueda de Personas dadas por Desaparecidas (UBPD) de Colombia a los sitios experimentales de FOUND en Jalisco',
          body: '<p>Agradecemos profundamente a <strong>CVM Cyber</strong> y a <strong>Ciaran Martin</strong> por su apoyo para hacer posible esta visita.</p><p>Recibimos a <strong>H\u00e9ctor Javier G\u00f3mez</strong>, geof\u00edsico de la <em>Unidad de B\u00fasqueda de Personas dadas por Desaparecidas (UBPD)</em> de Colombia, para un despliegue conjunto en los sitios experimentales de FOUND en Jalisco.</p><p>La visita se centr\u00f3 en la obtenci\u00f3n y el procesamiento de im\u00e1genes hiperespectrales mediante dron en los cinco sitios experimentales de FOUND \u2014 apenas la segunda vez que esta tecnolog\u00eda se utiliza en M\u00e9xico con fines humanitarios.</p><p>Se trata de la continuaci\u00f3n de la visita de octubre de 2025 de <strong>el Dr. Juli\u00e1n Arias</strong>, Director de Prospecci\u00f3n, Recuperaci\u00f3n e Identificaci\u00f3n de la UBPD, que marc\u00f3 el inicio formal de nuestra colaboraci\u00f3n en metodolog\u00edas de b\u00fasqueda e identificaci\u00f3n.</p><p>Durante esta segunda visita, la UBPD comparti\u00f3 recomendaciones t\u00e9cnicas clave para reforzar las estrategias de FOUND para detectar fosas clandestinas. La colaboraci\u00f3n continuar\u00e1 en enero de 2026, cuando el equipo de FOUND visitar\u00e1 a la UBPD en Colombia para intercambiar experiencias e integrar sus metodolog\u00edas en los estados aliados de FOUND en M\u00e9xico.</p>'
        },
        nah: {
          badge: 'Tlayekoliztli ipan tlalli',
          title: 'Ome visita de in Unidad de B\u00fasqueda de Colombia (UBPD) kan sitios experimentales de FOUND ipan Jalisco',
          body: '<p>Timitztlajkamatih miek ika <strong>CVM Cyber</strong> huan <strong>Ciaran Martin</strong> por ininpalehuiliztli para nikchihuase nin visita.</p><p>Otikweltaskeh <strong>H\u00e9ctor Javier G\u00f3mez</strong>, geof\u00edsico de in <em>Unidad de B\u00fasqueda de Personas dadas por Desaparecidas (UBPD)</em> de Colombia, para se tlatskayotl tlayekoliztli ipan sitios experimentales de FOUND ipan Jalisco.</p><p>In visita omochi para tiknotsaskeh huan tiktlaxtlawaskeh im\u00e1genes hiperespectrales ika dron ipan makuil sitios experimentales de FOUND \u2014 san ome welta okitekuitilijkeh nin tecnolog\u00eda ipan M\u0113xihco ika prop\u00f3sito humanitario.</p><p>Nin tlayekoliztli hualpehua desde in visita de octubre 2025 de <strong>Dr. Juli\u00e1n Arias</strong>, Director de Prospecci\u00f3n, Recuperaci\u00f3n e Identificaci\u00f3n de la UBPD, tlen okitlapolwi oficialmente in sekolaboraci\u00f3n ipan metodolog\u00edas de b\u00fasqueda e identificaci\u00f3n.</p><p>Ipan nin ompa visita, UBPD okimakak tlanawatilistli teknikah para okachi tikchikawaseh estrategias de FOUND para tlamiktiloyan tlatemohuiliztli. In sekolaboraci\u00f3n yas okachi wejkapa ipan enero 2026.</p>'
        }
      },

      /* ── 2: The Guardian ──────────────────────────────── */
      {
        id: 'guardian-article',
        date: '2025-11-19',
        image: 'https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true',
        link: 'https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims',
        featured: false,
        category: 'media',
        en: {
          badge: 'Media',
          title: 'FOUND in The Guardian',
          body: '<img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND in The Guardian"><p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist\u2019s in-person visit to our experimental sites in Jalisco, Mexico.</p><p>We are deeply grateful for the care, depth, and commitment brought to this story after months spent listening to families, researchers, and officials.</p><p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener noreferrer">Read the article in The Guardian \u2197</a></p>'
        },
        es: {
          badge: 'Medios',
          title: 'FOUND en The Guardian',
          body: '<img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND en The Guardian"><p>Este reportaje es el resultado de m\u00e1s de seis meses de correos electr\u00f3nicos, mensajes de WhatsApp y la visita en terreno de la periodista a nuestros sitios experimentales en Jalisco, M\u00e9xico.</p><p>Agradecemos profundamente el cuidado, la profundidad y el compromiso con el que se trabaj\u00f3 esta historia, tras meses escuchando a familias, personas investigadoras y autoridades.</p><p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener noreferrer">Leer el reportaje en The Guardian \u2197</a></p>'
        },
        nah: {
          badge: 'Medios',
          title: 'FOUND ipan The Guardian',
          body: '<img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND ipan The Guardian"><p>Nin reportaje omochi ika m\u00e1s de chikuasen metztli de correos, mensajes de WhatsApp huan visita de in periodista kan sitios experimentales de Jalisco, M\u0113xihco.</p><p>Titlajkamatih miek por in cuidado, hueyikan tlamachilistli huan compromiso tlen okitemitijkeh nin historia.</p><p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener noreferrer">Xikmotlajkolti in reportaje ipan The Guardian \u2197</a></p>'
        }
      },

      /* ── 3: Frontier Tech Funding ─────────────────────── */
      {
        id: 'frontier-tech-funding',
        date: '2025-09-01',
        image: null,
        link: null,
        featured: false,
        category: 'funding',
        en: {
          badge: 'Funding',
          title: "FOUND receives new support from the UK\u2019s FCDO through the Frontier Tech Hub",
          body: '<p>In the pitch, our team showcased FOUND\u2019s impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.</p><p><strong>\uD83C\uDF31 Driven by families and research communities</strong><br>FOUND is guided and motivated by mothers\u2019 search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potos\u00ed.</p><p><strong>We are now working directly with:</strong></p><ul><li>Executive Office of the UN Secretary-General</li><li>UK\u2019s Foreign, Commonwealth &amp; Development Office (FCDO)</li><li>Local Search Commissions and Attorney\u2019s Offices of Jalisco, Zacatecas, San Luis Potos\u00ed, and Chihuahua (Mexico)</li><li>Colombian Search Unit</li><li>Mexico\u2019s National Search Commission</li><li>Mexican Science and Technology Secretariat</li><li>British Embassy in Mexico City</li><li>British Association for Forensic Anthropology</li></ul><p><strong>Technology for memory, dignity, and closure</strong><br>We will continue developing \u2014 and embedding in official protocols \u2014 new ways to locate missing persons using advanced tools such as machine-learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.</p><p><em>FOUND: Interpreting Nature to Locate Those We Are Missing.</em></p>'
        },
        es: {
          badge: 'Financiaci\u00f3n',
          title: 'FOUND recibe nuevo apoyo del FCDO del Reino Unido a trav\u00e9s de Frontier Tech Hub',
          body: '<p>En la presentaci\u00f3n, nuestro equipo mostr\u00f3 el impacto alcanzado por FOUND hasta la fecha, y recibimos una financiaci\u00f3n que nos permitir\u00e1 escalar nuestra misi\u00f3n: impulsar cambios sist\u00e9micos en la forma de buscar a las personas desaparecidas en M\u00e9xico, Colombia y m\u00e1s all\u00e1.</p><p><strong>Impulsado por familias y comunidades de investigaci\u00f3n</strong><br>FOUND est\u00e1 guiado y motivado por colectivos de madres buscadoras y por personas investigadoras de CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge y las Universidades Aut\u00f3nomas de Zacatecas y San Luis Potos\u00ed.</p><p><strong>Actualmente trabajamos directamente con:</strong></p><ul><li>Oficina Ejecutiva del Secretario General de la ONU</li><li>Foreign, Commonwealth &amp; Development Office (FCDO) del Reino Unido</li><li>Comisiones y Fiscal\u00edas de B\u00fasqueda de Jalisco, Zacatecas, San Luis Potos\u00ed y Chihuahua (M\u00e9xico)</li><li>Unidad de B\u00fasqueda de Personas dadas por Desaparecidas de Colombia</li><li>Comisi\u00f3n Nacional de B\u00fasqueda de Personas de M\u00e9xico</li><li>Secretar\u00eda de Ciencia y Tecnolog\u00eda de M\u00e9xico</li><li>Embajada Brit\u00e1nica en M\u00e9xico</li><li>British Association for Forensic Anthropology</li></ul><p><strong>Tecnolog\u00eda para la memoria, la dignidad y el cierre</strong><br>Continuaremos desarrollando \u2014 y ayudando a incorporar en los protocolos oficiales \u2014 nuevas formas de localizar a personas desaparecidas.</p><p><em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em></p>'
        },
        nah: {
          badge: 'Financiamiento',
          title: 'FOUND kiselia yankuik tlapalehuiliztli de in FCDO brit\u00e1nico ika Frontier Tech Hub',
          body: '<p>Ipan in presentaci\u00f3n, inin equipo okixnexti in tlakameh tlen FOUND okichi, huan otikselijkeh se financiamiento tlen techpalehuis para tikueskaltis in misi\u00f3n: xikpatla se modo sist\u00e9mico de kenik tiktlatemohuah personas desaparecidas ipan M\u0113xihco, Colombia huan oksekan.</p><p><strong>Tlatekitilistli tlen petlani desde familias huan comunidades de investigaci\u00f3n</strong><br>FOUND kinyeknemilia nananmeh buscadoras huan investigadores de CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge huan Universidades Aut\u00f3nomas de Zacatecas huan San Luis Potos\u00ed.</p><p><strong>Axkan titekitih san sejco ika:</strong></p><ul><li>Oficina Ejecutiva del Secretario General de la ONU</li><li>Foreign, Commonwealth &amp; Development Office (FCDO) de Reino Unido</li><li>Comisiones de B\u00fasqueda huan Fiscal\u00edas de Jalisco, Zacatecas, San Luis Potos\u00ed huan Chihuahua</li><li>Unidad de B\u00fasqueda de Personas dadas por Desaparecidas de Colombia</li><li>Comisi\u00f3n Nacional de B\u00fasqueda de Personas de M\u00e9xico</li><li>Secretar\u00eda de Ciencia y Tecnolog\u00eda de M\u00e9xico</li><li>Embajada Brit\u00e1nica ipan M\u00e9xico</li><li>British Association for Forensic Anthropology</li></ul><p><em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em></p>'
        }
      },

      /* ── 4: International Media Coverage ─────────────── */
      {
        id: 'international-media',
        date: '2025-07-29',
        image: null,
        link: null,
        featured: false,
        category: 'coverage',
        en: {
          badge: 'Coverage',
          title: 'FOUND featured by Associated Press, The Independent, LA Times, VICE, and NBC',
          body: '<ul><li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li></ul>'
        },
        es: {
          badge: 'Cobertura',
          title: 'FOUND en Associated Press, The Independent, LA Times, VICE y NBC',
          body: '<ul><li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li></ul>'
        },
        nah: {
          badge: 'Tlayekoliztli ipan medios',
          title: 'FOUND ipan Associated Press, The Independent, LA Times, VICE huan NBC',
          body: '<ul><li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li></ul>'
        }
      }

      /* ─────────────────────────────────────────────────────
         TEMPLATE — copy & paste below to add a new card:

      ,{
        id: 'my-new-story',       // unique slug → URL hash
        date: '2026-04-01',       // YYYY-MM-DD
        image: null,              // image URL string, or null
        link: null,               // optional external URL, or null
        featured: false,          // true = gold top border
        category: 'media',        // award|media|field|funding|coverage
        en: {
          badge: 'Category',
          title: 'Headline in English',
          body:  '<p>Full HTML content for the expanded modal.</p>'
        },
        es: {
          badge: 'Categoría',
          title: 'Titular en español',
          body:  '<p>Contenido en español.</p>'
        },
        nah: {
          badge: 'Badge en náhuatl',
          title: 'Titular en náhuatl',
          body:  '<p>Contenido en náhuatl.</p>'
        }
      }

         ───────────────────────────────────────────────────── */
    ];

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       HEADER TRANSLATIONS
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    var UI = {
      en: {
        pill: 'NEWS \u00B7 IMPACT \u00B7 MEDIA',
        title: 'FOUND \u2014 News &amp; Updates',
        subtitle: 'Latest developments on our work across Mexico, Colombia, and beyond.',
        readMore: 'Read more',
        share: 'Share',
        statLocated: 'Located',
        statStates: 'Partner states',
        statCountries: 'Countries'
      },
      es: {
        pill: 'NOTICIAS \u00B7 IMPACTO \u00B7 MEDIOS',
        title: 'FOUND \u2014 Noticias y Actualizaciones',
        subtitle: 'Las novedades m\u00e1s recientes sobre nuestro trabajo en M\u00e9xico, Colombia y m\u00e1s all\u00e1.',
        readMore: 'Leer m\u00e1s',
        share: 'Compartir',
        statLocated: 'Localizadas',
        statStates: 'Estados aliados',
        statCountries: 'Pa\u00edses'
      },
      nah: {
        pill: 'TLATLAHCUILOLLI \u00B7 TLAKAMEH \u00B7 MEDIOS',
        title: 'FOUND \u2014 Tlen mochihua huan tlen pano',
        subtitle: 'Nuevas tlamantli tlen totlatequi ipan M\u0113xihco, Colombia huan oksekan.',
        readMore: 'Xikpoua okachi',
        share: 'Xiktemaka',
        statLocated: 'Telnextijkeh',
        statStates: 'Estados',
        statCountries: 'Tlaltipaktli'
      }
    };

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       STATE
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    var lang = 'en';
    var activeCardId = null;

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       HELPERS
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    function fmtDate(d, l) {
      try {
        var date = new Date(d + 'T00:00:00');
        return date.toLocaleDateString(l === 'en' ? 'en-US' : 'es-MX', { year:'numeric', month:'long', day:'numeric' });
      } catch(e) { return d; }
    }

    function cardById(id) {
      for (var i = 0; i < newsCards.length; i++) {
        if (newsCards[i].id === id) return newsCards[i];
      }
      return null;
    }

    function setMeta(id, val) {
      var el = document.getElementById(id);
      if (el) el.setAttribute('content', val);
    }

    function badgeClass(cat) {
      var map = { award:'badge-award', media:'badge-media', field:'badge-field', funding:'badge-funding', coverage:'badge-coverage' };
      return map[cat] || 'badge-field';
    }
    function bannerClass(cat) {
      var map = { award:'banner-award', media:'banner-media', field:'banner-field', funding:'banner-funding', coverage:'banner-coverage' };
      return map[cat] || 'banner-field';
    }

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       RENDER GRID
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
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

        /* Banner */
        var bannerHtml;
        if (card.image) {
          bannerHtml =
            '<div class="card-banner">' +
              '<img src="' + card.image + '" alt="" loading="lazy">' +
            '</div>';
        } else {
          bannerHtml =
            '<div class="card-banner no-photo ' + bannerClass(card.category) + '">' +
              '<div class="card-banner-watermark">' +
                '<img class="card-banner-logo" src="' + LOGO + '" alt="">' +
                '<span class="card-banner-label">FOUND</span>' +
              '</div>' +
            '</div>';
        }

        /* Body */
        article.innerHTML =
          bannerHtml +
          '<div class="card-body">' +
            '<div class="card-meta">' +
              '<span class="card-badge ' + badgeClass(card.category) + '">' + t.badge + '</span>' +
              (card.date ? '<span class="card-date">' + fmtDate(card.date, lang) + '</span>' : '') +
            '</div>' +
            '<span class="card-title">' + t.title + '</span>' +
            '<div class="card-cta">' +
              '<span class="card-read-more">' + ui.readMore + '</span>' +
              '<span class="card-arrow">' +
                '<svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>' +
              '</span>' +
            '</div>' +
          '</div>';

        article.addEventListener('click', function() { openModal(card.id); });
        article.addEventListener('keydown', function(e) {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(card.id); }
        });

        grid.appendChild(article);
      });
    }

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       MODAL
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    var overlay = document.getElementById('modal-overlay');
    var panel   = document.getElementById('modal-panel');

    function openModal(id) {
      var card = cardById(id);
      if (!card) return;
      activeCardId = id;
      var t  = card[lang] || card.en;
      var ui = UI[lang] || UI.en;

      /* Hero */
      var hero = document.getElementById('modal-hero');
      if (card.image) {
        hero.innerHTML =
          '<img class="modal-hero-img" src="' + card.image + '" alt="' + t.title.replace(/<[^>]*>/g,'') + '">' +
          '<img class="modal-img-wm" src="' + LOGO + '" alt="">';
      } else {
        hero.innerHTML =
          '<div class="modal-hero-gradient ' + bannerClass(card.category) + '">' +
            '<div class="modal-hero-wm">' +
              '<img class="modal-hero-logo" src="' + LOGO + '" alt="">' +
              '<span class="modal-hero-news-label">FOUND NEWS</span>' +
            '</div>' +
          '</div>';
      }

      /* Badge class */
      var badge = document.getElementById('modal-badge');
      badge.className = 'modal-badge ' + badgeClass(card.category);
      badge.innerHTML = t.badge;

      document.getElementById('modal-date').textContent = card.date ? fmtDate(card.date, lang) : '';
      document.getElementById('modal-title-el').innerHTML = t.title;
      document.getElementById('modal-body').innerHTML = t.body;
      document.getElementById('share-label').textContent = ui.share;

      /* OG meta */
      var plainTitle = t.title.replace(/<[^>]*>/g,'');
      setMeta('og-title',       plainTitle);
      setMeta('og-description', plainTitle);
      setMeta('og-image',       card.image || LOGO);
      setMeta('og-url',         BASE_URL + 'cards/' + id);
      setMeta('tw-title',       plainTitle);
      setMeta('tw-description', plainTitle);
      setMeta('tw-image',       card.image || LOGO);

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
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && overlay.classList.contains('active')) closeModal();
    });

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       SHARE BUTTONS
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    document.getElementById('btn-copy').addEventListener('click', function() {
      var url = BASE_URL + '#' + (activeCardId || '');
      var btn = document.getElementById('btn-copy');
      var tip = document.getElementById('copy-tooltip');
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(function() {
          btn.classList.add('copied');
          tip.classList.add('show');
          setTimeout(function() { btn.classList.remove('copied'); tip.classList.remove('show'); }, 2200);
        });
      } else {
        /* Fallback */
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

    document.getElementById('btn-twitter').addEventListener('click', function() {
      var card = cardById(activeCardId);
      if (!card) return;
      var t = card[lang] || card.en;
      var title = t.title.replace(/<[^>]*>/g,'');
      var url   = BASE_URL + '#' + activeCardId;
      window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(title) + '&url=' + encodeURIComponent(url), '_blank');
    });

    document.getElementById('btn-linkedin').addEventListener('click', function() {
      window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(BASE_URL + '#' + (activeCardId||'')), '_blank');
    });

    document.getElementById('btn-facebook').addEventListener('click', function() {
      window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(BASE_URL + '#' + (activeCardId||'')), '_blank');
    });

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       LANGUAGE
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    function setLang(l) {
      lang = l;
      var ui = UI[l] || UI.en;

      document.getElementById('news-pill').textContent    = ui.pill;
      document.getElementById('news-title').innerHTML     = ui.title;
      document.getElementById('news-subtitle').innerHTML  = ui.subtitle;
      document.getElementById('stat-label-located').textContent  = ui.statLocated;
      document.getElementById('stat-label-states').textContent   = ui.statStates;
      document.getElementById('stat-label-countries').textContent = ui.statCountries;

      document.documentElement.lang = l === 'es' ? 'es' : (l === 'nah' ? 'nah' : 'en');

      document.querySelectorAll('.lang-btn').forEach(function(btn) {
        btn.classList.toggle('active', btn.dataset.lang === l);
      });

      renderGrid();

      if (activeCardId && overlay.classList.contains('active')) openModal(activeCardId);

      try { localStorage.setItem('found-lang-news', l); } catch(e) {}
    }

    /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INIT
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
    document.addEventListener('DOMContentLoaded', function() {
      var saved = null;
      try { saved = localStorage.getItem('found-lang-news'); } catch(e) {}
      var init = (saved === 'es' || saved === 'en' || saved === 'nah') ? saved : 'en';

      document.querySelectorAll('.lang-btn').forEach(function(btn) {
        btn.addEventListener('click', function() { setLang(btn.dataset.lang); });
      });

      setLang(init);

      var hash = window.location.hash.replace('#', '');
      if (hash && cardById(hash)) {
        setTimeout(function() { openModal(hash); }, 280);
      }
    });

    window.addEventListener('hashchange', function() {
      var hash = window.location.hash.replace('#', '');
      if (hash && cardById(hash)) openModal(hash);
      else closeModal();
    });

  })();
  </script>
</body>
</html>---
