---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FOUND — Media & Talks</title>

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
        radial-gradient(1200px 600px at 10% 0%, rgba(45,95,77,.12) 0%, transparent 55%),
        radial-gradient(900px 520px at 80% 0%, rgba(232,245,240,.92) 0%, transparent 60%),
        linear-gradient(135deg,#f7fbfa 0%,#eef4f1 40%,#f9fbff 100%);
      min-height:100vh;
      color:var(--text-dark);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      padding:clamp(1.5rem,3vw,2.5rem) clamp(1rem,4vw,3rem);
    }

    /* Make Minimal Mistakes wrappers full width */
    .page,
    #main,
    .initial-content,
    .page__inner-wrap,
    .page__content,
    .archive{
      max-width:none!important;
      width:100%!important;
    }

    *:focus-visible{
      outline:3px solid rgba(74,140,115,.7);
      outline-offset:3px;
      border-radius:10px;
    }

    .media-shell{
      max-width:1300px;
      margin:0 auto;
      position:relative;
      /* push main content right so it does not sit over the author logos */
      padding-left:clamp(13rem, 18vw, 16rem);
    }

    /* Language toggle (same style as NEWS) */
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
    .media-header{
      background:
        radial-gradient(circle at 8% 0%, rgba(45,95,77,.20) 0%, transparent 55%),
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

    .media-header::before{
      content:'';
      position:absolute;
      inset:-1px;
      background:linear-gradient(
        120deg,
        rgba(255,255,255,.7),
        transparent 35%,
        transparent 65%,
        rgba(45,95,77,.22)
      );
      opacity:.85;
      pointer-events:none;
    }

    .media-logo-wrap{
      flex:0 0 auto;
      position:relative;
      z-index:1;
    }

    .media-header img{
      width:90px;
      height:90px;
      border-radius:20px;
      object-fit:cover;
      box-shadow:0 14px 30px rgba(15,23,42,.22);
      border:2px solid rgba(255,255,255,.9);
      background:#fff;
    }

    .media-header-main{
      position:relative;
      z-index:1;
      flex:1;
    }

    .media-header-pill{
      display:inline-flex;
      align-items:center;
      gap:.4rem;
      padding:.2rem .75rem;
      border-radius:var(--radius-pill);
      background:rgba(27,77,62,.08);
      border:1px solid rgba(27,77,62,.22);
      font-size:.78rem;
      font-weight:750;
      letter-spacing:.16em;
      text-transform:uppercase;
      color:var(--dark-green);
      margin-bottom:.55rem;
    }

    .media-header-pill::before{
      content:'';
      width:6px;
      height:6px;
      border-radius:50%;
      background:radial-gradient(circle,var(--primary-green) 0%,rgba(45,95,77,.18) 70%);
    }

    #media-title{
      font-size:clamp(1.9rem,3.2vw,2.4rem);
      color:var(--dark-green);
      font-weight:900;
      letter-spacing:-.03em;
      margin-bottom:.45rem;
    }

    #media-intro{
      font-size:clamp(1rem,1.4vw,1.15rem);
      color:var(--text-medium);
      max-width:780px;
      line-height:1.8;
    }

    /* MEDIA GRID */
    .media-grid{
      margin-top:0;
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
      gap:clamp(1.7rem,2.5vw,2.3rem);
      margin-bottom:2.4rem;
    }

    .media-card{
      background:#ffffff;
      border-radius:var(--radius-md);
      padding:1.6rem 1.6rem 1.7rem;
      box-shadow:var(--shadow-sm);
      border:1px solid rgba(15,23,42,.06);
      position:relative;
      overflow:hidden;
      transition:
        transform .25s var(--transition-smooth),
        box-shadow .25s var(--transition-smooth),
        border-color .25s var(--transition-smooth),
        background .25s var(--transition-smooth),
        filter .25s var(--transition-smooth);
      display:flex;
      flex-direction:column;
      min-height:0;
    }

    .media-card::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 10% 0%, rgba(232,245,240,.85) 0%, transparent 55%),
        radial-gradient(circle at 100% 0%, rgba(45,95,77,.16) 0%, transparent 55%);
      opacity:0;
      pointer-events:none;
      transition:opacity .25s var(--transition-smooth);
    }

    .media-card:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(45,95,77,.28);
      background:#ffffff;
      filter:saturate(1.03);
    }

    .media-card:hover::before{
      opacity:1;
    }

    .media-link{
      text-decoration:none;
      color:inherit;
      display:block;
      height:100%;
    }

    .media-outlet{
      font-size:.74rem;
      text-transform:uppercase;
      letter-spacing:.12em;
      font-weight:760;
      color:var(--dark-green);
      margin-bottom:.85rem;
      display:inline-flex;
      align-items:center;
      gap:.4rem;
    }

    .media-outlet::before{
      content:'';
      width:7px;
      height:7px;
      border-radius:50%;
      background:linear-gradient(135deg,var(--light-green),var(--primary-green));
      box-shadow:0 0 0 2px rgba(27,77,62,.15);
    }

    .media-title{
      font-size:1.06rem;
      font-weight:660;
      color:var(--text-dark);
      margin:0 0 1.15rem 0;
      line-height:1.5;
      letter-spacing:-.01em;
    }

    .media-link:hover .media-title{
      color:var(--dark-green);
    }

    .media-tag{
      display:inline-flex;
      align-items:center;
      gap:.35rem;
      margin-top:auto;
      font-size:.7rem;
      text-transform:uppercase;
      letter-spacing:.08em;
      font-weight:650;
      padding:.38rem .9rem;
      border-radius:var(--radius-pill);
      background:rgba(27,77,62,.08);
      color:var(--dark-green);
      transition:
        background .2s var(--transition-smooth),
        color .2s var(--transition-smooth),
        transform .2s var(--transition-smooth);
    }

    .media-tag::after{
      content:'↗';
      font-size:.78rem;
      opacity:.7;
    }

    .media-card:hover .media-tag{
      background:rgba(27,77,62,.14);
      transform:translateX(2px);
    }

    /* TALKS */
    .talks-section{
      margin-top:0;
      padding:1.9rem 1.9rem 1.3rem;
      border-radius:var(--radius-lg);
      background:
        radial-gradient(circle at 6% 0%, rgba(208,239,224,.95) 0%, transparent 55%),
        linear-gradient(135deg,#ffffff 0%,#f4fbf7 65%,#ffffff 100%);
      box-shadow:var(--shadow-sm);
      border:1px solid rgba(15,23,42,.06);
    }

    #talks-title{
      font-size:1.8rem;
      font-weight:860;
      color:var(--dark-green);
      margin-bottom:1.4rem;
      letter-spacing:-.02em;
    }

    .talk-card{
      background:linear-gradient(135deg,#ffffff 0%,#f7fbf9 100%);
      padding:1.25rem 1.5rem;
      border-radius:14px;
      box-shadow:0 1px 3px rgba(0,0,0,.05);
      border:1px solid rgba(0,0,0,.06);
      position:relative;
      overflow:hidden;
      transition:
        transform .25s var(--transition-smooth),
        box-shadow .25s var(--transition-smooth),
        border-color .25s var(--transition-smooth),
        background .25s var(--transition-smooth);
      margin-bottom:1.1rem;
    }

    .talk-card::before{
      content:'';
      position:absolute;
      left:0;
      top:0;
      bottom:0;
      width:4px;
      background:linear-gradient(180deg,var(--dark-green) 0%,var(--light-green) 100%);
      transform:scaleY(0);
      transform-origin:bottom;
      transition:transform .3s var(--transition-smooth);
    }

    .talk-card:hover{
      transform:translateX(4px);
      box-shadow:0 8px 24px rgba(0,0,0,.12);
      border-color:rgba(27,77,62,.25);
      background:linear-gradient(145deg,#ffffff 0%,#ebf6f1 100%);
    }

    .talk-card:hover::before{
      transform:scaleY(1);
      transform-origin:top;
    }

    .talk-title{
      font-size:.82rem;
      font-weight:750;
      text-transform:uppercase;
      letter-spacing:.08em;
      margin-bottom:.55rem;
      color:var(--dark-green);
    }

    .talk-link{
      font-size:1.03rem;
      text-decoration:none;
      color:var(--text-dark);
      font-weight:600;
      line-height:1.4;
      letter-spacing:-.01em;
      display:inline-block;
      transition:color .2s var(--transition-smooth);
    }

    .talk-link:hover{
      color:var(--dark-green);
    }

    @media (max-width:1100px){
      .media-shell{
        padding-left:0; /* remove offset on tablet/mobile so it uses full width */
      }
    }

    @media (max-width:900px){
      body{
        padding:1.4rem 1rem;
      }
      .lang-toggle{
        position:static;
        margin-left:auto;
        margin-bottom:.4rem;
      }
      .media-header{
        flex-direction:column;
        align-items:flex-start;
        margin-top:.5rem;
      }
      .media-logo-wrap{
        order:-1;
      }
      .media-header img{
        width:80px;
        height:80px;
      }
      #media-title{
        font-size:1.7rem;
      }
      .media-grid{
        grid-template-columns:1fr;
      }
      .talks-section{
        padding:1.5rem 1.3rem 1.1rem;
      }
    }

    @media (max-width:480px){
      .media-header{
        padding:1.3rem 1.1rem;
      }
      .media-card{
        padding:1.35rem 1.2rem 1.5rem;
      }
      #talks-title{
        font-size:1.55rem;
      }
    }
  </style>
