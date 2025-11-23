---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

<style>
  .news-card {
    border-left: 4px solid #1b4d3e;
    border-radius: 6px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    background-color: #f9f9f9;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
  }

  .news-card:hover {
    background-color: #eef6ee;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
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
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .news-content a {
    color: #1b4d3e;
    font-weight: bold;
    text-decoration: none;
  }

  .news-content a:hover {
    text-decoration: underline;
  }
</style>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".news-card");
    cards.forEach(card => {
      card.addEventListener("click", function () {
        card.classList.toggle("open");
      });
    });
  });
</script>

<div class="news-card">
  <div class="news-title">
    🇨🇴🇲🇽 Second Visit of Colombia’s Search Unit (UBPD) to FOUND’s Experimental Sites in Jalisco
  </div>
  <div class="news-content">
    <p>We are deeply grateful to <strong>CVM Cyber</strong> and <strong>Ciaran Martin</strong> for their generous support in making this visit possible.</p>
    <p>We welcomed <strong>Héctor Javier Gómez</strong>, geophysicist from Colombia’s <em>Unidad de Búsqueda de Personas Dadas por Desaparecidas (UBPD)</em>, for a joint field deployment to FOUND’s experimental sites in Jalisco.</p>
    <p>This visit focused on the gathering and processing of drone-based hyperspectral imagery across all five of FOUND’s experimental sites — marking only the second time this cutting-edge technology has been used in Mexico for humanitarian purposes.</p>
    <p>It follows the October 2025 visit by <strong>Dr Julián Arias</strong>, Director of Prospection, Recovery and Identification at UBPD, which formally launched our collaboration on search and identification methodologies.</p>
    <p>During this second visit, the UBPD offered key technical recommendations to enhance FOUND’s detection strategies for clandestine graves. The collaboration will continue in January 2026, when the FOUND team will visit UBPD’s facilities in Colombia to exchange experiences and integrate UBPD methodologies across FOUND’s partner states in Mexico.</p>
  </div>
</div>

<div class="news-card">
  <div class="news-title">
    📄 FOUND is in The Guardian
  </div>
  <div class="news-content">
    <p>This piece is the result of more than six months of email conversations, WhatsApp messages, and the journalist’s in-person visit to our experimental sites in Jalisco, Mexico. We are deeply grateful for the care, depth and commitment brought to this story after months spent listening to families, researchers and officials.</p>
    <p>
      <a href="https://www.theguardian.com/global-development/2025/nov/19/dead-pigs-grieving-mothers-missing-people-mexico-mexican-cartel-victims" target="_blank">
        📖 Read the article here
      </a>
    </p>
    <img src="/images/Found_theGuardian.jpeg" alt="FOUND in The Guardian">
  </div>
</div>
