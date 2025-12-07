---
layout: archive
title: 
permalink: /how-to-help/
author_profile: true
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Support the Mission</title>
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
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .hero-section {
      background: linear-gradient(135deg, #1b4d3e 0%, #2d7a5f 100%);
      color: white;
      padding: 4rem 3rem;
      border-radius: 20px;
      text-align: center;
      box-shadow: 0 20px 60px rgba(27, 77, 62, 0.3);
      margin-bottom: 3rem;
      position: relative;
      overflow: hidden;
    }

    .hero-section::before {
      content: '';
      position: absolute;
      top: -50%;
      right: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
      animation: pulse 15s ease-in-out infinite;
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 0.5; }
      50% { transform: scale(1.1); opacity: 0.8; }
    }

    .hero-section h1 {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
      position: relative;
      z-index: 1;
    }

    .hero-section p {
      font-size: 1.3rem;
      opacity: 0.95;
      line-height: 1.7;
      max-width: 800px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }

    .image-showcase {
      margin: 3rem 0;
      text-align: center;
    }

    .image-showcase img {
      width: 100%;
      max-width: 900px;
      border-radius: 16px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
      transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .image-showcase img:hover {
      transform: scale(1.02);
    }

    .donate-section {
      background: white;
      padding: 3rem;
      border-radius: 20px;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
      margin-bottom: 3rem;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 3px solid #1b4d3e;
    }

    .section-header h2 {
      font-size: 2rem;
      color: #1a1a1a;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .section-header .icon {
      font-size: 2rem;
    }

    .organization-card {
      background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%);
      border-radius: 16px;
      padding: 2rem;
      border: 2px solid rgba(27, 77, 62, 0.1);
      margin-bottom: 2rem;
      transition: all 0.3s ease;
    }

    .organization-card:hover {
      border-color: rgba(27, 77, 62, 0.3);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }

    .org-header {
      display: flex;
      align-items: center;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }

    .org-logo {
      width: 140px;
      height: auto;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }

    .org-info h3 {
      font-size: 1.5rem;
      color: #1b4d3e;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }

    .facebook-link {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.6rem 1.2rem;
      background: #1877f2;
      color: white;
      text-decoration: none;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.95rem;
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(24, 119, 242, 0.3);
    }

    .facebook-link:hover {
      background: #166fe5;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(24, 119, 242, 0.4);
    }

    .testimonial {
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      padding: 2rem;
      border-radius: 12px;
      border-left: 5px solid #1b4d3e;
      font-style: italic;
      color: #333;
      margin: 2rem 0;
      line-height: 1.8;
      font-size: 1.05rem;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
    }

    .testimonial::before {
      content: '"';
      font-size: 3rem;
      color: #1b4d3e;
      opacity: 0.3;
      font-family: Georgia, serif;
      line-height: 0;
      margin-right: 0.5rem;
    }

    .payment-details {
      background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
      padding: 2rem;
      border-radius: 12px;
      border: 2px solid #1b4d3e;
      box-shadow: 0 4px 20px rgba(27, 77, 62, 0.1);
    }

    .payment-details h4 {
      color: #1b4d3e;
      font-size: 1.3rem;
      margin-bottom: 1.5rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .payment-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.5rem;
    }

    .payment-item {
      background: white;
      padding: 1.2rem;
      border-radius: 10px;
      border: 1px solid rgba(0, 0, 0, 0.06);
      transition: all 0.3s ease;
    }

    .payment-item:hover {
      border-color: #1b4d3e;
      box-shadow: 0 4px 16px rgba(27, 77, 62, 0.1);
    }

    .payment-label {
      font-weight: 700;
      color: #1b4d3e;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
    }

    .payment-value {
      color: #1a1a1a;
      font-size: 1.05rem;
      font-weight: 500;
      word-break: break-word;
    }

    .collaborate-section {
      background: linear-gradient(135deg, #1b4d3e 0%, #2d7a5f 100%);
      color: white;
      padding: 3rem;
      border-radius: 20px;
      text-align: center;
      box-shadow: 0 12px 40px rgba(27, 77, 62, 0.3);
    }

    .collaborate-section h2 {
      font-size: 2rem;
      margin-bottom: 1rem;
      font-weight: 700;
    }

    .collaborate-section p {
      font-size: 1.2rem;
      margin-bottom: 2rem;
      opacity: 0.95;
    }

    .linkedin-link {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      padding: 1rem 2rem;
      background: white;
      color: #0a66c2;
      text-decoration: none;
      border-radius: 50px;
      font-weight: 700;
      font-size: 1.1rem;
      transition: all 0.3s ease;
      box-shadow: 0 8px 24px rgba(255, 255, 255, 0.3);
    }

    .linkedin-link:hover {
      transform: translateY(-3px);
      box-shadow: 0 12px 32px rgba(255, 255, 255, 0.5);
      background: #f8f9fa;
    }

    @media (max-width: 768px) {
      body {
        padding: 1.5rem 1rem;
      }

      .hero-section,
      .donate-section,
      .collaborate-section {
        padding: 2rem 1.5rem;
      }

      .hero-section h1 {
        font-size: 1.8rem;
      }

      .hero-section p {
        font-size: 1.1rem;
      }

      .section-header h2 {
        font-size: 1.5rem;
      }

      .payment-grid {
        grid-template-columns: 1fr;
      }

      .org-header {
        flex-direction: column;
        align-items: flex-start;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Hero Section -->
    <div class="hero-section">
      <h1>Support These Mothers</h1>
      <p>You can support these mothers directly — every contribution makes a difference in their search for missing loved ones.</p>
    </div>

    <!-- Image Showcase -->
    <div class="image-showcase">
      <img src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/mothers%20walking.gif?raw=true" alt="Mothers searching for their missing loved ones">
    </div>

    <!-- Donate Section -->
    <div class="donate-section">
      <div class="section-header">
        <span class="icon">💳</span>
        <h2>Donate</h2>
      </div>

      <div class="organization-card">
        <div class="org-header">
          <img class="org-logo" src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/Final%20Guerreros%20Buscadores.png?raw=true" alt="Guerreros Buscadores de Jalisco">
          <div class="org-info">
            <h3>Guerreros Buscadores de Jalisco</h3>
            <a class="facebook-link" href="https://www.facebook.com/profile.php?id=61555458753120" target="_blank" rel="noopener">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
              </svg>
              Visit Facebook Page
            </a>
          </div>
        </div>

        <div class="testimonial">
          These are the details to donate — your support allows us to continue our searches. Thank you for your empathy — it is through your support that we can carry on looking for our missing loved ones. Until we find them!
        </div>

        <div class="payment-details">
          <h4>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="1" y="4" width="22" height="16" rx="2" ry="2"/>
              <line x1="1" y1="10" x2="23" y2="10"/>
            </svg>
            Payment Information
          </h4>
          
          <div class="payment-grid">
            <div class="payment-item">
              <div class="payment-label">PayPal</div>
              <div class="payment-value">guerrerosbuscadoresdejalisco@gmail.com</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">Account Holder</div>
              <div class="payment-value">Indira Navarro</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">Country</div>
              <div class="payment-value">Mexico</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">Bank</div>
              <div class="payment-value">BBVA</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">Card Details</div>
              <div class="payment-value">4152 3142 5358 9934</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">Account Number</div>
              <div class="payment-value">1502613941</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">CLABE</div>
              <div class="payment-value">012320015026139414</div>
            </div>

            <div class="payment-item">
              <div class="payment-label">SWIFT</div>
              <div class="payment-value">BCMRMXMMPYM</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Collaborate Section -->
    <div class="collaborate-section">
      <h2>How to Collaborate & Amplify</h2>
      <p>Join us in raising awareness and supporting this critical mission</p>
      <a class="linkedin-link" href="https://www.linkedin.com/company/found-project" target="_blank" rel="noopener">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
        </svg>
        Follow on LinkedIn
      </a>
    </div>
  </div>
</body>
</html>
