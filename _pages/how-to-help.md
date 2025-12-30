---
layout: archive
title: 
permalink: /how-to-help/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200">
  <title>FOUND — How to Help</title>
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

    .help-shell{
      max-width:none;
      width:100%;
      margin:0;
      position:relative;
      padding-left:clamp(10rem,14vw,13rem);
      padding-right:2rem;
    }

    /* Language toggle */
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

    /* HERO */
    .hero-section{
      background:linear-gradient(135deg,#1b4d3e 0%,#2d7a5f 100%);
      color:#fff;
      padding:3.4rem 3rem;
      border-radius:var(--radius-lg);
      text-align:center;
      box-shadow:var(--shadow-lg);
      margin:1.9rem 0 2.8rem;
      position:relative;
      overflow:hidden;
    }

    .hero-section::before{
      content:'';
      position:absolute;
      top:-50%;
      right:-50%;
      width:200%;
      height:200%;
      background:radial-gradient(circle,rgba(255,255,255,.12) 0%,transparent 70%);
      animation:pulse 15s ease-in-out infinite;
    }

    @keyframes pulse{
      0%,100%{transform:scale(1);opacity:.5;}
      50%{transform:scale(1.1);opacity:.8;}
    }

    #hero-title{
      font-size:clamp(2.1rem,3.2vw,2.6rem);
      font-weight:750;
      margin-bottom:1rem;
      letter-spacing:-.03em;
      position:relative;
      z-index:1;
    }

    #hero-text{
      font-size:clamp(1.05rem,1.5vw,1.25rem);
      opacity:.96;
      line-height:1.8;
      max-width:850px;
      margin:0 auto;
      position:relative;
      z-index:1;
    }

    /* IMAGE */
    .image-showcase{
      margin:2.5rem 0 2.8rem;
      text-align:center;
    }

    .image-showcase img{
      width:100%;
      max-width:980px;
      border-radius:18px;
      box-shadow:0 14px 45px rgba(0,0,0,.16);
      transition:transform .4s var(--transition-smooth);
    }

    .image-showcase img:hover{
      transform:scale(1.02);
    }

    /* DONATE SECTION */
    .donate-section{
      background:#ffffff;
      padding:3rem;
      border-radius:var(--radius-lg);
      box-shadow:var(--shadow-md);
      margin-bottom:3rem;
    }

    .section-header{
      display:flex;
      align-items:center;
      gap:1rem;
      margin-bottom:2rem;
      padding-bottom:1rem;
      border-bottom:3px solid var(--dark-green);
    }

    .section-header .icon{
      font-size:2rem;
    }

    #donate-title{
      font-size:2rem;
      color:#1a1a1a;
      font-weight:750;
      letter-spacing:-.02em;
    }

    .organization-card{
      background:linear-gradient(135deg,#ffffff 0%,#f9fafb 100%);
      border-radius:16px;
      padding:2rem;
      border:2px solid rgba(27,77,62,.1);
      margin-bottom:2rem;
      transition:all .3s ease;
    }

    .organization-card:hover{
      border-color:rgba(27,77,62,.3);
      box-shadow:0 8px 32px rgba(0,0,0,.1);
    }

    .org-header{
      display:flex;
      align-items:center;
      gap:1.5rem;
      margin-bottom:1.5rem;
      flex-wrap:wrap;
    }

    .org-logo{
      width:140px;
      height:auto;
      border-radius:12px;
      box-shadow:0 4px 16px rgba(0,0,0,.1);
    }

    .org-info h3{
      font-size:1.5rem;
      color:var(--dark-green);
      font-weight:700;
      margin-bottom:.5rem;
    }

    .facebook-link{
      display:inline-flex;
      align-items:center;
      gap:.5rem;
      padding:.6rem 1.2rem;
      background:#1877f2;
      color:#fff;
      text-decoration:none;
      border-radius:8px;
      font-weight:600;
      font-size:.95rem;
      transition:all .3s ease;
      box-shadow:0 4px 12px rgba(24,119,242,.3);
    }

    .facebook-link:hover{
      background:#166fe5;
      transform:translateY(-2px);
      box-shadow:0 6px 20px rgba(24,119,242,.4);
    }

    .testimonial{
      background:linear-gradient(135deg,#f8f9fa 0%,#e9ecef 100%);
      padding:2rem;
      border-radius:12px;
      border-left:5px solid var(--dark-green);
      font-style:italic;
      color:#333;
      margin:2rem 0;
      line-height:1.8;
      font-size:1.02rem;
      box-shadow:0 4px 16px rgba(0,0,0,.06);
    }

    .testimonial::before{
      content:'"';
      font-size:3rem;
      color:var(--dark-green);
      opacity:.3;
      font-family:Georgia,serif;
      line-height:0;
      margin-right:.5rem;
    }

    .payment-details{
      background:linear-gradient(135deg,#ffffff 0%,#f8f9fa 100%);
      padding:2rem;
      border-radius:12px;
      border:2px solid var(--dark-green);
      box-shadow:0 4px 20px rgba(27,77,62,.1);
    }

    #payment-title{
      color:var(--dark-green);
      font-size:1.3rem;
      margin-bottom:1.5rem;
      font-weight:700;
      display:flex;
      align-items:center;
      gap:.5rem;
    }

    .payment-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
      gap:1.5rem;
    }

    .payment-item{
      background:#ffffff;
      padding:1.2rem;
      border-radius:10px;
      border:1px solid rgba(0,0,0,.06);
      transition:all .3s ease;
    }

    .payment-item:hover{
      border-color:var(--dark-green);
      box-shadow:0 4px 16px rgba(27,77,62,.1);
    }

    .payment-label{
      font-weight:700;
      color:var(--dark-green);
      font-size:.85rem;
      text-transform:uppercase;
      letter-spacing:.05em;
      margin-bottom:.4rem;
    }

    .payment-value{
      color:#1a1a1a;
      font-size:1.02rem;
      font-weight:500;
      word-break:break-word;
    }

    /* COLLABORATE */
    .collaborate-section{
      background:linear-gradient(135deg,#1b4d3e 0%,#2d7a5f 100%);
      color:#ffffff;
      padding:3rem;
      border-radius:var(--radius-lg);
      text-align:center;
      box-shadow:0 12px 40px rgba(27,77,62,.3);
      margin-bottom:1.5rem;
    }

    #collab-title{
      font-size:2rem;
      margin-bottom:1rem;
      font-weight:750;
      letter-spacing:-.02em;
    }

    #collab-text{
      font-size:1.15rem;
      margin-bottom:2rem;
      opacity:.95;
    }

    .linkedin-link{
      display:inline-flex;
      align-items:center;
      gap:.75rem;
      padding:1rem 2rem;
      background:#ffffff;
      color:#0a66c2;
      text-decoration:none;
      border-radius:50px;
      font-weight:700;
      font-size:1.05rem;
      transition:all .3s ease;
      box-shadow:0 8px 24px rgba(255,255,255,.3);
    }

    .linkedin-link:hover{
      transform:translateY(-3px);
      box-shadow:0 12px 32px rgba(255,255,255,.5);
      background:#f8f9fa;
    }

    #linkedin-label{
      display:inline-block;
    }

    @media (max-width:900px){
      body{
        padding:1.4rem 1rem;
      }
      .help-shell{
        padding-left:0;
        padding-right:0;
      }
      .lang-toggle{
        position:static;
        margin-left:auto;
        margin-bottom:.4rem;
      }
      .hero-section,
      .donate-section,
      .collaborate-section{
        padding:2rem 1.6rem;
      }
      #hero-title{
        font-size:1.9rem;
      }
      #hero-text{
        font-size:1.05rem;
      }
    }

    @media (max-width:600px){
      .org-header{
        flex-direction:column;
        align-items:flex-start;
      }
      .payment-grid{
        grid-template-columns:1fr;
      }
    }
  </style>
