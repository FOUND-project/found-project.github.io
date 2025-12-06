---
layout: archive
title: "In media and talks"
permalink: /media/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Media Coverage</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      background: #fafafa;
      padding: 3rem 2rem;
      line-height: 1.6;
    }

    .container {
      max-width: 1400px;
      margin: 0 auto;
      background: white;
      padding: 3rem;
      border-radius: 16px;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
    }

    h1 {
      font-size: 2.5rem;
      font-weight: 700;
      color: #1a1a1a;
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }

    .section-intro {
      font-size: 1.1rem;
      color: #666;
      margin-bottom: 3rem;
      line-height: 1.6;
    }

    .media-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin: 3rem 0 4rem;
    }

    .media-card {
      background: #ffffff;
      border-radius: 12px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1px solid rgba(0, 0, 0, 0.06);
      position: relative;
      overflow: hidden;
    }
    
    .media-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 0;
      background: linear-gradient(180deg, #1b4d3e 0%, #2d7a5f 100%);
      transition: height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .media-card:hover::before {
      height: 100%;
    }

    .media-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
      border-color: rgba(27, 77, 62, 0.15);
    }

    .media-outlet {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-weight: 700;
      color: #1b4d3e;
      margin-bottom: 0.75rem;
      display: inline-block;
    }

    .media-title {
      font-size: 1.05rem;
      font-weight: 600;
      color: #1a1a1a;
      margin: 0 0 1rem 0;
      line-height: 1.5;
      letter-spacing: -0.01em;
    }

    .media-link {
      text-decoration: none;
      color: inherit;
      display: block;
      height: 100%;
    }

    .media-link:hover .media-title {
      color: #1b4d3e;
    }

    .media-tag {
      display: inline-block;
      margin-top: auto;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      background: rgba(27, 77, 62, 0.08);
      color: #1b4d3e;
      transition: all 0.2s ease;
    }
    
    .media-card:hover .media-tag {
      background: rgba(27, 77, 62, 0.12);
    }

    .talks-section {
      margin-top: 4rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }
    
    .talks-section h2 {
      font-size: 1.75rem;
      font-weight: 700;
      color: #1a1a1a;
      margin-bottom: 1.5rem;
      letter-spacing: -0.02em;
    }

    .talk-card {
      background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
      padding: 1.5rem 1.75rem;
      border-radius: 10px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1px solid rgba(0, 0, 0, 0.06);
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
      background: linear-gradient(180deg, #1b4d3e 0%, #2d7a5f 100%);
      transform: scaleY(0);
      transform-origin: bottom;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .talk-card:hover {
      transform: translateX(4px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
      border-color: rgba(27, 77, 62, 0.2);
    }
    
    .talk-card:hover::before {
      transform: scaleY(1);
      transform-origin: top;
    }

    .talk-title {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.5rem;
      color: #1b4d3e;
    }

    .talk-link {
      font-size: 1.05rem;
      text-decoration: none;
      color: #1a1a1a;
      font-weight: 600;
      line-height: 1.4;
      letter-spacing: -0.01em;
      display: inline-block;
      transition: color 0.2s ease;
    }

    .talk-link:hover {
      color: #1b4d3e;
    }

    @media (max-width: 768px) {
      body {
        padding: 1rem;
      }

      .container {
        padding: 1.5rem;
      }

      h1 {
        font-size: 2rem;
      }

      .media-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Media Coverage</h1>
    <p class="section-intro">Our research and work has been featured in leading international publications.</p>

    <div class="media-grid">
      <!-- The Guardian -->
      <article class="media-card">
        <a class="media-link" href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">The Guardian</div>
            <h3 class="media-title">How dead pigs are helping in the search for missing victims of Mexico's drug wars</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- Associated Press (EN) -->
      <article class="media-card">
        <a class="media-link" href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Associated Press</div>
            <h3 class="media-title">Why are scientists dressing pigs in clothes and burying them in Mexico?</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- Associated Press (ES) -->
      <article class="media-card">
        <a class="media-link" href="https://apnews.com/article/mexico-desaparecidos-busqueda-ciencia-tecnologia-dron-92f74132a9a5035b73795181a1023d1e" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Associated Press</div>
            <h3 class="media-title">Ciencia, tecnología y cerdos. México experimenta nuevas formas de buscar a los desaparecidos</h3>
            <span class="media-tag">Artículo</span>
          </div>
        </a>
      </article>

      <!-- Independent -->
      <article class="media-card">
        <a class="media-link" href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">The Independent</div>
            <h3 class="media-title">How pigs could help find missing Mexican drug cartel victims</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- VICE -->
      <article class="media-card">
        <a class="media-link" href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">VICE</div>
            <h3 class="media-title">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- Los Angeles Times -->
      <article class="media-card">
        <a class="media-link" href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Los Angeles Times</div>
            <h3 class="media-title">Why are scientists dressing pigs in clothes and burying them in Mexico?</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- NBC News -->
      <article class="media-card">
        <a class="media-link" href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">NBC News</div>
            <h3 class="media-title">Clothed pigs are buried in Mexico as scientists use them in search of missing</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- Animal Político -->
      <article class="media-card">
        <a class="media-link" href="https://www.animalpolitico.com/sociedad/familias-desaparecidos-fosas-clandestinas-jalisco-tecnologia" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Animal Político</div>
            <h3 class="media-title">Con tecnología y drones, investigadores y familias de desaparecidos encuentran fosas clandestinas en Jalisco</h3>
            <span class="media-tag">Artículo</span>
          </div>
        </a>
      </article>

      <!-- Science -->
      <article class="media-card">
        <a class="media-link" href="https://www.science.org/content/article/satellites-could-reveal-secret-burial-grounds-mexico-s-murder-victims" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Science</div>
            <h3 class="media-title">Satellites could reveal the secret burial grounds of Mexico's murder victims</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- WIRED -->
      <article class="media-card">
        <a class="media-link" href="https://es.wired.com/articulos/tecnologia-geoespacial-expone-el-horror-de-las-fosas-clandestinas-en-mexico" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">WIRED (ES)</div>
            <h3 class="media-title">Cómo la tecnología geoespacial expone el horror de las fosas clandestinas en México</h3>
            <span class="media-tag">Artículo</span>
          </div>
        </a>
      </article>

      <!-- El País (EN) -->
      <article class="media-card">
        <a class="media-link" href="https://english.elpais.com/international/2025-03-28/mexicos-izaguirre-ranch-high-concentrations-of-ash-suggest-the-presence-of-clandestine-crematoriums.html" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">El País (EN)</div>
            <h3 class="media-title">Mexico's Izaguirre ranch: 'High concentrations of ash' suggest the presence of clandestine crematoriums</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- El País (ES) -->
      <article class="media-card">
        <a class="media-link" href="https://elpais.com/mexico/2025-03-28/altas-concentraciones-de-ceniza-y-humo-de-gasolina-los-indicios-que-apuntan-a-que-en-el-rancho-de-teuchitlan-hubo-crematorios-clandestinos.html" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">El País</div>
            <h3 class="media-title">"Altas concentraciones de ceniza" y humo de gasolina: los indicios que apuntan a que en el rancho de Teuchitlán hubo crematorios clandestinos</h3>
            <span class="media-tag">Artículo</span>
          </div>
        </a>
      </article>

      <!-- TV Azteca -->
      <article class="media-card">
        <a class="media-link" href="https://www.tvazteca.com/aztecanoticias/tecnologia-drones-desapariciones-mexico-fosas-clandestinas" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">TV Azteca</div>
            <h3 class="media-title">Tecnología contra las desapariciones en México</h3>
            <span class="media-tag">TV segment</span>
          </div>
        </a>
      </article>

      <!-- Animal Político (opinion) -->
      <article class="media-card">
        <a class="media-link" href="https://animalpolitico.com/analisis/invitades/libro-madres-buscadoras-fil" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Animal Político</div>
            <h3 class="media-title">Interpretar la naturaleza para encontrar a quienes nos faltan</h3>
            <span class="media-tag">Opinion</span>
          </div>
        </a>
      </article>

      <!-- Reuters -->
      <article class="media-card">
        <a class="media-link" href="https://www.reuters.com/world/americas/mexico-mothers-missing-turn-drones-look-unmarked-graves-2024-01-26/" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">Reuters</div>
            <h3 class="media-title">In Mexico, mothers of the missing turn to drones to look for unmarked graves</h3>
            <span class="media-tag">Article</span>
          </div>
        </a>
      </article>

      <!-- CGTN America -->
      <article class="media-card">
        <a class="media-link" href="https://twitter.com/cgtnamerica/status/1751362286118150555" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">CGTN America</div>
            <h3 class="media-title">Jalisco mothers search for hidden graves with drones</h3>
            <span class="media-tag">TV / Social</span>
          </div>
        </a>
      </article>

      <!-- SinEmbargo -->
      <article class="media-card">
        <a class="media-link" href="https://www.sinembargo.mx/18-12-2023/4440515" target="_blank" rel="noopener">
          <div>
            <div class="media-outlet">SinEmbargo</div>
            <h3 class="media-title">Tecnología para hallarlos</h3>
            <span class="media-tag">Artículo</span>
          </div>
        </a>
      </article>
    </div>

    <div class="talks-section">
      <h2>Talks</h2>

      <div class="talk-card">
        <div class="talk-title">University of Oxford / Oxford Festival of the Arts</div>
        <a class="talk-link" href="https://www.ox.ac.uk/event/technological-responses-disappearance" target="_blank" rel="noopener">
          Disappearance of Worlds | Art Exhibition & Dialogues on Disappearance
        </a>
      </div>

      <div class="talk-card">
        <div class="talk-title">British Association for Forensic Anthropology (BAFA)</div>
        <a class="talk-link" href="https://bafauk.weebly.com/winter-conference--agm-2024.html" target="_blank" rel="noopener">
          Interpreting nature to locate the disappeared: influencing search practices in Jalisco, Mexico
        </a>
      </div>

      <div class="talk-card">
        <div class="talk-title">Guadalajara International Book Fair (FIL)</div>
        <a class="talk-link" href="https://jalisco.quadratin.com.mx/principal/presentan-interpretar-la-naturaleza-para-encontrar-a-quienes-nos-faltan/" target="_blank" rel="noopener">
          Presentan Interpretar la naturaleza para encontrar a quienes nos faltan
        </a>
      </div>

      <div class="talk-card">
        <div class="talk-title">University of Oxford</div>
        <a class="talk-link" href="https://www.ox.ac.uk/event/mexicos-missing-how-families-and-technology-are-working-together" target="_blank" rel="noopener">
          Mexico's Missing: How families and technology are working together
        </a>
      </div>
    </div>
  </div>
</body>
</html>
