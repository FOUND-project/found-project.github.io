---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---

<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FOUND — Media & Talks</title>
  <meta name="description" content="Media coverage and talks about FOUND's work in using technology to search for Mexico's disappeared.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <style>
    :root {
      /* Primary green palette - inspired by foliage */
      --primary-green: #1B5E3E;
      --primary-green-rgb: 27, 94, 62;
      --primary-green-dark: #0F3A26;
      --primary-green-light: #2D7A52;
      --primary-green-soft: #E8F5EF;
      
      /* Secondary greens */
      --secondary-green: #4A8C73;
      --accent-green: #6BBF9A;
      --moss-green: #3D5B50;
      --sage-green: #8AAE9D;
      
      /* Supporting colors */
      --gold-accent: #C9A959;
      --gold-accent-rgb: 201, 169, 89;
      --white: #FFFFFF;
      --off-white: #FAFDFA;
      --gray-50: #F8FAF9;
      --gray-100: #F1F5F3;
      --gray-200: #E5ECE8;
      --gray-700: #37423D;
      --gray-900: #121615;
      
      /* Shadows */
      --shadow-xs: 0 1px 2px rgba(15, 41, 31, 0.05);
      --shadow-sm: 0 2px 8px rgba(15, 41, 31, 0.08);
      --shadow-md: 0 6px 20px rgba(15, 41, 31, 0.12);
      --shadow-lg: 0 12px 32px rgba(15, 41, 31, 0.18);
      --shadow-glow: 0 0 32px rgba(43, 140, 87, 0.15);
      
      /* Transitions */
      --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
      --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
      --transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
      
      /* Border radius */
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 24px;
      --radius-2xl: 32px;
      --radius-pill: 9999px;
      
      /* Typography */
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      --font-serif: 'Georgia', serif;
    }

    /* Dark theme */
    [data-theme="dark"] {
      --primary-green: #2D9D6B;
      --primary-green-dark: #1B5E3E;
      --primary-green-light: #4AC18E;
      --primary-green-soft: rgba(42, 157, 107, 0.12);
      
      --white: #0D1412;
      --off-white: #111A17;
      --gray-50: #15201C;
      --gray-100: #1A2621;
      --gray-200: #24312C;
      --gray-700: #BAC7C1;
      --gray-900: #E9EFEC;
      
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 6px 20px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.45);
    }

    /* Reset and base */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    @media (prefers-reduced-motion: reduce) {
      html {
        scroll-behavior: auto;
      }
      
      *,
      *::before,
      *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }

    body {
      font-family: var(--font-sans);
      background: linear-gradient(135deg, var(--gray-50) 0%, var(--off-white) 100%);
      color: var(--gray-900);
      line-height: 1.6;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      padding: 2rem 1.5rem;
      position: relative;
      overflow-x: hidden;
    }

    body::before {
      content: '';
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: 
        radial-gradient(circle at 10% 20%, rgba(var(--primary-green-rgb), 0.04) 0%, transparent 50%),
        radial-gradient(circle at 90% 80%, rgba(var(--gold-accent-rgb), 0.03) 0%, transparent 50%);
      pointer-events: none;
      z-index: -1;
    }

    /* Override Minimal Mistakes defaults */
    .page,
    #main,
    .initial-content,
    .page__inner-wrap,
    .page__content,
    .archive {
      max-width: none !important;
      width: 100% !important;
    }

    /* Focus styles */
    *:focus-visible {
      outline: 3px solid var(--accent-green);
      outline-offset: 2px;
      border-radius: var(--radius-sm);
    }

    /* Container */
    .media-container {
      max-width: 1400px;
      margin: 0 auto;
      position: relative;
    }

    /* Header controls */
    .header-controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2.5rem;
      flex-wrap: wrap;
      gap: 1rem;
      padding: 0.75rem 0;
      border-bottom: 1px solid var(--gray-200);
    }

    .theme-toggle {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .theme-btn {
      background: var(--gray-100);
      border: 1px solid var(--gray-200);
      color: var(--gray-700);
      padding: 0.5rem 1rem;
      border-radius: var(--radius-pill);
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-base);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .theme-btn:hover {
      background: var(--gray-200);
      transform: translateY(-1px);
    }

    .theme-btn.active {
      background: var(--primary-green);
      color: var(--white);
      border-color: var(--primary-green);
    }

    .theme-btn svg {
      width: 16px;
      height: 16px;
    }

    .lang-toggle {
      display: flex;
      gap: 0.5rem;
      background: var(--gray-100);
      padding: 0.25rem;
      border-radius: var(--radius-pill);
      border: 1px solid var(--gray-200);
    }

    .lang-btn {
      padding: 0.5rem 1.25rem;
      border: none;
      background: transparent;
      color: var(--gray-700);
      font-size: 0.875rem;
      font-weight: 600;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all var(--transition-base);
    }

    .lang-btn:hover {
      background: var(--gray-200);
    }

    .lang-btn.active {
      background: var(--primary-green);
      color: var(--white);
    }

    /* Main header */
    .main-header {
      margin-bottom: 3rem;
      position: relative;
    }

    .header-decoration {
      position: absolute;
      top: -20px;
      left: -20px;
      width: 120px;
      height: 120px;
      background: radial-gradient(circle, var(--primary-green-soft) 0%, transparent 70%);
      z-index: -1;
      opacity: 0.7;
    }

    .category-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1.25rem;
      background: var(--primary-green);
      color: var(--white);
      border-radius: var(--radius-pill);
      font-size: 0.875rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }

    .category-pill::before {
      content: '';
      width: 6px;
      height: 6px;
      background: var(--white);
      border-radius: 50%;
    }

    h1 {
      font-size: clamp(2.5rem, 5vw, 3.5rem);
      font-weight: 800;
      line-height: 1.1;
      color: var(--primary-green-dark);
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
      max-width: 800px;
    }

    .subtitle {
      font-size: clamp(1.125rem, 2vw, 1.25rem);
      color: var(--gray-700);
      max-width: 800px;
      margin-bottom: 2rem;
      line-height: 1.6;
    }

    /* Filters */
    .media-filters {
      margin: 0 0 3rem;
    }

    .filter-group {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .filter-btn {
      padding: 0.625rem 1.5rem;
      background: var(--gray-100);
      border: 1px solid var(--gray-200);
      color: var(--gray-700);
      border-radius: var(--radius-pill);
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-base);
    }

    .filter-btn:hover {
      background: var(--gray-200);
    }

    .filter-btn.active {
      background: var(--primary-green);
      color: var(--white);
      border-color: var(--primary-green);
    }

    /* Media grid */
    .media-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 2rem;
      margin-bottom: 4rem;
    }

    .media-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--gray-200);
      transition: all var(--transition-base);
      height: 100%;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .media-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, var(--primary-green) 0%, var(--accent-green) 100%);
      transform: scaleX(0);
      transform-origin: left;
      transition: transform var(--transition-base);
    }

    .media-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-lg);
      border-color: var(--primary-green-light);
    }

    .media-card:hover::before {
      transform: scaleX(1);
    }

    .card-content {
      padding: 1.75rem;
      flex: 1;
      display: flex;
      flex-direction: column;
    }

    .media-outlet {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--primary-green);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: 1rem;
    }

    .media-outlet::before {
      content: '●';
      font-size: 0.5rem;
    }

    .media-title {
      font-size: 1.125rem;
      font-weight: 600;
      color: var(--gray-900);
      line-height: 1.4;
      margin-bottom: 1.25rem;
      flex: 1;
    }

    .media-link {
      text-decoration: none;
      color: inherit;
    }

    .media-link:hover .media-title {
      color: var(--primary-green);
    }

    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: auto;
      padding-top: 1.25rem;
      border-top: 1px solid var(--gray-200);
    }

    .media-tag {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.375rem 0.875rem;
      background: var(--primary-green-soft);
      color: var(--primary-green);
      border-radius: var(--radius-pill);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .external-link {
      opacity: 0;
      transform: translateX(-10px);
      transition: all var(--transition-base);
      color: var(--primary-green);
    }

    .media-card:hover .external-link {
      opacity: 1;
      transform: translateX(0);
    }

    /* Talks section */
    .talks-section {
      margin-top: 4rem;
      padding-top: 3rem;
      border-top: 1px solid var(--gray-200);
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2.5rem;
    }

    h2 {
      font-size: 2rem;
      font-weight: 700;
      color: var(--primary-green-dark);
      letter-spacing: -0.01em;
    }

    .talks-grid {
      display: grid;
      gap: 1.5rem;
    }

    .talk-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--gray-200);
      transition: all var(--transition-base);
      position: relative;
      overflow: hidden;
    }

    .talk-card::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 4px;
      background: linear-gradient(to bottom, var(--primary-green) 0%, var(--accent-green) 100%);
      transform: scaleY(0);
      transform-origin: bottom;
      transition: transform var(--transition-base);
    }

    .talk-card:hover {
      transform: translateX(4px);
      box-shadow: var(--shadow-md);
    }

    .talk-card:hover::before {
      transform: scaleY(1);
    }

    .talk-meta {
      font-size: 0.875rem;
      color: var(--primary-green);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .talk-meta::before {
      content: '▶';
      font-size: 0.75rem;
    }

    .talk-title {
      font-size: 1.125rem;
      font-weight: 600;
      color: var(--gray-900);
      line-height: 1.4;
      margin-bottom: 0.75rem;
    }

    .talk-link {
      text-decoration: none;
      color: inherit;
    }

    .talk-link:hover .talk-title {
      color: var(--primary-green);
    }

    .talk-description {
      color: var(--gray-700);
      font-size: 0.9375rem;
      line-height: 1.5;
    }

    /* Footer */
    .page-footer {
      margin-top: 5rem;
      padding-top: 3rem;
      border-top: 1px solid var(--gray-200);
      text-align: center;
      color: var(--gray-700);
      font-size: 0.875rem;
    }

    .footer-links {
      display: flex;
      justify-content: center;
      gap: 2rem;
      margin-top: 1rem;
    }

    .footer-link {
      color: var(--primary-green);
      text-decoration: none;
      font-weight: 600;
    }

    .footer-link:hover {
      text-decoration: underline;
    }

    /* Responsive */
    @media (max-width: 768px) {
      body {
        padding: 1.5rem 1rem;
      }
      
      .header-controls {
        flex-direction: column;
        align-items: stretch;
      }
      
      .theme-toggle {
        justify-content: center;
      }
      
      .lang-toggle {
        justify-content: center;
      }
      
      .media-grid {
        grid-template-columns: 1fr;
      }
      
      .filter-group {
        justify-content: center;
      }
      
      .section-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
      }
    }

    @media (max-width: 480px) {
      .card-content {
        padding: 1.25rem;
      }
      
      .talk-card {
        padding: 1.25rem;
      }
      
      h1 {
        font-size: 2rem;
      }
      
      h2 {
        font-size: 1.5rem;
      }
    }

    /* Print styles */
    @media print {
      body {
        padding: 0;
        background: white;
      }
      
      .header-controls,
      .theme-btn,
      .lang-btn,
      .filter-btn,
      .external-link {
        display: none;
      }
      
      .media-card,
      .talk-card {
        break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ddd;
      }
    }
  </style>
