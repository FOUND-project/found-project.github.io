---
title: "Luis Fondebrider"
permalink: /team/luis-fondebrider/
author_profile: false
excerpt: "Argentine forensic anthropologist, co-founder of the EAAF and FOUND's Forensic Anthropology Advisor."
---
<style>
  .bio-page{max-width:var(--shell-max);margin:0 auto;padding:0 var(--shell-pad) 4rem;font-family:inherit}
  .bio-back{display:inline-flex;align-items:center;gap:.4rem;margin:0 0 1.6rem;font-size:.85rem;font-weight:700;letter-spacing:.04em;color:#1b4d3e}
  .archive a.bio-back,.page__content a.bio-back{text-decoration:none}
  .bio-back:hover{text-decoration:underline}
  .bio-card{background:#fff;border:1px solid rgba(27,77,62,.15);border-left:4px solid #d4af37;border-radius:14px;padding:2rem 2.25rem;max-width:1100px;display:grid;grid-template-columns:240px 1fr;gap:2.25rem;align-items:start}
  .bio-photo{width:240px;height:240px;border-radius:12px;object-fit:cover;display:block;background:#f3f4f6;box-shadow:0 6px 18px rgba(0,0,0,.08)}
  .bio-body{min-width:0;max-width:760px}
  .bio-role{font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:#1b4d3e;font-weight:700;margin:0 0 1.2rem}
  .bio-text p{font-size:1.05rem;line-height:1.75;color:#1f2937;margin:0 0 1.1rem}
  .bio-text p:last-child{margin-bottom:0}
  .bio-text[hidden]{display:none}
  /* Phones: portrait above the text */
  @media (max-width:700px){
    .bio-page{padding-bottom:2.5rem}
    .bio-back{margin-bottom:1rem}
    .bio-card{grid-template-columns:minmax(0,1fr);gap:1.15rem;padding:1.25rem 1.15rem 1.35rem}
    .bio-photo{width:132px;height:132px}
    .bio-role{margin-bottom:.9rem;font-size:.76rem}
    .bio-text p{font-size:1rem;line-height:1.7;margin-bottom:1rem}
  }
</style>
<div class="team-page bio-page" markdown="0">
  <header class="found-header">
    <div class="lang-toggle" aria-label="Language selection">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="es">ES</button>
    </div>
    <div class="found-header-logo"><img class="found-logo-tile" src="/images/logo_FOUND_leaf.png" alt="FOUND"></div>
    <div class="found-header-divider"></div>
    <div class="found-header-body">
      <div class="found-header-eyebrow fx">FOUND<span class="fxb">{</span><span data-en="Team · Advisors" data-es="Equipo · Consejo asesor">Team · Advisors</span><span class="fxb">}</span></div>
      <h1>Luis Fondebrider</h1>
    </div>
  </header>
  <a class="bio-back" href="/team/" data-en="← Back to Team" data-es="← Volver al equipo">← Back to Team</a>
  <article class="bio-card">
    <img class="bio-photo" src="/images/team/luis-fondebrider.jpg" alt="Luis Fondebrider" width="240" height="240">
    <div class="bio-body">
    <p class="bio-role" data-en="Forensic Anthropology Advisor" data-es="Asesor en antropología forense">Forensic Anthropology Advisor</p>
    <div class="bio-text" lang="en">
      <p>Luis Fondebrider is an Argentine forensic anthropologist known worldwide for investigating human rights violations and for helping to find and identify people who were forcibly disappeared.</p>
      <p>He co-founded the Argentine Forensic Anthropology Team (EAAF) and led it as president until 2021. From 2021 to 2022 he headed the Forensic Unit of the International Committee of the Red Cross (ICRC).</p>
      <p>In more than four decades of work he has led forensic investigations in over 65 countries, in settings of armed conflict and of political, ethnic and migration-related violence. Courts, United Nations commissions, human rights organisations and governments have sought his advice on more than 1,200 cases.</p>
      <p>His work goes beyond fieldwork. He also helps shape international protocols and policies on human rights and transitional justice. In 2020 the EAAF was nominated for the Nobel Peace Prize.</p>
    </div>
    <div class="bio-text" lang="es" hidden>
      <p>Luis Fondebrider es un antropólogo forense argentino con reconocimiento internacional por su labor en la investigación de violaciones a los derechos humanos y en la búsqueda e identificación de personas víctimas de desaparición forzada.</p>
      <p>Es cofundador del Equipo Argentino de Antropología Forense (EAAF), que presidió hasta 2021. Entre 2021 y 2022 dirigió la Unidad Forense del Comité Internacional de la Cruz Roja (CICR).</p>
      <p>En más de cuatro décadas de trayectoria ha encabezado investigaciones forenses en más de 65 países, en contextos de conflicto armado y de violencia política, étnica y vinculada a la migración. Tribunales, comisiones de Naciones Unidas, organizaciones de derechos humanos y gobiernos han recurrido a su asesoría en más de 1,200 casos.</p>
      <p>Su trabajo va más allá del campo. También contribuye a definir protocolos y políticas internacionales en materia de derechos humanos y justicia transicional. En 2020, el EAAF fue nominado al Premio Nobel de la Paz.</p>
    </div>
    </div>
  </article>
</div>
<script>
{% raw %}
(function () {
  function setLanguage(lang) {
    var es = lang === 'es';
    Array.prototype.forEach.call(document.querySelectorAll('.bio-page [data-en]'), function (el) {
      el.textContent = el.getAttribute(es ? 'data-es' : 'data-en');
    });
    Array.prototype.forEach.call(document.querySelectorAll('.bio-text'), function (el) {
      el.hidden = el.getAttribute('lang') !== (es ? 'es' : 'en');
    });
    document.documentElement.setAttribute('lang', es ? 'es' : 'en');
    Array.prototype.forEach.call(document.querySelectorAll('.found-header .lang-btn'), function (b) {
      b.classList.toggle('active', b.getAttribute('data-lang') === (es ? 'es' : 'en'));
    });
    try { localStorage.setItem('found-lang', es ? 'es' : 'en'); } catch (e) {}
  }
  function init() {
    var saved = null;
    try { saved = localStorage.getItem('found-lang'); } catch (e) {}
    setLanguage(saved === 'es' ? 'es' : 'en');
    Array.prototype.forEach.call(document.querySelectorAll('.found-header .lang-btn'), function (b) {
      b.addEventListener('click', function () { setLanguage(b.getAttribute('data-lang')); });
    });
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
{% endraw %}
</script>
