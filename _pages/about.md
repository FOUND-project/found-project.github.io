---
permalink: /
title: "[FOUND] Interpretar la Naturaleza para Encontrar a Quienes nos Faltan"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<!-- FOUND Landing Styling -->
<style>
  :root {
    --found-bg-deep: #020816;
    --found-bg-soft: #061520;
    --found-card-bg: rgba(255, 255, 255, 0.96);
    --found-accent: #0b5c3b;
    --found-accent-soft: rgba(11, 92, 59, 0.12);
    --found-accent-strong: #0c7a4d;
    --found-text-main: #111827;
    --found-text-muted: #4b5563;
    --found-border-subtle: rgba(15, 23, 42, 0.12);
    --found-radius-lg: 18px;
    --found-radius-xl: 22px;
    --found-shadow-soft: 0 22px 60px rgba(15, 23, 42, 0.24);
    --found-shadow-subtle: 0 12px 35px rgba(15, 23, 42, 0.18);
    --found-transition: 220ms ease-out;
  }

  /* Animated, respectful background */
  .found-landing-bg {
    position: relative;
    padding: 3.5rem 1rem 4rem;
    z-index: 0;
    overflow: hidden;
  }

  .found-landing-bg::before,
  .found-landing-bg::after {
    content: "";
    position: fixed;
    inset: -20%;
    z-index: -2;
    background:
      radial-gradient(circle at 10% 20%, rgba(88, 214, 141, 0.18) 0, transparent 45%),
      radial-gradient(circle at 90% 10%, rgba(16, 185, 129, 0.2) 0, transparent 50%),
      radial-gradient(circle at 80% 80%, rgba(56, 189, 248, 0.18) 0, transparent 50%),
      linear-gradient(135deg, var(--found-bg-deep), var(--found-bg-soft));
    animation: foundBgDrift 55s ease-in-out infinite alternate;
    opacity: 0.85;
  }

  .found-landing-bg::after {
    filter: blur(20px);
    opacity: 0.55;
    animation-duration: 75s;
    animation-direction: alternate-reverse;
  }

  @keyframes foundBgDrift {
    0% {
      transform: translate3d(0, 0, 0) scale(1);
    }
    50% {
      transform: translate3d(-10px, 18px, 0) scale(1.02);
    }
    100% {
      transform: translate3d(10px, -12px, 0) scale(1.03);
    }
  }

  /* Main card container */
  .found-landing.page {
    max-width: 1100px !important;
    margin: 0 auto;
    padding: 2.5rem clamp(1.5rem, 3vw, 3rem);
    background: radial-gradient(circle at top left, rgba(11, 92, 59, 0.06), transparent 55%),
                radial-gradient(circle at bottom right, rgba(56, 189, 248, 0.07), transparent 55%),
                var(--found-card-bg);
    border-radius: var(--found-radius-xl);
    box-shadow: var(--found-shadow-soft);
    border: 1px solid var(--found-border-subtle);
    backdrop-filter: blur(18px);
    color: var(--found-text-main);
    position: relative;
  }

  .found-landing.page::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    border: 1px solid rgba(255, 255, 255, 0.35);
    pointer-events: none;
    mix-blend-mode: soft-light;
  }

  /* Global typography tweaks inside card */
  .found-landing.page h1,
  .found-landing.page h2,
  .found-landing.page h3 {
    color: var(--found-text-main);
    letter-spacing: 0.02em;
  }

  .found-landing.page h2 {
    margin-top: 2.5rem;
    margin-bottom: 1rem;
    font-size: 1.45rem;
    position: relative;
  }

  .found-landing.page h2::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -0.35rem;
    width: 3.25rem;
    height: 2px;
    background: linear-gradient(90deg, var(--found-accent), transparent);
    opacity: 0.8;
  }

  .found-landing.page p {
    font-size: 1.02rem;
    line-height: 1.7;
    color: var(--found-text-muted);
  }

  .found-landing.page ul {
    padding-left: 1.1rem;
    margin-top: 0.4rem;
    margin-bottom: 0.8rem;
  }

  .found-landing.page li {
    margin-bottom: 0.2rem;
    color: var(--found-text-muted);
  }

  /* Section layout + fade-in on scroll */
  .found-section {
    position: relative;
    margin-bottom: 2.4rem;
    padding: 1.6rem 1.4rem;
    border-radius: var(--found-radius-lg);
    background: linear-gradient(120deg, rgba(15, 23, 42, 0.02), rgba(15, 23, 42, 0));
    border: 1px solid rgba(15, 23, 42, 0.03);
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
    overflow: hidden;
    opacity: 0;
    transform: translateY(12px);
    transition:
      opacity 520ms ease-out,
      transform 520ms ease-out,
      box-shadow var(--found-transition),
      border-color var(--found-transition),
      background var(--found-transition);
  }

  .found-section::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top left, rgba(11, 92, 59, 0.12), transparent 55%);
    opacity: 0;
    transition: opacity 400ms ease-out;
    pointer-events: none;
  }

  .found-section.is-visible {
    opacity: 1;
    transform: translateY(0);
  }

  .found-section:hover {
    box-shadow: var(--found-shadow-subtle);
    border-color: rgba(11, 92, 59, 0.2);
    background: linear-gradient(120deg, rgba(11, 92, 59, 0.05), rgba(15, 23, 42, 0.02));
  }

  .found-section:hover::before {
    opacity: 0.4;
  }

  /* Hero section */
  .found-hero {
    display: grid;
    grid-template-columns: minmax(0, 3fr) minmax(0, 2.1fr);
    gap: 2rem;
    align-items: center;
    padding: 2rem 2rem 2.2rem;
    background: radial-gradient(circle at top right, rgba(56, 189, 248, 0.12), transparent 55%),
                radial-gradient(circle at bottom left, rgba(11, 92, 59, 0.16), transparent 60%),
                rgba(255, 255, 255, 0.96);
  }

  .found-hero-text {
    position: relative;
    z-index: 2;
  }

  .found-hero-text p:first-of-type {
    font-size: 1.08rem;
  }

  .found-hero-gif {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .found-hero-gif img {
    max-width: 100%;
    border-radius: 18px;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.8);
    transform-origin: center;
    transition:
      transform 460ms ease-out,
      box-shadow 460ms ease-out,
      filter 460ms ease-out;
    filter: saturate(1.08) contrast(1.02);
  }

  .found-hero-gif img:hover {
    transform: translateY(-4px) scale(1.015);
    box-shadow: 0 24px 60px rgba(15, 23, 42, 0.5);
    filter: saturate(1.15) contrast(1.05);
  }

  @media (max-width: 840px) {
    .found-hero {
      grid-template-columns: minmax(0, 1fr);
      padding: 1.6rem 1.4rem 1.9rem;
    }
  }

  /* Rolling words strapline */
  .found-hero-strap {
    font-size: 1.3rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    height: 1.8rem;
    margin: 1.5rem 0 1.2rem;
    gap: 0.15rem;
    color: var(--found-text-main);
  }

  .found-hero-strap span {
    white-space: nowrap;
  }

  .found-hero-roller {
    overflow: hidden;
    height: 1.8rem;
    position: relative;
    padding-left: 0.1rem;
    min-width: 8.5rem;
  }

  .found-hero-roller::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(to right, transparent 0%, rgba(15, 23, 42, 0.02) 40%, rgba(15, 23, 42, 0.06) 100%);
    pointer-events: none;
  }

  #found-animated-words {
    margin: 0;
    padding: 0;
    list-style: none;
    animation: continuousScroll 8s linear infinite;
  }

  #found-animated-words li {
    height: 1.8rem;
    line-height: 1.8rem;
    color: var(--found-accent-strong);
  }

  @keyframes continuousScroll {
    0% {
      transform: translateY(0%);
    }
    100% {
      transform: translateY(-50%);
    }
  }

  /* Original page width helper preserved */
  .page {
    max-width: 1000px !important;
    margin: 0 auto;
    padding: 0 1rem;
  }

  @media (max-width: 768px) {
    .page {
      padding: 0 1rem;
    }
  }

  /* Responsive image groups (existing, slightly refined) */
  .responsive-img-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    margin: 1.5rem 0;
  }

  .responsive-img-group img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    object-fit: cover;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.85);
    transform-origin: center;
    transition:
      transform 380ms ease-out,
      box-shadow 380ms ease-out,
      filter 380ms ease-out;
  }

  .responsive-img-group img:hover {
    transform: translateY(-4px) scale(1.015);
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.6);
    filter: saturate(1.12);
  }

  @media (min-width: 600px) {
    .responsive-img-group img.small {
      width: 200px;
      height: 280px;
    }
    .responsive-img-group img.medium {
      width: 260px;
      height: 180px;
    }
    .responsive-img-group img.large {
      width: 350px;
    }
    .responsive-img-group img.xlarge {
      width: 500px;
    }
  }

  /* Button style (if used elsewhere) */
  .button-link {
    display: inline-block;
    padding: 10px 20px;
    color: #fff;
    background-color: rgba(0, 128, 0, 0.6);
    border: 2px solid #008000;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 600;
    margin-top: 10px;
    letter-spacing: 0.02em;
    box-shadow: 0 10px 25px rgba(0, 128, 0, 0.35);
    transition:
      background-color var(--found-transition),
      box-shadow var(--found-transition),
      transform var(--found-transition);
  }

  .button-link:hover {
    background-color: #008000;
    transform: translateY(-1px);
    box-shadow: 0 14px 32px rgba(0, 128, 0, 0.45);
  }

  /* Methods, mothers, partners logo grids – refined but same structure */
  .methods-logo-group,
  .mothers-logo-group,
  .partner-logo-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }

  .methods-logo,
  .mothers-logo,
  .partner-logo {
    max-width: 220px;
    height: auto;
    object-fit: contain;
    background-color: white;
    padding: 10px;
    border-radius: 12px;
    box-shadow: 0 14px 32px rgba(15, 23, 42, 0.2);
    cursor: pointer;
    transition:
      transform 280ms ease-out,
      box-shadow 280ms ease-out,
      filter 280ms ease-out;
    position: relative;
    z-index: 1;
    border: 1px solid rgba(148, 163, 184, 0.4);
  }

  .methods-logo:hover,
  .mothers-logo:hover,
  .partner-logo:hover {
    transform: translateY(-3px) scale(1.05);
    z-index: 5;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.55);
    filter: saturate(1.08);
  }

  @media (max-width: 600px) {
    .methods-logo,
    .mothers-logo,
    .partner-logo {
      max-width: 150px;
    }
  }

  /* FOUND tagline at bottom */
  .found-logo-container {
    text-align: center;
    margin-top: 2rem;
    margin-bottom: 3rem;
  }

  .found-logo-container p {
    font-style: italic;
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: #1b4d3e;
  }

  .found-logo-container img {
    max-width: 500px;
    width: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-radius: 12px;
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.35);
  }

  .found-logo-container img:hover {
    transform: scale(1.03);
    box-shadow: 0 18px 50px rgba(15, 23, 42, 0.55);
  }

  /* Clickable image expansion (existing behaviour preserved) */
  .clickable-image {
    cursor: pointer;
    transition: transform 0.3s ease;
  }

  .clickable-image.expanded {
    position: fixed;
    top: 10%;
    left: 5%;
    width: 90vw;
    height: auto;
    z-index: 1000;
    transform: scale(1.05);
    background-color: white;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  }

  @media (max-width: 640px) {
    .found-landing-bg {
      padding-top: 2.4rem;
      padding-bottom: 3rem;
    }
    .found-landing.page {
      padding: 1.8rem 1.3rem 2.2rem;
      border-radius: 20px;
    }
    .found-section {
      padding: 1.2rem 1rem;
      margin-bottom: 2rem;
    }
  }
