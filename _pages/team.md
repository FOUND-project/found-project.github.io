---
title: "Team"
permalink: /team/
author_profile: false
---
<style>
  .team-page {
    max-width: var(--shell-max);
    margin: 0 auto;
    padding: 3rem var(--shell-pad) 4rem;
    font-family: inherit;
  }

  .team-lang {
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
    margin: 0 0 1.5rem;
  }

  .team-lang button {
    padding: 0.45rem 1.1rem;
    border: 1px solid rgba(45, 95, 77, 0.25);
    background: rgba(255, 255, 255, 0.9);
    color: #2d5f4d;
    font-family: inherit;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    border-radius: 999px;
    cursor: pointer;
    transition: background 0.2s ease, color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
  }

  .team-lang button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.1);
  }

  .team-lang button.active {
    background: #2d5f4d;
    color: #fff;
    border-color: #2d5f4d;
  }

  .team-hero {
    text-align: center;
    margin-bottom: 3rem;
  }

  .team-hero h1 {
    font-size: clamp(2.2rem, 5vw, 3.2rem);
    letter-spacing: 0.04em;
    margin: 0 0 0.75rem;
    font-weight: 700;
  }

  .team-hero .team-tagline {
    font-style: italic;
    opacity: 0.8;
    font-size: 1.05rem;
    max-width: 620px;
    margin: 0 auto;
    line-height: 1.6;
  }

  .team-notice {
    border: 1px solid rgba(150, 120, 70, 0.45);
    background: rgba(150, 120, 70, 0.08);
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    margin: 0 auto 3.5rem;
    max-width: 720px;
    text-align: center;
    font-size: 0.95rem;
    line-height: 1.55;
  }

  .team-notice strong {
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-size: 0.78rem;
    display: block;
    margin-bottom: 0.4rem;
    opacity: 0.75;
  }

  .team-notice a {
    text-decoration: underline;
    font-weight: 600;
  }

  .team-group {
    margin-bottom: 3.5rem;
  }

  .team-group-title {
    font-size: 0.82rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.6;
    margin: 0 0 1.4rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid rgba(128, 128, 128, 0.25);
  }

  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    gap: 1.6rem 2rem;
  }

  .team-member {
    line-height: 1.4;
  }

  .team-member .name {
    font-size: 1.08rem;
    font-weight: 600;
    margin: 0 0 0.25rem;
  }

  .team-member .name a {
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.2s ease;
  }

  .team-member .name a:hover {
    border-bottom-color: currentColor;
  }

  .team-member .role {
    font-size: 0.8rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    opacity: 0.65;
    margin: 0;
  }

  @media (max-width: 520px) {
    .team-grid { grid-template-columns: 1fr 1fr; gap: 1.4rem 1.2rem; }
    .team-member .name { font-size: 0.98rem; }
  }
</style>

