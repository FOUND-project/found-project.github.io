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
      --text-dark:#121212;
      --text-medium:#3f3f3f;
      --text-light:#6b6b6b;
      --border-light:rgba(15, 23, 42, 0.10);
      --shadow-sm:0 2px 10px rgba(15, 23, 42,.06);
      --shadow-md:0 10px 28px rgba(15, 23, 42,.10);
      --shadow-lg:0 18px 48px rgba(15, 23, 42,.14);
      --transition-smooth:cubic-bezier(.4,0,.2,1);
      --radius-lg:22px;
      --radius-md:18px;
      --radius-sm:14px;

      /* Rolling words */
      --word-h: clamp(3rem,6vw,4.2rem);
      --word-duration: 10.5s; /* ✅ adjusted for 5 words */
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
      outline:3px solid rgba(74,140,115,.55);
      outline-offset:2px;
      border-radius:10px;
    }

    /* ==== FORCE Minimal Mistakes wrappers to full width (homepage) ==== */
    .page,
    #main,
    .initial-content,
    .page__inner-wrap,
    .page__content,
    .archive {
      max-width: none !important;
      width: 106% !important; /* keep as requested */
    }

    /* keep sensible side padding so content doesn't touch edges */
    .page__content{
      padding-left: clamp(1rem, 4vw, 3rem) !important;
      padding-right: clamp(1rem, 4vw, 3rem) !important;
    }

    /* =========================================================
       Language toggle
    ========================================================== */
    .lang-toggle{
      position:absolute;
      top:1.4rem;
      right:clamp(1rem,4vw,3rem);
      display:inline-flex;
      gap:.55rem;
      z-index:3;
    }

    .lang-btn{
      border:1px solid rgba(255,255,255,.75);
      background:rgba(0,0,0,.18);
      color:#fff;
      padding:.35rem .85rem;
      border-radius:999px;
      font-size:.82rem;
      font-weight:700;
      letter-spacing:.08em;
      text-transform:uppercase;
      cursor:pointer;
      transition:transform .2s var(--transition-smooth), background .2s var(--transition-smooth), box-shadow .2s var(--transition-smooth), border-color .2s var(--transition-smooth);
      backdrop-filter:blur(10px);
    }

    .lang-btn:hover{
      background:rgba(0,0,0,.28);
      transform:translateY(-1px);
      box-shadow:0 8px 22px rgba(0,0,0,.18);
      border-color:rgba(255,255,255,.9);
    }

    .lang-btn.active{
      background:#fff;
      color:var(--dark-green);
      border-color:#fff;
      box-shadow:0 0 0 1px rgba(0,0,0,.08), 0 10px 26px rgba(0,0,0,.12);
      transform:translateY(-1px);
    }

    /* =========================================================
       Title
    ========================================================== */
    .title-section{
      padding:clamp(3.25rem,8vw,5.5rem) 0 clamp(2.25rem,6vw,4.25rem);
      background:
        radial-gradient(1200px 600px at 15% 35%, rgba(212,175,55,.14) 0%, transparent 55%),
        radial-gradient(900px 520px at 85% 20%, rgba(232,245,240,.10) 0%, transparent 60%),
        linear-gradient(135deg,#0b1c16 0%, #123126 38%, var(--dark-green) 62%, var(--primary-green) 100%);
      position:relative;
      overflow:hidden;
      text-align:center;
      margin-bottom:2.25rem;
      box-shadow:var(--shadow-lg);
      isolation:isolate;
    }

    .title-section::before{
      content:'';
      position:absolute;
      inset:-2px;
      background:
        linear-gradient(90deg, rgba(74,140,115,.14), transparent 35%, transparent 65%, rgba(74,140,115,.12));
      opacity:.85;
      pointer-events:none;
      mask-image:linear-gradient(to bottom, transparent, black 18%, black 82%, transparent);
      -webkit-mask-image:linear-gradient(to bottom, transparent, black 18%, black 82%, transparent);
      z-index:0;
    }

    .title-section::after{
      content:'';
      position:absolute;
      left:50%;
      top:-120px;
      width:720px;
      height:720px;
      transform:translateX(-50%);
      background:
        radial-gradient(circle, rgba(255,255,255,.08) 0%, transparent 55%);
      filter:blur(1px);
      opacity:.55;
      pointer-events:none;
      z-index:0;
    }

    .project-title{
      font-size:clamp(2.6rem,6vw,4.7rem);
      font-weight:900;
      color:#fff;
      margin-bottom:1.2rem;
      letter-spacing:-.03em;
      line-height:1.06;
      text-shadow:0 10px 30px rgba(0,0,0,.28);
      position:relative;
      z-index:1;
    }

    .project-subtitle{
      font-size:clamp(1.25rem,3vw,1.85rem);
      font-weight:500;
      color:rgba(232,245,240,.92);
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.55;
      max-width:980px;
      margin:0 auto;
      position:relative;
      z-index:1;
      text-shadow:0 6px 18px rgba(0,0,0,.22);
      padding:0 clamp(1rem,4vw,3rem);
    }

    .title-accent{color:var(--gold-accent);font-weight:800;}

    /* =========================================================
       Hero
    ========================================================== */
    .hero{
      padding:clamp(2rem,6vw,4rem) 0;
      position:relative;
      overflow:hidden;
    }

    .hero::before{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(800px 420px at 12% 20%, rgba(232,245,240,.70) 0%, transparent 55%),
        radial-gradient(780px 420px at 86% 0%, rgba(212,175,55,.12) 0%, transparent 60%),
        linear-gradient(135deg,#f7fbfa 0%, #ffffff 60%);
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
      grid-template-columns: 1.1fr .9fr;
      gap:clamp(1.25rem,3vw,2.5rem);
      align-items:start;
    }

    @media (max-width: 980px){
      .hero-top{grid-template-columns:1fr;}
    }

    .animated-tagline{
      font-size:clamp(2.05rem,5vw,3.6rem);
      font-weight:900;
      display:flex;
      align-items:flex-start;
      color:var(--dark-green);
      flex-wrap:wrap;
      gap:.75rem;
      letter-spacing:-.03em;
      line-height:1.08;
      margin-bottom:1.25rem;
    }

    .tagline-chip{
      display:inline-flex;
      align-items:center;
      gap:.6rem;
      padding:.5rem .75rem;
      border-radius:999px;
      background:rgba(255,255,255,.75);
      border:1px solid rgba(45,95,77,.12);
      box-shadow:var(--shadow-sm);
      backdrop-filter:blur(10px);
    }

    .tagline-chip::before{
      content:'';
      width:10px;
      height:10px;
      border-radius:50%;
      background:radial-gradient(circle, rgba(212,175,55,.9) 0%, rgba(212,175,55,.25) 60%, transparent 70%);
      box-shadow:0 0 0 4px rgba(212,175,55,.12);
      flex:0 0 auto;
    }

/* --- Rolling words wrapper + sprout --- */
.rolling-wrap{
  display:inline-flex;
  align-items:center;
  gap:.55rem;
}

.word-carousel{
  height:var(--word-h);
  position:relative;
  display:inline-block;
  min-width:clamp(190px,30vw,320px);
  padding:0 .05rem;
  overflow:hidden;
  border-radius:14px;
  background:linear-gradient(135deg, rgba(255,255,255,.72) 0%, rgba(232,245,240,.55) 100%);
  border:1px solid rgba(45,95,77,.14);
  box-shadow:var(--shadow-sm);
  isolation:isolate;
  /* IMPORTANT: no flex here – it must act as a "mask window" */
}

.word-carousel::after{
  content:'';
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    radial-gradient(circle at 20% 30%, rgba(212,175,55,.14) 0%, transparent 45%),
    linear-gradient(180deg, rgba(0,0,0,.06) 0%, transparent 38%, transparent 62%, rgba(0,0,0,.04) 100%);
  opacity:.75;
  z-index:0;
}

.word-list{
  list-style:none;
  margin:0;
  padding:0 .65rem;
  will-change:transform;
  position:relative;
  z-index:1;
  animation:wordSlide var(--word-duration) cubic-bezier(.4,0,.2,1) infinite;
  /* IMPORTANT: no flex + no height: 100% */
}

.word-list li{
  height:var(--word-h);
  display:flex;
  align-items:center;
  justify-content:center;
  color:var(--light-green);
  font-weight:900;
  font-size:clamp(2.05rem,5vw,3.6rem);
  letter-spacing:-.02em;
  text-shadow:0 10px 28px rgba(15,23,42,.10);
  white-space:nowrap;
  flex-shrink:0;
  line-height:1;
  margin:0;
  padding:0;
}

/* ✅ 5 items => 20% steps */
@keyframes wordSlide{
  0%, 15.99%   { transform: translateY(0%); }
  16%, 35.99%  { transform: translateY(-20%); }
  36%, 55.99%  { transform: translateY(-40%); }
  56%, 75.99%  { transform: translateY(-60%); }
  76%, 100%    { transform: translateY(-80%); }
}

    /* ===== Sprout (improved) synced to the word animation (CSS-only) ===== */
  .sprout{
  width:26px;
  height:26px;
  position:relative;
  flex:0 0 auto;
  opacity:.98;
  filter: drop-shadow(0 12px 18px rgba(15,23,42,.14));
  animation:sproutBeat var(--word-duration) cubic-bezier(.4,0,.2,1) infinite;
  transform-origin: bottom center;
}

    /* stem */
    .sprout::before{
      content:'';
      position:absolute;
      left:50%;
      bottom:2px;
      width:4px;
      height:14px;
      transform:translateX(-50%);
      border-radius:999px;
      background:linear-gradient(180deg, rgba(74,140,115,1) 0%, rgba(45,95,77,1) 90%);
      box-shadow:0 0 0 1px rgba(255,255,255,.25) inset;
    }

    /* leaves + bud */
    .sprout::after{
      content:'';
      position:absolute;
      left:50%;
      bottom:9px;
      width:20px;
      height:16px;
      transform:translateX(-50%);
      background:
        radial-gradient(circle at 50% 0%, rgba(212,175,55,.55) 0 18%, transparent 19%), /* tiny bud */
        radial-gradient(ellipse at 30% 70%, rgba(74,140,115,1) 0 58%, transparent 59%),
        radial-gradient(ellipse at 70% 70%, rgba(74,140,115,1) 0 58%, transparent 59%),
        radial-gradient(circle at 30% 70%, rgba(255,255,255,.35) 0 35%, transparent 36%),
        radial-gradient(circle at 70% 70%, rgba(255,255,255,.35) 0 35%, transparent 36%);
      border-radius:999px;
      opacity:.98;
    }

    /* 5 “pops” aligned to the word holds */
    @keyframes sproutBeat{
      0%, 15%   { transform: rotate(-6deg) scale(.92); }
      18%       { transform: rotate(2deg)  scale(1.10); }
      22%       { transform: rotate(-3deg) scale(.96); }

      35%       { transform: rotate(-6deg) scale(.92); }
      38%       { transform: rotate(2deg)  scale(1.10); }
      42%       { transform: rotate(-3deg) scale(.96); }

      55%       { transform: rotate(-6deg) scale(.92); }
      58%       { transform: rotate(2deg)  scale(1.10); }
      62%       { transform: rotate(-3deg) scale(.96); }

      75%       { transform: rotate(-6deg) scale(.92); }
      78%       { transform: rotate(2deg)  scale(1.10); }
      82%       { transform: rotate(-3deg) scale(.96); }

      95%, 100% { transform: rotate(-6deg) scale(.92); }
    }

    .hero-description{
      font-size:clamp(1.08rem,2.4vw,1.25rem);
      color:var(--text-medium);
      max-width:900px;
      line-height:1.85;
      font-weight:450;
      margin-top:.35rem;
    }

    .hero-description strong{
      color:var(--primary-green);
      font-weight:750;
      background:linear-gradient(120deg, rgba(232,245,240,.95) 0%, transparent 100%);
      padding:.08rem .32rem;
      border-radius:6px;
    }

    /* Smaller, card-like hero media (as requested) */
    .hero-media{
      position:relative;
      border-radius:var(--radius-lg);
      overflow:hidden;
      border:1px solid rgba(45,95,77,.14);
      background:linear-gradient(135deg, rgba(232,245,240,.8) 0%, rgba(255,255,255,.9) 100%);
      box-shadow:var(--shadow-md);
      transform:translateY(0);
      transition:transform .45s var(--transition-smooth), box-shadow .45s var(--transition-smooth);
      max-width:520px;
      margin-left:auto;
    }

    @media (max-width: 980px){
      .hero-media{max-width:680px; margin:1rem 0 0;}
    }

    .hero-media:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
    }

    .hero-media::before{
      content:'';
      display:block;
      padding-top:62%;
    }

    .hero-image{
      position:absolute;
      inset:0;
      width:100%;
      height:100%;
      object-fit:cover;
      transform:scale(1.01);
      transition:transform .8s var(--transition-smooth), filter .8s var(--transition-smooth);
      filter:saturate(1.02) contrast(1.03);
    }

    .hero-media:hover .hero-image{transform:scale(1.06);}

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

    /* =========================================================
       Sections
    ========================================================== */
    .content-section{
      padding:clamp(2.75rem,5.2vw,4.5rem) 0;
      border-bottom:1px solid var(--border-light);
      scroll-margin-top:2rem;
      position:relative;
    }
    .content-section:last-of-type{border-bottom:none;}

    .section-container{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    h2{
      font-size:clamp(1.85rem,4vw,2.85rem);
      font-weight:900;
      color:var(--dark-green);
      margin-bottom:1.35rem;
      letter-spacing:-.02em;
      position:relative;
      padding-bottom:1rem;
      line-height:1.25;
    }

    h2::after{
      content:'';
      position:absolute;
      bottom:0; left:0;
      width:88px; height:4px;
      background:linear-gradient(90deg,var(--light-green),var(--primary-green));
      border-radius:999px;
    }

    .info-list{
      list-style:none;
      padding-left:0;
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));
      gap:1rem 1.75rem;
      margin-top:1.25rem;
    }

    .info-list li{
      padding:.9rem 1rem .9rem 2.55rem;
      position:relative;
      color:var(--text-medium);
      font-size:clamp(.98rem,2.25vw,1.05rem);
      transition:transform .25s var(--transition-smooth), box-shadow .25s var(--transition-smooth), border-color .25s var(--transition-smooth), background .25s var(--transition-smooth), color .25s var(--transition-smooth);
      min-height:46px;
      display:flex;
      align-items:center;
      line-height:1.5;
      border-radius:var(--radius-sm);
      background:rgba(255,255,255,.7);
      border:1px solid rgba(45,95,77,.10);
      box-shadow:var(--shadow-sm);
      backdrop-filter:blur(8px);
    }

    .info-list li:hover{
      color:var(--primary-green);
      transform:translateY(-3px);
      box-shadow:var(--shadow-md);
      border-color:rgba(74,140,115,.45);
      background:#fff;
    }

    .info-list li::before{
      content:"✓";
      position:absolute;
      left:.75rem;
      color:var(--light-green);
      font-weight:900;
      font-size:1.05rem;
      transition:transform .25s var(--transition-smooth), background .25s var(--transition-smooth), color .25s var(--transition-smooth);
      top:50%;
      transform:translateY(-50%);
      background:rgba(232,245,240,.95);
      width:28px; height:28px;
      border-radius:50%;
      display:flex;
      align-items:center;
      justify-content:center;
      box-shadow:0 8px 22px rgba(15,23,42,.08);
    }

    .info-list li:hover::before{
      transform:translateY(-50%) scale(1.08);
      background:var(--light-green);
      color:#fff;
    }

    /* =========================================================
       Technologies: smaller images + partnership-card feel
    ========================================================== */
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

    .image-gallery{
      margin-top:2.15rem;
      display:grid;
      grid-template-columns:repeat(12,1fr);
      gap:clamp(.75rem,1.25vw,1.05rem);
    }

    .gallery-item{
      grid-column:span 3;
      border-radius:18px;
      overflow:hidden;
      box-shadow:var(--shadow-md);
      border:1px solid rgba(45,95,77,.10);
      background:linear-gradient(180deg, rgba(232,245,240,.35) 0%, rgba(255,255,255,.9) 100%);
      position:relative;
      transform:translateY(0);
      transition:transform .35s var(--transition-smooth), box-shadow .35s var(--transition-smooth);
      aspect-ratio: 4 / 3;
      min-height:0;
    }

    .gallery-item::after{
      content:'';
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 20% 20%, rgba(212,175,55,.12) 0%, transparent 45%),
        linear-gradient(180deg, rgba(0,0,0,.06) 0%, transparent 45%);
      opacity:0;
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
      transition:transform .65s var(--transition-smooth);
    }

    .gallery-item:hover img{transform:scale(1.06);}

    @media (max-width: 1100px){
      .image-gallery{grid-template-columns:repeat(6,1fr);}
      .gallery-item{grid-column:span 3;}
    }

    @media (max-width: 700px){
      .image-gallery{grid-template-columns:repeat(2,1fr);}
      .gallery-item{grid-column:span 2; aspect-ratio: 16 / 10;}
    }

    /* =========================================================
       Buscadoras
    ========================================================== */
    .buscadoras-section{
      background:
        radial-gradient(circle at 15% 20%, rgba(212,175,55,.10) 0%, transparent 52%),
        radial-gradient(circle at 85% 0%, rgba(232,245,240,.55) 0%, transparent 60%),
        linear-gradient(135deg,#fff8f5 0%,#fff 55%);
      padding:clamp(3.25rem,7vw,5.5rem) 0;
      margin:0;
      position:relative;
      overflow:hidden;
      border-top:1px solid rgba(0,0,0,.04);
      border-bottom:1px solid rgba(0,0,0,.04);
    }

    .buscadoras-content{
      max-width:1100px;
      margin:0 auto;
      text-align:center;
      padding:0 clamp(1rem,4vw,3rem);
      background:rgba(255,255,255,.72);
      border:1px solid rgba(45,95,77,.12);
      border-radius:26px;
      box-shadow:var(--shadow-lg);
      padding-top:clamp(1.75rem,3vw,2.75rem);
      padding-bottom:clamp(1.75rem,3vw,2.75rem);
      backdrop-filter:blur(10px);
      position:relative;
      isolation:isolate;
    }

    .buscadoras-content::after{
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

    .buscadoras-content > *{position:relative; z-index:1;}

    .buscadoras-image{
      border-radius:24px;
      box-shadow:var(--shadow-lg);
      border:1px solid rgba(45,95,77,.12);
      overflow:hidden;
      margin:2.1rem auto 0;
      max-width:520px;
      position:relative;
      transform:translateY(0);
      transition:transform .35s var(--transition-smooth), box-shadow .35s var(--transition-smooth);
      background:#fff;
    }

    .buscadoras-image:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
    }

    .buscadoras-image img{
      width:100%;
      height:auto;
      display:block;
      transform:scale(1.01);
      transition:transform .7s var(--transition-smooth);
    }

    .buscadoras-image:hover img{transform:scale(1.05);}

    /* =========================================================
       Institutional Partnerships
    ========================================================== */
    .collab-wrap{margin-top:2rem;}

    .collab-grid{
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));
      gap:clamp(1.1rem,2.2vw,1.8rem);
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
      isolation:isolate;
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
      z-index:0;
    }

    .collab-card:hover{
      transform:translateY(-8px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.55);
    }
    .collab-card:hover::before{opacity:1;}

    .collab-logo{
      padding:1.15rem 1.15rem .65rem;
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
      filter:grayscale(25%) brightness(1.06);
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
      background:linear-gradient(180deg, rgba(232,245,240,.25) 0%, rgba(255,255,255,.92) 100%);
      position:relative;
      z-index:1;
    }

    .collab-name{
      font-weight:850;
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

    /* Search Collectives GIF: fill header area */
    .collab-card-gif .collab-logo{
      padding:0 !important;
      min-height:0 !important;
      height:168px;
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
      transition:transform .8s var(--transition-smooth);
    }

    .collab-card-gif:hover .collab-logo img{transform:scale(1.06);}

    /* =========================================================
       Social
    ========================================================== */
    .social-section{
      background:
        radial-gradient(900px 520px at 20% 0%, rgba(232,245,240,.75) 0%, transparent 55%),
        linear-gradient(135deg, rgba(232,245,240,.65) 0%, #fff 68%);
      padding:clamp(3rem,6vw,5rem) 0;
      margin:0;
      position:relative;
      overflow:hidden;
    }

    .social-container{
      max-width:1600px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    .section-title{
      font-size:clamp(2rem,5vw,3.2rem);
      font-weight:900;
      color:var(--dark-green);
      margin-bottom:1rem;
      text-align:center;
      letter-spacing:-.03em;
      line-height:1.15;
    }

    .section-subtitle{
      font-size:clamp(1.1rem,2.5vw,1.3rem);
      color:var(--text-medium);
      text-align:center;
      margin-bottom:3rem;
      max-width:900px;
      margin-left:auto;
      margin-right:auto;
      line-height:1.7;
    }

    .social-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));
      gap:clamp(1.25rem,2.6vw,2.25rem);
      align-items:start;
    }

    .social-embed{
      background:#fff;
      border-radius:20px;
      padding:1.25rem;
      box-shadow:var(--shadow-lg);
      display:flex;
      align-items:center;
      justify-content:center;
      min-height:420px;
      transition:transform .35s var(--transition-smooth), box-shadow .35s var(--transition-smooth), border-color .35s var(--transition-smooth);
      border:1px solid rgba(45,95,77,.12);
      overflow:hidden;
      position:relative;
    }

    .social-embed:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-lg);
      border-color:rgba(74,140,115,.50);
    }

    .iframe-container{
      position:relative;
      width:100%;
      max-width:560px;
      overflow:hidden;
      border-radius:16px;
      border:1px solid rgba(15,23,42,.08);
      box-shadow:0 10px 30px rgba(15,23,42,.08);
    }

    .iframe-container iframe{width:100%;border:0;display:block;}

    /* =========================================================
       Footer
    ========================================================== */
    .footer{
      text-align:center;
      padding:clamp(3.5rem,7vw,5.5rem) 0;
      margin-top:0;
      border-top:1px solid var(--border-light);
      background:
        radial-gradient(900px 520px at 80% 0%, rgba(232,245,240,.75) 0%, transparent 55%),
        linear-gradient(135deg,#f8fcfb 0%,#fff 72%);
      position:relative;
      overflow:hidden;
    }

    .footer-content{
      max-width:1400px;
      margin:0 auto;
      padding:0 clamp(1rem,4vw,3rem);
    }

    .footer em{
      font-size:clamp(1.22rem,3vw,1.65rem);
      color:var(--dark-green);
      font-weight:850;
      font-style:italic;
      letter-spacing:.02em;
      line-height:1.6;
      display:inline-block;
      max-width:100%;
      padding:.95rem 1.35rem;
      border-radius:16px;
      background:linear-gradient(135deg, rgba(232,245,240,.95) 0%, transparent 100%);
      border:1px solid rgba(45,95,77,.10);
      box-shadow:var(--shadow-sm);
    }

    html{scroll-behavior:smooth;}

    @media (max-width:768px){
      .animated-tagline{flex-direction:column;align-items:flex-start;gap:.6rem;}
      .word-carousel{min-width:220px;}
      .social-grid{grid-template-columns:1fr;}
      .hero-media{margin-left:0;}
    }

    /* Keep your 106% on desktop, but prevent phone overflow */
    @media (max-width: 768px){
      .page, #main, .initial-content, .page__inner-wrap, .page__content, .archive{
        width: 100% !important;
      }
      .word-carousel{ min-width: 0; width: 100%; max-width: 520px; }
      .word-list li{ white-space: normal; }
    }

