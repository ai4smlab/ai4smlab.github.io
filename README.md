# AI for Smart Mobility Lab at KFUPM

A modern, responsive, two-theme (light and dark) rebuild of the lab site, generated from the content
of the previous `AI4SM_lab` site. Static HTML, CSS, and JavaScript. No framework, no dependencies to
install, no build step required to serve it.

It shares its design system with [alaakhamis.org](https://alaakhamis.org/), so the personal site and
the lab site read as a family.

## Structure

```
index.html          Home: mission, key figures, research pillars, active projects, latest news
research.html       Current projects, previous projects, collaborator map
team.html           Faculty, researchers, open positions, collaborators
facilities.html     Research platforms and computing infrastructure
publications.html   Books, journal articles, conference papers, knowledge sharing hub
talks.html          Keynotes, seminars, and tutorials
news.html           News and events (searchable)
join.html           Six open positions and how to apply
contact.html        Contact details and online resources
404.html            Not-found page
sitemap.xml         Sitemap
robots.txt          Crawler policy

assets/css/style.css   Design system and every component
assets/js/main.js      Theme toggle, mobile nav, back-to-top, list filtering
images/                Logos, project and facility imagery, team photos
talks/                 Slide decks linked from the talks and news pages

tools/build.py         Regenerates all pages from tools/content.py
tools/content.py       All page copy and data, in plain Python lists
```

Page filenames match the previous site, so existing inbound links keep working.

## Editing

All content lives in `tools/content.py` as ordinary Python lists. Edit it, then run:

```bash
python tools/build.py
```

The build prints a warning next to any page that contains an em dash or a British spelling, so the
house style (American English, no em dashes) is enforced at build time.

Common edits:

- **Add a news item**: prepend a tuple to `NEWS`, as `(year, "html body", None)`. The third slot
  takes `("images/file.jpg", "alt text")` if the item has an image.
- **Add a publication**: add to `JOURNALS` or `CONFERENCES` as
  `(authors, title, venue, [(icon, url, label), ...])`. Available icons are the keys of `I` in
  `tools/build.py`.
- **Add a project**: add to `CURRENT_PROJECTS` or `PAST_PROJECTS`.
- **Add a person**: add to `RESEARCHERS` or `COLLABORATORS`, and drop the photo in `images/team/`.
- **Add or close a position**: edit `POSITIONS`. Each entry generates its own section and its
  table-of-contents entry automatically.

## Design

A technical, geometric template, deliberately distinct from
[alaakhamis.org](https://alaakhamis.org/): Space Grotesk display type, IBM Plex Sans body, IBM Plex
Mono for labels and navigation, square 4px corners, hairline dividers, and numbered section markers
(`01 / RESEARCH PILLARS`).

The accent is **KFUPM green `#027E40`**, sampled directly from the university mark, lifted to
`#4ED18A` in dark mode so it stays legible. The hero, callout, and footer sit on a fixed dark green
ink panel (`#04231A`) that is identical in both themes.

Light is the default; dark applies automatically when the visitor's system prefers it, and the
sun/moon button overrides that, remembered in `localStorage`. The theme is applied by an inline
script in `<head>` before first paint, so there is no flash of the wrong colors. All colors are
custom properties at the top of `assets/css/style.css`.

## The lab mark

`assets/img/mark.svg` is the lab icon: a location pin holding a brain whose right
hemisphere runs out into circuit traces. The pin carries mobility, the brain and traces carry AI, and
together they state the intersection the lab works in.

The brain is built from nine overlapping circles rather than one hand-drawn path, so the lobes union
cleanly and stay symmetric at any size.

The inline copy in `tools/build.py` is theme-adaptive. The tile takes `currentColor`; everything in
the `.glyph` group (pin outline and brain) uses `--accent-contrast`; the `.cut` details (midline,
traces, nodes) are knocked back out in `currentColor`. The same markup therefore renders
white-on-green in the light header, ink-on-mint in the dark header, and ink-on-mint in the footer
(see `.site-footer__mark` for that one override).

One known limitation: below about 24px the brain reads as a shape inside the pin rather than as a
brain. The pin silhouette is what carries recognition at favicon size. This is inherent to the
concept, not to this drawing of it.

## Notes

- The collaborator map on the research page uses Leaflet from unpkg and OpenStreetMap tiles. It needs
  an internet connection to draw tiles; the markers are defined in `COLLABORATOR_UNIS`. Tiles are
  filtered to a dark palette when the dark theme is active.
- The home page hero is text only. The old `AI4SM.png` graphic was removed from it; the image is
  still used on the publications page and `AV2.png` is now the social preview image.
- The home page has no key-figures band and no partner-logo strip; the lab's output is young and the
  page reads better without them. Both are easy to add back later.
- `images/temp/` from the old folder was **not** carried over. It held drafts, notebooks, and a `.env`
  file, none of which belong on a public site.