<div class="team-page" markdown="0">

  <div class="team-lang" aria-label="Language selection">
    <button type="button" class="active" data-lang="en">EN</button>
    <button type="button" data-lang="es">ES</button>
  </div>

  <div class="team-hero">
    <h1 id="team-title">Our Team</h1>
    <p class="team-tagline" id="team-tagline">FOUND brings together families, scientists, institutions, and practitioners across Mexico, Colombia, and the United Kingdom.</p>
  </div>

  <div class="team-notice">
    <strong id="team-notice-label">Under construction</strong>
    <span id="team-notice-text">This section is a work in progress. Names and roles will continue to be updated, and full biographies will be added in due course. For now, you can reach us at miguel.moctezuma[@]pmb.ox.ac.uk</span>
  </div>

  <div class="team-group">
    <h2 class="team-group-title" id="tg-direction">Direction</h2>
    <div class="team-grid">
      <div class="team-member">
        <p class="name">Miguel Moctezuma</p>
        <p class="role" id="r-miguel">Co-Founder &amp; Co-Director · University of Oxford</p>
      </div>
      <div class="team-member">
        <p class="name">José Luis Silván</p>
        <p class="role" id="r-silvan">Co-Founder &amp; Co-Director · CentroGeo</p>
      </div>
      <div class="team-member">
        <p class="name">Mariela Garfias</p>
        <p class="role" id="r-mariela">FCDO Pioneer</p>
      </div>
    </div>
  </div>

  <div class="team-group">
    <h2 class="team-group-title" id="tg-advisors">Advisors</h2>
    <div class="team-grid">
      <div class="team-member">
        <p class="name">Indira Navarro</p>
        <p class="role" id="r-indira">Search Group Leader · Guerreros Buscadores</p>
      </div>
      <div class="team-member">
        <p class="name">Guillermina Camacho</p>
        <p class="role" id="r-guillermina">Search Group Leader · Siguiendo tu Rastro con Amor</p>
      </div>
      <div class="team-member">
        <p class="name">Luis Fondebrider</p>
        <p class="role" id="r-fondebrider">Forensic Anthropology Advisor</p>
      </div>
      <div class="team-member">
        <p class="name">Victor Hugo Ávila Barrientos</p>
        <p class="role" id="r-avila">Jalisco Search Commission</p>
      </div>
      <div class="team-member">
        <p class="name">Tunuary Chávez</p>
        <p class="role" id="r-tunuary">Jalisco Search Commission</p>
      </div>
      <div class="team-member">
        <p class="name">Luz Janeth Forero</p>
        <p class="role" id="r-forero">Colombia Search Unit</p>
      </div>
      <div class="team-member">
        <p class="name">Martha Lidia Pérez</p>
        <p class="role" id="r-martha">Mexico Search Commission</p>
      </div>
      <div class="team-member">
        <p class="name">Brad Evans</p>
        <p class="role" id="r-brad">Ethics Advisor · University of Bath</p>
      </div>
      <div class="team-member">
        <p class="name">Karina García</p>
        <p class="role" id="r-karina">UWE Bristol</p>
      </div>
    </div>
  </div>

  <div class="team-group">
    <h2 class="team-group-title" id="tg-contributors">Contributors</h2>
    <div class="team-grid">
      <div class="team-member">
        <p class="name">David Vigoureux</p>
        <p class="role" id="r-vigoureux">Innovation Manager at Brink · FOUND Coach</p>
      </div>
      <div class="team-member">
        <p class="name">Samuel Fookes</p>
        <p class="role" id="r-fookes">Innovation at DT Global · FOUND Coach</p>
      </div>
      <div class="team-member">
        <p class="name">Magnus Green</p>
        <p class="role" id="r-green">FOUND Strategy &amp; External Affairs · Director, Istituto Fiorentino di Critica Culturale</p>
      </div>
      <div class="team-member">
        <p class="name">Mercedes Fernández</p>
        <p class="role" id="r-mercedes">FOUND Expert on Visual Cultures</p>
      </div>
      <div class="team-member">
        <p class="name">Daniel Nájera-Betancourt</p>
        <p class="role" id="r-najera">FOUND Documentalist</p>
      </div>
    </div>
  </div>

</div>

