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
  
  <!-- Open Graph Metadata -->
  <meta property="og:title" content="FOUND — News & Updates">
  <meta property="og:description" content="Latest developments from FOUND across Mexico, Colombia, and beyond.">
  <meta property="og:image" content="https://found-project.github.io/images/found-logo.png">
  <meta property="og:url" content="https://found-project.github.io/news/">
  <meta property="og:type" content="website">
  
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
      padding: 3rem 2rem;
      line-height: 1.6;
      color: #1a1a1a;
    }

    .container {
      max-width: 1000px;
      margin: 0 auto;
    }

    /* Header Section */
    .news-header {
      background: linear-gradient(135deg, #ffffff 0%, #f8faf8 100%);
      border-radius: 16px;
      padding: 2.5rem;
      margin-bottom: 3rem;
      display: flex;
      align-items: center;
      gap: 2rem;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
      border: 1px solid rgba(27, 77, 62, 0.1);
      position: relative;
      overflow: hidden;
    }

    .news-header::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 5px;
      background: linear-gradient(180deg, #1b4d3e 0%, #2d7a5f 100%);
    }

    .news-header img {
      width: 100px;
      height: auto;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }

    .news-header h1 {
      font-size: 2rem;
      color: #1b4d3e;
      font-weight: 700;
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }

    .news-header p {
      font-size: 1.1rem;
      color: #555;
      line-height: 1.5;
    }

    /* News Cards */
    .news-card {
      background: white;
      border-radius: 16px;
      padding: 2rem;
      margin-bottom: 2rem;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
      border: 1px solid rgba(0, 0, 0, 0.06);
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }

    .news-card::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 5px;
      background: linear-gradient(180deg, #1b4d3e 0%, #2d7a5f 100%);
      transform: scaleY(0.3);
      transform-origin: top;
      transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .news-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
      border-color: rgba(27, 77, 62, 0.2);
    }

    .news-card:hover::before {
      transform: scaleY(1);
    }

    .news-card.open {
      box-shadow: 0 8px 24px rgba(27, 77, 62, 0.15);
      border-color: rgba(27, 77, 62, 0.3);
    }

    .news-card.open::before {
      transform: scaleY(1);
    }

    .news-title {
      font-weight: 700;
      font-size: 1.35rem;
      color: #1b4d3e;
      line-height: 1.4;
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      letter-spacing: -0.01em;
    }

    .news-title .emoji {
      font-size: 1.5rem;
      flex-shrink: 0;
    }

    .expand-indicator {
      margin-left: auto;
      font-size: 1.2rem;
      color: #1b4d3e;
      transition: transform 0.3s ease;
      flex-shrink: 0;
    }

    .news-card.open .expand-indicator {
      transform: rotate(180deg);
    }

    .news-content {
      display: none;
      opacity: 0;
      transition: opacity 0.4s ease;
    }

    .news-card.open .news-content {
      display: block;
      opacity: 1;
      margin-top: 1.5rem;
      animation: slideDown 0.4s ease;
    }

    @keyframes slideDown {
      from {
        opacity: 0;
        transform: translateY(-10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .news-content p {
      margin-bottom: 1rem;
      line-height: 1.7;
      color: #333;
    }

    .news-content strong {
      color: #1b4d3e;
      font-weight: 600;
    }

    .news-content a {
      color: #1b4d3e;
      text-decoration: none;
      font-weight: 600;
      border-bottom: 2px solid transparent;
      transition: border-color 0.2s ease;
    }

    .news-content a:hover {
      border-bottom-color: #1b4d3e;
    }

    .news-content ul {
      margin: 1rem 0;
      padding-left: 1.5rem;
      line-height: 1.8;
    }

    .news-content ul li {
      margin-bottom: 0.5rem;
    }

    .news-content img {
      width: 100%;
      max-width: 700px;
      border-radius: 12px;
      margin: 1.5rem 0;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
      transition: transform 0.3s ease;
    }

    .news-content img:hover {
      transform: scale(1.02);
    }

    /* Share Section */
    .share-wrapper {
      margin-top: 2rem;
      padding-top: 1.5rem;
      border-top: 2px solid rgba(27, 77, 62, 0.1);
      display: flex;
      gap: 2rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .share-label {
      font-weight: 700;
      color: #1b4d3e;
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .share-buttons {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .share-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.3rem;
      padding: 0.75rem 1rem;
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      border-radius: 10px;
      color: #1b4d3e;
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
      border: 1px solid rgba(0, 0, 0, 0.06);
      position: relative;
    }

    .share-item:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(27, 77, 62, 0.15);
      background: linear-gradient(135deg, #ffffff 0%, #f0f4f0 100%);
      border-color: rgba(27, 77, 62, 0.2);
    }

    .share-item .icon {
      font-size: 1.5rem;
    }

    /* Copied Popup */
    #copied-popup {
      position: fixed;
      bottom: 40px;
      right: 40px;
      background: linear-gradient(135deg, #1b4d3e 0%, #2d7a5f 100%);
      color: white;
      padding: 1rem 1.5rem;
      border-radius: 12px;
      font-size: 1rem;
      font-weight: 600;
      opacity: 0;
      pointer-events: none;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      transform: translateY(20px) scale(0.9);
      z-index: 9999;
      box-shadow: 0 8px 32px rgba(27, 77, 62, 0.4);
    }

    #copied-popup.show {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    #copied-popup::before {
      content: '✓';
      margin-right: 0.5rem;
      font-weight: bold;
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

      .news-card {
        padding: 1.5rem;
      }

      .news-title {
        font-size: 1.15rem;
      }

      .share-wrapper {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
      }

      .share-buttons {
        width: 100%;
      }

      .share-item {
        flex: 1;
        min-width: 80px;
      }

      #copied-popup {
        bottom: 20px;
        right: 20px;
        left: 20px;
        text-align: center;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Header -->
    <div class="news-header">
      <img src="/images/Found_logo.jpg" alt="FOUND Logo">
      <div>
        <h1>FOUND — News & Updates</h1>
        <p>Latest developments on our work across Mexico, Colombia, and beyond.</p>
      </div>
    </div>

    <!-- Card 1: UBPD Visit -->
    <div class="news-card" id="ubpd-visit">
      <div class="news-title">
        <span class="emoji">🇨🇴🇲🇽</span>
        <span>Second Visit of Colombia's Search Unit for Missing Persons (UBPD) to FOUND's Experimental Sites in Jalisco</span>
        <span class="expand-indicator">▼</span>
      </div>
      
      <div class="news-content">
        <p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p>
        
        <p>We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia's <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND's experimental sites in Jalisco.</p>
        
        <p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND's experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p>
        
        <p>It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p>
        
        <p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND's detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD's team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND's partner states in Mexico.</p>
        
        <div class="share-wrapper">
          <span class="share-label">Share this update:</span>
          <div class="share-buttons">
            <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#ubpd-visit" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🔗</span>
              <span>LinkedIn</span>
            </a>
            <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#ubpd-visit" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🐦</span>
              <span>Twitter</span>
            </a>
            <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#ubpd-visit" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">💬</span>
              <span>WhatsApp</span>
            </a>
            <span class="share-item copy-link" data-share="https://found-project.github.io/news/#ubpd-visit" onclick="event.stopPropagation()">
              <span class="icon">📋</span>
              <span>Copy link</span>
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Card 2: The Guardian -->
    <div class="news-card" id="guardian">
      <div class="news-title">
        <span class="emoji">📄</span>
        <span>FOUND is in The Guardian</span>
        <span class="expand-indicator">▼</span>
      </div>
      
      <div class="news-content">
        <p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist's in-person visit to our experimental sites in Jalisco, Mexico. We are deeply grateful for the care, depth and commitment brought to this story after months spent listening to families, researchers and officials.</p>
        
        <p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank">📖 Read the article here</a></p>
        
        <img src="/images/Found_theGuardian.jpeg" alt="FOUND in The Guardian">
        
        <div class="share-wrapper">
          <span class="share-label">Share this update:</span>
          <div class="share-buttons">
            <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#guardian" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🔗</span>
              <span>LinkedIn</span>
            </a>
            <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#guardian" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🐦</span>
              <span>Twitter</span>
            </a>
            <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#guardian" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">💬</span>
              <span>WhatsApp</span>
            </a>
            <span class="share-item copy-link" data-share="https://found-project.github.io/news/#guardian" onclick="event.stopPropagation()">
              <span class="icon">📋</span>
              <span>Copy link</span>
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Card 3: FCDO Funding -->
    <div class="news-card" id="fcdo">
      <div class="news-title">
        <span class="emoji">🇬🇧</span>
        <span>FOUND has received new support from the UK's Foreign, Commonwealth and Development Office (FCDO) through the Frontier Tech Hub</span>
        <span class="expand-indicator">▼</span>
      </div>
      
      <div class="news-content">
        <p>In the pitch, our team showcased FOUND's impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.</p>
        
        <p><strong>🌱 Driven by families and research communities</strong><br>
        FOUND is guided and motivated by mothers' search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.</p>
        
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
        
        <p><strong>🛰️ Technology for memory, dignity, and closure</strong><br>
        We will continue developing — and embedding in official protocols — new ways to locate missing persons using advanced tools such as machine learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.</p>
        
        <p><em>FOUND: Interpreting Nature to Locate Those We Are Missing</em></p>
        
        <div class="share-wrapper">
          <span class="share-label">Share this update:</span>
          <div class="share-buttons">
            <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#fcdo" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🔗</span>
              <span>LinkedIn</span>
            </a>
            <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#fcdo" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🐦</span>
              <span>Twitter</span>
            </a>
            <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#fcdo" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">💬</span>
              <span>WhatsApp</span>
            </a>
            <span class="share-item copy-link" data-share="https://found-project.github.io/news/#fcdo" onclick="event.stopPropagation()">
              <span class="icon">📋</span>
              <span>Copy link</span>
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Card 4: Media Coverage -->
    <div class="news-card" id="media-coverage">
      <div class="news-title">
        <span class="emoji">📰</span>
        <span>FOUND featured by Associated Press, The Independent, LA Times, VICE, NBC</span>
        <span class="expand-indicator">▼</span>
      </div>
      
      <div class="news-content">
        <ul>
          <li><strong>Associated Press:</strong> <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
          <li><strong>The Independent:</strong> <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank">How pigs could help find missing Mexican drug cartel victims</a></li>
          <li><strong>LA Times:</strong> <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
          <li><strong>VICE:</strong> <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li>
          <li><strong>NBC:</strong> <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank">Clothed pigs are buried in Mexico as scientists use them in search of missing</a></li>
        </ul>
        
        <div class="share-wrapper">
          <span class="share-label">Share this update:</span>
          <div class="share-buttons">
            <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#media-coverage" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🔗</span>
              <span>LinkedIn</span>
            </a>
            <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#media-coverage" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">🐦</span>
              <span>Twitter</span>
            </a>
            <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#media-coverage" target="_blank" onclick="event.stopPropagation()">
              <span class="icon">💬</span>
              <span>WhatsApp</span>
            </a>
            <span class="share-item copy-link" data-share="https://found-project.github.io/news/#media-coverage" onclick="event.stopPropagation()">
              <span class="icon">📋</span>
              <span>Copy link</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Copied Popup -->
  <div id="copied-popup">Link copied!</div>

  <script>
    document.addEventListener("DOMContentLoaded", function () {
      // Expand/collapse cards
      document.querySelectorAll(".news-card").forEach(card => {
        card.addEventListener("click", function (e) {
          // Don't toggle if clicking on a link or share button
          if (e.target.closest("a") || e.target.closest(".share-item")) {
            return;
          }
          
          card.classList.toggle("open");
        });
      });

      // Copy link functionality
      const popup = document.getElementById("copied-popup");
      
      document.querySelectorAll(".copy-link").forEach(btn => {
        btn.addEventListener("click", async function (e) {
          e.stopPropagation();
          const link = btn.dataset.share;
          
          try {
            await navigator.clipboard.writeText(link);
            popup.classList.add("show");
            setTimeout(() => popup.classList.remove("show"), 2000);
          } catch (err) {
            console.error("Failed to copy:", err);
          }
        });
      });
    });
  </script>
</body>
</html>
