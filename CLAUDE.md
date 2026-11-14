# FOUND website — working notes

Jekyll site on GitHub Pages (minimal-mistakes theme, vendored under `_sass/`,
`_includes/`, `_layouts/`). Served at **found-project.org** from `master`.

## Workflow the site owner expects

Take every change all the way to `master` yourself. Do not stop at a pushed
branch and do not wait for the Claude Code UI to open a PR — it does so on a
delay of several minutes, which has repeatedly left work stranded.

1. Commit with a descriptive message
2. Push the working branch
3. **Open the PR yourself** (`create_pull_request`)
4. **Merge it** into `master`

If the UI races you and opens its own PR first, yours fails as a duplicate —
harmless, just merge whichever exists. Stop at step 3 only if the owner asks to
review first.

`master` is the live site: merging deploys it.

## Layout

- **Homepage is `_pages/about.md`** (`permalink: /`), not an `index.*`. It is
  self-contained: all its CSS and JS are inline in that one file.
- **Site-wide CSS lives in `_includes/head/custom.html`**, which the default
  layout pulls into `<head>` on every page. Layout shell, masthead and
  navigation styling belong there, not in individual pages.
- Shared width tokens: `--shell-max` (1860px) and `--shell-pad`. Use them for
  any new full-width section rather than inventing another max-width.

### Homepage structure (Nov 2026 refresh)

