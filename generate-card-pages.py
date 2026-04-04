#!/usr/bin/env python3
"""
FOUND News Card Page Generator

This script reads the newsCards data from news.html and generates
individual static HTML pages for each card with proper Open Graph meta tags.

Usage:
  python3 generate-card-pages.py

This creates:
  - news/cards/[card-id]/index.html (one file per card)

Each generated file:
  - Has OG meta tags baked in (title, description, image)
  - Redirects to the main news page with the card hash (#card-id)
  - Is crawlable by social media crawlers
"""

import os
import json
from pathlib import Path

# Card data (extracted from news.html newsCards array)
CARDS = [
    {
        "id": "mariela-award",
        "en_title": "FOUND's pioneer wins the UK FCDO's Sir Nicholas Browne Policy and Expertise Award",
        "es_title": "La pionera de FOUND recibe el Premio Sir Nicholas Browne de Política y Pericia del FCDO británico",
        "image": None,
        "description_en": "Award recognising excellence in delivering policy objectives. Mariela Garfias has been awarded the Sir Nicholas Browne Policy and Expertise Award from the UK FCDO.",
        "description_es": "Mariela Garfias ha recibido el Premio Sir Nicholas Browne de Política y Pericia del FCDO británico.",
    },
    {
        "id": "ubpd-visit",
        "en_title": "Second visit of Colombia's Search Unit for Missing Persons (UBPD) to FOUND's experimental sites in Jalisco",
        "es_title": "Segunda visita de la Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD) de Colombia",
        "image": None,
        "description_en": "Field deployment focusing on drone-based hyperspectral imagery across FOUND's experimental sites in Jalisco, Mexico.",
        "description_es": "Despliegue conjunto enfocado en imágenes hiperespectrales mediante dron en los sitios experimentales de FOUND en Jalisco.",
    },
    {
        "id": "guardian-article",
        "en_title": "FOUND in The Guardian",
        "es_title": "FOUND en The Guardian",
        "image": "https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_theGuardian.jpeg?raw=true",
        "description_en": "An in-depth feature by The Guardian about FOUND's work. The result of over six months of reporting, interviews, and field visits in Jalisco, Mexico.",
        "description_es": "Un reportaje en profundidad de The Guardian sobre el trabajo de FOUND. Resultado de más de seis meses de reportaje, entrevistas y visitas de campo.",
    },
    {
        "id": "frontier-tech-funding",
        "en_title": "FOUND receives new support from the UK's FCDO through the Frontier Tech Hub",
        "es_title": "FOUND recibe nuevo apoyo del FCDO del Reino Unido a través de Frontier Tech Hub",
        "image": None,
        "description_en": "Funding awarded to scale FOUND's mission: to drive systemic change in how missing persons are searched for in Mexico, Colombia, and beyond.",
        "description_es": "Financiación para escalar la misión de FOUND: impulsar cambios sistémicos en cómo se busca a personas desaparecidas.",
    },
    {
        "id": "international-media",
        "en_title": "FOUND featured by Associated Press, The Independent, LA Times, VICE, and NBC",
        "es_title": "FOUND en Associated Press, The Independent, LA Times, VICE y NBC",
        "image": None,
        "description_en": "International media coverage of FOUND's innovative approach to locating missing persons using scientific methods and advanced technology.",
        "description_es": "Cobertura internacional del enfoque innovador de FOUND para localizar a personas desaparecidas.",
    },
]

LOGO_URL = "https://github.com/FOUND-project/found-project.github.io/blob/master/images/Found_logo.jpg?raw=true"
BASE_URL = "https://found-project.org"
NEWS_PAGE = f"{BASE_URL}/news/"

def generate_card_page(card, lang="en"):
    """Generate HTML for a single card page."""
    card_id = card["id"]
    title = card[f"{lang}_title"]
    description = card[f"{lang}_description"]
    image = card["image"] or LOGO_URL

    # Determine page URL
    if lang == "en":
        card_url = f"{NEWS_PAGE}cards/{card_id}/"
    else:
        card_url = f"{NEWS_PAGE}cards/{card_id}/?lang={lang}"

    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Open Graph Meta Tags (for social media previews) -->
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="FOUND Project">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{image}">
    <meta property="og:url" content="{card_url}">

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{image}">
    <meta name="twitter:site" content="@found_project">

    <!-- Canonical & Redirect -->
    <link rel="canonical" href="{NEWS_PAGE}#{{card_id}}">
    <title>{title} — FOUND</title>

    <!-- Meta tags for SEO -->
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">

    <!-- Redirect to main news page after meta tags are read by crawlers -->
    <meta http-equiv="refresh" content="1; url={NEWS_PAGE}#{card_id}">
    <noscript>
        <meta http-equiv="refresh" content="0; url={NEWS_PAGE}#{card_id}">
    </noscript>
</head>
<body style="margin:0; padding:20px; font-family: system-ui, -apple-system, sans-serif; background: #f4faf7;">
    <div style="max-width: 600px; margin: 0 auto;">
        <p style="color: #6b7280; font-size: 14px;">
            Redirecting to FOUND news...
        </p>
        <a href="{NEWS_PAGE}#{card_id}" style="color: #1e4034; font-weight: 600; text-decoration: none; font-size: 16px;">
            Click here if you are not redirected
        </a>
    </div>

    <script>
        // Redirect immediately via JavaScript
        window.location.href = '{NEWS_PAGE}#{card_id}';
    </script>
</body>
</html>
'''
    return html

def main():
    """Generate all card pages."""
    # Determine output directory
    output_base = Path(__file__).parent / "news" / "cards"

    print(f"Generating card pages in: {output_base}")

    for card in CARDS:
        card_id = card["id"]
        card_dir = output_base / card_id

        # Create directory
        card_dir.mkdir(parents=True, exist_ok=True)

        # Generate English version
        en_html = generate_card_page(card, lang="en")
        en_file = card_dir / "index.html"
        en_file.write_text(en_html)
        print(f"✓ Created {en_file}")

        # Optionally generate Spanish version
        # (For now, just one version that auto-redirects)

    print(f"\n✅ Generated {len(CARDS)} card pages")
    print(f"\nDeploy these files to your GitHub Pages repo:")
    print(f"  Copy the 'news/cards' folder to your Jekyll site root")
    print(f"  Commit and push to GitHub")
    print(f"\nTest the links:")
    for card in CARDS:
        print(f"  https://found-project.org/news/cards/{card['id']}/")

if __name__ == "__main__":
    main()
