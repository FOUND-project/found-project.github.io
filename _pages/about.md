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
  <meta name="description" content="FOUND combines technology and grassroots knowledge to search for disappeared persons in Mexico, bringing dignity and closure to families.">
  <meta property="og:title" content="FOUND Project - Using Technology to Search and Remember">
  <meta property="og:description" content="Over 120,000 persons are reported as disappeared in Mexico. FOUND combines technology and grassroots knowledge to search, locate and drive systemic change.">
  <meta property="og:type" content="website">
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
      --accent-green: #e8f5f0;
      --text-dark: #1a1a1a;
      --text-medium: #4a4a4a;
      --text-light: #666;
      --border-light: #e0e0e0;
      --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
      --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
      --transition-smooth: cubic-bezier(0.4, 0, 0.2, 1);
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
      color: var(--text-dark);
      line-height: 1.65;
      background: #ffffff;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
    }

    /* Focus styles for accessibility */
    *:focus-visible {
      outline: 3px solid var(--light-green);
      outline-offset: 2px;
      border-radius: 4px;
    }

    .page {
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 clamp(1rem, 4vw, 2.5rem);
    }

    /* Hero Section */
    .hero {
      padding: clamp(3rem, 8vw, 5rem) 0 clamp(2rem, 6vw, 4rem);
      border-bottom: 2px solid var(--border-light);
      background: linear-gradient(to bottom, #ffffff 0%, #fafbfa 100%);
    }

    .animated-tagline {
      font-size: clamp(1.5rem, 4vw, 2.5rem);
      font-weight: 700;
      display: flex;
      align-items: center;
      margin-bottom: 2rem;
      color: var(--primary-green);
      flex-wrap: wrap;
      gap: 0.5rem;
      letter-spacing: -0.02em;
      line-height: 1.2;
    }

    .word-carousel {
      overflow: hidden;
      height: clamp(2.5rem, 5vw, 3rem);
      position: relative;
      display: inline-block;
      min-width: clamp(140px, 25vw, 200px);
    }

    .word-list {
      list-style: none;
      animation: continuousScroll 12s linear infinite;
      will-change: transform;
    }

    .word-list li {
      height: clamp(2.5rem, 5vw, 3rem);
      line-height: clamp(2.5rem, 5vw, 3rem);
      color: var(--light-green);
      font-weight: 700;
    }

    @keyframes continuousScroll {
      0% { transform: translateY(0%); }
      100% { transform: translateY(-50%); }
    }

    .hero-description {
      font-size: clamp(1.05rem, 2.5vw, 1.2rem);
      color: var(--text-medium);
      max-width: 850px;
      margin-bottom: 2.5rem;
      line-height: 1.75;
      font-weight: 400;
    }

    .hero-description strong {
      color: var(--primary-green);
      font-weight: 600;
    }

    /* Image container with aspect ratio */
    .hero-image-container {
      width: 100%;
      max-width: 700px;
      margin: 3rem auto;
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      background: var(--accent-green);
    }

    .hero-image-container::before {
      content: '';
      display: block;
      padding-top: 56.25%; /* 16:9 aspect ratio */
    }

    .hero-image {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s var(--transition-smooth);
    }

    .hero-image-container:hover .hero-image {
      transform: scale(1.03);
    }

    /* Skeleton loader */
    .skeleton {
      background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
      background-size: 200% 100%;
      animation: loading 1.5s infinite;
    }

    @keyframes loading {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    .hero-image.loading {
      opacity: 0;
    }

    /* Social Media Section */
    .social-section {
      background: var(--accent-green);
      padding: clamp(2rem, 5vw, 3rem) clamp(1rem, 4vw, 2.5rem);
      margin: 3rem calc(clamp(1rem, 4vw, 2.5rem) * -1);
      position: relative;
    }

    .social-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
      opacity: 0.2;
    }

    .section-title {
      font-size: clamp(1.75rem, 4vw, 2.75rem);
      font-weight: 700;
      color: var(--primary-green);
      margin-bottom: 0.75rem;
      text-align: center;
      letter-spacing: -0.02em;
      line-height: 1.2;
    }

    .section-subtitle {
      font-size: clamp(1rem, 2vw, 1.15rem);
      color: var(--text-light);
      text-align: center;
      margin-bottom: 2rem;
      max-width: 700px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.6;
    }

    .social-grid {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));
      gap: clamp(1.5rem, 3vw, 2rem);
    }

    .social-embed {
      background: #ffffff;
      border-radius: 16px;
      padding: 1.5rem;
      box-shadow: var(--shadow-md);
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 400px;
      transition: all 0.3s var(--transition-smooth);
      border: 1px solid rgba(45, 95, 77, 0.08);
      overflow: hidden;
      position: relative;
    }

    .social-embed:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(0,0,0,0.15);
      border-color: var(--light-green);
    }

    /* Responsive iframe container */
    .iframe-container {
      position: relative;
      width: 100%;
      max-width: 504px;
      overflow: hidden;
      border-radius: 12px;
    }

    .iframe-container iframe {
      width: 100%;
      border: 0;
      display: block;
    }

    .social-embed.twitter-embed {
      min-height: 450px;
    }

    .social-embed.twitter-embed .twitter-tweet {
      margin: 0 !important;
    }

    /* Loading state for embeds */
    .embed-loading {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: white;
      z-index: 1;
    }

    .embed-loading::after {
      content: '';
      width: 40px;
      height: 40px;
      border: 3px solid var(--accent-green);
      border-top-color: var(--light-green);
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    /* Content Sections */
    .content-section {
      padding: clamp(2rem, 4vw, 2.5rem) 0;
      border-bottom: 1px solid var(--border-light);
      scroll-margin-top: 2rem;
    }

    .content-section:last-of-type {
      border-bottom: none;
    }

    h2 {
      font-size: clamp(1.5rem, 3.5vw, 2.25rem);
      font-weight: 700;
      color: var(--primary-green);
      margin-bottom: 1.75rem;
      letter-spacing: -0.01em;
      position: relative;
      padding-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      line-height: 1.3;
      flex-wrap: wrap;
    }

    h2::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 60px;
      height: 3px;
      background: var(--light-green);
      border-radius: 2px;
    }

    .info-list {
      list-style: none;
      padding-left: 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
      gap: 0.75rem clamp(1rem, 3vw, 2rem);
      margin-top: 2rem;
    }

    .info-list li {
      padding: 0.75rem 0 0.75rem 2.25rem;
      position: relative;
      color: var(--text-medium);
      font-size: clamp(0.95rem, 2vw, 1.05rem);
      transition: all 0.2s ease;
      min-height: 44px;
      display: flex;
      align-items: center;
    }

    .info-list li:hover {
      color: var(--primary-green);
      padding-left: 2.5rem;
    }

    .info-list li::before {
      content: "✓";
      position: absolute;
      left: 0;
      color: var(--light-green);
      font-weight: bold;
      font-size: 1.3rem;
      transition: all 0.2s ease;
      top: 50%;
      transform: translateY(-50%);
    }

    .info-list li:hover::before {
      transform: translateY(-50%) scale(1.2);
    }

    /* Image Galleries with lazy loading */
    .image-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 220px), 1fr));
      gap: clamp(1rem, 2.5vw, 1.75rem);
      margin: 2.5rem 0;
    }

    .gallery-item {
      position: relative;
      overflow: hidden;
      border-radius: 12px;
      box-shadow: var(--shadow-sm);
      background: white;
      padding: 0.75rem;
      transition: all 0.35s var(--transition-smooth);
      cursor: pointer;
      border: 1px solid rgba(0,0,0,0.04);
      aspect-ratio: 1;
    }

    .gallery-item::before {
      content: '';
      display: block;
      position: absolute;
      inset: 0.75rem;
      background: var(--accent-green);
      border-radius: 8px;
      z-index: 0;
    }

    .gallery-item:hover {
      transform: translateY(-6px) scale(1.02);
      box-shadow: var(--shadow-lg);
      z-index: 10;
      border-color: var(--light-green);
    }

    .gallery-item img {
      width: 100%;
      height: 100%;
      display: block;
      border-radius: 8px;
      transition: transform 0.35s ease, opacity 0.3s ease;
      object-fit: cover;
      position: relative;
      z-index: 1;
    }

    .gallery-item img.loading {
      opacity: 0;
    }

    .gallery-item:hover img {
      transform: scale(1.05);
    }

    /* Partner Logos */
    .partner-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 180px), 1fr));
      gap: clamp(1.5rem, 3vw, 2rem);
      margin: 3rem 0;
    }

    .partner-logo {
      background: white;
      padding: clamp(1.5rem, 3vw, 2rem);
      border-radius: 12px;
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.3s var(--transition-smooth);
      border: 1px solid rgba(0,0,0,0.04);
      min-height: 120px;
      aspect-ratio: 1.5;
    }

    .partner-logo:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--light-green);
    }

    .partner-logo img {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      filter: grayscale(20%);
      transition: filter 0.3s ease, opacity 0.3s ease;
    }

    .partner-logo img.loading {
      opacity: 0;
    }

    .partner-logo:hover img {
      filter: grayscale(0%);
    }

    /* Footer */
    .footer {
      text-align: center;
      padding: clamp(3rem, 6vw, 4rem) 0;
      margin-top: 4rem;
      border-top: 2px solid var(--border-light);
      background: linear-gradient(to top, #fafbfa 0%, #ffffff 100%);
    }

    .footer em {
      font-size: clamp(1.1rem, 2.5vw, 1.3rem);
      color: var(--primary-green);
      font-weight: 600;
      font-style: italic;
      letter-spacing: 0.01em;
      line-height: 1.5;
      display: inline-block;
      max-width: 90%;
    }

    /* Mobile optimizations */
    @media (max-width: 768px) {
      .social-grid {
        grid-template-columns: 1fr;
      }

      .gallery-item {
        aspect-ratio: 1;
      }

      h2::after {
        width: 40px;
        height: 2px;
      }
    }

    @media (max-width: 480px) {
      .animated-tagline {
        font-size: 1.4rem;
      }

      .social-embed {
        padding: 1rem;
        min-height: 350px;
      }
    }

    /* Smooth scroll */
    html {
      scroll-behavior: smooth;
    }

    @media (prefers-reduced-motion: reduce) {
      html {
        scroll-behavior: auto;
      }
    }

    /* Selection styling */
    ::selection {
      background: var(--light-green);
      color: white;
    }

    /* Print styles */
    @media print {
      .social-section,
      .image-gallery,
      .partner-grid {
        break-inside: avoid;
      }
    }

    /* High contrast mode support */
    @media (prefers-contrast: high) {
      :root {
        --primary-green: #1a3d2f;
        --border-light: #999;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <!-- Hero Section -->
    <section class="hero">
      <div class="animated-tagline">
        <span>Using technology to&nbsp;</span>
        <div class="word-carousel" role="text" aria-label="Rotating tagline">
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
        Over 120,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> combines technology and grassroots knowledge to search, locate and drive systemic change.
      </p>

      <div class="hero-image-container skeleton">
        <img 
          src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/NDAI5.gif?raw=true" 
          alt="FOUND Project team using advanced technology in field search operations" 
          class="hero-image loading"
          loading="lazy"
          onload="this.classList.remove('loading'); this.parentElement.classList.remove('skeleton')">
      </div>
    </section>

    <!-- Community Driven Section -->
    <section class="content-section" id="community">
      <h2><span role="img" aria-label="seedling">🌱</span><span>Driven by families and research communities</span></h2>
      <p class="hero-description">
        FOUND is guided and motivated by <strong>search collectives</strong> and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
      </p>
    </section>

    <!-- Institutional Collaborations -->
    <section class="content-section" id="collaborations">
      <h2>Institutional Collaborations</h2>
      <ul class="info-list">
        <li>Executive Office of the UN Secretary-General</li>
        <li>UK's Foreign, Commonwealth & Development Office (FCDO)</li>
        <li>Local Search Commissions and Attorney's Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li>
        <li>Colombian Search Unit</li>
        <li>Mexico's National Search Commission</li>
        <li>Mexican Science and Technology Secretariat</li>
        <li>British Embassy in Mexico City</li>
        <li>British Association for Forensic Anthropology</li>
      </ul>
    </section>

    <!-- Technologies Section -->
    <section class="content-section" id="technologies">
      <h2>Technologies in Action</h2>
      <ul class="info-list">
        <li>Multispectral & Hyperspectral Imaging</li>
        <li>Airborne LiDAR</li>
        <li>Seismic Noise Interferometry (TIRSA)</li>
        <li>Electrical Resistivity Tomography, Conductivimetry Measurements</li>
        <li>Satellite Spectral Analysis</li>
        <li>Forensic Entomology, Botany, Territorial Analysis, Soil Science</li>
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
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/assets/WhatsApp%20Image%202025-03-22%20at%2019.01.47.jpeg?raw=true" alt="Search methodology in practice" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
      </div>
    </section>

    <!-- Buscadoras Section -->
    <section class="content-section" id="buscadoras">
      <h2>The Role of Buscadoras</h2>
      <p class="hero-description">
        Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. FOUND listens, learns, and incorporates their methods into our technological efforts.
      </p>
      <div class="image-gallery" style="max-width: 450px; margin: 2rem auto;">
        <div class="gallery-item">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolizing hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
      </div>
    </section>

    <!-- Social Media Section -->
    <section class="social-section" id="social">
      <h2 class="section-title">Follow Our Journey</h2>
      <p class="section-subtitle">Stay connected with our latest findings, community stories, and collaborative efforts</p>

      <div class="social-grid">
        <!-- Twitter/X -->
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

        <!-- LinkedIn FCDO -->
        <div class="social-embed">
          <div class="iframe-container">
            <iframe
              src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7343552976185114624"
              height="924"
              width="504"
              frameborder="0"
              allowfullscreen=""
              title="FCDO LinkedIn post about FOUND Project"
              loading="lazy"></iframe>
          </div>
        </div>

        <!-- LinkedIn 1 -->
        <div class="social-embed">
          <div class="iframe-container">
            <iframe
              src="https://www.linkedin.com/embed/feed/update/urn:li:share:7398929122778877954"
              height="1170"
              width="504"
              frameborder="0"
              allowfullscreen=""
              title="FOUND Project LinkedIn update"
              loading="lazy"></iframe>
          </div>
        </div>

        <!-- LinkedIn 2 -->
        <div class="social-embed">
          <div class="iframe-container">
            <iframe
              src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7398371958595145728"
              height="924"
              width="504"
              frameborder="0"
              allowfullscreen=""
              title="FOUND Project community engagement"
              loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </section>

    <!-- Partners Section -->
    <section class="content-section" id="partners">
      <h2>Partners</h2>
      <div class="partner-grid">
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Social-web-v1.jpg?raw=true" alt="Frontier Tech Hub partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/1%20logo%20Final%20Guerreros%20Buscadores.png?raw=true" alt="Guerreros Buscadores partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/2%20logo_centrogeo_wide.svg" alt="CentroGeo partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/3%20logo%20CBJ.png?raw=true" alt="Jalisco Search Commission partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/4%20logo%20oxford-university-logo.png?raw=true" alt="Oxford University partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/images(1).png?raw=true" alt="UNAM Geophysics partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/6%20logo%20Ingenieria%20UNAM.png?raw=true" alt="UNAM Engineering partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/580141488dfc53bfdbde59fa6b043438.jpg?raw=true" alt="UdeG partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/8%20logo%20UPZMG2.png?raw=true" alt="UPZMG partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/9%20logo%20UWE%20Bristol.svg" alt="UWE Bristol partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/11%20logo%20BAFAlogo_orig.png?raw=true" alt="BAFA partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/British%20Embassy%20Mexico_Blue%20(ENG).png?raw=true" alt="British Embassy partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/OFOTA_COLOUR_WEB.jpg?raw=true" alt="OFA partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Beth.jpg?raw=true" alt="Bath University partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
        <div class="partner-logo">
          <img src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg" alt="Colombia UBPD partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan</em>
    </footer>
  </div>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</body>
</html>
