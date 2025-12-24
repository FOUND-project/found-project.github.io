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
      position:relative;
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
      border-radius:10px;
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

    /* =========================================================
       ✅ ENHANCED DESIGN ONLY: TECHNOLOGIES + BUSCADORAS
       (Text unchanged; only layout/visual polish)
    ========================================================== */

    /* Technologies: featured panel + stronger layout rhythm */
    #technologies{
      background:
        radial-gradient(circle at 20% 15%, rgba(232,245,240,.75) 0%, transparent 52%),
        radial-gradient(circle at 80% 0%, rgba(212,175,55,.10) 0%, transparent 55%),
        linear-gradient(135deg,#f8fcfb 0%,#fff 60%);
      overflow:hidden;
    }

    #technologies::before{
      content:'';
      position:absolute;
      inset:-2px;
      background:
        linear-gradient(90deg, rgba(74,140,115,.12), transparent 35%, transparent 65%, rgba(74,140,115,.10));
      opacity:.6;
      pointer-events:none;
      mask-image:linear-gradient(to bottom, transparent, black 18%, black 82%, transparent);
      -webkit-mask-image:linear-gradient(to bottom, transparent, black 18%, black 82%, transparent);
    }

    #technologies .section-container{
      position:relative;
    }

    /* Tech list becomes a “card grid” feel without changing markup */
    #technologies .info-list{
      margin-top:1.75rem;
      gap:1rem 2rem;
    }

    #technologies .info-list li{
      background:rgba(255,255,255,.85);
      border:1px solid rgba(45,95,77,.10);
      box-shadow:var(--shadow-sm);
      padding:.9rem 1rem .9rem 2.45rem;
      backdrop-filter:blur(6px);
      transition:transform .3s var(--transition-smooth), box-shadow .3s var(--transition-smooth), border-color .3s var(--transition-smooth);
    }

    #technologies .info-list li:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-md);
      border-color:rgba(74,140,115,.45);
      padding-left:2.55rem; /* preserve your existing hover feel */
    }

    /* Gallery: masonry-ish feel, hover depth, consistent aspect */
    .image-gallery{
      margin-top:2.25rem;
      display:grid;
      grid-template-columns:repeat(12,1fr);
      gap:clamp(.75rem,1.4vw,1.15rem);
    }

    .gallery-item{
      border-radius:18px;
      overflow:hidden;
      box-shadow:var(--shadow-md);
      border:1px solid rgba(45,95,77,.10);
      background:linear-gradient(180deg, rgba(232,245,240,.35) 0%, rgba(255,255,255,.9) 100%);
      position:relative;
      transform:translateY(0);
      transition:transform .35s var(--transition-smooth), box-shadow .35s var(--transition-smooth);
      min-height:170px;
    }

    .gallery-item::after{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 20% 20%, rgba(212,175,55,.10) 0%, transparent 45%),
        linear-gradient(180deg, rgba(0,0,0,.05) 0%, transparent 45%);
      opacity:.0;
      transition:opacity .35s var(--transition-smooth);
      pointer-events:none;
    }

    .gallery-item:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
    }

    .gallery-item:hover::after{opacity:1;}

    .gallery-item img{
      width:100%;
      height:100%;
      object-fit:cover;
      display:block;
      transform:scale(1.01);
      transition:transform .6s var(--transition-smooth);
    }

    .gallery-item:hover img{transform:scale(1.06);}

    /* Responsive mosaic (no markup changes) */
    #technologies .image-gallery .gallery-item:nth-child(1){grid-column:span 4; min-height:220px;}
    #technologies .image-gallery .gallery-item:nth-child(2){grid-column:span 4; min-height:220px;}
    #technologies .image-gallery .gallery-item:nth-child(3){grid-column:span 4; min-height:220px;}
    #technologies .image-gallery .gallery-item:nth-child(4){grid-column:span 3;}
    #technologies .image-gallery .gallery-item:nth-child(5){grid-column:span 3;}
    #technologies .image-gallery .gallery-item:nth-child(6){grid-column:span 3;}
    #technologies .image-gallery .gallery-item:nth-child(7){grid-column:span 3;}
    #technologies .image-gallery .gallery-item:nth-child(8){grid-column:span 4; min-height:200px;}
    #technologies .image-gallery .gallery-item:nth-child(9){grid-column:span 4; min-height:200px;}
    #technologies .image-gallery .gallery-item:nth-child(10){grid-column:span 4; min-height:200px;}

    @media (max-width: 1100px){
      .image-gallery{grid-template-columns:repeat(6,1fr);}
      #technologies .image-gallery .gallery-item:nth-child(1),
      #technologies .image-gallery .gallery-item:nth-child(2),
      #technologies .image-gallery .gallery-item:nth-child(3){grid-column:span 6;}
      #technologies .image-gallery .gallery-item:nth-child(4),
      #technologies .image-gallery .gallery-item:nth-child(5),
      #technologies .image-gallery .gallery-item:nth-child(6),
      #technologies .image-gallery .gallery-item:nth-child(7){grid-column:span 3;}
      #technologies .image-gallery .gallery-item:nth-child(8),
      #technologies .image-gallery .gallery-item:nth-child(9),
      #technologies .image-gallery .gallery-item:nth-child(10){grid-column:span 6;}
    }

    @media (max-width: 700px){
      .image-gallery{grid-template-columns:repeat(2,1fr);}
      #technologies .image-gallery .gallery-item{grid-column:span 2; min-height:210px;}
    }

    /* Buscadoras: elegant “feature card” treatment */
    #buscadoras{
      position:relative;
      background:
        radial-gradient(circle at 15% 20%, rgba(212,175,55,.10) 0%, transparent 52%),
        radial-gradient(circle at 85% 0%, rgba(232,245,240,.55) 0%, transparent 60%),
        linear-gradient(135deg,#fff8f5 0%,#fff 55%);
      border-top:1px solid rgba(0,0,0,.04);
      border-bottom:1px solid rgba(0,0,0,.04);
    }

    #buscadoras::before{
      content:'';
      position:absolute;
      left:-120px;
      top:15%;
      width:320px;
      height:320px;
      background:radial-gradient(circle, rgba(74,140,115,.18) 0%, transparent 65%);
      filter:blur(2px);
      opacity:.55;
      pointer-events:none;
    }

    #buscadoras .buscadoras-content{
      background:rgba(255,255,255,.72);
      border:1px solid rgba(45,95,77,.12);
      border-radius:26px;
      box-shadow:var(--shadow-lg);
      padding:clamp(1.75rem,3vw,2.75rem);
      backdrop-filter:blur(10px);
      position:relative;
    }

    #buscadoras .buscadoras-content::after{
      content:'';
      position:absolute;
      inset:0;
      border-radius:26px;
      background:
        linear-gradient(135deg, rgba(232,245,240,.35) 0%, transparent 35%),
        radial-gradient(circle at 85% 15%, rgba(212,175,55,.10) 0%, transparent 55%);
      opacity:.9;
      pointer-events:none;
      z-index:0;
    }

    #buscadoras .buscadoras-content > *{
      position:relative;
      z-index:1;
    }

    #buscadoras .hero-description{
      margin-bottom:2rem; /* tighter rhythm */
    }

    #buscadoras .buscadoras-image{
      border-radius:24px;
      box-shadow:var(--shadow-lg);
      border:1px solid rgba(45,95,77,.12);
      overflow:hidden;
      margin:2.5rem auto 0;
      max-width:720px;
      position:relative;
      transform:translateY(0);
      transition:transform .35s var(--transition-smooth), box-shadow .35s var(--transition-smooth);
    }

    #buscadoras .buscadoras-image::before{
      content:'';
      position:absolute;
      inset:0;
      background:linear-gradient(180deg, rgba(0,0,0,.08) 0%, transparent 45%);
      opacity:.35;
      pointer-events:none;
      z-index:1;
    }

    #buscadoras .buscadoras-image:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
    }

    #buscadoras .buscadoras-image img{
      width:100%;
      height:auto;
      display:block;
      transform:scale(1.01);
      transition:transform .7s var(--transition-smooth);
    }

    #buscadoras .buscadoras-image:hover img{transform:scale(1.05);}

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

