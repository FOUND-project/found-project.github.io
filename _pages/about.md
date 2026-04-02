---
permalink: /
title:
author_profile: false
classes: wide home-full
redirect_from:
  - /about/
  - /about.html
---

<html lang="en">
<head>
  <meta name="viewport" content="width=1200">
  <meta name="description" content="FOUND combines technology and grassroots knowledge to search for disappeared persons in Mexico, bringing dignity and closure to families." />
  <meta property="og:title" content="FOUND Project - Using Technology to Search and Remember" />
  <meta property="og:description" content="Over 130,000 persons are reported as disappeared in Mexico. Behind each case, there is a family searching for answers. FOUND works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change in how governments and institutions respond to disappearance." />
  <meta property="og:type" content="website" />
  <title>FOUND Project - Using Technology to Search and Remember</title>

  <meta http-equiv="Strict-Transport-Security" content="max-age=31536000; includeSubDomains; preload">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="DENY">
  <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..800;1,9..40,300..800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

  <script>
    (function() {
      if (window.location.protocol === 'http:' && 
          window.location.hostname === 'found-project.org' &&
          !sessionStorage.getItem('redirecting_to_https')) {
        sessionStorage.setItem('redirecting_to_https', 'true');
        var httpsUrl = 'https://found-project.org' + 
                      window.location.pathname + 
                      window.location.search + 
                      window.location.hash;
        window.location.replace(httpsUrl);
        setTimeout(function() {
          sessionStorage.removeItem('redirecting_to_https');
        }, 2000);
      } else {
        sessionStorage.removeItem('redirecting_to_https');
      }
    })();
  </script>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
    }

    :root{
      --primary-green:#2d5f4d;
      --dark-green:#1a3d30;
      --deep-green:#0e2a1f;
      --light-green:#4a8c73;
      --accent-green:#e8f5f0;
      --gold-accent:#c9a227;
      --gold-light:#f0e4b8;
      --gold-glow:rgba(201,162,39,.12);
      --text-dark:#0f1a16;
      --text-medium:#374840;
      --text-light:#5e7268;
      --bg-warm:#fafcfb;
      --bg-cream:#f7f9f8;
      --border-light:rgba(15,23,42,0.08);
      --border-green:rgba(45,95,77,.12);
      --shadow-xs:0 1px 3px rgba(15,23,42,.04);
      --shadow-sm:0 2px 8px rgba(15,23,42,.05);
      --shadow-md:0 8px 24px rgba(15,23,42,.08);
      --shadow-lg:0 16px 48px rgba(15,23,42,.10);
      --shadow-xl:0 24px 64px rgba(15,23,42,.14);
      --transition-smooth:cubic-bezier(.4,0,.2,1);
      --transition-bounce:cubic-bezier(.34,1.56,.64,1);
      --radius-xl:28px;
      --radius-lg:22px;
      --radius-md:16px;
      --radius-sm:12px;
      --radius-xs:8px;
      --font-display:'DM Serif Display', Georgia, 'Times New Roman', serif;
      --font-body:'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      --font-mono:'JetBrains Mono', 'SFMono-Regular', 'Consolas', monospace;
    }

    @media (prefers-reduced-motion: reduce){
      *,*::before,*::after{
        animation-duration:.01ms!important;
        animation-iteration-count:1!important;
        transition-duration:.01ms!important;
      }
      html{scroll-behavior:auto!important;}
      body.reveal-ready .reveal{opacity:1!important;transform:none!important;}
    }

    html{scroll-behavior:smooth;}

    body{
      font-family:var(--font-body);
      color:var(--text-dark);
      line-height:1.7;
      background:var(--bg-warm);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      overflow-x:hidden;
    }

    body.zoom-active{
      overflow:hidden;
    }

    /* Subtle topographic background */
    body::before{
      content:"";
      position:fixed;
      inset:0;
      z-index:-1;
      pointer-events:none;
      opacity:0.028;
      background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='600'%3E%3Cpath d='M300 50c138 0 250 112 250 250S438 550 300 550 50 438 50 300 162 50 300 50z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 90c116 0 210 94 210 210s-94 210-210 210S90 416 90 300 184 90 300 90z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 130c94 0 170 76 170 170s-76 170-170 170-170-76-170-170 76-170 170-170z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 170c72 0 130 58 130 130s-58 130-130 130-130-58-130-130 58-130 130-130z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 210c50 0 90 40 90 90s-40 90-90 90-90-40-90-90 40-90 90-90z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3C/svg%3E");
      background-size:600px 600px;
      transform:translateZ(0);
    }

    *:focus-visible{
      outline:3px solid rgba(74,140,115,.55);
      outline-offset:2px;
      border-radius:8px;
    }

    .page,
    #main,
    .initial-content,
    .page__inner-wrap,
    .page__content,
    .archive{
      max-width:none!important;
      width:106% !important;
    }

    .page__content{
      padding-left:clamp(1rem,4vw,3rem) !important;
      padding-right:clamp(1rem,4vw,3rem) !important;
    }

    /* =========================
       Scroll reveal animations
       Only activate AFTER JS adds .reveal-ready to body
       so content is always visible if JS fails
    ========================== */
    body.reveal-ready .reveal{
      opacity:0;
      transform:translateY(28px);
      transition:opacity .65s var(--transition-smooth), transform .65s var(--transition-smooth);
    }
    body.reveal-ready .reveal.is-visible{
      opacity:1;
      transform:translateY(0);
    }
    body.reveal-ready .reveal-delay-1{transition-delay:.1s}
    body.reveal-ready .reveal-delay-2{transition-delay:.2s}
    body.reveal-ready .reveal-delay-3{transition-delay:.3s}
    body.reveal-ready .reveal-delay-4{transition-delay:.4s}

    /* =========================
       Language toggle
    ========================== */
    .lang-toggle{
      position:absolute;
      top:1.6rem;
      right:clamp(1rem,4vw,3rem);
      display:inline-flex;
      gap:.4rem;
      z-index:3;
    }

    .lang-btn{
      border:1.5px solid rgba(255,255,255,.35);
      background:rgba(255,255,255,.08);
      color:rgba(255,255,255,.72);
      padding:.38rem .9rem;
      border-radius:999px;
      font-size:.78rem;
      font-weight:700;
      font-family:var(--font-mono);
      letter-spacing:.1em;
      text-transform:uppercase;
      cursor:pointer;
      backdrop-filter:blur(12px);
      transition:all .25s var(--transition-smooth);
    }

    .lang-btn:hover{
      background:rgba(255,255,255,.15);
      color:rgba(255,255,255,.95);
      border-color:rgba(255,255,255,.55);
      transform:translateY(-1px);
    }

    .lang-btn.active{
      background:rgba(255,255,255,.95);
      color:var(--deep-green);
      border-color:rgba(255,255,255,.95);
      box-shadow:0 4px 16px rgba(0,0,0,.15);
      transform:translateY(-1px);
    }

    /* =========================
       Title section
    ========================== */
    .title-section{
      padding:clamp(4rem,8vw,6.5rem) 0 clamp(2.5rem,5vw,4rem);
      background:
        radial-gradient(ellipse 1100px 600px at 10% 40%, rgba(201,162,39,.10) 0%, transparent 60%),
        radial-gradient(ellipse 900px 500px at 90% 20%, rgba(74,140,115,.08) 0%, transparent 55%),
        linear-gradient(165deg, #071a12 0%, #0e2a1f 25%, var(--dark-green) 55%, #1e4d3a 85%, #255e48 100%);
      position:relative;
      overflow:hidden;
      margin-bottom:0;
      isolation:isolate;
    }

    .title-section::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        repeating-linear-gradient(
          0deg,
          transparent,
          transparent 120px,
          rgba(255,255,255,.015) 120px,
          rgba(255,255,255,.015) 121px
        );
      pointer-events:none;
      z-index:0;
    }

    .title-section::after{
      content:'';
      position:absolute;
      left:50%;
      top:-180px;
      width:800px;
      height:800px;
      transform:translateX(-50%);
      background:radial-gradient(circle, rgba(255,255,255,.04) 0%, transparent 55%);
      pointer-events:none;
      z-index:0;
    }

    .title-inner{
      max-width:1200px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
      z-index:1;
      display:flex;
      flex-direction:column;
      align-items:center;
      gap:1.6rem;
    }

    .title-brand{
      display:flex;
      align-items:center;
      justify-content:center;
      flex-wrap:wrap;
      gap:1.3rem;
    }
    
    .project-logo{
      width:105px;
      height:auto;
      border-radius:20px;
      box-shadow:0 12px 40px rgba(0,0,0,.35);
      border:1.5px solid rgba(255,255,255,.55);
      background:rgba(255,255,255,.06);
      padding:8px;
      flex-shrink:0;
      transition:transform .4s var(--transition-smooth);
    }

    .project-logo:hover{
      transform:scale(1.04);
    }

    .project-title{
      font-size:clamp(3rem,7vw,5.5rem);
      font-weight:900;
      color:#fff;
      letter-spacing:.06em;
      line-height:1;
      font-family:var(--font-body);
      text-shadow:0 8px 32px rgba(0,0,0,.25);
    }

    .project-subtitle{
      font-size:clamp(1.15rem,2.5vw,1.55rem);
      font-weight:400;
      color:rgba(232,245,240,.75);
      font-family:var(--font-display);
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.6;
      max-width:820px;
      margin:0 auto;
      text-align:center;
      text-shadow:0 4px 16px rgba(0,0,0,.18);
      padding:0 clamp(1rem,4vw,3rem);
    }

    .title-accent{
      color:var(--gold-accent);
      font-weight:400;
    }

    /* Gold line under title */
    .title-divider{
      width:80px;
      height:2px;
      background:linear-gradient(90deg, transparent, var(--gold-accent), transparent);
      border:none;
      margin:.2rem auto 0;
      opacity:.6;
    }

    /* =========================
       Hero
    ========================== */
    .hero{
      padding:clamp(2.5rem,5vw,4rem) 0 clamp(1.5rem,3vw,2.5rem);
      position:relative;
      overflow:hidden;
      background:var(--bg-warm);
    }

    .title-section,
    .hero{
      background-color:transparent;
    }

    .hero::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(ellipse 800px 400px at 8% 15%, rgba(232,245,240,.55) 0%, transparent 55%),
        radial-gradient(ellipse 600px 350px at 92% 5%, var(--gold-glow) 0%, transparent 55%),
        linear-gradient(180deg, var(--bg-warm) 0%, #fff 100%);
      z-index:0;
    }

    .hero-content{
      position:relative;
      z-index:1;
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    .hero-top{
      display:grid;
      grid-template-columns: minmax(0,1.15fr) minmax(0,.85fr);
      gap:clamp(2rem,4vw,3.5rem);
      align-items:start;
    }

    .hero-text{
      display:flex;
      flex-direction:column;
      gap:1.25rem;
      max-width:720px;
    }

    .animated-tagline{
      font-size:clamp(2rem,4.5vw,3.2rem);
      font-weight:900;
      display:flex;
      align-items:flex-start;
      color:var(--dark-green);
      flex-wrap:wrap;
      gap:.75rem;
      letter-spacing:-.02em;
      line-height:1.1;
    }

    .tagline-pill{
      display:inline-flex;
      flex-direction:column;
      align-items:flex-start;
      justify-content:flex-start;
      padding:.85rem 1.6rem;
      border-radius:var(--radius-xl);
      background:linear-gradient(145deg, #fff 0%, var(--accent-green) 100%);
      border:1.5px solid rgba(45,95,77,.12);
      box-shadow:var(--shadow-md), inset 0 1px 0 rgba(255,255,255,.8);
      white-space:normal;
    }

    .tagline-pill span#hero-tagline-static{
      display:block;
      width:100%;
      font-size:clamp(1.85rem,4vw,2.8rem);
      font-weight:800;
      color:var(--dark-green);
      letter-spacing:-.02em;
      line-height:1.15;
      text-align:left;
      font-family:var(--font-body);
    }

    .word-carousel{
      margin-top:.25rem;
      width:100%;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:1.3em;
    }

    .hero-word{
      display:block;
      font-size:clamp(1.8rem,4vw,2.65rem);
      font-weight:800;
      letter-spacing:-.01em;
      color:var(--light-green);
      white-space:nowrap;
      text-align:center;
      transition:opacity .3s ease, transform .3s ease;
      opacity:1;
      transform:translateY(0);
      font-family:var(--font-display);
      font-style:italic;
    }

    .hero-word.fading-out{
      opacity:0;
      transform:translateY(-8px);
    }

    .hero-word.fading-in{
      opacity:0;
      transform:translateY(8px);
    }

    .hero-description{
      font-size:clamp(1.02rem,2.2vw,1.15rem);
      color:var(--text-medium);
      max-width:900px;
      line-height:1.85;
      font-weight:400;
    }

    .hero-description strong{
      color:var(--primary-green);
      font-weight:700;
    }

    .hero-side{
      display:flex;
      flex-direction:column;
      gap:1rem;
      align-items:stretch;
      min-height:100%;
    }

    /* ==========================
       Award highlight
    =========================== */
    .award-highlight{
      margin-top:0;
    }

    .award-card{
      display:flex;
      flex-wrap:wrap;
      align-items:flex-start;
      gap:1rem;
      padding:1.4rem 1.6rem;
      border-radius:var(--radius-lg);
      background:
        linear-gradient(145deg, #fffcf2 0%, #fff 60%);
      border:1.5px solid rgba(201,162,39,.25);
      box-shadow:var(--shadow-md);
      text-decoration:none;
      color:var(--text-dark);
      position:relative;
      overflow:hidden;
      transition:all .35s var(--transition-smooth);
    }

    .award-card::before{
      content:'';
      position:absolute;
      top:0;
      left:0;
      right:0;
      height:3px;
      background:linear-gradient(90deg, var(--gold-accent), rgba(201,162,39,.3), var(--gold-accent));
      opacity:.7;
    }

    .award-card:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(201,162,39,.45);
    }

    .award-text{
      flex:1 1 220px;
      position:relative;
      z-index:1;
    }

    .award-pill{
      display:inline-flex;
      align-items:center;
      gap:.4rem;
      padding:.2rem .7rem;
      border-radius:999px;
      font-size:.72rem;
      font-weight:700;
      letter-spacing:.14em;
      text-transform:uppercase;
      background:rgba(201,162,39,.10);
      color:var(--gold-accent);
      border:1px solid rgba(201,162,39,.22);
      margin-bottom:.55rem;
      font-family:var(--font-mono);
    }

    .award-pill::before{
      content:'';
      width:5px;
      height:5px;
      border-radius:50%;
      background:var(--gold-accent);
    }

    .award-title{
      font-size:clamp(1.05rem,2vw,1.2rem);
      font-weight:700;
      letter-spacing:-.01em;
      color:var(--dark-green);
      margin-bottom:.35rem;
      line-height:1.4;
      font-family:var(--font-body);
    }

    .award-title span.arrow{
      display:inline-block;
      font-size:.9rem;
      transform:translateX(0);
      transition:transform .25s var(--transition-smooth);
    }

    .award-card:hover .award-title span.arrow{
      transform:translateX(5px);
    }

    .award-meta{
      font-size:.88rem;
      color:var(--text-light);
      line-height:1.5;
    }

    /* =========================
       Hero team bar
    ========================== */
    .hero-team-bar{
      position:relative;
      z-index:1;
      margin-top:clamp(1.5rem,3vw,2.5rem);
      padding:clamp(.85rem,1.5vw,1.15rem) clamp(1rem,4vw,3rem);
      background:var(--deep-green);
      border-top:1px solid rgba(74,140,115,.18);
      border-bottom:1px solid rgba(74,140,115,.08);
    }

    .hero-team-bar-inner{
      max-width:1400px;
      margin:0 auto;
      display:flex;
      flex-wrap:wrap;
      align-items:baseline;
      gap:.4rem 1rem;
      font-size:clamp(.78rem,1.5vw,.88rem);
      color:rgba(232,245,240,.65);
      font-family:var(--font-mono);
      line-height:1.7;
    }

    .htb-label{
      color:var(--gold-accent);
      font-weight:700;
      letter-spacing:.04em;
      white-space:nowrap;
      flex-shrink:0;
    }

    .htb-brace{
      color:rgba(74,140,115,.7);
      font-weight:400;
    }

    .htb-divider{
      color:rgba(74,140,115,.4);
      font-size:1rem;
      flex-shrink:0;
    }

    .htb-text{
      font-family:var(--font-body);
      font-size:clamp(.82rem,1.5vw,.9rem);
      color:rgba(232,245,240,.68);
      letter-spacing:.01em;
    }

    .htb-text strong{
      color:rgba(232,245,240,.92);
      font-weight:650;
    }

    /* =========================
       Generic sections
    ========================== */
    .content-section{
      padding:clamp(3rem,6vw,5rem) 0;
      position:relative;
      scroll-margin-top:2rem;
    }

    .section-container{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    /* Section divider line */
    .section-divider{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    .section-divider hr{
      border:none;
      height:1px;
      background:linear-gradient(90deg, transparent, var(--border-green), rgba(201,162,39,.1), var(--border-green), transparent);
    }

    h2{
      font-size:clamp(1.75rem,3.5vw,2.5rem);
      font-weight:400;
      font-family:var(--font-display);
      color:var(--dark-green);
      margin-bottom:1.5rem;
      letter-spacing:0;
      position:relative;
      padding-bottom:1.1rem;
      line-height:1.3;
    }

    h2::after{
      content:'';
      position:absolute;
      bottom:0;
      left:0;
      width:60px;
      height:2.5px;
      background:linear-gradient(90deg,var(--gold-accent), rgba(201,162,39,.2));
      border-radius:999px;
    }

    /* =========================
       Technologies & Buscadoras
    ========================== */
    .dual-sections-grid{
      display:grid;
      grid-template-columns:minmax(0,1.1fr) minmax(0,0.9fr);
      gap:clamp(2rem,4vw,3rem);
      align-items:stretch;
    }

    .dual-column{
      min-width:0;
    }

    #technologies{
      background:#fff;
      border-radius:var(--radius-xl);
      padding:clamp(2rem,3.5vw,3rem);
      border:1px solid var(--border-green);
      box-shadow:var(--shadow-md);
      position:relative;
      overflow:hidden;
    }

    #technologies::before{
      content:'';
      position:absolute;
      top:0;
      left:0;
      right:0;
      height:3px;
      background:linear-gradient(90deg, var(--light-green), var(--primary-green), var(--light-green));
      opacity:.5;
    }

    .info-list{
      list-style:none;
      padding-left:0;
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));
      gap:.85rem 1.25rem;
      margin-top:1.4rem;
    }

    .info-list li{
      padding:.8rem 1rem .8rem 2.8rem;
      position:relative;
      color:var(--text-medium);
      font-size:clamp(.94rem,2vw,1rem);
      min-height:46px;
      display:flex;
      align-items:center;
      line-height:1.5;
      border-radius:var(--radius-sm);
      background:var(--bg-cream);
      border:1px solid var(--border-green);
      transition:all .3s var(--transition-smooth);
    }

    .info-list li::before{
      content:"";
      position:absolute;
      left:.85rem;
      top:50%;
      transform:translateY(-50%);
      width:22px;
      height:22px;
      border-radius:50%;
      background:var(--accent-green);
      border:1.5px solid rgba(74,140,115,.25);
      display:flex;
      align-items:center;
      justify-content:center;
      transition:all .3s var(--transition-smooth);
    }

    .info-list li::after{
      content:"✓";
      position:absolute;
      left:.85rem;
      top:50%;
      transform:translateY(-50%);
      width:22px;
      height:22px;
      display:flex;
      align-items:center;
      justify-content:center;
      color:var(--primary-green);
      font-weight:800;
      font-size:.72rem;
      transition:all .3s var(--transition-smooth);
    }

    .info-list li:hover{
      color:var(--dark-green);
      transform:translateX(4px);
      border-color:rgba(74,140,115,.3);
      background:#fff;
      box-shadow:var(--shadow-sm);
    }

    .info-list li:hover::before{
      background:var(--primary-green);
      border-color:var(--primary-green);
    }
    .info-list li:hover::after{
      color:#fff;
    }

    .image-gallery{
      margin-top:2.25rem;
      display:grid;
      grid-template-columns:repeat(12,1fr);
      gap:clamp(.6rem,1vw,.85rem);
    }

    .gallery-item{
      grid-column:span 3;
      border-radius:var(--radius-md);
      overflow:hidden;
      box-shadow:var(--shadow-sm);
      border:1px solid var(--border-green);
      background:#fff;
      position:relative;
      transform:translateY(0);
      transition:all .4s var(--transition-smooth);
      aspect-ratio:4/3;
      min-height:0;
    }

    .gallery-item img{
      width:100%;
      height:100%;
      object-fit:cover;
      display:block;
      transform:scale(1.02);
      transition:transform .6s var(--transition-smooth), opacity .4s ease;
    }

    .gallery-item img.loading{
      opacity:0;
    }

    .gallery-item:hover{
      transform:translateY(-5px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.3);
    }

    .gallery-item:hover img{
      transform:scale(1.08);
    }

    .buscadoras-section{
      background:#fff;
      border-radius:var(--radius-xl);
      padding:clamp(2rem,3.5vw,3rem);
      border:1px solid var(--border-green);
      box-shadow:var(--shadow-md);
      position:relative;
      overflow:hidden;
      display:flex;
      align-items:stretch;
    }

    .buscadoras-section::before{
      content:'';
      position:absolute;
      top:0;
      left:0;
      right:0;
      height:3px;
      background:linear-gradient(90deg, rgba(201,162,39,.4), var(--gold-accent), rgba(201,162,39,.4));
      opacity:.5;
    }

    .buscadoras-content{
      max-width:100%;
      margin:0 auto;
      text-align:center;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
    }

    .buscadoras-text{
      font-size:clamp(1rem,2vw,1.1rem);
      color:var(--text-medium);
      line-height:1.85;
      margin-top:.6rem;
    }

    .buscadoras-image{
      border-radius:var(--radius-lg);
      box-shadow:var(--shadow-md);
      border:1px solid var(--border-green);
      overflow:hidden;
      margin:2rem auto .1rem;
      max-width:520px;
      position:relative;
      transform:translateY(0);
      transition:all .4s var(--transition-smooth);
      background:#fff;
    }

    .buscadoras-image img{
      width:100%;
      height:auto;
      display:block;
      transform:scale(1.02);
      transition:transform .6s var(--transition-smooth), opacity .4s ease;
    }

    .buscadoras-image img.loading{
      opacity:0;
    }

    .buscadoras-image:hover{
      transform:translateY(-5px);
      box-shadow:var(--shadow-lg);
    }

    .buscadoras-image:hover img{
      transform:scale(1.06);
    }

    /* =========================
       Institutional partnerships
    ========================== */
    .collab-wrap{
      margin-top:2rem;
    }

    .collab-grid{
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(min(100%,240px),1fr));
      gap:clamp(1rem,2vw,1.5rem);
      margin-top:1.5rem;
    }

    .collab-card{
      background:#fff;
      border-radius:var(--radius-md);
      box-shadow:var(--shadow-sm);
      border:1px solid var(--border-green);
      overflow:hidden;
      position:relative;
      transition:all .35s var(--transition-smooth);
      min-height:210px;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
    }

    .collab-card:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.35);
    }

    .collab-logo{
      padding:1.1rem 1.1rem .6rem;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:130px;
      position:relative;
    }

    .collab-logo img{
      max-width:100%;
      max-height:90px;
      width:auto;
      height:auto;
      object-fit:contain;
      filter:grayscale(30%) brightness(1.05);
      transition:all .35s var(--transition-smooth);
    }

    .collab-img{
      max-height:80px;
      width:auto;
      object-fit:contain;
      filter:drop-shadow(0 0 1px rgba(0,0,0,.18));
    }
                
    .collab-logo img.loading{
      opacity:0;
    }

    .collab-card:hover .collab-logo img{
      filter:grayscale(0%) brightness(1);
      transform:scale(1.03);
    }

    .collab-meta{
      padding:.75rem 1.1rem 1rem;
      border-top:1px solid rgba(0,0,0,.05);
      background:var(--bg-cream);
    }

    .collab-name{
      font-weight:700;
      color:var(--dark-green);
      font-size:.95rem;
      line-height:1.35;
      letter-spacing:-.01em;
    }

    .collab-note{
      margin-top:.3rem;
      color:var(--text-light);
      font-size:.85rem;
      line-height:1.45;
    }

    .collab-card-gif .collab-logo{
      padding:0 !important;
      min-height:0 !important;
      height:160px;
      display:block;
      overflow:hidden;
      background:#fff;
    }

    .collab-card-gif .collab-logo img{
      max-height:none !important;
      max-width:none !important;
      width:100% !important;
      height:100% !important;
      object-fit:cover !important;
      object-position:center 25%;
      display:block;
      filter:none !important;
      transform:scale(1.02);
      transition:transform .7s var(--transition-smooth), opacity .4s ease;
    }

    .collab-card-gif .collab-logo img.loading{
      opacity:0;
    }

    .collab-card-gif:hover .collab-logo img{
      transform:scale(1.06);
    }

    /* =========================
       Social
    ========================== */
    .social-section{
      background:#fff;
      padding:clamp(3.5rem,6vw,5.5rem) 0;
      margin:0;
      position:relative;
      overflow:hidden;
    }

    .social-section::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(ellipse 900px 500px at 20% 0%, rgba(232,245,240,.5) 0%, transparent 55%);
      pointer-events:none;
    }

    .social-container{
      max-width:1600px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
    }

    .section-title{
      font-size:clamp(1.85rem,4vw,2.8rem);
      font-weight:400;
      font-family:var(--font-display);
      color:var(--dark-green);
      margin-bottom:.8rem;
      text-align:center;
      letter-spacing:0;
      line-height:1.2;
    }

    .section-subtitle{
      font-size:clamp(1rem,2.2vw,1.15rem);
      color:var(--text-light);
      text-align:center;
      margin-bottom:3rem;
      max-width:700px;
      margin-left:auto;
      margin-right:auto;
      line-height:1.7;
    }

    .social-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));
      gap:clamp(1.25rem,2.5vw,2rem);
      align-items:start;
    }

    .social-embed{
      background:var(--bg-cream);
      border-radius:var(--radius-lg);
      padding:1.15rem;
      box-shadow:var(--shadow-md);
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:420px;
      border:1px solid var(--border-green);
      overflow:hidden;
      position:relative;
      transition:all .35s var(--transition-smooth);
    }

    .social-embed:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.3);
    }

    .iframe-container{
      position:relative;
      width:100%;
      max-width:560px;
      overflow:hidden;
      border-radius:var(--radius-sm);
      border:1px solid rgba(15,23,42,.06);
      box-shadow:var(--shadow-sm);
    }

    .iframe-container iframe{
      width:100%;
      border:0;
      display:block;
      height:880px;
    }

    /* =========================
       Footer
    ========================== */
    .footer{
      text-align:center;
      padding:clamp(4rem,7vw,6rem) 0;
      margin-top:0;
      background:var(--deep-green);
      position:relative;
      overflow:hidden;
    }

    .footer::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(ellipse 800px 400px at 50% 0%, rgba(74,140,115,.10) 0%, transparent 60%);
      pointer-events:none;
    }

    .footer-content{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
    }

    .footer em{
      font-size:clamp(1.15rem,2.5vw,1.45rem);
      color:rgba(232,245,240,.85);
      font-weight:400;
      font-family:var(--font-display);
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.65;
      display:inline-block;
      max-width:100%;
    }

    .footer-line{
      width:60px;
      height:1.5px;
      background:linear-gradient(90deg, transparent, rgba(201,162,39,.5), transparent);
      border:none;
      margin:1.5rem auto 0;
    }

    /* =========================
       Touch zoom
    ========================== */
    @media (max-width:768px){
      .touch-zoomable{
        cursor:zoom-in;
      }

      .touch-zoomable.is-expanded{
        position:fixed;
        inset:0;
        margin:0 !important;
        width:100vw !important;
        height:100vh !important;
        max-width:none !important;
        max-height:none !important;
        z-index:9999;
        background:rgba(0,0,0,.92);
        border-radius:0 !important;
        box-shadow:none !important;
        padding:0 !important;
        display:flex;
        align-items:center;
        justify-content:center;
      }

      .touch-zoomable.is-expanded img,
      .touch-zoomable.is-expanded .hero-image{
        width:100%;
        height:100%;
        object-fit:contain;
        transform:none !important;
        box-shadow:none !important;
      }
    }

    /* =========================
       Responsive
    ========================== */
    @media (max-width:1100px){
      .image-gallery{
        grid-template-columns:repeat(6,1fr);
      }
      .gallery-item{
        grid-column:span 3;
      }
    }

    @media (max-width:900px){
      .dual-sections-grid{
        grid-template-columns:1fr;
      }
      .hero-top{
        grid-template-columns:1fr;
      }
      .hero-side{
        max-width:520px;
        margin:0 auto;
      }
    }

    @media (max-width:768px){
      .page,
      #main,
      .initial-content,
      .page__inner-wrap,
      .page__content,
      .archive{
        width:100% !important;
      }

      .lang-toggle{
        top:1rem;
      }

      .hero{
        padding:1.5rem 0 2rem;
      }

      .hero-text{
        max-width:100%;
      }

      .animated-tagline{
        flex-direction:column;
        align-items:center;
        gap:.45rem;
      }

      .tagline-pill{
        padding:.6rem 1.1rem;
        max-width:100%;
        align-items:center;
        text-align:center;
      }

      .tagline-pill span#hero-tagline-static{
        font-size:clamp(1.5rem,5.5vw,1.9rem);
        text-align:center;
      }

      .hero-word{
        font-size:clamp(1.6rem,5.5vw,2rem);
      }

      .award-card{
        padding:1.1rem 1.2rem;
      }

      .image-gallery{
        grid-template-columns:repeat(2,1fr);
      }

      .gallery-item{
        grid-column:span 2;
        aspect-ratio:16/10;
        max-height:160px;
      }

      .buscadoras-image{
        max-width:100%;
        margin-top:1.2rem;
      }

      .collab-card{
        min-height:auto;
      }

      .collab-logo{
        min-height:70px;
        padding:.7rem;
      }

      .collab-logo img{
        max-height:60px;
      }

      .collab-meta{
        padding:.6rem .8rem .8rem;
      }

      .collab-name{
        font-size:.92rem;
      }

      .collab-note{
        font-size:.82rem;
      }

      .social-grid{
        grid-template-columns:1fr;
      }

      .social-embed{
        min-height:auto;
      }

      .iframe-container iframe{
        height:520px;
      }

      .project-logo{
        width:78px;
      }
    }

    @media (max-width:480px){
      .gallery-item{
        max-height:140px;
      }
      .iframe-container iframe{
        height:430px;
      }
    }

    /* Re-tint logos to dark */
    .collab-img.fth{
      filter: brightness(0) saturate(100%) invert(9%) sepia(6%)
              saturate(512%) hue-rotate(94deg)
              brightness(95%) contrast(96%);
    }
        
    .collab-img.labco{
      filter: brightness(0) saturate(100%) invert(9%) sepia(6%)
              saturate(512%) hue-rotate(94deg)
              brightness(95%) contrast(96%);
    }

    /* =========================
       GIF Strip
    ========================== */
    .gif-strip{
      padding:clamp(1.5rem,3vw,2.5rem) 0 0;
      position:relative;
      overflow:hidden;
      background:var(--bg-cream);
      isolation:isolate;
    }

    .gif-strip-inner{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
      z-index:1;
      display:grid;
      grid-template-columns: 1.55fr 1fr 1fr;
      gap:clamp(.55rem,1.1vw,.85rem);
      align-items:stretch;
    }

    .gs-panel{
      border-radius:var(--radius-md);
      overflow:hidden;
      border:1px solid var(--border-green);
      box-shadow:var(--shadow-md);
      position:relative;
      background:#fff;
      transform:translateY(0);
      transition:all .4s var(--transition-smooth);
    }

    .gs-panel-main { aspect-ratio:16/9; }
    .gs-panel-side { aspect-ratio:4/3; }

    .gs-panel::before{
      content:attr(data-label);
      position:absolute;
      bottom:.6rem;
      left:.6rem;
      z-index:2;
      font-size:.68rem;
      font-weight:600;
      letter-spacing:.08em;
      text-transform:uppercase;
      color:#fff;
      background:rgba(14,40,30,.7);
      backdrop-filter:blur(10px);
      padding:.2rem .6rem;
      border-radius:999px;
      border:1px solid rgba(255,255,255,.15);
      opacity:0;
      transform:translateY(4px);
      transition:opacity .3s ease, transform .3s ease;
      pointer-events:none;
      font-family:var(--font-mono);
      font-size:.62rem;
    }

    .gs-panel:hover::before{
      opacity:1;
      transform:translateY(0);
    }

    .gs-panel:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
    }

    .gs-panel img{
      position:absolute;
      inset:0;
      width:100%;
      height:100%;
      object-fit:cover;
      display:block;
      transform:scale(1.02);
      transition:transform .7s var(--transition-smooth), opacity .4s ease;
    }

    .gs-panel img.loading{ opacity:0; }
    .gs-panel:hover img{ transform:scale(1.06); }

    .gs-panel-side::after{
      content:'';
      position:absolute;
      top:.5rem;
      right:.5rem;
      width:7px;
      height:7px;
      background:var(--gold-accent);
      border-radius:50%;
      box-shadow:0 0 0 2px rgba(255,255,255,.5);
      animation:livePulse 2.2s ease-in-out infinite;
      z-index:2;
    }

    @keyframes livePulse{
      0%,100%{ opacity:1; transform:scale(1); }
      50%    { opacity:.5; transform:scale(1.4); }
    }

    /* GIF Strip Caption Bar */
    .gif-strip-caption {
      position: relative;
      z-index: 2;
      margin: clamp(.55rem,1.1vw,.8rem) 0 0;
      padding: clamp(.6rem, 1.2vw, .85rem) clamp(1rem, 4vw, 3rem);
      background: var(--deep-green);
      border-top: 1px solid rgba(74, 140, 115, .18);
    }

    .gif-caption-inner {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: .5rem 1rem;
      font-size: clamp(.76rem, 1.4vw, .85rem);
      color: rgba(232, 245, 240, .65);
      font-family: var(--font-mono);
      line-height: 1.65;
    }

    .gif-caption-tag {
      color: var(--gold-accent);
      font-weight: 700;
      letter-spacing: .04em;
      font-size: clamp(.78rem, 1.5vw, .88rem);
      white-space: nowrap;
    }

    .gif-caption-brace {
      color: rgba(74, 140, 115, .7);
      font-weight: 400;
    }

    .gif-caption-divider {
      color: rgba(74, 140, 115, .4);
      font-size: 1rem;
      font-family: inherit;
      flex-shrink: 0;
    }

    .gif-caption-item {
      font-family: var(--font-body);
      font-size: clamp(.78rem, 1.4vw, .85rem);
      color: rgba(232, 245, 240, .62);
      letter-spacing: .01em;
    }

    .gif-caption-item strong {
      color: rgba(232, 245, 240, .9);
      font-weight: 650;
    }

    @media (max-width:700px){
      .gif-strip-inner{ grid-template-columns:1fr; }
      .gs-panel-main, .gs-panel-side{ aspect-ratio:16/9; }
    }
    @media (min-width:701px) and (max-width:1050px){
      .gif-strip-inner{ grid-template-columns:1fr 1fr; grid-template-rows:auto auto; }
      .gs-panel-main{ grid-column:1; grid-row:1/3; aspect-ratio:unset; min-height:220px; }
      .gs-panel-side:nth-child(2){ grid-column:2; grid-row:1; }
      .gs-panel-side:nth-child(3){ grid-column:2; grid-row:2; }
    }

    /* =========================
       Stats ribbon 
    ========================== */
    .stats-ribbon{
      padding:clamp(1.5rem,3vw,2.2rem) 0;
      background:var(--bg-warm);
      position:relative;
    }
    .stats-ribbon-inner{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      display:flex;
      justify-content:center;
      gap:clamp(2rem,5vw,5rem);
      flex-wrap:wrap;
    }
    .stat-item{
      text-align:center;
      min-width:140px;
    }
    .stat-number{
      font-size:clamp(2rem,4vw,3rem);
      font-weight:800;
      color:var(--dark-green);
      font-family:var(--font-body);
      letter-spacing:-.03em;
      line-height:1.1;
    }
    .stat-number .stat-plus{
      color:var(--gold-accent);
      font-weight:700;
    }
    .stat-label{
      font-size:clamp(.78rem,1.5vw,.88rem);
      color:var(--text-light);
      margin-top:.3rem;
      letter-spacing:.03em;
      text-transform:uppercase;
      font-weight:600;
      font-family:var(--font-mono);
      font-size:.72rem;
    }
    .stat-divider{
      width:1px;
      background:linear-gradient(180deg, transparent, var(--border-green), transparent);
      align-self:stretch;
    }

    @media (max-width:600px){
      .stats-ribbon-inner{ gap:1.5rem 2rem; }
      .stat-divider{ display:none; }
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

    <div class="title-inner">
      <div class="title-brand">
        <img
          src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9466ebc27c9487e8bfbff1d1dd904f4f9e6df81d/images/logo_FOUND_white.png"
          alt="FOUND logo"
          class="project-logo"
        />
        <h1 class="project-title">FOUND</h1>
      </div>
      <hr class="title-divider" />
      <p class="project-subtitle" id="project-subtitle">
        <span class="title-accent">Interpretar la Naturaleza</span> para Encontrar a Quienes nos Faltan
      </p>
    </div>
  </section>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-top">
        <div class="hero-text reveal">
          <div class="animated-tagline">
            <div class="tagline-pill" aria-label="FOUND tagline">
              <span id="hero-tagline-static">Using technology to</span>
              <div class="word-carousel" role="text">
                <span id="hero-word" class="hero-word">search.</span>
              </div>
            </div>
          </div>

          <p class="hero-description" id="hero-main-text">
            Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
            <strong>FOUND</strong> builds the scientific and institutional capabilities needed to find and return missing persons to their families. Working at the intersection of frontier technology and the lived knowledge of search groups, we drive systemic change in how governments and institutions respond to disappearance.
          </p>
        </div>

        <div class="hero-side reveal reveal-delay-2">
          <div class="award-highlight">
            <a href="/news/#mariela-award" class="award-card">
              <div class="award-text">
                <div class="award-pill">Award</div>
                <div class="award-title">
                  FOUND recognised with the Sir Nicholas Browne Policy and Expertise Award
                  <span class="arrow">&#x2197;</span>
                </div>
                <div class="award-meta">
                  Selected from over 200 nominations across the UK Foreign, Commonwealth &amp; Development Office.
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Team bar -->
    <div class="hero-team-bar">
      <div class="hero-team-bar-inner">
        <span class="htb-label">FOUND<span class="htb-brace">{</span>Team<span class="htb-brace">}</span></span>
        <span class="htb-divider">·</span>
        <span class="htb-text" id="hero-team-text">Our core team brings together <strong>collectives of families from Jalisco, Zacatecas, and Colombia searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco's Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico's National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.</span>
      </div>
    </div>
  </section>

  <!-- GIF STRIP -->
  <section class="gif-strip" aria-label="FOUND in action">
    <div class="gif-strip-inner">
      <div class="gs-panel gs-panel-main touch-zoomable" data-label="Spectral indices · substance detection">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/1047db9c85ff842e083e9fb45c0bdf05213da88a/images/NDAI5.gif"
             alt="FOUND Project team using advanced technology in field search operations"
             loading="lazy" class="loading" onload="this.classList.remove('loading')" />
      </div>

      <div class="gs-panel gs-panel-side touch-zoomable" data-label="Satellite analysis · time series">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/33b2627b6b245e9632f59abf0a02f5ad58956bf4/images/Areas_de_busqueda_3.gif"
             alt="Satellite spectral time-series analysis of search areas"
             loading="lazy" class="loading" onload="this.classList.remove('loading')" />
      </div>

      <div class="gs-panel gs-panel-side touch-zoomable" data-label="Clandestine space detection">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9b9df755f7129ba10ee53479d528d42d14e5648a/images/ClandestineSpace.gif"
             alt="Spectral detection of clandestine sites using satellite imagery"
             loading="lazy" class="loading" onload="this.classList.remove('loading')" />
      </div>
    </div>

    <div class="gif-strip-caption">
      <div class="gif-caption-inner">
        <span class="gif-caption-tag">Platforms<span class="gif-caption-brace">{</span>core member: CentroGeo<span class="gif-caption-brace">}</span></span>
        <span class="gif-caption-divider">·</span>
        <span class="gif-caption-item"><strong>Spectral indices</strong> — Identifying substances linked to disappearances via satellite and drone imagery, and when they were present.</span>
        <span class="gif-caption-divider">·</span>
        <span class="gif-caption-item"><strong>Clandestine sites location</strong> — AI that finds what was meant to stay hidden.</span>
      </div>
    </div>
  </section>

  <!-- STATS RIBBON -->
  <section class="stats-ribbon reveal" aria-label="Key statistics">
    <div class="stats-ribbon-inner">
      <div class="stat-item">
        <div class="stat-number" id="stat-num-1">130,000<span class="stat-plus">+</span></div>
        <div class="stat-label" id="stat-label-1">Persons disappeared</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-number" id="stat-num-2">7<span class="stat-plus">+</span></div>
        <div class="stat-label" id="stat-label-2">Technologies deployed</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-number" id="stat-num-3">20<span class="stat-plus">+</span></div>
        <div class="stat-label" id="stat-label-3">Institutional partners</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-number" id="stat-num-4">3</div>
        <div class="stat-label" id="stat-label-4">Countries</div>
      </div>
    </div>
  </section>

  <!-- TECHNOLOGIES + BUSCADORAS -->
  <section class="content-section">
    <div class="section-container dual-sections-grid">
      <div class="dual-column reveal">
        <section id="technologies">
          <h2 id="tech-title">Technologies in Action</h2>
          <ul class="info-list">
            <li id="tech-item-1">Multispectral &amp; Hyperspectral Imaging</li>
            <li id="tech-item-2">Airborne LiDAR</li>
            <li id="tech-item-3">Seismic Noise Interferometry (TIRSA)</li>
            <li id="tech-item-4">Electrical Resistivity Tomography, Conductivimetry</li>
            <li id="tech-item-5">Satellite Spectral Analysis</li>
            <li id="tech-item-ml">Machine Learning</li>
            <li id="tech-item-6">Forensic Entomology, Botany, Territorial Analysis, Soil Science</li>
          </ul>

          <div class="image-gallery">
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/360.gif" alt="360 degree imaging technology in use" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.03.01.jpeg?raw=true" alt="Advanced field equipment setup" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/2.jpeg?raw=true" alt="Community collaboration in search efforts" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true" alt="Specialised search tools and equipment" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3.jpeg?raw=true" alt="Field research and data collection" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-07-30%20at%2021.40.57.jpeg?raw=true" alt="Team collaboration during field operations" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/c88e3807678629fcd59ad91baff20b6ec7a34f66/images/layers.jpg?raw=true"
                   alt="Technology deployment in field"
                   loading="lazy"
                   class="loading"
                   onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/IMG-20231204-WA0038.jpg?raw=true" alt="Field operations and search activities" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-12-02%20at%2018.42.17.jpeg?raw=true" alt="Search team in action" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/70206a6b5788f7204524bfdd4e1a6c365668b75d/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.44.jpeg" alt="Search methodology in practice" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/51a35a3f1915699b8fe9835270ddfe6f3c5c0946/images/hyperspectral%20from%20presentation.png?raw=true"
                   alt="Hyperspectral analysis output used in FOUND field validation"
                   loading="lazy"
                   class="loading"
                   onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/51a35a3f1915699b8fe9835270ddfe6f3c5c0946/images/pigs_aerial.jpg?raw=true"
                   alt="Aerial view of experimental calibration site using animal proxies"
                   loading="lazy"
                   class="loading"
                   onload="this.classList.remove('loading')">
            </div>  
          </div>
        </section>
      </div>

      <div class="dual-column reveal reveal-delay-2">
        <section class="buscadoras-section" id="buscadoras">
          <div class="buscadoras-content">
            <div>
              <h2 id="buscadoras-title">The Role of Buscadoras</h2>
              <p class="buscadoras-text hero-description" id="buscadoras-text">
                Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice.
                Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and
                incorporates their methods into our technological efforts.
              </p>
            </div>
            <div class="buscadoras-image touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolising hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
          </div>
        </section>
      </div>
    </div>
  </section>

  <!-- DIVIDER -->
  <div class="section-divider"><hr/></div>

  <!-- INSTITUTIONAL PARTNERSHIPS -->
  <section class="content-section" id="collaborations">
    <div class="section-container">
      <h2 id="collab-title" class="reveal">Institutional Partnerships</h2>

      <div class="collab-wrap reveal" aria-label="Institutional partnerships logos">
        <div class="collab-grid">

          <div class="collab-card collab-card-gif touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0bed7c6b4c906bc94116683368b679ba0bd80428/images/mothers%20walking.gif"
                alt="Search Collectives" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-7">Search Collectives</div>
              <div class="collab-note" id="collab-note-7">Leadership, field expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/1%20Executive%20Office%20of%20the%20UN%20Secretary-General.svg"
                alt="Executive Office of the UN Secretary-General" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-1">Executive Office of the UN Secretary-General</div>
              <div class="collab-note" id="collab-note-1">International collaboration</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/bd3ef3bd33596258b2738274017f51a2e2c05186/images/FCDO_logo_960x640.png"
                alt="UK Foreign, Commonwealth & Development Office" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-2">UK Foreign, Commonwealth &amp; Development Office (FCDO)</div>
              <div class="collab-note" id="collab-note-2">Policy, Funding, Partnerships</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/2%20logo_centrogeo_wide.svg"
                alt="CentroGeo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-3">CentroGeo</div>
              <div class="collab-note" id="collab-note-3">Co-lead, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/26bd52ce350828b22814cfedc872786dd43de672/images/580141488dfc53bfdbde59fa6b043438.jpg"
                alt="University of Guadalajara" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-4">University of Guadalajara (UdeG)</div>
              <div class="collab-note" id="collab-note-4">Technical expertise, Experimental sites</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg"
                alt="Colombian Search Unit" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-5">Colombian Search Unit (UBPD)</div>
              <div class="collab-note" id="collab-note-5">Casework, Technical exchange</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/4%20Comision%20Nacional%20de%20Busqueda.png"
                alt="Mexico National Search Commission" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-6">Mexico's National Search Commission</div>
              <div class="collab-note" id="collab-note-6">National coordination</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png"
                alt="British Embassy Mexico City" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-8">British Embassy in Mexico City</div>
              <div class="collab-note" id="collab-note-8">Funding, Coordination support</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/5ea7b61d8c5c6467ad4253f2898109033aac13e7/images/OFOTA_COLOUR_WEB.jpg"
                alt="Oxford Festival of the Arts" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-9">Oxford Festival of the Arts</div>
              <div class="collab-note" id="collab-note-9">Oxford Forum partner</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b2323f813df618867a6227a87e7efb9e084fe75e/images/Beth.jpg"
                alt="University of Bath" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-10">University of Bath</div>
              <div class="collab-note" id="collab-note-10">Technical expertise, Oxford Forum partner</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/11%20logo%20BAFAlogo_orig.png"
                alt="British Association for Forensic Anthropology" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-bafa">British Association for Forensic Anthropology</div>
              <div class="collab-note" id="collab-note-bafa">Forensic expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/3%20Comisio%CC%81n%20de%20Bu%CC%81squeda%20de%20Jalisco.png"
                alt="Comisión de Búsqueda de Jalisco" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-jalisco">Comisión de Búsqueda de Jalisco</div>
              <div class="collab-note" id="collab-note-jalisco">Technical expertise, Coordination</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/4%20logo%20oxford-university-logo.png"
                alt="University of Oxford" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-oxford">University of Oxford</div>
              <div class="collab-note" id="collab-note-oxford">Co-lead, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20Logotipo_SECIHTI_2025-2030.svg"
                alt="Mexico's Science and Technology Secretariat" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-secihti">Mexico's Science and Technology Secretariat</div>
              <div class="collab-note" id="collab-note-secihti">Funding, Policy impact</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20logo%20IGeofisicaUNAM.png"
                alt="UNAM Geophysics Institute" loading="lazy" onload="this.classList.remove('loading')"
                style="filter: brightness(0) invert(0);">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-unam-geo">UNAM – Geophysics</div>
              <div class="collab-note" id="collab-note-unam-geo">Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/6%20logo%20Ingenieria%20UNAM.png"
                alt="UNAM Engineering" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-unam-eng">UNAM – Engineering</div>
              <div class="collab-note" id="collab-note-unam-eng">Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/master/images/10%20logo%20FT%2Blogo_Primary%2Bversion_white%2Btext.png"
                alt="Frontier Tech Hub" loading="lazy" class="collab-img fth">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-fth">Frontier Tech Hub</div>
              <div class="collab-note" id="collab-note-fth">Funding, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20DTG_Logo_Screen_LRG-1.png"
                alt="DT Global" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-dtg">DT Global</div>
              <div class="collab-note" id="collab-note-dtg">Funding, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20logo%20UPZMG2.png"
                alt="UPZMG" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-upzmg">UPZMG</div>
              <div class="collab-note" id="collab-note-upzmg">Experimental site</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/9%20logo%20UWE%20Bristol.svg"
                alt="UWE Bristol" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-uwe">UWE Bristol</div>
              <div class="collab-note" id="collab-note-uwe">Funding, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d47bacb6b575270e7b5453c8ebc5b13bcec70a2f/images/dark-non-retina-labco.png"
                alt="LABCO" loading="lazy" class="collab-img labco">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-labco">LABCO</div>
              <div class="collab-note" id="collab-note-labco">Exploring AI together to locate and identify</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/82b303cdf26fa6a25e9845ff0d5fc10e070d94e6/images/logo_eaaf_rd.png?raw=true"
                alt="Argentine Forensic Anthropology Team (EAAF)" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-eaaf">Argentine Forensic Anthropology Team (EAAF)</div>
              <div class="collab-note" id="collab-note-eaaf">Luis Fondebrider, FOUND's advisor</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/a8209a23c303b55bda756d5a55b2c572ac2540a9/images/ori_logo_square_2024_150_inverted.png"
                alt="Oxford Robotics Institute" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-ori">Oxford Robotics Institute</div>
              <div class="collab-note" id="collab-note-ori">Partnership, technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b9419b5a0b9d80c6ae96d16642771d6c1d66cdf3/images/logo-ipn-guinda.svg"
                alt="Instituto Politécnico Nacional" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-ipn">Instituto Politécnico Nacional</div>
              <div class="collab-note" id="collab-note-ipn">Technical expertise, Technology</div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

  <!-- DIVIDER -->
  <div class="section-divider"><hr/></div>

  <!-- SOCIAL -->
  <section class="social-section" id="social">
    <div class="social-container">
      <h2 class="section-title reveal" id="social-title">Follow Our Journey</h2>
      <p class="section-subtitle reveal reveal-delay-1" id="social-subtitle">
        Our latest findings, community stories, and collaborations
      </p>

      <div class="social-grid reveal reveal-delay-2">
        <div class="social-embed">
          <div class="iframe-container">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7405294962692595712"
              height="880" width="504" frameborder="0" allowfullscreen
              title="FOUND Project LinkedIn update" loading="lazy"></iframe>
          </div>
        </div>

        <div class="social-embed twitter-embed">
          <div class="iframe-container">
            <blockquote class="twitter-tweet">
              <p lang="en" dir="ltr">
                Almost a year after I started researching the story, I'm thrilled that my
                <a href="https://twitter.com/guardian?ref_src=twsrc%5Etfw">@guardian</a>
                article about the innovations being used to try and find some of the thousands
                of people who have disappeared in Mexico is the most read in its Global Development section.
                <a href="https://t.co/NztFCj4uEF">https://t.co/NztFCj4uEF</a>
              </p>
              &mdash; Suzanne Bearne (@sbearne)
              <a href="https://twitter.com/sbearne/status/1991827389375193330?ref_src=twsrc%5Etfw">November 21, 2025</a>
            </blockquote>
          </div>
        </div>

        <div class="social-embed twitter-embed">
          <div class="iframe-container">
            <blockquote class="twitter-tweet">
              <p lang="es" dir="ltr">
                Cómo los cerdos y los insectos están ayudando a encontrar a los desaparecidos en México
                <a href="https://t.co/sJC3oaNLGL">https://t.co/sJC3oaNLGL</a>
              </p>
              &mdash; BBC News Mundo (@bbcmundo)
              <a href="https://twitter.com/bbcmundo/status/1973352689867063513?ref_src=twsrc%5Etfw">October 1, 2025</a>
            </blockquote>
          </div>
        </div>

        <div class="social-embed">
          <div class="iframe-container">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728"
              height="880" width="504" frameborder="0" allowfullscreen
              title="FOUND Project community engagement" loading="lazy"></iframe>
          </div>
        </div>

        <div class="social-embed">
          <div class="iframe-container">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7343552976185114624"
              height="880" width="504" frameborder="0" allowfullscreen
              title="FCDO LinkedIn post about FOUND Project" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-content">
      <em id="footer-text">FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
      <hr class="footer-line" />
    </div>
  </footer>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

  <script>
    (function(){
      /* ===========================
         TRANSLATIONS
      ============================ */
      const translations = {
        en:{
          'collab-item-labco':'LABCO',
          'collab-note-labco':'Exploring AI together to locate and identify',
          'collab-item-eaaf':'Argentine Forensic Anthropology Team (EAAF)',
          'collab-note-eaaf':"Luis Fondebrider, FOUND's advisor",
          'collab-item-ori':'Oxford Robotics Institute',
          'collab-note-ori':'Partnership, technical expertise',
          'collab-item-ipn':'Instituto Polit\u00e9cnico Nacional',
          'collab-note-ipn':'Technical expertise, Technology',
          'project-subtitle':'<span class="title-accent">Technologies</span> To Locate Those Who We Are Missing',
          'hero-tagline-static':'Using technology to',
          'word-1':'search.',
          'word-2':'remember.',
          'word-3':'dignify.',
          'word-4':'find.',
          'word-5':'bring closure.',
          'hero-main-text':'Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change in how governments and institutions respond to disappearance.',
          'hero-team-text':'Our core team brings together <strong>collectives of families from Jalisco and Zacatecas searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco\'s Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico\'s National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.',
          'collab-title':'Institutional Partnerships',
          'tech-title':'Technologies in Action',
          'tech-item-1':'Multispectral &amp; Hyperspectral Imaging',
          'tech-item-2':'Airborne LiDAR',
          'tech-item-3':'Seismic Noise Interferometry (TIRSA)',
          'tech-item-4':'Electrical Resistivity Tomography, Conductivimetry',
          'tech-item-5':'Satellite Spectral Analysis',
          'tech-item-ml':'Machine Learning',
          'tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science',
          'buscadoras-title':'The Role of Buscadoras',
          'buscadoras-text':"Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.",
          'social-title':'Follow Our Journey',
          'social-subtitle':'Stay connected with our latest findings, community stories, and collaborations',
          'footer-text':'FOUND: Tecnolog\u00edas para Encontrar a Quienes nos Faltan.',
          'stat-label-1':'Persons disappeared',
          'stat-label-2':'Technologies deployed',
          'stat-label-3':'Institutional partners',
          'stat-label-4':'Countries',
          'collab-item-7':'Search Collectives',
          'collab-note-7':'Leadership, field expertise',
          'collab-item-1':'Executive Office of the UN Secretary-General',
          'collab-note-1':'International collaboration',
          'collab-item-2':'UK Foreign, Commonwealth &amp; Development Office (FCDO)',
          'collab-note-2':'Policy, Funding, Partnerships',
          'collab-item-3':'CentroGeo',
          'collab-note-3':'Co-lead, Technical expertise',
          'collab-item-4':'University of Guadalajara (UdeG)',
          'collab-note-4':'Technical expertise, Experimental sites',
          'collab-item-5':'Colombian Search Unit (UBPD)',
          'collab-note-5':'Casework, Technical exchange',
          'collab-item-6':"Mexico's National Search Commission",
          'collab-note-6':'National coordination',
          'collab-item-8':'British Embassy in Mexico City',
          'collab-note-8':'Funding, Coordination support',
          'collab-item-9':'Oxford Festival of the Arts',
          'collab-note-9':'Oxford Forum partner',
          'collab-item-10':'University of Bath',
          'collab-note-10':'Technical expertise, Oxford Forum partner',
          'collab-item-bafa':'British Association for Forensic Anthropology',
          'collab-note-bafa':'Forensic expertise',
          'collab-item-jalisco':'Comisi\u00f3n de B\u00fasqueda de Jalisco',
          'collab-note-jalisco':'Technical expertise, Coordination',
          'collab-item-oxford':'University of Oxford',
          'collab-note-oxford':'Co-lead, Technical expertise',
          'collab-item-secihti':"Mexico's Science and Technology Secretariat",
          'collab-note-secihti':'Funding, Policy impact',
          'collab-item-unam-geo':'UNAM \u2013 Geophysics',
          'collab-note-unam-geo':'Technical expertise',
          'collab-item-unam-eng':'UNAM \u2013 Engineering',
          'collab-note-unam-eng':'Technical expertise',
          'collab-item-fth':'Frontier Tech Hub',
          'collab-note-fth':'Funding, Technical expertise',
          'collab-item-dtg':'DT Global',
          'collab-note-dtg':'Funding, Technical expertise',
          'collab-item-upzmg':'UPZMG',
          'collab-note-upzmg':'Experimental site',
          'collab-item-uwe':'UWE Bristol',
          'collab-note-uwe':'Funding, Technical expertise'
        },
        es:{
          'collab-item-labco':'LABCO',
          'collab-note-labco':'Explorando juntos el uso de IA para localizar e identificar',
          'collab-item-eaaf':'Equipo Argentino de Antropolog\u00eda Forense (EAAF)',
          'collab-note-eaaf':'Luis Fondebrider, asesor de FOUND',
          'collab-item-ori':'Oxford Robotics Institute',
          'collab-note-ori':'Alianza, experiencia t\u00e9cnica',
          'collab-item-ipn':'Instituto Polit\u00e9cnico Nacional',
          'collab-note-ipn':'Experiencia t\u00e9cnica, desarrollo tecnol\u00f3gico',
          'project-subtitle':'<span class="title-accent">Tecnolog\u00edas</span> para Encontrar a Quienes nos Faltan',
          'hero-tagline-static':'Usando tecnolog\u00eda para',
          'word-1':'buscar.',
          'word-2':'recordar.',
          'word-3':'dignificar.',
          'word-4':'encontrar.',
          'word-5':'dar cierre.',
          'hero-main-text':'M\u00e1s de 130,000 personas est\u00e1n registradas como desaparecidas en M\u00e9xico. Detr\u00e1s de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> combina tecnolog\u00eda y saberes de familias buscadoras para aprender del campo, localizar y promover cambios sist\u00e9micos.',
          'hero-team-text':'Nuestro equipo central re\u00fane <strong>colectivos de familias de Jalisco y Zacatecas que buscan a sus seres queridos desaparecidos</strong>, junto a CentroGeo, la Universidad de Oxford, la Comisi\u00f3n de B\u00fasqueda de Jalisco, la Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) y la Universidad de Guadalajara. Trabajamos junto a socios estrat\u00e9gicos, entre ellos la Oficina para Asuntos Exteriores, de la Commonwealth y de Desarrollo del Reino Unido (FCDO), la Oficina Ejecutiva del Secretario General de la ONU, la Unidad de B\u00fasqueda de Personas dadas por Desaparecidas (UBPD) de Colombia, la Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico, LAB-Co y Luis Fondebrider.',
          'collab-title':'Alianzas institucionales',
          'tech-title':'Tecnolog\u00edas en acci\u00f3n',
          'tech-item-1':'Im\u00e1genes multiespectrales e hiperespectrales',
          'tech-item-2':'LiDAR aerotransportado',
          'tech-item-3':'Interferometr\u00eda de ruido s\u00edsmico (TIRSA)',
          'tech-item-4':'Tomograf\u00eda de resistividad el\u00e9ctrica y mediciones de conductividad',
          'tech-item-5':'An\u00e1lisis espectral satelital',
          'tech-item-ml':'Aprendizaje autom\u00e1tico',
          'tech-item-6':'Entomolog\u00eda forense, bot\u00e1nica, an\u00e1lisis territorial y ciencia del suelo',
          'buscadoras-title':'El papel de las buscadoras',
          'buscadoras-text':'Los colectivos liderados por mujeres est\u00e1n en el coraz\u00f3n del trabajo de FOUND. Han transformado la conversaci\u00f3n nacional sobre desaparici\u00f3n y justicia. Sus pr\u00e1cticas de b\u00fasqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus m\u00e9todos en nuestros esfuerzos tecnol\u00f3gicos.',
          'social-title':'Sigue nuestro camino',
          'social-subtitle':'Mant\u00e9nte al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.',
          'footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.',
          'stat-label-1':'Personas desaparecidas',
          'stat-label-2':'Tecnolog\u00edas desplegadas',
          'stat-label-3':'Socios institucionales',
          'stat-label-4':'Pa\u00edses',
          'collab-item-7':'Colectivos de B\u00fasqueda',
          'collab-note-7':'Liderazgo, experiencia en campo',
          'collab-item-1':'Oficina Ejecutiva del Secretario General de la ONU',
          'collab-note-1':'Colaboraci\u00f3n internacional',
          'collab-item-2':'Oficina para Asuntos Exteriores, de la Commonwealth y de Desarrollo del Reino Unido (FCDO)',
          'collab-note-2':'Pol\u00edtica, financiamiento, alianzas',
          'collab-item-3':'CentroGeo',
          'collab-note-3':'Co-l\u00edder, experiencia t\u00e9cnica',
          'collab-item-4':'Universidad de Guadalajara (UdeG)',
          'collab-note-4':'Experiencia t\u00e9cnica, sitios experimentales',
          'collab-item-5':'Unidad de B\u00fasqueda de Colombia (UBPD)',
          'collab-note-5':'Casos, intercambio t\u00e9cnico',
          'collab-item-6':'Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico',
          'collab-note-6':'Coordinaci\u00f3n nacional',
          'collab-item-8':'Embajada Brit\u00e1nica en la Ciudad de M\u00e9xico',
          'collab-note-8':'Financiamiento, coordinaci\u00f3n',
          'collab-item-9':'Oxford Festival of the Arts',
          'collab-note-9':'Socio del Foro de Oxford',
          'collab-item-10':'University of Bath',
          'collab-note-10':'Experiencia t\u00e9cnica, socio del Foro de Oxford',
          'collab-item-bafa':'British Association for Forensic Anthropology',
          'collab-note-bafa':'Experiencia forense',
          'collab-item-jalisco':'Comisi\u00f3n de B\u00fasqueda de Jalisco',
          'collab-note-jalisco':'Experiencia t\u00e9cnica, coordinaci\u00f3n',
          'collab-item-oxford':'Universidad de Oxford',
          'collab-note-oxford':'Co-l\u00edder, experiencia t\u00e9cnica',
          'collab-item-secihti':'Secretar\u00eda de Ciencia y Tecnolog\u00eda de M\u00e9xico',
          'collab-note-secihti':'Financiamiento, impacto en pol\u00edticas',
          'collab-item-unam-geo':'UNAM \u2013 Geof\u00edsica',
          'collab-note-unam-geo':'Experiencia t\u00e9cnica',
          'collab-item-unam-eng':'UNAM \u2013 Ingenier\u00eda',
          'collab-note-unam-eng':'Experiencia t\u00e9cnica',
          'collab-item-fth':'Frontier Tech Hub',
          'collab-note-fth':'Financiamiento, experiencia t\u00e9cnica',
          'collab-item-dtg':'DT Global',
          'collab-note-dtg':'Financiamiento, experiencia t\u00e9cnica',
          'collab-item-upzmg':'UPZMG',
          'collab-note-upzmg':'Sitio experimental',
          'collab-item-uwe':'UWE Bristol',
          'collab-note-uwe':'Financiamiento, experiencia t\u00e9cnica'
        },
        nah:{
          'collab-item-labco':'LABCO',
          'collab-note-labco':'Timoitayoh ika IA para titemoa huan tiquixmati',
          'collab-item-eaaf':'Equipo Argentino de Antropolog\u00eda Forense (EAAF)',
          'collab-note-eaaf':'Luis Fondebrider, ixcuitlali (asesor) FOUND',
          'collab-item-ori':'Oxford Robotics Institute',
          'collab-note-ori':'Tlaneltiliztli (alianza), teknikoh tlamatiliztli',
          'collab-item-ipn':'Instituto Polit\u00e9cnico Nacional',
          'collab-note-ipn':'Teknikoh tlamatiliztli, teknoloj\u00edayoh tlatequipanoliztli',
          'project-subtitle':'<span class="title-accent">Tecnolog\u00edas</span> para Encontrar a Quienes nos Faltan',
          'hero-tagline-static':'Teknoloj\u00edayoh ika',
          'word-1':'temoa.',
          'word-2':'quilnamictia.',
          'word-3':'tlatepanita.',
          'word-4':'quipantlalia.',
          'word-5':'yolpakilistli quimacatia.',
          'hero-main-text':'124,354 tl\u0101cameh tlahcuil\u014dlmeh quen pol\u012bhuihqueh ipan M\u0113xihco. Ipan sesen inin caso cah se familia tlatehu\u00eda tlanemilistli. <strong>FOUND</strong> quimixnextia tehnolog\u00edayoh huan tlamatiliztli in familias buscadoras para momachtia, quitemoa, quipantlalia huan quinemililia yancuic tlanemilistli ipan sistema.',
          'hero-team-text':'In totequitlacauh quinnechicoa <strong>in colectivoh in familias tlen Jalisco huan Zacatecas tlen quitemoa in inpilhuan polihqueh</strong>, oc nochi CentroGeo, in Universidad de Oxford, in Comisi\u00f3n de B\u00fasqueda de Jalisco, in Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) huan in Universidad de Guadalajara. Timoitayoh ika in tlaneltililmeh tlen FCDO, in Oficina Ejecutiva del Secretario General de la ONU, UBPD, in Comisi\u00f3n Nacional de B\u00fasqueda, LAB-Co huan Luis Fondebrider.',
          'collab-title':'Alianzas institucionales',
          'tech-title':'Teknoloj\u00edayoh tlen motequiti',
          'tech-item-1':'Multispectral &amp; Hyperspectral Imaging',
          'tech-item-2':'Airborne LiDAR',
          'tech-item-3':'Seismic Noise Interferometry (TIRSA)',
          'tech-item-4':'Electrical Resistivity Tomography, Conductivimetry',
          'tech-item-5':'Satellite Spectral Analysis',
          'tech-item-ml':'Machine Learning',
          'tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science',
          'buscadoras-title':'In papel in buscadoras',
          'buscadoras-text':'In colectivoh de buscadoras cah ipan yollotl in tequitl tlen FOUND. Yehuan quipatlaqueh in tlajtol ipan pa\u00eds tlen polihuiliztli huan tlayectlaliz (justicia). Inintequiti tlen temoa, tlen tlapanextia de inin nemilistli, mochihua se tlamatiliztli forense huecapan. FOUND quincaca, momachtia huan quincalaquia inintequiti ipan inin teknol\u00f3gicoh tequitl.',
          'social-title':'Xiquito in totlanejmachtiliz',
          'social-subtitle':'Ximoyetkixtia inin tlen tipantlaliah, tlen tlanechicoliztli in comunidades huan inin tlen timocoyonaltiah san sejco.',
          'footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.',
          'stat-label-1':'Tl\u0101cameh pol\u012bhuihqueh',
          'stat-label-2':'Teknoloj\u00edayoh',
          'stat-label-3':'Tlaneltililmeh',
          'stat-label-4':'Tl\u0101ltlameh',
          'collab-item-7':'Colectivoh de B\u00fasqueda',
          'collab-note-7':'Teyacanaliztli, tlamatiliztli ipan tlalli',
          'collab-item-1':'Oficina Ejecutiva del Secretario General de la ONU',
          'collab-note-1':'Internacional tlapalewiliztli',
          'collab-item-2':'FCDO (Reino Unido)',
          'collab-note-2':'Pol\u00edtica, tomin, tlaneltiliztli',
          'collab-item-3':'CentroGeo',
          'collab-note-3':'Co-teyacanani, teknikoh tlamatiliztli',
          'collab-item-4':'Universidad de Guadalajara (UdeG)',
          'collab-note-4':'Teknikoh tlamatiliztli, sitios experimentales',
          'collab-item-5':'UBPD (Colombia)',
          'collab-note-5':'Casos, intercambio t\u00e9cnico',
          'collab-item-6':'Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico',
          'collab-note-6':'Nacional tlanechicol',
          'collab-item-8':'Embajada Brit\u00e1nica ipan M\u00e9xico',
          'collab-note-8':'Tomin, coordinaci\u00f3n',
          'collab-item-9':'Oxford Festival of the Arts',
          'collab-note-9':'Oxford Forum',
          'collab-item-10':'University of Bath',
          'collab-note-10':'Teknikoh tlamatiliztli',
          'collab-item-bafa':'British Association for Forensic Anthropology',
          'collab-note-bafa':'Forense tlamatiliztli',
          'collab-item-jalisco':'Comisi\u00f3n de B\u00fasqueda de Jalisco',
          'collab-note-jalisco':'Teknikoh tlamatiliztli, coordinaci\u00f3n',
          'collab-item-oxford':'Universidad de Oxford',
          'collab-note-oxford':'Co-teyacanani, teknikoh tlamatiliztli',
          'collab-item-secihti':'Secretar\u00eda de Ciencia y Tecnolog\u00eda de M\u00e9xico',
          'collab-note-secihti':'Tomin, pol\u00edtica',
          'collab-item-unam-geo':'UNAM \u2013 Geof\u00edsica',
          'collab-note-unam-geo':'Teknikoh tlamatiliztli',
          'collab-item-unam-eng':'UNAM \u2013 Ingenier\u00eda',
          'collab-note-unam-eng':'Teknikoh tlamatiliztli',
          'collab-item-fth':'Frontier Tech Hub',
          'collab-note-fth':'Tomin, teknikoh tlamatiliztli',
          'collab-item-dtg':'DT Global',
          'collab-note-dtg':'Tomin, teknikoh tlamatiliztli',
          'collab-item-upzmg':'UPZMG',
          'collab-note-upzmg':'Sitio experimental',
          'collab-item-uwe':'UWE Bristol',
          'collab-note-uwe':'Tomin, teknikoh tlamatiliztli'
        }
      };

      let heroWords = [];
      let wordIndex = 0;
      let wordInterval = null;

      function buildHeroWords(lang){
        var dict = translations[lang] || translations.en;
        var keys = ['word-1','word-2','word-3','word-4','word-5'];
        heroWords = keys.map(function(k){ return dict[k]; }).filter(Boolean);
        wordIndex = 0;
        var span = document.getElementById('hero-word');
        if(span && heroWords.length){ span.textContent = heroWords[0]; }
      }

      function startWordRotation(){
        var span = document.getElementById('hero-word');
        if(wordInterval){ clearInterval(wordInterval); }
        if(!span || heroWords.length < 2){ return; }
        wordInterval = setInterval(function(){
          span.classList.add('fading-out');
          setTimeout(function(){
            wordIndex = (wordIndex + 1) % heroWords.length;
            span.textContent = heroWords[wordIndex];
            span.classList.remove('fading-out');
            span.classList.add('fading-in');
            requestAnimationFrame(function(){
              requestAnimationFrame(function(){
                span.classList.remove('fading-in');
              });
            });
          }, 300);
        }, 1800);
      }

      function setLanguage(lang){
        var dict = translations[lang] || translations.en;
        Object.keys(dict).forEach(function(id){
          var el = document.getElementById(id);
          if(el){ el.innerHTML = dict[id]; }
        });
        document.documentElement.setAttribute('lang',
          lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en'));
        document.querySelectorAll('.lang-btn').forEach(function(btn){
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });
        try{ localStorage.setItem('found-lang', lang); }catch(e){}
        buildHeroWords(lang);
        startWordRotation();
      }

      /* ===========================
         SCROLL REVEAL
      ============================ */
      function setupScrollReveal(){
        var reveals = document.querySelectorAll('.reveal');
        if(!reveals.length) return;

        if('IntersectionObserver' in window){
          var observer = new IntersectionObserver(function(entries){
            entries.forEach(function(entry){
              if(entry.isIntersecting){
                entry.target.classList.add('is-visible');
              }
            });
          }, { threshold:0.05, rootMargin:'0px 0px -20px 0px' });

          reveals.forEach(function(el){ observer.observe(el); });
          // Only hide elements after observer is watching them
          document.body.classList.add('reveal-ready');
        }
        // If no IntersectionObserver, elements stay visible (no class added)
      }

      /* ===========================
         TOUCH ZOOM
      ============================ */
      function setupTouchZoom(){
        var zoomables = document.querySelectorAll('.touch-zoomable');
        if(!zoomables.length){ return; }
        function toggleZoom(el){
          var isExpanded = el.classList.contains('is-expanded');
          if(isExpanded){
            el.classList.remove('is-expanded');
            document.body.classList.remove('zoom-active');
          } else {
            document.querySelectorAll('.touch-zoomable.is-expanded').forEach(function(o){
              o.classList.remove('is-expanded');
            });
            el.classList.add('is-expanded');
            document.body.classList.add('zoom-active');
          }
        }
        zoomables.forEach(function(el){
          el.addEventListener('click', function(e){
            if(window.matchMedia && window.matchMedia('(max-width: 768px)').matches){
              e.preventDefault();
              e.stopPropagation();
              toggleZoom(el);
            }
          });
        });
        document.addEventListener('keydown', function(e){
          if(e.key === 'Escape'){
            document.querySelectorAll('.touch-zoomable.is-expanded').forEach(function(o){
              o.classList.remove('is-expanded');
            });
            document.body.classList.remove('zoom-active');
          }
        });
      }

      /* ===========================
         INIT
      ============================ */
      function init(){
        var savedLang = null;
        try{ savedLang = localStorage.getItem('found-lang'); }catch(e){}
        var initialLang = (savedLang === 'es' || savedLang === 'en' || savedLang === 'nah') ? savedLang : 'en';
        setLanguage(initialLang);

        document.querySelectorAll('.lang-btn').forEach(function(btn){
          btn.addEventListener('click', function(){
            setLanguage(btn.dataset.lang);
          });
        });

        setupTouchZoom();
        setupScrollReveal();
      }

      // Run init whether DOM is already ready or not
      if(document.readyState === 'loading'){
        document.addEventListener('DOMContentLoaded', init);
      } else {
        init();
      }
    })();
  </script>

</body>
</html>---
permalink: /
title:
author_profile: false
classes: wide home-full
redirect_from:
  - /about/
  - /about.html
---

<html lang="en">
<head>
  <meta name="viewport" content="width=1200">
  <meta name="description" content="FOUND combines technology and grassroots knowledge to search for disappeared persons in Mexico, bringing dignity and closure to families." />
  <meta property="og:title" content="FOUND Project - Using Technology to Search and Remember" />
  <meta property="og:description" content="Over 130,000 persons are reported as disappeared in Mexico. Behind each case, there is a family searching for answers. FOUND works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change in how governments and institutions respond to disappearance." />
  <meta property="og:type" content="website" />
  <title>FOUND Project - Using Technology to Search and Remember</title>

  <meta http-equiv="Strict-Transport-Security" content="max-age=31536000; includeSubDomains; preload">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="DENY">
  <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..800;1,9..40,300..800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

  <script>
    (function() {
      if (window.location.protocol === 'http:' && 
          window.location.hostname === 'found-project.org' &&
          !sessionStorage.getItem('redirecting_to_https')) {
        sessionStorage.setItem('redirecting_to_https', 'true');
        var httpsUrl = 'https://found-project.org' + 
                      window.location.pathname + 
                      window.location.search + 
                      window.location.hash;
        window.location.replace(httpsUrl);
        setTimeout(function() {
          sessionStorage.removeItem('redirecting_to_https');
        }, 2000);
      } else {
        sessionStorage.removeItem('redirecting_to_https');
      }
    })();
  </script>

  <style>
    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
    }

    :root{
      --primary-green:#2d5f4d;
      --dark-green:#1a3d30;
      --deep-green:#0e2a1f;
      --light-green:#4a8c73;
      --accent-green:#e8f5f0;
      --gold-accent:#c9a227;
      --gold-light:#f0e4b8;
      --gold-glow:rgba(201,162,39,.12);
      --text-dark:#0f1a16;
      --text-medium:#374840;
      --text-light:#5e7268;
      --bg-warm:#fafcfb;
      --bg-cream:#f7f9f8;
      --border-light:rgba(15,23,42,0.08);
      --border-green:rgba(45,95,77,.12);
      --shadow-xs:0 1px 3px rgba(15,23,42,.04);
      --shadow-sm:0 2px 8px rgba(15,23,42,.05);
      --shadow-md:0 8px 24px rgba(15,23,42,.08);
      --shadow-lg:0 16px 48px rgba(15,23,42,.10);
      --shadow-xl:0 24px 64px rgba(15,23,42,.14);
      --transition-smooth:cubic-bezier(.4,0,.2,1);
      --transition-bounce:cubic-bezier(.34,1.56,.64,1);
      --radius-xl:28px;
      --radius-lg:22px;
      --radius-md:16px;
      --radius-sm:12px;
      --radius-xs:8px;
      --font-display:'DM Serif Display', Georgia, 'Times New Roman', serif;
      --font-body:'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      --font-mono:'JetBrains Mono', 'SFMono-Regular', 'Consolas', monospace;
    }

    @media (prefers-reduced-motion: reduce){
      *,*::before,*::after{
        animation-duration:.01ms!important;
        animation-iteration-count:1!important;
        transition-duration:.01ms!important;
      }
      html{scroll-behavior:auto!important;}
      .reveal{opacity:1!important;transform:none!important;}
    }

    html{scroll-behavior:smooth;}

    body{
      font-family:var(--font-body);
      color:var(--text-dark);
      line-height:1.7;
      background:var(--bg-warm);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      overflow-x:hidden;
    }

    body.zoom-active{
      overflow:hidden;
    }

    /* Subtle topographic background */
    body::before{
      content:"";
      position:fixed;
      inset:0;
      z-index:-1;
      pointer-events:none;
      opacity:0.028;
      background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='600'%3E%3Cpath d='M300 50c138 0 250 112 250 250S438 550 300 550 50 438 50 300 162 50 300 50z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 90c116 0 210 94 210 210s-94 210-210 210S90 416 90 300 184 90 300 90z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 130c94 0 170 76 170 170s-76 170-170 170-170-76-170-170 76-170 170-170z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 170c72 0 130 58 130 130s-58 130-130 130-130-58-130-130 58-130 130-130z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3Cpath d='M300 210c50 0 90 40 90 90s-40 90-90 90-90-40-90-90 40-90 90-90z' fill='none' stroke='%232d5f4d' stroke-width='.5'/%3E%3C/svg%3E");
      background-size:600px 600px;
      transform:translateZ(0);
    }

    *:focus-visible{
      outline:3px solid rgba(74,140,115,.55);
      outline-offset:2px;
      border-radius:8px;
    }

    .page,
    #main,
    .initial-content,
    .page__inner-wrap,
    .page__content,
    .archive{
      max-width:none!important;
      width:106% !important;
    }

    .page__content{
      padding-left:clamp(1rem,4vw,3rem) !important;
      padding-right:clamp(1rem,4vw,3rem) !important;
    }

    /* =========================
       Scroll reveal animations
    ========================== */
    .reveal{
      opacity:0;
      transform:translateY(32px);
      transition:opacity .7s var(--transition-smooth), transform .7s var(--transition-smooth);
    }
    .reveal.is-visible{
      opacity:1;
      transform:translateY(0);
    }
    .reveal-delay-1{transition-delay:.1s}
    .reveal-delay-2{transition-delay:.2s}
    .reveal-delay-3{transition-delay:.3s}
    .reveal-delay-4{transition-delay:.4s}

    /* =========================
       Language toggle
    ========================== */
    .lang-toggle{
      position:absolute;
      top:1.6rem;
      right:clamp(1rem,4vw,3rem);
      display:inline-flex;
      gap:.4rem;
      z-index:3;
    }

    .lang-btn{
      border:1.5px solid rgba(255,255,255,.35);
      background:rgba(255,255,255,.08);
      color:rgba(255,255,255,.72);
      padding:.38rem .9rem;
      border-radius:999px;
      font-size:.78rem;
      font-weight:700;
      font-family:var(--font-mono);
      letter-spacing:.1em;
      text-transform:uppercase;
      cursor:pointer;
      backdrop-filter:blur(12px);
      transition:all .25s var(--transition-smooth);
    }

    .lang-btn:hover{
      background:rgba(255,255,255,.15);
      color:rgba(255,255,255,.95);
      border-color:rgba(255,255,255,.55);
      transform:translateY(-1px);
    }

    .lang-btn.active{
      background:rgba(255,255,255,.95);
      color:var(--deep-green);
      border-color:rgba(255,255,255,.95);
      box-shadow:0 4px 16px rgba(0,0,0,.15);
      transform:translateY(-1px);
    }

    /* =========================
       Title section
    ========================== */
    .title-section{
      padding:clamp(4rem,8vw,6.5rem) 0 clamp(2.5rem,5vw,4rem);
      background:
        radial-gradient(ellipse 1100px 600px at 10% 40%, rgba(201,162,39,.10) 0%, transparent 60%),
        radial-gradient(ellipse 900px 500px at 90% 20%, rgba(74,140,115,.08) 0%, transparent 55%),
        linear-gradient(165deg, #071a12 0%, #0e2a1f 25%, var(--dark-green) 55%, #1e4d3a 85%, #255e48 100%);
      position:relative;
      overflow:hidden;
      margin-bottom:0;
      isolation:isolate;
    }

    .title-section::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        repeating-linear-gradient(
          0deg,
          transparent,
          transparent 120px,
          rgba(255,255,255,.015) 120px,
          rgba(255,255,255,.015) 121px
        );
      pointer-events:none;
      z-index:0;
    }

    .title-section::after{
      content:'';
      position:absolute;
      left:50%;
      top:-180px;
      width:800px;
      height:800px;
      transform:translateX(-50%);
      background:radial-gradient(circle, rgba(255,255,255,.04) 0%, transparent 55%);
      pointer-events:none;
      z-index:0;
    }

    .title-inner{
      max-width:1200px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
      z-index:1;
      display:flex;
      flex-direction:column;
      align-items:center;
      gap:1.6rem;
    }

    .title-brand{
      display:flex;
      align-items:center;
      justify-content:center;
      flex-wrap:wrap;
      gap:1.3rem;
    }
    
    .project-logo{
      width:105px;
      height:auto;
      border-radius:20px;
      box-shadow:0 12px 40px rgba(0,0,0,.35);
      border:1.5px solid rgba(255,255,255,.55);
      background:rgba(255,255,255,.06);
      padding:8px;
      flex-shrink:0;
      transition:transform .4s var(--transition-smooth);
    }

    .project-logo:hover{
      transform:scale(1.04);
    }

    .project-title{
      font-size:clamp(3rem,7vw,5.5rem);
      font-weight:900;
      color:#fff;
      letter-spacing:.06em;
      line-height:1;
      font-family:var(--font-body);
      text-shadow:0 8px 32px rgba(0,0,0,.25);
    }

    .project-subtitle{
      font-size:clamp(1.15rem,2.5vw,1.55rem);
      font-weight:400;
      color:rgba(232,245,240,.75);
      font-family:var(--font-display);
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.6;
      max-width:820px;
      margin:0 auto;
      text-align:center;
      text-shadow:0 4px 16px rgba(0,0,0,.18);
      padding:0 clamp(1rem,4vw,3rem);
    }

    .title-accent{
      color:var(--gold-accent);
      font-weight:400;
    }

    /* Gold line under title */
    .title-divider{
      width:80px;
      height:2px;
      background:linear-gradient(90deg, transparent, var(--gold-accent), transparent);
      border:none;
      margin:.2rem auto 0;
      opacity:.6;
    }

    /* =========================
       Hero
    ========================== */
    .hero{
      padding:clamp(2.5rem,5vw,4rem) 0 clamp(1.5rem,3vw,2.5rem);
      position:relative;
      overflow:hidden;
      background:var(--bg-warm);
    }

    .title-section,
    .hero{
      background-color:transparent;
    }

    .hero::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(ellipse 800px 400px at 8% 15%, rgba(232,245,240,.55) 0%, transparent 55%),
        radial-gradient(ellipse 600px 350px at 92% 5%, var(--gold-glow) 0%, transparent 55%),
        linear-gradient(180deg, var(--bg-warm) 0%, #fff 100%);
      z-index:0;
    }

    .hero-content{
      position:relative;
      z-index:1;
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    .hero-top{
      display:grid;
      grid-template-columns: minmax(0,1.15fr) minmax(0,.85fr);
      gap:clamp(2rem,4vw,3.5rem);
      align-items:start;
    }

    .hero-text{
      display:flex;
      flex-direction:column;
      gap:1.25rem;
      max-width:720px;
    }

    .animated-tagline{
      font-size:clamp(2rem,4.5vw,3.2rem);
      font-weight:900;
      display:flex;
      align-items:flex-start;
      color:var(--dark-green);
      flex-wrap:wrap;
      gap:.75rem;
      letter-spacing:-.02em;
      line-height:1.1;
    }

    .tagline-pill{
      display:inline-flex;
      flex-direction:column;
      align-items:flex-start;
      justify-content:flex-start;
      padding:.85rem 1.6rem;
      border-radius:var(--radius-xl);
      background:linear-gradient(145deg, #fff 0%, var(--accent-green) 100%);
      border:1.5px solid rgba(45,95,77,.12);
      box-shadow:var(--shadow-md), inset 0 1px 0 rgba(255,255,255,.8);
      white-space:normal;
    }

    .tagline-pill span#hero-tagline-static{
      display:block;
      width:100%;
      font-size:clamp(1.85rem,4vw,2.8rem);
      font-weight:800;
      color:var(--dark-green);
      letter-spacing:-.02em;
      line-height:1.15;
      text-align:left;
      font-family:var(--font-body);
    }

    .word-carousel{
      margin-top:.25rem;
      width:100%;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:1.3em;
    }

    .hero-word{
      display:block;
      font-size:clamp(1.8rem,4vw,2.65rem);
      font-weight:800;
      letter-spacing:-.01em;
      color:var(--light-green);
      white-space:nowrap;
      text-align:center;
      transition:opacity .3s ease, transform .3s ease;
      opacity:1;
      transform:translateY(0);
      font-family:var(--font-display);
      font-style:italic;
    }

    .hero-word.fading-out{
      opacity:0;
      transform:translateY(-8px);
    }

    .hero-word.fading-in{
      opacity:0;
      transform:translateY(8px);
    }

    .hero-description{
      font-size:clamp(1.02rem,2.2vw,1.15rem);
      color:var(--text-medium);
      max-width:900px;
      line-height:1.85;
      font-weight:400;
    }

    .hero-description strong{
      color:var(--primary-green);
      font-weight:700;
    }

    .hero-side{
      display:flex;
      flex-direction:column;
      gap:1rem;
      align-items:stretch;
      min-height:100%;
    }

    /* ==========================
       Award highlight
    =========================== */
    .award-highlight{
      margin-top:0;
    }

    .award-card{
      display:flex;
      flex-wrap:wrap;
      align-items:flex-start;
      gap:1rem;
      padding:1.4rem 1.6rem;
      border-radius:var(--radius-lg);
      background:
        linear-gradient(145deg, #fffcf2 0%, #fff 60%);
      border:1.5px solid rgba(201,162,39,.25);
      box-shadow:var(--shadow-md);
      text-decoration:none;
      color:var(--text-dark);
      position:relative;
      overflow:hidden;
      transition:all .35s var(--transition-smooth);
    }

    .award-card::before{
      content:'';
      position:absolute;
      top:0;
      left:0;
      right:0;
      height:3px;
      background:linear-gradient(90deg, var(--gold-accent), rgba(201,162,39,.3), var(--gold-accent));
      opacity:.7;
    }

    .award-card:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(201,162,39,.45);
    }

    .award-text{
      flex:1 1 220px;
      position:relative;
      z-index:1;
    }

    .award-pill{
      display:inline-flex;
      align-items:center;
      gap:.4rem;
      padding:.2rem .7rem;
      border-radius:999px;
      font-size:.72rem;
      font-weight:700;
      letter-spacing:.14em;
      text-transform:uppercase;
      background:rgba(201,162,39,.10);
      color:var(--gold-accent);
      border:1px solid rgba(201,162,39,.22);
      margin-bottom:.55rem;
      font-family:var(--font-mono);
    }

    .award-pill::before{
      content:'';
      width:5px;
      height:5px;
      border-radius:50%;
      background:var(--gold-accent);
    }

    .award-title{
      font-size:clamp(1.05rem,2vw,1.2rem);
      font-weight:700;
      letter-spacing:-.01em;
      color:var(--dark-green);
      margin-bottom:.35rem;
      line-height:1.4;
      font-family:var(--font-body);
    }

    .award-title span.arrow{
      display:inline-block;
      font-size:.9rem;
      transform:translateX(0);
      transition:transform .25s var(--transition-smooth);
    }

    .award-card:hover .award-title span.arrow{
      transform:translateX(5px);
    }

    .award-meta{
      font-size:.88rem;
      color:var(--text-light);
      line-height:1.5;
    }

    /* =========================
       Hero team bar
    ========================== */
    .hero-team-bar{
      position:relative;
      z-index:1;
      margin-top:clamp(1.5rem,3vw,2.5rem);
      padding:clamp(.85rem,1.5vw,1.15rem) clamp(1rem,4vw,3rem);
      background:var(--deep-green);
      border-top:1px solid rgba(74,140,115,.18);
      border-bottom:1px solid rgba(74,140,115,.08);
    }

    .hero-team-bar-inner{
      max-width:1400px;
      margin:0 auto;
      display:flex;
      flex-wrap:wrap;
      align-items:baseline;
      gap:.4rem 1rem;
      font-size:clamp(.78rem,1.5vw,.88rem);
      color:rgba(232,245,240,.65);
      font-family:var(--font-mono);
      line-height:1.7;
    }

    .htb-label{
      color:var(--gold-accent);
      font-weight:700;
      letter-spacing:.04em;
      white-space:nowrap;
      flex-shrink:0;
    }

    .htb-brace{
      color:rgba(74,140,115,.7);
      font-weight:400;
    }

    .htb-divider{
      color:rgba(74,140,115,.4);
      font-size:1rem;
      flex-shrink:0;
    }

    .htb-text{
      font-family:var(--font-body);
      font-size:clamp(.82rem,1.5vw,.9rem);
      color:rgba(232,245,240,.68);
      letter-spacing:.01em;
    }

    .htb-text strong{
      color:rgba(232,245,240,.92);
      font-weight:650;
    }

    /* =========================
       Generic sections
    ========================== */
    .content-section{
      padding:clamp(3rem,6vw,5rem) 0;
      position:relative;
      scroll-margin-top:2rem;
    }

    .section-container{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    /* Section divider line */
    .section-divider{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    .section-divider hr{
      border:none;
      height:1px;
      background:linear-gradient(90deg, transparent, var(--border-green), rgba(201,162,39,.1), var(--border-green), transparent);
    }

    h2{
      font-size:clamp(1.75rem,3.5vw,2.5rem);
      font-weight:400;
      font-family:var(--font-display);
      color:var(--dark-green);
      margin-bottom:1.5rem;
      letter-spacing:0;
      position:relative;
      padding-bottom:1.1rem;
      line-height:1.3;
    }

    h2::after{
      content:'';
      position:absolute;
      bottom:0;
      left:0;
      width:60px;
      height:2.5px;
      background:linear-gradient(90deg,var(--gold-accent), rgba(201,162,39,.2));
      border-radius:999px;
    }

    /* =========================
       Technologies & Buscadoras
    ========================== */
    .dual-sections-grid{
      display:grid;
      grid-template-columns:minmax(0,1.1fr) minmax(0,0.9fr);
      gap:clamp(2rem,4vw,3rem);
      align-items:stretch;
    }

    .dual-column{
      min-width:0;
    }

    #technologies{
      background:#fff;
      border-radius:var(--radius-xl);
      padding:clamp(2rem,3.5vw,3rem);
      border:1px solid var(--border-green);
      box-shadow:var(--shadow-md);
      position:relative;
      overflow:hidden;
    }

    #technologies::before{
      content:'';
      position:absolute;
      top:0;
      left:0;
      right:0;
      height:3px;
      background:linear-gradient(90deg, var(--light-green), var(--primary-green), var(--light-green));
      opacity:.5;
    }

    .info-list{
      list-style:none;
      padding-left:0;
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));
      gap:.85rem 1.25rem;
      margin-top:1.4rem;
    }

    .info-list li{
      padding:.8rem 1rem .8rem 2.8rem;
      position:relative;
      color:var(--text-medium);
      font-size:clamp(.94rem,2vw,1rem);
      min-height:46px;
      display:flex;
      align-items:center;
      line-height:1.5;
      border-radius:var(--radius-sm);
      background:var(--bg-cream);
      border:1px solid var(--border-green);
      transition:all .3s var(--transition-smooth);
    }

    .info-list li::before{
      content:"";
      position:absolute;
      left:.85rem;
      top:50%;
      transform:translateY(-50%);
      width:22px;
      height:22px;
      border-radius:50%;
      background:var(--accent-green);
      border:1.5px solid rgba(74,140,115,.25);
      display:flex;
      align-items:center;
      justify-content:center;
      transition:all .3s var(--transition-smooth);
    }

    .info-list li::after{
      content:"✓";
      position:absolute;
      left:.85rem;
      top:50%;
      transform:translateY(-50%);
      width:22px;
      height:22px;
      display:flex;
      align-items:center;
      justify-content:center;
      color:var(--primary-green);
      font-weight:800;
      font-size:.72rem;
      transition:all .3s var(--transition-smooth);
    }

    .info-list li:hover{
      color:var(--dark-green);
      transform:translateX(4px);
      border-color:rgba(74,140,115,.3);
      background:#fff;
      box-shadow:var(--shadow-sm);
    }

    .info-list li:hover::before{
      background:var(--primary-green);
      border-color:var(--primary-green);
    }
    .info-list li:hover::after{
      color:#fff;
    }

    .image-gallery{
      margin-top:2.25rem;
      display:grid;
      grid-template-columns:repeat(12,1fr);
      gap:clamp(.6rem,1vw,.85rem);
    }

    .gallery-item{
      grid-column:span 3;
      border-radius:var(--radius-md);
      overflow:hidden;
      box-shadow:var(--shadow-sm);
      border:1px solid var(--border-green);
      background:#fff;
      position:relative;
      transform:translateY(0);
      transition:all .4s var(--transition-smooth);
      aspect-ratio:4/3;
      min-height:0;
    }

    .gallery-item img{
      width:100%;
      height:100%;
      object-fit:cover;
      display:block;
      transform:scale(1.02);
      transition:transform .6s var(--transition-smooth), opacity .4s ease;
    }

    .gallery-item img.loading{
      opacity:0;
    }

    .gallery-item:hover{
      transform:translateY(-5px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.3);
    }

    .gallery-item:hover img{
      transform:scale(1.08);
    }

    .buscadoras-section{
      background:#fff;
      border-radius:var(--radius-xl);
      padding:clamp(2rem,3.5vw,3rem);
      border:1px solid var(--border-green);
      box-shadow:var(--shadow-md);
      position:relative;
      overflow:hidden;
      display:flex;
      align-items:stretch;
    }

    .buscadoras-section::before{
      content:'';
      position:absolute;
      top:0;
      left:0;
      right:0;
      height:3px;
      background:linear-gradient(90deg, rgba(201,162,39,.4), var(--gold-accent), rgba(201,162,39,.4));
      opacity:.5;
    }

    .buscadoras-content{
      max-width:100%;
      margin:0 auto;
      text-align:center;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
    }

    .buscadoras-text{
      font-size:clamp(1rem,2vw,1.1rem);
      color:var(--text-medium);
      line-height:1.85;
      margin-top:.6rem;
    }

    .buscadoras-image{
      border-radius:var(--radius-lg);
      box-shadow:var(--shadow-md);
      border:1px solid var(--border-green);
      overflow:hidden;
      margin:2rem auto .1rem;
      max-width:520px;
      position:relative;
      transform:translateY(0);
      transition:all .4s var(--transition-smooth);
      background:#fff;
    }

    .buscadoras-image img{
      width:100%;
      height:auto;
      display:block;
      transform:scale(1.02);
      transition:transform .6s var(--transition-smooth), opacity .4s ease;
    }

    .buscadoras-image img.loading{
      opacity:0;
    }

    .buscadoras-image:hover{
      transform:translateY(-5px);
      box-shadow:var(--shadow-lg);
    }

    .buscadoras-image:hover img{
      transform:scale(1.06);
    }

    /* =========================
       Institutional partnerships
    ========================== */
    .collab-wrap{
      margin-top:2rem;
    }

    .collab-grid{
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(min(100%,240px),1fr));
      gap:clamp(1rem,2vw,1.5rem);
      margin-top:1.5rem;
    }

    .collab-card{
      background:#fff;
      border-radius:var(--radius-md);
      box-shadow:var(--shadow-sm);
      border:1px solid var(--border-green);
      overflow:hidden;
      position:relative;
      transition:all .35s var(--transition-smooth);
      min-height:210px;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
    }

    .collab-card:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.35);
    }

    .collab-logo{
      padding:1.1rem 1.1rem .6rem;
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:130px;
      position:relative;
    }

    .collab-logo img{
      max-width:100%;
      max-height:90px;
      width:auto;
      height:auto;
      object-fit:contain;
      filter:grayscale(30%) brightness(1.05);
      transition:all .35s var(--transition-smooth);
    }

    .collab-img{
      max-height:80px;
      width:auto;
      object-fit:contain;
      filter:drop-shadow(0 0 1px rgba(0,0,0,.18));
    }
                
    .collab-logo img.loading{
      opacity:0;
    }

    .collab-card:hover .collab-logo img{
      filter:grayscale(0%) brightness(1);
      transform:scale(1.03);
    }

    .collab-meta{
      padding:.75rem 1.1rem 1rem;
      border-top:1px solid rgba(0,0,0,.05);
      background:var(--bg-cream);
    }

    .collab-name{
      font-weight:700;
      color:var(--dark-green);
      font-size:.95rem;
      line-height:1.35;
      letter-spacing:-.01em;
    }

    .collab-note{
      margin-top:.3rem;
      color:var(--text-light);
      font-size:.85rem;
      line-height:1.45;
    }

    .collab-card-gif .collab-logo{
      padding:0 !important;
      min-height:0 !important;
      height:160px;
      display:block;
      overflow:hidden;
      background:#fff;
    }

    .collab-card-gif .collab-logo img{
      max-height:none !important;
      max-width:none !important;
      width:100% !important;
      height:100% !important;
      object-fit:cover !important;
      object-position:center 25%;
      display:block;
      filter:none !important;
      transform:scale(1.02);
      transition:transform .7s var(--transition-smooth), opacity .4s ease;
    }

    .collab-card-gif .collab-logo img.loading{
      opacity:0;
    }

    .collab-card-gif:hover .collab-logo img{
      transform:scale(1.06);
    }

    /* =========================
       Social
    ========================== */
    .social-section{
      background:#fff;
      padding:clamp(3.5rem,6vw,5.5rem) 0;
      margin:0;
      position:relative;
      overflow:hidden;
    }

    .social-section::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(ellipse 900px 500px at 20% 0%, rgba(232,245,240,.5) 0%, transparent 55%);
      pointer-events:none;
    }

    .social-container{
      max-width:1600px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
    }

    .section-title{
      font-size:clamp(1.85rem,4vw,2.8rem);
      font-weight:400;
      font-family:var(--font-display);
      color:var(--dark-green);
      margin-bottom:.8rem;
      text-align:center;
      letter-spacing:0;
      line-height:1.2;
    }

    .section-subtitle{
      font-size:clamp(1rem,2.2vw,1.15rem);
      color:var(--text-light);
      text-align:center;
      margin-bottom:3rem;
      max-width:700px;
      margin-left:auto;
      margin-right:auto;
      line-height:1.7;
    }

    .social-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));
      gap:clamp(1.25rem,2.5vw,2rem);
      align-items:start;
    }

    .social-embed{
      background:var(--bg-cream);
      border-radius:var(--radius-lg);
      padding:1.15rem;
      box-shadow:var(--shadow-md);
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:420px;
      border:1px solid var(--border-green);
      overflow:hidden;
      position:relative;
      transition:all .35s var(--transition-smooth);
    }

    .social-embed:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.3);
    }

    .iframe-container{
      position:relative;
      width:100%;
      max-width:560px;
      overflow:hidden;
      border-radius:var(--radius-sm);
      border:1px solid rgba(15,23,42,.06);
      box-shadow:var(--shadow-sm);
    }

    .iframe-container iframe{
      width:100%;
      border:0;
      display:block;
      height:880px;
    }

    /* =========================
       Footer
    ========================== */
    .footer{
      text-align:center;
      padding:clamp(4rem,7vw,6rem) 0;
      margin-top:0;
      background:var(--deep-green);
      position:relative;
      overflow:hidden;
    }

    .footer::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(ellipse 800px 400px at 50% 0%, rgba(74,140,115,.10) 0%, transparent 60%);
      pointer-events:none;
    }

    .footer-content{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
    }

    .footer em{
      font-size:clamp(1.15rem,2.5vw,1.45rem);
      color:rgba(232,245,240,.85);
      font-weight:400;
      font-family:var(--font-display);
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.65;
      display:inline-block;
      max-width:100%;
    }

    .footer-line{
      width:60px;
      height:1.5px;
      background:linear-gradient(90deg, transparent, rgba(201,162,39,.5), transparent);
      border:none;
      margin:1.5rem auto 0;
    }

    /* =========================
       Touch zoom
    ========================== */
    @media (max-width:768px){
      .touch-zoomable{
        cursor:zoom-in;
      }

      .touch-zoomable.is-expanded{
        position:fixed;
        inset:0;
        margin:0 !important;
        width:100vw !important;
        height:100vh !important;
        max-width:none !important;
        max-height:none !important;
        z-index:9999;
        background:rgba(0,0,0,.92);
        border-radius:0 !important;
        box-shadow:none !important;
        padding:0 !important;
        display:flex;
        align-items:center;
        justify-content:center;
      }

      .touch-zoomable.is-expanded img,
      .touch-zoomable.is-expanded .hero-image{
        width:100%;
        height:100%;
        object-fit:contain;
        transform:none !important;
        box-shadow:none !important;
      }
    }

    /* =========================
       Responsive
    ========================== */
    @media (max-width:1100px){
      .image-gallery{
        grid-template-columns:repeat(6,1fr);
      }
      .gallery-item{
        grid-column:span 3;
      }
    }

    @media (max-width:900px){
      .dual-sections-grid{
        grid-template-columns:1fr;
      }
      .hero-top{
        grid-template-columns:1fr;
      }
      .hero-side{
        max-width:520px;
        margin:0 auto;
      }
    }

    @media (max-width:768px){
      .page,
      #main,
      .initial-content,
      .page__inner-wrap,
      .page__content,
      .archive{
        width:100% !important;
      }

      .lang-toggle{
        top:1rem;
      }

      .hero{
        padding:1.5rem 0 2rem;
      }

      .hero-text{
        max-width:100%;
      }

      .animated-tagline{
        flex-direction:column;
        align-items:center;
        gap:.45rem;
      }

      .tagline-pill{
        padding:.6rem 1.1rem;
        max-width:100%;
        align-items:center;
        text-align:center;
      }

      .tagline-pill span#hero-tagline-static{
        font-size:clamp(1.5rem,5.5vw,1.9rem);
        text-align:center;
      }

      .hero-word{
        font-size:clamp(1.6rem,5.5vw,2rem);
      }

      .award-card{
        padding:1.1rem 1.2rem;
      }

      .image-gallery{
        grid-template-columns:repeat(2,1fr);
      }

      .gallery-item{
        grid-column:span 2;
        aspect-ratio:16/10;
        max-height:160px;
      }

      .buscadoras-image{
        max-width:100%;
        margin-top:1.2rem;
      }

      .collab-card{
        min-height:auto;
      }

      .collab-logo{
        min-height:70px;
        padding:.7rem;
      }

      .collab-logo img{
        max-height:60px;
      }

      .collab-meta{
        padding:.6rem .8rem .8rem;
      }

      .collab-name{
        font-size:.92rem;
      }

      .collab-note{
        font-size:.82rem;
      }

      .social-grid{
        grid-template-columns:1fr;
      }

      .social-embed{
        min-height:auto;
      }

      .iframe-container iframe{
        height:520px;
      }

      .project-logo{
        width:78px;
      }
    }

    @media (max-width:480px){
      .gallery-item{
        max-height:140px;
      }
      .iframe-container iframe{
        height:430px;
      }
    }

    /* Re-tint logos to dark */
    .collab-img.fth{
      filter: brightness(0) saturate(100%) invert(9%) sepia(6%)
              saturate(512%) hue-rotate(94deg)
              brightness(95%) contrast(96%);
    }
        
    .collab-img.labco{
      filter: brightness(0) saturate(100%) invert(9%) sepia(6%)
              saturate(512%) hue-rotate(94deg)
              brightness(95%) contrast(96%);
    }

    /* =========================
       GIF Strip
    ========================== */
    .gif-strip{
      padding:clamp(1.5rem,3vw,2.5rem) 0 0;
      position:relative;
      overflow:hidden;
      background:var(--bg-cream);
      isolation:isolate;
    }

    .gif-strip-inner{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      position:relative;
      z-index:1;
      display:grid;
      grid-template-columns: 1.55fr 1fr 1fr;
      gap:clamp(.55rem,1.1vw,.85rem);
      align-items:stretch;
    }

    .gs-panel{
      border-radius:var(--radius-md);
      overflow:hidden;
      border:1px solid var(--border-green);
      box-shadow:var(--shadow-md);
      position:relative;
      background:#fff;
      transform:translateY(0);
      transition:all .4s var(--transition-smooth);
    }

    .gs-panel-main { aspect-ratio:16/9; }
    .gs-panel-side { aspect-ratio:4/3; }

    .gs-panel::before{
      content:attr(data-label);
      position:absolute;
      bottom:.6rem;
      left:.6rem;
      z-index:2;
      font-size:.68rem;
      font-weight:600;
      letter-spacing:.08em;
      text-transform:uppercase;
      color:#fff;
      background:rgba(14,40,30,.7);
      backdrop-filter:blur(10px);
      padding:.2rem .6rem;
      border-radius:999px;
      border:1px solid rgba(255,255,255,.15);
      opacity:0;
      transform:translateY(4px);
      transition:opacity .3s ease, transform .3s ease;
      pointer-events:none;
      font-family:var(--font-mono);
      font-size:.62rem;
    }

    .gs-panel:hover::before{
      opacity:1;
      transform:translateY(0);
    }

    .gs-panel:hover{
      transform:translateY(-4px);
      box-shadow:var(--shadow-lg);
    }

    .gs-panel img{
      position:absolute;
      inset:0;
      width:100%;
      height:100%;
      object-fit:cover;
      display:block;
      transform:scale(1.02);
      transition:transform .7s var(--transition-smooth), opacity .4s ease;
    }

    .gs-panel img.loading{ opacity:0; }
    .gs-panel:hover img{ transform:scale(1.06); }

    .gs-panel-side::after{
      content:'';
      position:absolute;
      top:.5rem;
      right:.5rem;
      width:7px;
      height:7px;
      background:var(--gold-accent);
      border-radius:50%;
      box-shadow:0 0 0 2px rgba(255,255,255,.5);
      animation:livePulse 2.2s ease-in-out infinite;
      z-index:2;
    }

    @keyframes livePulse{
      0%,100%{ opacity:1; transform:scale(1); }
      50%    { opacity:.5; transform:scale(1.4); }
    }

    /* GIF Strip Caption Bar */
    .gif-strip-caption {
      position: relative;
      z-index: 2;
      margin: clamp(.55rem,1.1vw,.8rem) 0 0;
      padding: clamp(.6rem, 1.2vw, .85rem) clamp(1rem, 4vw, 3rem);
      background: var(--deep-green);
      border-top: 1px solid rgba(74, 140, 115, .18);
    }

    .gif-caption-inner {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: .5rem 1rem;
      font-size: clamp(.76rem, 1.4vw, .85rem);
      color: rgba(232, 245, 240, .65);
      font-family: var(--font-mono);
      line-height: 1.65;
    }

    .gif-caption-tag {
      color: var(--gold-accent);
      font-weight: 700;
      letter-spacing: .04em;
      font-size: clamp(.78rem, 1.5vw, .88rem);
      white-space: nowrap;
    }

    .gif-caption-brace {
      color: rgba(74, 140, 115, .7);
      font-weight: 400;
    }

    .gif-caption-divider {
      color: rgba(74, 140, 115, .4);
      font-size: 1rem;
      font-family: inherit;
      flex-shrink: 0;
    }

    .gif-caption-item {
      font-family: var(--font-body);
      font-size: clamp(.78rem, 1.4vw, .85rem);
      color: rgba(232, 245, 240, .62);
      letter-spacing: .01em;
    }

    .gif-caption-item strong {
      color: rgba(232, 245, 240, .9);
      font-weight: 650;
    }

    @media (max-width:700px){
      .gif-strip-inner{ grid-template-columns:1fr; }
      .gs-panel-main, .gs-panel-side{ aspect-ratio:16/9; }
    }
    @media (min-width:701px) and (max-width:1050px){
      .gif-strip-inner{ grid-template-columns:1fr 1fr; grid-template-rows:auto auto; }
      .gs-panel-main{ grid-column:1; grid-row:1/3; aspect-ratio:unset; min-height:220px; }
      .gs-panel-side:nth-child(2){ grid-column:2; grid-row:1; }
      .gs-panel-side:nth-child(3){ grid-column:2; grid-row:2; }
    }

    /* =========================
       Stats ribbon 
    ========================== */
    .stats-ribbon{
      padding:clamp(1.5rem,3vw,2.2rem) 0;
      background:var(--bg-warm);
      position:relative;
    }
    .stats-ribbon-inner{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
      display:flex;
      justify-content:center;
      gap:clamp(2rem,5vw,5rem);
      flex-wrap:wrap;
    }
    .stat-item{
      text-align:center;
      min-width:140px;
    }
    .stat-number{
      font-size:clamp(2rem,4vw,3rem);
      font-weight:800;
      color:var(--dark-green);
      font-family:var(--font-body);
      letter-spacing:-.03em;
      line-height:1.1;
    }
    .stat-number .stat-plus{
      color:var(--gold-accent);
      font-weight:700;
    }
    .stat-label{
      font-size:clamp(.78rem,1.5vw,.88rem);
      color:var(--text-light);
      margin-top:.3rem;
      letter-spacing:.03em;
      text-transform:uppercase;
      font-weight:600;
      font-family:var(--font-mono);
      font-size:.72rem;
    }
    .stat-divider{
      width:1px;
      background:linear-gradient(180deg, transparent, var(--border-green), transparent);
      align-self:stretch;
    }

    @media (max-width:600px){
      .stats-ribbon-inner{ gap:1.5rem 2rem; }
      .stat-divider{ display:none; }
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

    <div class="title-inner">
      <div class="title-brand">
        <img
          src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9466ebc27c9487e8bfbff1d1dd904f4f9e6df81d/images/logo_FOUND_white.png"
          alt="FOUND logo"
          class="project-logo"
        />
        <h1 class="project-title">FOUND</h1>
      </div>
      <hr class="title-divider" />
      <p class="project-subtitle" id="project-subtitle">
        <span class="title-accent">Interpretar la Naturaleza</span> para Encontrar a Quienes nos Faltan
      </p>
    </div>
  </section>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-top">
        <div class="hero-text reveal">
          <div class="animated-tagline">
            <div class="tagline-pill" aria-label="FOUND tagline">
              <span id="hero-tagline-static">Using technology to</span>
              <div class="word-carousel" role="text">
                <span id="hero-word" class="hero-word">search.</span>
              </div>
            </div>
          </div>

          <p class="hero-description" id="hero-main-text">
            Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
            <strong>FOUND</strong> builds the scientific and institutional capabilities needed to find and return missing persons to their families. Working at the intersection of frontier technology and the lived knowledge of search groups, we drive systemic change in how governments and institutions respond to disappearance.
          </p>
        </div>

        <div class="hero-side reveal reveal-delay-2">
          <div class="award-highlight">
            <a href="/news/#mariela-award" class="award-card">
              <div class="award-text">
                <div class="award-pill">Award</div>
                <div class="award-title">
                  FOUND recognised with the Sir Nicholas Browne Policy and Expertise Award
                  <span class="arrow">&#x2197;</span>
                </div>
                <div class="award-meta">
                  Selected from over 200 nominations across the UK Foreign, Commonwealth &amp; Development Office.
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Team bar -->
    <div class="hero-team-bar">
      <div class="hero-team-bar-inner">
        <span class="htb-label">FOUND<span class="htb-brace">{</span>Team<span class="htb-brace">}</span></span>
        <span class="htb-divider">·</span>
        <span class="htb-text" id="hero-team-text">Our core team brings together <strong>collectives of families from Jalisco, Zacatecas, and Colombia searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco's Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico's National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.</span>
      </div>
    </div>
  </section>

  <!-- GIF STRIP -->
  <section class="gif-strip" aria-label="FOUND in action">
    <div class="gif-strip-inner">
      <div class="gs-panel gs-panel-main touch-zoomable" data-label="Spectral indices · substance detection">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/1047db9c85ff842e083e9fb45c0bdf05213da88a/images/NDAI5.gif"
             alt="FOUND Project team using advanced technology in field search operations"
             loading="lazy" class="loading" onload="this.classList.remove('loading')" />
      </div>

      <div class="gs-panel gs-panel-side touch-zoomable" data-label="Satellite analysis · time series">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/33b2627b6b245e9632f59abf0a02f5ad58956bf4/images/Areas_de_busqueda_3.gif"
             alt="Satellite spectral time-series analysis of search areas"
             loading="lazy" class="loading" onload="this.classList.remove('loading')" />
      </div>

      <div class="gs-panel gs-panel-side touch-zoomable" data-label="Clandestine space detection">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9b9df755f7129ba10ee53479d528d42d14e5648a/images/ClandestineSpace.gif"
             alt="Spectral detection of clandestine sites using satellite imagery"
             loading="lazy" class="loading" onload="this.classList.remove('loading')" />
      </div>
    </div>

    <div class="gif-strip-caption">
      <div class="gif-caption-inner">
        <span class="gif-caption-tag">Platforms<span class="gif-caption-brace">{</span>core member: CentroGeo<span class="gif-caption-brace">}</span></span>
        <span class="gif-caption-divider">·</span>
        <span class="gif-caption-item"><strong>Spectral indices</strong> — Identifying substances linked to disappearances via satellite and drone imagery, and when they were present.</span>
        <span class="gif-caption-divider">·</span>
        <span class="gif-caption-item"><strong>Clandestine sites location</strong> — AI that finds what was meant to stay hidden.</span>
      </div>
    </div>
  </section>

  <!-- STATS RIBBON -->
  <section class="stats-ribbon reveal" aria-label="Key statistics">
    <div class="stats-ribbon-inner">
      <div class="stat-item">
        <div class="stat-number" id="stat-num-1">130,000<span class="stat-plus">+</span></div>
        <div class="stat-label" id="stat-label-1">Persons disappeared</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-number" id="stat-num-2">7<span class="stat-plus">+</span></div>
        <div class="stat-label" id="stat-label-2">Technologies deployed</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-number" id="stat-num-3">20<span class="stat-plus">+</span></div>
        <div class="stat-label" id="stat-label-3">Institutional partners</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <div class="stat-number" id="stat-num-4">3</div>
        <div class="stat-label" id="stat-label-4">Countries</div>
      </div>
    </div>
  </section>

  <!-- TECHNOLOGIES + BUSCADORAS -->
  <section class="content-section">
    <div class="section-container dual-sections-grid">
      <div class="dual-column reveal">
        <section id="technologies">
          <h2 id="tech-title">Technologies in Action</h2>
          <ul class="info-list">
            <li id="tech-item-1">Multispectral &amp; Hyperspectral Imaging</li>
            <li id="tech-item-2">Airborne LiDAR</li>
            <li id="tech-item-3">Seismic Noise Interferometry (TIRSA)</li>
            <li id="tech-item-4">Electrical Resistivity Tomography, Conductivimetry</li>
            <li id="tech-item-5">Satellite Spectral Analysis</li>
            <li id="tech-item-ml">Machine Learning</li>
            <li id="tech-item-6">Forensic Entomology, Botany, Territorial Analysis, Soil Science</li>
          </ul>

          <div class="image-gallery">
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/360.gif" alt="360 degree imaging technology in use" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.03.01.jpeg?raw=true" alt="Advanced field equipment setup" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/2.jpeg?raw=true" alt="Community collaboration in search efforts" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true" alt="Specialised search tools and equipment" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3.jpeg?raw=true" alt="Field research and data collection" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-07-30%20at%2021.40.57.jpeg?raw=true" alt="Team collaboration during field operations" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/c88e3807678629fcd59ad91baff20b6ec7a34f66/images/layers.jpg?raw=true"
                   alt="Technology deployment in field"
                   loading="lazy"
                   class="loading"
                   onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/IMG-20231204-WA0038.jpg?raw=true" alt="Field operations and search activities" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-12-02%20at%2018.42.17.jpeg?raw=true" alt="Search team in action" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/70206a6b5788f7204524bfdd4e1a6c365668b75d/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.44.jpeg" alt="Search methodology in practice" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/51a35a3f1915699b8fe9835270ddfe6f3c5c0946/images/hyperspectral%20from%20presentation.png?raw=true"
                   alt="Hyperspectral analysis output used in FOUND field validation"
                   loading="lazy"
                   class="loading"
                   onload="this.classList.remove('loading')">
            </div>
            <div class="gallery-item touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/51a35a3f1915699b8fe9835270ddfe6f3c5c0946/images/pigs_aerial.jpg?raw=true"
                   alt="Aerial view of experimental calibration site using animal proxies"
                   loading="lazy"
                   class="loading"
                   onload="this.classList.remove('loading')">
            </div>  
          </div>
        </section>
      </div>

      <div class="dual-column reveal reveal-delay-2">
        <section class="buscadoras-section" id="buscadoras">
          <div class="buscadoras-content">
            <div>
              <h2 id="buscadoras-title">The Role of Buscadoras</h2>
              <p class="buscadoras-text hero-description" id="buscadoras-text">
                Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice.
                Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and
                incorporates their methods into our technological efforts.
              </p>
            </div>
            <div class="buscadoras-image touch-zoomable">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolising hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
          </div>
        </section>
      </div>
    </div>
  </section>

  <!-- DIVIDER -->
  <div class="section-divider"><hr/></div>

  <!-- INSTITUTIONAL PARTNERSHIPS -->
  <section class="content-section" id="collaborations">
    <div class="section-container">
      <h2 id="collab-title" class="reveal">Institutional Partnerships</h2>

      <div class="collab-wrap reveal" aria-label="Institutional partnerships logos">
        <div class="collab-grid">

          <div class="collab-card collab-card-gif touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0bed7c6b4c906bc94116683368b679ba0bd80428/images/mothers%20walking.gif"
                alt="Search Collectives" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-7">Search Collectives</div>
              <div class="collab-note" id="collab-note-7">Leadership, field expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/1%20Executive%20Office%20of%20the%20UN%20Secretary-General.svg"
                alt="Executive Office of the UN Secretary-General" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-1">Executive Office of the UN Secretary-General</div>
              <div class="collab-note" id="collab-note-1">International collaboration</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/bd3ef3bd33596258b2738274017f51a2e2c05186/images/FCDO_logo_960x640.png"
                alt="UK Foreign, Commonwealth & Development Office" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-2">UK Foreign, Commonwealth &amp; Development Office (FCDO)</div>
              <div class="collab-note" id="collab-note-2">Policy, Funding, Partnerships</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/2%20logo_centrogeo_wide.svg"
                alt="CentroGeo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-3">CentroGeo</div>
              <div class="collab-note" id="collab-note-3">Co-lead, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/26bd52ce350828b22814cfedc872786dd43de672/images/580141488dfc53bfdbde59fa6b043438.jpg"
                alt="University of Guadalajara" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-4">University of Guadalajara (UdeG)</div>
              <div class="collab-note" id="collab-note-4">Technical expertise, Experimental sites</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg"
                alt="Colombian Search Unit" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-5">Colombian Search Unit (UBPD)</div>
              <div class="collab-note" id="collab-note-5">Casework, Technical exchange</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/4%20Comision%20Nacional%20de%20Busqueda.png"
                alt="Mexico National Search Commission" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-6">Mexico's National Search Commission</div>
              <div class="collab-note" id="collab-note-6">National coordination</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png"
                alt="British Embassy Mexico City" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-8">British Embassy in Mexico City</div>
              <div class="collab-note" id="collab-note-8">Funding, Coordination support</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/5ea7b61d8c5c6467ad4253f2898109033aac13e7/images/OFOTA_COLOUR_WEB.jpg"
                alt="Oxford Festival of the Arts" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-9">Oxford Festival of the Arts</div>
              <div class="collab-note" id="collab-note-9">Oxford Forum partner</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b2323f813df618867a6227a87e7efb9e084fe75e/images/Beth.jpg"
                alt="University of Bath" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-10">University of Bath</div>
              <div class="collab-note" id="collab-note-10">Technical expertise, Oxford Forum partner</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/11%20logo%20BAFAlogo_orig.png"
                alt="British Association for Forensic Anthropology" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-bafa">British Association for Forensic Anthropology</div>
              <div class="collab-note" id="collab-note-bafa">Forensic expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/3%20Comisio%CC%81n%20de%20Bu%CC%81squeda%20de%20Jalisco.png"
                alt="Comisión de Búsqueda de Jalisco" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-jalisco">Comisión de Búsqueda de Jalisco</div>
              <div class="collab-note" id="collab-note-jalisco">Technical expertise, Coordination</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/4%20logo%20oxford-university-logo.png"
                alt="University of Oxford" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-oxford">University of Oxford</div>
              <div class="collab-note" id="collab-note-oxford">Co-lead, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20Logotipo_SECIHTI_2025-2030.svg"
                alt="Mexico's Science and Technology Secretariat" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-secihti">Mexico's Science and Technology Secretariat</div>
              <div class="collab-note" id="collab-note-secihti">Funding, Policy impact</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20logo%20IGeofisicaUNAM.png"
                alt="UNAM Geophysics Institute" loading="lazy" onload="this.classList.remove('loading')"
                style="filter: brightness(0) invert(0);">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-unam-geo">UNAM – Geophysics</div>
              <div class="collab-note" id="collab-note-unam-geo">Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/6%20logo%20Ingenieria%20UNAM.png"
                alt="UNAM Engineering" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-unam-eng">UNAM – Engineering</div>
              <div class="collab-note" id="collab-note-unam-eng">Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/master/images/10%20logo%20FT%2Blogo_Primary%2Bversion_white%2Btext.png"
                alt="Frontier Tech Hub" loading="lazy" class="collab-img fth">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-fth">Frontier Tech Hub</div>
              <div class="collab-note" id="collab-note-fth">Funding, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20DTG_Logo_Screen_LRG-1.png"
                alt="DT Global" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-dtg">DT Global</div>
              <div class="collab-note" id="collab-note-dtg">Funding, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20logo%20UPZMG2.png"
                alt="UPZMG" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-upzmg">UPZMG</div>
              <div class="collab-note" id="collab-note-upzmg">Experimental site</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/9%20logo%20UWE%20Bristol.svg"
                alt="UWE Bristol" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-uwe">UWE Bristol</div>
              <div class="collab-note" id="collab-note-uwe">Funding, Technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d47bacb6b575270e7b5453c8ebc5b13bcec70a2f/images/dark-non-retina-labco.png"
                alt="LABCO" loading="lazy" class="collab-img labco">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-labco">LABCO</div>
              <div class="collab-note" id="collab-note-labco">Exploring AI together to locate and identify</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://github.com/FOUND-project/found-project.github.io/blob/82b303cdf26fa6a25e9845ff0d5fc10e070d94e6/images/logo_eaaf_rd.png?raw=true"
                alt="Argentine Forensic Anthropology Team (EAAF)" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-eaaf">Argentine Forensic Anthropology Team (EAAF)</div>
              <div class="collab-note" id="collab-note-eaaf">Luis Fondebrider, FOUND's advisor</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/a8209a23c303b55bda756d5a55b2c572ac2540a9/images/ori_logo_square_2024_150_inverted.png"
                alt="Oxford Robotics Institute" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-ori">Oxford Robotics Institute</div>
              <div class="collab-note" id="collab-note-ori">Partnership, technical expertise</div>
            </div>
          </div>

          <div class="collab-card touch-zoomable">
            <div class="collab-logo">
              <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b9419b5a0b9d80c6ae96d16642771d6c1d66cdf3/images/logo-ipn-guinda.svg"
                alt="Instituto Politécnico Nacional" loading="lazy" class="loading" onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-ipn">Instituto Politécnico Nacional</div>
              <div class="collab-note" id="collab-note-ipn">Technical expertise, Technology</div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

  <!-- DIVIDER -->
  <div class="section-divider"><hr/></div>

  <!-- SOCIAL -->
  <section class="social-section" id="social">
    <div class="social-container">
      <h2 class="section-title reveal" id="social-title">Follow Our Journey</h2>
      <p class="section-subtitle reveal reveal-delay-1" id="social-subtitle">
        Our latest findings, community stories, and collaborations
      </p>

      <div class="social-grid reveal reveal-delay-2">
        <div class="social-embed">
          <div class="iframe-container">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7405294962692595712"
              height="880" width="504" frameborder="0" allowfullscreen
              title="FOUND Project LinkedIn update" loading="lazy"></iframe>
          </div>
        </div>

        <div class="social-embed twitter-embed">
          <div class="iframe-container">
            <blockquote class="twitter-tweet">
              <p lang="en" dir="ltr">
                Almost a year after I started researching the story, I'm thrilled that my
                <a href="https://twitter.com/guardian?ref_src=twsrc%5Etfw">@guardian</a>
                article about the innovations being used to try and find some of the thousands
                of people who have disappeared in Mexico is the most read in its Global Development section.
                <a href="https://t.co/NztFCj4uEF">https://t.co/NztFCj4uEF</a>
              </p>
              &mdash; Suzanne Bearne (@sbearne)
              <a href="https://twitter.com/sbearne/status/1991827389375193330?ref_src=twsrc%5Etfw">November 21, 2025</a>
            </blockquote>
          </div>
        </div>

        <div class="social-embed twitter-embed">
          <div class="iframe-container">
            <blockquote class="twitter-tweet">
              <p lang="es" dir="ltr">
                Cómo los cerdos y los insectos están ayudando a encontrar a los desaparecidos en México
                <a href="https://t.co/sJC3oaNLGL">https://t.co/sJC3oaNLGL</a>
              </p>
              &mdash; BBC News Mundo (@bbcmundo)
              <a href="https://twitter.com/bbcmundo/status/1973352689867063513?ref_src=twsrc%5Etfw">October 1, 2025</a>
            </blockquote>
          </div>
        </div>

        <div class="social-embed">
          <div class="iframe-container">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728"
              height="880" width="504" frameborder="0" allowfullscreen
              title="FOUND Project community engagement" loading="lazy"></iframe>
          </div>
        </div>

        <div class="social-embed">
          <div class="iframe-container">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7343552976185114624"
              height="880" width="504" frameborder="0" allowfullscreen
              title="FCDO LinkedIn post about FOUND Project" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-content">
      <em id="footer-text">FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
      <hr class="footer-line" />
    </div>
  </footer>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

  <script>
    (function(){
      /* ===========================
         TRANSLATIONS
      ============================ */
      const translations = {
        en:{
          'collab-item-labco':'LABCO',
          'collab-note-labco':'Exploring AI together to locate and identify',
          'collab-item-eaaf':'Argentine Forensic Anthropology Team (EAAF)',
          'collab-note-eaaf':"Luis Fondebrider, FOUND's advisor",
          'collab-item-ori':'Oxford Robotics Institute',
          'collab-note-ori':'Partnership, technical expertise',
          'collab-item-ipn':'Instituto Polit\u00e9cnico Nacional',
          'collab-note-ipn':'Technical expertise, Technology',
          'project-subtitle':'<span class="title-accent">Technologies</span> To Locate Those Who We Are Missing',
          'hero-tagline-static':'Using technology to',
          'word-1':'search.',
          'word-2':'remember.',
          'word-3':'dignify.',
          'word-4':'find.',
          'word-5':'bring closure.',
          'hero-main-text':'Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change in how governments and institutions respond to disappearance.',
          'hero-team-text':'Our core team brings together <strong>collectives of families from Jalisco and Zacatecas searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco\'s Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico\'s National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.',
          'collab-title':'Institutional Partnerships',
          'tech-title':'Technologies in Action',
          'tech-item-1':'Multispectral &amp; Hyperspectral Imaging',
          'tech-item-2':'Airborne LiDAR',
          'tech-item-3':'Seismic Noise Interferometry (TIRSA)',
          'tech-item-4':'Electrical Resistivity Tomography, Conductivimetry',
          'tech-item-5':'Satellite Spectral Analysis',
          'tech-item-ml':'Machine Learning',
          'tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science',
          'buscadoras-title':'The Role of Buscadoras',
          'buscadoras-text':"Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.",
          'social-title':'Follow Our Journey',
          'social-subtitle':'Stay connected with our latest findings, community stories, and collaborations',
          'footer-text':'FOUND: Tecnolog\u00edas para Encontrar a Quienes nos Faltan.',
          'stat-label-1':'Persons disappeared',
          'stat-label-2':'Technologies deployed',
          'stat-label-3':'Institutional partners',
          'stat-label-4':'Countries',
          'collab-item-7':'Search Collectives',
          'collab-note-7':'Leadership, field expertise',
          'collab-item-1':'Executive Office of the UN Secretary-General',
          'collab-note-1':'International collaboration',
          'collab-item-2':'UK Foreign, Commonwealth &amp; Development Office (FCDO)',
          'collab-note-2':'Policy, Funding, Partnerships',
          'collab-item-3':'CentroGeo',
          'collab-note-3':'Co-lead, Technical expertise',
          'collab-item-4':'University of Guadalajara (UdeG)',
          'collab-note-4':'Technical expertise, Experimental sites',
          'collab-item-5':'Colombian Search Unit (UBPD)',
          'collab-note-5':'Casework, Technical exchange',
          'collab-item-6':"Mexico's National Search Commission",
          'collab-note-6':'National coordination',
          'collab-item-8':'British Embassy in Mexico City',
          'collab-note-8':'Funding, Coordination support',
          'collab-item-9':'Oxford Festival of the Arts',
          'collab-note-9':'Oxford Forum partner',
          'collab-item-10':'University of Bath',
          'collab-note-10':'Technical expertise, Oxford Forum partner',
          'collab-item-bafa':'British Association for Forensic Anthropology',
          'collab-note-bafa':'Forensic expertise',
          'collab-item-jalisco':'Comisi\u00f3n de B\u00fasqueda de Jalisco',
          'collab-note-jalisco':'Technical expertise, Coordination',
          'collab-item-oxford':'University of Oxford',
          'collab-note-oxford':'Co-lead, Technical expertise',
          'collab-item-secihti':"Mexico's Science and Technology Secretariat",
          'collab-note-secihti':'Funding, Policy impact',
          'collab-item-unam-geo':'UNAM \u2013 Geophysics',
          'collab-note-unam-geo':'Technical expertise',
          'collab-item-unam-eng':'UNAM \u2013 Engineering',
          'collab-note-unam-eng':'Technical expertise',
          'collab-item-fth':'Frontier Tech Hub',
          'collab-note-fth':'Funding, Technical expertise',
          'collab-item-dtg':'DT Global',
          'collab-note-dtg':'Funding, Technical expertise',
          'collab-item-upzmg':'UPZMG',
          'collab-note-upzmg':'Experimental site',
          'collab-item-uwe':'UWE Bristol',
          'collab-note-uwe':'Funding, Technical expertise'
        },
        es:{
          'collab-item-labco':'LABCO',
          'collab-note-labco':'Explorando juntos el uso de IA para localizar e identificar',
          'collab-item-eaaf':'Equipo Argentino de Antropolog\u00eda Forense (EAAF)',
          'collab-note-eaaf':'Luis Fondebrider, asesor de FOUND',
          'collab-item-ori':'Oxford Robotics Institute',
          'collab-note-ori':'Alianza, experiencia t\u00e9cnica',
          'collab-item-ipn':'Instituto Polit\u00e9cnico Nacional',
          'collab-note-ipn':'Experiencia t\u00e9cnica, desarrollo tecnol\u00f3gico',
          'project-subtitle':'<span class="title-accent">Tecnolog\u00edas</span> para Encontrar a Quienes nos Faltan',
          'hero-tagline-static':'Usando tecnolog\u00eda para',
          'word-1':'buscar.',
          'word-2':'recordar.',
          'word-3':'dignificar.',
          'word-4':'encontrar.',
          'word-5':'dar cierre.',
          'hero-main-text':'M\u00e1s de 130,000 personas est\u00e1n registradas como desaparecidas en M\u00e9xico. Detr\u00e1s de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> combina tecnolog\u00eda y saberes de familias buscadoras para aprender del campo, localizar y promover cambios sist\u00e9micos.',
          'hero-team-text':'Nuestro equipo central re\u00fane <strong>colectivos de familias de Jalisco y Zacatecas que buscan a sus seres queridos desaparecidos</strong>, junto a CentroGeo, la Universidad de Oxford, la Comisi\u00f3n de B\u00fasqueda de Jalisco, la Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) y la Universidad de Guadalajara. Trabajamos junto a socios estrat\u00e9gicos, entre ellos la Oficina para Asuntos Exteriores, de la Commonwealth y de Desarrollo del Reino Unido (FCDO), la Oficina Ejecutiva del Secretario General de la ONU, la Unidad de B\u00fasqueda de Personas dadas por Desaparecidas (UBPD) de Colombia, la Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico, LAB-Co y Luis Fondebrider.',
          'collab-title':'Alianzas institucionales',
          'tech-title':'Tecnolog\u00edas en acci\u00f3n',
          'tech-item-1':'Im\u00e1genes multiespectrales e hiperespectrales',
          'tech-item-2':'LiDAR aerotransportado',
          'tech-item-3':'Interferometr\u00eda de ruido s\u00edsmico (TIRSA)',
          'tech-item-4':'Tomograf\u00eda de resistividad el\u00e9ctrica y mediciones de conductividad',
          'tech-item-5':'An\u00e1lisis espectral satelital',
          'tech-item-ml':'Aprendizaje autom\u00e1tico',
          'tech-item-6':'Entomolog\u00eda forense, bot\u00e1nica, an\u00e1lisis territorial y ciencia del suelo',
          'buscadoras-title':'El papel de las buscadoras',
          'buscadoras-text':'Los colectivos liderados por mujeres est\u00e1n en el coraz\u00f3n del trabajo de FOUND. Han transformado la conversaci\u00f3n nacional sobre desaparici\u00f3n y justicia. Sus pr\u00e1cticas de b\u00fasqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus m\u00e9todos en nuestros esfuerzos tecnol\u00f3gicos.',
          'social-title':'Sigue nuestro camino',
          'social-subtitle':'Mant\u00e9nte al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.',
          'footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.',
          'stat-label-1':'Personas desaparecidas',
          'stat-label-2':'Tecnolog\u00edas desplegadas',
          'stat-label-3':'Socios institucionales',
          'stat-label-4':'Pa\u00edses',
          'collab-item-7':'Colectivos de B\u00fasqueda',
          'collab-note-7':'Liderazgo, experiencia en campo',
          'collab-item-1':'Oficina Ejecutiva del Secretario General de la ONU',
          'collab-note-1':'Colaboraci\u00f3n internacional',
          'collab-item-2':'Oficina para Asuntos Exteriores, de la Commonwealth y de Desarrollo del Reino Unido (FCDO)',
          'collab-note-2':'Pol\u00edtica, financiamiento, alianzas',
          'collab-item-3':'CentroGeo',
          'collab-note-3':'Co-l\u00edder, experiencia t\u00e9cnica',
          'collab-item-4':'Universidad de Guadalajara (UdeG)',
          'collab-note-4':'Experiencia t\u00e9cnica, sitios experimentales',
          'collab-item-5':'Unidad de B\u00fasqueda de Colombia (UBPD)',
          'collab-note-5':'Casos, intercambio t\u00e9cnico',
          'collab-item-6':'Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico',
          'collab-note-6':'Coordinaci\u00f3n nacional',
          'collab-item-8':'Embajada Brit\u00e1nica en la Ciudad de M\u00e9xico',
          'collab-note-8':'Financiamiento, coordinaci\u00f3n',
          'collab-item-9':'Oxford Festival of the Arts',
          'collab-note-9':'Socio del Foro de Oxford',
          'collab-item-10':'University of Bath',
          'collab-note-10':'Experiencia t\u00e9cnica, socio del Foro de Oxford',
          'collab-item-bafa':'British Association for Forensic Anthropology',
          'collab-note-bafa':'Experiencia forense',
          'collab-item-jalisco':'Comisi\u00f3n de B\u00fasqueda de Jalisco',
          'collab-note-jalisco':'Experiencia t\u00e9cnica, coordinaci\u00f3n',
          'collab-item-oxford':'Universidad de Oxford',
          'collab-note-oxford':'Co-l\u00edder, experiencia t\u00e9cnica',
          'collab-item-secihti':'Secretar\u00eda de Ciencia y Tecnolog\u00eda de M\u00e9xico',
          'collab-note-secihti':'Financiamiento, impacto en pol\u00edticas',
          'collab-item-unam-geo':'UNAM \u2013 Geof\u00edsica',
          'collab-note-unam-geo':'Experiencia t\u00e9cnica',
          'collab-item-unam-eng':'UNAM \u2013 Ingenier\u00eda',
          'collab-note-unam-eng':'Experiencia t\u00e9cnica',
          'collab-item-fth':'Frontier Tech Hub',
          'collab-note-fth':'Financiamiento, experiencia t\u00e9cnica',
          'collab-item-dtg':'DT Global',
          'collab-note-dtg':'Financiamiento, experiencia t\u00e9cnica',
          'collab-item-upzmg':'UPZMG',
          'collab-note-upzmg':'Sitio experimental',
          'collab-item-uwe':'UWE Bristol',
          'collab-note-uwe':'Financiamiento, experiencia t\u00e9cnica'
        },
        nah:{
          'collab-item-labco':'LABCO',
          'collab-note-labco':'Timoitayoh ika IA para titemoa huan tiquixmati',
          'collab-item-eaaf':'Equipo Argentino de Antropolog\u00eda Forense (EAAF)',
          'collab-note-eaaf':'Luis Fondebrider, ixcuitlali (asesor) FOUND',
          'collab-item-ori':'Oxford Robotics Institute',
          'collab-note-ori':'Tlaneltiliztli (alianza), teknikoh tlamatiliztli',
          'collab-item-ipn':'Instituto Polit\u00e9cnico Nacional',
          'collab-note-ipn':'Teknikoh tlamatiliztli, teknoloj\u00edayoh tlatequipanoliztli',
          'project-subtitle':'<span class="title-accent">Tecnolog\u00edas</span> para Encontrar a Quienes nos Faltan',
          'hero-tagline-static':'Teknoloj\u00edayoh ika',
          'word-1':'temoa.',
          'word-2':'quilnamictia.',
          'word-3':'tlatepanita.',
          'word-4':'quipantlalia.',
          'word-5':'yolpakilistli quimacatia.',
          'hero-main-text':'124,354 tl\u0101cameh tlahcuil\u014dlmeh quen pol\u012bhuihqueh ipan M\u0113xihco. Ipan sesen inin caso cah se familia tlatehu\u00eda tlanemilistli. <strong>FOUND</strong> quimixnextia tehnolog\u00edayoh huan tlamatiliztli in familias buscadoras para momachtia, quitemoa, quipantlalia huan quinemililia yancuic tlanemilistli ipan sistema.',
          'hero-team-text':'In totequitlacauh quinnechicoa <strong>in colectivoh in familias tlen Jalisco huan Zacatecas tlen quitemoa in inpilhuan polihqueh</strong>, oc nochi CentroGeo, in Universidad de Oxford, in Comisi\u00f3n de B\u00fasqueda de Jalisco, in Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) huan in Universidad de Guadalajara. Timoitayoh ika in tlaneltililmeh tlen FCDO, in Oficina Ejecutiva del Secretario General de la ONU, UBPD, in Comisi\u00f3n Nacional de B\u00fasqueda, LAB-Co huan Luis Fondebrider.',
          'collab-title':'Alianzas institucionales',
          'tech-title':'Teknoloj\u00edayoh tlen motequiti',
          'tech-item-1':'Multispectral &amp; Hyperspectral Imaging',
          'tech-item-2':'Airborne LiDAR',
          'tech-item-3':'Seismic Noise Interferometry (TIRSA)',
          'tech-item-4':'Electrical Resistivity Tomography, Conductivimetry',
          'tech-item-5':'Satellite Spectral Analysis',
          'tech-item-ml':'Machine Learning',
          'tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science',
          'buscadoras-title':'In papel in buscadoras',
          'buscadoras-text':'In colectivoh de buscadoras cah ipan yollotl in tequitl tlen FOUND. Yehuan quipatlaqueh in tlajtol ipan pa\u00eds tlen polihuiliztli huan tlayectlaliz (justicia). Inintequiti tlen temoa, tlen tlapanextia de inin nemilistli, mochihua se tlamatiliztli forense huecapan. FOUND quincaca, momachtia huan quincalaquia inintequiti ipan inin teknol\u00f3gicoh tequitl.',
          'social-title':'Xiquito in totlanejmachtiliz',
          'social-subtitle':'Ximoyetkixtia inin tlen tipantlaliah, tlen tlanechicoliztli in comunidades huan inin tlen timocoyonaltiah san sejco.',
          'footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.',
          'stat-label-1':'Tl\u0101cameh pol\u012bhuihqueh',
          'stat-label-2':'Teknoloj\u00edayoh',
          'stat-label-3':'Tlaneltililmeh',
          'stat-label-4':'Tl\u0101ltlameh',
          'collab-item-7':'Colectivoh de B\u00fasqueda',
          'collab-note-7':'Teyacanaliztli, tlamatiliztli ipan tlalli',
          'collab-item-1':'Oficina Ejecutiva del Secretario General de la ONU',
          'collab-note-1':'Internacional tlapalewiliztli',
          'collab-item-2':'FCDO (Reino Unido)',
          'collab-note-2':'Pol\u00edtica, tomin, tlaneltiliztli',
          'collab-item-3':'CentroGeo',
          'collab-note-3':'Co-teyacanani, teknikoh tlamatiliztli',
          'collab-item-4':'Universidad de Guadalajara (UdeG)',
          'collab-note-4':'Teknikoh tlamatiliztli, sitios experimentales',
          'collab-item-5':'UBPD (Colombia)',
          'collab-note-5':'Casos, intercambio t\u00e9cnico',
          'collab-item-6':'Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico',
          'collab-note-6':'Nacional tlanechicol',
          'collab-item-8':'Embajada Brit\u00e1nica ipan M\u00e9xico',
          'collab-note-8':'Tomin, coordinaci\u00f3n',
          'collab-item-9':'Oxford Festival of the Arts',
          'collab-note-9':'Oxford Forum',
          'collab-item-10':'University of Bath',
          'collab-note-10':'Teknikoh tlamatiliztli',
          'collab-item-bafa':'British Association for Forensic Anthropology',
          'collab-note-bafa':'Forense tlamatiliztli',
          'collab-item-jalisco':'Comisi\u00f3n de B\u00fasqueda de Jalisco',
          'collab-note-jalisco':'Teknikoh tlamatiliztli, coordinaci\u00f3n',
          'collab-item-oxford':'Universidad de Oxford',
          'collab-note-oxford':'Co-teyacanani, teknikoh tlamatiliztli',
          'collab-item-secihti':'Secretar\u00eda de Ciencia y Tecnolog\u00eda de M\u00e9xico',
          'collab-note-secihti':'Tomin, pol\u00edtica',
          'collab-item-unam-geo':'UNAM \u2013 Geof\u00edsica',
          'collab-note-unam-geo':'Teknikoh tlamatiliztli',
          'collab-item-unam-eng':'UNAM \u2013 Ingenier\u00eda',
          'collab-note-unam-eng':'Teknikoh tlamatiliztli',
          'collab-item-fth':'Frontier Tech Hub',
          'collab-note-fth':'Tomin, teknikoh tlamatiliztli',
          'collab-item-dtg':'DT Global',
          'collab-note-dtg':'Tomin, teknikoh tlamatiliztli',
          'collab-item-upzmg':'UPZMG',
          'collab-note-upzmg':'Sitio experimental',
          'collab-item-uwe':'UWE Bristol',
          'collab-note-uwe':'Tomin, teknikoh tlamatiliztli'
        }
      };

      let heroWords = [];
      let wordIndex = 0;
      let wordInterval = null;

      function buildHeroWords(lang){
        var dict = translations[lang] || translations.en;
        var keys = ['word-1','word-2','word-3','word-4','word-5'];
        heroWords = keys.map(function(k){ return dict[k]; }).filter(Boolean);
        wordIndex = 0;
        var span = document.getElementById('hero-word');
        if(span && heroWords.length){ span.textContent = heroWords[0]; }
      }

      function startWordRotation(){
        var span = document.getElementById('hero-word');
        if(wordInterval){ clearInterval(wordInterval); }
        if(!span || heroWords.length < 2){ return; }
        wordInterval = setInterval(function(){
          span.classList.add('fading-out');
          setTimeout(function(){
            wordIndex = (wordIndex + 1) % heroWords.length;
            span.textContent = heroWords[wordIndex];
            span.classList.remove('fading-out');
            span.classList.add('fading-in');
            requestAnimationFrame(function(){
              requestAnimationFrame(function(){
                span.classList.remove('fading-in');
              });
            });
          }, 300);
        }, 1800);
      }

      function setLanguage(lang){
        var dict = translations[lang] || translations.en;
        Object.keys(dict).forEach(function(id){
          var el = document.getElementById(id);
          if(el){ el.innerHTML = dict[id]; }
        });
        document.documentElement.setAttribute('lang',
          lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en'));
        document.querySelectorAll('.lang-btn').forEach(function(btn){
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });
        try{ localStorage.setItem('found-lang', lang); }catch(e){}
        buildHeroWords(lang);
        startWordRotation();
      }

      /* ===========================
         SCROLL REVEAL
      ============================ */
      function setupScrollReveal(){
        var reveals = document.querySelectorAll('.reveal');
        if(!reveals.length) return;

        if('IntersectionObserver' in window){
          var observer = new IntersectionObserver(function(entries){
            entries.forEach(function(entry){
              if(entry.isIntersecting){
                entry.target.classList.add('is-visible');
              }
            });
          }, { threshold:0.08, rootMargin:'0px 0px -40px 0px' });

          reveals.forEach(function(el){ observer.observe(el); });
        } else {
          // Fallback: show all
          reveals.forEach(function(el){ el.classList.add('is-visible'); });
        }
      }

      /* ===========================
         TOUCH ZOOM
      ============================ */
      function setupTouchZoom(){
        var zoomables = document.querySelectorAll('.touch-zoomable');
        if(!zoomables.length){ return; }
        function toggleZoom(el){
          var isExpanded = el.classList.contains('is-expanded');
          if(isExpanded){
            el.classList.remove('is-expanded');
            document.body.classList.remove('zoom-active');
          } else {
            document.querySelectorAll('.touch-zoomable.is-expanded').forEach(function(o){
              o.classList.remove('is-expanded');
            });
            el.classList.add('is-expanded');
            document.body.classList.add('zoom-active');
          }
        }
        zoomables.forEach(function(el){
          el.addEventListener('click', function(e){
            if(window.matchMedia && window.matchMedia('(max-width: 768px)').matches){
              e.preventDefault();
              e.stopPropagation();
              toggleZoom(el);
            }
          });
        });
        document.addEventListener('keydown', function(e){
          if(e.key === 'Escape'){
            document.querySelectorAll('.touch-zoomable.is-expanded').forEach(function(o){
              o.classList.remove('is-expanded');
            });
            document.body.classList.remove('zoom-active');
          }
        });
      }

      /* ===========================
         INIT
      ============================ */
      document.addEventListener('DOMContentLoaded', function(){
        var savedLang = null;
        try{ savedLang = localStorage.getItem('found-lang'); }catch(e){}
        var initialLang = (savedLang === 'es' || savedLang === 'en' || savedLang === 'nah') ? savedLang : 'en';
        setLanguage(initialLang);

        document.querySelectorAll('.lang-btn').forEach(function(btn){
          btn.addEventListener('click', function(){
            setLanguage(btn.dataset.lang);
          });
        });

        setupTouchZoom();
        setupScrollReveal();
      });
    })();
  </script>

</body>
</html>
