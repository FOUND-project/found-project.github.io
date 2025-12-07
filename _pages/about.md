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

    /* Language Toggle Styles - FIXED POSITIONING */
    .language-toggle {
      position: fixed;
      top: 2.5rem; /* Increased from 1.5rem */
      right: clamp(1rem, 4vw, 3rem);
      z-index: 1000;
      display: flex;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-radius: 50px;
      padding: 0.5rem;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border-light);
      transition: all 0.3s var(--transition-smooth);
    }

    .language-toggle:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
    }

    .lang-btn {
      padding: 0.6rem 1.2rem;
      border: none;
      border-radius: 50px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.3s var(--transition-smooth);
      background: transparent;
      color: var(--text-medium);
    }

    .lang-btn.active {
      background: var(--primary-green);
      color: white;
      box-shadow: 0 2px 8px rgba(45, 95, 77, 0.2);
    }

    .lang-btn:hover:not(.active) {
      background: var(--accent-green);
      color: var(--primary-green);
    }

    .lang-btn.es {
      min-width: 85px;
    }

    /* Content visibility based on language */
    .lang-en {
      display: block;
    }

    .lang-es {
      display: none;
    }

    body.spanish .lang-en {
      display: none;
    }

    body.spanish .lang-es {
      display: block;
    }

    /* Language-specific animations */
    .word-carousel.es {
      min-width: clamp(220px, 35vw, 350px);
    }

    /* ENHANCED TITLE SECTION - Now full width */
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
      margin-top: 1rem; /* Added space for the button */
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

    .title-accent {
      color: var(--gold-accent);
      font-weight: 700;
    }

    /* Hero Section - Now wider */
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

    /* Hero Image */
    .hero-image-container {
      width: 100%;
      max-width: 1100px; /* Increased from 900px */
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

    /* Content Sections - Now wider */
    .content-section {
      padding: clamp(2.5rem, 5vw, 4rem) clamp(1rem, 4vw, 3rem);
      border-bottom: 1px solid var(--border-light);
      scroll-margin-top: 2rem;
    }

    .content-section:last-of-type {
      border-bottom: none;
    }

    .section-container {
      max-width: 1400px;
      margin: 0 auto;
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

    /* ENHANCED & COMPACT Info Lists - Now wider */
    .info-list {
      list-style: none;
      padding-left: 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); /* Increased from 300px */
      gap: 0.75rem 2rem; /* Increased horizontal gap */
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

    /* Enhanced Image Galleries - Now wider */
    .image-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); /* Increased from 280px */
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

    /* Social Media Section - Now wider */
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

    .social-container {
      max-width: 1600px; /* Increased from 1400px */
      margin: 0 auto;
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
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 400px), 1fr)); /* Increased from 350px */
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
      max-width: 600px; /* Increased from 550px */
      overflow: hidden;
      border-radius: 16px;
    }

    .iframe-container iframe {
      width: 100%;
      border: 0;
      display: block;
    }

    /* Enhanced Partners Section - Now wider */
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

    .partners-container {
      max-width: 1600px; /* Increased */
      margin: 0 auto;
    }

    .partners-intro {
      text-align: center;
      max-width: 1000px; /* Increased from 900px */
      margin: 0 auto 4rem;
      color: var(--text-medium);
      font-size: clamp(1.1rem, 2.5vw, 1.3rem);
      line-height: 1.8;
    }

    /* ENHANCED PARTNER GRID - Bigger logos and wider */
    .partner-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr)); /* Increased from 240px */
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
      min-height: 200px; /* Increased from 180px */
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
      min-height: 220px; /* Increased from 200px */
    }

    /* Buscadoras Special Section - Now wider */
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
      max-width: 1100px; /* Increased from 900px */
      margin: 0 auto;
      text-align: center;
    }

    .buscadoras-image {
      max-width: 600px; /* Increased from 500px */
      margin: 3rem auto;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      transition: transform 0.6s var(--transition-smooth);
    }

    .buscadoras-image:hover {
      transform: translateY(-8px);
    }

    /* Footer - Now wider */
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

    .footer-content {
      max-width: 1400px;
      margin: 0 auto;
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
        grid-template-columns: repeat(auto-fill, minmax(min(100%, 220px), 1fr));
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
        grid-template-columns: repeat(auto-fill, minmax(min(100%, 180px), 1fr));
        gap: 1.25rem;
      }

      .partner-logo {
        padding: 1.5rem;
        min-height: 160px; /* Adjusted for mobile */
      }

      .partner-logo:nth-child(2),
      .partner-logo:nth-child(3),
      .partner-logo:nth-child(4),
      .partner-logo:nth-child(5) {
        min-height: 180px; /* Adjusted for mobile */
      }

      .info-list {
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }
      
      .info-list li {
        padding: 0.5rem 0 0.5rem 2rem;
        min-height: 38px;
      }
      
      .hero,
      .content-section,
      .social-section,
      .partners-section,
      .buscadoras-section,
      .footer {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
      }

      .language-toggle {
        top: 1.5rem; /* Adjusted for mobile */
        right: 1.5rem;
      }
      
      .project-title {
        margin-top: 1.5rem; /* More space for button on mobile */
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
        min-height: 140px;
      }
      
      .title-section {
        padding: 3rem 1rem 2rem; /* Adjusted top padding */
      }
      
      .project-title {
        font-size: 2.2rem;
        margin-top: 1.5rem; /* More space for button */
      }
      
      .project-subtitle {
        font-size: 1.2rem;
      }
      
      .hero,
      .content-section,
      .social-section,
      .partners-section,
      .buscadoras-section,
      .footer {
        padding-left: 1rem;
        padding-right: 1rem;
      }

      .language-toggle {
        top: 1rem;
        right: 1rem;
        padding: 0.3rem;
      }

      .lang-btn {
        padding: 0.5rem 0.8rem;
        font-size: 0.8rem;
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
      
      .language-toggle {
        display: none !important;
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
  <!-- Language Toggle Button - NOW VISIBLE -->
  <div class="language-toggle">
    <button class="lang-btn en active" onclick="switchLanguage('en')">ENGLISH</button>
    <button class="lang-btn es" onclick="switchLanguage('es')">ESPAÑOL</button>
  </div>

  <!-- ENHANCED TITLE SECTION -->
  <section class="title-section">
    <h1 class="project-title">FOUND</h1>
    <p class="project-subtitle">
      <span class="title-accent lang-en">Interpretar la Naturaleza</span>
      <span class="title-accent lang-es">Interpretar la Naturaleza</span>
      <span class="lang-en">para Encontrar a Quienes nos Faltan</span>
      <span class="lang-es">para Encontrar a Quienes nos Faltan</span>
    </p>
  </section>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-content">
      <div class="animated-tagline">
        <span class="lang-en">Using technology to&nbsp;</span>
        <span class="lang-es">Usando tecnología para&nbsp;</span>
        <div class="word-carousel en" role="text" aria-label="Rotating tagline">
          <ul class="word-list">
            <li>dignify.</li>
            <li>remember.</li>
            <li>search.</li>
            <li>bring closure.</li>
          </ul>
        </div>
        <div class="word-carousel es" role="text" aria-label="Rotating tagline">
          <ul class="word-list">
            <li>dignificar.</li>
            <li>recordar.</li>
            <li>buscar.</li>
            <li>dar consuelo.</li>
          </ul>
        </div>
      </div>

      <p class="hero-description lang-en">
        Over 120,000 persons are reported as disappeared in Mexico. Behind each case there is a family searching for answers. <strong>FOUND</strong> combines technology and grassroots knowledge to search, locate and drive systemic change.
      </p>
      <p class="hero-description lang-es">
        Más de 120,000 personas están reportadas como desaparecidas en México. Detrás de cada caso hay una familia buscando respuestas. <strong>FOUND</strong> combina tecnología y conocimiento comunitario para buscar, localizar e impulsar cambios sistémicos.
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
    <div class="section-container">
      <div class="section-header">
        <h2 class="lang-en"><span>Driven by Families and Research Communities</span></h2>
        <h2 class="lang-es"><span>Impulsado por Familias y Comunidades de Investigación</span></h2>
      </div>
      <p class="hero-description lang-en">
        FOUND is guided and motivated by <strong>search collectives</strong> and researchers from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.
      </p>
      <p class="hero-description lang-es">
        FOUND es guiado y motivado por <strong>colectivos de búsqueda</strong> e investigadores del CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, y las Universidades Autónomas de Zacatecas y San Luis Potosí.
      </p>
    </div>
  </section>

  <!-- Institutional Collaborations -->
  <section class="content-section" id="collaborations">
    <div class="section-container">
      <h2 class="lang-en">Institutional Collaborations</h2>
      <h2 class="lang-es">Colaboraciones Institucionales</h2>
      
      <ul class="info-list lang-en">
        <li>Executive Office of the UN Secretary-General</li>
        <li>UK's Foreign, Commonwealth & Development Office (FCDO)</li>
        <li>Local Search Commissions and Attorney's Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li>
        <li>Colombian Search Unit</li>
        <li>Mexico's National Search Commission</li>
        <li>Mexican Science and Technology Secretariat</li>
        <li>British Embassy in Mexico City</li>
        <li>British Association for Forensic Anthropology</li>
      </ul>
      
      <ul class="info-list lang-es">
        <li>Oficina Ejecutiva del Secretario General de la ONU</li>
        <li>Oficina de Relaciones Exteriores, Commonwealth y Desarrollo del Reino Unido (FCDO)</li>
        <li>Comisiones Locales de Búsqueda y Fiscalías de Jalisco, Zacatecas, San Luis Potosí y Chihuahua (México)</li>
        <li>Unidad de Búsqueda de Personas Dadas por Desaparecidas de Colombia</li>
        <li>Comisión Nacional de Búsqueda de México</li>
        <li>Secretaría de Ciencia y Tecnología de México</li>
        <li>Embajada Británica en la Ciudad de México</li>
        <li>Asociación Británica de Antropología Forense</li>
      </ul>
    </div>
  </section>

  <!-- Technologies Section -->
  <section class="content-section" id="technologies">
    <div class="section-container">
      <h2 class="lang-en">Technologies in Action</h2>
      <h2 class="lang-es">Tecnologías en Acción</h2>
      
      <ul class="info-list lang-en">
        <li>Multispectral & Hyperspectral Imaging</li>
        <li>Airborne LiDAR</li>
        <li>Seismic Noise Interferometry (TIRSA)</li>
        <li>Electrical Resistivity Tomography, Conductivimetry Measurements</li>
        <li>Satellite Spectral Analysis</li>
        <li>Forensic Entomology, Botany, Territorial Analysis, Soil Science</li>
      </ul>
      
      <ul class="info-list lang-es">
        <li>Imágenes Multiespectrales e Hiperspectrales</li>
        <li>LiDAR Aéreo</li>
        <li>Interferometría de Ruido Sísmico (TIRSA)</li>
        <li>Tomografía de Resistividad Eléctrica, Mediciones de Conductividad</li>
        <li>Análisis Espectral por Satélite</li>
        <li>Entomología Forense, Botánica, Análisis Territorial, Ciencias del Suelo</li>
      </ul>

      <div class="image-gallery">
        <!-- Gallery items remain the same (images don't need translation) -->
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

  <!-- Buscadoras Section -->
  <section class="buscadoras-section" id="buscadoras">
    <div class="buscadoras-content">
      <h2 class="lang-en">The Role of Buscadoras</h2>
      <h2 class="lang-es">El Papel de las Buscadoras</h2>
      
      <p class="hero-description lang-en">
        Women-led collectives are at the heart of FOUND's work. They have reshaped the national conversation on disappearance and justice. Their search practices, born from lived experience, are vital forensic knowledge. FOUND listens, learns, and incorporates their methods into our technological efforts.
      </p>
      <p class="hero-description lang-es">
        Los colectivos liderados por mujeres están en el corazón del trabajo de FOUND. Han transformado la conversación nacional sobre desaparición y justicia. Sus prácticas de búsqueda, nacidas de la experiencia vivida, son conocimiento forense vital. FOUND escucha, aprende e incorpora sus métodos en nuestros esfuerzos tecnológicos.
      </p>
      
      <div class="buscadoras-image">
        <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/plant%20hands.jpeg?raw=true" alt="Buscadoras hands with plants symbolizing hope and remembrance" loading="lazy" class="loading" onload="this.classList.remove('loading')">
      </div>
    </div>
  </section>

  <!-- Social Media Section -->
  <section class="social-section" id="social">
    <div class="social-container">
      <h2 class="section-title lang-en">Follow Our Journey</h2>
      <h2 class="section-title lang-es">Sigue Nuestro Recorrido</h2>
      
      <p class="section-subtitle lang-en">Stay connected with our latest findings, community stories, and collaborative efforts</p>
      <p class="section-subtitle lang-es">Mantente conectado con nuestros últimos hallazgos, historias comunitarias y esfuerzos colaborativos</p>

      <div class="social-grid">
        <!-- Social media embeds remain the same (they display in their original language) -->
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

  <!-- Enhanced Partners Section -->
  <section class="partners-section" id="partners">
    <div class="partners-container">
      <h2 class="section-title lang-en">Our Partners</h2>
      <h2 class="section-title lang-es">Nuestros Socios</h2>
      
      <p class="partners-intro lang-en">
        FOUND brings together an exceptional coalition of academic institutions, government agencies, civil society organizations, and international partners. Together, we work toward a common goal: bringing dignity and closure to families searching for their loved ones.
      </p>
      <p class="partners-intro lang-es">
        FOUND reúne una coalición excepcional de instituciones académicas, agencias gubernamentales, organizaciones de la sociedad civil y socios internacionales. Juntos, trabajamos hacia un objetivo común: brindar dignidad y consuelo a las familias que buscan a sus seres queridos.
      </p>

      <div class="partner-grid">
        <!-- Partner logos remain the same -->
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
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-content">
      <em class="lang-en">FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
      <em class="lang-es">FOUND: Interpretar la Naturaleza para Encontrar a Quienes nos Faltan.</em>
    </div>
  </footer>

  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

  <script>
    // Language switching functionality
    function switchLanguage(lang) {
      // Update body class
      document.body.classList.remove('english', 'spanish');
      document.body.classList.add(lang === 'es' ? 'spanish' : 'english');
      
      // Update button states
      document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.classList.contains(lang)) {
          btn.classList.add('active');
        }
      });
      
      // Save preference to localStorage
      localStorage.setItem('preferred-language', lang);
      
      // Update meta tags for SEO
      if (lang === 'es') {
        document.documentElement.lang = 'es';
        document.title = 'Proyecto FOUND - Usando Tecnología para Buscar y Recordar';
        document.querySelector('meta[name="description"]').content = 'FOUND combina tecnología y conocimiento comunitario para buscar personas desaparecidas en México, brindando dignidad y consuelo a las familias.';
        document.querySelector('meta[property="og:title"]').content = 'Proyecto FOUND - Usando Tecnología para Buscar y Recordar';
        document.querySelector('meta[property="og:description"]').content = 'Más de 120,000 personas están reportadas como desaparecidas en México. FOUND combina tecnología y conocimiento comunitario para buscar, localizar e impulsar cambios sistémicos.';
      } else {
        document.documentElement.lang = 'en';
        document.title = 'FOUND Project - Using Technology to Search and Remember';
        document.querySelector('meta[name="description"]').content = 'FOUND combines technology and grassroots knowledge to search for disappeared persons in Mexico, bringing dignity and closure to families.';
        document.querySelector('meta[property="og:title"]').content = 'FOUND Project - Using Technology to Search and Remember';
        document.querySelector('meta[property="og:description"]').content = 'Over 120,000 persons are reported as disappeared in Mexico. FOUND combines technology and grassroots knowledge to search, locate and drive systemic change.';
      }
    }

    // Initialize language based on user preference or browser language
    document.addEventListener('DOMContentLoaded', function() {
      const savedLang = localStorage.getItem('preferred-language');
      const browserLang = navigator.language.startsWith('es') ? 'es' : 'en';
      const defaultLang = savedLang || browserLang;
      
      switchLanguage(defaultLang);
      
      // Add smooth transition for language switching
      document.body.style.transition = 'opacity 0.3s ease';
    });
  </script>
</body>
</html>
