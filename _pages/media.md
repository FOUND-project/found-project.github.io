---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200">
  <title>FOUND — Media & Talks</title>
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
    .media-shell {
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
    .media-header {
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
    .media-header::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 5px;
      background: linear-gradient(180deg, var(--gold) 0%, rgba(212,175,55,.3) 100%);
      border-radius: var(--radius-xl) 0 0 var(--radius-xl);
    }

    /* Radial glow */
    .media-header::after {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 600px 300px at -5% 0%, rgba(212,175,55,.13) 0%, transparent 60%),
        radial-gradient(ellipse 500px 300px at 110% 100%, rgba(198,226,216,.5) 0%, transparent 60%);
      pointer-events: none;
    }

    .media-header-logo {
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      padding: 2.2rem 2rem 2.2rem 2.8rem;
      position: relative;
      z-index: 1;
    }
    .media-header-logo img {
      width: 88px;
      height: 88px;
      border-radius: 20px;
      object-fit: cover;
      box-shadow: 0 12px 32px rgba(15,23,42,.22);
      border: 3px solid rgba(255,255,255,.95);
      background: #fff;
    }

    /* Subtle divider */
    .media-header-divider {
      width: 1px;
      background: linear-gradient(180deg, transparent, rgba(15,23,42,.08), transparent);
      margin: 2rem 0;
      flex-shrink: 0;
    }

    .media-header-body {
      flex: 1;
      padding: 2.2rem 2.8rem 2.2rem 2.4rem;
      position: relative;
      z-index: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .media-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: .5rem;
      margin-bottom: .65rem;
    }
    .media-eyebrow-dot {
      width: 7px; height: 7px;
      border-radius: 50%;
      background: var(--gold);
      box-shadow: 0 0 0 3px rgba(212,175,55,.2);
    }
    .media-eyebrow-text {
      font-size: .7rem;
      font-weight: 800;
      letter-spacing: .2em;
      text-transform: uppercase;
      color: var(--green-700);
    }

    #media-title {
      font-size: clamp(1.8rem, 3vw, 2.5rem);
      font-weight: 900;
      color: var(--green-900);
      letter-spacing: -.035em;
      line-height: 1.15;
      margin-bottom: .5rem;
    }
    #media-intro {
      font-size: clamp(.95rem, 1.3vw, 1.1rem);
      color: var(--text-medium);
      line-height: 1.75;
      max-width: 680px;
    }

    /* ═══════════════════════════════════════════════════════
       MEDIA GRID
       ═══════════════════════════════════════════════════════ */
    .media-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: clamp(1.2rem, 2vw, 1.8rem);
      margin-bottom: 3rem;
      --stagger: 60ms;
    }

    /* ── Individual card ── */
    .media-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      border: 1px solid rgba(15,23,42,.055);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      position: relative;
      text-decoration: none;
      color: inherit;
      transition:
        transform   .28s var(--ease),
        box-shadow  .28s var(--ease),
        border-color .28s var(--ease);

      /* Entrance animation */
      animation: cardIn .55s var(--ease) both;
    }
    .media-card:nth-child(1) { animation-delay: calc(1 * var(--stagger)); }
    .media-card:nth-child(2) { animation-delay: calc(2 * var(--stagger)); }
    .media-card:nth-child(3) { animation-delay: calc(3 * var(--stagger)); }
    .media-card:nth-child(4) { animation-delay: calc(4 * var(--stagger)); }
    .media-card:nth-child(5) { animation-delay: calc(5 * var(--stagger)); }
    .media-card:nth-child(6) { animation-delay: calc(6 * var(--stagger)); }
    .media-card:nth-child(7) { animation-delay: calc(7 * var(--stagger)); }
    .media-card:nth-child(8) { animation-delay: calc(8 * var(--stagger)); }

    @keyframes cardIn {
      from { opacity:0; transform:translateY(18px); }
      to   { opacity:1; transform:translateY(0); }
    }

    .media-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-lg);
      border-color: rgba(45,95,77,.22);
    }

    .media-card:hover .media-image {
      transform: scale(1.05);
    }

    /* ── Card image ── */
    .media-image {
      width: 100%;
      height: 160px;
      object-fit: cover;
      background: linear-gradient(135deg, rgba(45,95,77,.08) 0%, rgba(198,226,216,.15) 100%);
      transition: transform .3s var(--ease);
      display: block;
    }

    .media-image.loading {
      background: linear-gradient(90deg, rgba(45,95,77,.05) 0%, rgba(45,95,77,.1) 50%, rgba(45,95,77,.05) 100%);
      background-size: 200% 100%;
      animation: shimmer 1.5s infinite;
    }

    @keyframes shimmer {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    .media-image-placeholder {
      width: 100%;
      height: 160px;
      background: linear-gradient(135deg, rgba(45,95,77,.08) 0%, rgba(198,226,216,.15) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-light);
      font-size: .8rem;
      text-align: center;
      padding: 1rem;
    }

    /* ── Card inner ── */
    .media-card-inner {
      padding: 1.4rem 1.5rem;
      display: flex;
      flex-direction: column;
      flex: 1;
      gap: .4rem;
    }

    .media-outlet {
      font-size: .68rem;
      text-transform: uppercase;
      letter-spacing: .14em;
      font-weight: 800;
      color: var(--green-800);
      display: inline-flex;
      align-items: center;
      gap: .35rem;
      width: fit-content;
    }
    .media-outlet::before {
      content: '';
      width: 5px; height: 5px;
      border-radius: 50%;
      background: var(--green-700);
      opacity: .8;
    }

    .media-title {
      font-size: 1.06rem;
      font-weight: 800;
      color: var(--green-900);
      line-height: 1.4;
      letter-spacing: -.015em;
      flex: 1;
    }

    .media-tag {
      font-size: .72rem;
      text-transform: uppercase;
      letter-spacing: .1em;
      font-weight: 750;
      padding: .2rem .65rem;
      border-radius: var(--radius-pill);
      display: inline-flex;
      width: fit-content;
      background: rgba(45,95,77,.07);
      color: var(--green-800);
      border: 1px solid rgba(45,95,77,.14);
      margin-top: .6rem;
    }

    /* ═══════════════════════════════════════════════════════
       TALKS SECTION
       ═══════════════════════════════════════════════════════ */
    .talks-section {
      margin-top: 2rem;
      padding: 2.2rem 2.6rem;
      border-radius: var(--radius-xl);
      background:
        radial-gradient(ellipse 700px 400px at 0% -10%, rgba(212,175,55,.08) 0%, transparent 60%),
        linear-gradient(135deg, #ffffff 0%, #f6fbf8 100%);
      box-shadow: var(--shadow-md);
      border: 1px solid rgba(15,23,42,.055);
      position: relative;
      overflow: hidden;
    }

    .talks-section::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 4px;
      background: linear-gradient(180deg, var(--gold) 0%, rgba(212,175,55,.2) 100%);
    }

    #talks-title {
      font-size: clamp(1.5rem, 2.2vw, 2rem);
      font-weight: 900;
      color: var(--green-900);
      letter-spacing: -.03em;
      margin-bottom: 1.8rem;
      padding-left: 1rem;
    }

    .talk-card {
      background: var(--white);
      padding: 1.3rem 1.6rem;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-xs);
      border: 1px solid rgba(15,23,42,.055);
      position: relative;
      overflow: hidden;
      transition:
        transform .25s var(--ease),
        box-shadow .25s var(--ease),
        border-color .25s var(--ease);
      margin-bottom: 1rem;
      margin-left: 1rem;
      display: flex;
      flex-direction: column;
      gap: .5rem;
    }

    .talk-card::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 3px;
      background: var(--green-700);
      transform: scaleY(0);
      transform-origin: bottom;
      transition: transform .3s var(--ease-spring);
    }

    .talk-card:hover {
      transform: translateX(4px);
      box-shadow: var(--shadow-md);
      border-color: rgba(45,95,77,.18);
    }

    .talk-card:hover::before {
      transform: scaleY(1);
      transform-origin: top;
    }

    .talk-title {
      font-size: .75rem;
      font-weight: 750;
      text-transform: uppercase;
      letter-spacing: .1em;
      color: var(--text-light);
    }

    .talk-link {
      font-size: 1.04rem;
      text-decoration: none;
      color: var(--text-dark);
      font-weight: 700;
      line-height: 1.45;
      letter-spacing: -.01em;
      transition: color .2s var(--ease);
    }
    .talk-link:hover {
      color: var(--green-800);
    }

    /* ═══════════════════════════════════════════════════════
       RESPONSIVE
       ═══════════════════════════════════════════════════════ */
    @media (max-width: 900px) {
      body { padding: 1.4rem 1rem; }
      .media-shell { margin-left: 0; }
      .lang-toggle { position: static; margin-bottom: .75rem; }
      .media-header { flex-direction: column; }
      .media-header-logo { padding: 1.6rem 1.6rem 0; }
      .media-header-divider { display: none; }
      .media-header-body { padding: 1rem 1.6rem 1.8rem; }
      #media-title { font-size: 1.65rem; }
      .media-grid { grid-template-columns: 1fr; }
      .talks-section { padding: 1.8rem 1.6rem; }
      #talks-title { padding-left: 1.5rem; }
    }

    @media (max-width: 480px) {
      .media-header { padding: 1.3rem 1.1rem; }
      .media-card-inner { padding: 1.1rem 1.1rem 1.3rem; }
      #talks-title { font-size: 1.45rem; }
      .talk-card { margin-left: .5rem; }
      .media-image { height: 120px; }
      .media-image-placeholder { height: 120px; }
    }
  </style>
