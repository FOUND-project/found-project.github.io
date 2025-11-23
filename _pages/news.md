---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---
<!-- ===========================
     NEWS CARDS STYLES
=========================== -->
<style>
  .news-card {
    border-left: 4px solid #1b4d3e;
    border-radius: 6px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    background-color: #f9f9f9;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    position: relative;
  }

  .news-card:hover {
    background-color: #eef6ee;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    cursor: pointer;
  }

  .news-title {
    font-weight: bold;
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
    color: #1b4d3e;
  }

  .news-content {
    display: none;
    line-height: 1.6;
    font-size: 1rem;
    color: #333;
  }

  .news-card.open .news-content {
    display: block;
    margin-top: 1rem;
  }

  .news-content img {
    width: 100%;
    max-width: 600px;
    border-radius: 6px;
    margin: 1rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  /* SHARE SECTION */
  .share-wrapper {
    margin-top: 1.5rem;
    display: flex;
    gap: 28px;
    align-items: center;
  }

  .share-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #1b4d3e;
    text-decoration: none;
    font-size: 0.8rem;
    cursor: pointer;
    position: relative;
  }

  .share-item .icon {
    font-size: 1.35rem;
    margin-bottom: 2px;
  }

  /* Tooltip */
  .share-item:hover .icon::after {
    content: attr(data-tooltip);
    position: absolute;
    top: -28px;
    left: 50%;
    transform: translateX(-50%);
    background: #1b4d3e;
    color: white;
    padding: 4px 8px;
    font-size: 0.7rem;
    border-radius: 4px;
    white-space: nowrap;
    z-index: 999;
  }

  /* Floating "Copied!" popup */
  #copied-popup {
    position: fixed;
    bottom: 40px;
    right: 40px;
    background: #1b4d3e;
    color: #fff;
    padding: 12px 18px;
    border-radius: 6px;
    font-size: 0.95rem;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease, transform 0.4s ease;
    transform: translateY(20px);
    z-index: 9999;
  }

  #copied-popup.show {
    opacity: 1;
    transform: translateY(0);
  }
</style>


<!-- Popup for copied link -->
<div id="copied-popup">Link copied!</div>

<!-- ==========================================
     NEWS PAGE HEADER (Fixes LinkedIn Preview)
=========================================== -->

<!-- Open Graph Metadata -->
<meta property="og:title" content="FOUND — News & Updates">
<meta property="og:description" content="Latest developments from FOUND across Mexico, Colombia, and beyond.">
<meta property="og:image" content="https://found-project.github.io/images/found-logo.png">
<meta property="og:url" content="https://found-project.github.io/news/">
<meta property="og:type" content="website">

<!-- Visible Header Section -->
<div class="news-header" style="
  border-left: 4px solid #1b4d3e;
  background: #f5f8f5;
  padding: 1.8rem;
  border-radius: 6px;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
">
  <img src="/images/Found_logo.jpg" alt="FOUND Logo" style=" 
    width: 90px;
    height: auto;
    border-radius: 4px;
  ">
  <div>
    <h1 style="margin: 0; font-size: 1.6rem; color: #1b4d3e;">FOUND — News & Updates</h1>
    <p style="margin: 0.4rem 0 0; font-size: 1rem; color: #333;">
      Latest developments on our work.
    </p>
  </div>
</div>

<!-- ===========================
     CARD 1 — UBPD VISIT
