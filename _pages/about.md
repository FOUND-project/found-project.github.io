---
permalink: /
title: "[FOUND] Interpretar la Naturaleza para Encontrar a Quienes nos Faltan"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<style>
  /* Layout wrapper */
  .page {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 1rem;
  }

  @media (max-width: 768px) {
    .page {
      padding: 0 1rem;
    }
  }

  /* Soft nebula-style animated background */
  .found-shell {
    position: relative;
    overflow: hidden;
    border-radius: 24px;
    padding: 2.5rem 1.25rem 3rem;
    background: radial-gradient(circle at 0% 0%, #e5f7f3, #f9fafb 55%);
  }

  .found-shell::before {
    content: "";
    position: absolute;
    inset: -40%;
    background:
      radial-gradient(circle at 20% 20%, rgba(56, 189, 148, 0.22), transparent 55%),
      radial-gradient(circle at 80% 80%, rgba(34, 197, 235, 0.18), transparent 55%),
      radial-gradient(circle at 0% 100%, rgba(59, 130, 246, 0.16), transparent 55%);
    opacity: 0.8;
    filter: blur(8px);
    mix-blend-mode: multiply;
    animation: foundNebula 42s ease-in-out infinite alternate;
  }

  .found-shell-inner {
    position: relative;
    z-index: 1;
  }

  @keyframes foundNebula {
    0% {
      transform: translate3d(0, 0, 0) scale(1);
    }
    50% {
      transform: translate3d(-4%, 3%, 0) scale(1.03);
    }
    100% {
      transform: translate3d(4%, -3%, 0) scale(1.05);
    }
  }

  /* Rolling words line */
  .found-word-wrapper {
    font-size: 1.3rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    height: 1.8rem;
    margin: 1.5rem 0;
  }

  .found-word-window {
    overflow: hidden;
    height: 1.8rem;
    position: relative;
  }

  .found-word-list {
    margin: 0;
    padding: 0;
    list-style: none;
    animation: continuousScroll 8s linear infinite;
  }

  .found-word-item {
    height: 1.8rem;
    line-height: 1.8rem;
  }

  @keyframes continuousScroll {
    0% {
      transform: translateY(0%);
    }
    100% {
      transform: translateY(-50%);
    }
  }

  /* First GIF block */
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
    border-radius: 6px;
    object-fit: cover;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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

  .button-link {
    display: inline-block;
    padding: 10px 20px;
    color: #fff;
    background-color: rgba(0, 128, 0, 0.6);
    border: 2px solid #008000;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 10px;
  }

  .button-link:hover {
    background-color: #008000;
  }

  /* Methods / technology image grid */
  .methods-logo-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }

  .methods-logo {
    max-width: 220px;
    height: auto;
    object-fit: contain;
    background-color: white;
    padding: 10px;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    cursor: pointer;
    transition: transform 0.3s ease;
    position: relative;
    z-index: 1;
  }

  .methods-logo:hover {
    transform: scale(2);
    z-index: 5;
  }

  @media (max-width: 600px) {
    .methods-logo {
      max-width: 140px;
    }
  }

  /* Mothers image block */
  .mothers-logo-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }

  .mothers-logo {
    max-width: 220px;
    height: auto;
    object-fit: contain;
    background-color: white;
    padding: 10px;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    cursor: pointer;
    transition: transform 0.3s ease;
    position: relative;
    z-index: 1;
  }

  .mothers-logo:hover {
    transform: scale(2);
    z-index: 5;
  }

  @media (max-width: 600px) {
    .mothers-logo {
      max-width: 140px;
    }
  }

  /* Partners grid */
  .partner-logo-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }

  .partner-logo {
    max-width: 220px;
    height: auto;
    object-fit: contain;
    background-color: white;
    padding: 10px;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }

  @media (max-width: 600px) {
    .partner-logo {
      max-width: 140px;
    }
  }

  /* Social media highlight cards (2 columns -> 1 on mobile) */
  .social-highlights {
    margin: 2.5rem 0 2rem;
  }

  .social-highlights h2 {
    margin-bottom: 0.75rem;
  }

  .social-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.5rem;
  }

  @media (max-width: 768px) {
    .social-grid {
      grid-template-columns: 1fr;
    }
  }

  .social-card {
    background: rgba(255, 255, 255, 0.96);
    border-radius: 16px;
    padding: 1rem 1.2rem;
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.18);
    min-height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .social-card h3 {
    margin-top: 0;
    margin-bottom: 0.35rem;
    font-size: 1rem;
  }

  .social-card p {
    margin: 0;
    font-size: 0.9rem;
    opacity: 0.85;
  }

  /* FOUND line at the bottom */
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
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  }

  .found-logo-container img:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
  }

  /* Optional click-to-expand behaviour (for any image you give class="clickable-image") */
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
</style>