Top to bottom: `.home-hero` (one dark band: brand lockup, `.hh-headline` with the
rotating word, mission paragraph, one gold `.hh-btn` to `#buscadoras`; the two featured cards sit
in `.hh-featured` on the right, below on screens under 1100px) → `.stats-ribbon` →
timeline → `.gif-strip` ("Platforms", heading above the clips) → trailer → FOUND in
Action → Buscadoras → coproduction → partnerships → `.social-section` ("In the
media") → closing `.footer`. Bands alternate dark and light; keep that when adding
a section.

The refresh styles are one block at the **end** of the page `<style>`, under the
`HOME REFRESH` comment, so they win ties with the older rules above them. Put
homepage polish there. The version before the refresh is kept on the branch
`backup/home-before-redesign-2026-11-10`.

Theme rules that silently distort the homepage (all neutralised in that block —
do not reintroduce):

- `h1`–`h6` get `margin-top:2em`, and `.page__content h2` a `border-bottom`. That
  was ~100px of dead space and a stray rule above every section title.
- `.page__content p` sets margins and beats a bare class, so a `<p>` styled as a
  headline or centred with `margin:auto` needs `.parent p.class`.
- `body` has `padding-bottom:9em` and the empty `.page__meta` a top margin: a white
  gap between the closing band and the site footer.
- The fixed masthead is 70px tall: sections that are link targets need
  `scroll-margin-top` of at least that.

### Full-bleed: two things fight it

The theme reserves large empty margins. Both are already neutralised in
`head/custom.html` — do not reintroduce them:

- `_sass/_page.scss` puts `.page` on a Susy grid (`span(10 of 12 last)` with a
  `suffix(2 of 12)`), reserving ~17% of the viewport, plus `1em` padding on
  `#main`.
- Several pages set their own horizontal `body` padding. That creates gutters
  **and** drags the fixed masthead sideways, because `.masthead` has no `left`
  and so sits at its static position. It also clobbers the top padding that
  clears the nav.

## Navigation

`_includes/masthead.html` carries the FOUND mark (`images/logo_FOUND_mark.png`)
beside the wordmark.

**`.visible-links` must shrink-wrap.** `assets/js/plugins/jquery.greedy-navigation.js`
compares `$vlinks.width()` against the available space and moves links into the
hidden menu while it overflows. A full-width `display:flex` container makes that
always true, so the script silently evacuates *every* link into the hamburger.
Use `display:inline-flex` with `width:auto`.

## Languages

English and Spanish only — no other locales.

- Every page with a toggle (`about`, `news`, `media`, `publications`,
  `team`) stores the choice under the single key **`found-lang`**,
  so one choice follows the reader across the site. Some pages still read a
  legacy per-page key as a fallback; keep writing to `found-lang`.
- Translations are dictionaries keyed by element `id`; `setLanguage` walks the
  keys and sets `innerHTML`/`textContent`. To add translatable copy, give the
  element an id and add it to both dictionaries.
- Where one piece of content is rendered twice (e.g. the "four ways of seeing"
  SVG and its small-screen card list), copy the text from the primary element in
  JS after each language switch rather than duplicating strings.

**Never translate people's names.** For role titles, avoid guessing someone's
gender: prefer forms that do not require one, and follow the site's own existing
Spanish where it already establishes a form.

## Editing these pages

- Inline `<script>` blocks must be wrapped in `{% raw %}` / `{% endraw %}`;
  Liquid runs before kramdown and will otherwise eat `{{` and `{%`.
- Avoid blank lines inside `<style>` and `<script>` blocks.
- Check for stray `{{` before committing.

### The theme outranks your page CSS more often than you expect

Page-level styles sit in an inline `<style>`, so they win ties on order — but a
bare class (0,1,0) loses to the theme's compound selectors. These three have
each silently overridden new styling:

| Theme rule | Where | Beats |
|---|---|---|
| `.archive a { text-decoration: underline }` | `_sass/_archive.scss` | any `.my-btn` |
| `.page__content a { text-decoration: underline }` | `_sass/_page.scss` | any `.my-btn` |
| `input[type="search"] { box-sizing: content-box }` | `_sass/_reset.scss` | any `.my-input` |

Note most custom pages render inside `.archive`, **not** `.page__content` — but the
homepage (`about.md`) renders inside `.page__content` — check
which wrapper you are actually in before writing a defensive selector. Confirm
with `getComputedStyle` rather than by eye; all three of these look like
"my CSS didn't apply".

### Render content in HTML, not from JS

The Volume 1 chapter list was first built by a JS renderer writing into an empty
`<div>`. It built correctly and passed every local check, but on the owner's
browser the script did not run and the section was simply **empty** — header,
search box and nothing else. Nothing in the build was wrong, and it is not
reproducible from here.

So: emit the content as real HTML and let JS only enhance it. The chapter list
now uses native `<details>`/`<summary>`, so every chapter opens and every PDF
downloads with JavaScript switched off entirely; each translatable node carries
`data-en` / `data-es` and JS swaps `textContent` on a language click. Controls
that genuinely need JS (filter, expand-all, copy) are hidden by default and
revealed by a `.bk-js` class the script adds to the section.

Test it: Playwright with `javaScriptEnabled: false` must still show all 17
chapters and 17 download links.

### Phones and tablets: the section pages have real small-screen layouts

Until Nov 2026 **News, Media, Publications and Team** pinned
`<meta name="viewport" content="width=1200">` and showed the desktop layout
scaled down. The owner then asked for them to be phone friendly like the
homepage, so the pin is gone from all four and from the bio pages. Do not put it
back.

- **Shared header card** (`_includes/head/custom.html`, the `max-width:600px`
  block at the end): one compact row, 58px logo tile left, eyebrow and `<h1>`
  right, EN/ES top right. The selectors carry a `body` prefix on purpose: News
  and Media keep their own header CSS in the page, which loads later and would
  otherwise win.
- **Each page's phone rules** are one block at the end of that page's `<style>`.
  News: the pop-up starts below the 70px masthead (the masthead sits above the
  overlay, so a centred pop-up hides its close button). Media: each card is a
  row, 104px thumbnail left. Publications: tighter cards, chevron pinned in the
  chapter bar. Team: one column, each card a row (avatar, text, collective logo).
  Bio: portrait above the text.
- **Tablets (601-900px)** get two columns on News, Media and Publications. The
  pages' older `max-width:900px` rules force one column, which is right for a
  phone and far too wide at 768px.
- The same block removes the theme's `9em` body padding on these pages (via
  `body:has(...)`), which left a tall empty band above the footer.

Test with device profiles (`devices['iPhone 13']`, `['Galaxy S8']`,
`['iPad Mini']`) as well as 1440px, in both languages, and check
`document.documentElement.scrollWidth` equals the viewport width. Desktop must
stay pixel-identical when only phone rules change: build `origin/master` to a
second folder and diff full-page screenshots (looping card videos differ by a
frame, nothing else should).

## Verifying before you push

There is no `.github/workflows` — GitHub Pages runs its own legacy build, and a
failure means the site silently keeps serving the last good build. Build locally
first:

```sh
gem install jekyll -v 3.10.0 jekyll-paginate jekyll-sitemap jekyll-gist \
    jekyll-feed jekyll-redirect-from jekyll-include-cache kramdown-parser-gfm
# run from a directory with no Gemfile, or Jekyll tries to load github-pages
cd /tmp && jekyll build --safe --source <repo> --destination /tmp/_site
```