=========================== -->
<div class="news-card" id="ubpd-visit">
  <div class="news-title">
    🇨🇴🇲🇽 Second Visit of Colombia’s Search Unit for Missing Persons (UBPD) to FOUND’s Experimental Sites in Jalisco
  </div>

  <div class="news-content">
    <p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p>

    <p>We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia’s <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND’s experimental sites in Jalisco.</p>

    <p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND’s experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p>

    <p>It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p>

    <p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND’s detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD’s team in Colombia to exchange experiences and integrate UBPD methodologies across FOUND’s partner states in Mexico.</p>

    <div class="share-wrapper">

      <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#ubpd-visit" target="_blank">
        <span class="icon" data-tooltip="LinkedIn">🔗</span>
        <span>LinkedIn</span>
      </a>

      <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#ubpd-visit" target="_blank">
        <span class="icon" data-tooltip="Twitter / X">🐦</span>
        <span>Twitter</span>
      </a>

      <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#ubpd-visit" target="_blank">
        <span class="icon" data-tooltip="WhatsApp">💬</span>
        <span>WhatsApp</span>
      </a>

      <span class="share-item copy-link" data-share="https://found-project.github.io/news/#ubpd-visit">
        <span class="icon" data-tooltip="Copy link">📋</span>
        <span>Copy link</span>
      </span>

    </div>
  </div>
</div>


<!-- ===========================
     CARD 2 — THE GUARDIAN
=========================== -->
<div class="news-card" id="guardian">
  <div class="news-title">
    📄 FOUND is in The Guardian
  </div>

  <div class="news-content">
    <p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist’s in-person visit to our experimental sites in Jalisco, Mexico. We are deeply grateful for the care, depth and commitment brought to this story after months spent listening to families, researchers and officials.</p>

    <p><a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank">📖 Read the article here</a></p>

    <img src="/images/Found_theGuardian.jpeg" alt="FOUND in The Guardian">

    <div class="share-wrapper">

      <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#guardian" target="_blank">
        <span class="icon" data-tooltip="LinkedIn">🔗</span>
        <span>LinkedIn</span>
      </a>

      <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#guardian" target="_blank">
        <span class="icon" data-tooltip="Twitter / X">🐦</span>
        <span>Twitter</span>
      </a>

      <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#guardian" target="_blank">
        <span class="icon" data-tooltip="WhatsApp">💬</span>
        <span>WhatsApp</span>
      </a>

      <span class="share-item copy-link" data-share="https://found-project.github.io/news/#guardian">
        <span class="icon" data-tooltip="Copy link">📋</span>
        <span>Copy link</span>
      </span>

    </div>
  </div>
</div>


<!-- ===========================
     CARD 3 — FCDO FUNDING
=========================== -->
<div class="news-card" id="fcdo">
  <div class="news-title">
    FOUND has received new support from the UK's Foreign, Commonwealth and Development Office (FCDO) through the Frontier Tech Hub.
  </div>

  <div class="news-content">

    <p>In the pitch, our team showcased FOUND’s impact to date, and we were awarded funding that will enable us to scale our mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.</p>

    <p>🌱 Driven by families and research communities<br>
    FOUND is guided and motivated by mothers’ search groups and researchers from CentroGeo, UNAM, IPN, UdeG, ITESO, Oxford, Bristol, Bath, Cambridge, and the Autonomous Universities of Zacatecas and San Luis Potosí.</p>

    <p>🔍 We are now working directly with:</p>
    <ul style="margin-top: 0; padding-left: 20px; line-height: 1.3;">
      <li>Executive Office of the UN Secretary-General</li>
      <li>UK’s Foreign, Commonwealth & Development Office (FCDO)</li>
      <li>Local Search Commissions and Attorney’s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li>
      <li>Colombian Search Unit</li>
      <li>Mexico’s National Search Commission</li>
      <li>Mexican Science and Technology Secretariat</li>
      <li>British Embassy in Mexico City</li>
      <li>British Association for Forensic Anthropology</li>
    </ul>

    <p>🛰️ Technology for memory, dignity, and closure<br>
    We will continue developing — and embedding in official protocols — new ways to locate missing persons using advanced tools such as machine learning models, hyperspectral cameras, seismic instruments, and electrical resistivity.</p>

    <p><em>FOUND: Interpreting Nature to Locate Those We Are Missing</em></p>

    <div class="share-wrapper">

      <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#fcdo" target="_blank">
        <span class="icon" data-tooltip="LinkedIn">🔗</span>
        <span>LinkedIn</span>
      </a>

      <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#fcdo" target="_blank">
        <span class="icon" data-tooltip="Twitter / X">🐦</span>
        <span>Twitter</span>
      </a>

      <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#fcdo" target="_blank">
        <span class="icon" data-tooltip="WhatsApp">💬</span>
        <span>WhatsApp</span>
      </a>

      <span class="share-item copy-link" data-share="https://found-project.github.io/news/#fcdo">
        <span class="icon" data-tooltip="Copy link">📋</span>
        <span>Copy link</span>
      </span>

    </div>
  </div>
