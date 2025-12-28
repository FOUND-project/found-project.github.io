---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FOUND — News & Updates</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
      padding: 3rem 2rem;
      line-height: 1.6;
      color: #1a1a1a;
      min-height: 100vh;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .news-header {
      background: white;
      border-radius: 16px;
      padding: 2.5rem;
      margin-bottom: 3rem;
      display: flex;
      align-items: center;
      gap: 2rem;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
      border-left: 5px solid #1b4d3e;
    }

    .news-header img {
      width: 100px;
      height: auto;
      border-radius: 12px;
    }

    .news-header h1 {
      font-size: 2rem;
      color: #1b4d3e;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }

    .news-header p {
      font-size: 1.1rem;
      color: #555;
    }

    .news-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 2rem;
    }

    .news-card {
      background: white;
      border-radius: 16px;
      padding: 2rem;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
      border: 1px solid rgba(0, 0, 0, 0.06);
      border-left: 5px solid #1b4d3e;
      transition: all 0.3s ease;
    }

    .news-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
    }

    .card-emoji {
      font-size: 2.5rem;
      display: block;
      margin-bottom: 1rem;
    }

    .expand-toggle {
      display: none;
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: start;
      gap: 1rem;
      cursor: pointer;
    }

    .card-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: #1b4d3e;
      line-height: 1.4;
      flex: 1;
    }

    .expand-icon {
      background: #1b4d3e;
      color: white;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      transition: all 0.3s ease;
      flex-shrink: 0;
      user-select: none;
    }

    .card-header:hover .expand-icon {
      background: #2d7a5f;
      transform: scale(1.1);
    }

    .expand-icon::before {
      content: '+';
    }

    .expand-toggle:checked ~ .card-header .expand-icon::before {
      content: '−';
    }

    .card-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.5s ease;
      color: #333;
      line-height: 1.7;
    }

    .expand-toggle:checked ~ .card-content {
      max-height: 5000px;
      margin-top: 1rem;
    }

    .card-content p {
      margin-bottom: 1rem;
    }

    .card-content strong {
      color: #1b4d3e;
      font-weight: 600;
    }

    .card-content a {
      color: #1b4d3e;
      text-decoration: none;
      font-weight: 600;
      border-bottom: 2px solid transparent;
      transition: border-color 0.2s ease;
    }

    .card-content a:hover {
      border-bottom-color: #1b4d3e;
    }

    .card-content ul {
      margin: 1rem 0;
      padding-left: 1.5rem;
    }

    .card-content ul li {
      margin-bottom: 0.5rem;
    }

    .card-content img {
      width: 100%;
      border-radius: 12px;
      margin: 1.5rem 0;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }

    @media (max-width: 768px) {
      body {
        padding: 1.5rem 1rem;
      }

      .news-header {
        flex-direction: column;
        align-items: flex-start;
        padding: 1.5rem;
      }

      .news-header h1 {
        font-size: 1.5rem;
      }

      .news-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
      }

      .card-title {
        font-size: 1.2rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="news-header">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true" alt="FOUND Logo">
      <div>
        <h1>FOUND — News & Updates</h1>
        <p>Latest developments on our work across Mexico, Colombia, and beyond.</p>
      </div>
    </div>

    <div class="news-grid">
    
      <!-- Card 0 -->
      <div class="news-card">
        <span class="card-emoji">🎖️</span>
        <input type="checkbox" id="card0" class="expand-toggle">
        <label for="card0" class="card-header">
          <span class="card-title">FOUND's Prioneer wins UK FCDO's Sir Nicholas Browne Policy and Expertise Award</span>
          <span class="expand-icon"></span>
        </label>
        <div class="card-content">
          <p>We are proud to share that <strong>Mariela Garfias</strong> has been awarded the <strong>Sir Nicholas Browne Policy and Expertise Award</strong>, a UK FCDO award recognising excellence in delivering policy objectives, selected from 200+ nominations.</p>
          <p>Mariela is FOUND’s FCDO pioneer and one of the people most responsible for the project’s impact.</p>
          <p>Through FOUND, and with the support of incredible partners, we have located 27 people who were victims of disappearance in <strong>Mexico</strong>, allowing families move towards answers, and a form of closure. Our work is now being embedded with local and national authorities, and has expanded to collaboration with the <strong>Colombian Search Unit</strong> and the Executive Office of the <strong>UN Secretary-General</strong>.</p>
          <p>In her acceptance speech, Mariela shared words that capture the spirit of FOUND: “From my decomposed body, flowers shall grow, and I am in them. That is eternity.” — Edvard Munch.</p>
          <p>When searching for clandestine graves using technologies, nature often bears witness — through subtle changes in soil and vegetation. Memory persists. Our responsibility is to find it.</p>
          <p>Mariela thanked those who carry this work with us: the British Embassy Mexico City Embassy in Mexico City, our mentor Martin Johnston, the Frontier Tech Hub team, and above all the searching mothers, whose knowledge and strength remain our compass.</p>
        </div>
      </div>

      <!-- Card 1 -->
      <div class="news-card">
        <span class="card-emoji">🇨🇴🇲🇽</span>
        <input type="checkbox" id="card1" class="expand-toggle">
        <label for="card1" class="card-header">
          <span class="card-title">Second Visit of Colombia's Search Unit for Missing Persons (UBPD) to FOUND's Experimental Sites in Jalisco</span>
          <span class="expand-icon"></span>
        </label>
        <div class="card-content">
          <p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p>
          <p>We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia's <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND's experimental sites in Jalisco.</p>
          <p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND's experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p>
          <p>It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p>
          <p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND's detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD's team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND's partner states in Mexico.</p>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="news-card">
        <span class="card-emoji">📄</span>
        <input type="checkbox" id="card2" class="expand-toggle">
        <label for="card2" class="card-header">
          <span class="card-title">FOUND is in The Guardian</span>
          <span class="expand-icon"></span>
        </label>
        <div class="card-content">
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND in The Guardian">
          <p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist's in-person visit to our experimental sites in Jalisco, Mexico. We are deeply grateful for the care, depth and commitment brought to this story after months spent listening to families, researchers and officials.</p>
          <p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank">📖 Read the article here</a></p>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="news-card">
        <span class="card-emoji">🇬🇧</span>
        <input type="checkbox" id="card3" class="expand-toggle">
        <label for="card3" class="card-header">
          <span class="card-title">FOUND has received new support from the UK's FCDO through the Frontier Tech Hub</span>
          <span class="expand-icon"></span>
        </label>
        <div class="card-content">
          <p>In the pitch, our team showcased FOUND's impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.</p>
          <p><strong>🌱 Driven by families and research communities</strong><br>FOUND is guided and motivated by mothers' search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.</p>
          <p><strong>🔍 We are now working directly with:</strong></p>
          <ul>
            <li>Executive Office of the UN Secretary-General</li>
            <li>UK's Foreign, Commonwealth & Development Office (FCDO)</li>
            <li>Local Search Commissions and Attorney's Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li>
            <li>Colombian Search Unit</li>
            <li>Mexico's National Search Commission</li>
            <li>Mexican Science and Technology Secretariat</li>
            <li>British Embassy in Mexico City</li>
            <li>British Association for Forensic Anthropology</li>
          </ul>
          <p><strong>🛰️ Technology for memory, dignity, and closure</strong><br>We will continue developing — and embedding in official protocols — new ways to locate missing persons using advanced tools such as machine learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.</p>
          <p><em>FOUND: Interpreting Nature to Locate Those We Are Missing</em></p>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="news-card">
        <span class="card-emoji">📰</span>
        <input type="checkbox" id="card4" class="expand-toggle">
        <label for="card4" class="card-header">
          <span class="card-title">FOUND featured by Associated Press, The Independent, LA Times, VICE, NBC</span>
          <span class="expand-icon"></span>
        </label>
        <div class="card-content">
          <ul>
            <li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
            <li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank">How pigs could help find missing Mexican drug cartel victims</a></li>
            <li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
            <li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li>
            <li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank">Clothed pigs are buried in Mexico as scientists use them in search of missing</a></li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</body>
</html>
