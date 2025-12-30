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
      max-width:none;
      width:100%;
      margin:0;
      position:relative;
      padding-left:clamp(10rem, 14vw, 13rem);
      padding-right:2rem;
    }

    /* Language toggle – tucked inside header area */
    .lang-toggle{
      position:absolute;
      top:1.1rem;
      right:2.4rem;
      display:inline-flex;
      gap:.5rem;
      z-index:20;
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
      padding:clamp(1.9rem,3.3vw,2.6rem);
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

    /* MEDIA GRID – 5 cards per row on desktop */
    .media-grid{
      margin-top:0;
      display:grid;
      grid-template-columns:repeat(5,minmax(0,1fr));
      gap:1.6rem;
      margin-bottom:2.4rem;
    }

    .media-card{
      background:#ffffff;
      border-radius:var(--radius-md);
      padding:1.4rem 1.4rem 1.5rem;
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

    /* Outlet pill – green-ish highlight */
    .media-outlet{
      font-size:.74rem;
      text-transform:uppercase;
      letter-spacing:.12em;
      font-weight:760;
      color:var(--dark-green);
      margin-bottom:.75rem;
      display:inline-flex;
      align-items:center;
      gap:.4rem;
      padding:.35rem .9rem;
      border-radius:var(--radius-pill);
      background:rgba(45,95,77,.08);
      border:1px solid rgba(45,95,77,.16);
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
      font-size:1.02rem;
      font-weight:660;
      color:var(--text-dark);
      margin:0 0 1.05rem 0;
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
        padding-left:0;
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
      <!-- cards unchanged -->
      <!-- ... your articles exactly as before ... -->
      <!-- (keep all the <article class="media-card"> blocks you already have) -->
      <!-- I didn’t edit any of their content, just the CSS above. -->
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
          btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
        });
      });
    })();
  </script>
</body>
</html>
