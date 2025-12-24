---
permalink: /
title:
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="FOUND combines technology and grassroots knowledge to search for disappeared persons in Mexico, bringing dignity and closure to families." />
  <meta property="og:title" content="FOUND Project - Using Technology to Search and Remember" />
  <meta property="og:description" content="124,354 persons are reported as disappeared in Mexico. Behind each case, there is a family searching for answers. FOUND combines technology with the knowledge of searching families to learn, locate, and drive systemic change." />
  <meta property="og:type" content="website" />
  <title>FOUND Project - Using Technology to Search and Remember</title>

  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    :root{
      --primary-green:#2d5f4d;
      --dark-green:#1e4034;
      --light-green:#4a8c73;
      --accent-green:#e8f5f0;
      --gold-accent:#d4af37;
      --text-dark:#1a1a1a;
      --text-medium:#4a4a4a;
      --text-light:#666;
      --border-light:#e0e0e0;
      --shadow-sm:0 2px 8px rgba(0,0,0,.06);
      --shadow-md:0 4px 16px rgba(0,0,0,.08);
      --shadow-lg:0 8px 24px rgba(0,0,0,.12);
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

    body{
      font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
      color:var(--text-dark);
      line-height:1.7;
      background:#fff;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      overflow-x:hidden;
    }

    *:focus-visible{
      outline:3px solid var(--light-green);
      outline-offset:2px;
      border-radius:6px;
    }

    /* Language toggle */
    .lang-toggle{
      position:absolute;
      top:1.5rem;
      right:clamp(1rem,4vw,3rem);
      display:inline-flex;
      gap:.5rem;
      z-index:2;
    }

    .lang-btn{
      border:1px solid rgba(255,255,255,.8);
      background:rgba(0,0,0,.15);
      color:#fff;
      padding:.25rem .75rem;
      border-radius:999px;
      font-size:.85rem;
      font-weight:600;
      letter-spacing:.06em;
      text-transform:uppercase;
      cursor:pointer;
      transition:all .2s var(--transition-smooth);
      backdrop-filter:blur(6px);
    }

    .lang-btn:hover{background:rgba(0,0,0,.3);}

    .lang-btn.active{
      background:#fff;
      color:var(--dark-green);
      border-color:#fff;
      box-shadow:0 0 0 1px rgba(0,0,0,.08);
    }

    /* Title */
    .title-section{
      padding:clamp(3rem,8vw,5rem) 0 clamp(2rem,6vw,4rem);
      background:linear-gradient(135deg,#1a3d2f 0%,var(--dark-green) 50%,var(--primary-green) 100%);
      position:relative;
      overflow:hidden;
      text-align:center;
      margin-bottom:2rem;
      box-shadow:var(--shadow-lg);
    }

    .title-section::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 30% 50%, rgba(212,175,55,.1) 0%, transparent 50%),
        radial-gradient(circle at 70% 30%, rgba(232,245,240,.05) 0%, transparent 50%);
      z-index:0;
    }

    .project-title{
      font-size:clamp(2.5rem,6vw,4.5rem);
      font-weight:800;
      color:#fff;
      margin-bottom:1.5rem;
      letter-spacing:-.02em;
      line-height:1.1;
      text-shadow:0 4px 12px rgba(0,0,0,.2);
      position:relative;
      z-index:1;
    }

    .project-subtitle{
      font-size:clamp(1.3rem,3vw,1.8rem);
      font-weight:400;
      color:var(--accent-green);
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.5;
      max-width:900px;
      margin:0 auto;
      position:relative;
      z-index:1;
      text-shadow:0 2px 8px rgba(0,0,0,.1);
      padding:0 clamp(1rem,4vw,3rem);
    }

    .title-accent{color:var(--gold-accent);font-weight:700;}

    /* Hero */
    .hero{
      padding:clamp(2rem,6vw,4rem) clamp(1rem,4vw,3rem);
      background:linear-gradient(135deg,#f8fcfb 0%,#fff 100%);
      position:relative;
      overflow:hidden;
    }

    .hero::before{
      content:'';
      position:absolute;
      top:0; right:0;
      width:40%; height:100%;
      background:linear-gradient(45deg,var(--accent-green) 0%,transparent 100%);
      opacity:.3;
      z-index:0;
    }

    .hero-content{
      position:relative;
      z-index:1;
      max-width:1400px;
      margin:0 auto;
    }

    .animated-tagline{
      font-size:clamp(2rem,5vw,3.5rem);
      font-weight:800;
      display:flex;
      align-items:center;
      margin-bottom:2rem;
      color:var(--dark-green);
      flex-wrap:wrap;
      gap:.75rem;
      letter-spacing:-.02em;
      line-height:1.1;
    }

    .word-carousel{
      overflow:hidden;
      height:clamp(3rem,6vw,4rem);
      position:relative;
      display:inline-block;
      min-width:clamp(180px,30vw,300px);
    }

    .word-list{
      list-style:none;
      animation:continuousScroll 15s ease-in-out infinite;
      will-change:transform;
    }

    .word-list li{
      height:clamp(3rem,6vw,4rem);
      line-height:clamp(3rem,6vw,4rem);
      color:var(--light-green);
      font-weight:800;
      font-size:clamp(2rem,5vw,3.5rem);
    }

    @keyframes continuousScroll{
      0%,12.5%{transform:translateY(0%);}
      25%,37.5%{transform:translateY(-25%);}
      50%,62.5%{transform:translateY(-50%);}
      75%,87.5%{transform:translateY(-75%);}
      100%{transform:translateY(-100%);}
    }

    .hero-description{
      font-size:clamp(1.1rem,2.5vw,1.3rem);
      color:var(--text-medium);
      max-width:900px;
      margin-bottom:3rem;
      line-height:1.8;
      font-weight:400;
    }

    .hero-description strong{
      color:var(--primary-green);
      font-weight:600;
      background:linear-gradient(120deg,var(--accent-green) 0%,transparent 100%);
      padding:.1rem .3rem;
      border-radius:3px;
    }

    .hero-image-container{
      width:100%;
      max-width:1100px;
      margin:4rem auto 0;
      position:relative;
      border-radius:20px;
      overflow:hidden;
      box-shadow:var(--shadow-lg);
      background:var(--accent-green);
      transform:translateY(0);
      transition:transform .6s var(--transition-smooth);
    }

    .hero-image-container:hover{transform:translateY(-8px);}
    .hero-image-container::before{content:'';display:block;padding-top:56.25%;}

    .hero-image{
      position:absolute;
      inset:0;
      width:100%;
      height:100%;
      object-fit:cover;
      transition:transform .8s var(--transition-smooth);
    }

    .hero-image-container:hover .hero-image{transform:scale(1.05);}

    .skeleton{
      background:linear-gradient(90deg,#f0f0f0 25%,#e8f5f0 50%,#f0f0f0 75%);
      background-size:200% 100%;
      animation:loading 1.5s ease-in-out infinite;
    }

    @keyframes loading{
      0%{background-position:200% 0;}
      100%{background-position:-200% 0;}
    }

    .hero-image.loading{opacity:0;}

    /* Sections */
    .content-section{
      padding:clamp(2.5rem,5vw,4rem) clamp(1rem,4vw,3rem);
      border-bottom:1px solid var(--border-light);
      scroll-margin-top:2rem;
    }

    .content-section:last-of-type{border-bottom:none;}

    .section-container{
      max-width:1400px;
      margin:0 auto;
    }

    h2{
      font-size:clamp(1.8rem,4vw,2.8rem);
      font-weight:700;
      color:var(--dark-green);
      margin-bottom:1.5rem;
      letter-spacing:-.01em;
      position:relative;
      padding-bottom:1rem;
      line-height:1.3;
    }

    h2::after{
      content:'';
      position:absolute;
      bottom:0; left:0;
      width:80px; height:4px;
      background:linear-gradient(90deg,var(--light-green),var(--primary-green));
      border-radius:2px;
    }

    .info-list{
      list-style:none;
      padding-left:0;
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));
      gap:.75rem 2rem;
      margin-top:1.5rem;
    }

    .info-list li{
      padding:.75rem 0 .75rem 2.25rem;
      position:relative;
      color:var(--text-medium);
      font-size:clamp(.95rem,2.5vw,1.05rem);
      transition:all .3s ease;
      min-height:42px;
      display:flex;
      align-items:center;
      border-bottom:1px solid transparent;
      line-height:1.5;
    }

    .info-list li:hover{
      color:var(--primary-green);
      padding-left:2.5rem;
      border-bottom-color:var(--accent-green);
    }

    .info-list li::before{
      content:"✓";
      position:absolute;
      left:0;
      color:var(--light-green);
      font-weight:bold;
      font-size:1.2rem;
      transition:all .3s ease;
      top:50%;
      transform:translateY(-50%);
      background:var(--accent-green);
      width:28px; height:28px;
      border-radius:50%;
      display:flex;
      align-items:center;
      justify-content:center;
    }

    .info-list li:hover::before{
      transform:translateY(-50%) scale(1.1);
      background:var(--light-green);
      color:#fff;
    }

    /* Institutional Partnerships (logos + labels) */
    .collab-wrap{margin-top:2rem;}

    .collab-grid{
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));
      gap:clamp(1.25rem,2.5vw,2rem);
      margin-top:1.5rem;
    }

    .collab-card{
      background:#fff;
      border-radius:18px;
      box-shadow:var(--shadow-md);
      border:1px solid rgba(45,95,77,.10);
      overflow:hidden;
      position:relative;
      transition:transform .35s var(--transition-smooth), box-shadow .35s var(--transition-smooth), border-color .35s var(--transition-smooth);
      min-height:220px;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
    }

    .collab-card::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 15% 10%, rgba(232,245,240,.85) 0%, transparent 55%),
        radial-gradient(circle at 85% 0%, rgba(212,175,55,.12) 0%, transparent 60%);
      opacity:0;
      transition:opacity .35s ease;
      pointer-events:none;
    }

    .collab-card:hover{
      transform:translateY(-8px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.55);
    }

    .collab-card:hover::before{opacity:1;}

    .collab-logo{
      padding:1.25rem 1.25rem .75rem;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:140px;
      position:relative;
      z-index:1;
    }

    .collab-logo img{
      max-width:100%;
      max-height:95px;
      width:auto;
      height:auto;
      object-fit:contain;
      filter:grayscale(25%) brightness(1.05);
      transition:transform .35s var(--transition-smooth), filter .35s var(--transition-smooth), opacity .3s ease;
    }

    .collab-logo img.loading{opacity:0;}

    .collab-card:hover .collab-logo img{
      filter:grayscale(0%) brightness(1);
      transform:scale(1.04);
    }

    .collab-meta{
      padding:.85rem 1.15rem 1.15rem;
      border-top:1px solid rgba(0,0,0,.06);
      background:linear-gradient(180deg, rgba(232,245,240,.25) 0%, rgba(255,255,255,.85) 100%);
      position:relative;
      z-index:1;
    }

    .collab-name{
      font-weight:700;
      color:var(--dark-green);
      font-size:1.02rem;
      line-height:1.35;
      letter-spacing:-.01em;
    }

    .collab-note{
      margin-top:.35rem;
      color:var(--text-light);
      font-size:.92rem;
      line-height:1.45;
    }

    /* Social */
    .social-section{
      background:linear-gradient(135deg,var(--accent-green) 0%,#fff 100%);
      padding:clamp(3rem,6vw,5rem) clamp(1rem,4vw,3rem);
      margin:4rem 0;
      position:relative;
      overflow:hidden;
    }

    .social-container{max-width:1600px;margin:0 auto;}

    .section-title{
      font-size:clamp(2rem,5vw,3.2rem);
      font-weight:800;
      color:var(--dark-green);
      margin-bottom:1rem;
      text-align:center;
      letter-spacing:-.02em;
      line-height:1.2;
    }

    .section-subtitle{
      font-size:clamp(1.1rem,2.5vw,1.3rem);
      color:var(--text-medium);
      text-align:center;
      margin-bottom:3rem;
      max-width:800px;
      margin-left:auto;
      margin-right:auto;
      line-height:1.7;
    }

    .social-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,400px),1fr));
      gap:clamp(1.5rem,3vw,2.5rem);
    }

    .social-embed{
      background:#fff;
      border-radius:20px;
      padding:1.75rem;
      box-shadow:var(--shadow-lg);
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:450px;
      transition:all .4s var(--transition-smooth);
      border:1px solid rgba(45,95,77,.1);
      overflow:hidden;
      position:relative;
    }

    .iframe-container{
      position:relative;
      width:100%;
      max-width:600px;
      overflow:hidden;
      border-radius:16px;
    }

    .iframe-container iframe{width:100%;border:0;display:block;}

    /* Partners */
    .partners-section{
      background:linear-gradient(135deg,#f8fcfb 0%,#fff 100%);
      padding:clamp(4rem,8vw,6rem) clamp(1rem,4vw,3rem);
      position:relative;
    }

    .partners-container{max-width:1600px;margin:0 auto;}

    .partners-intro{
      text-align:center;
      max-width:1000px;
      margin:0 auto 4rem;
      color:var(--text-medium);
      font-size:clamp(1.1rem,2.5vw,1.3rem);
      line-height:1.8;
    }

    .partner-grid{
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));
      gap:clamp(2rem,4vw,3rem);
      margin:4rem 0;
    }

    .partner-logo{
      background:#fff;
      padding:clamp(2rem,4vw,3rem);
      border-radius:20px;
      box-shadow:var(--shadow-md);
      display:flex;
      align-items:center;
      justify-content:center;
      transition:all .4s var(--transition-smooth);
      border:2px solid transparent;
      min-height:200px;
      aspect-ratio:1.5;
      position:relative;
      overflow:hidden;
    }

    .partner-logo:hover{
      transform:translateY(-8px) scale(1.03);
      box-shadow:var(--shadow-lg);
      border-color:var(--light-green);
    }

    .partner-logo img{
      max-width:100%;
      max-height:100%;
      width:auto;
      height:auto;
      object-fit:contain;
      filter:grayscale(30%) brightness(1.1);
      transition:all .4s var(--transition-smooth);
      position:relative;
      z-index:1;
    }

    .partner-logo img.loading{opacity:0;}
    .partner-logo:hover img{filter:grayscale(0%) brightness(1);transform:scale(1.05);}

    /* Buscadoras */
    .buscadoras-section{
      background:linear-gradient(135deg,#fff8f5 0%,#fff 100%);
      padding:clamp(4rem,8vw,6rem) clamp(1rem,4vw,3rem);
      margin:4rem 0;
      position:relative;
      overflow:hidden;
    }

    .buscadoras-content{
      max-width:1100px;
      margin:0 auto;
      text-align:center;
    }

    .buscadoras-image{
      max-width:600px;
      margin:3rem auto;
      border-radius:20px;
      overflow:hidden;
      box-shadow:var(--shadow-lg);
    }

    /* Footer */
    .footer{
      text-align:center;
      padding:clamp(4rem,8vw,6rem) clamp(1rem,4vw,3rem);
      margin-top:4rem;
      border-top:2px solid var(--border-light);
      background:linear-gradient(135deg,#f8fcfb 0%,#fff 100%);
      position:relative;
      overflow:hidden;
    }

    .footer-content{max-width:1400px;margin:0 auto;}

    .footer em{
      font-size:clamp(1.3rem,3vw,1.8rem);
      color:var(--dark-green);
      font-weight:700;
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.6;
      display:inline-block;
      max-width:90%;
      padding:1rem 2rem;
      border-radius:16px;
      background:linear-gradient(135deg,var(--accent-green) 0%,transparent 100%);
      position:relative;
      z-index:1;
    }

    html{scroll-behavior:smooth;}

    @media (max-width:768px){
      .animated-tagline{flex-direction:column;align-items:flex-start;gap:.5rem;}
      .word-carousel{min-width:200px;}
      .social-grid{grid-template-columns:1fr;}
    }
  </style>
</head>

<body>
  <!-- TITLE SECTION -->
  <section class="title-section">
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
    </div>
    <h1 class="project-title">FOUND</h1>
    <p class="project-subtitle">
      <span class="title-accent">Interpretar la Naturaleza</span> para Encontrar a Quienes nos Faltan
    </p>
  </section>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <div class="animated-tagline">
        <span id="hero-tagline-static">Using technology to&nbsp;</span>
        <div class="word-carousel" role="text" aria-label="Rotating tagline">
          <ul class="word-list">
            <li id="word-1">dignify.</li>
            <li id="word-2">remember.</li>
            <li id="word-3">search.</li>
            <li id="word-4">bring closure.</li>
          </ul>
        </div>
      </div>

      <p class="hero-description" id="hero-main-text">
        124,354 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
        <strong>FOUND</strong> combines technology with the knowledge of searching families to learn, locate, and drive systemic change.
      </p>

      <div class="hero-image-container skeleton">
        <img
          src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/NDAI5.gif?raw=true"
          alt="FOUND Project team using advanced technology in field search operations"
          class="hero-image loading"
          loading="lazy"
          onload="this.classList.remove('loading'); this.parentElement.classList.remove('skeleton')" />
      </div>
    </div>
  </section>

  <!-- COMMUNITY -->
  <section class="content-section" id="community">
    <div class="section-container">
      <h2 id="community-title">Driven by Families and Research Communities</h2>
      <p class="hero-description" id="community-text">
        FOUND is guided and motivated by <strong>search collectives</strong> and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
      </p>
    </div>
  </section>

 <!-- INSTITUTIONAL PARTNERSHIPS -->
<section class="content-section" id="collaborations">
  <div class="section-container">
    <h2 id="collab-title">Institutional Partnerships</h2>

    <div class="collab-wrap" aria-label="Institutional partnerships logos">
      <div class="collab-grid">

        <!-- 1. UN -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/1%20Executive%20Office%20of%20the%20UN%20Secretary-General.svg"
                 alt="Executive Office of the UN Secretary-General logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-1">Executive Office of the UN Secretary-General</div>
            <div class="collab-note" id="collab-note-1">International collaboration</div>
          </div>
        </div>

        <!-- 2. FCDO -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/2%20UK's%20Foreign%2C%20Commonwealth%20%26%20Development%20Office%20(FCDO).png"
                 alt="UK Foreign, Commonwealth & Development Office logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-2">UK Foreign, Commonwealth &amp; Development Office (FCDO)</div>
            <div class="collab-note" id="collab-note-2">Policy, funding, and partnerships</div>
          </div>
        </div>

        <!-- 3. CentroGeo -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/2%20logo_centrogeo_wide.svg"
                 alt="CentroGeo logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-3">CentroGeo</div>
            <div class="collab-note" id="collab-note-3">Co-lead, technical expertise</div>
          </div>
        </div>

        <!-- 4. University of Guadalajara -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/26bd52ce350828b22814cfedc872786dd43de672/images/580141488dfc53bfdbde59fa6b043438.jpg"
                 alt="University of Guadalajara logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-4">University of Guadalajara (UdeG)</div>
            <div class="collab-note" id="collab-note-4">Technical expertise, experimental sites</div>
          </div>
        </div>

        <!-- 5. Colombian Search Unit -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg"
                 alt="Colombian Search Unit logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-5">Colombian Search Unit (UBPD)</div>
            <div class="collab-note" id="collab-note-5">Casework and technical exchange</div>
          </div>
        </div>

        <!-- 6. Mexico National Search Commission -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/4%20Comision%20Nacional%20de%20Busqueda.png"
                 alt="Mexico National Search Commission logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-6">Mexico’s National Search Commission</div>
            <div class="collab-note" id="collab-note-6">National coordination</div>
          </div>
        </div>

      <!-- 7. Guerreros Buscadores -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b2323f813df618867a6227a87e7efb9e084fe75e/images/Final%20Guerreros%20Buscadores.png"
      alt="Guerreros Buscadores de Jalisco logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-7">Guerreros Buscadores de Jalisco</div>
    <div class="collab-note" id="collab-note-7">Families’ leadership and field expertise</div>
  </div>
</div>

        <!-- 8. British Embassy -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png"
                 alt="British Embassy Mexico City logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-8">British Embassy in Mexico City</div>
            <div class="collab-note" id="collab-note-8">Funding and coordination support</div>
          </div>
        </div>

        <!-- 9. Oxford Forum (OFOTA) -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/5ea7b61d8c5c6467ad4253f2898109033aac13e7/images/OFOTA_COLOUR_WEB.jpg"
                 alt="Oxford Festival of the Arts logo"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-9">Oxford Festival of the Arts</div>
            <div class="collab-note" id="collab-note-9">Oxford Forum partner</div>
          </div>
        </div>

        <!-- 10. Bath (Oxford Forum) -->
        <div class="collab-card">
          <div class="collab-logo">
            <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b2323f813df618867a6227a87e7efb9e084fe75e/images/Beth.jpg"
                 alt="University of Bath – Oxford Forum partner"
                 loading="lazy" class="loading" onload="this.classList.remove('loading')">
          </div>
          <div class="collab-meta">
            <div class="collab-name" id="collab-item-10">University of Bath</div>
            <div class="collab-note" id="collab-note-10">Technical expertise · Oxford Forum partner</div>
          </div>
        </div>

<!-- British Association for Forensic Anthropology -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/11%20logo%20BAFAlogo_orig.png"
      alt="British Association for Forensic Anthropology logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-bafa">British Association for Forensic Anthropology</div>
    <div class="collab-note" id="collab-note-bafa">Forensic expertise</div>
  </div>
</div>

<!-- Comisión de Búsqueda de Jalisco -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/3%20Comisio%CC%81n%20de%20Bu%CC%81squeda%20de%20Jalisco.png"
      alt="Comisión de Búsqueda de Jalisco logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-jalisco">Comisión de Búsqueda de Jalisco</div>
    <div class="collab-note" id="collab-note-jalisco">Technical expertise, coordination</div>
  </div>
</div>

<!-- University of Oxford -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/4%20logo%20oxford-university-logo.png"
      alt="University of Oxford logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-oxford">University of Oxford</div>
    <div class="collab-note" id="collab-note-oxford">Technical expertise</div>
  </div>
</div>

<!-- Mexico's Science and Technology Secretariat -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20Logotipo_SECIHTI_2025-2030.svg"
      alt="Mexico's Science and Technology Secretariat logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-secihti">Mexico’s Science and Technology Secretariat</div>
    <div class="collab-note" id="collab-note-secihti">Funding, policy impact</div>
  </div>
</div>

<!-- UNAM Geophysics -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20logo%20IGeofisicaUNAM.png"
      alt="UNAM Geophysics Institute logo"
      loading="lazy"
      onload="this.classList.remove('loading')"
      style="filter: brightness(0) invert(0);">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-unam-geo">UNAM – Geophysics</div>
    <div class="collab-note" id="collab-note-unam-geo">Technical expertise</div>
  </div>
</div>

<!-- UNAM Engineering -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/6%20logo%20Ingenieria%20UNAM.png"
      alt="UNAM Engineering logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-unam-eng">UNAM – Engineering</div>
    <div class="collab-note" id="collab-note-unam-eng">Technical expertise</div>
  </div>
</div>

<!-- Frontier Tech Hub -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4dc9341c21cbe08685242e48c8241a1a51ad3151/images/10%20logo%20FT%2Blogo_Primary%2Bversion_white%2Btext.png"
      alt="Frontier Tech Hub logo"
      loading="lazy"
      onload="this.classList.remove('loading')"
      style="filter: brightness(0) invert(0);">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-fth">Frontier Tech Hub</div>
    <div class="collab-note" id="collab-note-fth">Funding, technical expertise</div>
  </div>
</div>

<!-- DT Global -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20DTG_Logo_Screen_LRG-1.png"
      alt="DT Global logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-dtg">DT Global</div>
    <div class="collab-note" id="collab-note-dtg">Funding, technical expertise</div>
  </div>
</div>

<!-- UPZMG -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20logo%20UPZMG2.png"
      alt="UPZMG logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-upzmg">UPZMG</div>
    <div class="collab-note" id="collab-note-upzmg">Experimental site</div>
  </div>
</div>

<!-- UWE Bristol -->
<div class="collab-card">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/9%20logo%20UWE%20Bristol.svg"
      alt="UWE Bristol logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-uwe">UWE Bristol</div>
    <div class="collab-note" id="collab-note-uwe">Funding, technical expertise</div>
  </div>
</div>
        <!-- Remaining academic & funding partners can follow here -->

      </div>
    </div>
  </div>
</section>

  <!-- SOCIAL (3rd element fixed) -->
  <section class="social-section" id="social">
    <div class="social-container">
      <h2 class="section-title" id="social-title">Follow Our Journey</h2>
      <p class="section-subtitle" id="social-subtitle">Stay connected with our latest findings, community stories, and collaborations</p>

      <div class="social-grid">
        <div class="social-embed twitter-embed">
          <blockquote class="twitter-tweet">
            <p lang="en" dir="ltr">
              Almost a year after I started researching the story, I'm thrilled that my
              <a href="https://twitter.com/guardian?ref_src=twsrc%5Etfw">@guardian</a> article about the innovations being used to try and find some of the thousands of people who have disappeared in Mexico is the most read in its Global Development section.
              <a href="https://t.co/NztFCj4uEF">https://t.co/NztFCj4uEF</a>
            </p>
            &mdash; Suzanne Bearne (@sbearne)
            <a href="https://twitter.com/sbearne/status/1991827389375193330?ref_src=twsrc%5Etfw">November 21, 2025</a>
          </blockquote>
        </div>

        <div class="social-embed">
          <div class="iframe-container">
            <iframe
              src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7343552976185114624"
              height="924"
              width="504"
              frameborder="0"
              allowfullscreen
              title="FCDO LinkedIn post about FOUND Project"
              loading="lazy"></iframe>
          </div>
        </div>

        <!-- ✅ FIXED: your broken third iframe (missing quote + misplaced loading) -->
        <div class="social-embed">
          <div class="iframe-container">
            <iframe
              src="https://www.linkedin.com/embed/feed/update/urn:li:share:7407705201647845376"
              height="1170"
              width="504"
              frameborder="0"
              allowfullscreen
              title="FOUND Project LinkedIn update"
              loading="lazy"></iframe>
          </div>
        </div>

        <div class="social-embed">
          <div class="iframe-container">
            <iframe
              src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728"
              height="924"
              width="504"
              frameborder="0"
              allowfullscreen
              title="FOUND Project community engagement"
              loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-content">
      <em id="footer-text">FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
    </div>
  </footer>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

  <!-- LANGUAGE TOGGLE -->
  <script>
    (function() {
      const translations = {
        en: {
          'hero-tagline-static': 'Using technology to&nbsp;',
          'word-1': 'dignify.',
          'word-2': 'remember.',
          'word-3': 'search.',
          'word-4': 'bring closure.',
          'hero-main-text': '124,354 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> combines technology with the knowledge of searching families to learn, locate, and drive systemic change.',
          'community-title': 'Driven by Families and Research Communities',
          'community-text': 'FOUND is guided and motivated by <strong>search collectives</strong> and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.',
          'collab-title': 'Institutional Partnerships',
          'tech-title': 'Technologies in Action',
          'buscadoras-title': 'The Role of Buscadoras',
          'buscadoras-text': 'Women-led collectives are at the heart of FOUND\'s work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.',
          'social-title': 'Follow Our Journey',
          'social-subtitle': 'Stay connected with our latest findings, community stories, and collaborations',
          'partners-title': 'Our Partners',
          'partners-intro': 'FOUND brings together a coalition of academic institutions, government bodies, civil society organisations, and international partners. Together, we seek to honour the memory of those who are missing and stand with families as they search for a form of closure.',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        },
        es: {
          'hero-tagline-static': 'Usando tecnología para&nbsp;',
          'word-1': 'dignificar.',
          'word-2': 'recordar.',
          'word-3': 'buscar.',
          'word-4': 'dar cierre.',
          'hero-main-text': '124,354 personas están registradas como desaparecidas en México. Detrás de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> combina tecnología y saberes de familias buscadoras para buscar, localizar y promover cambios sistémicos.',
          'community-title': 'Impulsado por familias y comunidades de investigación',
          'community-text': 'FOUND está guiado e impulsado por <strong>colectivos de búsqueda</strong> y personas investigadoras de CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge y las Universidades Autónomas de Zacatecas y San Luis Potosí.',
          'collab-title': 'Alianzas institucionales',
          'tech-title': 'Tecnologías en acción',
          'buscadoras-title': 'El papel de las buscadoras',
          'buscadoras-text': 'Los colectivos de búsqueda están en el corazón del trabajo de FOUND. Estas familias han transformado la conversación nacional sobre desaparición y justicia. Sus prácticas de búsqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus métodos en nuestros esfuerzos tecnológicos.',
          'social-title': 'Sigue nuestro camino',
          'social-subtitle': 'Mantente al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.',
          'partners-title': 'Nuestras alianzas',
          'partners-intro': 'FOUND reúne una coalición de instituciones académicas, instancias gubernamentales, organizaciones de la sociedad civil y aliados internacionales. Trabajamos con un objetivo común: honrar la memoria de quienes nos faltan y acompañar a las familias en la búsqueda de una forma de cierre.',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        },
        nah: {
          'hero-tagline-static': 'Teknolojíayoh ika&nbsp;',
          'word-1': 'tlatepanita.',
          'word-2': 'quilnamictia.',
          'word-3': 'temoa.',
          'word-4': 'yolpakilistli quimacatia.',
          'hero-main-text': '124,354 tlācameh tlahcuilōlmeh quen polīhuihqueh ipan Mēxihco. Ipan sesen inin caso cah se familia tlatehuía tlanemilistli. <strong>FOUND</strong> quimixnextia teknolojíayoh huan tlamatiliztli in familias buscadoras para momachtia, quitemoa, quipantlalia huan quinemililia tlanemilistli yancuic ipan sistema.',
          'community-title': 'In familias huan tlamachtianimeh quinyecana',
          'community-text': 'FOUND quinyecanah huan quinyolchicahua <strong>colectivos de búsqueda</strong> huan tlamachtianimeh de CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge huan Universidades Autónomas de Zacatecas huan San Luis Potosí.',
          'collab-title': 'Tlen tlatlanecuiltilis nemilistli (alianzas institucionales)',
          'tech-title': 'Teknolojíayoh tlen motequiti',
          'buscadoras-title': 'In papel in buscadoras',
          'buscadoras-text': 'In colectivoh de buscadoras cah ipan yollotl in tequitl tlen FOUND. Yehuan quipatlaqueh in tlajtol ipan país tlen polihuiliztli huan tlayectlaliz justice. Inintequiti tlen temoa, tlen tlapanextia de inin nemilistli, mochihua se tlamatiliztli forense huecapan. FOUND quincaca, momachtia huan quincalaquia inintequiti ipan inin teknológicoh tequitl.',
          'social-title': 'Xiquito in totlanejmachtiliz',
          'social-subtitle': 'Ximoyetkixtia inin tlen tipantlaliah, tlen tlanechicoliztli in comunidades huan inin tlen timocoyonaltiah san sejco.',
          'partners-title': 'Tochan tlacamachtiloyan huan tocnihhuan',
          'partners-intro': 'FOUND quitlalia san sejco tlacamachtiloyan, tlatocayotl tlen gobierno, organizaciones de la sociedad civil huan tocnihhuan internacionales. San sejco titequitiyah para tlachihua tlatlepanittacayotl in aquin polihuihqueh huan para timochicahualtia in familias tlen quitemoah se tlayolpakilistli.',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        }
      };

      function setLanguage(lang) {
        const dict = translations[lang] || translations.en;
        Object.keys(dict).forEach(function(id) {
          const el = document.getElementById(id);
          if (el) el.innerHTML = dict[id];
        });

        document.documentElement.setAttribute('lang', lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en'));

        document.querySelectorAll('.lang-btn').forEach(function(btn) {
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        try { localStorage.setItem('found-lang', lang); } catch(e) {}
      }

      document.addEventListener('DOMContentLoaded', function() {
        let savedLang = null;
        try { savedLang = localStorage.getItem('found-lang'); } catch(e) {}
        const initialLang = (savedLang === 'es' || savedLang === 'en' || savedLang === 'nah') ? savedLang : 'en';
        setLanguage(initialLang);

        document.querySelectorAll('.lang-btn').forEach(function(btn) {
          btn.addEventListener('click', function() {
            setLanguage(btn.dataset.lang);
          });
        });
      });
    })();
  </script>
</body>
</html>
