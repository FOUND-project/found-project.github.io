---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

    .news-shell{
      max-width:1300px;
      margin:0 auto;
      position:relative;
    }

    /* Language toggle (same style as home) */
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

    /* Grid of cards */
    .news-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
      gap:clamp(1.5rem,2.4vw,2.2rem);
      margin-bottom:2rem;
    }

    .news-card{
      background:#ffffff;
      border-radius:var(--radius-md);
      padding:1.6rem 1.6rem 1.85rem;
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

    /* SPECIAL BACKGROUND FOR FOUND SECTION */
    .news-card.found-section{
      background:
        radial-gradient(circle at 0% 0%, rgba(232,245,240,.95) 0%, transparent 55%),
        linear-gradient(145deg,#f8fcfb 0%,#e8f5f0 50%,#ffffff 100%);
      border-left:4px solid var(--primary-green);
    }

    .news-card.found-section::before{
      background:
        radial-gradient(circle at 5% 0%, rgba(232,245,240,.9) 0%, transparent 55%),
        radial-gradient(circle at 100% 0%, rgba(45,95,77,.12) 0%, transparent 55%);
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
      font-size:2.1rem;
      margin-bottom:.6rem;
    }

    .card-badge{
      display:inline-flex;
      align-items:center;
      gap:.35rem;
      padding:.16rem .65rem;
      border-radius:var(--radius-pill);
      font-size:.72rem;
      font-weight:750;
      letter-spacing:.12em;
      text-transform:uppercase;
      background:rgba(27,77,62,.06);
      color:var(--dark-green);
      border:1px solid rgba(27,77,62,.18);
      margin-bottom:.55rem;
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
      font-size:1.18rem;
      font-weight:800;
      color:var(--dark-green);
      line-height:1.4;
      flex:1;
      letter-spacing:-.01em;
    }

    .expand-icon{
      background:var(--dark-green);
      color:#fff;
      width:30px;
      height:30px;
      border-radius:50%;
      display:flex;
      align-items:center;
      justify-content:center;
      font-size:1.1rem;
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
      margin-top:.95rem;
    }

    .card-content p{
      margin-bottom:.9rem;
      font-size:.98rem;
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
      margin:1.4rem 0 1rem;
      box-shadow:0 14px 30px rgba(15,23,42,.22);
      border:1px solid rgba(255,255,255,.9);
    }

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
        padding:1.3rem 1.15rem 1.5rem;
      }
      .card-title{
        font-size:1.05rem;
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

      <!-- Card 3: Frontier Tech Hub support (FOUND section with new background) -->
      <article class="news-card found-section">
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
        /* ... unchanged JS translations ... */
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
