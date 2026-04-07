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
      *, *::before, *::after { animation-duration:.01ms!important; transition-duration:.01ms!important; }
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

    .page, #main, .initial-content, .page__inner-wrap, .page__content, .archive {
      max-width: none !important;
      width: 100% !important;
    }

    *:focus-visible {
      outline: 3px solid rgba(74,140,115,.55);
      outline-offset: 3px;
      border-radius: var(--radius-sm);
    }

    .media-shell {
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

    .media-header::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 5px;
      background: linear-gradient(180deg, var(--gold) 0%, rgba(212,175,55,.3) 100%);
      border-radius: var(--radius-xl) 0 0 var(--radius-xl);
    }

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

    .media-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: clamp(1.2rem, 2vw, 1.8rem);
      margin-bottom: 3rem;
      --stagger: 60ms;
    }

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
      transition: transform .28s var(--ease), box-shadow .28s var(--ease), border-color .28s var(--ease);
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
    .media-card:hover .card-img { transform: scale(1.05); }

    /* ── image area ── */
    .card-img-wrap {
      width: 100%;
      height: 160px;
      overflow: hidden;
      background: linear-gradient(135deg, rgba(45,95,77,.07) 0%, rgba(198,226,216,.18) 100%);
      flex-shrink: 0;
      position: relative;
    }

    .card-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform .3s var(--ease);
    }

    /* outlet-initial fallback shown when no image loads */
    .card-img-fallback {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: .4rem;
      pointer-events: none;
    }
    .card-img-fallback-initial {
      width: 48px; height: 48px;
      border-radius: 12px;
      background: rgba(45,95,77,.10);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      font-weight: 900;
      color: var(--green-700);
      letter-spacing: -.02em;
    }
    .card-img-fallback-label {
      font-size: .65rem;
      font-weight: 700;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--text-light);
    }

    /* hide fallback once real image loads */
    .card-img-wrap.has-image .card-img-fallback { display: none; }
    /* shimmer while loading */
    .card-img-wrap.loading {
      background: linear-gradient(90deg, rgba(45,95,77,.05) 0%, rgba(45,95,77,.12) 50%, rgba(45,95,77,.05) 100%);
      background-size: 200% 100%;
      animation: shimmer 1.4s infinite;
    }
    @keyframes shimmer {
      0%   { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

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
      transition: transform .25s var(--ease), box-shadow .25s var(--ease), border-color .25s var(--ease);
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
    .talk-card:hover { transform: translateX(4px); box-shadow: var(--shadow-md); border-color: rgba(45,95,77,.18); }
    .talk-card:hover::before { transform: scaleY(1); transform-origin: top; }

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
    .talk-link:hover { color: var(--green-800); }

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
      .card-img-wrap { height: 120px; }
    }
  </style>
</head>
<body>
  <div class="media-shell">

    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
    </div>

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

    <section class="media-grid">

      <a class="media-card" href="https://www.museocasadelamemoria.gov.co/noticias/encontrar-a-las-personas-que-nos-hacen-falta-mision-de-alianza-entre-medellin-reino-unido-y-mexico/" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.museocasadelamemoria.gov.co/noticias/encontrar-a-las-personas-que-nos-hacen-falta-mision-de-alianza-entre-medellin-reino-unido-y-mexico/">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">MM</div><span class="card-img-fallback-label">Museo Medellín</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Museo Medellín</div>
          <h3 class="media-title">Encontrar a las personas que nos hacen falta: misión de alianza entre Medellín, Reino Unido y México</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">GU</div><span class="card-img-fallback-label">The Guardian</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">The Guardian</div>
          <h3 class="media-title">How dead pigs are helping in the search for missing victims of Mexico's drug wars</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://www.bbc.com/mundo/articles/c4gv9r1120mo" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.bbc.com/mundo/articles/c4gv9r1120mo">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">BB</div><span class="card-img-fallback-label">BBC Mundo</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">BBC Mundo</div>
          <h3 class="media-title">Los cerdos y los insectos que están ayudando a encontrar a los desaparecidos en México</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">AP</div><span class="card-img-fallback-label">Associated Press</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Associated Press</div>
          <h3 class="media-title">Why are scientists dressing pigs in clothes and burying them in Mexico?</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">AP</div><span class="card-img-fallback-label">Associated Press</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Associated Press</div>
          <h3 class="media-title">Ciencia, tecnología y cerdos. México experimenta nuevas formas de buscar a los desaparecidos</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <a class="media-card" href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">IN</div><span class="card-img-fallback-label">The Independent</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">The Independent</div>
          <h3 class="media-title">How pigs could help find missing Mexican drug cartel victims</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">VC</div><span class="card-img-fallback-label">VICE</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">VICE</div>
          <h3 class="media-title">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">LA</div><span class="card-img-fallback-label">Los Angeles Times</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Los Angeles Times</div>
          <h3 class="media-title">Why are scientists dressing pigs in clothes and burying them in Mexico?</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.nbcnews.com/news/amp/rcna221791">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">NB</div><span class="card-img-fallback-label">NBC News</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">NBC News</div>
          <h3 class="media-title">Clothed pigs are buried in Mexico as scientists use them in search of missing</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://www.animalpolitico.com/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.animalpolitico.com/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">AP</div><span class="card-img-fallback-label">Animal Político</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Animal Político</div>
          <h3 class="media-title">Con tecnología y drones, investigadores y familias de desaparecidos encuentran fosas clandestinas en Jalisco</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <a class="media-card" href="https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">SC</div><span class="card-img-fallback-label">Science</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Science</div>
          <h3 class="media-title">Satellites could reveal the secret burial grounds of Mexico's murder victims</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">WI</div><span class="card-img-fallback-label">WIRED</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">WIRED</div>
          <h3 class="media-title">Cómo la tecnología geoespacial expone el horror de las fosas clandestinas en México</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <a class="media-card" href="https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">EP</div><span class="card-img-fallback-label">El País</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">El País</div>
          <h3 class="media-title">Mexico's Izaguirre ranch: high concentrations of ash suggest clandestine crematoriums</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">EP</div><span class="card-img-fallback-label">El País</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">El País</div>
          <h3 class="media-title">Altas concentraciones de ceniza y humo: indicios de crematorios clandestinos en Teuchitlán</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

      <a class="media-card" href="https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">TV</div><span class="card-img-fallback-label">TV Azteca</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">TV Azteca</div>
          <h3 class="media-title">Tecnología contra las desapariciones en México</h3>
          <span class="media-tag" data-key="tv">TV Segment</span>
        </div>
      </a>

      <a class="media-card" href="https://animalpolitico.com/analisis/invitades/libro-madres-buscadoras-fil" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://animalpolitico.com/analisis/invitades/libro-madres-buscadoras-fil">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">AP</div><span class="card-img-fallback-label">Animal Político</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Animal Político</div>
          <h3 class="media-title">Interpretar la naturaleza para encontrar a quienes nos faltan</h3>
          <span class="media-tag" data-key="opinion">Opinion</span>
        </div>
      </a>

      <a class="media-card" href="https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">RE</div><span class="card-img-fallback-label">Reuters</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">Reuters</div>
          <h3 class="media-title">In Mexico, mothers of the missing turn to drones to look for unmarked graves</h3>
          <span class="media-tag" data-key="article">Article</span>
        </div>
      </a>

      <a class="media-card" href="https://twitter.com/cgtnamerica/status/1751362286118150555" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://twitter.com/cgtnamerica/status/1751362286118150555">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">CG</div><span class="card-img-fallback-label">CGTN America</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">CGTN America</div>
          <h3 class="media-title">Jalisco mothers search for hidden graves with drones</h3>
          <span class="media-tag" data-key="tv-social">TV / Social</span>
        </div>
      </a>

      <a class="media-card" href="https://www.sinembargo.mx/18-12-2023/4440515" target="_blank" rel="noopener">
        <div class="card-img-wrap" data-url="https://www.sinembargo.mx/18-12-2023/4440515">
          <div class="card-img-fallback"><div class="card-img-fallback-initial">SE</div><span class="card-img-fallback-label">SinEmbargo</span></div>
        </div>
        <div class="media-card-inner">
          <div class="media-outlet">SinEmbargo</div>
          <h3 class="media-title">Tecnología para hallarlos</h3>
          <span class="media-tag" data-key="article">Artículo</span>
        </div>
      </a>

    </section>

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

  </div>

  <script>
  (function(){

    /* ── translations ── */
    const translations = {
      en:{ 'media-pill':'MEDIA · COVERAGE · TALKS','media-title':'Media Coverage','media-intro':'Our research and work has been featured in leading international publications.','talks-title':'Talks' },
      es:{ 'media-pill':'MEDIOS · COBERTURA · CHARLAS','media-title':'Cobertura en medios','media-intro':'Nuestras investigaciones y trabajo han aparecido en medios internacionales de referencia.','talks-title':'Charlas' },
      nah:{ 'media-pill':'MEDIOS · TLAYEKOLOLLO · TLAHTOLMEH','media-title':'Tlayekoliztli ipan medios','media-intro':'Totlatequi huan totlatlamachtiliztli yopanok ipan medios internacionales.','talks-title':'Tlatlahtolmeh' }
    };
    const tagLabels = {
      en:{ article:'Article', tv:'TV Segment', 'tv-social':'TV / Social', opinion:'Opinion' },
      es:{ article:'Artículo', tv:'Segmento TV', 'tv-social':'TV / Redes', opinion:'Opinión' },
      nah:{ article:'Tlatlaquiliztli', tv:'Segmento TV', 'tv-social':'TV / Social', opinion:'Tlaixkomati' }
    };

    /* ── verified OG image cache ──────────────────────────────────────────
       Only URLs that are real, publicly accessible CDN images go here.
       Fabricated / guessed paths have been removed — they silently 404ed.
       To add more: open the article, right-click the hero image → Copy image address.
    ────────────────────────────────────────────────────────────────────── */
  const imageCache = {
  /* AP English – verified dims.apnews.com CDN */
  'https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86':
    'https://dims.apnews.com/dims4/default/1339f24/2147483647/strip/true/crop/5787x3858+0+0/resize/800x533!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F28%2Fd6%2F16de093c02d8eca2c4e72728ee15%2Ff711d05e15a441539dd2a5c5c0d96024',
  /* AP Spanish – verified */
  'https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e':
    'https://dims.apnews.com/dims4/default/84d15a6/2147483647/strip/true/crop/6000x4000+0+0/resize/1440x960!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F8a%2F79%2F48ede3475408ac83e81f43fba2df%2Fc4afa1567a524012b687f4a20f823071',
  /* NBC News – verified s-nbcnews.com CDN */
  'https://www.nbcnews.com/news/amp/rcna221791':
    'https://media4.s-nbcnews.com/j/newscms/2025_31/8b3c7f/250729-mexico-pigs-ac-1148a.jpg',
  /* BBC Mundo – verified ichef.bbci.co.uk CDN */
  'https://www.bbc.com/mundo/articles/c4gv9r1120mo':
    'https://ichef.bbci.co.uk/ace/ws/960/cpsprodpb/b0cc/live/6dd78840-9ebb-11f0-85b6-27ff7e482819.jpg',
  /* El País (English & Spanish) – same image */
  'https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html':
    'https://imagenes.elpais.com/resizer/v2/5DABWFBL4VEBVBR5EIKKVFRESM.png?auth=9adc5210e779bc292717217b2f47e0aee59c66535e9f222f1070a21c00e54fbb&width=1200',
  'https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html':
    'https://imagenes.elpais.com/resizer/v2/5DABWFBL4VEBVBR5EIKKVFRESM.png?auth=9adc5210e779bc292717217b2f47e0aee59c66535e9f222f1070a21c00e54fbb&width=1200',
  /* Reuters – verified */
  'https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/':
    'https://www.reuters.com/resizer/v2/X6RTO532DRPT7JPBEEGLTE3DJY.jpg?auth=0317c4086f252f559ecf2bc523208bba7a2d81ec1308e0aae7e35826387c779f&width=960&quality=80',
  /* Museo Medellín – verified wp-content path */
  'https://www.museocasadelamemoria.gov.co/noticias/encontrar-a-las-personas-que-nos-hacen-falta-mision-de-alianza-entre-medellin-reino-unido-y-mexico/':
    'https://www.museocasadelamemoria.gov.co/wp-content/uploads/2026/02/5.jpeg',
  /* The Independent – verified static.independent.co.uk */
  'https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html':
    'https://static.independent.co.uk/2025/07/29/05/Mexico_Disappeared_Science_73653.jpg',
  /* The Guardian */
  'https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims':
    'https://i.guim.co.uk/img/media/a4f0273b6434132a9a64254814c782cf7ad4cc09/836_132_5157_3438/master/5157.jpg?width=1900&dpr=1&s=none&crop=none',
  /* Vice */
  'https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/':
    'https://www.vice.com/wp-content/uploads/sites/2/2024/06/vice-logo_white@2x.png?resize=150,48',
  /* Los Angeles Times */
  'https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico':
    'https://ca-times.brightspotcdn.com/dims4/default/90e3690/2147483647/strip/true/crop/6000x4000+0+0/resize/1200x800!/format/webp/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fc8%2F73%2Fd34a1997355bc3ef47a5b6d7295f%2F73062f68829c4f328744e1d92862bfcb',
  /* NBC News */
  'https://www.nbcnews.com/news/latino/mexico-pigs-buried-help-find-missing-rcna221791':
    'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1000w,f_auto,q_auto:best/rockcms/2025-07/250729-Zapopan-ch-1409-5f806d.jpg',
  /* Animal Politico */
  'https://grupoanimal.mx/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia':
    'https://grupoanimal.mx/api/image-proxy?url=https%3A%2F%2Fap-cdn.sfo3.cdn.digitaloceanspaces.com%2Fuploads%2F2024%2F11%2Fmadres-buscadoras-ia.jpg',
  /* Science */
  'https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims':
    'https://www.science.org/do/10.1126/science.z3qry0t/full/_20250825_on_drug_war_graves.jpg',
  /* Wired */
  'https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico':
    'https://media.es.wired.com/photos/6524b15390bca1e6dd148cb7/master/w_1600,c_limit/%20Familiares%20de%20vi%CC%81ctimas%20desaparecidas%20y%20miembros%20de%20la%20Comisio%CC%81n%20Nacional%20de%20Bu%CC%81squeda%20y%20Guardias%20Nacionales%20buscan%20personas%20desaparecidas%20en%20Morelos,%202022..jpg',
  /* TV Azteca */
  'https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas':
    'https://tvazteca.brightspotcdn.com/dims4/default/1eaebde/2147483647/strip/true/crop/92x59+0+0/resize/70x45!/format/webp/quality/90/?url=http%3A%2F%2Ftv-azteca-brightspot.s3.amazonaws.com%2F26%2F7e%2F9c61ae1d4b8dbcc1c816c086707d%2Fimagotipo-azteca.webp',
  /* Animal Politico Interpretar la Naturaleza */
  'https://grupoanimal.mx/opinion/libro-madres-buscadoras-fil':
    'https://grupoanimal.mx/api/image-proxy?url=https%3A%2F%2Fap-cdn.sfo3.cdn.digitaloceanspaces.com%2Fuploads%2F2024%2F11%2Fmadres-buscadoras-ia.jpg',
  /* CGTN America */
  'https://x.com/cgtnamerica/status/1751362286118150555':
    'https://pbs.twimg.com/media/GE4Wp0mWMAA29uD?format=jpg&name=small',
  /* SinEmbargo */
  'https://www.sinembargo.mx/18-12-2023/4440515':
    'https://www.sinembargo.mx/wp-content/uploads/2023/12/busqueda-fosas-2-768x768.jpeg'
};

    /* ── load image for one card ── */
    function loadCard(wrap) {
      const url = wrap.dataset.url;
      if (!url) return;

      const cached = imageCache[url];
      if (cached) {
        tryImage(wrap, cached);
        return;
      }

      /* OG fetch fallback via allorigins proxy */
      wrap.classList.add('loading');
      const proxy = 'https://api.allorigins.win/raw?url=';
      fetch(proxy + encodeURIComponent(url), { signal: AbortSignal.timeout(6000) })
        .then(r => r.text())
        .then(html => {
          const m =
            html.match(/<meta[^>]+property=["']og:image["'][^>]+content=["']([^"']+)["']/i) ||
            html.match(/<meta[^>]+content=["']([^"']+)["'][^>]+property=["']og:image["']/i);
          wrap.classList.remove('loading');
          if (m && m[1]) tryImage(wrap, m[1]);
        })
        .catch(() => wrap.classList.remove('loading'));
    }

    /* try loading an image URL; silently keep fallback if it errors */
    function tryImage(wrap, src) {
      const img = new Image();
      img.className = 'card-img';
      img.alt = '';
      img.onload = () => {
        wrap.classList.add('has-image');
        wrap.insertBefore(img, wrap.firstChild);
      };
      img.onerror = () => { /* fallback stays visible */ };
      img.src = src;
    }

    /* ── language ── */
    function setLanguage(lang) {
      const dict = translations[lang] || translations.en;
      Object.keys(dict).forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerHTML = dict[id];
      });
      const tagMap = tagLabels[lang] || tagLabels.en;
      document.querySelectorAll('.media-tag').forEach(el => {
        const key = el.dataset.key;
        if (key && tagMap[key]) el.textContent = tagMap[key];
      });
      document.documentElement.lang = lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en');
      document.querySelectorAll('.lang-btn').forEach(btn =>
        btn.classList.toggle('active', btn.dataset.lang === lang)
      );
      try { localStorage.setItem('found-lang-media', lang); } catch(e) {}
    }

    /* ── init ── */
    document.addEventListener('DOMContentLoaded', function() {
      let saved = null;
      try { saved = localStorage.getItem('found-lang-media'); } catch(e) {}
      setLanguage((saved === 'es' || saved === 'en' || saved === 'nah') ? saved : 'en');

      document.querySelectorAll('.lang-btn').forEach(btn =>
        btn.addEventListener('click', () => setLanguage(btn.dataset.lang))
      );

      /* staggered load so network isn't hammered at once */
      document.querySelectorAll('.card-img-wrap').forEach((wrap, i) =>
        setTimeout(() => loadCard(wrap), i * 120)
      );
    });

  })();
  </script>
</body>
</html>
