<script>
  // Run after the whole page has loaded
  window.addEventListener('load', function () {
    var STORAGE_KEY = 'found-lang';

    var translations = {
      en: {
        'pill-book':'BOOK',
        'title-book':'The Book',
        'book-badge':'Peer-reviewed chapters',
        'book-desc':'This volume brings together biological, physical, and earth sciences to design and test methods for detecting clandestine graves. The English translation is currently in progress.',

        'pill-articles':'ARTICLES',
        'title-articles':'Articles',
        'a1-badge':'Peer-reviewed',
        'a2-badge':'Peer-reviewed',
        'a3-badge':'Book chapter',
        'a1-title':'Design of spectral indices for the detection of soil pollutants associated with the disappearance of persons',
        'a1-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, J.M. Madrigal-Gómez, C. Silva-Arias (2025)',
        'a2-title':'Assessing Geospatial Models to Explain the Occurrence of Clandestine Graves in Mexico',
        'a2-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, C. Silva-Arias (2024)',
        'a3-title':'Espacio Clandestino: A Nationwide Platform to Support Clandestine Graves Search in Mexico',
        'a3-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón (2024)',

        'pill-blogs':'BLOGS &amp; INSIGHTS',
        'title-blogs':'Blogs',
        'b1-badge':'Blog',
        'b2-badge':'News story',
        'b3-badge':'Op-ed',
        'b1-title':'On the Frontier of Finding Peace',
        'b1-meta':'Mariela Garfias &amp; Frontier Tech Hub (2025)',
        'b2-title':'Academic playing role in project to find hidden graves in Mexico using drone technology',
        'b2-meta':'University of the West of England – Bristol (2025)',
        'b3-title':'Camera-Fitted Drones May Help Locate Graves of Mexico’s Disappeared',
        'b3-meta':'Karina García-Reyes &amp; Miguel Moctezuma (2024)'
      },

      es: {
        'pill-book':'LIBRO',
        'title-book':'El libro',
        'book-badge':'Arbitraje científico de capítulos',
        'book-desc':'Este volumen reúne ciencias biológicas, físicas y de la Tierra para diseñar y probar métodos de detección de fosas clandestinas. La traducción al inglés está en proceso.',

        'pill-articles':'ARTÍCULOS',
        'title-articles':'Artículos',
        'a1-badge':'Revisado por pares',
        'a2-badge':'Revisado por pares',
        'a3-badge':'Capítulo de libro',
        'a1-title':'Diseño de índices espectrales para detectar contaminantes del suelo asociados con la desaparición de personas',
        'a1-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, J.M. Madrigal-Gómez, C. Silva-Arias (2025)',
        'a2-title':'Evaluación de modelos geoespaciales para explicar la ocurrencia de fosas clandestinas en México',
        'a2-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, C. Silva-Arias (2024)',
        'a3-title':'Espacio Clandestino: una plataforma nacional para apoyar la búsqueda de fosas clandestinas en México',
        'a3-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón (2024)',

        'pill-blogs':'BLOGS Y REFLEXIONES',
        'title-blogs':'Blogs',
        'b1-badge':'Blog',
        'b2-badge':'Nota informativa',
        'b3-badge':'Artículo de opinión',
        'b1-title':'En la frontera de encontrar la paz',
        'b1-meta':'Mariela Garfias &amp; Frontier Tech Hub (2025)',
        'b2-title':'Académica participa en proyecto para encontrar fosas ocultas en México mediante tecnología de drones',
        'b2-meta':'University of the West of England – Bristol (2025)',
        'b3-title':'Drones con cámara pueden ayudar a localizar fosas de personas desaparecidas en México',
        'b3-meta':'Karina García-Reyes &amp; Miguel Moctezuma (2024)'
      },

      nah: {
        'pill-book':'AMATLAHCUILOLLI',
        'title-book':'In amatl',
        'book-badge':'Amatl kuali',
        'book-desc':'Nin amatl kualtsin kualtlalia ciencias de biología, física huan tlalli para kijtos kenik tiktlatemohuah fosas clandestinas. In traducción inglés ok inon onkaj ipan tequiti.',

        'pill-articles':'TLATLAHCUILOLLI',
        'title-articles':'Tlatlahcuilolli',
        'a1-badge':'Tlatlatzintli ipan revista',
        'a2-badge':'Tlatlatzintli ipan revista',
        'a3-badge':'Capítulo de libro',
        'a1-title':'Diseño de índices espectrales para detectar kontaminantes ipan tlalli tlen kixnechikah desaparición de tlācameh',
        'a1-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, J.M. Madrigal-Gómez, C. Silva-Arias (2025)',
        'a2-title':'Evaluación de modelos geoespaciales para explicar tlen ika mochihua fosas clandestinas ipan Mēxihco',
        'a2-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón, C. Silva-Arias (2024)',
        'a3-title':'Espacio Clandestino: plataforma para se país tlen kipalehui tlatemohuiliztli de fosas clandestinas ipan Mēxihco',
        'a3-meta':'J.L. Silván-Cárdenas, A.J. Alegre-Mondragón (2024)',

        'pill-blogs':'BLOGS',
        'title-blogs':'Blogs',
        'b1-badge':'Blog',
        'b2-badge':'Noticia',
        'b3-badge':'Op-ed',
        'b1-title':'Ipan frontera para kajsikamatilistli yolsewilia',
        'b1-meta':'Mariela Garfias &amp; Frontier Tech Hub (2025)',
        'b2-title':'Tlamachtij ipan universidad kimpalehui proyekto para tiktlatemohua fosas tlatsentlalka ipan Mēxihco ika drones',
        'b2-meta':'University of the West of England – Bristol (2025)',
        'b3-title':'Drones ika cámara welis kimpalehuiah tiktlatemohua fosas de tlācameh tlen polihuitkeh ipan Mēxihco',
        'b3-meta':'Karina García-Reyes &amp; Miguel Moctezuma (2024)'
      }
    };

    var ids = [
      'pill-book','title-book','book-badge','book-desc',
      'pill-articles','title-articles',
      'a1-badge','a2-badge','a3-badge',
      'a1-title','a1-meta','a2-title','a2-meta','a3-title','a3-meta',
      'pill-blogs','title-blogs',
      'b1-badge','b2-badge','b3-badge',
      'b1-title','b1-meta','b2-title','b2-meta','b3-title','b3-meta'
    ];

    function setLanguage(lang) {
      var dict = translations[lang] || translations.en;

      // Swap text
      for (var i = 0; i < ids.length; i++) {
        var id = ids[i];
        var el = document.getElementById(id);
        if (el && dict.hasOwnProperty(id)) {
          el.innerHTML = dict[id];
        }
      }

      // Toggle active pill
      var buttons = document.querySelectorAll('.lang-btn');
      for (var j = 0; j < buttons.length; j++) {
        var btn = buttons[j];
        var langAttr = btn.getAttribute('data-lang');
        if (langAttr === lang) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      }

      // Save preference
      try {
        localStorage.setItem(STORAGE_KEY, lang);
      } catch (e) {}
    }

    // Initial language (from storage if present)
    var initial = 'en';
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'en' || saved === 'es' || saved === 'nah') {
        initial = saved;
      }
    } catch (e) {}

    setLanguage(initial);

    // Button click handlers
    var buttons = document.querySelectorAll('.lang-btn');
    for (var k = 0; k < buttons.length; k++) {
      buttons[k].addEventListener('click', function () {
        var lang = this.getAttribute('data-lang');
        setLanguage(lang);
      });
    }
  });
</script>
