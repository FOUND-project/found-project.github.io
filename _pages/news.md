---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FOUND — News & Updates</title>
  
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
      min-height: 100vh;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    /* Header */
    .news-header {
      background: linear-gradient(135deg, #ffffff 0%, #f8faf8 100%);
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
    }

    /* News Grid */
    .news-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 2rem;
      margin-bottom: 3rem;
    }

    /* News Cards */
    .news-card {
      background: white;
      border-radius: 16px;
      padding: 2rem;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
      border: 1px solid rgba(0, 0, 0, 0.06);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
      position: relative;
      border-left: 5px solid #1b4d3e;
    }

    .news-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
      border-left-color: #2d7a5f;
    }

    .news-card.active {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 90%;
      max-width: 800px;
      max-height: 85vh;
      overflow-y: auto;
      z-index: 1000;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
      animation: popIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    @keyframes popIn {
      from {
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.9);
      }
      to {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
      }
    }

    .news-card.active:hover {
      transform: translate(-50%, -50%);
    }

    /* Overlay */
    .overlay {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 999;
      backdrop-filter: blur(4px);
    }

    .overlay.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    /* Close Button */
    .close-btn {
      position: absolute;
      top: 1rem;
      right: 1rem;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #f0f0f0;
      border: none;
      cursor: pointer;
      font-size: 1.5rem;
      color: #1b4d3e;
      display: none;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
      z-index: 10;
    }

    .news-card.active .close-btn {
      display: flex;
    }

    .close-btn:hover {
      background: #1b4d3e;
      color: white;
      transform: rotate(90deg);
    }

    /* Card Content */
    .card-emoji {
      font-size: 2.5rem;
      margin-bottom: 1rem;
      display: block;
    }

    .card-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: #1b4d3e;
      line-height: 1.4;
      margin-bottom: 1rem;
      letter-spacing: -0.01em;
    }

    .card-preview {
      color: #666;
      line-height: 1.6;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .news-card.active .card-preview {
      display: none;
    }

    .card-content {
      display: none;
      margin-top: 1.5rem;
      color: #333;
      line-height: 1.7;
    }

    .news-card.active .card-content {
      display: block;
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
    }

    .share-item:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(27, 77, 62, 0.15);
      background: linear-gradient(135deg, #ffffff 0%, #f0f4f0 100%);
    }

    .share-item .icon {
      font-size: 1.5rem;
    }

    /* Toast */
    #toast {
      position: fixed;
      bottom: 40px;
      right: 40px;
      background: linear-gradient(135deg, #1b4d3e 0%, #2d7a5f 100%);
      color: white;
      padding: 1rem 1.5rem;
      border-radius: 12px;
      font-weight: 600;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
      z-index: 9999;
      box-shadow: 0 8px 32px rgba(27, 77, 62, 0.4);
    }

    #toast.show {
      opacity: 1;
    }

    /* Responsive */
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

      .news-card.active {
        width: 95%;
        max-height: 90vh;
        padding: 1.5rem;
      }

      .card-title {
        font-size: 1.2rem;
      }

      .share-wrapper {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
      }

      #toast {
        bottom: 20px;
        right: 20px;
        left: 20px;
        text-align: center;
      }
    }
  </style>
