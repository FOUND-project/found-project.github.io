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
body.reveal-ready .reveal{opacity:0;transform:translateY(24px);transition:opacity .6s var(--transition-smooth),transform .6s var(--transition-smooth)}
body.reveal-ready .reveal.is-visible{opacity:1;transform:translateY(0)}
body.reveal-ready .reveal-delay-2{transition-delay:.18s}
.lang-toggle{position:absolute;top:1.4rem;right:clamp(1rem,4vw,3rem);display:inline-flex;gap:.45rem;z-index:3}
.lang-btn{border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.08);color:rgba(255,255,255,.75);padding:.35rem .95rem;border-radius:999px;font-size:.78rem;font-weight:700;font-family:var(--font-mono);letter-spacing:.09em;text-transform:uppercase;cursor:pointer;backdrop-filter:blur(10px);transition:transform .2s var(--transition-smooth),background .2s var(--transition-smooth),box-shadow .2s var(--transition-smooth),border-color .2s var(--transition-smooth)}
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
/* ===== HERO ===== */
.hero{padding:clamp(2rem,4.5vw,3.75rem) 0 clamp(1.75rem,4vw,3rem);position:relative;overflow:hidden}
.title-section,.hero{background-color:transparent}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(800px 420px at 12% 20%,rgba(232,245,240,.70) 0%,transparent 55%),radial-gradient(780px 420px at 86% 0%,rgba(212,175,55,.12) 0%,transparent 60%),linear-gradient(135deg,#f7fbfa 0%,#ffffff 60%);z-index:0}
.hero-content{position:relative;z-index:1;max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.hero-text{display:flex;flex-direction:column;align-items:center;text-align:center;gap:1.35rem;max-width:1020px;margin:0 auto}
.animated-tagline{font-size:clamp(2.05rem,5vw,3.6rem);font-weight:900;display:flex;align-items:center;justify-content:center;color:var(--dark-green);flex-wrap:wrap;gap:.75rem;letter-spacing:-.03em;line-height:1.08}
.tagline-pill{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;padding:1rem 2.2rem 1.15rem;border-radius:32px;background:linear-gradient(135deg,rgba(255,255,255,.92) 0%,rgba(232,245,240,.82) 100%);border:1px solid rgba(45,95,77,.16);box-shadow:var(--shadow-md);white-space:normal;position:relative;isolation:isolate;overflow:hidden}
.tagline-pill::after{content:'';position:absolute;left:50%;bottom:0;width:180px;height:2px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,var(--gold-accent),transparent);opacity:.65}
.tagline-pill span#hero-tagline-static{display:block;width:100%;font-size:clamp(1.9rem,4.2vw,3rem);font-weight:900;color:var(--dark-green);letter-spacing:-.03em;line-height:1.12;text-align:center}
.word-carousel{margin-top:.2rem;width:100%;display:flex;align-items:center;justify-content:center;min-height:1.35em}
.hero-word{display:block;font-size:clamp(1.9rem,4.4vw,3rem);font-weight:900;letter-spacing:-.02em;color:var(--light-green);text-shadow:0 10px 28px rgba(15,23,42,.10);white-space:nowrap;text-align:center;transition:opacity .28s var(--transition-smooth),transform .28s var(--transition-smooth);opacity:1;transform:translateY(0);font-family:var(--font-display);font-style:italic}
.hero-word.fading-out{opacity:0;transform:translateY(-8px)}
.hero-word.fading-in{opacity:0;transform:translateY(8px)}
.hero-description{font-size:clamp(1.06rem,2.4vw,1.3rem);color:var(--text-medium);max-width:920px;line-height:1.85;font-weight:450}
.hero-description strong{color:var(--primary-green);font-weight:750;background:linear-gradient(120deg,rgba(232,245,240,.95) 0%,transparent 100%);padding:.08rem .32rem;border-radius:6px}
.hero-cue{display:inline-flex;align-items:center;gap:.55rem;text-decoration:none;font-family:var(--font-mono);font-size:.76rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--primary-green);background:rgba(255,255,255,.72);border:1px solid rgba(45,95,77,.18);padding:.5rem 1.15rem;border-radius:999px;box-shadow:var(--shadow-sm);transition:transform .25s var(--transition-smooth),box-shadow .25s var(--transition-smooth),border-color .25s var(--transition-smooth),background .25s var(--transition-smooth)}
.hero-cue:hover{transform:translateY(-2px);box-shadow:var(--shadow-md);border-color:rgba(212,175,55,.55);background:#fff;color:var(--dark-green)}
.hero-cue .cue-arrow{display:inline-block;animation:cueBob 2.2s ease-in-out infinite}
@keyframes cueBob{0%,100%{transform:translateY(0)}50%{transform:translateY(4px)}}
/* ===== TIMELINE ===== */
.timeline-section{position:relative;overflow:hidden;padding:clamp(2.75rem,6vw,4.75rem) 0 clamp(2rem,4.5vw,3.25rem);background:radial-gradient(1100px 560px at 18% 0%,rgba(74,140,115,.22) 0%,transparent 58%),radial-gradient(900px 520px at 86% 100%,rgba(212,175,55,.13) 0%,transparent 62%),linear-gradient(180deg,#0b1c16 0%,#0e2a1f 46%,#0b1c16 100%);isolation:isolate;scroll-margin-top:1rem}
.timeline-section::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(232,245,240,.05) 0 1px,transparent 1px 28px),repeating-linear-gradient(0deg,rgba(232,245,240,.04) 0 1px,transparent 1px 28px);mask-image:radial-gradient(circle at 50% 48%,black 0%,black 52%,transparent 86%);-webkit-mask-image:radial-gradient(circle at 50% 48%,black 0%,black 52%,transparent 86%);opacity:.55;pointer-events:none;z-index:0}
.tl-inner{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem);position:relative;z-index:2}
.tl-head{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.85rem}
.tl-eyebrow{display:inline-flex;align-items:center;gap:.5rem;padding:.32rem .95rem;border-radius:999px;font-size:.7rem;font-weight:750;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-accent);background:rgba(212,175,55,.09);border:1px solid rgba(212,175,55,.28);font-family:var(--font-mono)}
.tl-eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--gold-accent);box-shadow:0 0 9px rgba(212,175,55,.65)}
.tl-title{font-family:var(--font-display);font-size:clamp(1.95rem,4.5vw,3.05rem);font-weight:400;color:#fff;line-height:1.2;letter-spacing:0;padding-bottom:.95rem;margin:0;position:relative;text-shadow:0 8px 26px rgba(0,0,0,.32)}
.tl-title::after{content:'';position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:64px;height:3px;border-radius:999px;background:linear-gradient(90deg,rgba(212,175,55,.25),var(--gold-accent),rgba(212,175,55,.25))}
.tl-sub{max-width:820px;font-size:clamp(1rem,2.1vw,1.14rem);line-height:1.78;color:rgba(232,245,240,.72)}
.tl-filters{display:flex;flex-wrap:wrap;justify-content:center;gap:.45rem;margin-top:.4rem}
.tl-chip{font-family:var(--font-mono);font-size:.78rem;font-weight:700;letter-spacing:.09em;color:rgba(232,245,240,.72);background:rgba(255,255,255,.06);border:1px solid rgba(232,245,240,.18);padding:.4rem 1rem;border-radius:999px;cursor:pointer;transition:transform .22s var(--transition-smooth),background .22s var(--transition-smooth),color .22s var(--transition-smooth),border-color .22s var(--transition-smooth),box-shadow .22s var(--transition-smooth)}
.tl-chip:hover{transform:translateY(-2px);color:#fff;border-color:rgba(212,175,55,.55);background:rgba(255,255,255,.12)}
.tl-chip.is-active{background:linear-gradient(135deg,var(--gold-accent),#f0d478);color:#0b1c16;border-color:transparent;box-shadow:0 10px 26px rgba(212,175,55,.28)}
.tl-stage{position:relative;z-index:2;margin-top:clamp(1.5rem,3.2vw,2.5rem)}
.tl-viewport{overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch;scrollbar-width:none;cursor:grab;overscroll-behavior-x:contain}
.tl-viewport::-webkit-scrollbar{display:none}
.tl-viewport.is-dragging{cursor:grabbing}
.tl-track{position:relative;display:flex;align-items:stretch;width:max-content;min-height:470px;padding:0 clamp(1rem,4vw,3rem)}
.tl-track::before{content:'';position:absolute;left:0;right:0;top:50%;height:2px;margin-top:-1px;background:linear-gradient(90deg,rgba(122,190,158,.85),rgba(212,175,55,.95) 50%,rgba(122,190,158,.85));box-shadow:0 0 14px rgba(212,175,55,.35);border-radius:2px;z-index:0}
.tl-group{display:contents}
.tl-year{position:relative;flex:0 0 auto;width:clamp(104px,10vw,146px);display:flex;align-items:center;justify-content:center;z-index:3;border:none;background:none;padding:0;margin:0;font:inherit;color:inherit;cursor:pointer;-webkit-appearance:none;appearance:none}
.tl-year-pill{display:inline-flex;align-items:center;gap:.4rem;font-family:var(--font-mono);font-weight:700;font-size:clamp(.92rem,1.9vw,1.12rem);letter-spacing:.13em;color:#0b1c16;background:linear-gradient(135deg,var(--gold-accent),#f0d478);padding:.4rem .8rem;border-radius:999px;box-shadow:0 12px 28px rgba(0,0,0,.4),0 0 0 4px rgba(11,28,22,.55);transition:transform .25s var(--transition-smooth),box-shadow .25s var(--transition-smooth)}
.tl-year:hover .tl-year-pill{transform:translateY(-2px);box-shadow:0 16px 34px rgba(0,0,0,.45),0 0 0 4px rgba(11,28,22,.55)}
.tl-leaf{width:15px;height:18px;flex:0 0 auto;color:#173d2f;display:block}
.tl-year-count,.tl-year-chev{display:none}
.tl-item{position:relative;flex:0 0 clamp(232px,24vw,292px);z-index:1}
.tl-track.tl-anim .tl-item{opacity:0;transform:translateY(14px);transition:opacity .55s var(--transition-smooth),transform .55s var(--transition-smooth)}
.tl-track.tl-anim .tl-item.is-in{opacity:1;transform:translateY(0)}
.tl-dot{position:absolute;left:50%;top:50%;width:13px;height:13px;margin:-6.5px 0 0 -6.5px;border-radius:50%;background:var(--gold-accent);box-shadow:0 0 0 4px rgba(11,28,22,.95),0 0 16px rgba(212,175,55,.6);z-index:3;transition:transform .3s var(--transition-smooth),box-shadow .3s var(--transition-smooth)}
.tl-item[data-soon="1"] .tl-dot{background:rgba(11,28,22,.95);border:2px solid var(--gold-accent);box-shadow:0 0 0 4px rgba(11,28,22,.95)}
.tl-item:hover .tl-dot,.tl-item:focus-within .tl-dot{transform:scale(1.45);box-shadow:0 0 0 4px rgba(11,28,22,.95),0 0 26px rgba(212,175,55,.85)}
.tl-stem{position:absolute;left:50%;width:2px;margin-left:-1px;z-index:1;background:linear-gradient(180deg,rgba(212,175,55,.6),rgba(212,175,55,.1))}
.tl-up .tl-stem{bottom:50%;height:54px}
.tl-down .tl-stem{top:50%;height:54px;background:linear-gradient(0deg,rgba(212,175,55,.6),rgba(212,175,55,.1))}
.tl-card{position:absolute;left:.6rem;right:.6rem;background:rgba(255,255,255,.055);border:1px solid rgba(232,245,240,.14);border-radius:16px;padding:.9rem 1rem 1.05rem;backdrop-filter:blur(10px);box-shadow:0 14px 36px rgba(0,0,0,.3);z-index:2;transition:transform .3s var(--transition-smooth),border-color .3s var(--transition-smooth),background .3s var(--transition-smooth),box-shadow .3s var(--transition-smooth)}
.tl-up .tl-card{bottom:calc(50% + 54px)}
.tl-down .tl-card{top:calc(50% + 54px)}
.tl-item[data-soon="1"] .tl-card{border-style:dashed;border-color:rgba(212,175,55,.42);background:rgba(212,175,55,.05)}
.tl-item:hover .tl-card,.tl-item:focus-within .tl-card{transform:translateY(-5px);border-color:rgba(212,175,55,.55);background:rgba(255,255,255,.11);box-shadow:0 22px 48px rgba(0,0,0,.42)}
.tl-meta{display:flex;align-items:center;flex-wrap:wrap;gap:.4rem;margin-bottom:.5rem}
.tl-month{font-family:var(--font-mono);font-size:.68rem;font-weight:700;letter-spacing:.15em;color:var(--gold-accent)}
.tl-kind{font-family:var(--font-mono);font-size:.6rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.16rem .52rem;border-radius:999px;border:1px solid currentColor;opacity:.92}
.tl-kind[data-kind="field"]{color:#8fd6b4}
.tl-kind[data-kind="tech"]{color:#7cc4dd}
.tl-kind[data-kind="inst"]{color:#b9cfe6}
.tl-kind[data-kind="media"]{color:#e8c766}
.tl-kind[data-kind="award"]{color:#f0a878}
.tl-kind[data-kind="research"]{color:#c3b0e8}
.tl-soon{font-family:var(--font-mono);font-size:.58rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#0b1c16;background:var(--gold-accent);padding:.14rem .5rem;border-radius:999px}
.tl-text{font-size:.94rem;line-height:1.55;color:rgba(255,255,255,.93);font-weight:500}
.tl-controls{display:flex;align-items:center;gap:1rem;margin-top:1.5rem}
.tl-nav{flex:0 0 auto;width:44px;height:44px;border-radius:50%;border:1px solid rgba(232,245,240,.22);background:rgba(255,255,255,.07);color:rgba(232,245,240,.9);font-size:1.1rem;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .22s var(--transition-smooth),background .22s var(--transition-smooth),border-color .22s var(--transition-smooth),opacity .22s ease}
.tl-nav:hover:not(:disabled){transform:translateY(-2px);background:rgba(212,175,55,.18);border-color:rgba(212,175,55,.6);color:#fff}
.tl-nav:disabled{opacity:.26;cursor:default}
.tl-progress{flex:1;height:3px;border-radius:999px;background:rgba(232,245,240,.14);overflow:hidden}
.tl-progress-bar{display:block;height:100%;width:0;border-radius:999px;background:linear-gradient(90deg,var(--light-green),var(--gold-accent));transition:width .16s linear}
.tl-hint{margin-top:1rem;text-align:center;font-family:var(--font-mono);font-size:.74rem;letter-spacing:.05em;color:rgba(232,245,240,.5);line-height:1.6}
.tl-hint-m{display:none}
@media(max-width:860px){
  .tl-viewport{overflow-x:hidden;overflow-y:visible;cursor:auto;padding:0 clamp(1rem,4vw,2rem)}
  .tl-track{flex-direction:column;width:100%;min-height:0;padding:0}
  .tl-track::before{left:7px;right:auto;top:0;bottom:0;width:2px;height:auto;margin:0;background:linear-gradient(180deg,rgba(122,190,158,.9),rgba(212,175,55,.95),rgba(122,190,158,.9))}
  .tl-year{width:100%;justify-content:flex-start;margin:.55rem 0 .2rem;padding:.35rem 0;cursor:pointer}
  .tl-year-pill{width:100%;justify-content:flex-start;gap:.55rem;padding:.55rem .9rem;box-shadow:0 10px 22px rgba(0,0,0,.4),0 0 0 4px rgba(11,28,22,.55)}
  .tl-year-num{flex:0 0 auto}
  .tl-year-count{display:inline-flex;align-items:center;justify-content:center;min-width:1.5rem;height:1.5rem;padding:0 .4rem;border-radius:999px;background:rgba(11,28,22,.82);color:#f0d478;font-size:.68rem;letter-spacing:.04em}
  .tl-year-chev{display:inline-flex;margin-left:auto;font-size:.9rem;line-height:1;transition:transform .3s var(--transition-smooth)}
  .tl-year-chev::before{content:'\25BE'}
  .tl-year[aria-expanded="true"] .tl-year-chev{transform:rotate(180deg)}
  .tl-group{display:block;overflow:hidden;max-height:0;opacity:0;transition:max-height .45s var(--transition-smooth),opacity .3s ease}
  .tl-group.is-open{max-height:5000px;opacity:1}
  .tl-item{flex:0 0 auto;width:100%;padding:.3rem 0 .3rem 30px}
  .tl-track.tl-anim .tl-item{opacity:1;transform:none}
  .tl-up .tl-card,.tl-down .tl-card{position:relative;top:auto;bottom:auto;left:0;right:0}
  .tl-stem{display:none}
  .tl-dot{left:7px;top:1.85rem;margin:0}
  .tl-controls{display:none}
  .tl-hint{display:none}
  .tl-hint-m{display:block}
}
/* ===== TEAM BAR ===== */
.hero-team-bar{position:relative;z-index:1;padding:clamp(.9rem,1.7vw,1.2rem) clamp(1rem,4vw,3rem);background:rgba(9,24,19,.94);backdrop-filter:blur(12px);border-top:1px solid rgba(74,140,115,.22);border-bottom:1px solid rgba(74,140,115,.12)}
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
.info-list li::before{content:"\2713";position:absolute;left:.75rem;top:50%;transform:translateY(-50%);color:var(--light-green);font-weight:900;font-size:1.05rem;background:rgba(232,245,240,.95);width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 22px rgba(15,23,42,.08);transition:transform .25s var(--transition-smooth),background .25s var(--transition-smooth),color .25s var(--transition-smooth)}
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
.footer-figure{margin:clamp(1.9rem,4vw,2.9rem) auto 0;max-width:min(680px,94%);border-radius:var(--radius-lg);overflow:hidden;position:relative;border:1px solid rgba(212,175,55,.28);box-shadow:0 26px 64px rgba(0,0,0,.5);background:#0b1c16;line-height:0}
.footer-figure img{width:100%;height:auto;display:block;transform:scale(1.005);transition:transform .9s var(--transition-smooth),opacity .5s ease}
.footer-figure img.loading{opacity:0}
.footer-figure::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,28,22,.30) 0%,transparent 26%,transparent 74%,rgba(11,28,22,.45) 100%);pointer-events:none}
.footer-figure:hover img{transform:scale(1.04)}
@media(max-width:768px){.touch-zoomable{cursor:zoom-in}.touch-zoomable.is-expanded{position:fixed;inset:0;margin:0!important;width:100vw!important;height:100vh!important;max-width:none!important;max-height:none!important;z-index:9999;background:rgba(0,0,0,.9);border-radius:0!important;box-shadow:none!important;padding:0!important;display:flex;align-items:center;justify-content:center}.touch-zoomable.is-expanded img,.touch-zoomable.is-expanded .hero-image{width:100%;height:100%;object-fit:contain;transform:none!important;box-shadow:none!important}}
@media(max-width:1100px){.image-gallery{grid-template-columns:repeat(6,1fr)}.gallery-item{grid-column:span 3}}
@media(max-width:900px){.dual-sections-grid{grid-template-columns:1fr}.copro-grid{grid-template-columns:1fr}}
@media(max-width:768px){.page,#main,.initial-content,.page__inner-wrap,.page__content,.archive{width:100%!important}.lang-toggle{top:.9rem}.hero{padding:1.5rem 0 1.75rem}.hero-text{max-width:100%;gap:1.1rem}.animated-tagline{flex-direction:column;align-items:center;gap:.45rem}.tagline-pill{padding:.75rem 1.25rem .9rem;max-width:100%;border-radius:26px}.tagline-pill span#hero-tagline-static{font-size:clamp(1.6rem,6.4vw,2.1rem)}.hero-word{font-size:clamp(1.7rem,6.4vw,2.2rem)}.image-gallery{grid-template-columns:repeat(2,1fr)}.gallery-item{grid-column:span 2;aspect-ratio:16/10;max-height:160px;box-shadow:var(--shadow-sm)}.buscadoras-image{max-width:100%;margin-top:1.2rem;box-shadow:var(--shadow-sm)}.collab-card{min-height:auto;box-shadow:var(--shadow-sm)}.collab-logo{min-height:70px;padding:.7rem}.collab-logo img{max-height:60px}.collab-meta{padding:.6rem .8rem .8rem}.collab-name{font-size:.96rem}.collab-note{font-size:.85rem}.social-grid{grid-template-columns:1fr}.social-embed{min-height:auto;box-shadow:var(--shadow-sm)}.iframe-container iframe{height:520px}.project-logo{width:80px}}
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
.stats-ribbon{padding:clamp(1.5rem,3vw,2.2rem) 0;background:radial-gradient(700px 350px at 50% 50%,rgba(232,245,240,.45) 0%,transparent 60%),linear-gradient(180deg,#f7fbfa 0%,#fff 100%);position:relative}
.stats-ribbon-inner{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem);display:flex;justify-content:center;gap:clamp(2rem,5vw,5rem);flex-wrap:wrap}
.stat-item{text-align:center;min-width:120px}
.stat-number{font-size:clamp(2rem,4.5vw,3.2rem);font-weight:900;color:var(--dark-green);font-family:var(--font-body);letter-spacing:-.03em;line-height:1.1;font-variant-numeric:tabular-nums}
.stat-number .stat-plus{color:var(--gold-accent);font-weight:700}
.stat-label{font-size:.72rem;color:var(--text-light);margin-top:.3rem;letter-spacing:.05em;text-transform:uppercase;font-weight:700;font-family:var(--font-mono)}
.stat-divider{width:1px;background:linear-gradient(180deg,transparent,rgba(45,95,77,.15),transparent);align-self:stretch}
@media(max-width:600px){.stats-ribbon-inner{gap:1.5rem 2rem}.stat-divider{display:none}}
.trailer-section{position:relative;overflow:hidden;padding:clamp(3rem,6vw,5rem) 0;background:radial-gradient(1000px 500px at 50% 40%,rgba(212,175,55,.10) 0%,transparent 55%),linear-gradient(180deg,#0e2a1f 0%,#0b1c16 50%,#0e2a1f 100%);isolation:isolate}
.trailer-section::before{content:'';position:absolute;inset:0;background:radial-gradient(600px 300px at 20% 30%,rgba(74,140,115,.12) 0%,transparent 55%),radial-gradient(600px 300px at 80% 70%,rgba(212,175,55,.08) 0%,transparent 55%);pointer-events:none;z-index:0}
.trailer-section::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,transparent 10%,rgba(212,175,55,.35),var(--gold-accent),rgba(212,175,55,.35),transparent 90%);opacity:.7;z-index:1}
.trailer-container{max-width:1000px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem);position:relative;z-index:1;text-align:center}
.trailer-eyebrow{display:inline-flex;align-items:center;gap:.5rem;padding:.3rem .85rem;border-radius:999px;font-size:.72rem;font-weight:750;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-accent);background:rgba(212,175,55,.08);border:1px solid rgba(212,175,55,.25);margin-bottom:1.2rem;font-family:var(--font-mono)}
.trailer-eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--gold-accent);box-shadow:0 0 8px rgba(212,175,55,.5)}
.trailer-title{font-size:clamp(1.8rem,4.5vw,3rem);font-weight:400;font-family:var(--font-display);color:#fff;margin-bottom:.6rem;letter-spacing:0;line-height:1.2;text-shadow:0 8px 24px rgba(0,0,0,.3)}
.trailer-subtitle{font-size:clamp(1rem,2.2vw,1.2rem);color:rgba(232,245,240,.65);margin-bottom:clamp(1.5rem,3vw,2.5rem);max-width:700px;margin-left:auto;margin-right:auto;line-height:1.7;font-weight:400}
.trailer-embed-wrapper{position:relative;width:100%;max-width:900px;margin:0 auto;border-radius:var(--radius-lg);overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.45),0 0 0 1px rgba(255,255,255,.08);border:1px solid rgba(74,140,115,.20);background:#000;transition:transform .4s var(--transition-smooth),box-shadow .4s var(--transition-smooth)}
.trailer-embed-wrapper:hover{transform:translateY(-4px);box-shadow:0 32px 72px rgba(0,0,0,.55),0 0 0 1px rgba(212,175,55,.15)}
.trailer-embed-responsive{position:relative;padding-bottom:56.25%;height:0;overflow:hidden}
.trailer-embed-responsive iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
.trailer-caption{margin-top:1.4rem;display:flex;align-items:center;justify-content:center;gap:.8rem;flex-wrap:wrap}
.trailer-caption-text{font-size:clamp(.82rem,1.6vw,.92rem);color:rgba(232,245,240,.55);font-family:var(--font-mono);letter-spacing:.03em}
.trailer-caption-divider{width:28px;height:1px;background:linear-gradient(90deg,transparent,rgba(212,175,55,.4),transparent)}
@media(max-width:768px){.trailer-section{padding:clamp(2rem,5vw,3.5rem) 0}.trailer-embed-wrapper{border-radius:var(--radius-md)}}
.copro-section{padding:clamp(2.5rem,5vw,4.25rem) 0;border-bottom:1px solid var(--border-light);position:relative;scroll-margin-top:2rem}
.copro-inner{max-width:1400px;margin:0 auto;padding:0 clamp(1rem,4vw,3rem)}
.copro-eyebrow{display:inline-flex;align-items:center;gap:.5rem;padding:.3rem .85rem;border-radius:999px;font-size:.72rem;font-weight:750;letter-spacing:.14em;text-transform:uppercase;color:var(--primary-green);background:rgba(45,95,77,.07);border:1px solid rgba(45,95,77,.16);margin-bottom:1rem;font-family:var(--font-mono)}
.copro-eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--gold-accent);box-shadow:0 0 8px rgba(212,175,55,.5)}
.copro-lead{font-size:clamp(1.15rem,2.6vw,1.5rem);line-height:1.6;color:var(--text-dark);font-weight:450;max-width:920px;margin-bottom:1.1rem}
.copro-lead strong{color:var(--primary-green);font-weight:750}
.copro-body{font-size:clamp(1.02rem,2.2vw,1.15rem);line-height:1.85;color:var(--text-medium);max-width:920px;margin-bottom:1rem}
.copro-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(1.5rem,3vw,2.75rem);align-items:center;margin-top:clamp(1.75rem,3vw,2.5rem)}
.copro-quote{position:relative;border-radius:var(--radius-lg);padding:clamp(1.75rem,3vw,2.5rem) clamp(1.75rem,3vw,2.75rem);background:radial-gradient(circle at 12% 0%,rgba(212,175,55,.10) 0%,transparent 55%),linear-gradient(135deg,#0e2a1f 0%,#0b1c16 100%);overflow:hidden;isolation:isolate;box-shadow:var(--shadow-lg)}
.copro-quote::before{content:'\201C';position:absolute;top:-.35em;left:.28em;font-family:var(--font-display);font-size:8rem;line-height:1;color:rgba(212,175,55,.22);pointer-events:none;z-index:0}
.copro-quote-text{position:relative;z-index:1;font-family:var(--font-display);font-style:italic;font-size:clamp(1.3rem,2.6vw,1.7rem);line-height:1.5;color:#fff;letter-spacing:.01em;margin-bottom:1.1rem}
.copro-quote-attr{position:relative;z-index:1;font-family:var(--font-mono);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(212,175,55,.85);font-weight:700}
.copro-quote-sub{position:relative;z-index:1;display:block;margin-top:.5rem;font-family:var(--font-body);font-size:.92rem;line-height:1.6;color:rgba(232,245,240,.72);text-transform:none;letter-spacing:0;font-weight:400}
.copro-example{background:#fff;border-radius:var(--radius-lg);border:1px solid rgba(45,95,77,.12);box-shadow:var(--shadow-md);padding:clamp(1.5rem,2.8vw,2rem);position:relative;overflow:hidden}
.copro-example::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--gold-accent),rgba(212,175,55,.25));opacity:.85}
.copro-example-label{font-family:var(--font-mono);font-size:.7rem;font-weight:750;letter-spacing:.12em;text-transform:uppercase;color:var(--light-green);margin-bottom:.55rem}
.copro-example-title{font-size:1.15rem;font-weight:800;color:var(--dark-green);line-height:1.35;letter-spacing:-.01em;margin-bottom:.55rem}
.copro-example-text{font-size:.98rem;line-height:1.75;color:var(--text-medium)}
.copro-example-text strong{color:var(--primary-green);font-weight:700}
.fwos{margin-top:clamp(2.5rem,4vw,3.5rem)}
.fwos-title{font-size:clamp(1.4rem,3vw,2rem);font-weight:400;font-family:var(--font-display);color:var(--dark-green);margin-bottom:.4rem;line-height:1.25}
.fwos-sub{font-size:clamp(1rem,2.1vw,1.12rem);color:var(--text-medium);line-height:1.75;max-width:820px;margin-bottom:1.5rem}
.fwos-figure{width:100%;max-width:980px;margin:0 auto;display:block}
.fwos-figure svg{width:100%;height:auto;display:block;overflow:visible}
.fwos-caption{text-align:center;font-family:var(--font-mono);font-size:.8rem;color:var(--text-light);letter-spacing:.03em;margin-top:1rem}
</style>
<!-- TITLE SECTION -->
<section class="title-section">
  <div class="lang-toggle" aria-label="Language selection">
    <button type="button" class="lang-btn active" data-lang="en">EN</button>
    <button type="button" class="lang-btn" data-lang="es">ES</button>
  </div>
  <div class="title-inner">
    <div class="title-brand">
      <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9466ebc27c9487e8bfbff1d1dd904f4f9e6df81d/images/logo_FOUND_white.png" alt="FOUND logo" class="project-logo" />
      <h1 class="project-title">FOUND</h1>
    </div>
    <hr class="title-divider" />
    <p class="project-subtitle" id="project-subtitle"><span class="title-accent">Interpreting Nature</span> to Locate Those Who We Are Missing</p>
  </div>
</section>
<!-- HERO -->
<section class="hero">
  <div class="hero-content">
    <div class="hero-text reveal">
      <div class="animated-tagline">
        <div class="tagline-pill" aria-label="FOUND tagline">
          <span id="hero-tagline-static">Using technology to</span>
          <div class="word-carousel" role="text"><span id="hero-word" class="hero-word">search.</span></div>
        </div>
      </div>
      <p class="hero-description" id="hero-main-text">Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change and building institutional capacity to improve how governments respond to disappearance.</p>
      <a class="hero-cue" href="#journey" id="hero-cue">Explore our journey <span class="cue-arrow" aria-hidden="true">&#x2193;</span></a>
    </div>
  </div>
</section>
<!-- TIMELINE -->
<section class="timeline-section" id="journey" aria-label="FOUND timeline 2023 to 2027">
  <div class="tl-inner">
    <div class="tl-head reveal">
      <div class="tl-eyebrow" id="tl-eyebrow">Our journey &middot; 2023 &ndash; 2027</div>
      <h2 class="tl-title" id="tl-title"></h2>
      <p class="tl-sub" id="tl-sub">From the first experimental site in Jalisco to platforms now running inside the national search commissions of Mexico and Colombia.</p>
      <div class="tl-filters" id="tl-filters" role="group" aria-label="Jump to year">
        <button type="button" class="tl-chip is-active" data-year="2023">2023</button>
        <button type="button" class="tl-chip" data-year="2024">2024</button>
        <button type="button" class="tl-chip" data-year="2025">2025</button>
        <button type="button" class="tl-chip" data-year="2026">2026</button>
        <button type="button" class="tl-chip" data-year="2027">2027</button>
      </div>
    </div>
  </div>
  <div class="tl-stage">
    <div class="tl-viewport" id="tl-viewport" tabindex="0" role="region" aria-label="FOUND milestones, scrollable timeline">
      <div class="tl-track" id="tl-track"></div>
    </div>
  </div>
  <div class="tl-inner">
    <div class="tl-controls">
      <button type="button" class="tl-nav" id="tl-prev" aria-label="Previous milestones">&#x2190;</button>
      <div class="tl-progress" aria-hidden="true"><span class="tl-progress-bar" id="tl-bar"></span></div>
      <button type="button" class="tl-nav" id="tl-next" aria-label="Next milestones">&#x2192;</button>
    </div>
    <p class="tl-hint" id="tl-hint">Drag, scroll or use the arrows to travel through the timeline &middot; Click a year to jump</p>
    <p class="tl-hint tl-hint-m" id="tl-hint-m">Tap a year to open its milestones</p>
  </div>
</section>
<!-- TEAM BAR -->
<div class="hero-team-bar">
  <div class="hero-team-bar-inner">
    <span class="htb-label">FOUND<span class="htb-brace">{</span>Team<span class="htb-brace">}</span></span>
    <span class="htb-divider">&middot;</span>
    <span class="htb-text" id="hero-team-text">Our core team brings together <strong>collectives of families from Jalisco, Zacatecas, and Colombia searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco's Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico's National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.</span>
  </div>
</div>
<!-- GIF STRIP -->
<section class="gif-strip" aria-label="FOUND in action">
  <div class="gif-strip-inner">
    <div class="gs-panel gs-panel-main touch-zoomable" data-label="Spectral indices, clandestine crematoriums, substance detection"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/1047db9c85ff842e083e9fb45c0bdf05213da88a/images/NDAI5.gif" alt="FOUND Project team using advanced technology in field search operations" loading="lazy" class="loading" onload="this.classList.remove('loading')" /></div>
    <div class="gs-panel gs-panel-side touch-zoomable" data-label="Satellite analysis, time series"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/33b2627b6b245e9632f59abf0a02f5ad58956bf4/images/Areas_de_busqueda_3.gif" alt="Satellite spectral time-series analysis of search areas" loading="lazy" class="loading" onload="this.classList.remove('loading')" /></div>
    <div class="gs-panel gs-panel-side touch-zoomable" data-label="Clandestine space detection"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/9b9df755f7129ba10ee53479d528d42d14e5648a/images/ClandestineSpace.gif" alt="Spectral detection of clandestine sites using satellite imagery" loading="lazy" class="loading" onload="this.classList.remove('loading')" /></div>
  </div>
  <div class="gif-strip-caption"><div class="gif-caption-inner">
    <span class="gif-caption-tag">Platforms<span class="gif-caption-brace">{</span>core member: CentroGeo<span class="gif-caption-brace">}</span></span>
    <span class="gif-caption-divider">&middot;</span>
    <span class="gif-caption-item"><strong>Spectral indices</strong> &mdash; Identifying substances linked to disappearances via satellite and drone imagery, and when they were present.</span>
    <span class="gif-caption-divider">&middot;</span>
    <span class="gif-caption-item"><strong>Clandestine sites location</strong> &mdash; AI that finds what was meant to stay hidden.</span>
  </div></div>
</section>
<!-- STATS RIBBON -->
<section class="stats-ribbon reveal" aria-label="Key statistics">
  <div class="stats-ribbon-inner">
    <div class="stat-item"><div class="stat-number"><span class="stat-value" data-to="7">7</span><span class="stat-plus">+</span></div><div class="stat-label" id="stat-label-1">Technologies deployed</div></div>
    <div class="stat-divider"></div>
    <div class="stat-item"><div class="stat-number"><span class="stat-value" data-to="20">20</span><span class="stat-plus">+</span></div><div class="stat-label" id="stat-label-2">Institutional partners</div></div>
    <div class="stat-divider"></div>
    <div class="stat-item"><div class="stat-number"><span class="stat-value" data-to="3">3</span></div><div class="stat-label" id="stat-label-3">Countries</div></div>
  </div>
</section>
<!-- ===== DOCUMENTARY TRAILER ===== -->
<section class="trailer-section reveal" id="documentary" aria-label="FOUND documentary trailer">
  <div class="trailer-container">
    <div class="trailer-eyebrow" id="trailer-eyebrow">Documentary</div>
    <h2 class="trailer-title" id="trailer-title" style="color:#fff;padding-bottom:0;margin-bottom:.6rem">Watch the Trailer</h2>
    <p class="trailer-subtitle" id="trailer-subtitle">The story of families, science, and the search for those who are missing.</p>
    <div class="trailer-embed-wrapper">
      <div class="trailer-embed-responsive">
        <iframe src="https://www.youtube.com/embed/hbo9H4yj1VQ?si=0o_D0HgsLp2pMjW5" title="FOUND Documentary Trailer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>
    <div class="trailer-caption">
      <span class="trailer-caption-text" id="trailer-caption-text">FOUND Documentary</span>
      <span class="trailer-caption-divider"></span>
      <span class="trailer-caption-text">2026</span>
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
<section class="copro-section reveal" id="coproduction" aria-label="Coproduction with search groups">
  <div class="copro-inner">
    <div class="copro-eyebrow" id="copro-eyebrow">Coproduction with search groups</div>
    <p class="copro-lead"><strong id="copro-lead">The knowledge was already there.</strong></p>
    <p class="copro-body" id="copro-body">For years, searching mothers have walked hills, ranches, abandoned houses and countless roads across Mexico. They learned to read the earth with a precision no book or scientist taught them: that disturbed soil looks different, that certain flowers bloom where or when they shouldn't, that vegetation changes colour where the ground holds extra nutrients as a result of the presence of buried bodies. This is, in effect, forensic knowledge; a practice of citizen science. FOUND begins by listening, learning, and building the place where this knowledge can sit at the same table as science, context analysis, and the institutions responsible for the search.</p>
    <div class="copro-grid">
      <figure class="copro-quote">
        <p class="copro-quote-text" id="copro-quote-text">When families speak, they speak in the present tense. "He is a son." "She is a student." The verb stays in present tense. There is an ethic in that grammar &mdash; and we have learned it from them, and made it our own.</p>
        <figcaption class="copro-quote-attr" id="copro-quote-attr">A principle FOUND adopted from searching families
          <span class="copro-quote-sub" id="copro-quote-sub">"There is always something" &mdash; in the words of the mothers, nature is a witness of what happens.</span>
        </figcaption>
      </figure>
      <div class="copro-example">
        <div class="copro-example-label" id="copro-ex-label">Coproduction in practice &middot; Tlajomulco</div>
        <div class="copro-example-title" id="copro-ex-title">An example of how families codesigned an experimental site</div>
        <p class="copro-example-text" id="copro-ex-text">Our experimental sites were not built from institutional data or scientific evidence alone. Families described that when large amounts of soil are moved to install <strong>electrical-tower bases</strong>, clandestine graves can appear in that disturbed ground. So we built a site beside electrical towers to replicate exactly that condition &mdash; and to test how each instrument behaves where the problem actually occurs. The methods adapt to each place; the principle of coproduction with families does not.</p>
      </div>
    </div>
    <div class="fwos">
      <h2 class="fwos-title" id="fwos-title" style="padding-bottom:0">Four ways of seeing the territory</h2>
      <p class="fwos-sub" id="fwos-sub">FOUND is the integration of four ways of observing the land. The work is to hold the conversation between them &mdash; so that, together, they lead to better-equipped and better-informed search.</p>
      <figure class="fwos-figure" aria-label="Diagram: four ways of seeing converging on coproduced search">
        <svg viewBox="0 0 980 520" role="img" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="fwosCore" cx="50%" cy="50%" r="60%">
              <stop offset="0%" stop-color="#2d5f4d"/>
              <stop offset="100%" stop-color="#0e2a1f"/>
            </radialGradient>
            <linearGradient id="fwosLine" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="#4a8c73" stop-opacity="0.15"/>
              <stop offset="100%" stop-color="#d4af37" stop-opacity="0.75"/>
            </linearGradient>
            <filter id="fwosShadow" x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#0f172a" flood-opacity="0.14"/>
            </filter>
          </defs>
          <g stroke="url(#fwosLine)" stroke-width="2.5" fill="none">
            <line x1="210" y1="120" x2="490" y2="260"/>
            <line x1="770" y1="120" x2="490" y2="260"/>
            <line x1="210" y1="400" x2="490" y2="260"/>
            <line x1="770" y1="400" x2="490" y2="260"/>
          </g>
          <g filter="url(#fwosShadow)"><rect x="40" y="70" width="320" height="100" rx="18" fill="#ffffff" stroke="rgba(45,95,77,.16)"/></g>
          <circle cx="74" cy="104" r="7" fill="#d4af37"/>
          <text id="fwos-n1-k" x="92" y="100" font-family="'JetBrains Mono',monospace" font-size="12" font-weight="700" fill="#2d5f4d" letter-spacing="1.5">01 &#183; FAMILIES' KNOWLEDGE</text>
          <text id="fwos-n1-t" x="64" y="132" font-family="'DM Sans',sans-serif" font-size="15.5" font-weight="700" fill="#1e4034">Reading the landscape</text>
          <text id="fwos-n1-s" x="64" y="153" font-family="'DM Sans',sans-serif" font-size="13.5" fill="#3f3f3f">Signs in nature &#183; care &#183; memory</text>
          <g filter="url(#fwosShadow)"><rect x="620" y="70" width="320" height="100" rx="18" fill="#ffffff" stroke="rgba(45,95,77,.16)"/></g>
          <circle cx="654" cy="104" r="7" fill="#d4af37"/>
          <text id="fwos-n2-k" x="672" y="100" font-family="'JetBrains Mono',monospace" font-size="12" font-weight="700" fill="#2d5f4d" letter-spacing="1.5">02 &#183; CONTEXT ANALYSIS</text>
          <text id="fwos-n2-t" x="644" y="132" font-family="'DM Sans',sans-serif" font-size="15.5" font-weight="700" fill="#1e4034">Territorial &amp; criminal patterns</text>
          <text id="fwos-n2-s" x="644" y="153" font-family="'DM Sans',sans-serif" font-size="13.5" fill="#3f3f3f">Why a place becomes clandestine</text>
          <g filter="url(#fwosShadow)"><rect x="40" y="350" width="320" height="100" rx="18" fill="#ffffff" stroke="rgba(45,95,77,.16)"/></g>
          <circle cx="74" cy="384" r="7" fill="#d4af37"/>
          <text id="fwos-n3-k" x="92" y="380" font-family="'JetBrains Mono',monospace" font-size="12" font-weight="700" fill="#2d5f4d" letter-spacing="1.5">03 &#183; REMOTE SENSING &amp; GEOPHYSICS</text>
          <text id="fwos-n3-t" x="64" y="412" font-family="'DM Sans',sans-serif" font-size="15.5" font-weight="700" fill="#1e4034">Reading from air, space &amp; below</text>
          <text id="fwos-n3-s" x="64" y="433" font-family="'DM Sans',sans-serif" font-size="13.5" fill="#3f3f3f">Spectral &#183; LiDAR &#183; seismic &#183; Machine Learning</text>
          <g filter="url(#fwosShadow)"><rect x="620" y="350" width="320" height="100" rx="18" fill="#ffffff" stroke="rgba(45,95,77,.16)"/></g>
          <circle cx="654" cy="384" r="7" fill="#d4af37"/>
          <text id="fwos-n4-k" x="672" y="380" font-family="'JetBrains Mono',monospace" font-size="12" font-weight="700" fill="#2d5f4d" letter-spacing="1.5">04 &#183; INSTITUTIONAL PRACTICE</text>
          <text id="fwos-n4-t" x="644" y="412" font-family="'DM Sans',sans-serif" font-size="15.5" font-weight="700" fill="#1e4034">Formal search decisions</text>
          <text id="fwos-n4-s" x="644" y="433" font-family="'DM Sans',sans-serif" font-size="13.5" fill="#3f3f3f">Legal &amp; operational backing</text>
          <circle cx="490" cy="260" r="92" fill="url(#fwosCore)" filter="url(#fwosShadow)"/>
          <circle cx="490" cy="260" r="92" fill="none" stroke="#d4af37" stroke-opacity="0.5" stroke-width="1.5"/>
          <text id="fwos-core1" x="490" y="246" text-anchor="middle" font-family="'DM Serif Display',serif" font-style="italic" font-size="21" fill="#ffffff">Coproduced</text>
          <text id="fwos-core2" x="490" y="272" text-anchor="middle" font-family="'DM Serif Display',serif" font-style="italic" font-size="21" fill="#ffffff">search</text>
          <text id="fwos-sub1" x="490" y="293" text-anchor="middle" font-family="'JetBrains Mono',monospace" font-size="9" fill="rgba(212,175,55,.9)" letter-spacing="1">PRACTICES &#183; PLATFORMS</text>
          <text id="fwos-sub2" x="490" y="306" text-anchor="middle" font-family="'JetBrains Mono',monospace" font-size="9" fill="rgba(212,175,55,.9)" letter-spacing="1">&#183; POLICY</text>
        </svg>
      </figure>
      <figcaption class="fwos-caption" id="fwos-caption">None of these pieces is enough on its own. FOUND builds the place where they converse &mdash; and decide, together, where to search.</figcaption>
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
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/5%20logo%20IGeofisicaUNAM.png" alt="UNAM Geophysics" loading="lazy" onload="this.classList.remove('loading')" style="filter:brightness(0) invert(0);"></div><div class="collab-meta"><div class="collab-name" id="collab-item-unam-geo">UNAM &ndash; Geophysics</div><div class="collab-note" id="collab-note-unam-geo">Technical expertise</div></div></div>
        <div class="collab-card touch-zoomable"><div class="collab-logo"><img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/0ed8741a1541acc7269cded8a4eb5b46bf515ecd/images/6%20logo%20Ingenieria%20UNAM.png" alt="UNAM Engineering" loading="lazy" class="loading" onload="this.classList.remove('loading')"></div><div class="collab-meta"><div class="collab-name" id="collab-item-unam-eng">UNAM &ndash; Engineering</div><div class="collab-note" id="collab-note-unam-eng">Technical expertise</div></div></div>
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
      <div class="social-embed twitter-embed"><div class="iframe-container"><blockquote class="twitter-tweet"><p lang="en" dir="ltr">Almost a year after I started researching the story, I'm thrilled that my <a href="https://twitter.com/guardian?ref_src=twsrc%5Etfw">@guardian</a> article about the innovations being used to try and find some of the thousands of people who have disappeared in Mexico is the most read in its Global Development section. <a href="https://t.co/NztFCj4uEF">https://t.co/NztFCj4uEF</a></p>&mdash; Suzanne Bearne (@sbearne) <a href="https://twitter.com/sbearne/status/1991827389375193330?ref_src=twsrc%5Etfw">November 21, 2025</a></blockquote></div></div>
      <div class="social-embed twitter-embed"><div class="iframe-container"><blockquote class="twitter-tweet"><p lang="es" dir="ltr">Cómo los cerdos y los insectos están ayudando a encontrar a los desaparecidos en México <a href="https://t.co/sJC3oaNLGL">https://t.co/sJC3oaNLGL</a></p>&mdash; BBC News Mundo (@bbcmundo) <a href="https://twitter.com/bbcmundo/status/1973352689867063513?ref_src=twsrc%5Etfw">October 1, 2025</a></blockquote></div></div>
    </div>
  </div>
</section>
<!-- FOOTER -->
<footer class="footer">
  <div class="footer-content">
    <em id="footer-text">FOUND: Interpreting Nature to Locate Those Who We Are Missing.</em>
    <hr class="footer-line" />
    <figure class="footer-figure reveal touch-zoomable">
      <img src="/images/in-the-flowers-web.jpg" alt="A woman standing in a field of marigolds and roses, holding a close embrace with a figure made entirely of flowers" loading="lazy" decoding="async" class="loading" onload="this.classList.remove('loading')" onerror="this.onerror=null;this.src='https://raw.githubusercontent.com/FOUND-project/found-project.github.io/dd7511b6f55996f5326948a347665c5b24da86ca/images/In%20the%20flowers1.png';this.classList.remove('loading')">
    </figure>
  </div>
</footer>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<script>
{% raw %}
(function(){
  var translations={
    en:{'copro-eyebrow':'Coproduction with search groups','copro-lead':'The knowledge was already there.','copro-body':'For years, searching mothers have walked hills, ranches, abandoned houses and countless roads across Mexico. They learned to read the earth with a precision no book or scientist taught them: that disturbed soil looks different, that certain flowers bloom where or when they shouldn\'t, that vegetation changes colour where the ground holds extra nutrients as a result of the presence of buried bodies. This is, in effect, forensic knowledge; a practice of citizen science. FOUND begins by listening, learning, and building the place where this knowledge can sit at the same table as science, context analysis, and the institutions responsible for the search.','copro-quote-text':'When families speak, they speak in the present tense. "He is a son." "She is a student." The verb stays in present tense. There is an ethic in that grammar — and we have learned it from them, and made it our own.','copro-quote-attr':'A principle FOUND adopted from searching families <span class="copro-quote-sub" id="copro-quote-sub">"There is always something" — in the words of the mothers, nature is a witness of what happens.</span>','copro-ex-label':'Coproduction in practice · Tlajomulco','copro-ex-title':'An example of how families codesigned an experimental site','copro-ex-text':'Our experimental sites were not built from institutional data or scientific evidence alone. Families described that when large amounts of soil are moved to install <strong>electrical-tower bases</strong>, clandestine graves can appear in that disturbed ground. So we built a site beside electrical towers to replicate exactly that condition — and to test how each instrument behaves where the problem actually occurs. The methods adapt to each place; the principle of coproduction with families does not.','fwos-title':'Four ways of seeing the territory','fwos-sub':'FOUND is the integration of four ways of observing the land. The work is to hold the conversation between them — so that, together, they lead to better-equipped and better-informed search.','fwos-caption':'None of these pieces is enough on its own. FOUND builds the place where they converse — and decide, together, where to search.','fwos-n1-k':'01 · FAMILIES\' KNOWLEDGE','fwos-n1-t':'Reading the landscape','fwos-n1-s':'Signs in nature · care · memory','fwos-n2-k':'02 · CONTEXT ANALYSIS','fwos-n2-t':'Territorial & criminal patterns','fwos-n2-s':'Why a place becomes clandestine','fwos-n3-k':'03 · REMOTE SENSING & GEOPHYSICS','fwos-n3-t':'Reading from air, space & below','fwos-n3-s':'Spectral · LiDAR · seismic · Machine Learning','fwos-n4-k':'04 · INSTITUTIONAL PRACTICE','fwos-n4-t':'Formal search decisions','fwos-n4-s':'Legal & operational backing','fwos-core1':'Coproduced','fwos-core2':'search','fwos-sub1':'PRACTICES · PLATFORMS','fwos-sub2':'· POLICY','trailer-eyebrow':'Documentary','trailer-title':'Watch the Trailer','trailer-subtitle':'The story of families, science, and the search for those who are missing.','trailer-caption-text':'FOUND Documentary','collab-item-labco':'LABCO','collab-note-labco':'Exploring AI together to locate and identify','collab-item-eaaf':'Argentine Forensic Anthropology Team (EAAF)','collab-note-eaaf':"Luis Fondebrider, FOUND's advisor",'collab-item-ori':'Oxford Robotics Institute','collab-note-ori':'Partnership, technical expertise','collab-item-ipn':'Instituto Politécnico Nacional','collab-note-ipn':'Technical expertise, Technology','project-subtitle':'<span class="title-accent">Interpreting Nature</span> to Locate Those Who We Are Missing','hero-tagline-static':'Using technology to','word-1':'search.','word-2':'remember.','word-3':'dignify.','word-4':'find.','word-5':'bring closure.','hero-main-text':'Over 130,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> works at the intersection of frontier technology and the lived knowledge of search groups, driving systemic change and building institutional capacity to improve how governments respond to disappearance.','hero-cue':'Explore our journey <span class="cue-arrow" aria-hidden="true">&#x2193;</span>','tl-eyebrow':'Our journey · 2023 – 2027','tl-title':'Our journey, milestone by milestone','tl-sub':'From the first experimental site in Jalisco to platforms now running inside the national search commissions of Mexico and Colombia.','tl-hint':'Drag, scroll or use the arrows to travel through the timeline · Click a year to jump','tl-hint-m':'Tap a year to open its milestones','hero-team-text':"Our core team brings together <strong>collectives of families from Jalisco, Zacatecas, and Colombia searching for their missing loved ones</strong>, alongside CentroGeo, the University of Oxford, Jalisco's Search Commission, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara. We work alongside strategic partners including the UK Foreign, Commonwealth and Development Office (FCDO), the Executive Office of the UN Secretary-General, the Colombian Search Unit (UBPD), Mexico's National Search Commission, LAB-CO, and forensic anthropologist Luis Fondebrider.",'collab-title':'Institutional Partnerships','tech-title':'Technologies in Action','tech-item-1':'Multispectral & Hyperspectral Imaging','tech-item-2':'Airborne LiDAR','tech-item-3':'Seismic Noise Interferometry (TIRSA)','tech-item-4':'Electrical Resistivity Tomography, Conductivimetry','tech-item-5':'Satellite Spectral Analysis','tech-item-ml':'Machine Learning','tech-item-6':'Forensic Entomology, Botany, Territorial Analysis, Soil Science','buscadoras-title':'The Role of Buscadoras','buscadoras-text':"Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.",'social-title':'Follow Our Journey','social-subtitle':'Stay connected with our latest findings, community stories, and collaborations','footer-text':'FOUND: Interpreting Nature to Locate Those Who We Are Missing.','stat-label-1':'Technologies deployed','stat-label-2':'Institutional partners','stat-label-3':'Countries'},
    es:{'copro-eyebrow':'Coproducción con colectivos de búsqueda','copro-lead':'El conocimiento ya estaba ahí.','copro-body':'Durante años, las madres buscadoras han recorrido cerros, ranchos, casas abandonadas e innumerables caminos y veredas por todo México. Aprendieron a leer la naturaleza con una precisión que ningún libro ni científico les enseñó: que un suelo removido se ve distinto, que ciertas flores brotan donde o cuando no deberían, que la vegetación cambia de color donde el suelo guarda nutrientes adicionales por la presencia de cuerpos enterrados. Esto es, en efecto, un saber forense; una práctica de ciencia ciudadana. FOUND comienza por escuchar, aprender y construir el lugar donde ese conocimiento puede sentarse a la misma mesa que la ciencia, el análisis de contexto y las instituciones responsables de la búsqueda.','copro-quote-text':'Las familias hablan en presente. «Es hijo.» «Es estudiante.» El verbo se mantiene en presente. Hay una ética en esa gramática — y la hemos aprendido de ellas, y la hemos hecho nuestra.','copro-quote-attr':'Un principio que FOUND adoptó de las familias buscadoras <span class="copro-quote-sub" id="copro-quote-sub">«Siempre hay algo» — en palabras de las madres, la naturaleza es testiga de lo que ocurre.</span>','copro-ex-label':'Coproducción en la práctica · Tlajomulco','copro-ex-title':'Un ejemplo de cómo las familias codiseñaron un sitio de experimentación','copro-ex-text':'Nuestros sitios de experimentación no se construyeron únicamente a partir de datos institucionales o evidencia científica. Las familias describieron que, cuando se mueven grandes cantidades de tierra para instalar las bases de <strong>torres eléctricas</strong>, pueden aparecer fosas clandestinas en ese suelo removido. Por eso construimos un sitio junto a torres eléctricas para replicar exactamente esa condición — y probar cómo se comporta cada instrumento ahí donde el problema realmente ocurre. Los métodos se adaptan a cada lugar; el principio de coproducción con las familias, no.','fwos-title':'Cuatro maneras de observar el entorno','fwos-sub':'FOUND es la integración de cuatro maneras de observar el entorno y la naturaleza. El trabajo es sostener la conversación entre ellas — para que, juntas, conduzcan a una búsqueda mejor equipada y mejor informada.','fwos-caption':'Ninguna de estas piezas basta por sí sola. FOUND construye el lugar donde conversan — y deciden, juntas, dónde buscar.','fwos-n1-k':'01 · CONOCIMIENTO DE LAS FAMILIAS','fwos-n1-t':'Leer el paisaje','fwos-n1-s':'Señales en la naturaleza · cuidado · memoria','fwos-n2-k':'02 · ANÁLISIS DE CONTEXTO','fwos-n2-t':'Patrones territoriales y criminales','fwos-n2-s':'Por qué un lugar se vuelve clandestino','fwos-n3-k':'03 · PERCEPCIÓN REMOTA Y GEOFÍSICA','fwos-n3-t':'Leer desde el aire, el espacio y el subsuelo','fwos-n3-s':'Espectral · LiDAR · sísmico · Machine Learning','fwos-n4-k':'04 · PRÁCTICA INSTITUCIONAL','fwos-n4-t':'Decisiones formales de búsqueda','fwos-n4-s':'Respaldo legal y operativo','fwos-core1':'Búsqueda','fwos-core2':'coproducida','fwos-sub1':'PRÁCTICAS · PLATAFORMAS','fwos-sub2':'· POLÍTICAS','trailer-eyebrow':'Documental','trailer-title':'Mira el tráiler','trailer-subtitle':'La historia de las familias, la ciencia y la búsqueda de quienes nos faltan.','trailer-caption-text':'Documental FOUND','collab-item-labco':'LABCO','collab-note-labco':'Explorando juntos el uso de IA para localizar e identificar','collab-item-eaaf':'Equipo Argentino de Antropología Forense (EAAF)','collab-note-eaaf':'Luis Fondebrider, asesor de FOUND','collab-item-ori':'Oxford Robotics Institute','collab-note-ori':'Alianza, experiencia técnica','collab-item-ipn':'Instituto Politécnico Nacional','collab-note-ipn':'Experiencia técnica, desarrollo tecnológico','project-subtitle':'<span class="title-accent">Interpretar la Naturaleza</span> para Encontrar a Quienes Nos Faltan','hero-tagline-static':'Usando tecnología para','word-1':'buscar.','word-2':'recordar.','word-3':'dignificar.','word-4':'encontrar.','word-5':'dar cierre.','hero-main-text':'Más de 130,000 personas están registradas como desaparecidas en México. Detrás de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> trabaja en la intersección entre la tecnología de frontera y el conocimiento vivido de los colectivos de búsqueda, impulsando cambios sistémicos y fortaleciendo las capacidades institucionales para mejorar la respuesta de los gobiernos ante la desaparición.','hero-cue':'Recorre nuestro camino <span class="cue-arrow" aria-hidden="true">&#x2193;</span>','tl-eyebrow':'Nuestro camino · 2023 – 2027','tl-title':'Nuestro camino, hito a hito','tl-sub':'Del primer sitio experimental en Jalisco a plataformas que hoy operan dentro de las comisiones nacionales de México y Colombia.','tl-hint':'Arrastra, desplázate o usa las flechas para recorrer la línea del tiempo · Haz clic en un año para saltar','tl-hint-m':'Toca un año para ver sus hitos','hero-team-text':'Nuestro equipo central reúne <strong>colectivos de familias de Jalisco, Zacatecas y Colombia que buscan a sus seres queridos desaparecidos</strong>, junto a CentroGeo, la Universidad de Oxford, la Comisión de Búsqueda de Jalisco, la Universidad Nacional Autónoma de México (UNAM) y la Universidad de Guadalajara. Trabajamos junto a socios estratégicos, entre ellos la Oficina para Asuntos Exteriores, de la Commonwealth y de Desarrollo del Reino Unido (FCDO), la Oficina Ejecutiva del Secretario General de la ONU, la Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD) de Colombia, la Comisión Nacional de Búsqueda de México, LAB-Co y el antropólogo forense Luis Fondebrider.','collab-title':'Alianzas institucionales','tech-title':'Tecnologías en acción','tech-item-1':'Imágenes multiespectrales e hiperespectrales','tech-item-2':'LiDAR aerotransportado','tech-item-3':'Interferometría de ruido sísmico (TIRSA)','tech-item-4':'Tomografía de resistividad eléctrica y mediciones de conductividad','tech-item-5':'Análisis espectral satelital','tech-item-ml':'Machine Learning','tech-item-6':'Entomología forense, botánica, análisis territorial y ciencia del suelo','buscadoras-title':'El papel de las buscadoras','buscadoras-text':'Los colectivos liderados por mujeres están en el corazón del trabajo de FOUND. Han transformado la conversación nacional sobre desaparición y justicia. Sus prácticas de búsqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus métodos en nuestros esfuerzos tecnológicos.','social-title':'Sigue nuestro camino','social-subtitle':'Mantente al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.','footer-text':'FOUND: Interpretar la Naturaleza para Encontrar a Quienes Nos Faltan.','stat-label-1':'Tecnologías desplegadas','stat-label-2':'Socios institucionales','stat-label-3':'Países'}
  };
  /* ---------- TIMELINE DATA ---------- */
  var TL_KIND={
    field:['Field','Campo'],
    tech:['Platform','Plataforma'],
    inst:['Institutional','Institucional'],
    media:['Media','Medios'],
    award:['Recognition','Reconocimiento'],
    research:['Research','Investigación']
  };
  var TL_SOON={en:'Upcoming',es:'Próximamente'};
  var TL=[
    {y:'2023',m:['MAY','MAY'],k:'field',t:['First experimental site, University of Guadalajara','Primer sitio experimental, Universidad de Guadalajara']},
    {y:'2023',m:['AUG','AGO'],k:'field',t:['First studies in forensic entomology, botany, territorial analysis and soil science','Primeros estudios de entomología forense, botánica, análisis territorial y ciencia del suelo']},
    {y:'2024',m:['JAN','ENE'],k:'media',t:['FOUND in Reuters','FOUND en Reuters']},
    {y:'2024',m:['FEB','FEB'],k:'field',t:['First LiDAR at the Forensic Experimentation Sites','Primer LiDAR en los Sitios de Experimentación Forense']},
    {y:'2024',m:['MAR','MAR'],k:'inst',t:['Presented at the British Embassy in Uruguay','Presentación en la Embajada Británica en Uruguay']},
    {y:'2024',m:['MAY','MAY'],k:'inst',t:['Hosted by Ciaran Martin, University of Oxford','Sesión organizada por Ciaran Martin, Universidad de Oxford']},
    {y:'2024',m:['AUG','AGO'],k:'inst',t:['Funding secured from the FCDO’s Frontier Tech Hub','Financiamiento obtenido del Frontier Tech Hub de la FCDO']},
    {y:'2024',m:['NOV','NOV'],k:'research',t:['FOUND in Just Security','FOUND en Just Security']},
    {y:'2024',m:['DEC','DIC'],k:'inst',t:['Keynote at the British Association for Forensic Anthropology','Conferencia magistral en la British Association for Forensic Anthropology']},
    {y:'2024',m:['DEC','DIC'],k:'research',t:['FOUND book, Volume 1, presented at the FIL, Guadalajara','Volumen 1 del libro de FOUND presentado en la FIL, Guadalajara']},
    {y:'2025',m:['MAR','MAR'],k:'field',t:['First electromagnetic conductivity (FDEM) studies: 27 findings','Primeros estudios de conductividad electromagnética (FDEM): 27 hallazgos']},
    {y:'2025',m:['MAR','MAR'],k:'field',t:['First seismic noise studies','Primeros estudios de ruido sísmico']},
    {y:'2025',m:['JUN','JUN'],k:'research',t:['‘Disappearance of Worlds’ exhibition, Oxford — with buscadora Indira Navarro in person','Exposición ‘Disappearance of Worlds’, Oxford — con la buscadora Indira Navarro en persona']},
    {y:'2025',m:['JUL','JUL'],k:'media',t:['FOUND in AP, The Independent, LA Times, VICE and NBC','FOUND en AP, The Independent, LA Times, VICE y NBC']},
    {y:'2025',m:['AUG','AGO'],k:'field',t:['First hyperspectral flight for search purposes','Primer vuelo hiperespectral con fines de búsqueda']},
    {y:'2025',m:['SEP','SEP'],k:'inst',t:['Colombia Search Unit (UBPD) visits the experimental sites','La Unidad de Búsqueda de Colombia (UBPD) visita los sitios experimentales']},
    {y:'2025',m:['NOV','NOV'],k:'media',t:['FOUND in The Guardian','FOUND en The Guardian']},
    {y:'2025',m:['DEC','DIC'],k:'award',t:['Sir Nicholas Browne Award by the FCDO to FOUND’s pioneer','Premio Sir Nicholas Browne de la FCDO a la pionera de FOUND']},
    {y:'2026',m:['FEB','FEB'],k:'tech',t:['Platform integrated with the Colombia Search Unit (UBPD)','Plataforma integrada con la Unidad de Búsqueda de Colombia (UBPD)']},
    {y:'2026',m:['MAR','MAR'],k:'inst',t:['Agreement signed with the Mexico National Search Commission (CNB)','Convenio firmado con la Comisión Nacional de Búsqueda (CNB) de México']},
    {y:'2026',m:['APR','ABR'],k:'tech',t:['Platform integrated with the Mexico National Search Commission (CNB)','Plataforma integrada con la Comisión Nacional de Búsqueda (CNB)']},
    {y:'2026',m:['JUN','JUN'],k:'inst',t:['Public event with identIA, University of Oxford','Evento público con identIA, Universidad de Oxford']},
    {y:'2026',m:['JUN','JUN'],k:'field',t:['Zacatecas: clandestine crematorium located','Zacatecas: crematorio clandestino localizado']},
    {y:'2026',m:['JUL','JUL'],k:'inst',t:['Luis Fondebrider joins as Forensic Advisor','Luis Fondebrider se suma como Asesor Forense']},
    {y:'2026',m:['JUL','JUL'],k:'inst',t:['Indira Navarro and Guillermina Camacho join the Advisory Board','Indira Navarro y Guillermina Camacho se suman al Consejo Asesor']},
    {y:'2026',m:['JUL','JUL'],k:'inst',t:['AI for Good Global Summit, Geneva','Cumbre Global AI for Good, Ginebra']},
    {y:'2026',m:['JUL','JUL'],k:'field',t:['Jalisco: recovery of persons located through machine learning','Jalisco: recuperación de personas localizadas mediante machine learning']},
    {y:'2026',m:['AUG','AGO'],k:'award',t:['Invited to the Routledge Handbook on Forensic Anthropology and Human Rights','Invitación al Routledge Handbook on Forensic Anthropology and Human Rights']},
    {y:'2026',m:['OCT','OCT'],k:'inst',s:1,t:['State trainings in Colima, Zacatecas and Sonora','Capacitaciones estatales en Colima, Zacatecas y Sonora']},
    {y:'2026',m:['DEC','DIC'],k:'research',s:1,t:['FOUND book, Volumes 2 & 3, presented at the FIL','Volúmenes 2 y 3 del libro de FOUND presentados en la FIL']},
    {y:'2027',m:['FEB','FEB'],k:'research',s:1,t:['Worldwide premiere of ‘The Pattern Hunters’, by Storyteller Films for CNA','Estreno mundial de ‘The Pattern Hunters’, de Storyteller Films para CNA']}
  ];
  var TL_LEAF='<svg class="tl-leaf" viewBox="0 0 22 26" aria-hidden="true" focusable="false">'
    +'<g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
    +'<path d="M11 1C3.9 7.4 3.3 17.4 11 25 18.7 17.4 18.1 7.4 11 1Z"/>'
    +'<path d="M11 3.2V23.4"/>'
    +'<path d="M11 9.6 6.6 13.4M11 16 7.1 19.4"/>'
    +'<path d="M11 8.8h3.5V6.2M11 15.4h4.1V12"/>'
    +'</g><g fill="currentColor">'
    +'<circle cx="14.5" cy="5" r="1.5"/><circle cx="15.1" cy="10.8" r="1.5"/>'
    +'</g></svg>';
  var reduceMotion=false;
  try{reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}
  /* ---------- HERO WORD CAROUSEL ---------- */
  var heroWords=[],wordIndex=0,wordInterval=null;
  function buildHeroWords(lang){var dict=translations[lang]||translations.en;heroWords=['word-1','word-2','word-3','word-4','word-5'].map(function(k){return dict[k]}).filter(Boolean);wordIndex=0;var span=document.getElementById('hero-word');if(span&&heroWords.length)span.textContent=heroWords[0]}
  function startWordRotation(){var span=document.getElementById('hero-word');if(wordInterval)clearInterval(wordInterval);if(!span||heroWords.length<2)return;wordInterval=setInterval(function(){span.classList.add('fading-out');setTimeout(function(){wordIndex=(wordIndex+1)%heroWords.length;span.textContent=heroWords[wordIndex];span.classList.remove('fading-out');span.classList.add('fading-in');requestAnimationFrame(function(){requestAnimationFrame(function(){span.classList.remove('fading-in')})})},280)},1800)}
  /* ---------- TIMELINE ---------- */
  var tlVp,tlTrack,tlBar,tlPrev,tlNext,tlObs=null,tlLang='en';
  function tlHorizontal(){return !!tlVp&&(tlVp.scrollWidth-tlVp.clientWidth)>8}
  function tlAccordion(){try{return window.matchMedia&&window.matchMedia('(max-width: 860px)').matches}catch(e){return false}}
  function tlRender(lang){
    tlTrack=document.getElementById('tl-track');tlVp=document.getElementById('tl-viewport');
    if(!tlTrack)return;
    tlLang=lang;
    var i=(lang==='es')?1:0,ratio=0;
    if(tlVp&&tlVp.scrollWidth>tlVp.clientWidth)ratio=tlVp.scrollLeft/(tlVp.scrollWidth-tlVp.clientWidth);
    var openYears={};
    Array.prototype.forEach.call(tlTrack.querySelectorAll('.tl-group.is-open'),function(g){openYears[g.getAttribute('data-year')]=true});
    tlTrack.innerHTML='';
    var counts={};
    TL.forEach(function(it){counts[it.y]=(counts[it.y]||0)+1});
    var lastYear=null,group=null,flip=0;
    TL.forEach(function(it,idx){
      if(it.y!==lastYear){
        var btn=document.createElement('button');
        btn.type='button';btn.className='tl-year';btn.setAttribute('data-year',it.y);
        btn.id='tl-year-'+it.y;
        var pill=document.createElement('span');pill.className='tl-year-pill';
        pill.innerHTML=TL_LEAF+'<span class="tl-year-num"></span><span class="tl-year-count"></span><span class="tl-year-chev" aria-hidden="true"></span>';
        pill.querySelector('.tl-year-num').textContent=it.y;
        pill.querySelector('.tl-year-count').textContent=counts[it.y];
        btn.appendChild(pill);
        tlTrack.appendChild(btn);
        group=document.createElement('div');
        group.className='tl-group'+(openYears[it.y]?' is-open':'');
        group.setAttribute('data-year',it.y);
        group.id='tl-group-'+it.y;
        btn.setAttribute('aria-controls',group.id);
        tlTrack.appendChild(group);
        lastYear=it.y;
      }
      var art=document.createElement('article');
      art.className='tl-item '+((flip%2===0)?'tl-up':'tl-down');
      art.setAttribute('data-year',it.y);
      if(it.s)art.setAttribute('data-soon','1');
      art.setAttribute('tabindex','0');
      if(!reduceMotion)art.style.transitionDelay=Math.min(idx*35,300)+'ms';
      var card=document.createElement('div');card.className='tl-card';
      var meta=document.createElement('div');meta.className='tl-meta';
      var mo=document.createElement('span');mo.className='tl-month';mo.textContent=it.m[i];meta.appendChild(mo);
      var kd=document.createElement('span');kd.className='tl-kind';kd.setAttribute('data-kind',it.k);kd.textContent=(TL_KIND[it.k]||['',''])[i];meta.appendChild(kd);
      if(it.s){var sn=document.createElement('span');sn.className='tl-soon';sn.textContent=TL_SOON[lang]||TL_SOON.en;meta.appendChild(sn)}
      var tx=document.createElement('p');tx.className='tl-text';tx.textContent=it.t[i];
      card.appendChild(meta);card.appendChild(tx);
      var stem=document.createElement('span');stem.className='tl-stem';
      var dot=document.createElement('span');dot.className='tl-dot';
      art.appendChild(card);art.appendChild(stem);art.appendChild(dot);
      group.appendChild(art);flip++;
    });
    Array.prototype.forEach.call(tlTrack.querySelectorAll('.tl-year'),function(btn){
      btn.addEventListener('click',function(){
        if(tlAccordion())tlToggleYear(btn.getAttribute('data-year'));
        else tlGoToYear(btn.getAttribute('data-year'));
      });
    });
    tlApplyMode();
    tlAnimate();
    if(tlVp&&ratio>0){var max=tlVp.scrollWidth-tlVp.clientWidth;if(max>0)tlVp.scrollLeft=ratio*max}
    tlSync();
  }
  function tlApplyMode(){
    if(!tlTrack)return;
    var acc=tlAccordion();
    Array.prototype.forEach.call(tlTrack.querySelectorAll('.tl-year'),function(btn){
      if(acc){
        var g=tlTrack.querySelector('.tl-group[data-year="'+btn.getAttribute('data-year')+'"]');
        btn.setAttribute('aria-expanded',(g&&g.classList.contains('is-open'))?'true':'false');
      }else{
        btn.removeAttribute('aria-expanded');
      }
    });
  }
  function tlToggleYear(year,forceOpen){
    var g=tlTrack.querySelector('.tl-group[data-year="'+year+'"]');
    var btn=tlTrack.querySelector('.tl-year[data-year="'+year+'"]');
    if(!g||!btn)return false;
    var open=forceOpen===true?true:!g.classList.contains('is-open');
    g.classList.toggle('is-open',open);
    btn.setAttribute('aria-expanded',open?'true':'false');
    return open;
  }
  function tlAnimate(){
    if(reduceMotion||!('IntersectionObserver' in window)){tlTrack.classList.remove('tl-anim');return}
    if(tlObs)tlObs.disconnect();
    tlTrack.classList.add('tl-anim');
    tlObs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');tlObs.unobserve(e.target)}})},{threshold:0.18});
    Array.prototype.forEach.call(tlTrack.querySelectorAll('.tl-item'),function(el){tlObs.observe(el)});
  }
  function tlSync(){
    if(!tlVp||!tlTrack)return;
    var max=tlVp.scrollWidth-tlVp.clientWidth;
    if(tlBar)tlBar.style.width=(max>0?(tlVp.scrollLeft/max)*100:0).toFixed(2)+'%';
    if(tlPrev)tlPrev.disabled=tlVp.scrollLeft<=2;
    if(tlNext)tlNext.disabled=max<=0||tlVp.scrollLeft>=max-2;
    var markers=tlTrack.querySelectorAll('.tl-year'),active=null;
    if(tlHorizontal()){
      if(max>0&&tlVp.scrollLeft>=max-4){active=markers[markers.length-1].getAttribute('data-year')}
      else{
        var probe=tlVp.scrollLeft+tlVp.clientWidth*0.3;
        for(var i=0;i<markers.length;i++){if(markers[i].offsetLeft<=probe)active=markers[i].getAttribute('data-year')}
      }
    }else{
      var best=Infinity;
      for(var j=0;j<markers.length;j++){var d=Math.abs(markers[j].getBoundingClientRect().top-120);if(d<best){best=d;active=markers[j].getAttribute('data-year')}}
    }
    if(!active&&markers.length)active=markers[0].getAttribute('data-year');
    Array.prototype.forEach.call(document.querySelectorAll('.tl-chip'),function(c){c.classList.toggle('is-active',c.getAttribute('data-year')===active)});
  }
  function tlGoToYear(year){
    var marker=tlTrack.querySelector('.tl-year[data-year="'+year+'"]');
    if(!marker)return;
    if(tlHorizontal()){
      var left=Math.max(0,marker.offsetLeft-tlVp.clientWidth*0.14);
      if(tlVp.scrollTo)tlVp.scrollTo({left:left,behavior:reduceMotion?'auto':'smooth'});else tlVp.scrollLeft=left;
    }else{
      if(tlAccordion())tlToggleYear(year,true);
      marker.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'center'});
    }
  }
  function tlNudge(dir){
    if(!tlHorizontal())return;
    var step=Math.max(240,tlVp.clientWidth*0.78);
    var left=tlVp.scrollLeft+dir*step;
    if(tlVp.scrollTo)tlVp.scrollTo({left:left,behavior:reduceMotion?'auto':'smooth'});else tlVp.scrollLeft=left;
  }
  function setupTimeline(){
    tlVp=document.getElementById('tl-viewport');tlTrack=document.getElementById('tl-track');
    tlBar=document.getElementById('tl-bar');tlPrev=document.getElementById('tl-prev');tlNext=document.getElementById('tl-next');
    if(!tlVp||!tlTrack)return;
    tlVp.addEventListener('scroll',tlSync,{passive:true});
    window.addEventListener('resize',function(){tlApplyMode();tlSync()});
    window.addEventListener('scroll',function(){if(!tlHorizontal())tlSync()},{passive:true});
    if(tlPrev)tlPrev.addEventListener('click',function(){tlNudge(-1)});
    if(tlNext)tlNext.addEventListener('click',function(){tlNudge(1)});
    Array.prototype.forEach.call(document.querySelectorAll('.tl-chip'),function(chip){
      chip.addEventListener('click',function(){tlGoToYear(chip.getAttribute('data-year'))});
    });
    /* drag to scroll (mouse only; touch keeps native scrolling) */
    var down=false,startX=0,startLeft=0,moved=false;
    tlVp.addEventListener('pointerdown',function(e){
      if(e.pointerType!=='mouse'||e.button!==0||!tlHorizontal())return;
      down=true;moved=false;startX=e.clientX;startLeft=tlVp.scrollLeft;tlVp.classList.add('is-dragging');
    });
    tlVp.addEventListener('pointermove',function(e){
      if(!down)return;
      var dx=e.clientX-startX;
      if(Math.abs(dx)>3)moved=true;
      if(moved){tlVp.scrollLeft=startLeft-dx;e.preventDefault()}
    });
    ['pointerup','pointercancel','pointerleave'].forEach(function(ev){
      tlVp.addEventListener(ev,function(){down=false;tlVp.classList.remove('is-dragging')});
    });
    tlVp.addEventListener('click',function(e){if(moved){e.preventDefault();e.stopPropagation()}},true);
  }
  /* ---------- STAT COUNTERS ---------- */
  function setupCounters(){
    var vals=document.querySelectorAll('.stat-value');
    if(!vals.length)return;
    if(reduceMotion||!('IntersectionObserver' in window))return;
    var obs=new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(!entry.isIntersecting)return;
        var el=entry.target,target=parseInt(el.getAttribute('data-to'),10)||0,start=null,dur=1100;
        obs.unobserve(el);
        function step(ts){
          if(start===null)start=ts;
          var p=Math.min((ts-start)/dur,1);
          el.textContent=Math.round(target*(1-Math.pow(1-p,3)));
          if(p<1)requestAnimationFrame(step);
        }
        el.textContent='0';
        requestAnimationFrame(step);
      });
    },{threshold:0.4});
    Array.prototype.forEach.call(vals,function(el){obs.observe(el)});
  }
  /* ---------- LANGUAGE ---------- */
  function setLanguage(lang){
    var dict=translations[lang]||translations.en;
    Object.keys(dict).forEach(function(id){var el=document.getElementById(id);if(el)el.innerHTML=dict[id]});
    document.documentElement.setAttribute('lang',lang==='es'?'es':'en');
    Array.prototype.forEach.call(document.querySelectorAll('.lang-btn'),function(btn){btn.classList.toggle('active',btn.dataset.lang===lang)});
    try{localStorage.setItem('found-lang',lang)}catch(e){}
    buildHeroWords(lang);startWordRotation();tlRender(lang);
  }
  function setupScrollReveal(){var reveals=document.querySelectorAll('.reveal');if(!reveals.length)return;if('IntersectionObserver' in window){var observer=new IntersectionObserver(function(entries){entries.forEach(function(entry){if(entry.isIntersecting)entry.target.classList.add('is-visible')})},{threshold:0.05,rootMargin:'0px 0px -20px 0px'});Array.prototype.forEach.call(reveals,function(el){observer.observe(el)});document.body.classList.add('reveal-ready')}}
  function setupTouchZoom(){var zoomables=document.querySelectorAll('.touch-zoomable');if(!zoomables.length)return;function toggleZoom(el){if(el.classList.contains('is-expanded')){el.classList.remove('is-expanded');document.body.classList.remove('zoom-active')}else{Array.prototype.forEach.call(document.querySelectorAll('.touch-zoomable.is-expanded'),function(o){o.classList.remove('is-expanded')});el.classList.add('is-expanded');document.body.classList.add('zoom-active')}}Array.prototype.forEach.call(zoomables,function(el){el.addEventListener('click',function(e){if(window.matchMedia&&window.matchMedia('(max-width: 768px)').matches){e.preventDefault();e.stopPropagation();toggleZoom(el)}})});document.addEventListener('keydown',function(e){if(e.key==='Escape'){Array.prototype.forEach.call(document.querySelectorAll('.touch-zoomable.is-expanded'),function(o){o.classList.remove('is-expanded')});document.body.classList.remove('zoom-active')}})}
  function init(){
    var savedLang=null;try{savedLang=localStorage.getItem('found-lang')}catch(e){}
    var initialLang=(savedLang==='es')?'es':'en';
    setupTimeline();
    setLanguage(initialLang);
    Array.prototype.forEach.call(document.querySelectorAll('.lang-btn'),function(btn){btn.addEventListener('click',function(){setLanguage(btn.dataset.lang)})});
    setupTouchZoom();setupScrollReveal();setupCounters();
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init)}else{init()}
})();
{% endraw %}
</script>
