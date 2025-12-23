---
permalink: /
title:
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
  <meta property="og:description" content="124,354 persons are reported as disappeared in Mexico. Behind each case, there is a family searching for answers. FOUND combines technology with the knowledge of searching families to learn, locate, and drive systemic change.">
  <meta property="og:type" content="website">
  <title>FOUND Project - Using Technology to Search and Remember</title>

  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

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
      html { scroll-behavior: auto !important; }
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

    *:focus-visible {
      outline: 3px solid var(--light-green);
      outline-offset: 2px;
      border-radius: 6px;
    }

    /* Language toggle */
    .lang-toggle {
      position: absolute;
      top: 1.5rem;
      right: clamp(1rem, 4vw, 3rem);
      display: inline-flex;
      gap: 0.5rem;
      z-index: 2;
    }

    .lang-btn {
      border: 1px solid rgba(255,255,255,0.8);
      background: rgba(0,0,0,0.15);
      color: #ffffff;
      padding: 0.25rem 0.75rem;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s var(--transition-smooth);
      backdrop-filter: blur(6px);
    }

    .lang-btn:hover { background: rgba(0,0,0,0.3); }

    .lang-btn.active {
      background: #ffffff;
      color: var(--dark-green);
      border-color: #ffffff;
      box-shadow: 0 0 0 1px rgba(0,0,0,0.08);
    }

    /* Title */
    .title-section {
      padding: clamp(3rem, 8vw, 5rem) 0 clamp(2rem, 6vw, 4rem);
      background: linear-gradient(135deg, #1a3d2f 0%, var(--dark-green) 50%, var(--primary-green) 100%);
      position: relative;
      overflow: hidden;
      text-align: center;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-lg);
    }

    .title-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(circle at 30% 50%, rgba(212, 175, 55, 0.1) 0%, transparent 50%),
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
      padding: 0 clamp(1rem, 4vw, 3rem);
    }

    .title-accent { color: var(--gold-accent); font-weight: 700; }

    /* Hero */
    .hero {
      padding: clamp(2rem, 6vw, 4rem) clamp(1rem, 4vw, 3rem);
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
      max-width: 1400px;
      margin: 0 auto;
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

    .hero-image-container {
      width: 100%;
      max-width: 1100px;
      margin: 4rem auto 0;
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      background: var(--accent-green);
      transform: translateY(0);
      transition: transform 0.6s var(--transition-smooth);
    }

    .hero-image-container:hover { transform: translateY(-8px); }
    .hero-image-container::before { content: ''; display: block; padding-top: 56.25%; }

    .hero-image {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s var(--transition-smooth);
    }

    .hero-image-container:hover .hero-image { transform: scale(1.05); }

    .skeleton {
      background: linear-gradient(90deg, #f0f0f0 25%, #e8f5f0 50%, #f0f0f0 75%);
      background-size: 200% 100%;
      animation: loading 1.5s ease-in-out infinite;
    }

    @keyframes loading {
      0% { background-position: 200% 0; }
      100% { background-position: -200% 0; }
    }

    .hero-image.loading { opacity: 0; }

    /* Sections */
    .content-section {
      padding: clamp(2.5rem, 5vw, 4rem) clamp(1rem, 4vw, 3rem);
      border-bottom: 1px solid var(--border-light);
      scroll-margin-top: 2rem;
    }

    .content-section:last-of-type { border-bottom: none; }

    .section-container {
      max-width: 1400px;
      margin: 0 auto;
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

    .info-list {
      list-style: none;
      padding-left: 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));
      gap: 0.75rem 2rem;
      margin-top: 1.5rem;
    }

    .info-list li {
      padding: 0.75rem 0 0.75rem 2.25rem;
      position: relative;
      color: var(--text-medium);
      font-size: clamp(0.95rem, 2.5vw, 1.05rem);
      transition: all 0.3s ease;
      min-height: 42px;
      display: flex;
      align-items: center;
      border-bottom: 1px solid transparent;
      line-height: 1.5;
    }

    .info-list li:hover {
      color: var(--primary-green);
      padding-left: 2.5rem;
      border-bottom-color: var(--accent-green);
    }

    .info-list li::before {
      content: "✓";
      position: absolute;
      left: 0;
      color: var(--light-green);
      font-weight: bold;
      font-size: 1.2rem;
      transition: all 0.3s ease;
      top: 50%;
      transform: translateY(-50%);
      background: var(--accent-green);
      width: 28px;
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

    /* === Institutional Collaborations (logos + labels) === */
    .collab-wrap { margin-top: 2rem; }

    .collab-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr));
      gap: clamp(1.25rem, 2.5vw, 2rem);
      margin-top: 1.5rem;
    }

    .collab-card {
      background: #ffffff;
      border-radius: 18px;
      box-shadow: var(--shadow-md);
      border: 1px solid rgba(45, 95, 77, 0.10);
      overflow: hidden;
      position: relative;
      transition: transform 0.35s var(--transition-smooth), box-shadow 0.35s var(--transition-smooth), border-color 0.35s var(--transition-smooth);
      min-height: 220px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .collab-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(circle at 15% 10%, rgba(232,245,240,0.85) 0%, transparent 55%),
        radial-gradient(circle at 85% 0%, rgba(212,175,55,0.12) 0%, transparent 60%);
      opacity: 0;
      transition: opacity 0.35s ease;
      pointer-events: none;
    }

    .collab-card:hover {
      transform: translateY(-8px);
      box-shadow: var(--shadow-lg);
      border-color: rgba(74, 140, 115, 0.55);
    }

    .collab-card:hover::before { opacity: 1; }

    .collab-logo {
      padding: 1.25rem 1.25rem 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 140px;
      position: relative;
      z-index: 1;
    }

    .collab-logo img {
      max-width: 100%;
      max-height: 95px;
      width: auto;
      height: auto;
      object-fit: contain;
      filter: grayscale(25%) brightness(1.05);
      transition: transform 0.35s var(--transition-smooth), filter 0.35s var(--transition-smooth), opacity 0.3s ease;
    }

    .collab-logo img.loading { opacity: 0; }

    .collab-card:hover .collab-logo img {
      filter: grayscale(0%) brightness(1);
      transform: scale(1.04);
    }

    .collab-meta {
      padding: 0.85rem 1.15rem 1.15rem;
      border-top: 1px solid rgba(0,0,0,0.06);
      background: linear-gradient(180deg, rgba(232,245,240,0.25) 0%, rgba(255,255,255,0.85) 100%);
      position: relative;
      z-index: 1;
    }

    .collab-name {
      font-weight: 700;
      color: var(--dark-green);
      font-size: 1.02rem;
      line-height: 1.35;
      letter-spacing: -0.01em;
    }

    .collab-note {
      margin-top: 0.35rem;
      color: var(--text-light);
      font-size: 0.92rem;
      line-height: 1.45;
    }

    /* Gallery */
    .image-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr));
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

    .gallery-item img.loading { opacity: 0; }
    .gallery-item:hover img { transform: scale(1.08); }

    /* Social */
    .social-section {
      background: linear-gradient(135deg, var(--accent-green) 0%, #ffffff 100%);
      padding: clamp(3rem, 6vw, 5rem) clamp(1rem, 4vw, 3rem);
      margin: 4rem 0;
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

    .social-container { max-width: 1600px; margin: 0 auto; }

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
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 400px), 1fr));
      gap: clamp(1.5rem, 3vw, 2.5rem);
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
      max-width: 600px;
      overflow: hidden;
      border-radius: 16px;
    }

    .iframe-container iframe { width: 100%; border: 0; display: block; }

    /* Partners */
    .partners-section {
      background: linear-gradient(135deg, #f8fcfb 0%, #ffffff 100%);
      padding: clamp(4rem, 8vw, 6rem) clamp(1rem, 4vw, 3rem);
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

    .partners-container { max-width: 1600px; margin: 0 auto; }

    .partners-intro {
      text-align: center;
      max-width: 1000px;
      margin: 0 auto 4rem;
      color: var(--text-medium);
      font-size: clamp(1.1rem, 2.5vw, 1.3rem);
      line-height: 1.8;
    }

    .partner-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr));
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
      min-height: 200px;
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

    .partner-logo:hover::before { opacity: 0.1; }

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

    .partner-logo img.loading { opacity: 0; }

    .partner-logo:hover img {
      filter: grayscale(0%) brightness(1);
      transform: scale(1.05);
    }

    .partner-logo:nth-child(2),
    .partner-logo:nth-child(3),
    .partner-logo:nth-child(4),
    .partner-logo:nth-child(5) {
      padding: clamp(2.5rem, 5vw, 3.5rem);
      min-height: 220px;
    }

    /* Buscadoras */
    .buscadoras-section {
      background: linear-gradient(135deg, #fff8f5 0%, #ffffff 100%);
      padding: clamp(4rem, 8vw, 6rem) clamp(1rem, 4vw, 3rem);
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
      max-width: 1100px;
      margin: 0 auto;
      text-align: center;
    }

    .buscadoras-image {
      max-width: 600px;
      margin: 3rem auto;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      transition: transform 0.6s var(--transition-smooth);
    }

    .buscadoras-image:hover { transform: translateY(-8px); }

    /* Footer */
    .footer {
      text-align: center;
      padding: clamp(4rem, 8vw, 6rem) clamp(1rem, 4vw, 3rem);
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

    .footer-content { max-width: 1400px; margin: 0 auto; }

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

    html { scroll-behavior: smooth; }

    ::selection { background: var(--light-green); color: white; }
    ::-moz-selection { background: var(--light-green); color: white; }

    @media (max-width: 1024px) {
      .partner-grid { grid-template-columns: repeat(auto-fill, minmax(min(100%, 220px), 1fr)); gap: 1.5rem; }
      .collab-grid { grid-template-columns: repeat(auto-fill, minmax(min(100%, 220px), 1fr)); }
    }

    @media (max-width: 768px) {
      .animated-tagline { flex-direction: column; align-items: flex-start; gap: 0.5rem; }
      .word-carousel { min-width: 200px; }
      .social-grid { grid-template-columns: 1fr; }

      .partner-grid { grid-template-columns: repeat(auto-fill, minmax(min(100%, 180px), 1fr)); gap: 1.25rem; }
      .partner-logo { padding: 1.5rem; min-height: 160px; }

      .partner-logo:nth-child(2),
      .partner-logo:nth-child(3),
      .partner-logo:nth-child(4),
      .partner-logo:nth-child(5) { min-height: 180px; }

      .info-list { grid-template-columns: 1fr; gap: 0.5rem; }
      .info-list li { padding: 0.5rem 0 0.5rem 2rem; min-height: 38px; }

      .hero,
      .content-section,
      .social-section,
      .partners-section,
      .buscadoras-section,
      .footer { padding-left: 1.5rem; padding-right: 1.5rem; }

      .lang-toggle { top: 1rem; right: 1rem; }
    }

    @media (max-width: 480px) {
      .animated-tagline { font-size: 1.8rem; }
      .word-carousel { height: 2.5rem; min-width: 150px; }
      .word-list li { height: 2.5rem; line-height: 2.5rem; font-size: 1.8rem; }

      .partner-grid { grid-template-columns: repeat(2, 1fr); gap: 1rem; }
      .partner-logo { padding: 1rem; min-height: 140px; }

      .title-section { padding: 2.5rem 1rem 2rem; }
      .project-title { font-size: 2.2rem; }
      .project-subtitle { font-size: 1.2rem; }

      .hero,
      .content-section,
      .social-section,
      .partners-section,
      .buscadoras-section,
      .footer { padding-left: 1rem; padding-right: 1rem; }
    }

    @media print {
      .social-section, .image-gallery, .partner-grid, .collab-grid { break-inside: avoid; }
      .social-embed:hover, .gallery-item:hover, .partner-logo:hover, .collab-card:hover {
        transform: none !important;
        box-shadow: var(--shadow-sm) !important;
      }
    }

    @media (prefers-contrast: high) {
      :root { --primary-green: #1a3d2f; --border-light: #999; }
      .partner-logo, .collab-card { border: 2px solid var(--primary-green) !important; }
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
      <div class="animated-tagline">
        <span id="hero-tagline-static">Using technology to&nbsp;</span>
        <div class="word-carousel" role="text" aria-label="Rotating tagline">
          <ul class="word-list">
            <li id="word-1">dignify.</li>
            <li id="word-2">remember.</li>
            <li id="word-3">search.</li>
            <li id="word-4">bring closure.</li>
          </ul>
        </div>
      </div>

      <p class="hero-description" id="hero-main-text">
        124,354 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers.
        <strong>FOUND</strong> combines technology with the knowledge of searching families to learn, locate, and drive systemic change.
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

  <!-- COMMUNITY -->
  <section class="content-section" id="community">
    <div class="section-container">
      <div class="section-header">
        <h2 id="community-title"><span>Driven by Families and Research Communities</span></h2>
      </div>
      <p class="hero-description" id="community-text">
        FOUND is guided and motivated by <strong>search collectives</strong> and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
      </p>
    </div>
  </section>

  <!-- INSTITUTIONAL COLLABORATIONS (FIXED + IMAGES + UNIQUE IDs + WORKS IN 3 LANGUAGES) -->
  <section class="content-section" id="collaborations">
    <div class="section-container">
      <h2 id="collab-title">Institutional Collaborations</h2>

      <div class="collab-wrap" aria-label="Institutional collaborations logos">
        <div class="collab-grid">
          <!-- 1 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/1%20Executive%20Office%20of%20the%20UN%20Secretary-General.svg"
                alt="Executive Office of the UN Secretary-General logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-1">Executive Office of the UN Secretary-General</div>
              <div class="collab-note" id="collab-note-1">International collaboration</div>
            </div>
          </div>

          <!-- 2 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/2%20UK's%20Foreign%2C%20Commonwealth%20%26%20Development%20Office%20(FCDO).png"
                alt="UK Foreign, Commonwealth &amp; Development Office (FCDO) logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-2">UK's Foreign, Commonwealth &amp; Development Office (FCDO)</div>
              <div class="collab-note" id="collab-note-2">Policy, funding, and partnerships</div>
            </div>
          </div>

          <!-- 3 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/3%20Comisio%CC%81n%20de%20Bu%CC%81squeda%20de%20Jalisco.png"
                alt="Comisión de Búsqueda de Jalisco logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-3">
                Local Search Commissions and Attorney's Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)
              </div>
              <div class="collab-note" id="collab-note-3">Operational collaboration, policy impact</div>
            </div>
          </div>

          <!-- 4 (UBPD) -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/4292155f0372a05a0900046966657f02b7e6e7c9/images/12%20logo%20ubpd_color_logo.svg"
                alt="Colombian Search Unit (UBPD) logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-4">Colombian Search Unit</div>
              <div class="collab-note" id="collab-note-4">Casework and technical exchange</div>
            </div>
          </div>

          <!-- 5 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/4%20Comision%20Nacional%20de%20Busqueda.png"
                alt="Mexico's National Search Commission logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-5">Mexico's National Search Commission</div>
              <div class="collab-note" id="collab-note-5">Casework and technical exchange</div>
            </div>
          </div>

          <!-- 6 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/5%20Logotipo_SECIHTI_2025-2030.svg"
                alt="Mexican Science and Technology Secretariat (SECIHTI) logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-6">Mexican Science and Technology Secretariat</div>
              <div class="collab-note" id="collab-note-6">Funding</div>
            </div>
          </div>

          <!-- 7 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png"
                alt="British Embassy Mexico City logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-7">British Embassy in Mexico City</div>
              <div class="collab-note" id="collab-note-7">Funding, Coordination support</div>
            </div>
          </div>

          <!-- 8 -->
          <div class="collab-card">
            <div class="collab-logo">
              <img
                src="https://raw.githubusercontent.com/FOUND-project/found-project.github.io/d7867dc147eb1b230142511fce739aa481c6177d/images/7%20logo%20BAFAlogo_orig.png"
                alt="British Association for Forensic Anthropology logo"
                loading="lazy"
                class="loading"
                onload="this.classList.remove('loading')">
            </div>
            <div class="collab-meta">
              <div class="collab-name" id="collab-item-8">British Association for Forensic Anthropology</div>
              <div class="collab-note" id="collab-note-8">Forensic expertise</div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

  <!-- TECHNOLOGIES -->
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
    </div>
  </section>

  <!-- BUSCADORAS -->
  <section class="buscadoras-section" id="buscadoras">
    <div class="buscadoras-content">
      <h2 id="buscadoras-title">The Role of Buscadoras</h2>
      <p class="hero-description" id="buscadoras-text">
        Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. Alongside them, FOUND listens, learns, and incorporates their methods into our technological efforts.
      </p>
      <div class="buscadoras-image">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolizing hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
      </div>
    </div>
  </section>

  <!-- SOCIAL -->
  <section class="social-section" id="social">
    <div class="social-container">
      <h2 class="section-title" id="social-title">Follow Our Journey</h2>
      <p class="section-subtitle" id="social-subtitle">Stay connected with our latest findings, community stories, and collaborations</p>

      <div class="social-grid">
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
    </div>
  </section>

  <!-- PARTNERS (UNCHANGED) -->
  <section class="partners-section" id="partners">
    <div class="partners-container">
      <h2 class="section-title" id="partners-title">Our Partners</h2>
      <p class="partners-intro" id="partners-intro">
        FOUND brings together a coalition of academic institutions, government bodies, civil society organisations, and international partners. Together, we seek to honour the memory of those who are missing and stand with families as they search for a form of closure.
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
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/d7867dc147eb1b230142511fce739aa481c6177d/images/6%20British%20Embassy%20Mexico_Blue%20(ENG).png?raw=true" alt="British Embassy partner logo" loading="lazy" class="loading" onload="this.classList.remove('loading')">
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
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-content">
      <em id="footer-text">FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
    </div>
  </footer>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

  <!-- LANGUAGE TOGGLE -->
  <script>
    (function() {
      const translations = {
        en: {
          'hero-tagline-static': 'Using technology to&nbsp;',
          'word-1': 'dignify.',
          'word-2': 'remember.',
          'word-3': 'search.',
          'word-4': 'bring closure.',
          'hero-main-text': '124,354 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> combines technology and the knowledge of searching families to learn, locate, and drive systemic change.',
          'community-title': 'Driven by Families and Research Communities',
          'community-text': 'FOUND is guided and motivated by <strong>search collectives</strong> and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.',
          'collab-title': 'Institutional Collaborations',
          'collab-item-1': 'Executive Office of the UN Secretary-General',
          'collab-item-2': 'UK\'s Foreign, Commonwealth &amp; Development Office (FCDO)',
          'collab-item-3': 'Local Search Commissions and Attorney\'s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)',
          'collab-item-4': 'Colombian Search Unit',
          'collab-item-5': 'Mexico\'s National Search Commission',
          'collab-item-6': 'Mexican Science and Technology Secretariat',
          'collab-item-7': 'British Embassy in Mexico City',
          'collab-item-8': 'British Association for Forensic Anthropology',
          'collab-note-1': 'International collaboration',
          'collab-note-2': 'Policy, funding, and partnerships',
          'collab-note-3': 'Operational collaboration, policy impact',
          'collab-note-4': 'Casework and technical exchange',
          'collab-note-5': 'Casework and technical exchang',
          'collab-note-6': 'Funding, policy impact',
          'collab-note-7': 'Funding, Coordination support',
          'collab-note-8': 'Forensic expertise',
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
          'partners-title': 'Our Partners',
          'partners-intro': 'FOUND brings together a coalition of academic institutions, government bodies, civil society organisations, and international partners. Together, we seek to honour the memory of those who are missing and stand with families as they search for a form of closure.',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        },
        es: {
          'hero-tagline-static': 'Usando tecnología para&nbsp;',
          'word-1': 'dignificar.',
          'word-2': 'recordar.',
          'word-3': 'buscar.',
          'word-4': 'dar cierre.',
          'hero-main-text': '124,354 personas están registradas como desaparecidas en México. Detrás de cada caso hay una familia que busca respuestas. <strong>FOUND</strong> combina tecnología y saberes de familias buscadoras para buscar, localizar y promover cambios sistémicos.',
          'community-title': 'Impulsado por familias y comunidades de investigación',
          'community-text': 'FOUND está guiado e impulsado por <strong>colectivos de búsqueda</strong> y personas investigadoras de CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge y las Universidades Autónomas de Zacatecas y San Luis Potosí.',
          'collab-title': 'Colaboraciones institucionales',
          'collab-item-1': 'Oficina Ejecutiva del Secretario General de la ONU',
          'collab-item-2': 'Ministerio de Asuntos Exteriores, de la Mancomunidad y de Desarrollo del Reino Unido (FCDO)',
          'collab-item-3': 'Comisiones Locales de Búsqueda y Fiscalías de Jalisco, Zacatecas, San Luis Potosí y Chihuahua (México)',
          'collab-item-4': 'Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia',
          'collab-item-5': 'Comisión Nacional de Búsqueda de Personas de México',
          'collab-item-6': 'Secretaría de Ciencia y Tecnología de México',
          'collab-item-7': 'Embajada Británica en la Ciudad de México',
          'collab-item-8': 'Asociación Británica de Antropología Forense',
          'collab-note-1': 'Colaboración internacional',
          'collab-note-2': 'Política pública, financiamiento y alianzas',
          'collab-note-3': 'Colaboración operativa e impacto en políticas',
          'collab-note-4': 'Casos e intercambio técnico',
          'collab-note-5': 'Casos e intercambio técnico',
          'collab-note-6': 'Financiamiento, Política pública',
          'collab-note-7': 'Financiamiento, Colaboración operativa',
          'collab-note-8': 'Experiencia forense',
          'tech-title': 'Tecnologías en acción',
          'tech-item-1': 'Imágenes multiespectrales e hiperespectrales',
          'tech-item-2': 'LiDAR aerotransportado',
          'tech-item-3': 'Interferometría de ruido sísmico (TIRSA)',
          'tech-item-4': 'Tomografía de resistividad eléctrica y mediciones de conductividad',
          'tech-item-5': 'Análisis espectral satelital',
          'tech-item-6': 'Entomología y botánica forense, análisis territorial y ciencia del suelo',
          'buscadoras-title': 'El papel de las buscadoras',
          'buscadoras-text': 'Los colectivos de búsqueda están en el corazón del trabajo de FOUND. Estas familias han transformado la conversación nacional sobre desaparición y justicia. Sus prácticas de búsqueda, nacidas de la experiencia vivida, constituyen un saber forense fundamental. FOUND escucha, aprende e incorpora sus métodos en nuestros esfuerzos tecnológicos.',
          'social-title': 'Sigue nuestro camino',
          'social-subtitle': 'Mantente al tanto de nuestros hallazgos, las historias de las comunidades y nuestras colaboraciones.',
          'partners-title': 'Nuestras alianzas',
          'partners-intro': 'FOUND reúne una coalición de instituciones académicas, instancias gubernamentales, organizaciones de la sociedad civil y aliados internacionales. Trabajamos con un objetivo común: honrar la memoria de quienes nos faltan y acompañar a las familias en la búsqueda de una forma de cierre.',
          'footer-text': 'FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.'
        },
        nah: {
          'hero-tagline-static': 'Teknolojíayoh ika&nbsp;',
          'word-1': 'tlatepanita.',
          'word-2': 'quilnamictia.',
          'word-3': 'temoa.',
          'word-4': 'yolpakilistli quimacatia.',
          'hero-main-text': '124,354 tlācameh tlahcuilōlmeh quen polīhuihqueh ipan Mēxihco. Ipan sesen inin caso cah se familia tlatehuía tlanemilistli. <strong>FOUND</strong> quimixnextia teknolojíayoh huan tlamatiliztli in familias buscadoras para momachtia, quitemoa, quipantlalia huan quinemililia tlanemilistli yancuic ipan sistema.',
          'community-title': 'In familias huan tlamachtianimeh quinyecana',
          'community-text': 'FOUND quinyecanah huan quinyolchicahua <strong>colectivos de búsqueda</strong> huan tlamachtianimeh de CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge huan Universidades Autónomas de Zacatecas huan San Luis Potosí.',
          'collab-title': 'Tlen tlatlanecuiltilis nemilistli (colaboraciones institucionales)',
          'collab-item-1': 'Oficina Ejecutiva del Secretario General de la ONU',
          'collab-item-2': 'Foreign, Commonwealth &amp; Development Office (FCDO) tlen Reino Unido',
          'collab-item-3': 'Comisiones Locales de Búsqueda huan Fiscalías de Jalisco, Zacatecas, San Luis Potosí huan Chihuahua (México)',
          'collab-item-4': 'Unidad de Búsqueda de Personas dadas por Desaparecidas de Colombia',
          'collab-item-5': 'Comisión Nacional de Búsqueda de Personas de México',
          'collab-item-6': 'Secretaría de Ciencia y Tecnología de México',
          'collab-item-7': 'Embajada Británica ipan Ciudad de México',
          'collab-item-8': 'Asociación Británica de Antropología Forense',
          'collab-note-1': 'Colaboración internacional',
          'collab-note-2': 'Política pública, financiamiento huan alianzas',
          'collab-note-3': 'Colaboración operativa huan impacto ipan políticas',
          'collab-note-4': 'Casos huan intercambio técnico',
          'collab-note-5': 'Coordinación nacional',
          'collab-note-6': 'Colaboración ipan ciencia huan tecnología',
          'collab-note-7': 'Acompañamiento diplomático',
          'collab-note-8': 'Experiencia forense',
          'tech-title': 'Teknolojíayoh tlen motequiti',
          'tech-item-1': 'Imágenes multiespectrales huan hiperespectrales',
          'tech-item-2': 'LiDAR ipan aire',
          'tech-item-3': 'Interferometría de ruido sísmico (TIRSA)',
          'tech-item-4': 'Tomografía de resistividad eléctrica huan medisión de conductividad',
          'tech-item-5': 'Análisis espectral satelital',
          'tech-item-6': 'Entomología huan botánica forense, análisis de tlalli huan territorio',
          'buscadoras-title': 'In papel in buscadoras',
          'buscadoras-text': 'In colectivoh de buscadoras cah ipan yollotl in tequitl tlen FOUND. Yehuan quipatlaqueh in tlajtol ipan país tlen polihuiliztli huan tlayectlaliz justice. Inintequiti tlen temoa, tlen tlapanextia de inin nemilistli, mochihua se tlamatiliztli forense huecapan. FOUND quincaca, momachtia huan quincalaquia inintequiti ipan inin teknológicoh tequitl.',
          'social-title': 'Xiquito in totlanejmachtiliz',
          'social-subtitle': 'Ximoyetkixtia inin tlen tipantlaliah, tlen tlanechicoliztli in comunidades huan inin tlen timocoyonaltiah san sejco.',
          'partners-title': 'Tochan tlacamachtiloyan huan tocnihhuan',
          'partners-intro': 'FOUND quitlalia san sejco tlacamachtiloyan, tlatocayotl tlen gobierno, organizaciones de la sociedad civil huan tocnihhuan internacionales. San sejco titequitiyah para tlachihua tlatlepanittacayotl in aquin polihuihqueh huan para timochicahualtia in familias tlen quitemoah se tlayolpakilistli.',
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

        try { localStorage.setItem('found-lang', lang); } catch (e) {}
      }

      document.addEventListener('DOMContentLoaded', function() {
        let savedLang = null;
        try { savedLang = localStorage.getItem('found-lang'); } catch (e) {}
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