</head>
<body>
  <div class="overlay" id="overlay"></div>
  
  <div class="container">
    <!-- Header -->
    <div class="news-header">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true" alt="FOUND Logo">
      <div>
        <h1>FOUND — News & Updates</h1>
        <p>Latest developments on our work across Mexico, Colombia, and beyond.</p>
      </div>
    </div>

    <!-- News Grid -->
    <div class="news-grid">
      <!-- Card 1 -->
      <div class="news-card" data-id="ubpd-visit">
        <button class="close-btn">×</button>
        <span class="card-emoji">🇨🇴🇲🇽</span>
        <h2 class="card-title">Second Visit of Colombia's Search Unit for Missing Persons (UBPD) to FOUND's Experimental Sites in Jalisco</h2>
        <p class="card-preview">We welcomed Héctor Javier Gómez, geophysicist from Colombia's UBPD, for a joint field deployment to FOUND's experimental sites in Jalisco...</p>
        
        <div class="card-content">
          <p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p>
          
          <p>We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia's <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND's experimental sites in Jalisco.</p>
          
          <p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND's experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p>
          
          <p>It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p>
          
          <p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND's detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD's team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND's partner states in Mexico.</p>
          
          <div class="share-wrapper">
            <span class="share-label">Share this update:</span>
            <div class="share-buttons">
              <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#ubpd-visit" target="_blank">
                <span class="icon">🔗</span>
                <span>LinkedIn</span>
              </a>
              <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#ubpd-visit" target="_blank">
                <span class="icon">🐦</span>
                <span>Twitter</span>
              </a>
              <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#ubpd-visit" target="_blank">
                <span class="icon">💬</span>
                <span>WhatsApp</span>
              </a>
              <span class="share-item copy-link" data-url="https://found-project.github.io/news/#ubpd-visit">
                <span class="icon">📋</span>
                <span>Copy</span>
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="news-card" data-id="guardian">
        <button class="close-btn">×</button>
        <span class="card-emoji">📄</span>
        <h2 class="card-title">FOUND is in The Guardian</h2>
        <p class="card-preview">This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist's in-person visit to our experimental sites...</p>
        
        <div class="card-content">
          <p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist's in-person visit to our experimental sites in Jalisco, Mexico. We are deeply grateful for the care, depth and commitment brought to this story after months spent listening to families, researchers and officials.</p>
          
          <p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank">📖 Read the article here</a></p>
          
          <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true" alt="FOUND in The Guardian">
          
          <div class="share-wrapper">
            <span class="share-label">Share this update:</span>
            <div class="share-buttons">
              <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#guardian" target="_blank">
                <span class="icon">🔗</span>
                <span>LinkedIn</span>
              </a>
              <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#guardian" target="_blank">
                <span class="icon">🐦</span>
                <span>Twitter</span>
              </a>
              <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#guardian" target="_blank">
                <span class="icon">💬</span>
                <span>WhatsApp</span>
              </a>
              <span class="share-item copy-link" data-url="https://found-project.github.io/news/#guardian">
                <span class="icon">📋</span>
                <span>Copy</span>
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="news-card" data-id="fcdo">
        <button class="close-btn">×</button>
        <span class="card-emoji">🇬🇧</span>
        <h2 class="card-title">FOUND has received new support from the UK's FCDO through the Frontier Tech Hub</h2>
        <p class="card-preview">In the pitch, our team showcased FOUND's impact to date, and we were awarded funding that will enable us to scale our mission...</p>
        
        <div class="card-content">
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
              <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#fcdo" target="_blank">
                <span class="icon">🔗</span>
                <span>LinkedIn</span>
              </a>
              <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#fcdo" target="_blank">
                <span class="icon">🐦</span>
                <span>Twitter</span>
              </a>
              <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#fcdo" target="_blank">
                <span class="icon">💬</span>
                <span>WhatsApp</span>
              </a>
              <span class="share-item copy-link" data-url="https://found-project.github.io/news/#fcdo">
                <span class="icon">📋</span>
                <span>Copy</span>
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="news-card" data-id="media-coverage">
        <button class="close-btn">×</button>
        <span class="card-emoji">📰</span>
        <h2 class="card-title">FOUND featured by Associated Press, The Independent, LA Times, VICE, NBC</h2>
        <p class="card-preview">Major international media outlets have covered FOUND's innovative work in Mexico...</p>
        
        <div class="card-content">
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
              <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#media-coverage" target="_blank">
                <span class="icon">🔗</span>
                <span>LinkedIn</span>
              </a>
              <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#media-coverage" target="_blank">
                <span class="icon">🐦</span>
                <span>Twitter</span>
              </a>
              <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#media-coverage" target="_blank">
                <span class="icon">💬</span>
                <span>WhatsApp</span>
              </a>
              <span class="share-item copy-link" data-url="https://found-project.github.io/news/#media-coverage">
                <span class="icon">📋</span>
                <span>Copy</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="toast">✓ Link copied!</div>

  <script>
    const overlay = document.getElementById('overlay');
    const toast = document.getElementById('toast');
    const cards = document.querySelectorAll('.news-card');

    // Open card on click
    cards.forEach(card => {
      card.addEventListener('click', (e) => {
        // Don't open if clicking on links, share buttons, or close button
        if (e.target.closest('a') || e.target.closest('.share-item') || e.target.closest('.close-btn')) {
          return;
        }
        
        card.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      });

      // Close button
      const closeBtn = card.querySelector('.close-btn');
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        closeCard();
      });
    });

    // Close on overlay click
    overlay.addEventListener('click', closeCard);

    // Close on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeCard();
      }
    });

    function closeCard() {
      cards.forEach(card => card.classList.remove('active'));
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }

    // Copy link functionality
    document.querySelectorAll('.copy-link').forEach(btn => {
      btn.addEventListener('click', async (e) => {
        e.stopPropagation();
        e.preventDefault();
        const url = btn.dataset.url;
        
        try {
          await navigator.clipboard.writeText(url);
          showToast();
        } catch (err) {
          // Fallback
          const textarea = document.createElement('textarea');
          textarea.value = url;
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand('copy');
          document.body.removeChild(textarea);
          showToast();
        }
      });
    });

    function showToast() {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2000);
    }

    // Open card from URL hash
    if (window.location.hash) {
      const id = window.location.hash.substring(1);
      const card = document.querySelector(`[data-id="${id}"]`);
      if (card) {
        setTimeout(() => {
          card.classList.add('active');
          overlay.classList.add('active');
          document.body.style.overflow = 'hidden';
        }, 100);
      }
    }
  </script>
</body>
</html>
