---
title: "Team"
permalink: /team/
author_profile: false
---
<meta name="viewport" content="width=1200">
<style>
  .team-page {
    max-width: var(--shell-max);
    margin: 0 auto;
    padding: 0 var(--shell-pad) 4rem;
    font-family: inherit;
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
  .team-hero .team-intro { max-width: none; margin: 0; padding: 1.1rem 1.5rem; border-radius: 14px; background: rgba(9,24,19,.94); color: rgba(232,245,240,.85); line-height: 1.7; font-size: 1.02rem; text-align: left; }
  .team-intro .ti-label { color: #d4af37; font-weight: 700; letter-spacing: .04em; white-space: nowrap; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .92rem; }
  .team-intro .ti-brace { color: rgba(74,140,115,.9); font-weight: 400; }
  .team-intro .ti-divider { color: rgba(74,140,115,.6); margin: 0 .6rem; }
  .team-notice { display: flex; align-items: center; gap: 1rem 1.4rem; flex-wrap: wrap; border: 1px solid rgba(212,175,55,.5); border-left: 4px solid #d4af37; background: #fffdf6; border-radius: 14px; padding: 1rem 1.4rem; margin: 0 0 3.25rem; font-size: .98rem; line-height: 1.55; color: #3f3f3f; }
  .team-notice strong { flex: none; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: .14em; text-transform: uppercase; font-size: .72rem; color: #7a5f00; background: rgba(212,175,55,.16); border: 1px solid rgba(212,175,55,.5); border-radius: 999px; padding: .3rem .8rem; }
  .team-group { margin-bottom: 3.5rem; }
  .archive h2.team-group-title, .page__content h2.team-group-title { display: flex; align-items: center; gap: 1rem; font-family: 'DM Serif Display', Georgia, serif; font-weight: 400; font-size: 1.9rem; letter-spacing: 0; text-transform: none; color: #1e4034; margin: 0 0 1.5rem; padding: 0; border: 0; opacity: 1; }
  .team-group-title::after { content: ''; flex: 1; height: 1px; background: linear-gradient(90deg, rgba(212,175,55,.75), rgba(212,175,55,0)); }
  .team-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(255px, 1fr)); gap: 1.25rem; }
  .team-group--lead .team-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .team-member { position: relative; display: flex; flex-direction: column; align-items: flex-start; gap: .2rem; padding: 1.4rem 1.35rem 1.3rem; background: #fff; border: 1px solid rgba(45,95,77,.14); border-radius: 18px; box-shadow: 0 2px 10px rgba(15,23,42,.06); overflow: hidden; line-height: 1.4; transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease; }
  .team-member::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 4px; background: linear-gradient(90deg, #d4af37, rgba(212,175,55,.2)); }
  .team-member:hover { transform: translateY(-4px); box-shadow: 0 16px 36px rgba(15,23,42,.12); border-color: rgba(212,175,55,.6); }
  .team-avatar { flex: none; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: .85rem; background: linear-gradient(135deg, #123126, #2d5f4d); color: #f1d98a; font-family: 'DM Serif Display', Georgia, serif; font-size: 1.3rem; letter-spacing: .03em; box-shadow: 0 0 0 3px #fff, 0 0 0 4px rgba(212,175,55,.55); overflow: hidden; }
  .team-member .team-logo { position: absolute; top: 1.15rem; right: 1.1rem; height: 66px; width: auto; max-width: 42%; object-fit: contain; margin: 0; border-radius: 6px; }
  .team-avatar img { width: 100%; height: 100%; object-fit: cover; display: block; margin: 0; }
  .team-group--lead .team-member { padding: 1.7rem 1.6rem 1.55rem; background: linear-gradient(135deg, #fff 0%, #f5fbf8 100%); }
  .team-group--lead .team-avatar { width: 72px; height: 72px; font-size: 1.55rem; }
  .team-member .name { font-size: 1.14rem; font-weight: 700; color: #1e4034; margin: 0; letter-spacing: 0; }
  .team-group--lead .team-member .name { font-size: 1.3rem; }
  .team-member .name a { color: inherit; }
  .archive .team-member .name a, .page__content .team-member .name a { text-decoration: none; }
  .team-member .name a::after { content: ''; position: absolute; inset: 0; }
  .team-member .role { font-size: .9rem; line-height: 1.5; letter-spacing: 0; text-transform: none; color: #5d6763; opacity: 1; margin: .15rem 0 0; }
  .team-member .bio-link { position: relative; display: inline-block; margin-top: auto; padding-top: .9rem; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .72rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #2d5f4d; }
  .archive .team-member a.bio-link, .page__content .team-member a.bio-link { text-decoration: none; }
  .team-member:hover .bio-link { color: #1e4034; }
</style>

<div class="team-page" markdown="0">


  <header class="found-header">
      <div class="lang-toggle" aria-label="Language selection">
        <button type="button" class="lang-btn active" data-lang="en">EN</button>
        <button type="button" class="lang-btn" data-lang="es">ES</button>
      </div>
      <div class="found-header-logo"><img class="found-logo-tile" src="/images/logo_FOUND_leaf.png" alt="FOUND"></div>
      <div class="found-header-divider"></div>
      <div class="found-header-body">
        <div class="found-header-eyebrow" id="team-pill">FOUND · Team</div>
        <h1 id="team-title">Our Team</h1>
      </div>
    </header>
  <div class="team-hero">
    <p class="team-intro"><span class="ti-label" aria-hidden="true">FOUND<span class="ti-brace">{</span>Team<span class="ti-brace">}</span></span><span class="ti-divider" aria-hidden="true">&middot;</span><span id="team-intro-text">Our core team brings together search collectives of Mexico and Colombia, CentroGeo, the University of Oxford, Jalisco’s Search Commission, the British Embassy in Mexico City, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara.</span></p>
  </div>

  <div class="team-notice">
    <strong id="team-notice-label">Under construction</strong>
    <span id="team-notice-text">This section is a work in progress. For now, you can reach us at miguel.moctezuma[@]found-project.org</span>
  </div>

  <div class="team-group team-group--lead">
    <h2 class="team-group-title" id="tg-direction">Direction</h2>
    <div class="team-grid">
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">MM</span>
        <p class="name">Miguel Moctezuma</p>
        <p class="role" id="r-miguel">Co-Founder &amp; Co-Director · University of Oxford</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">JS</span>
        <p class="name">José Luis Silván</p>
        <p class="role" id="r-silvan">Co-Founder &amp; Co-Director · CentroGeo</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">MG</span>
        <p class="name">Mariela Garfias</p>
        <p class="role" id="r-mariela">FCDO Pioneer</p>
      </div>
    </div>
  </div>

  <div class="team-group">
    <h2 class="team-group-title" id="tg-advisors">Advisors</h2>
    <div class="team-grid">
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">IN</span>
        <img class="team-logo" src="/images/logos/guerreros_buscadores.png" alt="Guerreros Buscadores de Jalisco" loading="lazy">
        <p class="name">Indira Navarro</p>
        <p class="role" id="r-indira">Search Collective · Guerreros Buscadores</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">GC</span>
        <p class="name">Guillermina Camacho</p>
        <p class="role" id="r-guillermina">Search Collective · Siguiendo tu Rastro con Amor</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">MM</span>
        <p class="name">María del Carmen Meza Ponce</p>
        <p class="role" id="r-meza">Search Collective · Manos Buscadoras de Jalisco</p>
      </div>
      <div class="team-member">
        <span class="team-avatar"><img src="/images/team/luis-fondebrider.jpg" alt="" loading="lazy"></span>
        <p class="name"><a href="/team/luis-fondebrider/">Luis Fondebrider</a></p>
        <p class="role" id="r-fondebrider">Forensic Anthropology Advisor</p>
        <a class="bio-link" href="/team/luis-fondebrider/" id="bio-fondebrider">Read bio →</a>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">VÁ</span>
        <p class="name">Victor Hugo Ávila Barrientos</p>
        <p class="role" id="r-avila">Jalisco Search Commission</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">TC</span>
        <p class="name">Tunuary Chávez</p>
        <p class="role" id="r-tunuary">Jalisco Search Commission</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">LF</span>
        <p class="name">Luz Janeth Forero</p>
        <p class="role" id="r-forero">Colombia Search Unit</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">MP</span>
        <p class="name">Martha Lidia Pérez</p>
        <p class="role" id="r-martha">Mexico Search Commission</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">BE</span>
        <p class="name">Brad Evans</p>
        <p class="role" id="r-brad">Ethics Advisor · University of Bath</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">KG</span>
        <p class="name">Karina García</p>
        <p class="role" id="r-karina">UWE Bristol</p>
      </div>
    </div>
  </div>

  <div class="team-group">
    <h2 class="team-group-title" id="tg-contributors">Contributors</h2>
    <div class="team-grid">
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">DV</span>
        <p class="name">David Vigoureux</p>
        <p class="role" id="r-vigoureux">Innovation Manager at Brink · FOUND Coach</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">SF</span>
        <p class="name">Samuel Fookes</p>
        <p class="role" id="r-fookes">Innovation at DT Global · FOUND Coach</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">MG</span>
        <p class="name">Magnus Green</p>
        <p class="role" id="r-green">FOUND Strategy &amp; External Affairs · Director, Istituto Fiorentino di Critica Culturale</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">MF</span>
        <p class="name">Mercedes Fernández</p>
        <p class="role" id="r-mercedes">FOUND Expert on Visual Cultures</p>
      </div>
      <div class="team-member">
        <span class="team-avatar" aria-hidden="true">DN</span>
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
    'team-pill':         ['FOUND · Team', 'FOUND · Equipo'],
    'team-intro-text':   ['Our core team brings together search collectives of Mexico and Colombia, CentroGeo, the University of Oxford, Jalisco\u2019s Search Commission, the British Embassy in Mexico City, the National Autonomous University of Mexico (UNAM), and the Universidad de Guadalajara.',
                          'Nuestro equipo central re\u00fane a colectivos de b\u00fasqueda de M\u00e9xico y Colombia, CentroGeo, la Universidad de Oxford, la Comisi\u00f3n de B\u00fasqueda de Jalisco, la Embajada Brit\u00e1nica en la Ciudad de M\u00e9xico, la Universidad Nacional Aut\u00f3noma de M\u00e9xico (UNAM) y la Universidad de Guadalajara.'],
    'team-notice-label': ['Under construction', 'En construcci\u00f3n'],
    'team-notice-text':  ['This section is a work in progress. For now, you can reach us at miguel.moctezuma[@]found-project.org',
                          'Esta secci\u00f3n est\u00e1 en desarrollo. Por ahora, puedes escribirnos a miguel.moctezuma[@]found-project.org'],
    'tg-direction':      ['Direction', 'Direcci\u00f3n'],
    'tg-advisors':       ['Advisors', 'Consejo asesor'],
    'tg-contributors':   ['Contributors', 'Colaboradores'],
    'r-miguel':          ['Co-Founder & Co-Director \u00b7 University of Oxford', 'Cofundaci\u00f3n y codirecci\u00f3n \u00b7 Universidad de Oxford'],
    'r-silvan':          ['Co-Founder & Co-Director \u00b7 CentroGeo', 'Cofundaci\u00f3n y codirecci\u00f3n \u00b7 CentroGeo'],
    'r-mariela':         ['FCDO Pioneer', 'Pionera del FCDO'],
    'r-indira':          ['Search Collective \u00b7 Guerreros Buscadores', 'Colectivo de b\u00fasqueda \u00b7 Guerreros Buscadores'],
    'r-guillermina':     ['Search Collective \u00b7 Siguiendo tu Rastro con Amor', 'Colectivo de b\u00fasqueda \u00b7 Siguiendo tu Rastro con Amor'],
    'r-meza':            ['Search Collective \u00b7 Manos Buscadoras de Jalisco', 'Colectivo de b\u00fasqueda \u00b7 Manos Buscadoras de Jalisco'],
    'r-fondebrider':     ['Forensic Anthropology Advisor', 'Asesor en antropolog\u00eda forense'],
    'bio-fondebrider':   ['Read bio \u2192', 'Leer biograf\u00eda \u2192'],
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
    Array.prototype.forEach.call(document.querySelectorAll('.found-header .lang-btn'), function (b) {
      b.classList.toggle('active', b.getAttribute('data-lang') === (i ? 'es' : 'en'));
    });
    try { localStorage.setItem('found-lang', i ? 'es' : 'en'); } catch (e) {}
  }

  function init() {
    var saved = null;
    try { saved = localStorage.getItem('found-lang'); } catch (e) {}
    setLanguage(saved === 'es' ? 'es' : 'en');
    Array.prototype.forEach.call(document.querySelectorAll('.found-header .lang-btn'), function (b) {
      b.addEventListener('click', function () { setLanguage(b.getAttribute('data-lang')); });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }
})();
{% endraw %}
</script>
