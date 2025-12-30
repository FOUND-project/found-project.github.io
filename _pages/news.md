---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- Keep desktop layout on all screens -->
  <meta name="viewport" content="width=1200">
  <title>FOUND — News & Updates</title>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
    }

    :root{
      --primary-green:#2d5f4d;
      --dark-green:#1e4034;
      --light-green:#4a8c73;
      --gold-accent:#d4af37;
      --bg-soft:#f4faf7;
      --text-dark:#121212;
      --text-medium:#3f3f3f;
      --text-light:#6b6b6b;
      --shadow-sm:0 4px 16px rgba(15,23,42,.08);
      --shadow-md:0 10px 28px rgba(15,23,42,.12);
      --shadow-lg:0 20px 50px rgba(15,23,42,.18);
      --radius-lg:22px;
      --radius-md:18px;
      --radius-pill:999px;
      --transition-smooth:cubic-bezier(.4,0,.2,1);
    }

    @media (prefers-reduced-motion: reduce){
      *,*::before,*::after{
        animation-duration:.01ms!important;
        animation-iteration-count:1!important;
        transition-duration:.01ms!important;
      }
      html{scroll-behavior:auto!important;}
    }

    html{scroll-behavior:smooth;}

    body{
      font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,system-ui,sans-serif;
      background:
        radial-gradient(1200px 600px at 10% 0%, rgba(212,175,55,.12) 0%, transparent 55%),
        radial-gradient(900px 520px at 80% 0%, rgba(232,245,240,.85) 0%, transparent 60%),
        linear-gradient(135deg,#f7fbfa 0%,#eef4f1 40%,#f9fbff 100%);
      min-height:100vh;
      color:var(--text-dark);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      padding:clamp(1.5rem,3vw,2.5rem) clamp(1rem,4vw,3rem);
    }

    /* Make page full-width inside Minimal Mistakes */
    .page,
    #main,
    .initial-content,
    .page__inner-wrap,
    .page__content,
    .archive{
      max-width:none!important;
      width:100% !important;
    }

    *:focus-visible{
      outline:3px solid rgba(74,140,115,.6);
      outline-offset:2px;
      border-radius:10px;
    }

    /* SHIFT WHOLE NEWS AREA TO THE RIGHT (like Media) */
    .news-shell{
      max-width:1300px;
      margin:0 auto 0 5.6rem; /* space for the circular logo on the left */
      position:relative;
    }

    /* Language toggle (same style as home / media) */
    .lang-toggle{
      position:absolute;
      top:0.25rem;
      right:0;
      display:inline-flex;
      gap:.5rem;
      z-index:10;
    }

    .lang-btn{
      border:1px solid rgba(15,23,42,.08);
      background:rgba(255,255,255,.9);
      color:var(--dark-green);
      padding:.3rem .8rem;
      border-radius:var(--radius-pill);
      font-size:.78rem;
      font-weight:700;
      letter-spacing:.08em;
      text-transform:uppercase;
      cursor:pointer;
      backdrop-filter:blur(10px);
      box-shadow:0 4px 14px rgba(15,23,42,.08);
      transition:
        transform .2s var(--transition-smooth),
        background .2s var(--transition-smooth),
        box-shadow .2s var(--transition-smooth),
        border-color .2s var(--transition-smooth),
        color .2s var(--transition-smooth);
    }

    .lang-btn:hover{
      background:#fff;
      transform:translateY(-1px);
      box-shadow:0 8px 22px rgba(15,23,42,.16);
    }

    .lang-btn.active{
      background:var(--dark-green);
      color:#fff;
      border-color:var(--dark-green);
    }

    /* Header */
    .news-header{
      background:
        radial-gradient(circle at 8% 0%, rgba(212,175,55,.18) 0%, transparent 55%),
        linear-gradient(135deg,#ffffff 0%,#f6faf8 40%,#ffffff 100%);
      border-radius:var(--radius-lg);
      padding:clamp(1.75rem,3vw,2.4rem);
      margin:1.75rem 0 2.8rem;
      display:flex;
      align-items:center;
      gap:clamp(1.4rem,3vw,2.4rem);
      box-shadow:var(--shadow-md);
      border:1px solid rgba(15,23,42,.06);
      position:relative;
      overflow:hidden;
    }

    .news-header::before{
      content:'';
      position:absolute;
      inset:-1px;
      background:linear-gradient(120deg, rgba(255,255,255,.6), transparent 35%, transparent 65%, rgba(212,175,55,.25));
      opacity:.8;
      pointer-events:none;
    }

    .news-logo-wrap{
      flex:0 0 auto;
      position:relative;
      z-index:1;
    }

    .news-header img{
      width:90px;
      height:90px;
      border-radius:20px;
      object-fit:cover;
      box-shadow:0 14px 30px rgba(15,23,42,.22);
      border:2px solid rgba(255,255,255,.9);
      background:#fff;
    }

    .news-header-main{
      position:relative;
      z-index:1;
      flex:1;
    }

    #news-title{
      font-size:clamp(1.9rem,3.2vw,2.4rem);
      color:var(--dark-green);
      font-weight:900;
      letter-spacing:-.03em;
      margin-bottom:.45rem;
    }

    #news-subtitle{
      font-size:clamp(1rem,1.4vw,1.15rem);
      color:var(--text-medium);
      max-width:720px;
      line-height:1.75;
    }

    .news-tagline-pill{
      display:inline-flex;
      align-items:center;
      gap:.4rem;
      padding:.2rem .75rem;
      border-radius:var(--radius-pill);
      background:rgba(27,77,62,.06);
      border:1px solid rgba(27,77,62,.2);
      font-size:.78rem;
      font-weight:750;
      letter-spacing:.16em;
      text-transform:uppercase;
      color:var(--dark-green);
      margin-bottom:.5rem;
    }

    .news-tagline-pill::before{
      content:'';
      width:6px;
      height:6px;
      border-radius:50%;
      background:radial-gradient(circle,var(--gold-accent) 0%,rgba(212,175,55,.18) 70%);
    }

    /* Grid of cards – slightly smaller */
    .news-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); /* was 280px */
      gap:clamp(1.3rem,2.1vw,2rem); /* a bit tighter */
      margin-bottom:2rem;
    }

    .news-card{
      background:#ffffff;
      border-radius:var(--radius-md);
      padding:1.4rem 1.5rem 1.6rem; /* smaller padding */
      box-shadow:var(--shadow-sm);
      border:1px solid rgba(15,23,42,.06);
      position:relative;
      overflow:hidden;
      transition:
        transform .25s var(--transition-smooth),
        box-shadow .25s var(--transition-smooth),
        border-color .25s var(--transition-smooth),
        background .25s var(--transition-smooth);
      display:flex;
      flex-direction:column;
      min-height:0;
    }

    .news-card::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 10% 0%, rgba(232,245,240,.7) 0%, transparent 55%),
        radial-gradient(circle at 100% 0%, rgba(212,175,55,.16) 0%, transparent 55%);
      opacity:0;
      pointer-events:none;
      transition:opacity .25s var(--transition-smooth);
    }

    .news-card.mariela-card{
      border-left:4px solid var(--gold-accent);
    }

    .news-card:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(45,95,77,.28);
      background:#ffffff;
    }

    .news-card:hover::before{
      opacity:1;
    }

    .card-inner{
      position:relative;
      z-index:1;
      display:flex;
      flex-direction:column;
      height:100%;
    }

    .card-emoji{
      font-size:2rem; /* slightly smaller */
      margin-bottom:.55rem;
    }

    .card-badge{
      display:inline-flex;
      align-items:center;
      gap:.35rem;
      padding:.14rem .6rem;
      border-radius:var(--radius-pill);
      font-size:.7rem;
      font-weight:750;
      letter-spacing:.12em;
      text-transform:uppercase;
      background:rgba(27,77,62,.06);
      color:var(--dark-green);
      border:1px solid rgba(27,77,62,.18);
      margin-bottom:.5rem;
    }

    .card-badge::before{
      content:'●';
      font-size:.46rem;
    }

    .expand-toggle{
      display:none;
    }

    .card-header{
      display:flex;
      justify-content:space-between;
      align-items:flex-start;
      gap:1rem;
      cursor:pointer;
    }

    .card-title{
      font-size:1.12rem; /* a bit smaller than before */
      font-weight:800;
      color:var(--dark-green);
      line-height:1.4;
      flex:1;
      letter-spacing:-.01em;
    }

    .expand-icon{
      background:var(--dark-green);
      color:#fff;
      width:28px;
      height:28px;
      border-radius:50%;
      display:flex;
      align-items:center;
      justify-content:center;
      font-size:1rem;
      transition:
        background .2s var(--transition-smooth),
        transform .2s var(--transition-smooth),
        box-shadow .2s var(--transition-smooth);
      flex-shrink:0;
      user-select:none;
      box-shadow:0 8px 18px rgba(15,23,42,.25);
    }

    .card-header:hover .expand-icon{
      background:var(--light-green);
      transform:scale(1.06);
      box-shadow:0 12px 24px rgba(15,23,42,.3);
    }

    .expand-icon::before{
      content:'+';
    }

    .expand-toggle:checked ~ .card-header .expand-icon::before{
      content:'−';
    }

    .card-content{
      max-height:0;
      overflow:hidden;
      transition:max-height .5s var(--transition-smooth), margin-top .4s var(--transition-smooth);
      color:var(--text-medium);
      line-height:1.7;
    }

    .expand-toggle:checked ~ .card-header + .card-content{
      max-height:5000px;
      margin-top:.9rem;
    }

    .card-content p{
      margin-bottom:.85rem;
      font-size:.96rem;
    }

    .card-content strong{
      color:var(--dark-green);
      font-weight:650;
    }

    .card-content a{
      color:var(--dark-green);
      text-decoration:none;
      font-weight:650;
      border-bottom:2px solid rgba(45,95,77,.35);
      padding-bottom:.05rem;
      transition:border-color .2s var(--transition-smooth), color .2s var(--transition-smooth);
    }

    .card-content a:hover{
      border-bottom-color:var(--gold-accent);
      color:var(--primary-green);
    }

    .card-content ul{
      margin:1rem 0;
      padding-left:1.25rem;
    }

    .card-content ul li{
      margin-bottom:.45rem;
    }

    .card-content img{
      width:100%;
      border-radius:16px;
      margin:1.3rem 0 1rem;
      box-shadow:0 14px 30px rgba(15,23,42,.22);
      border:1px solid rgba(255,255,255,.9);
    }

    /* These mobile rules won't trigger while viewport is fixed at 1200,
       but keeping them is harmless if you ever switch back */
    @media (max-width:900px){
      body{
        padding:1.4rem 1rem;
      }
      .lang-toggle{
        position:static;
        margin-left:auto;
        margin-right:0;
        margin-bottom:.6rem;
      }
      .news-header{
        flex-direction:column;
        align-items:flex-start;
        margin-top:.5rem;
      }
      .news-logo-wrap{
        order:-1;
      }
      .news-header img{
        width:80px;
        height:80px;
      }
      #news-title{
        font-size:1.6rem;
      }
      .news-grid{
        grid-template-columns:1fr;
      }
    }

    @media (max-width:480px){
      .news-header{
        padding:1.3rem 1.1rem;
      }
      .news-card{
        padding:1.3rem 1.1rem 1.45rem;
      }
      .card-title{
        font-size:1.04rem;
      }
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

    <!-- HEADER -->
    <header class="news-header">
      <div class="news-logo-wrap">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true" alt="FOUND Logo">
      </div>
      <div class="news-header-main">
        <div class="news-tagline-pill" id="news-pill">
          NEWS • IMPACT • MEDIA
        </div>
        <h1 id="news-title">FOUND — News &amp; Updates</h1>
        <p id="news-subtitle">
          Latest developments on our work across Mexico, Colombia, and beyond.
        </p>
      </div>
    </header>

    <!-- GRID -->
    <section class="news-grid">

      <!-- Card 0: Mariela award -->
      <article class="news-card mariela-card" id="mariela-award">
        <div class="card-inner">
          <span class="card-emoji">🎖️</span>
          <span class="card-badge" id="card0-badge">Award</span>

          <input type="checkbox" id="card0" class="expand-toggle">
          <label for="card0" class="card-header">
            <span class="card-title" id="card0-title">
              FOUND’s pioneer wins the UK FCDO’s Sir Nicholas Browne Policy and Expertise Award
            </span>
            <span class="expand-icon"></span>
          </label>

          <div class="card-content">
            <p id="card0-p1">
              We are proud to share that <strong>Mariela Garfias</strong> has been awarded the
              <strong>Sir Nicholas Browne Policy and Expertise Award</strong>, a UK FCDO award recognising excellence in delivering policy objectives, selected from more than 200 nominations.
            </p>
            <p id="card0-p2">
              Mariela is FOUND’s FCDO pioneer and one of the people most responsible for the project’s impact.
            </p>
            <p id="card0-p3">
              Through FOUND, and with the support of incredible partners, we have located <strong>27 people</strong> who were victims of disappearance in Mexico, allowing families to move towards answers and a form of closure. Our work is now being embedded with local and national authorities, and has expanded to collaboration with the <strong>Colombian Search Unit</strong> and the Executive Office of the <strong>UN Secretary-General</strong>.
            </p>
            <p id="card0-p4">
              In her acceptance speech, Mariela shared words that capture the spirit of FOUND:
              “From my decomposed body, flowers shall grow, and I am in them. That is eternity.” — Edvard Munch.
            </p>
            <p id="card0-p5">
              When searching for clandestine graves using technologies, nature often bears witness — through subtle changes in soil and vegetation. Memory persists. Our responsibility is to find it.
            </p>
            <p id="card0-p6">
              Mariela thanked those who carry this work with us: the British Embassy in Mexico City, our mentor <strong>Martin Johnston</strong>, the Frontier Tech Hub team, and above all the searching mothers, whose knowledge and strength remain our compass.
            </p>
            <p>
              <a
                id="card0-link"
                href="https://www.linkedin.com/posts/found-project_mexico-colombian-activity-7405294966266044416-2-bh"
                target="_blank"
                rel="noopener noreferrer"
              >
                Read the full post on LinkedIn ↗
              </a>
            </p>
          </div>
        </div>
      </article>

      <!-- Card 1: UBPD visit -->
      <article class="news-card">
        <div class="card-inner">
          <span class="card-emoji">🇨🇴🇲🇽</span>
          <span class="card-badge" id="card1-badge">Field visit</span>

          <input type="checkbox" id="card1" class="expand-toggle">
          <label for="card1" class="card-header">
            <span class="card-title" id="card1-title">
              Second visit of Colombia’s Search Unit for Missing Persons (UBPD) to FOUND’s experimental sites in Jalisco
            </span>
            <span class="expand-icon"></span>
          </label>

          <div class="card-content">
            <p id="card1-p1">
              We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.
            </p>
            <p id="card1-p2">
              We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia’s <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND’s experimental sites in Jalisco.
            </p>
            <p id="card1-p3">
              This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND’s experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.
            </p>
            <p id="card1-p4">
              It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.
            </p>
            <p id="card1-p5">
              During this second visit, the UBPD offered key technical recommendations to enhance FOUND’s detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD’s team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND’s partner states in Mexico.
            </p>
          </div>
        </div>
      </article>

      <!-- Card 2: Guardian article -->
      <article class="news-card">
        <div class="card-inner">
          <span class="card-emoji">📄</span>
          <span class="card-badge" id="card2-badge">Media</span>

          <input type="checkbox" id="card2" class="expand-toggle">
          <label for="card2" class="card-header">
            <span class="card-title" id="card2-title">FOUND in The Guardian</span>
            <span class="expand-icon"></span>
          </label>

          <div class="card-content">
            <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND in The Guardian">
            <p id="card2-p1">
              This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist’s in-person visit to our experimental sites in Jalisco, Mexico.
            </p>
            <p id="card2-p2">
              We are deeply grateful for the care, depth, and commitment brought to this story after months spent listening to families, researchers, and officials.
            </p>
            <p>
              <a id="card2-link" href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener noreferrer">
                Read the article in The Guardian ↗
              </a>
            </p>
          </div>
        </div>
      </article>

      <!-- Card 3: Frontier Tech Hub support -->
      <article class="news-card">
        <div class="card-inner">
          <span class="card-emoji">🇬🇧</span>
          <span class="card-badge" id="card3-badge">Funding</span>

          <input type="checkbox" id="card3" class="expand-toggle">
          <label for="card3" class="card-header">
            <span class="card-title" id="card3-title">
              FOUND receives new support from the UK’s FCDO through the Frontier Tech Hub
            </span>
            <span class="expand-icon"></span>
          </label>

          <div class="card-content">
            <p id="card3-p1">
              In the pitch, our team showcased FOUND’s impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.
            </p>
            <p id="card3-p2">
              <strong>🌱 Driven by families and research communities</strong><br>
              FOUND is guided and motivated by mothers’ search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
            </p>
            <p id="card3-p3">
              <strong>🔍 We are now working directly with:</strong>
            </p>
            <ul id="card3-list">
              <li>Executive Office of the UN Secretary-General</li>
              <li>UK’s Foreign, Commonwealth &amp; Development Office (FCDO)</li>
              <li>Local Search Commissions and Attorney’s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li>
              <li>Colombian Search Unit</li>
              <li>Mexico’s National Search Commission</li>
              <li>Mexican Science and Technology Secretariat</li>
              <li>British Embassy in Mexico City</li>
              <li>British Association for Forensic Anthropology</li>
            </ul>
            <p id="card3-p4">
              <strong>🛰️ Technology for memory, dignity, and closure</strong><br>
              We will continue developing — and embedding in official protocols — new ways to locate missing persons using advanced tools such as machine-learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.
            </p>
            <p id="card3-p5"><em>FOUND: Interpreting Nature to Locate Those We Are Missing.</em></p>
          </div>
        </div>
      </article>

      <!-- Card 4: International media coverage -->
      <article class="news-card">
        <div class="card-inner">
          <span class="card-emoji">📰</span>
          <span class="card-badge" id="card4-badge">Coverage</span>

          <input type="checkbox" id="card4" class="expand-toggle">
          <label for="card4" class="card-header">
            <span class="card-title" id="card4-title">
              FOUND featured by Associated Press, The Independent, LA Times, VICE, and NBC
            </span>
            <span class="expand-icon"></span>
          </label>

          <div class="card-content">
            <ul id="card4-list">
              <li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
              <li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li>
              <li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
              <li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li>
              <li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li>
            </ul>
          </div>
        </div>
      </article>

    </section>
  </div>

  <!-- LANGUAGE SCRIPT -->
  <script>
    (function(){
      const translations = {
        en:{
          'news-pill':'NEWS • IMPACT • MEDIA',
          'news-title':'FOUND — News &amp; Updates',
          'news-subtitle':'Latest developments on our work across Mexico, Colombia, and beyond.',
          'card0-badge':'Award',
          'card0-title':'FOUND’s pioneer wins the UK FCDO’s Sir Nicholas Browne Policy and Expertise Award',
          'card0-p1':'We are proud to share that <strong>Mariela Garfias</strong> has been awarded the <strong>Sir Nicholas Browne Policy and Expertise Award</strong>, a UK FCDO award recognising excellence in delivering policy objectives, selected from more than 200 nominations.',
          'card0-p2':'Mariela is FOUND’s FCDO pioneer and one of the people most responsible for the project’s impact.',
          'card0-p3':'Through FOUND, and with the support of incredible partners, we have located <strong>27 people</strong> who were victims of disappearance in Mexico, allowing families to move towards answers and a form of closure. Our work is now being embedded with local and national authorities, and has expanded to collaboration with the <strong>Colombian Search Unit</strong> and the Executive Office of the <strong>UN Secretary-General</strong>.',
          'card0-p4':'In her acceptance speech, Mariela shared words that capture the spirit of FOUND: “From my decomposed body, flowers shall grow, and I am in them. That is eternity.” — Edvard Munch.',
          'card0-p5':'When searching for clandestine graves using technologies, nature often bears witness — through subtle changes in soil and vegetation. Memory persists. Our responsibility is to find it.',
          'card0-p6':'Mariela thanked those who carry this work with us: the British Embassy in Mexico City, our mentor <strong>Martin Johnston</strong>, the Frontier Tech Hub team, and above all the searching mothers, whose knowledge and strength remain our compass.',
          'card0-link':'Read the full post on LinkedIn ↗',

          'card1-badge':'Field visit',
          'card1-title':'Second visit of Colombia’s Search Unit for Missing Persons (UBPD) to FOUND’s experimental sites in Jalisco',
          'card1-p1':'We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.',
          'card1-p2':'We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia’s <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND’s experimental sites in Jalisco.',
          'card1-p3':'This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND’s experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.',
          'card1-p4':'It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.',
          'card1-p5':'During this second visit, the UBPD offered key technical recommendations to enhance FOUND’s detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD’s team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND’s partner states in Mexico.',

          'card2-badge':'Media',
          'card2-title':'FOUND in The Guardian',
          'card2-p1':'This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist’s in-person visit to our experimental sites in Jalisco, Mexico.',
          'card2-p2':'We are deeply grateful for the care, depth, and commitment brought to this story after months spent listening to families, researchers, and officials.',
          'card2-link':'Read the article in The Guardian ↗',

          'card3-badge':'Funding',
          'card3-title':'FOUND receives new support from the UK’s FCDO through the Frontier Tech Hub',
          'card3-p1':'In the pitch, our team showcased FOUND’s impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.',
          'card3-p2':'<strong>🌱 Driven by families and research communities</strong><br>FOUND is guided and motivated by mothers’ search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.',
          'card3-p3':'<strong>🔍 We are now working directly with:</strong>',
          'card3-list':'<li>Executive Office of the UN Secretary-General</li><li>UK’s Foreign, Commonwealth &amp; Development Office (FCDO)</li><li>Local Search Commissions and Attorney’s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li><li>Colombian Search Unit</li><li>Mexico’s National Search Commission</li><li>Mexican Science and Technology Secretariat</li><li>British Embassy in Mexico City</li><li>British Association for Forensic Anthropology</li>',
          'card3-p4':'<strong>🛰️ Technology for memory, dignity, and closure</strong><br>We will continue developing — and embedding in official protocols — new ways to locate missing persons using advanced tools such as machine-learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.',
          'card3-p5':'<em>FOUND: Interpreting Nature to Locate Those We Are Missing.</em>',

          'card4-badge':'Coverage',
          'card4-title':'FOUND featured by Associated Press, The Independent, LA Times, VICE, and NBC',
          'card4-list':'<li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li>'
        },

        es:{
          'news-pill':'NOTICIAS • IMPACTO • MEDIOS',
          'news-title':'FOUND — Noticias y Actualizaciones',
          'news-subtitle':'Las novedades más recientes sobre nuestro trabajo en México, Colombia y más allá.',
          'card0-badge':'Reconocimiento',
          'card0-title':'La pionera de FOUND recibe el Premio Sir Nicholas Browne de Política y Pericia del FCDO británico',
          'card0-p1':'Nos enorgullece compartir que <strong>Mariela Garfias</strong> ha recibido el <strong>Premio Sir Nicholas Browne de Política y Pericia</strong>, un reconocimiento del FCDO británico a la excelencia en la implementación de objetivos de política, seleccionado entre más de 200 nominaciones.',
          'card0-p2':'Mariela es la pionera de FOUND dentro del FCDO y una de las personas más responsables del impacto del proyecto.',
          'card0-p3':'A través de FOUND, y con el apoyo de aliadas y aliados extraordinarios, hemos localizado a <strong>27 personas</strong> víctimas de desaparición en México, permitiendo que sus familias avancen hacia respuestas y alguna forma de cierre. Nuestro trabajo se está incorporando a autoridades locales y nacionales, y se ha ampliado a una colaboración con la <strong>Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia</strong> y con la Oficina Ejecutiva del <strong>Secretario General de la ONU</strong>.',
          'card0-p4':'En su discurso de aceptación, Mariela compartió unas palabras que capturan el espíritu de FOUND: “De mi cuerpo descompuesto crecerán flores, y yo estoy en ellas. Eso es la eternidad”. — Edvard Munch.',
          'card0-p5':'Al buscar fosas clandestinas con tecnologías, la naturaleza suele dar testimonio — a través de cambios sutiles en el suelo y la vegetación. La memoria persiste. Nuestra responsabilidad es encontrarla.',
          'card0-p6':'Mariela agradeció a quienes sostienen este trabajo con nosotras y nosotros: la Embajada Británica en Ciudad de México, nuestro mentor <strong>Martin Johnston</strong>, el equipo de Frontier Tech Hub y, sobre todo, las madres buscadoras, cuyo conocimiento y fuerza siguen siendo nuestra brújula.',
          'card0-link':'Leer la publicación completa en LinkedIn ↗',

          'card1-badge':'Visita de campo',
          'card1-title':'Segunda visita de la Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD) de Colombia a los sitios experimentales de FOUND en Jalisco',
          'card1-p1':'Agradecemos profundamente a <strong>CVM Cyber</strong> y a <strong>Ciaran Martin</strong> por su apoyo para hacer posible esta visita.',
          'card1-p2':'Recibimos a <strong>Héctor Javier Gómez</strong>, geofísico de la <em>Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)</em> de Colombia, para un despliegue conjunto en los sitios experimentales de FOUND en Jalisco.',
          'card1-p3':'La visita se centró en la obtención y el procesamiento de imágenes hiperespectrales mediante dron en los cinco sitios experimentales de FOUND — apenas la segunda vez que esta tecnología se utiliza en México con fines humanitarios.',
          'card1-p4':'Se trata de la continuación de la visita de octubre de 2025 de <strong>el Dr. Julián Arias</strong>, Director de Prospección, Recuperación e Identificación de la UBPD, que marcó el inicio formal de nuestra colaboración en metodologías de búsqueda e identificación.',
          'card1-p5':'Durante esta segunda visita, la UBPD compartió recomendaciones técnicas clave para reforzar las estrategias de FOUND para detectar fosas clandestinas. La colaboración continuará en enero de 2026, cuando el equipo de FOUND visitará a la UBPD en Colombia para intercambiar experiencias e integrar sus metodologías en los estados aliados de FOUND en México.',

          'card2-badge':'Medios',
          'card2-title':'FOUND en The Guardian',
          'card2-p1':'Este reportaje es el resultado de más de seis meses de correos electrónicos, mensajes de WhatsApp y la visita en terreno de la periodista a nuestros sitios experimentales en Jalisco, México.',
          'card2-p2':'Agradecemos profundamente el cuidado, la profundidad y el compromiso con el que se trabajó esta historia, tras meses escuchando a familias, personas investigadoras y autoridades.',
          'card2-link':'Leer el reportaje en The Guardian ↗',

          'card3-badge':'Financiación',
          'card3-title':'FOUND recibe nuevo apoyo del FCDO del Reino Unido a través de Frontier Tech Hub',
          'card3-p1':'En la presentación, nuestro equipo mostró el impacto alcanzado por FOUND hasta la fecha, y recibimos una financiación que nos permitirá escalar nuestra misión: impulsar cambios sistémicos en la forma de buscar a las personas desaparecidas en México, Colombia y más allá.',
          'card3-p2':'<strong>🌱 Impulsado por familias y comunidades de investigación</strong><br>FOUND está guiado y motivado por colectivos de madres buscadoras y por personas investigadoras de CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge y las Universidades Autónomas de Zacatecas y San Luis Potosí.',
          'card3-p3':'<strong>🔍 Actualmente trabajamos directamente con:</strong>',
          'card3-list':'<li>Oficina Ejecutiva del Secretario General de la ONU</li><li>Foreign, Commonwealth &amp; Development Office (FCDO) del Reino Unido</li><li>Comisiones y Fiscalías de Búsqueda de Jalisco, Zacatecas, San Luis Potosí y Chihuahua (México)</li><li>Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia</li><li>Comisión Nacional de Búsqueda de Personas de México</li><li>Secretaría de Ciencia y Tecnología de México</li><li>Embajada Británica en México</li><li>British Association for Forensic Anthropology</li>',
          'card3-p4':'<strong>🛰️ Tecnología para la memoria, la dignidad y el cierre</strong><br>Continuaremos desarrollando — y ayudando a incorporar en los protocolos oficiales — nuevas formas de localizar a personas desaparecidas mediante herramientas como modelos de aprendizaje automático, cámaras hiperespectrales, instrumentos sísmicos y tomografía eléctrica.',
          'card3-p5':'<em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>',

          'card4-badge':'Cobertura',
          'card4-title':'FOUND en Associated Press, The Independent, LA Times, VICE y NBC',
          'card4-list':'<li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li>'
        },

        nah:{
          'news-pill':'TLATLAHCUILOLLI • TLAKAMEH • MEDIOS',
          'news-title':'FOUND — Tlen mochihua huan tlen pano',
          'news-subtitle':'Nuevas tlamantli tlen totlatequi ipan Mēxihco, Colombia huan oksekan.',
          'card0-badge':'Tlatlepanitaliztli',
          'card0-title':'In pionera de FOUND kiseli in Premio Sir Nicholas Browne de Política huan Pericia (FCDO)',
          'card0-p1':'Tiquinechpoua ika pakilistli ke <strong>Mariela Garfias</strong> okiseli in <strong>Premio Sir Nicholas Browne de Política y Pericia</strong>, tlatlepanitaliztli de in FCDO británico tlen kixnextia kualli tequitl ipan políticas, tlaxtlahuilli tlen más de 200 propuestah.',
          'card0-p2':'Mariela yeto in pionera de FOUND dentro de in FCDO huan se de in tlacameh tlen okitmaka hueyi tlakameh inin proyecto.',
          'card0-p3':'Ika FOUND, huan ika tlatlapalehuiliztli de miek toknihuan, yotiknextijkeh kan okatkah <strong>27 tlācameh</strong> tlen polihuitkeh ipan Mēxihco, tlen kimpalehuiah in familias kiseliskeh tlanemilistli huan se tipo de cierre. In tequitl yotemosewia kan autoridades locales huan nacionales, huan yopanok ika sekolaboración ika <strong>Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia</strong> huan ika Oficina Ejecutiva del <strong>Secretario General de la ONU</strong>.',
          'card0-p4':'Ipan in tlajtohketl de kiselis in premio, Mariela okijtoua tlahtolli tlen kixkopina in espíritu de FOUND: “De mi cuerpo descompuesto crecerán flores, y yo estoy en ellas. Eso es la eternidad”. — Edvard Munch.',
          'card0-p5':'Ijkuak tiktlatemohuah fosas clandestinas ika tecnologías, in tlalli huan xihuitl miek wel kitenextiah — ika tlapeyaliztli tlen tzintla o ipan xihuitl. In memoria amo polihui. Totekipano in tikajsikilis.',
          'card0-p6':'Mariela okimotlajkamat in tlen kualkanin kinyeknekiltiah nin tequitl: Embajada Británica ipan Ciudad de México, in tomentor <strong>Martin Johnston</strong>, in equipo de Frontier Tech Hub, huan, achtoyan, in nananmeh buscadoras, tlen inintlamatiliztli huan yolchikahualiztli mochipa yetos tocompás.',
          'card0-link':'Xikmotlajkolti in tlatlatol ipan LinkedIn ↗',

          'card1-badge':'Tlayekoliztli ipan tlalli',
          'card1-title':'Ome visita de in Unidad de Búsqueda de Colombia (UBPD) kan sitios experimentales de FOUND ipan Jalisco',
          'card1-p1':'Timitztlajkamatih miek ika <strong>CVM Cyber</strong> huan <strong>Ciaran Martin</strong> por ininpalehuiliztli para nikchihuase nin visita.',
          'card1-p2':'Otikweltaskeh <strong>Héctor Javier Gómez</strong>, geofísico de in <em>Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)</em> de Colombia, para se tlatskayotl tlayekoliztli ipan sitios experimentales de FOUND ipan Jalisco.',
          'card1-p3':'In visita omochi para tiknotsaskeh huan tiktlaxtlawaskeh imágenes hiperespectrales ika dron ipan makuil sitios experimentales de FOUND — san ome welta okitekuitilijkeh nin tecnología ipan Mēxihco ika propósito humanitario.',
          'card1-p4':'Nin tlayekoliztli hualpehua desde in visita de octubre 2025 de <strong>Dr. Julián Arias</strong>, Director de Prospección, Recuperación e Identificación de la UBPD, tlen okitlapolwi oficialmente in sekolaboración ipan metodologías de búsqueda e identificación.',
          'card1-p5':'Ipan nin ompa visita, UBPD okimakak tlanawatilistli teknikah para okachi tikchikawaseh estrategias de FOUND para tlamiktiloyan tlatemohuiliztli. In sekolaboración yas okachi wejkapa ipan enero 2026, ijkuak in equipo FOUND yas Colombia para motla’ahxilis huan kinekitsas metodologías de UBPD ipan estados compañero de FOUND ipan Mēxihco.',

          'card2-badge':'Medios',
          'card2-title':'FOUND ipan The Guardian',
          'card2-p1':'Nin reportaje omochi ika más de chikuasen metztli de correos, mensajes de WhatsApp huan visita de in periodista kan sitios experimentales de Jalisco, Mēxihco.',
          'card2-p2':'Titlajkamatih miek por in cuidado, hueyikan tlamachilistli huan compromiso tlen okitemitijkeh nin historia, satepan de miek metztli okikakiah familias, investigadores huan autoridades.',
          'card2-link':'Xikmotlajkolti in reportaje ipan The Guardian ↗',

          'card3-badge':'Financiamiento',
          'card3-title':'FOUND kiselia yankuik tlapalehuiliztli de in FCDO británico ika Frontier Tech Hub',
          'card3-p1':'Ipan in presentación, inin equipo okixnexti in tlakameh tlen FOUND okichi, huan otikselijkeh se financiamiento tlen techpalehuis para tikueskaltis in misión: xikpatla se modo sistémico de kenik tiktlatemohuah personas desaparecidas ipan Mēxihco, Colombia huan oksekan.',
          'card3-p2':'<strong>🌱 Tlatekitilistli tlen petlani desde familias huan comunidades de investigación</strong><br>FOUND kinyeknemilia nananmeh buscadoras huan investigadores de CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge huan Universidades Autónomas de Zacatecas huan San Luis Potosí.',
          'card3-p3':'<strong>🔍 Axkan titekitih san sejco ika:</strong>',
          'card3-list':'<li>Oficina Ejecutiva del Secretario General de la ONU</li><li>Foreign, Commonwealth &amp; Development Office (FCDO) de Reino Unido</li><li>Comisiones de Búsqueda huan Fiscalías de Jalisco, Zacatecas, San Luis Potosí huan Chihuahua (Mēxihco)</li><li>Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia</li><li>Comisión Nacional de Búsqueda de Personas de México</li><li>Secretaría de Ciencia y Tecnología de México</li><li>Embajada Británica ipan México</li><li>British Association for Forensic Anthropology</li>',
          'card3-p4':'<strong>🛰️ Teknolojía para memoria, tlatepanitaliztli huan cierre</strong><br>Tikchiwaseh okse yankuik ojtli para tiktlatemohuah personas desaparecidas ika modelos de machine learning, cámaras hiperespectrales, instrumentos sísmicos huan tomografía eléctrica, huan tikneki se tlamantli momanah inin ipan protocolos oficiales.',
          'card3-p5':'<em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>',

          'card4-badge':'Tlayekoliztli ipan medios',
          'card4-title':'FOUND ipan Associated Press, The Independent, LA Times, VICE huan NBC',
          'card4-list':'<li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener noreferrer">How pigs could help find missing Mexican drug cartel victims</a></li><li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener noreferrer">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li><li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener noreferrer">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li><li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener noreferrer">Clothed pigs are buried in Mexico as scientists use them in search of the missing</a></li>'
        }
      };

      const ids = [
        'news-pill','news-title','news-subtitle',
        'card0-badge','card0-title','card0-p1','card0-p2','card0-p3','card0-p4','card0-p5','card0-p6','card0-link',
        'card1-badge','card1-title','card1-p1','card1-p2','card1-p3','card1-p4','card1-p5',
        'card2-badge','card2-title','card2-p1','card2-p2','card2-link',
        'card3-badge','card3-title','card3-p1','card3-p2','card3-p3','card3-list','card3-p4','card3-p5',
        'card4-badge','card4-title','card4-list'
      ];

      function setLanguage(lang){
        const dict = translations[lang] || translations.en;

        ids.forEach(id=>{
          const el = document.getElementById(id);
          if(el && dict[id] !== undefined){
            el.innerHTML = dict[id];
          }
        });

        document.documentElement.setAttribute(
          'lang',
          lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en')
        );

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        try{ localStorage.setItem('found-lang-news', lang); }catch(e){}
      }

      document.addEventListener('DOMContentLoaded', function(){
        let savedLang = null;
        try{ savedLang = localStorage.getItem('found-lang-news'); }catch(e){}
        const initialLang = (savedLang === 'es' || savedLang === 'en' || savedLang === 'nah') ? savedLang : 'en';
        setLanguage(initialLang);

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.addEventListener('click', ()=> setLanguage(btn.dataset.lang));
        });
      });
    })();
  </script>
</body>
</html>
