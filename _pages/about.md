---
permalink: /
title: "[FOUND] Interpretar la Naturaleza para Encontrar a Quienes nos Faltan"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FOUND Project - Using Technology to Search and Remember</title>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    :root {
      --primary-green: #2d5f4d;
      --light-green: #4a8c73;
      --accent-green: rgba(0, 128, 0, 0.1);
      --text-dark: #1a1a1a;
      --text-light: #666;
      --bg-light: #f8f9fa;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', sans-serif;
      color: var(--text-dark);
      line-height: 1.7;
      background: #fff;
    }

    .page {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 2rem;
    }

    /* Hero */
    .hero {
      padding: 4rem 0 3rem;
      border-bottom: 1px solid #e0e0e0;
    }

    .animated-tagline {
      font-size: clamp(1.5rem, 3vw, 2rem);
      font-weight: 600;
      display: flex;
      align-items: center;
      margin-bottom: 2rem;
      color: var(--primary-green);
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .word-carousel {
      overflow: hidden;
      height: 2.5rem;
      position: relative;
      display: inline-block;
      min-width: 180px;
    }

    .word-list {
      list-style: none;
      animation: continuousScroll 10s linear infinite;
    }

    .word-list li {
      height: 2.5rem;
      line-height: 2.5rem;
      color: var(--light-green);
      font-weight: 700;
    }

    @keyframes continuousScroll {
      0% { transform: translateY(0%); }
      100% { transform: translateY(-50%); }
    }

    .hero-description {
      font-size: 1.15rem;
      color: var(--text-light);
      max-width: 800px;
      margin-bottom: 2rem;
      line-height: 1.8;
    }

    .hero-image {
      width: 100%;
      max-width: 600px;
      margin: 2rem auto;
      display: block;
      border-radius: 12px;
      box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }

    /* FOLLOW OUR JOURNEY — CAROUSEL */
    .social-section {
      background: linear-gradient(135deg, var(--accent-green) 0%, rgba(74, 140, 115, 0.05) 100%);
      padding: 2rem 0;
      margin: 1.5rem 0;
      border-radius: 16px;
    }

    .section-title {
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      color: var(--primary-green);
      margin-bottom: 1rem;
      text-align: center;
    }

    .section-subtitle {
      font-size: 1.1rem;
      color: var(--text-light);
      text-align: center;
      margin-bottom: 1.5rem;
      max-width: 700px;
      margin-left: auto;
      margin-right: auto;
    }

    .social-carousel {
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .carousel-window {
      overflow: hidden;
      flex: 1;
    }

    .carousel-track {
      display: flex;
      transition: transform 0.5s ease;
      will-change: transform;
    }

    .social-embed {
      background: white;
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      min-height: 400px;
      min-width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-sizing: border-box;
    }

    .carousel-btn {
      background: #ffffff;
      border-radius: 999px;
      border: 1px solid rgba(0,0,0,0.1);
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 2px 8px rgba(0,0,0,0.12);
      transition: 0.2s ease;
      color: var(--primary-green);
      font-size: 1.4rem;
      flex-shrink: 0;
    }

    .carousel-btn:hover {
      background: rgba(74, 140, 115, 0.06);
      transform: translateY(-2px);
    }

    .carousel-dots {
      margin-top: 1.2rem;
      text-align: center;
    }

    .carousel-dots .dot {
      width: 10px;
      height: 10px;
      border-radius: 999px;
      border: none;
      margin: 0 4px;
      background: rgba(0,0,0,0.18);
      cursor: pointer;
      transition: 0.2s ease;
    }

    .carousel-dots .dot.active {
      background: var(--primary-green);
      width: 16px;
      transform: scale(1.15);
    }


    /* Content Sections */
    .content-section {
      padding: 2rem 0;
      border-bottom: 1px solid #e8e8e8;
    }

    .content-section:last-of-type {
      border-bottom: none;
    }

    h2 {
      font-size: clamp(1.6rem, 3vw, 2rem);
      font-weight: 700;
      color: var(--primary-green);
      margin-bottom: 1.5rem;
    }

    .info-list {
      list-style: none;
      padding-left: 0;
    }

    .info-list li {
      padding: 0.5rem 0 0.5rem 2rem;
      position: relative;
      color: var(--text-light);
    }

    .info-list li:before {
      content: "✓";
      position: absolute;
      left: 0;
      color: var(--light-green);
      font-weight: bold;
      font-size: 1.2rem;
    }

    /* Gallery */
    .image-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1.5rem;
      margin: 2rem 0;
    }

    .gallery-item {
      overflow: hidden;
      border-radius: 10px;
      background: white;
      padding: 12px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .gallery-item img {
      width: 100%;
      border-radius: 6px;
    }

    /* Partners */
    .partner-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 2rem;
      margin: 2.5rem 0;
    }

    .partner-logo {
      background: white;
      padding: 1.5rem;
      border-radius: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    }

    /* Footer */
    .footer {
      text-align: center;
      padding: 3rem 0;
      margin-top: 3rem;
      border-top: 1px solid #e0e0e0;
    }

  </style>
</head>

<body>
<div class="page">

  <!-- HERO -->
  <section class="hero">
    <div class="animated-tagline">
      <span>Using technology to&nbsp;</span>
      <div class="word-carousel">
        <ul class="word-list">
          <li>dignify.</li>
          <li>remember.</li>
          <li>search.</li>
          <li>bring closure.</li>
          <li>dignify.</li>
          <li>remember.</li>
          <li>search.</li>
          <li>bring closure.</li>
        </ul>
      </div>
    </div>

    <p class="hero-description">
      Over 120,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
      <strong>FOUND</strong> combines technology and grassroots knowledge to search, locate and drive systemic change.
    </p>

    <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/NDAI5.gif?raw=true"
         class="hero-image" alt="FOUND Project in Action">
  </section>


  <!-- FOLLOW OUR JOURNEY CAROUSEL -->
  <section class="social-section">
    <h2 class="section-title">Follow Our Journey</h2>
    <p class="section-subtitle">Stay connected with our latest findings, community stories, and collaborative efforts</p>

    <div class="social-carousel">
      <button class="carousel-btn prev">&#10094;</button>

      <div class="carousel-window">
        <div class="carousel-track">

          <!-- Slide 1: Twitter -->
          <div class="social-embed">
            <blockquote class="twitter-tweet">
              <p lang="en">
                Almost a year after I started researching the story, I'm thrilled that my
                @guardian article about the innovations used to find disappeared persons in Mexico is now trending.
              </p>
              — Suzanne Bearne (@sbearne)
              <a href="https://twitter.com/sbearne/status/1991827389375193330">
                November 21, 2025
              </a>
            </blockquote>
            <script async src="https://platform.twitter.com/widgets.js"></script>
          </div>

          <!-- Slide 2: LinkedIn -->
          <div class="social-embed">
            <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728"
                    height="924" width="504" frameborder="0"
                    allowfullscreen="" title="Embedded LinkedIn Post"
                    style="max-width: 100%;">
            </iframe>
          </div>

          <!-- Slide 3 -->
          <div class="social-embed">
            <div>
              <h3>Coming soon…</h3>
              <p>More FOUND updates and embeds will appear here.</p>
            </div>
          </div>

          <!-- Slide 4 -->
          <div class="social-embed">
            <div>
              <h3>Media Highlights</h3>
              <p>Documentaries, interviews, and news coverage.</p>
            </div>
          </div>

          <!-- Slide 5 -->
          <div class="social-embed">
            <div>
              <h3>Community Stories</h3>
              <p>Stories from buscadoras, partners, and communities.</p>
            </div>
          </div>

        </div>
      </div>

      <button class="carousel-btn next">&#10095;</button>
    </div>

    <div class="carousel-dots">
      <button class="dot active" data-slide="0"></button>
      <button class="dot" data-slide="1"></button>
      <button class="dot" data-slide="2"></button>
      <button class="dot" data-slide="3"></button>
      <button class="dot" data-slide="4"></button>
    </div>

  </section>


  <!-- COMMUNITY SECTION -->
  <section class="content-section">
    <h2>🌱 Driven by families and research communities</h2>
    <p class="hero-description">
      FOUND is guided and motivated by <strong>search collectives</strong> and researchers from leading universities and institutions.
    </p>
  </section>


  <!-- INSTITUTIONAL COLLABORATIONS -->
  <section class="content-section">
    <h2>Institutional Collaborations</h2>
    <ul class="info-list">
      <li>Executive Office of the UN Secretary-General</li>
      <li>FCDO (United Kingdom)</li>
      <li>Local Search Commissions</li>
      <li>Colombian Search Unit</li>
      <li>National Search Commission of Mexico</li>
    </ul>
  </section>


  <!-- TECHNOLOGIES -->
  <section class="content-section">
    <h2>Technologies in Action</h2>
    <ul class="info-list">
      <li>Multispectral & Hyperspectral Imaging</li>
      <li>LiDAR</li>
      <li>Seismic Noise Interferometry</li>
      <li>Electrical Resistivity</li>
      <li>Satellite Analysis</li>
    </ul>
  </section>


  <!-- FOOTER -->
  <footer class="footer">
    <em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan</em>
  </footer>

</div>

<!-- CAROUSEL SCRIPT -->
<script>
(function () {
  const track = document.querySelector('.carousel-track');
  const slides = document.querySelectorAll('.social-embed');
  const prevBtn = document.querySelector('.carousel-btn.prev');
  const nextBtn = document.querySelector('.carousel-btn.next');
  const dots = document.querySelectorAll('.carousel-dots .dot');

  let index = 0;

  function updateCarousel(newIndex) {
    index = (newIndex + slides.length) % slides.length;
    track.style.transform = 'translateX(' + (-index * 100) + '%)';
    dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
  }

  prevBtn.addEventListener('click', () => updateCarousel(index - 1));
  nextBtn.addEventListener('click', () => updateCarousel(index + 1));

  dots.forEach(dot => {
    dot.addEventListener('click', () => updateCarousel(Number(dot.dataset.slide)));
  });
})();
</script>

</body>
</html>
