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
      --dark-green: #1e4034;
      --light-green: #4a8c73;
      --accent-green: #e8f5f0;
      --gold-accent: #d4af37;
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
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', sans-serif;
      color: var(--text-dark);
      line-height: 1.7;
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
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 clamp(1rem, 4vw, 3rem);
    }

    /* ENHANCED TITLE SECTION */
    .title-section {
      padding: clamp(3rem, 8vw, 5rem) 0 clamp(2rem, 6vw, 4rem);
      background: linear-gradient(135deg, #1a3d2f 0%, var(--dark-green) 50%, var(--primary-green) 100%);
      position: relative;
      overflow: hidden;
      text-align: center;
      margin-bottom: 2rem;
      border-radius: 0 0 24px 24px;
      box-shadow: var(--shadow-lg);
    }

    .title-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at 30% 50%, rgba(212, 175, 55, 0.1) 0%, transparent 50%),
                  radial-gradient(circle at 70% 30%, rgba(232, 245, 240, 0.05) 0%, transparent 50%);
      z-index: 0;
    }

    .project-title {
      font-size: clamp(2.5rem, 6vw, 4.5rem);
      font-weight: 800;
      color: white;
      margin-bottom: 1.5rem;
      letter-spacing: -0.02em;
      line-height: 1.1;
      text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
      position: relative;
      z-index: 1;
    }

    .project-subtitle {
      font-size: clamp(1.3rem, 3vw, 1.8rem);
      font-weight: 400;
      color: var(--accent-green);
      font-style: italic;
      letter-spacing: 0.02em;
      line-height: 1.5;
      max-width: 900px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .title-accent {
      color: var(--gold-accent);
      font-weight: 700;
    }

    /* Hero Section */
    .hero {
      padding: clamp(2rem, 6vw, 4rem) 0 clamp(2rem, 6vw, 4rem);
      background: linear-gradient(135deg, #f8fcfb 0%, #ffffff 100%);
      position: relative;
      overflow: hidden;
    }

    .hero::before {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 40%;
      height: 100%;
      background: linear-gradient(45deg, var(--accent-green) 0%, transparent 100%);
      opacity: 0.3;
      z-index: 0;
    }

    .hero-content {
      position: relative;
      z-index: 1;
    }

    .animated-tagline {
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 800;
      display: flex;
      align-items: center;
      margin-bottom: 2rem;
      color: var(--dark-green);
      flex-wrap: wrap;
      gap: 0.75rem;
      letter-spacing: -0.02em;
      line-height: 1.1;
    }

    .word-carousel {
      overflow: hidden;
      height: clamp(3rem, 6vw, 4rem);
      position: relative;
      display: inline-block;
      min-width: clamp(180px, 30vw, 300px);
    }

    .word-list {
      list-style: none;
      animation: continuousScroll 15s ease-in-out infinite;
      will-change: transform;
    }

    .word-list li {
      height: clamp(3rem, 6vw, 4rem);
      line-height: clamp(3rem, 6vw, 4rem);
      color: var(--light-green);
      font-weight: 800;
      font-size: clamp(2rem, 5vw, 3.5rem);
    }

    @keyframes continuousScroll {
      0%, 12.5% { transform: translateY(0%); }
      25%, 37.5% { transform: translateY(-25%); }
      50%, 62.5% { transform: translateY(-50%); }
      75%, 87.5% { transform: translateY(-75%); }
      100% { transform: translateY(-100%); }
    }

    .hero-description {
      font-size: clamp(1.1rem, 2.5vw, 1.3rem);
      color: var(--text-medium);
      max-width: 900px;
      margin-bottom: 3rem;
      line-height: 1.8;
      font-weight: 400;
    }

    .hero-description strong {
      color: var(--primary-green);
      font-weight: 600;
      background: linear-gradient(120deg, var(--accent-green) 0%, transparent 100%);
      padding: 0.1rem 0.3rem;
      border-radius: 3px;
    }

    /* Hero Image */
    .hero-image-container {
      width: 100%;
      max-width: 900px;
      margin: 4rem auto 0;
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      background: var(--accent-green);
      transform: translateY(0);
      transition: transform 0.6s var(--transition-smooth);
    }

    .hero-image-container:hover {
      transform: translateY(-8px);
    }

    .hero-image-container::before {
      content: '';
      display: block;
      padding-top: 56.25%;
    }

    .hero-image {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s var(--transition-smooth);
    }

    .hero-image-container:hover .hero-image {
      transform: scale(1.05);
    }

    /* Skeleton loader */
    .skeleton {
      background: linear-gradient(90deg, #f0f0f0 25%, #e8f5f0 50%, #f0f0f0 75%);
      background-size: 200% 100%;
      animation: loading 1.5s ease-in-out infinite;
    }

    @keyframes loading {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    .hero-image.loading {
      opacity: 0;
    }

    /* Content Sections */
    .content-section {
      padding: clamp(2.5rem, 5vw, 4rem) 0;
      border-bottom: 1px solid var(--border-light);
      scroll-margin-top: 2rem;
    }

    .content-section:last-of-type {
      border-bottom: none;
    }

    .section-header {
      margin-bottom: 2.5rem;
    }

    h2 {
      font-size: clamp(1.8rem, 4vw, 2.8rem);
      font-weight: 700;
      color: var(--dark-green);
      margin-bottom: 1.5rem;
      letter-spacing: -0.01em;
      position: relative;
      padding-bottom: 1rem;
      line-height: 1.3;
    }

    h2::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 80px;
      height: 4px;
      background: linear-gradient(90deg, var(--light-green), var(--primary-green));
      border-radius: 2px;
    }

    /* ENHANCED & COMPACT Info Lists */
    .info-list {
      list-style: none;
      padding-left: 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
      gap: 0.75rem 1.5rem; /* Reduced vertical and horizontal gap */
      margin-top: 1.5rem;
    }

    .info-list li {
      padding: 0.75rem 0 0.75rem 2.25rem; /* Reduced padding */
      position: relative;
      color: var(--text-medium);
      font-size: clamp(0.95rem, 2.5vw, 1.05rem); /* Slightly smaller font */
      transition: all 0.3s ease;
      min-height: 42px; /* Reduced min-height */
      display: flex;
      align-items: center;
      border-bottom: 1px solid transparent;
      line-height: 1.5;
    }

    .info-list li:hover {
      color: var(--primary-green);
      padding-left: 2.5rem; /* Reduced hover padding */
      border-bottom-color: var(--accent-green);
    }

    .info-list li::before {
      content: "✓";
      position: absolute;
      left: 0;
      color: var(--light-green);
      font-weight: bold;
      font-size: 1.2rem; /* Slightly smaller */
      transition: all 0.3s ease;
      top: 50%;
      transform: translateY(-50%);
      background: var(--accent-green);
      width: 28px; /* Smaller circle */
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .info-list li:hover::before {
      transform: translateY(-50%) scale(1.1);
      background: var(--light-green);
      color: white;
    }

    /* Enhanced Image Galleries */
    .image-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
      gap: clamp(1.5rem, 3vw, 2.5rem);
      margin: 3rem 0;
    }

    .gallery-item {
      position: relative;
      overflow: hidden;
      border-radius: 16px;
      box-shadow: var(--shadow-md);
      background: white;
      padding: 1rem;
      transition: all 0.4s var(--transition-smooth);
      cursor: pointer;
      border: 1px solid rgba(0,0,0,0.05);
      aspect-ratio: 1;
    }

    .gallery-item::before {
      content: '';
      display: block;
      position: absolute;
      inset: 1rem;
      background: var(--accent-green);
      border-radius: 12px;
      z-index: 0;
      opacity: 0.1;
    }

    .gallery-item:hover {
      transform: translateY(-8px) scale(1.02);
      box-shadow: var(--shadow-lg);
      z-index: 10;
      border-color: var(--light-green);
    }

    .gallery-item img {
      width: 100%;
      height: 100%;
      display: block;
      border-radius: 12px;
      transition: transform 0.5s ease, opacity 0.4s ease;
      object-fit: cover;
      position: relative;
      z-index: 1;
    }

    .gallery-item img.loading {
      opacity: 0;
    }

    .gallery-item:hover img {
      transform: scale(1.08);
    }

    /* Social Media Section */
    .social-section {
      background: linear-gradient(135deg, var(--accent-green) 0%, #ffffff 100%);
      padding: clamp(3rem, 6vw, 5rem) 0;
      margin: 4rem calc(clamp(1rem, 4vw, 3rem) * -1);
      position: relative;
      overflow: hidden;
    }

    .social-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
      opacity: 0.3;
    }

    .section-title {
      font-size: clamp(2rem, 5vw, 3.2rem);
      font-weight: 800;
      color: var(--dark-green);
      margin-bottom: 1rem;
      text-align: center;
      letter-spacing: -0.02em;
      line-height: 1.2;
    }

    .section-subtitle {
      font-size: clamp(1.1rem, 2.5vw, 1.3rem);
      color: var(--text-medium);
      text-align: center;
      margin-bottom: 3rem;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.7;
    }

    .social-grid {
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 350px), 1fr));
      gap: clamp(1.5rem, 3vw, 2.5rem);
      padding: 0 clamp(1rem, 4vw, 2.5rem);
    }

    .social-embed {
      background: #ffffff;
      border-radius: 20px;
      padding: 1.75rem;
      box-shadow: var(--shadow-lg);
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 450px;
      transition: all 0.4s var(--transition-smooth);
      border: 1px solid rgba(45, 95, 77, 0.1);
      overflow: hidden;
      position: relative;
    }

    .social-embed:hover {
      transform: translateY(-6px);
      box-shadow: 0 16px 40px rgba(0,0,0,0.15);
      border-color: var(--light-green);
    }

    .iframe-container {
      position: relative;
      width: 100%;
      max-width: 550px;
      overflow: hidden;
      border-radius: 16px;
    }

    .iframe-container iframe {
      width: 100%;
      border: 0;
      display: block;
    }

    /* Enhanced Partners Section */
    .partners-section {
      background: linear-gradient(135deg, #f8fcfb 0%, #ffffff 100%);
      padding: clamp(4rem, 8vw, 6rem) 0;
      position: relative;
    }

    .partners-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
      opacity: 0.2;
    }

    .partners-intro {
      text-align: center;
      max-width: 900px;
      margin: 0 auto 4rem;
      color: var(--text-medium);
      font-size: clamp(1.1rem, 2.5vw, 1.3rem);
      line-height: 1.8;
    }

    /* ENHANCED PARTNER GRID - Bigger logos */
    .partner-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 240px), 1fr));
      gap: clamp(2rem, 4vw, 3rem);
      margin: 4rem 0;
    }

    .partner-logo {
      background: white;
      padding: clamp(2rem, 4vw, 3rem);
      border-radius: 20px;
      box-shadow: var(--shadow-md);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.4s var(--transition-smooth);
      border: 2px solid transparent;
      min-height: 180px;
      aspect-ratio: 1.5;
      position: relative;
      overflow: hidden;
    }

    .partner-logo::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, var(--accent-green) 0%, transparent 100%);
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .partner-logo:hover {
      transform: translateY(-8px) scale(1.03);
      box-shadow: var(--shadow-lg);
      border-color: var(--light-green);
    }

    .partner-logo:hover::before {
      opacity: 0.1;
    }

    .partner-logo img {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      filter: grayscale(30%) brightness(1.1);
      transition: all 0.4s var(--transition-smooth);
      position: relative;
      z-index: 1;
    }

    .partner-logo img.loading {
      opacity: 0;
    }

    .partner-logo:hover img {
      filter: grayscale(0%) brightness(1);
      transform: scale(1.05);
    }

    /* Special styling for logos that need more visibility */
    .partner-logo:nth-child(2), /* Guerreros Buscadores */
    .partner-logo:nth-child(3), /* CentroGeo */
    .partner-logo:nth-child(4), /* Jalisco Search Commission */
    .partner-logo:nth-child(5) { /* Oxford */
      padding: clamp(2.5rem, 5vw, 3.5rem);
      min-height: 200px;
    }

    /* Partner Categories */
    .partner-category {
      margin: 5rem 0 3rem;
    }

    .partner-category h3 {
      font-size: clamp(1.5rem, 3vw, 2rem);
      color: var(--primary-green);
      margin-bottom: 2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--accent-green);
      font-weight: 600;
    }

    /* Buscadoras Special Section */
    .buscadoras-section {
      background: linear-gradient(135deg, #fff8f5 0%, #ffffff 100%);
      padding: clamp(4rem, 8vw, 6rem) 0;
      border-radius: 24px;
      margin: 4rem 0;
      position: relative;
      overflow: hidden;
    }

    .buscadoras-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
      opacity: 0.1;
    }

    .buscadoras-content {
      max-width: 900px;
      margin: 0 auto;
      text-align: center;
    }

    .buscadoras-image {
      max-width: 500px;
      margin: 3rem auto;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      transition: transform 0.6s var(--transition-smooth);
    }

    .buscadoras-image:hover {
      transform: translateY(-8px);
    }

    /* Footer */
    .footer {
      text-align: center;
      padding: clamp(4rem, 8vw, 6rem) 0;
      margin-top: 4rem;
      border-top: 2px solid var(--border-light);
      background: linear-gradient(135deg, #f8fcfb 0%, #ffffff 100%);
      position: relative;
      overflow: hidden;
    }

    .footer::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
    }

    .footer em {
      font-size: clamp(1.3rem, 3vw, 1.8rem);
      color: var(--dark-green);
      font-weight: 700;
      font-style: italic;
      letter-spacing: 0.02em;
      line-height: 1.6;
      display: inline-block;
      max-width: 90%;
      padding: 1rem 2rem;
      border-radius: 16px;
      background: linear-gradient(135deg, var(--accent-green) 0%, transparent 100%);
      position: relative;
      z-index: 1;
    }

    /* Mobile optimizations */
    @media (max-width: 1024px) {
      .partner-grid {
        grid-template-columns: repeat(auto-fill, minmax(min(100%, 200px), 1fr));
        gap: 1.5rem;
      }
    }

    @media (max-width: 768px) {
      .animated-tagline {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
      }

      .word-carousel {
        min-width: 200px;
      }

      .social-grid {
        grid-template-columns: 1fr;
      }

      .partner-grid {
        grid-template-columns: repeat(auto-fill, minmax(min(100%, 160px), 1fr));
        gap: 1.25rem;
      }

      .partner-logo {
        padding: 1.5rem;
        min-height: 140px;
      }

      .info-list {
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }
      
      .info-list li {
        padding: 0.5rem 0 0.5rem 2rem;
        min-height: 38px;
      }
    }

    @media (max-width: 480px) {
      .animated-tagline {
        font-size: 1.8rem;
      }

      .word-carousel {
        height: 2.5rem;
        min-width: 150px;
      }

      .word-list li {
        height: 2.5rem;
        line-height: 2.5rem;
        font-size: 1.8rem;
      }

      .partner-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
      }

      .partner-logo {
        padding: 1rem;
        min-height: 120px;
      }
      
      .title-section {
        padding: 2.5rem 1rem 2rem;
      }
      
      .project-title {
        font-size: 2.2rem;
      }
      
      .project-subtitle {
        font-size: 1.2rem;
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

    ::-moz-selection {
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

      .social-embed:hover,
      .gallery-item:hover,
      .partner-logo:hover {
        transform: none !important;
        box-shadow: var(--shadow-sm) !important;
      }
    }

    /* High contrast mode support */
    @media (prefers-contrast: high) {
      :root {
        --primary-green: #1a3d2f;
        --border-light: #999;
      }

      .partner-logo {
        border: 2px solid var(--primary-green);
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <!-- ENHANCED TITLE SECTION -->
    <section class="title-section">
      <h1 class="project-title">FOUND Project</h1>
      <p class="project-subtitle">
        <span class="title-accent">Interpretar la Naturaleza</span> para Encontrar a Quienes nos Faltan
      </p>
    </section>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <div class="animated-tagline">
          <span>Using technology to&nbsp;</span>
          <div class="word-carousel" role="text" aria-label="Rotating tagline">
            <ul class="word-list">
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
      </div>
    </section>

    <!-- Community Driven Section -->
    <section class="content-section" id="community">
      <div class="section-header">
        <h2><span>Driven by Families and Research Communities</span></h2>
      </div>
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
    <section class="buscadoras-section" id="buscadoras">
      <div class="buscadoras-content">
        <h2>The Role of Buscadoras</h2>
        <p class="hero-description">
          Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. FOUND listens, learns, and incorporates their methods into our technological efforts.
        </p>
        <div class="buscadoras-image">
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

    <!-- Enhanced Partners Section -->
    <section class="partners-section" id="partners">
      <h2 class="section-title">Our Partners</h2>
      <p class="partners-intro">
        FOUND brings together an exceptional coalition of academic institutions, government agencies, civil society organizations, and international partners. Together, we work toward a common goal: bringing dignity and closure to families searching for their loved ones.
      </p>

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
      <em>FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
    </footer>
  </div>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</body>
</html>
