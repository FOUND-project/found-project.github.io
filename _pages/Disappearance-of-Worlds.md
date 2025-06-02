---
layout: archive
title: "Events & Projects"
permalink: /Events-&-Projects/
author_profile: true
---

<!-- Dark Mode Toggle -->
<script>
  function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
  }

  window.onload = () => {
    if (localStorage.getItem('darkMode') === 'true') {
      document.body.classList.add('dark-mode');
    }
  }
</script>

<style>
  :root {
    --primary: #004080;
    --background: #ffffff;
    --text: #000000;
    --card: #f9f9f9;
  }

  .dark-mode {
    --background: #121212;
    --text: #f0f0f0;
    --card: #1e1e1e;
  }

  body {
    background-color: var(--background);
    color: var(--text);
    transition: background 0.3s, color 0.3s;
  }

  .event-details {
    background-color: var(--card);
  }

  .dark-toggle {
    display: inline-block;
    margin: 1rem 0;
    padding: 0.4rem 0.8rem;
    border: none;
    background-color: var(--primary);
    color: #fff;
    border-radius: 6px;
    cursor: pointer;
  }
</style>

<button class="dark-toggle" onclick="toggleDarkMode()">Toggle Dark Mode</button>

<!-- Existing Styles and Content Below -->

<style>
  .image-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 2rem;
  }

  .image-row img, .full-width-img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }

  .event-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-top: 1.5rem;
    color: var(--primary);
  }

  .event-details {
    margin-bottom: 2.5rem;
    padding: 1.2rem;
    border-left: 4px solid var(--primary);
    border-radius: 6px;
  }

  .event-details p {
    margin: 0.4rem 0;
    line-height: 1.6;
  }

  a {
    color: var(--primary);
    text-decoration: underline;
  }

  a:hover {
    text-decoration: none;
    color: #002c5d;
  }
</style>

## Disappearance of Worlds | Art Exhibition & Dialogues on Disappearance  
### University of Oxford, 7–22 June 2025

We invite you to attend **The Disappearance of Worlds**, a solo exhibition by Mexican artist **Chantal Meza**, hosted at Pembroke College, University of Oxford, from **7–22 June 2025**.

This powerful exhibition and accompanying dialogues are dedicated to the search for truth and justice in the face of disappearance in Mexico. It features *madres buscadoras* (searching mothers) from Jalisco and Estado de México, alongside researchers, who will share their stories and insights surrounded by Chantal Meza’s evocative artwork.

<img class="full-width-img" src="https://github.com/FOUND-project/found-project.github.io/blob/master/images/talksmothers.jpeg?raw=true" alt="Talks with mothers">

<!-- PROGRAMME AND REST OF CONTENT CONTINUES HERE -->