Then serve `/tmp/_site` and check in a browser at 1440px and 390px, in both
languages. Note that `base_path` renders as the absolute production URL, so
local previews need those requests routed back to the built site.

Check the deployed result with the GitHub Actions API: the "pages build and
deployment" run for the merge commit must be `success`. Its logs are not
retrievable, so a green local `jekyll build --safe` is the real safety net.

### When the deploy times out

The run has two jobs. `build` can pass while `deploy` fails: GitHub copies the
built site and aborts after 10 minutes ("Timeout reached, aborting!" in the
deploy job log, which *is* retrievable with `get_job_logs`). On 10 Nov 2026 the
homepage refresh hit this four times in a row, at 282MB and again at 125MB; the
next re-run then deployed in 43 seconds. So the timeouts were GitHub being slow,
not the site's size. A green `build` job with a timed-out `deploy` is not a
problem with the change: re-run the failed job (`rerun_failed_jobs`), and if it
keeps timing out, wait and re-run later. Never push an empty commit to force it.
The live site keeps serving the last good deploy meanwhile.

Heavy files no page references are still listed under `exclude:` in
`_config.yml` (old GIF originals, 157MB): they stay in the repository but are not
published, which keeps the site at ~125MB. When a large original is replaced by a
lighter version, add the original to that list.

### Moving belts

Strips marked `data-belt` (the "FOUND in Action" photos, all widths) or
`data-belt-mobile` (the gif strip under the timeline, phones only) are plain
swipeable rows in HTML. `setupBelts()` in `about.md` clones the items once and
drifts the row right-to-left by advancing `scrollLeft`, not with a CSS
transform, to keep layout simple. It pauses on hover, touch and zoom, and stays still
under reduced motion.

Tap-to-zoom (`.touch-zoomable`, phones only) opens a separate lightbox
appended to `<body>` — never make the element itself `position:fixed`: the
`.reveal` sections carry transforms, which trap fixed children, and the old
version also locked body scroll. The lightbox closes on tap, swipe or scroll.
The documentary trailer is a poster button that only inserts the YouTube
iframe (`playsinline=1`) when tapped, so a scroll gesture over it can no longer
hit YouTube's own links and open the app.

## Page headers