</div>


<!-- ===========================
     CARD 4 — MEDIA COVERAGE
=========================== -->
<div class="news-card" id="media-coverage">
  <div class="news-title">
    FOUND featured by Associated Press, The Independent, LA Times, VICE, NBC
  </div>

  <div class="news-content">
    <ul style="margin-top: 0; padding-left: 20px; line-height: 1.3;">
      <li>Associated Press: <a href="https://apnews.com/article/mexico-cartels-disappeared-technology-pigs-9e0fec063c7365c9b1dc4d2262313f86" target="_blank">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
      <li>The Independent: <a href="https://www.independent.co.uk/news/world/americas/mexico-pigs-tools-drug-cartel-b2797915.html" target="_blank">How pigs could help find missing Mexican drug cartel victims</a></li>
      <li>LA Times: <a href="https://www.latimes.com/science/story/2025-07-29/why-are-scientists-dressing-pigs-in-clothes-and-burying-them-in-mexico" target="_blank">Why are scientists dressing pigs in clothes and burying them in Mexico?</a></li>
      <li>VICE: <a href="https://www.vice.com/en/article/mexico-is-using-pigs-drones-and-lasers-to-find-drug-cartel-victims/" target="_blank">Mexico Is Using Pigs, Drones, and Lasers to Find Drug Cartel Victims</a></li>
      <li>NBC: <a href="https://www.nbcnews.com/news/amp/rcna221791" target="_blank">Clothed pigs are buried in Mexico as scientists use them in search of missing</a></li>
    </ul>

    <div class="share-wrapper">

      <a class="share-item" href="https://www.linkedin.com/shareArticle?mini=true&url=https://found-project.github.io/news/#media-coverage" target="_blank">
        <span class="icon" data-tooltip="LinkedIn">🔗</span>
        <span>LinkedIn</span>
      </a>

      <a class="share-item" href="https://twitter.com/intent/tweet?url=https://found-project.github.io/news/#media-coverage" target="_blank">
        <span class="icon" data-tooltip="Twitter / X">🐦</span>
        <span>Twitter</span>
      </a>

      <a class="share-item" href="https://wa.me/?text=https://found-project.github.io/news/#media-coverage" target="_blank">
        <span class="icon" data-tooltip="WhatsApp">💬</span>
        <span>WhatsApp</span>
      </a>

      <span class="share-item copy-link" data-share="https://found-project.github.io/news/#media-coverage">
        <span class="icon" data-tooltip="Copy link">📋</span>
        <span>Copy link</span>
      </span>

    </div>
  </div>
</div>


<!-- ===========================
     JAVASCRIPT FOR CARDS + SHARE + COPY
=========================== -->
<script>
document.addEventListener("DOMContentLoaded", function () {

  /* Expand/collapse cards */
  document.querySelectorAll(".news-card").forEach(card => {
    card.addEventListener("click", function (e) {
      if (e.target.closest(".share-item")) return; 
      card.classList.toggle("open");
    });
  });

  /* Copy link animation */
  const popup = document.getElementById("copied-popup");

  document.querySelectorAll(".copy-link").forEach(btn => {
    btn.addEventListener("click", async function (e) {
      e.stopPropagation();
      const link = btn.dataset.share;
      await navigator.clipboard.writeText(link);

      popup.classList.add("show");
      setTimeout(() => popup.classList.remove("show"), 1500);
    });
  });
});
</script>