</head>
<body>
  <div class="help-shell">
    <!-- Language toggle -->
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
      <button type="button" class="lang-btn" data-lang="nah">NÁHUATL</button>
    </div>

    <!-- Hero Section -->
    <section class="hero-section">
      <h1 id="hero-title">Support These Mothers</h1>
      <p id="hero-text">
        You can support these mothers directly — every contribution makes a difference in their search for missing loved ones.
      </p>
    </section>

    <!-- Image Showcase -->
    <section class="image-showcase">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/mothers%20walking.gif?raw=true"
           alt="Mothers searching for their missing loved ones">
    </section>

    <!-- Donate Section -->
    <section class="donate-section">
      <div class="section-header">
        <span class="icon">💳</span>
        <h2 id="donate-title">Donate</h2>
      </div>

      <article class="organization-card">
        <div class="org-header">
          <img class="org-logo" src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Final%20Guerreros%20Buscadores.png?raw=true" alt="Guerreros Buscadores de Jalisco">
          <div class="org-info">
            <h3>Guerreros Buscadores de Jalisco</h3>
            <a class="facebook-link" href="https://www.facebook.com/profile.php?id=61555458753120" target="_blank" rel="noopener">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
              <span id="facebook-label">Visit Facebook Page</span>
            </a>
          </div>
        </div>

        <div class="testimonial" id="testimonial-text">
          These are the details to donate — your support allows us to continue our searches. Thank you for your empathy — it is through your support that we can carry on looking for our missing loved ones. Until we find them!
        </div>

        <div class="payment-details">
          <h4 id="payment-title">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <rect x="1" y="4" width="22" height="16" rx="2" ry="2"/>
              <line x1="1" y1="10" x2="23" y2="10"/>
            </svg>
            Payment Information
          </h4>

          <div class="payment-grid">
            <div class="payment-item">
              <div class="payment-label" id="label-paypal">PayPal</div>
              <div class="payment-value">guerrerosbuscadoresdejalisco@gmail.com</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-holder">Account Holder</div>
              <div class="payment-value">Indira Navarro</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-country">Country</div>
              <div class="payment-value">Mexico</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-bank">Bank</div>
              <div class="payment-value">BBVA</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-card">Card Details</div>
              <div class="payment-value">4152 3142 5358 9934</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-account">Account Number</div>
              <div class="payment-value">1502613941</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-clabe">CLABE</div>
              <div class="payment-value">012320015026139414</div>
            </div>

            <div class="payment-item">
              <div class="payment-label" id="label-swift">SWIFT</div>
              <div class="payment-value">BCMRMXMMPYM</div>
            </div>
          </div>
        </div>
      </article>
    </section>

    <!-- Collaborate Section -->
    <section class="collaborate-section">
      <h2 id="collab-title">How to Collaborate & Amplify</h2>
      <p id="collab-text">Join us in raising awareness and supporting this critical mission.</p>
      <a class="linkedin-link" href="https://www.linkedin.com/company/found-project" target="_blank" rel="noopener">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
        </svg>
        <span id="linkedin-label">Follow on LinkedIn</span>
      </a>
    </section>
  </div>

  <!-- LANGUAGE SCRIPT -->
  <script>
    (function(){
      const translations = {
        en:{
          'hero-title':'Support These Mothers',
          'hero-text':'You can support these mothers directly — every contribution makes a difference in their search for missing loved ones.',
          'donate-title':'Donate',
          'facebook-label':'Visit Facebook Page',
          'testimonial-text':'These are the details to donate — your support allows us to continue our searches. Thank you for your empathy — it is through your support that we can carry on looking for our missing loved ones. Until we find them!',
          'payment-title':'Payment Information',
          'label-paypal':'PayPal',
          'label-holder':'Account Holder',
          'label-country':'Country',
          'label-bank':'Bank',
          'label-card':'Card Details',
          'label-account':'Account Number',
          'label-clabe':'CLABE',
          'label-swift':'SWIFT',
          'collab-title':'How to Collaborate & Amplify',
          'collab-text':'Join us in raising awareness and supporting this critical mission.',
          'linkedin-label':'Follow on LinkedIn'
        },
        es:{
          'hero-title':'Apoya a Estas Madres',
          'hero-text':'Puedes apoyar directamente a estas madres — cada contribución marca una diferencia en la búsqueda de sus seres queridos desaparecidos.',
          'donate-title':'Donar',
          'facebook-label':'Visitar página de Facebook',
          'testimonial-text':'Estos son los datos para donar — tu apoyo nos permite seguir buscando. Gracias por tu empatía: es gracias a tu apoyo que podemos continuar la búsqueda de nuestros seres queridos. ¡Hasta encontrarles!',
          'payment-title':'Información de pago',
          'label-paypal':'PayPal',
          'label-holder':'Titular de la cuenta',
          'label-country':'País',
          'label-bank':'Banco',
          'label-card':'Datos de tarjeta',
          'label-account':'Número de cuenta',
          'label-clabe':'CLABE',
          'label-swift':'SWIFT',
          'collab-title':'Cómo Colaborar y Amplificar',
          'collab-text':'Súmate a visibilizar y apoyar esta misión fundamental.',
          'linkedin-label':'Seguir en LinkedIn'
        },
        nah:{
          'hero-title':'Tlen tikpalehuise ininon nanmeh',
          'hero-text':'Tikonpalehui ninnananmeh direkte — nochi tlen tiktoktia kipalehui in tlatemoliztli de ininteixpoyohwan tlapolpoliwkeh.',
          'donate-title':'Titetlanejma',
          'facebook-label':'Tlachiyaliztli ipan Facebook',
          'testimonial-text':'Ini nin datos para titetlanejma — motlapalehuilis techmaka chicahualistli para oksejpa titetlatemoliseh. Tlazohcamati por moempatía; ika motlapalehuilis weli tikmoyetztia in tlatemoliztli de ininteixpoyohwan. ¡Hasta tikinmatiskeh!',
          'payment-title':'Tlatlajko tlen tlapalehuilistli (pago)',
          'label-paypal':'PayPal',
          'label-holder':'Tlen motoka ipan cuenta',
          'label-country':'País',
          'label-bank':'Banco',
          'label-card':'Datos de tarjeta',
          'label-account':'Número de cuenta',
          'label-clabe':'CLABE',
          'label-swift':'SWIFT',
          'collab-title':'Kenin Tikonpalehuis huan Tikonmachtis',
          'collab-text':'Ximoyekona techpalehuikan para se okachi motematiltis nin importante tlamantli.',
          'linkedin-label':'Tikneki tiksewis ipan LinkedIn'
        }
      };

      function setLanguage(lang){
        const dict = translations[lang] || translations.en;

        Object.keys(dict).forEach(id=>{
          const el = document.getElementById(id);
          if(el) el.innerHTML = dict[id];
        });

        document.documentElement.setAttribute(
          'lang',
          lang === 'es' ? 'es' : (lang === 'nah' ? 'nah' : 'en')
        );

        document.querySelectorAll('.lang-btn').forEach(btn=>{
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });

        try{
          localStorage.setItem('found-lang-help', lang);
        }catch(e){}
      }

      document.addEventListener('DOMContentLoaded', function(){
        let savedLang = null;
        try{
          savedLang = localStorage.getItem('found-lang-help');
        }catch(e){}
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
