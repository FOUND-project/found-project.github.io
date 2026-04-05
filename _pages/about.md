---
permalink: /
title:
author_profile: false
classes: wide home-full
redirect_from:
  - /about/
  - /about.html
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..800;1,9..40,300..800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --primary-green:#2d5f4d;--dark-green:#1e4034;--light-green:#4a8c73;
  --accent-green:#e8f5f0;--gold-accent:#d4af37;
  --text-dark:#121212;--text-medium:#3f3f3f;--text-light:#6b6b6b;
  --border-light:rgba(15,23,42,0.10);
  --shadow-sm:0 2px 10px rgba(15,23,42,.06);--shadow-md:0 10px 28px rgba(15,23,42,.10);--shadow-lg:0 18px 48px rgba(15,23,42,.14);
  --transition-smooth:cubic-bezier(.4,0,.2,1);
  --radius-lg:22px;--radius-md:18px;--radius-sm:14px;
  --font-display:'DM Serif Display',Georgia,'Times New Roman',serif;
  --font-body:'DM Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  --font-mono:'JetBrains Mono','SFMono-Regular','Consolas','Liberation Mono','Menlo',monospace;
}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}html{scroll-behavior:auto!important}}
body{font-family:var(--font-body);color:var(--text-dark);line-height:1.7;background:#fff;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;overflow-x:hidden}
body.zoom-active{overflow:hidden}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;background-image:radial-gradient(900px 520px at 18% 18%,rgba(232,245,240,.55) 0%,transparent 60%),radial-gradient(820px 520px at 82% 10%,rgba(212,175,55,.10) 0%,transparent 62%),url("/images/found-bg.svg");background-repeat:no-repeat;background-size:cover;background-position:center;opacity:0.14;transform:translateZ(0)}
@media(prefers-reduced-motion:reduce){body::before{transform:none}}
html{scroll-behavior:smooth}
*:focus-visible{outline:3px solid rgba(74,140,115,.55);outline-offset:2px;border-radius:10px}
.page,#main,.initial-content,.page__inner-wrap,.page__content,.archive{max-width:none!important;width:106%!important}
.page__content{padding-left:clamp(1rem,4vw,3rem)!important;padding-right:clamp(1rem,4vw,3rem)!important}

/* Scroll reveal — safe: gated by JS class on body */
body.reveal-ready .reveal{opacity:0;transform:translateY(24px);transition:opacity .6s var(--transition-smooth),transform .6s var(--transition-smooth)}
body.reveal-ready .reveal.is-visible{opacity:1;transform:translateY(0)}
body.reveal-ready .reveal-delay-2{transition-delay:.18s}