</head>
<body>
  <div class="media-container">
    <!-- Header controls -->
    <div class="header-controls">
      <div class="theme-toggle">
        <button class="theme-btn active" data-theme="light">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 7a5 5 0 1 0 5 5 5 5 0 0 0-5-5z"/>
          </svg>
          Light
        </button>
        <button class="theme-btn" data-theme="dark">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 3a9 9 0 1 0 9 9 9 9 0 0 0-9-9z"/>
          </svg>
          Dark
        </button>
      </div>
      
      <div class="lang-toggle">
        <button class="lang-btn active" data-lang="en">EN</button>
        <button class="lang-btn" data-lang="es">ES</button>
        <button class="lang-btn" data-lang="nah">NÁHUATL</button>
      </div>
    </div>

    <!-- Main header -->
    <header class="main-header">
      <div class="header-decoration"></div>
      
      <div class="category-pill" id="media-pill">
        MEDIA • COVERAGE • TALKS
      </div>
      
      <h1 id="media-title">Media Coverage</h1>
      
      <p class="subtitle" id="media-intro">
        Our research and humanitarian work has been featured in leading international publications, 
        highlighting the intersection of technology and human rights in the search for Mexico's disappeared.
      </p>
    </header>

    <!-- Filters -->
    <div class="media-filters">
      <div class="filter-group">
        <button class="filter-btn active" data-filter="all">All Media</button>
        <button class="filter-btn" data-filter="international">International</button>
        <button class="filter-btn" data-filter="mexican">Mexican Media</button>
        <button class="filter-btn" data-filter="academic">Academic</button>
      </div>
    </div>

    <!-- Media grid -->
    <div class="media-grid" id="media-grid">
      <!-- Cards will be populated by JavaScript -->
    </div>

    <!-- Talks section -->
    <section class="talks-section">
      <div class="section-header">
        <h2 id="talks-title">Talks & Presentations</h2>
      </div>
      
      <div class="talks-grid" id="talks-grid">
        <!-- Talks will be populated by JavaScript -->
      </div>
    </section>

    <!-- Footer -->
    <footer class="page-footer">
      <p>FOUND — Using technology to search, remember, dignify, find, and bring closure.</p>
      <div class="footer-links">
        <a href="https://found-project.org" class="footer-link">Home</a>
        <a href="https://github.com/found-project" class="footer-link">GitHub</a>
        <a href="mailto:contact@found-project.org" class="footer-link">Contact</a>
      </div>
    </footer>
  </div>

  <script>
    // Data layer - separating content from presentation
    const mediaData = {
      en: {
        header: {
          category: 'MEDIA • COVERAGE • TALKS',
          title: 'Media Coverage',
          subtitle: 'Our research and humanitarian work has been featured in leading international publications, highlighting the intersection of technology and human rights in the search for Mexico\'s disappeared.'
        },
        filters: {
          all: 'All Media',
          international: 'International',
          mexican: 'Mexican Media',
          academic: 'Academic'
        },
        tags: {
          article: 'Article',
          tv: 'TV Segment',
          opinion: 'Opinion',
          social: 'Social Media'
        },
        talks: {
          title: 'Talks & Presentations'
        },
        footer: {
          text: 'FOUND — Using technology to search, remember, dignify, find, and bring closure.'
        }
      },
      es: {
        header: {
          category: 'MEDIOS • COBERTURA • CHARLAS',
          title: 'Cobertura en Medios',
          subtitle: 'Nuestro trabajo de investigación y humanitario ha sido destacado en publicaciones internacionales líderes, resaltando la intersección entre tecnología y derechos humanos en la búsqueda de desaparecidos en México.'
        },
        filters: {
          all: 'Todos',
          international: 'Internacional',
          mexican: 'Medios Mexicanos',
          academic: 'Académico'
        },
        tags: {
          article: 'Artículo',
          tv: 'Segmento TV',
          opinion: 'Opinión',
          social: 'Redes Sociales'
        },
        talks: {
          title: 'Charlas y Presentaciones'
        },
        footer: {
          text: 'FOUND — Usando tecnología para buscar, recordar, dignificar, encontrar y dar cierre.'
        }
      },
      nah: {
        header: {
          category: 'MEDIOS • TLAYEKOLIZTLI • TLAHTOLMEH',
          title: 'Tlayekoliztli ipan Medios',
          subtitle: 'Tonemilistli huan totlatequi yokinextijkeh ipan miek medios tlen weyi tlaltikpak, kitemokaua in teknoloia huan tlakamikilistli ipan temoliztli tlen miktlantekitkeh ipan Mexico.'
        },
        filters: {
          all: 'Nochi',
          international: 'Internacional',
          mexican: 'Medios Mexicanos',
          academic: 'Tlamachtiloyan'
        },
        tags: {
          article: 'Tlahtolli',
          tv: 'TV Sektsiōn',
          opinion: 'Tlamachtiliztli',
          social: 'Redes Sociales'
        },
        talks: {
          title: 'Tlahtolmeh huan Presentaciones'
        },
        footer: {
          text: 'FOUND — Teknoloia para temoa, ilnamikia, tenamiktilia, kiteki huan patlamiki.'
        }
      }
    };

    const articles = [
      {
        id: 1,
        outlet: 'The Guardian',
        title: 'How dead pigs are helping in the search for missing victims of Mexico\'s drug wars',
        url: 'https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims',
        tags: ['article'],
        category: 'international',
        date: '2025-11-19'
      },
      {
        id: 2,
        outlet: 'Associated Press',
        title: 'Why are scientists dressing pigs in clothes and burying them in Mexico?',
        url: 'https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86',
        tags: ['article'],
        category: 'international',
        date: '2025-07-29'
      },
      {
        id: 3,
        outlet: 'Associated Press',
        title: 'Ciencia, tecnología y cerdos. México experimenta nuevas formas de buscar a los desaparecidos',
        url: 'https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e',
        tags: ['article'],
        category: 'international',
        language: 'es',
        date: '2025-07-29'
      },
      {
        id: 4,
        outlet: 'Science',
        title: 'Satellites could reveal the secret burial grounds of Mexico\'s murder victims',
        url: 'https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims',
        tags: ['article'],
        category: 'academic',
        date: '2024-03-28'
      },
      {
        id: 5,
        outlet: 'El País',
        title: 'Mexico\'s Izaguirre ranch: "High concentrations of ash" suggest the presence of clandestine crematoriums',
        url: 'https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html',
        tags: ['article'],
        category: 'international',
        date: '2025-03-28'
      },
      {
        id: 6,
        outlet: 'El País',
        title: '"Altas concentraciones de ceniza" y humo de gasolina: los indicios que apuntan a que en el rancho de Teuchitlán hubo crematorios clandestinos',
        url: 'https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html',
        tags: ['article'],
        category: 'international',
        language: 'es',
        date: '2025-03-28'
      },
      {
        id: 7,
        outlet: 'Animal Político',
        title: 'Con tecnología y drones, investigadores y familias de desaparecidos encuentran fosas clandestinas en Jalisco',
        url: 'https://www.animalpolitico.com/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia',
        tags: ['article'],
        category: 'mexican',
        language: 'es',
        date: '2024-12-18'
      },
      {
        id: 8,
        outlet: 'TV Azteca',
        title: 'Tecnología contra las desapariciones en México',
        url: 'https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas',
        tags: ['tv'],
        category: 'mexican',
        language: 'es',
        date: '2024-11-15'
      },
      {
        id: 9,
        outlet: 'Reuters',
        title: 'In Mexico, mothers of the missing turn to drones to look for unmarked graves',
        url: 'https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/',
        tags: ['article'],
        category: 'international',
        date: '2024-01-26'
      },
      {
        id: 10,
        outlet: 'VICE',
        title: 'Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims',
        url: 'https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/',
        tags: ['article'],
        category: 'international',
        date: '2025-08-12'
      },
      {
        id: 11,
        outlet: 'Los Angeles Times',
        title: 'Why are scientists dressing pigs in clothes and burying them in Mexico?',
        url: 'https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico',
        tags: ['article'],
        category: 'international',
        date: '2025-07-29'
      },
      {
        id: 12,
        outlet: 'The Independent',
        title: 'How pigs could help find missing Mexican drug cartel victims',
        url: 'https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html',
        tags: ['article'],
        category: 'international',
        date: '2025-08-01'
      },
      {
        id: 13,
        outlet: 'NBC News',
        title: 'Clothed pigs are buried in Mexico as scientists use them in search of missing',
        url: 'https://www.nbcnews.com/news/amp/rcna221791',
        tags: ['article'],
        category: 'international',
        date: '2025-08-05'
      },
      {
        id: 14,
        outlet: 'WIRED',
        title: 'Cómo la tecnología geoespacial expone el horror de las fosas clandestinas en México',
        url: 'https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico',
        tags: ['article'],
        category: 'international',
        language: 'es',
        date: '2024-04-22'
      },
      {
        id: 15,
        outlet: 'Animal Político',
        title: 'Interpretar la naturaleza para encontrar a quienes nos faltan',
        url: 'https://animalpolitico.com/analisis/invitades/libro-madres-buscadoras-fil',
        tags: ['opinion'],
        category: 'mexican',
        language: 'es',
        date: '2024-11-30'
      },
      {
        id: 16,
        outlet: 'CGTN America',
        title: 'Jalisco mothers search for hidden graves with drones',
        url: 'https://twitter.com/cgtnamerica/status/1751362286118150555',
        tags: ['social'],
        category: 'international',
        date: '2024-01-26'
      },
      {
        id: 17,
        outlet: 'SinEmbargo',
        title: 'Tecnología para hallarlos',
        url: 'https://www.sinembargo.mx/18-12-2023/4440515',
        tags: ['article'],
        category: 'mexican',
        language: 'es',
        date: '2023-12-18'
      }
    ];

    const talks = [
      {
        id: 1,
        venue: 'University of Oxford / Oxford Festival of the Arts',
        title: 'Disappearance of Worlds | Art Exhibition & Dialogues on Disappearance',
        url: 'https://www.ox.ac.uk/event/technological-responses-disappearance',
        date: '2024-06-15',
        type: 'exhibition'
      },
      {
        id: 2,
        venue: 'British Association for Forensic Anthropology (BAFA)',
        title: 'Interpreting nature to locate the disappeared: influencing search practices in Jalisco, Mexico',
        url: 'https://bafauk.weebly.com/winter-conference--agm-2024.html',
        date: '2024-11-22',
        type: 'conference'
      },
      {
        id: 3,
        venue: 'Guadalajara International Book Fair (FIL)',
        title: 'Presentan Interpretar la naturaleza para encontrar a quienes nos faltan',
        url: 'https://jalisco.quadratin.com.mx/principal/presentan-interpretar-la-naturaleza-para-encontrar-a-quienes-nos-faltan/',
        date: '2024-11-30',
        type: 'presentation'
      },
      {
        id: 4,
        venue: 'University of Oxford',
        title: 'Mexico\'s Missing: How families and technology are working together',
        url: 'https://www.ox.ac.uk/event/mexicos-missing-how-families-and-technology-are-working-together',
        date: '2024-02-10',
        type: 'lecture'
      }
    ];

    class MediaPage {
      constructor() {
        this.currentLang = 'en';
        this.currentTheme = 'light';
        this.currentFilter = 'all';
        this.init();
      }

      init() {
        this.setupEventListeners();
        this.loadPreferences();
        this.renderPage();
      }

      setupEventListeners() {
        // Theme toggle
        document.querySelectorAll('[data-theme]').forEach(btn => {
          btn.addEventListener('click', (e) => {
            this.setTheme(e.target.dataset.theme);
          });
        });

        // Language toggle
        document.querySelectorAll('[data-lang]').forEach(btn => {
          btn.addEventListener('click', (e) => {
            this.setLanguage(e.target.dataset.lang);
          });
        });

        // Filter buttons
        document.querySelectorAll('[data-filter]').forEach(btn => {
          btn.addEventListener('click', (e) => {
            this.setFilter(e.target.dataset.filter);
          });
        });
      }

      loadPreferences() {
        // Load saved preferences
        try {
          const savedLang = localStorage.getItem('found-lang-media');
          const savedTheme = localStorage.getItem('found-theme');
          
          if (savedLang && ['en', 'es', 'nah'].includes(savedLang)) {
            this.currentLang = savedLang;
          }
          
          if (savedTheme && ['light', 'dark'].includes(savedTheme)) {
            this.currentTheme = savedTheme;
          }
        } catch (e) {
          console.log('Could not load preferences:', e);
        }
      }

      setTheme(theme) {
        this.currentTheme = theme;
        document.documentElement.setAttribute('data-theme', theme);
        
        // Update button states
        document.querySelectorAll('[data-theme]').forEach(btn => {
          btn.classList.toggle('active', btn.dataset.theme === theme);
        });
        
        // Save preference
        try {
          localStorage.setItem('found-theme', theme);
        } catch (e) {
          console.log('Could not save theme preference:', e);
        }
      }

      setLanguage(lang) {
        this.currentLang = lang;
        this.renderPage();
        
        // Update button states
        document.querySelectorAll('[data-lang]').forEach(btn => {
          btn.classList.toggle('active', btn.dataset.lang === lang);
        });
        
        // Save preference
        try {
          localStorage.setItem('found-lang-media', lang);
        } catch (e) {
          console.log('Could not save language preference:', e);
        }
      }

      setFilter(filter) {
        this.currentFilter = filter;
        this.renderArticles();
        
        // Update button states
        document.querySelectorAll('[data-filter]').forEach(btn => {
          btn.classList.toggle('active', btn.dataset.filter === filter);
        });
      }

      renderPage() {
        this.renderHeader();
        this.renderArticles();
        this.renderTalks();
        this.renderFooter();
      }

      renderHeader() {
        const langData = mediaData[this.currentLang];
        
        document.getElementById('media-pill').textContent = langData.header.category;
        document.getElementById('media-title').textContent = langData.header.title;
        document.getElementById('media-intro').textContent = langData.header.subtitle;
        document.getElementById('talks-title').textContent = langData.talks.title;
        
        // Update filter buttons
        document.querySelectorAll('[data-filter]').forEach(btn => {
          const filter = btn.dataset.filter;
          if (langData.filters[filter]) {
            btn.textContent = langData.filters[filter];
          }
        });
      }

      renderArticles() {
        const grid = document.getElementById('media-grid');
        const langData = mediaData[this.currentLang];
        
        // Filter articles
        const filteredArticles = this.currentFilter === 'all' 
          ? articles 
          : articles.filter(article => article.category === this.currentFilter);
        
        // Sort by date (newest first)
        filteredArticles.sort((a, b) => new Date(b.date) - new Date(a.date));
        
        grid.innerHTML = filteredArticles.map(article => `
          <article class="media-card" data-category="${article.category}">
            <a class="media-link" href="${article.url}" target="_blank" rel="noopener noreferrer">
              <div class="card-content">
                <div class="media-outlet">${article.outlet}</div>
                <h3 class="media-title">${article.title}</h3>
                <div class="card-footer">
                  <span class="media-tag">${langData.tags[article.tags[0]] || langData.tags.article}</span>
                  <span class="external-link">→</span>
                </div>
              </div>
            </a>
          </article>
        `).join('');
      }

      renderTalks() {
        const grid = document.getElementById('talks-grid');
        const langData = mediaData[this.currentLang];
        
        // Sort talks by date (newest first)
        const sortedTalks = [...talks].sort((a, b) => new Date(b.date) - new Date(a.date));
        
        grid.innerHTML = sortedTalks.map(talk => `
          <article class="talk-card">
            <a class="talk-link" href="${talk.url}" target="_blank" rel="noopener noreferrer">
              <div class="talk-meta">${talk.venue}</div>
              <h3 class="talk-title">${talk.title}</h3>
              <p class="talk-description">
                ${this.formatDate(talk.date, this.currentLang)}
              </p>
            </a>
          </article>
        `).join('');
      }

      renderFooter() {
        const langData = mediaData[this.currentLang];
        const footer = document.querySelector('.page-footer p');
        if (footer) {
          footer.textContent = langData.footer.text;
        }
      }

      formatDate(dateString, lang) {
        const date = new Date(dateString);
        const options = { 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric' 
        };
        
        if (lang === 'es') {
          return date.toLocaleDateString('es-ES', options);
        } else if (lang === 'nah') {
          // Simple fallback for Nahuatl
          return date.toLocaleDateString('en-US', options);
        }
        
        return date.toLocaleDateString('en-US', options);
      }
    }

    // Initialize the page when DOM is loaded
    document.addEventListener('DOMContentLoaded', () => {
      new MediaPage();
    });
  </script>
</body>
</html>