</style>

<div class="found-landing-bg">
  <div class="found-landing page">

    <!-- HERO -->
    <section class="found-section found-hero">
      <div class="found-hero-text">
        <div class="found-hero-strap">
          <span>Using technology to&nbsp;</span>
          <div class="found-hero-roller">
            <ul id="found-animated-words">
              <li>dignify.</li>
              <li>remember.</li>
              <li>search.</li>
              <li>bring closure.</li>
              <!-- Repeat for seamless loop -->
              <li>dignify.</li>
              <li>remember.</li>
              <li>search.</li>
              <li>bring closure.</li>
            </ul>
          </div>
        </div>

        Over 120,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
        **FOUND** combines technology and grassroots knowledge to search, locate and drive systemic change.
      </div>

      <div class="found-hero-gif">
        <div class="responsive-img-group">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/NDAI5.gif?raw=true" alt="360 gif" class="large">
        </div>
      </div>
    </section>

    <!-- Driven by families -->
    <section class="found-section">
      <h2>🌱 Driven by families and research communities</h2>

      FOUND is guided and motivated by **search collectives** and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
    </section>

    <!-- Institutional Collaborations -->
    <section class="found-section">
      <h2>Institutional Collaborations</h2>

      - Executive Office of the UN Secretary-General  
      - UK's Foreign, Commonwealth & Development Office (FCDO)  
      - Local Search Commissions and Attorney’s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)  
      - ⁠Colombian Search Unit  
      - ⁠Mexico’s National Search Commission  
      - ⁠Mexican Science and Technology Secretariat  
      - ⁠British Embassy in Mexico City  
      - British Association for Forensic Anthropology
    </section>

    <!-- Technologies in Action -->
    <section class="found-section">
      <h2>Technologies in Action</h2>

      - Multispectral & Hyperspectral Imaging  
      - Airborne LiDAR  
      - Seismic Noise Interferometry (TIRSA)  
      - Electrical Resistivity Tomography, Conductivimetry Measurements  
      - Satellite Spectral Analysis  
      - Forensic Entomology, Botany, Territorial Analysis, Soil Science

      <div class="methods-logo-group">
        <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/360.gif" alt="Fieldwork" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/flowers%20graves.gif" alt="Fieldwork" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.03.01.jpeg?raw=true" alt="Fieldwork" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47.jpeg?raw=true" alt="Search practice" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/2.jpeg?raw=true" alt="Search practice" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true" alt="Search tool" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3.jpeg?raw=true" alt="Search practice" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-07-30%20at%2021.40.57.jpeg?raw=true" alt="Search practice" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/6.jpg?raw=true" alt="Search practice" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/IMG-20231204-WA0038.jpg?raw=true" alt="Search practice" class="methods-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-12-02%20at%2018.42.17.jpeg?raw=true" alt="Search practice" class="methods-logo">
      </div>
    </section>

    <!-- Buscadoras -->
    <section class="found-section">
      <h2>The Role of Buscadoras</h2>
      Women-led collectives are at the heart of FOUND’s work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. FOUND listens, learns, and incorporates their methods into our technological efforts.

      <div class="mothers-logo-group">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Plants and hands" class="mothers-logo">
      </div>
    </section>

    <!-- Partners -->
    <section class="found-section">
      ## Partners

      <div class="partner-logo-group">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Social-web-v1.jpg?raw=true" alt="Frontier Tech Hub" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/1%20logo%20Final%20Guerreros%20Buscadores.png?raw=true" alt="Guerreros Buscadores de Jalisco" class="partner-logo">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/2%20logo_centrogeo_wide.svg" alt="CentroGeo" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3%20logo%20CBJ.png?raw=true" alt="Jalisco Search Commission" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/4%20logo%20oxford-university-logo.png?raw=true" alt="University of Oxford" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/images(1).png?raw=true" alt="UNAM Institute of Geophysics" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/6%20logo%20Ingenieria%20UNAM.png?raw=true" alt="UNAM Faculty of Engineering" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/580141488dfc53bfdbde59fa6b043438.jpg?raw=true" alt="University of Guadalajara" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/8%20logo%20UPZMG2.png?raw=true" alt="UPZMG" class="partner-logo">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/9%20logo%20UWE%20Bristol.svg" alt="University of the West of England" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/11%20logo%20BAFAlogo_orig.png?raw=true" alt="British Association for Forensic Anthropology" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/British%20Embassy%20Mexico_Blue%20(ENG).png?raw=true" alt="British Embassy" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/OFOTA_COLOUR_WEB.jpg?raw=true" alt="OFA" class="partner-logo">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Beth.jpg?raw=true" alt="Bath" class="partner-logo">
        <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg" alt="Colombia’s Unit for the Search of Disappeared Persons" class="partner-logo">
      </div>
    </section>

    ---

    <div class="found-logo-container">
      <p><em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan</em></p>
    </div>

  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Existing clickable image behaviour
    const imgs = document.querySelectorAll('.clickable-image');
    imgs.forEach(img => {
      img.addEventListener('click', () => {
        img.classList.toggle('expanded');
      });
    });

    // Fade-in on scroll for sections
    const sections = document.querySelectorAll('.found-section');
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.15
      }
    );

    sections.forEach(section => observer.observe(section));
  });
</script>