.lang-toggle{position:absolute;top:1.4rem;right:clamp(1rem,4vw,3rem);display:inline-flex;gap:.45rem;z-index:3}
.lang-btn{border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.08);color:rgba(255,255,255,.75);padding:.35rem .85rem;border-radius:999px;font-size:.78rem;font-weight:700;font-family:var(--font-mono);letter-spacing:.09em;text-transform:uppercase;cursor:pointer;backdrop-filter:blur(10px);transition:transform .2s var(--transition-smooth),background .2s var(--transition-smooth),box-shadow .2s var(--transition-smooth),border-color .2s var(--transition-smooth)}
.lang-btn:hover{background:rgba(255,255,255,.16);transform:translateY(-1px);box-shadow:0 8px 22px rgba(0,0,0,.18);border-color:rgba(255,255,255,.7);color:#fff}
.lang-btn.active{background:rgba(255,255,255,.95);color:var(--dark-green);border-color:rgba(255,255,255,.95);box-shadow:0 0 0 1px rgba(0,0,0,.08),0 10px 26px rgba(0,0,0,.12);transform:translateY(-1px)}

.title-section{padding:clamp(3.5rem,7vw,5.5rem) 0 clamp(2rem,5vw,3.5rem);background:radial-gradient(1200px 600px at 15% 35%,rgba(212,175,55,.14) 0%,transparent 55%),radial-gradient(900px 520px at 85% 20%,rgba(232,245,240,.10) 0%,transparent 60%),linear-gradient(135deg,#0b1c16 0%,#123126 38%,var(--dark-green) 62%,var(--primary-green) 100%);position:relative;overflow:hidden;margin-bottom:2rem;box-shadow:var(--shadow-lg);isolation:isolate}
.title-section::before{content:'';position:absolute;inset:-2px;background:linear-gradient(90deg,rgba(74,140,115,.14),transparent 35%,transparent 65%,rgba(74,140,115,.12));opacity:.85;pointer-events:none;mask-image:linear-gradient(to bottom,transparent,black 18%,black 82%,transparent);-webkit-mask-image:linear-gradient(to bottom,transparent,black 18%,black 82%,transparent);z-index:0}
.title-section::after{content:'';position:absolute;left:50%;top:-120px;width:720px;height:720px;transform:translateX(-50%);background:radial-gradient(circle,rgba(255,255,255,.08) 0%,transparent 55%);filter:blur(1px);opacity:.55;pointer-events:none;z-index:0}
.title-inner{max-width:1200px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem);position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:1.4rem}
.title-brand{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:1.1rem}
.project-logo{width:110px;height:auto;border-radius:18px;box-shadow:0 14px 32px rgba(0,0,0,.45);border:1px solid rgba(255,255,255,.75);background:rgba(255,255,255,.06);padding:8px;flex-shrink:0}
.project-title{font-size:clamp(2.8rem,6.5vw,5rem);font-weight:900;color:#fff;letter-spacing:.08em;line-height:1.06;text-shadow:0 10px 30px rgba(0,0,0,.28);font-family:var(--font-body)}
.project-subtitle{font-size:clamp(1.15rem,2.5vw,1.6rem);font-weight:400;color:rgba(232,245,240,.85);font-family:var(--font-display);font-style:italic;letter-spacing:.02em;line-height:1.55;max-width:980px;margin:0 auto;text-align:center;text-shadow:0 6px 18px rgba(0,0,0,.22);padding:0 clamp(1rem,4vw,3rem)}
.title-accent{color:var(--gold-accent)}
.title-divider{width:72px;height:1.5px;background:linear-gradient(90deg,transparent,var(--gold-accent),transparent);border:none;margin:.1rem auto 0;opacity:.55}

.hero{padding:clamp(1.75rem,4vw,3rem) 0;position:relative;overflow:hidden}
.title-section,.hero{background-color:transparent}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(800px 420px at 12% 20%,rgba(232,245,240,.70) 0%,transparent 55%),radial-gradient(780px 420px at 86% 0%,rgba(212,175,55,.12) 0%,transparent 60%),linear-gradient(135deg,#f7fbfa 0%,#ffffff 60%);z-index:0}
.hero-content{position:relative;z-index:1;max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.hero-top{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(1.25rem,3vw,2.5rem);align-items:start}
.hero-text{display:flex;flex-direction:column;gap:1rem;max-width:720px}
.animated-tagline{font-size:clamp(2.05rem,5vw,3.6rem);font-weight:900;display:flex;align-items:flex-start;color:var(--dark-green);flex-wrap:wrap;gap:.75rem;letter-spacing:-.03em;line-height:1.08}
.tagline-pill{display:inline-flex;flex-direction:column;align-items:flex-start;justify-content:flex-start;padding:.7rem 1.4rem;border-radius:999px;background:linear-gradient(135deg,rgba(255,255,255,.9) 0%,rgba(232,245,240,.8) 100%);border:1px solid rgba(45,95,77,.16);box-shadow:var(--shadow-sm);white-space:normal}
.tagline-pill span#hero-tagline-static{display:block;width:100%;font-size:clamp(2rem,4.5vw,3.2rem);font-weight:900;color:var(--dark-green);letter-spacing:-.03em;line-height:1.1;text-align:left}
.word-carousel{margin-top:.15rem;width:100%;display:flex;align-items:center;justify-content:center}
.hero-word{display:block;font-size:clamp(1.9rem,4.4vw,3rem);font-weight:900;letter-spacing:-.02em;color:var(--light-green);text-shadow:0 10px 28px rgba(15,23,42,.10);white-space:nowrap;text-align:center;transition:opacity .28s var(--transition-smooth),transform .28s var(--transition-smooth);opacity:1;transform:translateY(0);font-family:var(--font-display);font-style:italic}
.hero-word.fading-out{opacity:0;transform:translateY(-6px)}
.hero-word.fading-in{opacity:0;transform:translateY(6px)}
.hero-description{font-size:clamp(1.05rem,2.4vw,1.25rem);color:var(--text-medium);max-width:900px;line-height:1.85;font-weight:450}
.hero-description strong{color:var(--primary-green);font-weight:750;background:linear-gradient(120deg,rgba(232,245,240,.95) 0%,transparent 100%);padding:.08rem .32rem;border-radius:6px}
.hero-side{display:flex;flex-direction:column;gap:1rem;align-items:stretch;min-height:100%}

.award-highlight{margin-top:0}
.award-card{display:flex;flex-wrap:wrap;align-items:flex-start;gap:1.1rem;padding:1.25rem 1.5rem;border-radius:20px;background:radial-gradient(circle at 5% 0%,rgba(212,175,55,.18) 0%,transparent 55%),linear-gradient(135deg,#fff9ec 0%,#fffdf7 45%,#ffffff 100%);border:1px solid rgba(212,175,55,.35);box-shadow:0 18px 40px rgba(15,23,42,.14);text-decoration:none;color:var(--text-dark);position:relative;overflow:hidden;transition:transform .3s var(--transition-smooth),box-shadow .3s var(--transition-smooth),border-color .3s var(--transition-smooth),background .3s var(--transition-smooth)}
.award-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,rgba(212,175,55,.3),var(--gold-accent),rgba(212,175,55,.3));opacity:.8;pointer-events:none}
.award-card:hover{transform:translateY(-4px);box-shadow:0 24px 55px rgba(15,23,42,.20);border-color:rgba(212,175,55,.65)}
.award-text{flex:1 1 220px;position:relative;z-index:1}
.award-pill{display:inline-flex;align-items:center;gap:.4rem;padding:.18rem .65rem;border-radius:999px;font-size:.72rem;font-weight:750;letter-spacing:.12em;text-transform:uppercase;background:rgba(27,77,62,.08);color:var(--dark-green);border:1px solid rgba(27,77,62,.18);margin-bottom:.45rem;font-family:var(--font-mono)}
.award-pill::before{content:'';width:6px;height:6px;border-radius:50%;background:radial-gradient(circle,var(--gold-accent) 0%,rgba(212,175,55,.2) 70%)}
.award-title{font-size:clamp(1.1rem,2.2vw,1.35rem);font-weight:800;letter-spacing:-.02em;color:var(--dark-green);margin-bottom:.3rem}
.award-title span.arrow{display:inline-block;font-size:.95rem;transform:translateX(0);transition:transform .25s var(--transition-smooth)}
.award-card:hover .award-title span.arrow{transform:translateX(4px)}
.award-meta{font-size:.9rem;color:var(--text-light)}

.hero-team-bar{position:relative;z-index:1;margin-top:clamp(1.25rem,2.5vw,2rem);padding:clamp(.75rem,1.5vw,1.1rem) clamp(1rem,4vw,3rem);background:rgba(11,28,22,.82);backdrop-filter:blur(12px);border-top:1px solid rgba(74,140,115,.22);border-bottom:1px solid rgba(74,140,115,.12)}
.hero-team-bar-inner{max-width:1400px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:baseline;gap:.4rem 1rem;font-size:clamp(.8rem,1.6vw,.92rem);color:rgba(232,245,240,.78);font-family:var(--font-mono);line-height:1.65}
.htb-label{color:var(--gold-accent);font-weight:700;letter-spacing:.04em;white-space:nowrap;flex-shrink:0}
.htb-brace{color:rgba(74,140,115,.9);font-weight:400}
.htb-divider{color:rgba(74,140,115,.5);font-size:1rem;flex-shrink:0}
.htb-text{font-family:var(--font-body);font-size:clamp(.82rem,1.6vw,.92rem);color:rgba(232,245,240,.80);letter-spacing:.01em}
.htb-text strong{color:rgba(232,245,240,.97);font-weight:650}

.content-section{padding:clamp(2.5rem,5vw,4.25rem) 0;border-bottom:1px solid var(--border-light);position:relative;scroll-margin-top:2rem}
.content-section:last-of-type{border-bottom:none}
.section-container{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.section-divider{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.section-divider hr{border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(45,95,77,.12),rgba(212,175,55,.08),rgba(45,95,77,.12),transparent)}

h2{font-size:clamp(1.85rem,4vw,2.85rem);font-weight:400;font-family:var(--font-display);color:var(--dark-green);margin-bottom:1.35rem;letter-spacing:0;position:relative;padding-bottom:1rem;line-height:1.25}
h2::after{content:'';position:absolute;bottom:0;left:0;width:60px;height:3px;background:linear-gradient(90deg,var(--gold-accent),rgba(212,175,55,.25));border-radius:999px}

.dual-sections-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,0.9fr);gap:clamp(2rem,4vw,3rem);align-items:stretch}
.dual-column{min-width:0}
#technologies{background:radial-gradient(circle at 20% 15%,rgba(232,245,240,.75) 0%,transparent 52%),radial-gradient(circle at 80% 0%,rgba(212,175,55,.10) 0%,transparent 55%),linear-gradient(135deg,#f8fcfb 0%,#fff 60%);border-radius:26px;padding:clamp(1.75rem,3vw,2.5rem);border:1px solid rgba(45,95,77,.10);box-shadow:var(--shadow-md);position:relative;overflow:hidden}
#technologies::before{content:'';position:absolute;inset:-2px;background:linear-gradient(90deg,rgba(74,140,115,.12),transparent 35%,transparent 65%,rgba(74,140,115,.10));opacity:.6;pointer-events:none;mask-image:linear-gradient(to bottom,transparent,black 18%,black 82%,transparent);-webkit-mask-image:linear-gradient(to bottom,transparent,black 18%,black 82%,transparent)}
.info-list{list-style:none;padding-left:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:1rem 1.75rem;margin-top:1.25rem}
.info-list li{padding:.9rem 1rem .9rem 2.55rem;position:relative;color:var(--text-medium);font-size:clamp(.98rem,2.25vw,1.05rem);min-height:46px;display:flex;align-items:center;line-height:1.5;border-radius:var(--radius-sm);background:rgba(255,255,255,.7);border:1px solid rgba(45,95,77,.10);box-shadow:var(--shadow-sm);backdrop-filter:blur(8px);transition:transform .25s var(--transition-smooth),box-shadow .25s var(--transition-smooth),border-color .25s var(--transition-smooth),background .25s var(--transition-smooth),color .25s var(--transition-smooth)}
.info-list li::before{content:"✓";position:absolute;left:.75rem;top:50%;transform:translateY(-50%);color:var(--light-green);font-weight:900;font-size:1.05rem;background:rgba(232,245,240,.95);width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 22px rgba(15,23,42,.08);transition:transform .25s var(--transition-smooth),background .25s var(--transition-smooth),color .25s var(--transition-smooth)}
.info-list li:hover{color:var(--primary-green);transform:translateY(-3px);box-shadow:var(--shadow-md);border-color:rgba(74,140,115,.45);background:#fff}
.info-list li:hover::before{transform:translateY(-50%) scale(1.08);background:var(--light-green);color:#fff}
.image-gallery{margin-top:2.15rem;display:grid;grid-template-columns:repeat(12,1fr);gap:clamp(.75rem,1.25vw,1.05rem)}
.gallery-item{grid-column:span 3;border-radius:18px;overflow:hidden;box-shadow:var(--shadow-md);border:1px solid rgba(45,95,77,.10);background:linear-gradient(180deg,rgba(232,245,240,.35) 0%,rgba(255,255,255,.9) 100%);position:relative;transform:translateY(0);transition:transform .35s var(--transition-smooth),box-shadow .35s var(--transition-smooth);aspect-ratio:4/3;min-height:0}
.gallery-item::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 20% 20%,rgba(212,175,55,.12) 0%,transparent 45%),linear-gradient(180deg,rgba(0,0,0,.06) 0%,transparent 45%);opacity:0;transition:opacity .35s var(--transition-smooth);pointer-events:none}
.gallery-item img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.01);transition:transform .65s var(--transition-smooth),opacity .4s ease}
.gallery-item img.loading{opacity:0}
.gallery-item:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.gallery-item:hover::after{opacity:1}
.gallery-item:hover img{transform:scale(1.06)}
.buscadoras-section{background:radial-gradient(circle at 15% 20%,rgba(212,175,55,.10) 0%,transparent 52%),radial-gradient(circle at 85% 0%,rgba(232,245,240,.55) 0%,transparent 60%),linear-gradient(135deg,#fff8f5 0%,#fff 55%);border-radius:26px;padding:clamp(1.75rem,3vw,2.5rem);border:1px solid rgba(45,95,77,.10);box-shadow:var(--shadow-md);position:relative;overflow:hidden;display:flex;align-items:stretch}
.buscadoras-content{max-width:100%;margin:0 auto;text-align:center;padding:0 clamp(.5rem,3vw,1.25rem);background:rgba(255,255,255,.72);border-radius:22px;box-shadow:var(--shadow-sm);backdrop-filter:blur(10px);position:relative;isolation:isolate;display:flex;flex-direction:column;justify-content:space-between}
.buscadoras-content::after{content:'';position:absolute;inset:0;border-radius:22px;background:linear-gradient(135deg,rgba(232,245,240,.35) 0%,transparent 35%),radial-gradient(circle at 85% 15%,rgba(212,175,55,.10) 0%,transparent 55%);opacity:.9;pointer-events:none;z-index:0}
.buscadoras-content>*{position:relative;z-index:1}
.buscadoras-text{font-size:clamp(1.02rem,2.2vw,1.18rem);color:var(--text-medium);line-height:1.8;margin-top:.4rem}
.buscadoras-image{border-radius:24px;box-shadow:var(--shadow-lg);border:1px solid rgba(45,95,77,.12);overflow:hidden;margin:1.75rem auto .1rem;max-width:520px;position:relative;transform:translateY(0);transition:transform .35s var(--transition-smooth),box-shadow .35s var(--transition-smooth);background:#fff}
.buscadoras-image img{width:100%;height:auto;display:block;transform:scale(1.01);transition:transform .7s var(--transition-smooth),opacity .4s ease}
.buscadoras-image img.loading{opacity:0}
.buscadoras-image:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.buscadoras-image:hover img{transform:scale(1.05)}

.collab-wrap{margin-top:2rem}
.collab-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:clamp(1.1rem,2.2vw,1.8rem);margin-top:1.5rem}
.collab-card{background:#fff;border-radius:18px;box-shadow:var(--shadow-md);border:1px solid rgba(45,95,77,.10);overflow:hidden;position:relative;transition:transform .35s var(--transition-smooth),box-shadow .35s var(--transition-smooth),border-color .35s var(--transition-smooth);min-height:220px;display:flex;flex-direction:column;justify-content:space-between;isolation:isolate}
.collab-card::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 15% 10%,rgba(232,245,240,.85) 0%,transparent 55%),radial-gradient(circle at 85% 0%,rgba(212,175,55,.12) 0%,transparent 60%);opacity:0;transition:opacity .35s ease;pointer-events:none;z-index:0}
.collab-card:hover{transform:translateY(-8px);box-shadow:var(--shadow-lg);border-color:rgba(74,140,115,.55)}
.collab-card:hover::before{opacity:1}
.collab-logo{padding:1.15rem 1.15rem .65rem;display:flex;align-items:center;justify-content:center;min-height:140px;position:relative;z-index:1}
.collab-logo img{max-width:100%;max-height:95px;width:auto;height:auto;object-fit:contain;filter:grayscale(25%) brightness(1.06);transition:transform .35s var(--transition-smooth),filter .35s var(--transition-smooth),opacity .3s ease}
.collab-img{max-height:80px;width:auto;object-fit:contain;filter:drop-shadow(0 0 1px rgba(0,0,0,.18))}
.collab-logo img.loading{opacity:0}
.collab-card:hover .collab-logo img{filter:grayscale(0%) brightness(1);transform:scale(1.04)}
.collab-meta{padding:.85rem 1.15rem 1.15rem;border-top:1px solid rgba(0,0,0,.06);background:linear-gradient(180deg,rgba(232,245,240,.25) 0%,rgba(255,255,255,.92) 100%);position:relative;z-index:1}
.collab-name{font-weight:850;color:var(--dark-green);font-size:1.02rem;line-height:1.35;letter-spacing:-.01em}
.collab-note{margin-top:.35rem;color:var(--text-light);font-size:.92rem;line-height:1.45}
.collab-card-gif .collab-logo{padding:0!important;min-height:0!important;height:168px;display:block;overflow:hidden;background:#fff}
.collab-card-gif .collab-logo img{max-height:none!important;max-width:none!important;width:100%!important;height:100%!important;object-fit:cover!important;object-position:center 25%;display:block;filter:none!important;transform:scale(1.02);transition:transform .8s var(--transition-smooth),opacity .4s ease}
.collab-card-gif .collab-logo img.loading{opacity:0}
.collab-card-gif:hover .collab-logo img{transform:scale(1.06)}

.social-section{background:radial-gradient(900px 520px at 20% 0%,rgba(232,245,240,.75) 0%,transparent 55%),linear-gradient(135deg,rgba(232,245,240,.65) 0%,#fff 68%);padding:clamp(3rem,6vw,5rem) 0;margin:0;position:relative;overflow:hidden}
.social-container{max-width:1600px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.section-title{font-size:clamp(2rem,5vw,3.2rem);font-weight:400;font-family:var(--font-display);color:var(--dark-green);margin-bottom:1rem;text-align:center;letter-spacing:0;line-height:1.15}
.section-subtitle{font-size:clamp(1.1rem,2.5vw,1.3rem);color:var(--text-medium);text-align:center;margin-bottom:3rem;max-width:900px;margin-left:auto;margin-right:auto;line-height:1.7}
.social-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:clamp(1.25rem,2.6vw,2.25rem);align-items:start}
.social-embed{background:#fff;border-radius:20px;padding:1.25rem;box-shadow:var(--shadow-lg);display:flex;align-items:center;justify-content:center;min-height:420px;border:1px solid rgba(45,95,77,.12);overflow:hidden;position:relative;transition:transform .35s var(--transition-smooth),box-shadow .35s var(--transition-smooth),border-color .35s var(--transition-smooth)}
.social-embed:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:rgba(74,140,115,.50)}
.iframe-container{position:relative;width:100%;max-width:560px;overflow:hidden;border-radius:16px;border:1px solid rgba(15,23,42,.08);box-shadow:0 10px 30px rgba(15,23,42,.08)}
.iframe-container iframe{width:100%;border:0;display:block;height:880px}

.footer{text-align:center;padding:clamp(3.5rem,7vw,5.5rem) 0;margin-top:0;border-top:none;background:radial-gradient(800px 400px at 50% 0%,rgba(74,140,115,.10) 0%,transparent 55%),linear-gradient(180deg,#0e2a1f 0%,#0b1c16 100%);position:relative;overflow:hidden}
.footer-content{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.footer em{font-size:clamp(1.22rem,3vw,1.65rem);color:rgba(232,245,240,.82);font-weight:400;font-family:var(--font-display);font-style:italic;letter-spacing:.02em;line-height:1.6;display:inline-block;max-width:100%}
.footer-line{width:60px;height:1.5px;background:linear-gradient(90deg,transparent,rgba(212,175,55,.45),transparent);border:none;margin:1.25rem auto 0}

@media(max-width:768px){.touch-zoomable{cursor:zoom-in}.touch-zoomable.is-expanded{position:fixed;inset:0;margin:0!important;width:100vw!important;height:100vh!important;max-width:none!important;max-height:none!important;z-index:9999;background:rgba(0,0,0,.9);border-radius:0!important;box-shadow:none!important;padding:0!important;display:flex;align-items:center;justify-content:center}.touch-zoomable.is-expanded img,.touch-zoomable.is-expanded .hero-image{width:100%;height:100%;object-fit:contain;transform:none!important;box-shadow:none!important}}
@media(max-width:1100px){.image-gallery{grid-template-columns:repeat(6,1fr)}.gallery-item{grid-column:span 3}}
@media(max-width:900px){.dual-sections-grid{grid-template-columns:1fr}.hero-top{grid-template-columns:1fr}.hero-side{max-width:520px;margin:0 auto}}
@media(max-width:768px){.page,#main,.initial-content,.page__inner-wrap,.page__content,.archive{width:100%!important}.lang-toggle{top:.9rem}.hero{padding:1.25rem 0 1.75rem}.hero-text{max-width:100%}.animated-tagline{flex-direction:column;align-items:center;gap:.45rem}.tagline-pill{padding:.55rem 1rem;max-width:100%;align-items:center;text-align:center}.tagline-pill span#hero-tagline-static{font-size:clamp(1.6rem,6vw,2rem);text-align:center}.hero-word{font-size:clamp(1.7rem,6vw,2.2rem)}.award-card{padding:1.1rem 1.2rem}.image-gallery{grid-template-columns:repeat(2,1fr)}.gallery-item{grid-column:span 2;aspect-ratio:16/10;max-height:160px;box-shadow:var(--shadow-sm)}.buscadoras-image{max-width:100%;margin-top:1.2rem;box-shadow:var(--shadow-sm)}.collab-card{min-height:auto;box-shadow:var(--shadow-sm)}.collab-logo{min-height:70px;padding:.7rem}.collab-logo img{max-height:60px}.collab-meta{padding:.6rem .8rem .8rem}.collab-name{font-size:.96rem}.collab-note{font-size:.85rem}.social-grid{grid-template-columns:1fr}.social-embed{min-height:auto;box-shadow:var(--shadow-sm)}.iframe-container iframe{height:520px}.project-logo{width:80px}}
@media(max-width:480px){.gallery-item{max-height:140px}.iframe-container iframe{height:430px}}
.collab-img.fth{filter:brightness(0) saturate(100%) invert(9%) sepia(6%) saturate(512%) hue-rotate(94deg) brightness(95%) contrast(96%)}
.collab-img.labco{filter:brightness(0) saturate(100%) invert(9%) sepia(6%) saturate(512%) hue-rotate(94deg) brightness(95%) contrast(96%)}

.gif-strip{padding:clamp(1.4rem,3vw,2.4rem) 0 0;position:relative;overflow:hidden;border-top:1px solid var(--border-light);background:radial-gradient(900px 520px at 15% 10%,rgba(232,245,240,.85) 0%,transparent 55%),radial-gradient(820px 520px at 85% 0%,rgba(212,175,55,.10) 0%,transparent 60%),linear-gradient(135deg,#f8fcfb 0%,#ffffff 65%);isolation:isolate}
.gif-strip::before{content:'';position:absolute;inset:-2px;background:repeating-linear-gradient(90deg,rgba(45,95,77,.10) 0px,rgba(45,95,77,.10) 1px,transparent 1px,transparent 18px),repeating-linear-gradient(0deg,rgba(74,140,115,.08) 0px,rgba(74,140,115,.08) 1px,transparent 1px,transparent 22px);opacity:.22;pointer-events:none;mask-image:radial-gradient(circle at 60% 50%,black 0%,black 55%,transparent 78%);-webkit-mask-image:radial-gradient(circle at 60% 50%,black 0%,black 55%,transparent 78%);z-index:0;animation:circuitDrift 14s linear infinite}
.gif-strip::after{content:'';position:absolute;inset:0;background:radial-gradient(600px 320px at 70% 50%,rgba(74,140,115,.18) 0%,transparent 60%),radial-gradient(520px 280px at 30% 70%,rgba(212,175,55,.12) 0%,transparent 62%);opacity:.55;pointer-events:none;z-index:0}
.gif-strip-inner{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem);position:relative;z-index:1;display:grid;grid-template-columns:1.55fr 1fr 1fr;gap:clamp(.55rem,1.2vw,.9rem);align-items:stretch}
.gs-panel{border-radius:var(--radius-md);overflow:hidden;border:1px solid rgba(45,95,77,.14);box-shadow:var(--shadow-md);position:relative;background:linear-gradient(135deg,rgba(232,245,240,.8),rgba(255,255,255,.9));transform:translateY(0);transition:transform .4s var(--transition-smooth),box-shadow .4s var(--transition-smooth)}
.gs-panel-main{aspect-ratio:16/9}
.gs-panel-side{aspect-ratio:4/3}
.gs-panel::before{content:attr(data-label);position:absolute;bottom:.65rem;left:.65rem;z-index:2;font-size:.68rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:rgba(14,40,30,.62);backdrop-filter:blur(8px);padding:.22rem .65rem;border-radius:999px;border:1px solid rgba(255,255,255,.22);opacity:0;transform:translateY(4px);transition:opacity .3s ease,transform .3s ease;pointer-events:none;font-family:var(--font-mono)}
.gs-panel:hover::before{opacity:1;transform:translateY(0)}
.gs-panel:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg)}
.gs-panel img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.01);transition:transform .75s var(--transition-smooth),opacity .4s ease}
.gs-panel img.loading{opacity:0}
.gs-panel:hover img{transform:scale(1.05)}
.gs-panel-side::after{content:'';position:absolute;top:.55rem;right:.55rem;width:8px;height:8px;background:var(--gold-accent);border-radius:50%;box-shadow:0 0 0 2px rgba(255,255,255,.55);animation:livePulse 2.2s ease-in-out infinite;z-index:2}
@keyframes livePulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.55;transform:scale(1.35)}}
.gif-strip-caption{position:relative;z-index:2;margin:clamp(.55rem,1.2vw,.85rem) 0 0;padding:clamp(.55rem,1.2vw,.85rem) clamp(1rem,4vw,3rem);background:rgba(11,28,22,0.82);backdrop-filter:blur(12px);border-top:1px solid rgba(74,140,115,.22)}
.gif-caption-inner{max-width:1400px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:baseline;gap:.55rem 1.1rem;font-size:clamp(.78rem,1.5vw,.88rem);color:rgba(232,245,240,.78);font-family:var(--font-mono);line-height:1.6}
.gif-caption-tag{color:var(--gold-accent);font-weight:700;letter-spacing:.04em;font-size:clamp(.8rem,1.6vw,.92rem);white-space:nowrap}
.gif-caption-brace{color:rgba(74,140,115,.9);font-weight:400}
.gif-caption-divider{color:rgba(74,140,115,.5);font-size:1rem;font-family:inherit;flex-shrink:0}
.gif-caption-item{font-family:var(--font-body);font-size:clamp(.8rem,1.5vw,.88rem);color:rgba(232,245,240,.72);letter-spacing:.01em}
.gif-caption-item strong{color:rgba(232,245,240,.95);font-weight:650}
@keyframes circuitDrift{0%{transform:translate3d(0,0,0)}100%{transform:translate3d(-40px,18px,0)}}
@media(max-width:700px){.gif-strip-inner{grid-template-columns:1fr}.gs-panel-main,.gs-panel-side{aspect-ratio:16/9}}
@media(min-width:701px) and (max-width:1050px){.gif-strip-inner{grid-template-columns:1fr 1fr;grid-template-rows:auto auto}.gs-panel-main{grid-column:1;grid-row:1/3;aspect-ratio:unset;min-height:220px}.gs-panel-side:nth-child(2){grid-column:2;grid-row:1}.gs-panel-side:nth-child(3){grid-column:2;grid-row:2}}

/* Stats ribbon */
.stats-ribbon{padding:clamp(1.5rem,3vw,2.2rem) 0;background:radial-gradient(700px 350px at 50% 50%,rgba(232,245,240,.45) 0%,transparent 60%),linear-gradient(180deg,#f7fbfa 0%,#fff 100%);position:relative}
.stats-ribbon-inner{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem);display:flex;justify-content:center;gap:clamp(2rem,5vw,5rem);flex-wrap:wrap}
.stat-item{text-align:center;min-width:120px}
.stat-number{font-size:clamp(2rem,4.5vw,3.2rem);font-weight:900;color:var(--dark-green);font-family:var(--font-body);letter-spacing:-.03em;line-height:1.1}
.stat-number .stat-plus{color:var(--gold-accent);font-weight:700}
.stat-label{font-size:.72rem;color:var(--text-light);margin-top:.3rem;letter-spacing:.05em;text-transform:uppercase;font-weight:700;font-family:var(--font-mono)}
.stat-divider{width:1px;background:linear-gradient(180deg,transparent,rgba(45,95,77,.15),transparent);align-self:stretch}
@media(max-width:600px){.stats-ribbon-inner{gap:1.5rem 2rem}.stat-divider{display:none}}
</style>

<!-- TITLE SECTION -->
<section class="title-section">
  <div class="lang-toggle" aria-label="Language selection">
    <button type="button" class="lang-btn active" data-lang="en">EN</button>
    <button type="button" class="lang-btn" data-lang="es">ES</button>
    <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
  </div>
  <div class="title-inner">
    <div class="title-brand">
      <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9466ebc27c9487e8bfbff1d1dd904f4f9e6df81d/images/logo_FOUND_white.png" alt="FOUND logo" class="project-logo" />
      <h1 class="project-title">FOUND</h1>
    </div>
    <hr class="title-divider" />
    <p class="project-subtitle" id="project-subtitle"><span class="title-accent">Interpretar la Naturaleza</span> para Encontrar a Quienes nos Faltan</p>
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
            <div class="word-carousel" role="text"><span id="hero-word" class="hero-word">search.</span></div>
          </div>
        </div>
        <p class="hero-description" id="hero-main-text">Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> builds the scientific and institutional capabilities needed to find and return missing persons to their families. Working at the intersection of frontier technology and the lived knowledge of search groups, we drive systemic change in how governments and institutions respond to disappearance.</p>
      </div>
      <div class="hero-side reveal reveal-delay-2">
        <div class="award-highlight">
          <a href="/news/#mariela-award" class="award-card">
            <div class="award-text">
              <div class="award-pill">Award</div>
              <div class="award-title">FOUND recognised with the Sir Nicholas Browne Policy and Expertise Award <span class="arrow">&#x2197;</span></div>
              <div class="award-meta">Selected from over 200 nominations across the UK Foreign, Commonwealth &amp; Development Office.</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
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
    <div class="gs-panel gs-panel-main touch-zoomable" data-label="Spectral indices, clandestine crematoriums, substance detection"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/1047db9c85ff842e083e9fb45c0bdf05213da88a/images/NDAI5.gif" alt="FOUND Project team using advanced technology in field search operations" loading="lazy" class="loading" onload="this.classList.remove('loading')" /></div>
    <div class="gs-panel gs-panel-side touch-zoomable" data-label="Satellite analysis, time series"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/33b2627b6b245e9632f59abf0a02f5ad58956bf4/images/Areas_de_busqueda_3.gif" alt="Satellite spectral time-series analysis of search areas" loading="lazy" class="loading" onload="this.classList.remove('loading')" /></div>
    <div class="gs-panel gs-panel-side touch-zoomable" data-label="Clandestine space detection"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9b9df755f7129ba10ee53479d528d42d14e5648a/images/ClandestineSpace.gif" alt="Spectral detection of clandestine sites using satellite imagery" loading="lazy" class="loading" onload="this.classList.remove('loading')" /></div>
  </div>
  <div class="gif-strip-caption"><div class="gif-caption-inner">
    <span class="gif-caption-tag">Platforms<span class="gif-caption-brace">{</span>core member: CentroGeo<span class="gif-caption-brace">}</span></span>
    <span class="gif-caption-divider">·</span>
    <span class="gif-caption-item"><strong>Spectral indices</strong> — Identifying substances linked to disappearances via satellite and drone imagery, and when they were present.</span>
    <span class="gif-caption-divider">·</span>
    <span class="gif-caption-item"><strong>Clandestine sites location</strong> — AI that finds what was meant to stay hidden.</span>
  </div></div>
</section>

<!-- STATS RIBBON -->
<section class="stats-ribbon reveal" aria-label="Key statistics">
  <div class="stats-ribbon-inner">
    <div class="stat-item"><div class="stat-number" id="stat-num-1">7<span class="stat-plus">+</span></div><div class="stat-label" id="stat-label-1">Technologies deployed</div></div>
    <div class="stat-divider"></div>
    <div class="stat-item"><div class="stat-number" id="stat-num-2">20<span class="stat-plus">+</span></div><div class="stat-label" id="stat-label-2">Institutional partners</div></div>
    <div class="stat-divider"></div>
    <div class="stat-item"><div class="stat-number" id="stat-num-3">3</div><div class="stat-label" id="stat-label-3">Countries</div></div>
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
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/360.gif" alt="360 degree imaging technology in use" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.03.01.jpeg?raw=true" alt="Advanced field equipment setup" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/2.jpeg?raw=true" alt="Community collaboration in search efforts" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true" alt="Specialised search tools and equipment" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3.jpeg?raw=true" alt="Field research and data collection" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-07-30%20at%2021.40.57.jpeg?raw=true" alt="Team collaboration during field operations" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/c88e3807678629fcd59ad91baff20b6ec7a34f66/images/layers.jpg?raw=true" alt="Technology deployment in field" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/IMG-20231204-WA0038.jpg?raw=true" alt="Field operations and search activities" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-12-02%20at%2018.42.17.jpeg?raw=true" alt="Search team in action" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/70206a6b5788f7204524bfdd4e1a6c365668b75d/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.44.jpeg" alt="Search methodology in practice" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/51a35a3f1915699b8fe9835270ddfe6f3c5c0946/images/hyperspectral%20from%20presentation.png?raw=true" alt="Hyperspectral analysis output" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
          <div class="gallery-item touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/51a35a3f1915699b8fe9835270ddfe6f3c5c0946/images/pigs_aerial.jpg?raw=true" alt="Aerial view of experimental calibration site" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
        </div>
      </section>
    </div>
    <div class="dual-column reveal reveal-delay-2">
      <section class="buscadoras-section" id="buscadoras">
        <div class="buscadoras-content">
          <div>
            <h2 id="buscadoras-title">The Role of Buscadoras</h2>
            <p class="buscadoras-text hero-description" id="buscadoras-text">Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.</p>
          </div>
          <div class="buscadoras-image touch-zoomable"><img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolising hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div>
        </div>
      </section>
    </div>
  </div>
</section>

<div class="section-divider"><hr/></div>

<!-- INSTITUTIONAL PARTNERSHIPS -->
<section class="content-section" id="collaborations">
  <div class="section-container">
    <h2 id="collab-title" class="reveal">Institutional Partnerships</h2>
    <div class="collab-wrap reveal" aria-label="Institutional partnerships logos">
      <div class="collab-grid">
        <div class="collab-card collab-card-gif touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0bed7c6b4c906bc94116683368b679ba0bd80428/images/mothers%20walking.gif" alt="Search Collectives" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-7">Search Collectives</div><div class="collab-note" id="collab-note-7">Leadership, field expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/1%20Executive%20Office%20of%20the%20UN%20Secretary-General.svg" alt="Executive Office of the UN Secretary-General" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-1">Executive Office of the UN Secretary-General</div><div class="collab-note" id="collab-note-1">International collaboration</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/bd3ef3bd33596258b2738274017f51a2e2c05186/images/FCDO_logo_960x640.png" alt="UK FCDO" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-2">UK Foreign, Commonwealth &amp; Development Office (FCDO)</div><div class="collab-note" id="collab-note-2">Policy, Funding, Partnerships</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/2%20logo_centrogeo_wide.svg" alt="CentroGeo" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-3">CentroGeo</div><div class="collab-note" id="collab-note-3">Co-lead, Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/26bd52ce350828b22814cfedc872786dd43de672/images/580141488dfc53bfdbde59fa6b043438.jpg" alt="University of Guadalajara" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-4">University of Guadalajara (UdeG)</div><div class="collab-note" id="collab-note-4">Technical expertise, Experimental sites</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg" alt="Colombian Search Unit" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-5">Colombian Search Unit (UBPD)</div><div class="collab-note" id="collab-note-5">Casework, Technical exchange</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/4%20Comision%20Nacional%20de%20Busqueda.png" alt="Mexico National Search Commission" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-6">Mexico's National Search Commission</div><div class="collab-note" id="collab-note-6">National coordination</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png" alt="British Embassy Mexico City" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-8">British Embassy in Mexico City</div><div class="collab-note" id="collab-note-8">Funding, Coordination support</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/5ea7b61d8c5c6467ad4253f2898109033aac13e7/images/OFOTA_COLOUR_WEB.jpg" alt="Oxford Festival of the Arts" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-9">Oxford Festival of the Arts</div><div class="collab-note" id="collab-note-9">Oxford Forum partner</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b2323f813df618867a6227a87e7efb9e084fe75e/images/Beth.jpg" alt="University of Bath" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-10">University of Bath</div><div class="collab-note" id="collab-note-10">Technical expertise, Oxford Forum partner</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/11%20logo%20BAFAlogo_orig.png" alt="BAFA" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-bafa">British Association for Forensic Anthropology</div><div class="collab-note" id="collab-note-bafa">Forensic expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/3%20Comisio%CC%81n%20de%20Bu%CC%81squeda%20de%20Jalisco.png" alt="Comisión de Búsqueda de Jalisco" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-jalisco">Comisión de Búsqueda de Jalisco</div><div class="collab-note" id="collab-note-jalisco">Technical expertise, Coordination</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/4%20logo%20oxford-university-logo.png" alt="University of Oxford" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-oxford">University of Oxford</div><div class="collab-note" id="collab-note-oxford">Co-lead, Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20Logotipo_SECIHTI_2025-2030.svg" alt="SECIHTI" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-secihti">Mexico's Science and Technology Secretariat</div><div class="collab-note" id="collab-note-secihti">Funding, Policy impact</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20logo%20IGeofisicaUNAM.png" alt="UNAM Geophysics" loading="lazy" onload="this.classList.remove('loading')" style="filter:brightness(0) invert(0);"></div><div class="collab-meta"><div class="collab-name" id="collab-item-unam-geo">UNAM – Geophysics</div><div class="collab-note" id="collab-note-unam-geo">Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/6%20logo%20Ingenieria%20UNAM.png" alt="UNAM Engineering" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-unam-eng">UNAM – Engineering</div><div class="collab-note" id="collab-note-unam-eng">Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/master/images/10%20logo%20FT%2Blogo_Primary%2Bversion_white%2Btext.png" alt="Frontier Tech Hub" loading="lazy" class="collab-img fth"></div><div class="collab-meta"><div class="collab-name" id="collab-item-fth">Frontier Tech Hub</div><div class="collab-note" id="collab-note-fth">Funding, Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20DTG_Logo_Screen_LRG-1.png" alt="DT Global" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-dtg">DT Global</div><div class="collab-note" id="collab-note-dtg">Funding, Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/8%20logo%20UPZMG2.png" alt="UPZMG" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-upzmg">UPZMG</div><div class="collab-note" id="collab-note-upzmg">Experimental site</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/9%20logo%20UWE%20Bristol.svg" alt="UWE Bristol" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-uwe">UWE Bristol</div><div class="collab-note" id="collab-note-uwe">Funding, Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d47bacb6b575270e7b5453c8ebc5b13bcec70a2f/images/dark-non-retina-labco.png" alt="LABCO" loading="lazy" class="collab-img labco"></div><div class="collab-meta"><div class="collab-name" id="collab-item-labco">LABCO</div><div class="collab-note" id="collab-note-labco">Exploring AI together to locate and identify</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://github.com/FOUND-project/found-project.github.io/blob/82b303cdf26fa6a25e9845ff0d5fc10e070d94e6/images/logo_eaaf_rd.png?raw=true" alt="EAAF" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-eaaf">Argentine Forensic Anthropology Team (EAAF)</div><div class="collab-note" id="collab-note-eaaf">Luis Fondebrider, FOUND's advisor</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/a8209a23c303b55bda756d5a55b2c572ac2540a9/images/ori_logo_square_2024_150_inverted.png" alt="Oxford Robotics Institute" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-ori">Oxford Robotics Institute</div><div class="collab-note" id="collab-note-ori">Partnership, technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/b9419b5a0b9d80c6ae96d16642771d6c1d66cdf3/images/logo-ipn-guinda.svg" alt="IPN" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-ipn">Instituto Politécnico Nacional</div><div class="collab-note" id="collab-note-ipn">Technical expertise, Technology</div></div></div>
      </div>
    </div>
  </div>
</section>

<!-- SOCIAL -->
<section class="social-section" id="social">
  <div class="social-container">
    <h2 class="section-title" id="social-title">Follow Our Journey</h2>
    <p class="section-subtitle" id="social-subtitle">Our latest findings, community stories, and collaborations</p>
    <div class="social-grid">
      <div class="social-embed"><div class="iframe-container"><iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7405294962692595712" height="880" width="504" frameborder="0" allowfullscreen title="FOUND Project LinkedIn update" loading="lazy"></iframe></div></div>
      <div class="social-embed twitter-embed"><div class="iframe-container"><blockquote class="twitter-tweet"><p lang="en" dir="ltr">Almost a year after I started researching the story, I'm thrilled that my <a href="https://twitter.com/guardian?ref_src=twsrc%5Etfw">@guardian</a> article about the innovations being used to try and find some of the thousands of people who have disappeared in Mexico is the most read in its Global Development section. <a href="https://t.co/NztFCj4uEF">https://t.co/NztFCj4uEF</a></p>&mdash; Suzanne Bearne (@sbearne) <a href="https://twitter.com/sbearne/status/1991827389375193330?ref_src=twsrc%5Etfw">November 21, 2025</a></blockquote></div></div>
      <div class="social-embed twitter-embed"><div class="iframe-container"><blockquote class="twitter-tweet"><p lang="es" dir="ltr">Cómo los cerdos y los insectos están ayudando a encontrar a los desaparecidos en México <a href="https://t.co/sJC3oaNLGL">https://t.co/sJC3oaNLGL</a></p>&mdash; BBC News Mundo (@bbcmundo) <a href="https://twitter.com/bbcmundo/status/1973352689867063513?ref_src=twsrc%5Etfw">October 1, 2025</a></blockquote></div></div>
      <div class="social-embed"><div class="iframe-container"><iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728" height="880" width="504" frameborder="0" allowfullscreen title="FOUND Project community engagement" loading="lazy"></iframe></div></div>
      <div class="social-embed"><div class="iframe-container"><iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7343552976185114624" height="880" width="504" frameborder="0" allowfullscreen title="FCDO LinkedIn post" loading="lazy"></iframe></div></div>
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
  var translations={en:{'collab-item-labco':'LABCO','collab-note-labco':'Exploring AI together to locate and identify','collab-item-eaaf':'Argentine Forensic Anthropology Team (EAAF)','collab-note-eaaf':"Luis Fondebrider, FOUND's advisor",'collab-item-ori':'Oxford Robotics Institute','collab-note-ori':'Partnership, technical expertise','collab-item-ipn':'Instituto Polit\u00e9cnico Nacional','collab-note-ipn':'Technical expertise, Technology','project-subtitle':'<span class="title-accent">Technologies</span> To Locate Those Who We Are Missing','hero-tagline-static':'Using technology to','word-1':'search.','word-2':'remember.','word-3':'dignify.','word-4':'find.','word-5':'bring closure.','hero-main-text':'Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change and building institutional capacity to improve how governments respond to disappearance','hero-team-text':'Our core team brings together <strong>collectives of families from Jalisco and Zacatecas searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco\'s Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico\'s National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.','collab-title':'Institutional Partnerships','tech-title':'Technologies in Action','tech-item-1':'Multispectral &amp; Hyperspectral Imaging','tech-item-2':'Airborne LiDAR','tech-item-3':'Seismic Noise Interferometry (TIRSA)','tech-item-4':'Electrical Resistivity Tomography, Conductivimetry','tech-item-5':'Satellite Spectral Analysis','tech-item-ml':'Machine Learning','tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science','buscadoras-title':'The Role of Buscadoras','buscadoras-text':"Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.",'social-title':'Follow Our Journey','social-subtitle':'Stay connected with our latest findings, community stories, and collaborations','footer-text':'FOUND: Tecnolog\u00edas para Encontrar a Quienes nos Faltan.','stat-label-1':'Technologies deployed','stat-label-2':'Institutional partners','stat-label-3':'Countries'},es:{'collab-item-labco':'LABCO','collab-note-labco':'Explorando juntos el uso de IA para localizar e identificar','collab-item-eaaf':'Equipo Argentino de Antropolog\u00eda Forense (EAAF)','collab-note-eaaf':'Luis Fondebrider, asesor de FOUND','collab-item-ori':'Oxford Robotics Institute','collab-note-ori':'Alianza, experiencia t\u00e9cnica','collab-item-ipn':'Instituto Polit\u00e9cnico Nacional','collab-note-ipn':'Experiencia t\u00e9cnica, desarrollo tecnol\u00f3gico','project-subtitle':'<span class="title-accent">Tecnolog\u00edas</span> para Encontrar a Quienes nos Faltan','hero-tagline-static':'Usando tecnolog\u00eda para','word-1':'buscar.','word-2':'recordar.','word-3':'dignificar.','word-4':'encontrar.','word-5':'dar cierre.','hero-main-text':'M\u00e1s de 130,000 personas est\u00e1n registradas como desaparecidas en M\u00e9xico. Detr\u00e1s de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> combina tecnolog\u00eda y saberes de familias buscadoras para aprender del campo, localizar y promover cambios sist\u00e9micos.','hero-team-text':'Nuestro equipo central re\u00fane <strong>colectivos de familias de Jalisco y Zacatecas que buscan a sus seres queridos desaparecidos</strong>, junto a CentroGeo, la Universidad de Oxford, la Comisi\u00f3n de B\u00fasqueda de Jalisco, la Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) y la Universidad de Guadalajara. Trabajamos junto a socios estrat\u00e9gicos, entre ellos la Oficina para Asuntos Exteriores, de la Commonwealth y de Desarrollo del Reino Unido (FCDO), la Oficina Ejecutiva del Secretario General de la ONU, la Unidad de B\u00fasqueda de Personas dadas por Desaparecidas (UBPD) de Colombia, la Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico, LAB-Co y Luis Fondebrider.','collab-title':'Alianzas institucionales','tech-title':'Tecnolog\u00edas en acci\u00f3n','tech-item-1':'Im\u00e1genes multiespectrales e hiperespectrales','tech-item-2':'LiDAR aerotransportado','tech-item-3':'Interferometr\u00eda de ruido s\u00edsmico (TIRSA)','tech-item-4':'Tomograf\u00eda de resistividad el\u00e9ctrica y mediciones de conductividad','tech-item-5':'An\u00e1lisis espectral satelital','tech-item-ml':'Aprendizaje autom\u00e1tico','tech-item-6':'Entomolog\u00eda forense, bot\u00e1nica, an\u00e1lisis territorial y ciencia del suelo','buscadoras-title':'El papel de las buscadoras','buscadoras-text':'Los colectivos liderados por mujeres est\u00e1n en el coraz\u00f3n del trabajo de FOUND. Han transformado la conversaci\u00f3n nacional sobre desaparici\u00f3n y justicia. Sus pr\u00e1cticas de b\u00fasqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus m\u00e9todos en nuestros esfuerzos tecnol\u00f3gicos.','social-title':'Sigue nuestro camino','social-subtitle':'Mant\u00e9nte al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.','footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.','stat-label-1':'Tecnolog\u00edas desplegadas','stat-label-2':'Socios institucionales','stat-label-3':'Pa\u00edses'},nah:{'collab-item-labco':'LABCO','collab-note-labco':'Timoitayoh ika IA para titemoa huan tiquixmati','collab-item-eaaf':'Equipo Argentino de Antropolog\u00eda Forense (EAAF)','collab-note-eaaf':'Luis Fondebrider, ixcuitlali (asesor) FOUND','collab-item-ori':'Oxford Robotics Institute','collab-note-ori':'Tlaneltiliztli (alianza), teknikoh tlamatiliztli','collab-item-ipn':'Instituto Polit\u00e9cnico Nacional','collab-note-ipn':'Teknikoh tlamatiliztli, teknoloj\u00edayoh tlatequipanoliztli','project-subtitle':'<span class="title-accent">Tecnolog\u00edas</span> para Encontrar a Quienes nos Faltan','hero-tagline-static':'Teknoloj\u00edayoh ika','word-1':'temoa.','word-2':'quilnamictia.','word-3':'tlatepanita.','word-4':'quipantlalia.','word-5':'yolpakilistli quimacatia.','hero-main-text':'124,354 tl\u0101cameh tlahcuil\u014dlmeh quen pol\u012bhuihqueh ipan M\u0113xihco. Ipan sesen inin caso cah se familia tlatehu\u00eda tlanemilistli. <strong>FOUND</strong> quimixnextia tehnolog\u00edayoh huan tlamatiliztli in familias buscadoras para momachtia, quitemoa, quipantlalia huan quinemililia yancuic tlanemilistli ipan sistema.','hero-team-text':'In totequitlacauh quinnechicoa <strong>in colectivoh in familias tlen Jalisco huan Zacatecas tlen quitemoa in inpilhuan polihqueh</strong>, oc nochi CentroGeo, in Universidad de Oxford, in Comisi\u00f3n de B\u00fasqueda de Jalisco, in Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) huan in Universidad de Guadalajara. Timoitayoh ika in tlaneltililmeh tlen FCDO, in Oficina Ejecutiva del Secretario General de la ONU, UBPD, in Comisi\u00f3n Nacional de B\u00fasqueda, LAB-Co huan Luis Fondebrider.','collab-title':'Alianzas institucionales','tech-title':'Teknoloj\u00edayoh tlen motequiti','tech-item-1':'Multispectral &amp; Hyperspectral Imaging','tech-item-2':'Airborne LiDAR','tech-item-3':'Seismic Noise Interferometry (TIRSA)','tech-item-4':'Electrical Resistivity Tomography, Conductivimetry','tech-item-5':'Satellite Spectral Analysis','tech-item-ml':'Machine Learning','tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science','buscadoras-title':'In papel in buscadoras','buscadoras-text':'In colectivoh de buscadoras cah ipan yollotl in tequitl tlen FOUND. Yehuan quipatlaqueh in tlajtol ipan pa\u00eds tlen polihuiliztli huan tlayectlaliz (justicia). Inintequiti tlen temoa, tlen tlapanextia de inin nemilistli, mochihua se tlamatiliztli forense huecapan. FOUND quincaca, momachtia huan quincalaquia inintequiti ipan inin teknol\u00f3gicoh tequitl.','social-title':'Xiquito in totlanejmachtiliz','social-subtitle':'Ximoyetkixtia inin tlen tipantlaliah, tlen tlanechicoliztli in comunidades huan inin tlen timocoyonaltiah san sejco.','footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.','stat-label-1':'Teknoloj\u00edayoh','stat-label-2':'Tlaneltililmeh','stat-label-3':'Tl\u0101ltlameh'}};
  var heroWords=[],wordIndex=0,wordInterval=null;
  function buildHeroWords(lang){var dict=translations[lang]||translations.en;heroWords=['word-1','word-2','word-3','word-4','word-5'].map(function(k){return dict[k]}).filter(Boolean);wordIndex=0;var span=document.getElementById('hero-word');if(span&&heroWords.length)span.textContent=heroWords[0]}
  function startWordRotation(){var span=document.getElementById('hero-word');if(wordInterval)clearInterval(wordInterval);if(!span||heroWords.length<2)return;wordInterval=setInterval(function(){span.classList.add('fading-out');setTimeout(function(){wordIndex=(wordIndex+1)%heroWords.length;span.textContent=heroWords[wordIndex];span.classList.remove('fading-out');span.classList.add('fading-in');requestAnimationFrame(function(){requestAnimationFrame(function(){span.classList.remove('fading-in')})})},280)},1600)}
  function setLanguage(lang){var dict=translations[lang]||translations.en;Object.keys(dict).forEach(function(id){var el=document.getElementById(id);if(el)el.innerHTML=dict[id]});document.documentElement.setAttribute('lang',lang==='es'?'es':(lang==='nah'?'nah':'en'));document.querySelectorAll('.lang-btn').forEach(function(btn){btn.classList.toggle('active',btn.dataset.lang===lang)});try{localStorage.setItem('found-lang',lang)}catch(e){}buildHeroWords(lang);startWordRotation()}
  function setupScrollReveal(){var reveals=document.querySelectorAll('.reveal');if(!reveals.length)return;if('IntersectionObserver' in window){var observer=new IntersectionObserver(function(entries){entries.forEach(function(entry){if(entry.isIntersecting)entry.target.classList.add('is-visible')})},{threshold:0.05,rootMargin:'0px 0px -20px 0px'});reveals.forEach(function(el){observer.observe(el)});document.body.classList.add('reveal-ready')}}
  function setupTouchZoom(){var zoomables=document.querySelectorAll('.touch-zoomable');if(!zoomables.length)return;function toggleZoom(el){if(el.classList.contains('is-expanded')){el.classList.remove('is-expanded');document.body.classList.remove('zoom-active')}else{document.querySelectorAll('.touch-zoomable.is-expanded').forEach(function(o){o.classList.remove('is-expanded')});el.classList.add('is-expanded');document.body.classList.add('zoom-active')}}zoomables.forEach(function(el){el.addEventListener('click',function(e){if(window.matchMedia&&window.matchMedia('(max-width: 768px)').matches){e.preventDefault();e.stopPropagation();toggleZoom(el)}})});document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.touch-zoomable.is-expanded').forEach(function(o){o.classList.remove('is-expanded')});document.body.classList.remove('zoom-active')}})}
  function init(){var savedLang=null;try{savedLang=localStorage.getItem('found-lang')}catch(e){}var initialLang=(savedLang==='es'||savedLang==='en'||savedLang==='nah')?savedLang:'en';setLanguage(initialLang);document.querySelectorAll('.lang-btn').forEach(function(btn){btn.addEventListener('click',function(){setLanguage(btn.dataset.lang)})});setupTouchZoom();setupScrollReveal()}
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init)}else{init()}
})();
</script>
