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
  `how-to-help`, `team`) stores the choice under the single key **`found-lang`**,
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

## Images

Large source images live in `images/`; several are 6–23MB. Optimise before
referencing anything new on a page (`images/in-the-flowers-web.jpg` is a 329KB
web version of a 6MB PNG). Many `<img>` tags point at
`raw.githubusercontent.com` pinned to a commit — that works, but new assets are
better referenced by site-relative path.