<script>
{% raw %}
(function () {
  var T = {
    'team-title':        ['Our Team', 'Nuestro equipo'],
    'team-tagline':      ['FOUND brings together families, scientists, institutions, and practitioners across Mexico, Colombia, and the United Kingdom.',
                          'FOUND re\u00fane a familias, cient\u00edficos, instituciones y profesionales de M\u00e9xico, Colombia y el Reino Unido.'],
    'team-notice-label': ['Under construction', 'En construcci\u00f3n'],
    'team-notice-text':  ['This section is a work in progress. Names and roles will continue to be updated, and full biographies will be added in due course. For now, you can reach us at miguel.moctezuma[@]pmb.ox.ac.uk',
                          'Esta secci\u00f3n est\u00e1 en desarrollo. Los nombres y los cargos se seguir\u00e1n actualizando, y las biograf\u00edas completas se a\u00f1adir\u00e1n en su momento. Por ahora, puedes escribirnos a miguel.moctezuma[@]pmb.ox.ac.uk'],
    'tg-direction':      ['Direction', 'Direcci\u00f3n'],
    'tg-advisors':       ['Advisors', 'Consejo asesor'],
    'tg-contributors':   ['Contributors', 'Colaboradores'],
    'r-miguel':          ['Co-Founder & Co-Director \u00b7 University of Oxford', 'Cofundaci\u00f3n y codirecci\u00f3n \u00b7 Universidad de Oxford'],
    'r-silvan':          ['Co-Founder & Co-Director \u00b7 CentroGeo', 'Cofundaci\u00f3n y codirecci\u00f3n \u00b7 CentroGeo'],
    'r-mariela':         ['FCDO Pioneer', 'Pionera del FCDO'],
    'r-indira':          ['Search Group Leader \u00b7 Guerreros Buscadores', 'Liderazgo de colectivo de b\u00fasqueda \u00b7 Guerreros Buscadores'],
    'r-guillermina':     ['Search Group Leader \u00b7 Siguiendo tu Rastro con Amor', 'Liderazgo de colectivo de b\u00fasqueda \u00b7 Siguiendo tu Rastro con Amor'],
    'r-fondebrider':     ['Forensic Anthropology Advisor', 'Asesor en antropolog\u00eda forense'],
    'r-avila':           ['Jalisco Search Commission', 'Comisi\u00f3n de B\u00fasqueda de Jalisco'],
    'r-tunuary':         ['Jalisco Search Commission', 'Comisi\u00f3n de B\u00fasqueda de Jalisco'],
    'r-forero':          ['Colombia Search Unit', 'Unidad de B\u00fasqueda de Colombia'],
    'r-martha':          ['Mexico Search Commission', 'Comisi\u00f3n Nacional de B\u00fasqueda de M\u00e9xico'],
    'r-brad':            ['Ethics Advisor \u00b7 University of Bath', 'Asesor\u00eda en \u00e9tica \u00b7 Universidad de Bath'],
    'r-karina':          ['UWE Bristol', 'UWE Bristol'],
    'r-vigoureux':       ['Innovation Manager at Brink \u00b7 FOUND Coach', 'Gesti\u00f3n de innovaci\u00f3n en Brink \u00b7 Coach de FOUND'],
    'r-fookes':          ['Innovation at DT Global \u00b7 FOUND Coach', 'Innovaci\u00f3n en DT Global \u00b7 Coach de FOUND'],
    'r-green':           ['FOUND Strategy & External Affairs \u00b7 Director, Istituto Fiorentino di Critica Culturale',
                          'Estrategia y asuntos externos de FOUND \u00b7 Direcci\u00f3n, Istituto Fiorentino di Critica Culturale'],
    'r-mercedes':        ['FOUND Expert on Visual Cultures', 'Especialista en culturas visuales de FOUND'],
    'r-najera':          ['FOUND Documentalist', 'Documentalista de FOUND']
  };

  function setLanguage(lang) {
    var i = (lang === 'es') ? 1 : 0;
    Object.keys(T).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.textContent = T[id][i];
    });
    document.documentElement.setAttribute('lang', i ? 'es' : 'en');
    Array.prototype.forEach.call(document.querySelectorAll('.team-lang button'), function (b) {
      b.classList.toggle('active', b.getAttribute('data-lang') === (i ? 'es' : 'en'));
    });
    try { localStorage.setItem('found-lang', i ? 'es' : 'en'); } catch (e) {}
  }

  function init() {
    var saved = null;
    try { saved = localStorage.getItem('found-lang'); } catch (e) {}
    setLanguage(saved === 'es' ? 'es' : 'en');
    Array.prototype.forEach.call(document.querySelectorAll('.team-lang button'), function (b) {
      b.addEventListener('click', function () { setLanguage(b.getAttribute('data-lang')); });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }
})();
{% endraw %}
</script>