</head>
<body>
  <div class="media-shell">

    <!-- LANGUAGE TOGGLE -->
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
    </div>

    <!-- PAGE HEADER -->
    <header class="media-header">
      <div class="media-header-logo">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/master/images/Found_logo.jpg" alt="FOUND Logo">
      </div>
      <div class="media-header-divider"></div>
      <div class="media-header-body">
        <div class="media-eyebrow">
          <span class="media-eyebrow-dot"></span>
          <span class="media-eyebrow-text" id="media-pill">MEDIA · COVERAGE · TALKS</span>
        </div>
        <h1 id="media-title">Media Coverage</h1>
        <p id="media-intro">Our research and work has been featured in leading international publications.</p>
      </div>
    </header>

    <!-- MEDIA GRID -->
    <section class="media-grid">

       <!-- Museo Cada de la Memoria, Medellín -->
      <a class="media-card" href="https://www.museocasadelamemoria.gov.co/noticias/encontrar-a-las-personas-que-nos-hacen-falta-mision-de-alianza-entre-medellin-reino-unido-y-mexico/" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Museo Medellín</div>
          <h3 class="media-title">Encontrar a las personas que nos hacen falta: misión de alianza entre Medellín, Reino Unido y México</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>
      
      <!-- The Guardian -->
      <a class="media-card" href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">The Guardian</div>
          <h3 class="media-title">How dead pigs are helping in the search for missing victims of Mexico's drug wars</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- BBC Mundo -->
      <a class="media-card" href="https://www.bbc.com/mundo/articles/c4gv9r1120mo" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">BBC Mundo</div>
          <h3 class="media-title">Los cerdos y los insectos que están ayudando a encontrar a los desaparecidos en México</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- Associated Press (EN) -->
      <a class="media-card" href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Associated Press</div>
          <h3 class="media-title">Why are scientists dressing pigs in clothes and burying them in Mexico?</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- Associated Press (ES) -->
      <a class="media-card" href="https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Associated Press</div>
          <h3 class="media-title">Ciencia, tecnología y cerdos. México experimenta nuevas formas de buscar a los desaparecidos</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <!-- The Independent -->
      <a class="media-card" href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">The Independent</div>
          <h3 class="media-title">How pigs could help find missing Mexican drug cartel victims</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- VICE -->
      <a class="media-card" href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">VICE</div>
          <h3 class="media-title">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- Los Angeles Times -->
      <a class="media-card" href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Los Angeles Times</div>
          <h3 class="media-title">Why are scientists dressing pigs in clothes and burying them in Mexico?</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- NBC News -->
      <a class="media-card" href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">NBC News</div>
          <h3 class="media-title">Clothed pigs are buried in Mexico as scientists use them in search of missing</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- Animal Político -->
      <a class="media-card" href="https://www.animalpolitico.com/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Animal Político</div>
          <h3 class="media-title">Con tecnología y drones, investigadores y familias de desaparecidos encuentran fosas clandestinas en Jalisco</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <!-- Science -->
      <a class="media-card" href="https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Science</div>
          <h3 class="media-title">Satellites could reveal the secret burial grounds of Mexico's murder victims</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- WIRED -->
      <a class="media-card" href="https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">WIRED</div>
          <h3 class="media-title">Cómo la tecnología geoespacial expone el horror de las fosas clandestinas en México</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <!-- El País (EN) -->
      <a class="media-card" href="https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">El País</div>
          <h3 class="media-title">Mexico's Izaguirre ranch: high concentrations of ash suggest clandestine crematoriums</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- El País (ES) -->
      <a class="media-card" href="https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">El País</div>
          <h3 class="media-title">Altas concentraciones de ceniza y humo: indicios de crematorios clandestinos en Teuchitlán</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <!-- TV Azteca -->
      <a class="media-card" href="https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">TV Azteca</div>
          <h3 class="media-title">Tecnología contra las desapariciones en México</h3>
          <span class="media-tag" data-key="tv">TV Segment</span>
        </div>
      </a>

      <!-- Animal Político (Opinion) -->
      <a class="media-card" href="https://animalpolitico.com/analisis/invitades/libro-madres-buscadoras-fil" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Animal Político</div>
          <h3 class="media-title">Interpretar la naturaleza para encontrar a quienes nos faltan</h3>
          <span class="media-tag" data-key="opinion">Opinion</span>
        </div>
      </a>

      <!-- Reuters -->
      <a class="media-card" href="https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">Reuters</div>
          <h3 class="media-title">In Mexico, mothers of the missing turn to drones to look for unmarked graves</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <!-- CGTN America -->
      <a class="media-card" href="https://twitter.com/cgtnamerica/status/1751362286118150555" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">CGTN America</div>
          <h3 class="media-title">Jalisco mothers search for hidden graves with drones</h3>
          <span class="media-tag" data-key="tv-social">TV / Social</span>
        </div>
      </a>

      <!-- SinEmbargo -->
      <a class="media-card" href="https://www.sinembargo.mx/18-12-2023/4440515" target="_blank" rel="noopener">
        <div class="media-image-placeholder">Image</div>
        <div class="media-card-inner">
          <div class="media-outlet">SinEmbargo</div>
          <h3 class="media-title">Tecnología para hallarlos</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>
    </section>

    <!-- TALKS SECTION -->
    <section class="talks-section">
      <h2 id="talks-title">Talks</h2>

      <a class="talk-card" href="https://www.ox.ac.uk/event/technological-responses-disappearance" target="_blank" rel="noopener">
        <div class="talk-title">University of Oxford / Oxford Festival of the Arts</div>
        <span class="talk-link">Disappearance of Worlds | Art Exhibition & Dialogues on Disappearance</span>
      </a>

      <a class="talk-card" href="https://bafauk.weebly.com/winter-conference--agm-2024.html" target="_blank" rel="noopener">
        <div class="talk-title">British Association for Forensic Anthropology</div>
        <span class="talk-link">Interpreting nature to locate the disappeared: influencing search practices</span>
      </a>

      <a class="talk-card" href="https://jalisco.quadratin.com.mx/principal/presentan-interpretar-la-naturaleza-para-encontrar-a-quienes-nos-faltan/" target="_blank" rel="noopener">
        <div class="talk-title">Guadalajara International Book Fair</div>
        <span class="talk-link">Presentan Interpretar la naturaleza para encontrar a quienes nos faltan</span>
      </a>

      <a class="talk-card" href="https://www.ox.ac.uk/event/mexicos-missing-how-families-and-technology-are-working-together" target="_blank" rel="noopener">
        <div class="talk-title">University of Oxford</div>
        <span class="talk-link">Mexico's Missing: How families and technology are working together</span>
      </a>
    </section>

  </div><!-- /media-shell -->

  <!-- LANGUAGE SCRIPT -->
  <script>
    (function(){
      const translations = {
        en:{
          'media-pill':'MEDIA · COVERAGE · TALKS',
          'media-title':'Media Coverage',
          'media-intro':'Our research and work has been featured in leading international publications.',
          'talks-title':'Talks'
        },
        es:{
          'media-pill':'MEDIOS · COBERTURA · CHARLAS',
          'media-title':'Cobertura en medios',
          'media-intro':'Nuestras investigaciones y trabajo han aparecido en medios internacionales de referencia.',
          'talks-title':'Charlas'
        },
        nah:{
          'media-pill':'MEDIOS · TLAYEKOLOLLO · TLAHTOLMEH',
          'media-title':'Tlayekoliztli ipan medios',
          'media-intro':'Totlatequi huan totlatlamachtiliztli yopanok ipan medios internacionales.',
          'talks-title':'Tlatlahtolmeh'
        }
      };

      const tagLabels = {
        en:{ article:'Article', tv:'TV Segment', 'tv-social':'TV / Social', opinion:'Opinion' },
        es:{ article:'Artículo', tv:'Segmento TV', 'tv-social':'TV / Redes', opinion:'Opinión' },
        nah:{ article:'Tlatlaquiliztli', tv:'Segmento TV', 'tv-social':'TV / Social', opinion:'Tlaixkomati' }
      };

      function setLanguage(lang){
        const dict = translations[lang] || translations.en;
        Object.keys(dict).forEach(id => {
          const el = document.getElementById(id);
          if(el) el.innerHTML = dict[id];
        });

        const tagMap = tagLabels[lang] || tagLabels.en;
        document.querySelectorAll('.media-tag').forEach(el=>{
          const key = el.dataset.key;
          if(key && tagMap[key]){
            el.textContent = tagMap[key];
          }
        });

        document.documentElement.lang = lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en');

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        try{ localStorage.setItem('found-lang-media', lang); }catch(e){}
      }

      function fetchOpenGraphImage(url){
        return fetch(url)
          .then(r => r.text())
          .then(html => {
            const match = html.match(/<meta\s+property=['"]og:image['"]\s+content=['"]([^'"]+)['"]/i) ||
                          html.match(/<meta\s+content=['"]([^'"]+)['"]\s+property=['"]og:image['"]/i);
            return match ? match[1] : null;
          })
          .catch(() => null);
      }

      function loadCardImage(card){
        const href = card.getAttribute('href');
        const placeholder = card.querySelector('.media-image-placeholder');
        
        if(!placeholder || !href) return;

        placeholder.classList.add('loading');

        fetchOpenGraphImage(href).then(imageUrl => {
          if(imageUrl){
            const img = document.createElement('img');
            img.className = 'media-image';
            img.src = imageUrl;
            img.alt = card.querySelector('.media-title')?.textContent || 'Article image';
            img.onerror = () => {
              placeholder.classList.remove('loading');
            };
            img.onload = () => {
              placeholder.replaceWith(img);
            };
          } else {
            placeholder.classList.remove('loading');
          }
        });
      }

      document.addEventListener('DOMContentLoaded', function(){
        let savedLang = null;
        try{ savedLang = localStorage.getItem('found-lang-media'); }catch(e){}
        const initialLang = (savedLang === 'es' || savedLang === 'en' || savedLang === 'nah') ? savedLang : 'en';
        setLanguage(initialLang);

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
        });

        document.querySelectorAll('.media-card').forEach(card => {
          loadCardImage(card);
        });
      });
    })();
  </script>
</body>
</html>