News, Media, Publications and Team open with the same header card, modelled on
News: the FOUND pin-and-leaf logo (`images/logo_FOUND_leaf.png`, transparent, no
wordmark) in an 88px white tile (`.found-logo-tile`, `object-fit:contain`) on the
left, then an eyebrow and the `<h1>`. **EN/ES sit inside the card, top right** —
the `.lang-toggle` markup goes inside the `<header>` on every page, and shared
rules in `_includes/head/custom.html` place and style it (they override each
page's older `.lang-toggle` CSS). Publications and Team use `.found-header`,
whose CSS there mirrors News's own `.news-header` copy; keep the two in step.
Page shells use `padding:0 var(--shell-pad)` so every header lands at the same
x and width (32px/1377px at 1440, 14px/363px at 390). Do not reintroduce the
cream `Found_logo.jpg` there.

## Team page cards

Each person on `team.md` is a `.team-member` card: a `.team-avatar` circle (initials
written in the HTML, or the portrait `<img>` when one exists), name, role, and a
`.bio-link` when there is a bio page. The Direction group carries
`.team-group--lead` (three larger cards). Page order, set by the owner: Advisors
(the two Jalisco Search Commission members last), Contributors, then Direction at
the very end, with the two co-directors as its last cards. Add a person by copying a card.
A search-collective member's card also carries the collective's logo as
`<img class="team-logo">` (top-right corner, from `images/logos/`, ~240px PNG) —
never in the avatar circle, which is reserved for the person's portrait.

## Team bio pages

A team member with a full biography gets their own page at
`/team/<first-last>/` (e.g. `_pages/team-luis-fondebrider.md`, served at
`found-project.org/team/luis-fondebrider/`). Copy that file for the next one.
It reuses the shared header card, wraps content in `.team-page` (so the theme's
duplicate `page__title` stays hidden); on phones the portrait stacks above the
text. Both language versions of the bio are real HTML blocks (`lang="en"` /
`lang="es" hidden`), so the English one shows with JS off. On `team.md`, link the
name and add a `.bio-link` "Read bio →" with an id in the `T` dictionary.
The owner supplies source bios; paraphrase them (not literal) and show the
draft in EN and ES for approval before posting. Portraits go in `images/team/<first-last>.jpg`
(square, ~600px, flattened onto white, well under 100KB) and sit in the bio card
beside the text.

## Link previews

`og_image` in `_config.yml` is `images/og-found.png` (1200x630, the full
pin-and-wordmark logo `images/logo_FOUND_pin.png` on white). The theme's
`seo.html` only emitted page header images, so it now falls back to
`og_image` for `og:image` and a large Twitter card.

## Event cards and the homepage feature

An event is a News card (`newsCards` in `_pages/news.md`) with `fullImage: true`,
a 1200x630 image (also its link preview), the partner logos in a
`<div class="partner-logos">` row and a `<a class="register-btn">` to the
registration page, in both `en` and `es`. Partner logos live in `images/logos/`
(trimmed PNGs on white, 160px tall). Give it a share page at
`news/cards/<id>/index.html` (copy an existing one). The homepage hero's
`.featured-row` (in `about.md`, inside `.hh-featured`) holds the featured item: a `.featured-pub-card`
with ids `featured-pub-eyebrow|title|meta|link` in both dictionaries, linking to
the News card (`/news/#<id>`); an event's image goes inside that card as
`<span class="featured-pub-img">` (an image, or a looping `<video>` inside
`.featured-pub-vid`). The row now holds **two** highlighted cards: the Oxford
event and the Jalisco machine-learning finding (ids `featured2-*` in both
dictionaries).

The Tree of Hope video lives in **The Role of Buscadoras**, as the first tile of
the photo strip: `.buscadoras-belt-row` holds a still `figure.belt-still` (never
cropped: `object-fit:contain`, `aspect-ratio:400/224`, height matched to the
belt's 4:3 tiles) followed by the moving `data-belt` strip, whose left edge
fades under it. On phones the video stacks full-width above the strip.

## Files and downloads

`files/` is served as-is by Pages, so anything in it is downloadable at
`found-project.org/files/...`. The book's chapters live in
`files/libro-vol1/` (17 chapter PDFs plus the index, ~45MB). The publications
page builds its index, download links and Harvard citations from a JS data
array in `_pages/publications.md` — chapter titles, authors, page ranges and
file sizes are all in that one array, so add or correct a chapter there rather
than in the markup.

## Images

Large source images live in `images/`; several are 6–23MB. Optimise before
referencing anything new on a page (`images/in-the-flowers-web.jpg` is a 329KB
web version of a 6MB PNG). Many `<img>` tags point at
`raw.githubusercontent.com` pinned to a commit — that works, but new assets are
better referenced by site-relative path.

### Search sites: never publish exact locations

Screenshots of Espacio Clandestino, Global Index Mapper or drone tools can carry
the coordinates of a search or recovery site (e.g. the "Carga puntos" text box).
Blur or pixelate them before publishing, and tell the owner you did.

### Small or soft photos

When only a low-resolution or heavily compressed photo exists (e.g. the four
documentary stills, ~490x265 each), upscale it with OpenCV's EDSR x4 model
(`opencv-contrib-python-headless`; weights `EDSR_x4.pb` from the
Saafke/EDSR_Tensorflow repo), after a light `fastNlMeansDenoisingColored` pass,
then blend ~25% of a plain Lanczos upscale back in so skin and fabric keep their
texture, and cut to the exact display size with a mild unsharp mask. In this
sandbox `pip` stalls because PyPI is in `NO_PROXY`; run it with
`NO_PROXY=localhost,127.0.0.1`.

### Animated images

The homepage loads **no GIFs**: the five it used (68MB together) are looping
videos (`site_360`, `ndai5`, `areas_de_busqueda`, `clandestine_space`,
`mothers_walking`, each `.webm` + `.mp4` + `.jpg` poster in `images/`, under 4MB
in total). `setupVideos()` in `about.md` pauses any `video[autoplay]` that is off
screen. The original `.gif` files are still in `images/` but excluded from the
published site (see "When the deploy times out").

GIFs sent in the chat arrive as a single still frame — ask the owner to upload
the file to `images/` on GitHub instead. Large GIFs go on the page as a looping
muted video (`ffmpeg` to `.webm` VP9 + `.mp4` H.264, both as `<source>`s, with
a still `poster`): the 11.5MB Tree of Hope GIF became ~1MB each. News cards take
a `video:` field (path without extension) alongside `image:` for this.
