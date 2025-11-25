---
permalink: /
title: "[FOUND] Interpretar la Naturaleza para Encontrar a Quienes nos Faltan"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<style>
  /* ============= GLOBAL PAGE LAYOUT ============= */
  .page {
    max-width: 1400px !important;
    margin: 0 auto;
    padding: 0 1.5rem;
    display: flex;
    flex-direction: row;
    gap: 2rem;
    position: relative;
    overflow-x: hidden;
  }

  /* ============= SUBTLE MOVING BACKGROUND ============= */
  .page::before {
    content: "";
    position: absolute;
    top: -200px;
    right: -200px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(70,130,100,0.18), transparent 70%);
    animation: floatBg 16s ease-in-out infinite alternate;
    z-index: -2;
  }

  @keyframes floatBg {
    from { transform: translate(0,0) scale(1); opacity: 0.6; }
    to   { transform: translate(-60px,40px) scale(1.15); opacity: 0.9; }
  }

  /* ============= LEFT SIDEBAR ============= */
  .sidebar {
    width: 260px;
    flex-shrink: 0;
    position: sticky;
    top: 2rem;
    height: fit-content;
  }

  .sidebar img {
    width: 100%;
    border-radius: 50%;
    margin-bottom: 1rem;
  }

  .sidebar p {
    margin: 0.3rem 0;
  }

  /* ============= MAIN CONTENT ============= */
  .content {
    flex: 1;
    max-width: 100%;
  }

  /* ============= SECTIONS ============= */
  .section {
    background: #f7fafa;
    border-radius: 18px;
    padding: 2.2rem;
    margin-bottom: 2rem;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
    opacity: 0;
    transform: translateY(20px);
    animation: fadeSlide 0.8s ease-out forwards;
  }

  /* Delay per section for staggered animation */
  .section:nth-child(1) { animation-delay: 0.1s; }
  .section:nth-child(2) { animation-delay: 0.2s; }
  .section:nth-child(3) { animation-delay: 0.3s; }
  .section:nth-child(4) { animation-delay: 0.4s; }

  @keyframes fadeSlide {
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .section h2 {
    margin-top: 0;
  }

  /* Lists */
  .section ul {
    margin: 1rem 0 0 1.2rem;
    padding: 0;
  }

  .section ul li {
    margin-bottom: 0.4rem;
    line-height: 1.4;
  }

  /* ============= TECHNOLOGY IMAGE GRID ============= */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .tech-grid img {
    width: 100%;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .tech-grid img:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 26px rgba(0,0,0,0.12);
  }

  /* ============= SOCIAL MEDIA HIGHLIGHTS ============= */
  .social-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  .social-card {
    background: white;
    border-radius: 14px;
    padding: 1rem;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    animation: fadeSlide 0.8s ease-out forwards;
    opacity: 0;
    transform: translateY(20px);
  }

  .social-card iframe,
  .social-card blockquote {
    width: 100%;
  }

  /* ============= RESPONSIVE ============= */
  @media (max-width: 768px) {
    .page {
      flex-direction: column;
    }
    .sidebar {
      width: 100%;
      position: relative;
    }
  }
</style>


<div class="page">
  
  <!-- ============= LEFT SIDEBAR ============= -->
  <div class="sidebar">
    <img src="/images/found-logo.png">
    <h3>FOUND</h3>
    <p>📍 Mexico</p>
    <p><a href="/">🔗 Website</a></p>
    <p><a href="mailto:">✉️ Email</a></p>
  </div>

  <!-- ============= MAIN CONTENT ============= -->
  <div class="content">

    <!-- HERO (unchanged content from your existing page) -->
    {{ the_rest_of_your_hero_section }}

    <!-- ============= SECTION 1 ============= -->
    <div class="section">
      <h2>🌱 Driven by families and research communities</h2>
      <p>
        FOUND is guided and motivated by <strong>search collectives</strong> and researchers
        from CentroGeo, IPN, UNAM, UdeG, Oxford, Bristol, Bath, Cambridge, and the Autonomous
        Universities of Zacatecas and San Luis Potosí.
      </p>
    </div>

    <!-- ============= SECTION 2 ============= -->
    <div class="section">
      <h2>Institutional Collaborations</h2>
      <ul>
        <li>Executive Office of the UN Secretary-General</li>
        <li>UK’s Foreign, Commonwealth & Development Office (FCDO)</li>
        <li>Local Search Commissions and Attorney’s Offices of Jalisco, Zacatecas, San Luis Potosí, and Chihuahua (Mexico)</li>
        <li>Colombian Search Unit</li>
        <li>Mexico’s National Search Commission</li>
        <li>Mexican Science and Technology Secretariat</li>
        <li>British Embassy in Mexico City</li>
        <li>British Association for Forensic Anthropology</li>
      </ul>
    </div>

    <!-- ============= SECTION 3 ============= -->
    <div class="section">
      <h2>Technologies in Action</h2>

      <ul>
        <li>Multispectral & Hyperspectral Imaging</li>
        <li>Airborne LiDAR</li>
        <li>Seismic Noise Interferometry (TIRSA)</li>
        <li>Electrical Resistivity Tomography</li>
        <li>Conductivimetry Measurements</li>
        <li>Satellite Spectral Analysis</li>
        <li>Forensic Entomology</li>
        <li>Botany</li>
        <li>Territorial Analysis</li>
        <li>Soil Science</li>
      </ul>

      <div class="tech-grid">
        <img src="/images/tech1.jpg">
        <img src="/images/tech2.jpg">
        <img src="/images/tech3.jpg">
        <img src="/images/tech4.jpg">
      </div>
    </div>

    <!-- ============= SECTION 4: SOCIAL MEDIA HIGHLIGHTS ============= -->
    <div class="section">
      <h2>Social Media Highlights</h2>
      <p>Recent updates from FOUND’s work (this section can be updated anytime).</p>

      <div class="social-grid">

        <!-- Example card 1 -->
        <div class="social-card">
          <!-- Replace with your real embed -->
          <blockquote class="twitter-tweet">
            <p>Loading Twitter embed…</p>
          </blockquote>
        </div>

        <!-- Example card 2 -->
        <div class="social-card">
          <iframe src="https://www.linkedin.com/embed/feed/update/placeholder" height="420" frameborder="0"></iframe>
        </div>

      </div>
    </div>

  </div>
</div>