/* =========================================================
   Search Collectives – let GIF use all space above divider
   ========================================================= */

.collab-card-gif .collab-logo{
  padding: 0;            /* remove logo padding */
  min-height: 0;         /* remove reserved height */
  height: auto;
  display: block;
}

/* GIF hero fills entire logo area */
.collab-card-gif .gif-hero{
  height: 230px;         /* fills space above divider */
  overflow: hidden;
  background: #fff;
}

/* GIF itself */
.collab-card-gif .gif-hero img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 25%;   /* show more top */
  transform: scale(1.02);
  transition: transform .8s var(--transition-smooth);
}

.collab-card-gif:hover .gif-hero img{
  transform: scale(1.06);
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

/* =========================================================
   Override logo spacing ONLY for Search Collectives card
   ========================================================= */

.collab-card-gif .collab-logo{
  padding: 0;        /* remove default logo padding */
  min-height: 0;     /* remove forced logo height */
  height: auto;
  display: block;    /* disable flex centring */
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

    /* Buscadoras (base, retained; enhanced above with #buscadoras overrides) */
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
  
  /* =========================================================
   Search Collectives card – make GIF fill all space above divider
   ========================================================= */

.collab-card-gif .collab-logo{
  padding: 0 !important;
  min-height: 0 !important;
  height: 164px;              /* controls how tall the GIF area is */
  display: block;
  overflow: hidden;
  background: #fff;
}

/* Override the global logo image constraints for THIS card */
.collab-card-gif .collab-logo img{
  max-height: none !important; /* IMPORTANT: overrides the 95px cap */
  max-width: none !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center 25%; /* tweak this if needed */
  display: block;
  filter: none !important;
  transform: scale(1.02);
  transition: transform .8s var(--transition-smooth);
}

.collab-card-gif:hover .collab-logo img{
  transform: scale(1.06);
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

  <!-- Technologies Section (TEXT UNCHANGED) -->
  <section class="content-section" id="technologies">
    <div class="section-container">
      <h2 id="tech-title">Technologies in Action</h2>
      <ul class="info-list">
        <li id="tech-item-1">Multispectral &amp; Hyperspectral Imaging</li>
        <li id="tech-item-2">Airborne LiDAR</li>
        <li id="tech-item-3">Seismic Noise Interferometry (TIRSA)</li>
        <li id="tech-item-4">Electrical Resistivity Tomography, Conductivimetry Measurements</li>
        <li id="tech-item-5">Satellite Spectral Analysis</li>
        <li id="tech-item-6">Forensic Entomology, Botany, Territorial Analysis, Soil Science</li>
      </ul>

      <div class="image-gallery">
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/360.gif" alt="360 degree imaging technology in use" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.03.01.jpeg?raw=true" alt="Advanced field equipment setup" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/2.jpeg?raw=true" alt="Community collaboration in search efforts" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true" alt="Specialized search tools and equipment" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3.jpeg?raw=true" alt="Field research and data collection" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-07-30%20at%2021.40.57.jpeg?raw=true" alt="Team collaboration during field operations" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/6.jpg?raw=true" alt="Technology deployment in field" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/IMG-20231204-WA0038.jpg?raw=true" alt="Field operations and search activities" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-12-02%20at%2018.42.17.jpeg?raw=true" alt="Search team in action" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="gallery-item">
          <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/70206a6b5788f7204524bfdd4e1a6c365668b75d/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.44.jpeg" alt="Search methodology in practice" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
      </div>
    </div>
  </section>

  <!-- Buscadoras Section (TEXT UNCHANGED) -->
  <section class="buscadoras-section" id="buscadoras">
    <div class="buscadoras-content">
      <h2 id="buscadoras-title">The Role of Buscadoras</h2>
      <p class="hero-description" id="buscadoras-text">
        Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.
      </p>
      <div class="buscadoras-image">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolizing hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
      </div>
    </div>
  </section>

  <!-- INSTITUTIONAL PARTNERSHIPS -->
  <section class="content-section" id="collaborations">
    <div class="section-container">
      <h2 id="collab-title">Institutional Partnerships</h2>

      <div class="collab-wrap" aria-label="Institutional partnerships logos">
        <div class="collab-grid">

<!-- 7. Search Collectives -->
<div class="collab-card collab-card-gif">
  <div class="collab-logo">
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0bed7c6b4c906bc94116683368b679ba0bd80428/images/mothers%20walking.gif"
      alt="Search Collectives logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>
  <div class="collab-meta">
    <div class="collab-name" id="collab-item-7">Search Collectives</div>
    <div class="collab-note" id="collab-note-7">Leadership, field expertise</div>
  </div>
</div>

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
              <div class="collab-note" id="collab-note-2">Policy, Funding, Partnerships</div>
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
              <div class="collab-note" id="collab-note-3">Co-lead, Technical expertise</div>
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
              <div class="collab-note" id="collab-note-4">Technical expertise, Experimental sites</div>
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
              <div class="collab-note" id="collab-note-5">Casework, Technical exchange</div>
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

          <!-- 8. British Embassy -->
          <div class="collab-card">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png"
                   alt="British Embassy Mexico City logo"
                   loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-8">British Embassy in Mexico City</div>
              <div class="collab-note" id="collab-note-8">Funding, Coordination support</div>
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
              <div class="collab-note" id="collab-note-10">Technical expertise, Oxford Forum partner</div>
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
              <div class="collab-note" id="collab-note-jalisco">Technical expertise, Coordination</div>
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
              <div class="collab-note" id="collab-note-oxford">Co-lead, Technical expertise</div>
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
              <div class="collab-note" id="collab-note-secihti">Funding, Policy impact</div>
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
              <div class="collab-note" id="collab-note-fth">Funding, Technical expertise</div>
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
              <div class="collab-note" id="collab-note-dtg">Funding, Technical expertise</div>
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
              <div class="collab-note" id="collab-note-uwe">Funding, Technical expertise</div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

  <!-- SOCIAL -->
  <section class="social-section" id="social">
    <div class="social-container">
      <h2 class="section-title" id="social-title">Follow Our Journey</h2>
      <p class="section-subtitle" id="social-subtitle">Our latest findings, community stories, and collaborations</p>

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