</head>

<body>
  <div class="media-shell">
    <!-- Language toggle -->
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
    </div>

    <!-- HEADER -->
    <header class="media-header">
      <div class="media-logo-wrap">
        <img
          src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/master/images/Found_logo.jpg"
          alt="FOUND logo"
        >
      </div>
      <div class="media-header-main">
        <div class="media-header-pill" id="media-pill">
          MEDIA • COVERAGE • TALKS
        </div>
        <h1 id="media-title">Media Coverage</h1>
        <p id="media-intro">
          Our research and work has been featured in leading international publications.
        </p>
      </div>
    </header>

    <!-- MEDIA GRID -->
    <section class="media-grid">
      <!-- The Guardian -->
      <article class="media-card">
        <a class="media-link" href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">The Guardian</div>
            <h3 class="media-title">
              How dead pigs are helping in the search for missing victims of Mexico's drug wars
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- Associated Press (EN) -->
      <article class="media-card">
        <a class="media-link" href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Associated Press</div>
            <h3 class="media-title">
              Why are scientists dressing pigs in clothes and burying them in Mexico?
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- Associated Press (ES) -->
      <article class="media-card">
        <a class="media-link" href="https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Associated Press</div>
            <h3 class="media-title">
              Ciencia, tecnología y cerdos. México experimenta nuevas formas de buscar a los desaparecidos
            </h3>
            <span class="media-tag" data-key="article">Artículo</span>
          </div>
        </a>
      </article>

      <!-- Independent -->
      <article class="media-card">
        <a class="media-link" href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">The Independent</div>
            <h3 class="media-title">
              How pigs could help find missing Mexican drug cartel victims
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- VICE -->
      <article class="media-card">
        <a class="media-link" href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">VICE</div>
            <h3 class="media-title">
              Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- Los Angeles Times -->
      <article class="media-card">
        <a class="media-link" href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Los Angeles Times</div>
            <h3 class="media-title">
              Why are scientists dressing pigs in clothes and burying them in Mexico?
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- NBC News -->
      <article class="media-card">
        <a class="media-link" href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">NBC News</div>
            <h3 class="media-title">
              Clothed pigs are buried in Mexico as scientists use them in search of missing
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- Animal Político -->
      <article class="media-card">
        <a class="media-link" href="https://www.animalpolitico.com/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Animal Político</div>
            <h3 class="media-title">
              Con tecnología y drones, investigadores y familias de desaparecidos encuentran fosas clandestinas en Jalisco
            </h3>
            <span class="media-tag" data-key="article">Artículo</span>
          </div>
        </a>
      </article>

      <!-- Science -->
      <article class="media-card">
        <a class="media-link" href="https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Science</div>
            <h3 class="media-title">
              Satellites could reveal the secret burial grounds of Mexico's murder victims
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- WIRED -->
      <article class="media-card">
        <a class="media-link" href="https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">WIRED (ES)</div>
            <h3 class="media-title">
              Cómo la tecnología geoespacial expone el horror de las fosas clandestinas en México
            </h3>
            <span class="media-tag" data-key="article">Artículo</span>
          </div>
        </a>
      </article>

      <!-- El País (EN) -->
      <article class="media-card">
        <a class="media-link" href="https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">El País (EN)</div>
            <h3 class="media-title">
              Mexico's Izaguirre ranch: “High concentrations of ash” suggest the presence of clandestine crematoriums
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- El País (ES) -->
      <article class="media-card">
        <a class="media-link" href="https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">El País</div>
            <h3 class="media-title">
              "Altas concentraciones de ceniza" y humo de gasolina: los indicios que apuntan a que en el rancho de Teuchitlán hubo crematorios clandestinos
            </h3>
            <span class="media-tag" data-key="article">Artículo</span>
          </div>
        </a>
      </article>

      <!-- TV Azteca -->
      <article class="media-card">
        <a class="media-link" href="https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">TV Azteca</div>
            <h3 class="media-title">
              Tecnología contra las desapariciones en México
            </h3>
            <span class="media-tag" data-key="tv">TV segment</span>
          </div>
        </a>
      </article>

      <!-- Animal Político (opinion) -->
      <article class="media-card">
        <a class="media-link" href="https://animalpolitico.com/analisis/invitades/libro-madres-buscadoras-fil" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Animal Político</div>
            <h3 class="media-title">
              Interpretar la naturaleza para encontrar a quienes nos faltan
            </h3>
            <span class="media-tag" data-key="opinion">Opinion</span>
          </div>
        </a>
      </article>

      <!-- Reuters -->
      <article class="media-card">
        <a class="media-link" href="https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Reuters</div>
            <h3 class="media-title">
              In Mexico, mothers of the missing turn to drones to look for unmarked graves
            </h3>
            <span class="media-tag" data-key="article">Article</span>
          </div>
        </a>
      </article>

      <!-- CGTN America -->
      <article class="media-card">
        <a class="media-link" href="https://twitter.com/cgtnamerica/status/1751362286118150555" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">CGTN America</div>
            <h3 class="media-title">
              Jalisco mothers search for hidden graves with drones
            </h3>
            <span class="media-tag" data-key="tv-social">TV / Social</span>
          </div>
        </a>
      </article>

      <!-- SinEmbargo -->
      <article class="media-card">
        <a class="media-link" href="https://www.sinembargo.mx/18-12-2023/4440515" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">SinEmbargo</div>
            <h3 class="media-title">
              Tecnología para hallarlos
            </h3>
            <span class="media-tag" data-key="article">Artículo</span>
          </div>
        </a>
      </article>
    </section>

    <!-- TALKS -->
    <section class="talks-section">
      <h2 id="talks-title">Talks</h2>

      <div class="talk-card">
        <div class="talk-title">
          University of Oxford / Oxford Festival of the Arts
        </div>
        <a class="talk-link" href="https://www.ox.ac.uk/event/technological-responses-disappearance" target="_blank" rel="noopener">
          Disappearance of Worlds | Art Exhibition &amp; Dialogues on Disappearance
        </a>
      </div>

      <div class="talk-card">
        <div class="talk-title">
          British Association for Forensic Anthropology (BAFA)
        </div>
        <a class="talk-link" href="https://bafauk.weebly.com/winter-conference--agm-2024.html" target="_blank" rel="noopener">
          Interpreting nature to locate the disappeared: influencing search practices in Jalisco, Mexico
        </a>
      </div>

      <div class="talk-card">
        <div class="talk-title">
          Guadalajara International Book Fair (FIL)
        </div>
        <a class="talk-link" href="https://jalisco.quadratin.com.mx/principal/presentan-interpretar-la-naturaleza-para-encontrar-a-quienes-nos-faltan/" target="_blank" rel="noopener">
          Presentan Interpretar la naturaleza para encontrar a quienes nos faltan
        </a>
      </div>

      <div class="talk-card">
        <div class="talk-title">
          University of Oxford
        </div>
        <a class="talk-link" href="https://www.ox.ac.uk/event/mexicos-missing-how-families-and-technology-are-working-together" target="_blank" rel="noopener">
          Mexico's Missing: How families and technology are working together
        </a>
      </div>
    </section>
  </div>

  <!-- LANGUAGE SCRIPT -->
  <script>
    (function(){
      const translations = {
        en:{
          'media-pill':'MEDIA • COVERAGE • TALKS',
          'media-title':'Media Coverage',
          'media-intro':'Our research and work has been featured in leading international publications.',
          'talks-title':'Talks'
        },
        es:{
          'media-pill':'MEDIOS • COBERTURA • CHARLAS',
          'media-title':'Cobertura en medios',
          'media-intro':'Nuestras investigaciones y trabajo han aparecido en medios internacionales de referencia.',
          'talks-title':'Charlas'
        },
        nah:{
          'media-pill':'MEDIOS • TLAYEKOLOLLO • TLAHTOLMEH',
          'media-title':'Tlayekoliztli ipan medios',
          'media-intro':'Totlatequi huan totlatlamachtiliztli yopanok ipan medios internacionales tlen hueyi tlanechicoliztli.',
          'talks-title':'Tlatlahtolmeh'
        }
      };

      const tagLabels = {
        en:{
          article:'Article',
          tv:'TV segment',
          'tv-social':'TV / Social',
          opinion:'Opinion'
        },
        es:{
          article:'Artículo',
          tv:'Segmento TV',
          'tv-social':'TV / Redes',
          opinion:'Opinión'
        },
        nah:{
          article:'Tlatlaquiliztli',
          tv:'Segmento TV',
          'tv-social':'TV / Social',
          opinion:'Tlaixkomati'
        }
      };

      function setLanguage(lang){
        const dict = translations[lang] || translations.en;

        Object.keys(dict).forEach(id => {
          const el = document.getElementById(id);
          if(el) el.innerHTML = dict[id];
        });

        // update tag chips
        const tagMap = tagLabels[lang] || tagLabels.en;
        document.querySelectorAll('.media-tag').forEach(el=>{
          const key = el.dataset.key;
          if(key && tagMap[key]){
            el.textContent = tagMap[key];
          }
        });

        document.documentElement.setAttribute(
          'lang',
          lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en')
        );

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        try{ localStorage.setItem('found-lang-media', lang); }catch(e){}
      }

      document.addEventListener('DOMContentLoaded', function(){
        let savedLang = null;
        try{ savedLang = localStorage.getItem('found-lang-media'); }catch(e){}
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