/* ==========================
   Award Highlight Card
   ========================== */
.award-highlight{
  margin: 1.5rem 0 2.25rem;
}

.award-card{
  display:flex;
  flex-wrap:wrap;
  align-items:flex-start;
  gap:1.25rem;
  padding:1.35rem 1.6rem;
  border-radius:20px;
  background:
    radial-gradient(circle at 5% 0%, rgba(212,175,55,.18) 0%, transparent 55%),
    linear-gradient(135deg, #fff9ec 0%, #fffdf7 45%, #ffffff 100%);
  border:1px solid rgba(212,175,55,.35);
  box-shadow:0 18px 40px rgba(15,23,42,.14);
  text-decoration:none;
  color:var(--text-dark);
  position:relative;
  overflow:hidden;
  transition:
    transform .3s var(--transition-smooth),
    box-shadow .3s var(--transition-smooth),
    border-color .3s var(--transition-smooth),
    background .3s var(--transition-smooth);
}

.award-card::before{
  content:'';
  position:absolute;
  inset:-1px;
  background:
    linear-gradient(120deg, rgba(255,255,255,.45), transparent 40%, transparent 60%, rgba(212,175,55,.25));
  mix-blend-mode:soft-light;
  opacity:.9;
  pointer-events:none;
}

.award-card:hover{
  transform:translateY(-4px);
  box-shadow:0 24px 55px rgba(15,23,42,.20);
  border-color:rgba(212,175,55,.65);
}

/* small “glow dot” instead of an emoji */
.award-icon{
  width:40px;
  height:40px;
  border-radius:50%;
  background:
    radial-gradient(circle at 30% 30%, #fff 0%, #fff6d9 30%, #d4af37 60%, #8a6c18 100%);
  box-shadow:
    0 0 0 4px rgba(212,175,55,.25),
    0 16px 30px rgba(15,23,42,.28);
  flex:0 0 auto;
  position:relative;
}

.award-icon::after{
  content:'★';
  position:absolute;
  inset:0;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:1.1rem;
  color:#fffdf2;
  text-shadow:0 1px 3px rgba(0,0,0,.35);
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
  padding:.18rem .65rem;
  border-radius:999px;
  font-size:.75rem;
  font-weight:750;
  letter-spacing:.12em;
  text-transform:uppercase;
  background:rgba(27,77,62,.08);
  color:var(--dark-green);
  border:1px solid rgba(27,77,62,.18);
  margin-bottom:.45rem;
}

.award-pill::before{
  content:'';
  width:6px;
  height:6px;
  border-radius:50%;
  background:radial-gradient(circle, var(--gold-accent) 0%, rgba(212,175,55,.2) 70%);
}

.award-title{
  font-size:clamp(1.1rem,2.2vw,1.35rem);
  font-weight:800;
  letter-spacing:-.02em;
  color:var(--dark-green);
  margin-bottom:.3rem;
}

.award-meta{
  font-size:.9rem;
  color:var(--text-light);
  margin-bottom:.4rem;
}

.award-summary{
  font-size:.95rem;
  color:var(--text-medium);
  line-height:1.6;
}

.award-summary strong{
  color:var(--dark-green);
  font-weight:700;
}

/* small arrow on hover */
.award-card .award-title span.arrow{
  display:inline-block;
  font-size:.95rem;
  transform:translateX(0);
  transition:transform .25s var(--transition-smooth);
}

.award-card:hover .award-title span.arrow{
  transform:translateX(4px);
}

@media (max-width:600px){
  .award-card{
    padding:1.1rem 1.2rem;
  }
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
      <div class="hero-top">
        <div>
          <div class="animated-tagline">
            <span class="tagline-chip"><span id="hero-tagline-static">Using technology to&nbsp;</span></span>

            <!-- Rolling words + sprout -->
            <div class="rolling-wrap" aria-label="Rotating tagline">
              <div class="word-carousel" role="text">
                <ul class="word-list">
                  <li id="word-1">search.</li>
                  <li id="word-2">remember.</li>
                  <li id="word-3">dignify.</li>
                  <li id="word-4">find.</li>
                  <li id="word-5">bring closure.</li>
                </ul>
              </div>
              <span class="sprout" aria-hidden="true"></span>
            </div>
          </div>

          <p class="hero-description" id="hero-main-text">
            124,354 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
            <strong>FOUND</strong> combines technology with the knowledge of searching families to learn, locate, and drive systemic change.
          </p>
        </div>

<div class="award-highlight">
  <a href="/news/#mariela-award" class="award-card">
    <div class="award-icon" aria-hidden="true"></div>
    <div class="award-text">
      <div class="award-pill">Award</div>
      <div class="award-title">
        FOUND's pioneer recognised with the Sir Nicholas Browne Policy and Expertise Award
        <span class="arrow">↗</span>
      </div>
      <div class="award-meta">
        Selected from over 200 nominations across the UK Foreign, Commonwealth &amp; Development Office.
      </div>
    </div>
  </a>
</div>

        <div class="hero-media skeleton" aria-label="Hero media">
          <img
            src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/NDAI5.gif?raw=true"
            alt="FOUND Project team using advanced technology in field search operations"
            class="hero-image loading"
            loading="lazy"
            onload="this.classList.remove('loading'); this.parentElement.classList.remove('skeleton')" />
        </div>
      </div>
    </div>
  </section>

  <!-- Technologies Section -->
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
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true" alt="Specialised search tools and equipment" loading="lazy" class="loading" onload="this.classList.remove('loading')">
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

  <!-- Buscadoras Section -->
  <section class="buscadoras-section" id="buscadoras">
    <div class="buscadoras-content">
      <h2 id="buscadoras-title">The Role of Buscadoras</h2>
      <p class="hero-description" id="buscadoras-text">
        Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.
      </p>
      <div class="buscadoras-image">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolising hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
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
    <img
      src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/bd3ef3bd33596258b2738274017f51a2e2c05186/images/FCDO_logo_960x640.png"
      alt="UK Foreign, Commonwealth & Development Office logo"
      loading="lazy"
      class="loading"
      onload="this.classList.remove('loading')">
  </div>

  <div class="collab-meta">
    <div class="collab-name" id="collab-item-2">
      UK Foreign, Commonwealth &amp; Development Office (FCDO)
    </div>
    <div class="collab-note" id="collab-note-2">
      Policy, Funding, Partnerships
    </div>
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

          <!-- 10. Bath -->
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

          <!-- Mexico’s Science and Technology Secretariat -->
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
    <p class="section-subtitle" id="social-subtitle">
      Our latest findings, community stories, and collaborations
    </p>

    <div class="social-grid">
      <!-- Card 1 -->
      <div class="social-embed">
        <div class="iframe-container">
          <iframe
            src="https://www.linkedin.com/embed/feed/update/urn:li:share:7405294962692595712"
            height="880"
            width="504"
            frameborder="0"
            allowfullscreen
            title="FOUND Project LinkedIn update"
            loading="lazy"></iframe>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="social-embed">
        <div class="iframe-container">
          <iframe
            src="https://www.linkedin.com/embed/feed/update/urn:li:share:7407705201647845376"
            height="880"
            width="504"
            frameborder="0"
            allowfullscreen
            title="FOUND Project LinkedIn update"
            loading="lazy"></iframe>
        </div>
      </div>

      <!-- Guardian / The Guardian tweet -->
      <div class="social-embed twitter-embed">
        <blockquote class="twitter-tweet">
          <p lang="en" dir="ltr">
            Almost a year after I started researching the story, I'm thrilled that my
            <a href="https://twitter.com/guardian?ref_src=twsrc%5Etfw">@guardian</a>
            article about the innovations being used to try and find some of the thousands
            of people who have disappeared in Mexico is the most read in its Global Development section.
            <a href="https://t.co/NztFCj4uEF">https://t.co/NztFCj4uEF</a>
          </p>
          &mdash; Suzanne Bearne (@sbearne)
          <a href="https://twitter.com/sbearne/status/1991827389375193330?ref_src=twsrc%5Etfw">
            November 21, 2025
          </a>
        </blockquote>
      </div>

      <!-- Card 3 -->
      <div class="social-embed">
        <div class="iframe-container">
          <iframe
            src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728"
            height="880"
            width="504"
            frameborder="0"
            allowfullscreen
            title="FOUND Project community engagement"
            loading="lazy"></iframe>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="social-embed">
        <div class="iframe-container">
          <iframe
            src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7343552976185114624"
            height="880"
            width="504"
            frameborder="0"
            allowfullscreen
            title="FCDO LinkedIn post about FOUND Project"
            loading="lazy"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-content">
      <em id="footer-text">FOUND: Interpreting Nature to Find Those We Are Missing</em>
    </div>
  </footer>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

  <!-- LANGUAGE TOGGLE -->
  <script>
    (function() {
      const translations = {
        en: {
          'hero-tagline-static': 'Using technology to&nbsp;',
          'word-1': 'search.',
          'word-2': 'remember.',
          'word-3': 'dignify.',
          'word-4': 'find.',
          'word-5': 'bring closure.',
          'hero-main-text': '124,354 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> combines technology with the knowledge of searching families to learn, locate, and drive systemic change.',
          'collab-title': 'Institutional Partnerships',
          'tech-title': 'Technologies in Action',
          'tech-item-1': 'Multispectral &amp; Hyperspectral Imaging',
          'tech-item-2': 'Airborne LiDAR',
          'tech-item-3': 'Seismic Noise Interferometry (TIRSA)',
          'tech-item-4': 'Electrical Resistivity Tomography, Conductivimetry Measurements',
          'tech-item-5': 'Satellite Spectral Analysis',
          'tech-item-6': 'Forensic Entomology, Botany, Territorial Analysis, Soil Science',
          'buscadoras-title': 'The Role of Buscadoras',
          'buscadoras-text': 'Women-led collectives are at the heart of FOUND\'s work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.',
          'social-title': 'Follow Our Journey',
          'social-subtitle': 'Stay connected with our latest findings, community stories, and collaborations',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        },
        es: {
          'hero-tagline-static': 'Usando tecnología para&nbsp;',
          'word-1': 'buscar.',
          'word-2': 'recordar.',
          'word-3': 'dignificar.',
          'word-4': 'encontrar.',
          'word-5': 'dar cierre.',
          'hero-main-text': '124,354 personas están registradas como desaparecidas en México. Detrás de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> combina tecnología y saberes de familias buscadoras para aprender del campo, localizar y promover cambios sistémicos.',
          'collab-title': 'Alianzas institucionales',
          'tech-title': 'Tecnologías en acción',
          'tech-item-1': 'Imágenes multiespectrales e hiperespectrales',
          'tech-item-2': 'LiDAR aerotransportado',
          'tech-item-3': 'Interferometría de ruido sísmico (TIRSA)',
          'tech-item-4': 'Tomografía de resistividad eléctrica y mediciones de conductividad',
          'tech-item-5': 'Análisis espectral satelital',
          'tech-item-6': 'Entomología forense, botánica, análisis territorial y ciencia del suelo',
          'buscadoras-title': 'El papel de las buscadoras',
          'buscadoras-text': 'Los colectivos liderados por mujeres están en el corazón del trabajo de FOUND. Han transformado la conversación nacional sobre desaparición y justicia. Sus prácticas de búsqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus métodos en nuestros esfuerzos tecnológicos.',
          'social-title': 'Sigue nuestro camino',
          'social-subtitle': 'Mantente al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        },
        nah: {
          'hero-tagline-static': 'Teknolojíayoh ika&nbsp;',
          'word-1': 'temoa.',
          'word-2': 'quilnamictia.',
          'word-3': 'tlatepanita.',
          'word-4': 'quipantlalia.',
          'word-5': 'yolpakilistli quimacatia.',
          'hero-main-text': '124,354 tlācameh tlahcuilōlmeh quen polīhuihqueh ipan Mēxihco. Ipan sesen inin caso cah se familia tlatehuía tlanemilistli. <strong>FOUND</strong> quimixnextia tehnologíayoh huan tlamatiliztli in familias buscadoras para momachtia, quitemoa, quipantlalia huan quinemililia tlanemilistli yancuic ipan sistema.',
          'collab-title': 'Tlen tlatlanecuiltilis nemilistli (alianzas institucionales)',
          'tech-title': 'Teknolojíayoh tlen motequiti',
          'tech-item-1': 'Multispectral &amp; Hyperspectral Imaging',
          'tech-item-2': 'Airborne LiDAR',
          'tech-item-3': 'Seismic Noise Interferometry (TIRSA)',
          'tech-item-4': 'Electrical Resistivity Tomography, Conductivimetry Measurements',
          'tech-item-5': 'Satellite Spectral Analysis',
          'tech-item-6': 'Forensic Entomology, Botany, Territorial Analysis, Soil Science',
          'buscadoras-title': 'In papel in buscadoras',
          'buscadoras-text': 'In colectivoh de buscadoras cah ipan yollotl in tequitl tlen FOUND. Yehuan quipatlaqueh in tlajtol ipan país tlen polihuiliztli huan tlayectlaliz justice. Inintequiti tlen temoa, tlen tlapanextia de inin nemilistli, mochihua se tlamatiliztli forense huecapan. FOUND quincaca, momachtia huan quincalaquia inintequiti ipan inin teknológicoh tequitl.',
          'social-title': 'Xiquito in totlanejmachtiliz',
          'social-subtitle': 'Ximoyetkixtia inin tlen tipantlaliah, tlen tlanechicoliztli in comunidades huan inin tlen timocoyonaltiah san sejco.',
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