<div class="found-shell">
  <div class="page found-shell-inner">

    <!-- Rolling words line -->
    <div class="found-word-wrapper">
      <span>Using technology to&nbsp;</span>
      <div class="found-word-window">
        <ul class="found-word-list" id="found-animated-words">
          <li class="found-word-item">dignify.</li>
          <li class="found-word-item">remember.</li>
          <li class="found-word-item">search.</li>
          <li class="found-word-item">bring closure.</li>
          <!-- Repeat for seamless loop -->
          <li class="found-word-item">dignify.</li>
          <li class="found-word-item">remember.</li>
          <li class="found-word-item">search.</li>
          <li class="found-word-item">bring closure.</li>
        </ul>
      </div>
    </div>

    <p>
      Over 120,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
      FOUND combines technology and grassroots knowledge to search, locate and drive systemic change.
    </p>

    <div class="responsive-img-group">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/NDAI5.gif?raw=true"
           alt="360 gif" class="large">
    </div>

    <h2>🌱 Driven by families and research communities</h2>
    <p>
      FOUND is guided and motivated by search collectives and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
    </p>

    <h2>Institutional Collaborations</h2>
    <p>Executive Office of the UN Secretary-General</p>
    <p>UK's Foreign, Commonwealth &amp; Development Office (FCDO)</p>
    <p>Local Search Commissions and Attorney’s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</p>
    <p>⁠Colombian Search Unit</p>
    <p>⁠Mexico’s National Search Commission</p>
    <p>⁠Mexican Science and Technology Secretariat</p>
    <p>⁠British Embassy in Mexico City</p>
    <p>British Association for Forensic Anthropology</p>

    <h2>Technologies in Action</h2>
    <p>Multispectral &amp; Hyperspectral Imaging</p>
    <p>Airborne LiDAR</p>
    <p>Seismic Noise Interferometry (TIRSA)</p>
    <p>Electrical Resistivity Tomography, Conductivimetry Measurements</p>
    <p>Satellite Spectral Analysis</p>
    <p>Forensic Entomology, Botany, Territorial Analysis, Soil Science</p>

    <div class="methods-logo-group">
      <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/360.gif"
           alt="Fieldwork" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/raw/master/images/flowers%20graves.gif"
           alt="Fieldwork" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.03.01.jpeg?raw=true"
           alt="Fieldwork" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47.jpeg?raw=true"
           alt="Search practice" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/2.jpeg?raw=true"
           alt="Search practice" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47%20(3).jpeg?raw=true"
           alt="Search tool" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3.jpeg?raw=true"
           alt="Search practice" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-07-30%20at%2021.40.57.jpeg?raw=true"
           alt="Search practice" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/6.jpg?raw=true"
           alt="Search practice" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/IMG-20231204-WA0038.jpg?raw=true"
           alt="Search practice" class="methods-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/WhatsApp%20Image%202024-12-02%20at%2018.42.17.jpeg?raw=true"
           alt="Search practice" class="methods-logo">
    </div>

    <h2>The Role of Buscadoras</h2>
    <p>
      Women-led collectives are at the heart of FOUND’s work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. FOUND listens, learns, and incorporates their methods into our technological efforts.
    </p>

    <div class="mothers-logo-group">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true"
           alt="Plants and hands" class="mothers-logo">
    </div>

    <h2>Partners</h2>

    <div class="partner-logo-group">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Social-web-v1.jpg?raw=true"
           alt="Frontier Tech Hub" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/1%20logo%20Final%20Guerreros%20Buscadores.png?raw=true"
           alt="Guerreros Buscadores de Jalisco" class="partner-logo">
      <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/2%20logo_centrogeo_wide.svg"
           alt="CentroGeo" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3%20logo%20CBJ.png?raw=true"
           alt="Jalisco Search Commission" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/4%20logo%20oxford-university-logo.png?raw=true"
           alt="University of Oxford" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/images(1).png?raw=true"
           alt="UNAM Institute of Geophysics" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/6%20logo%20Ingenieria%20UNAM.png?raw=true"
           alt="UNAM Faculty of Engineering" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/580141488dfc53bfdbde59fa6b043438.jpg?raw=true"
           alt="University of Guadalajara" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/8%20logo%20UPZMG2.png?raw=true"
           alt="UPZMG" class="partner-logo">
      <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/9%20logo%20UWE%20Bristol.svg"
           alt="University of the West of England" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/11%20logo%20BAFAlogo_orig.png?raw=true"
           alt="British Association for Forensic Anthropology" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/British%20Embassy%20Mexico_Blue%20(ENG).png?raw=true"
           alt="British Embassy" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/OFOTA_COLOUR_WEB.jpg?raw=true"
           alt="OFA" class="partner-logo">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Beth.jpg?raw=true"
           alt="Bath" class="partner-logo">
      <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg"
           alt="Colombia’s Unit for the Search of Disappeared Persons" class="partner-logo">
    </div>

    <!-- NEW: Social media highlights section (Option 2 – styled boxes for your embeds) -->
    <section class="social-highlights">
      <h2>Social Media Highlights</h2>
      <p>
        Selected moments and reflections about FOUND shared on social media.
      </p>
      <div class="social-grid">
        <div class="social-card">
          <h3>Highlight 1</h3>
          <p><em><iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728" height="924" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe></em></p>
        </div>
        <div class="social-card">
          <h3>Highlight 2</h3>
          <p><em>Paste your second embed code here. You can replace this text entirely with the platform’s embed snippet.</em></p>
        </div>
      </div>
    </section>

    <div class="found-logo-container">
      <p><em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan</em></p>
    </div>

  </div>
</div>

<script>
  // Click-to-expand effect for any image with class="clickable-image"
  document.addEventListener('DOMContentLoaded', () => {
    const imgs = document.querySelectorAll('.clickable-image');
    imgs.forEach(img => {
      img.addEventListener('click', () => {
        img.classList.toggle('expanded');
      });
    });
  });
</script>
