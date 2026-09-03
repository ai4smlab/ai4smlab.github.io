"""Build the AI for Smart Mobility Lab site.

Content is carried over from the previous AI4SM_lab site and re-laid out on a
technical/geometric template in KFUPM green (#027E40).

    python tools/build.py

House style: American English, no em dashes.
"""

import os
import re
import sys

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = "AI for Smart Mobility Lab"
URL = "https://ai4sm.org/"

NAV = [
    ("index.html", "Home"),
    ("research.html", "Research"),
    ("team.html", "Team"),
    ("facilities.html", "Facilities"),
    ("publications.html", "Publications"),
    ("talks.html", "Talks"),
    ("news.html", "News"),
    ("join.html", "Join"),
    ("contact.html", "Contact"),
]

# The lab mark: a location pin (mobility) holding a brain whose right hemisphere
# runs out into circuit traces (AI).
#
# The tile takes `currentColor`. Everything in `.glyph` is the foreground and
# uses --accent-contrast so it stays legible whichever color the tile is; the
# `.cut` details are knocked back out in the tile color, so they follow
# currentColor automatically. See .site-footer__mark for the mint-tile override.
_PIN = ("M24 4c6.63 0 12 5.37 12 12 0 4.2-2.6 9.3-5.4 13.4"
        "C27.9 33.3 24 41 24 41s-3.9-7.7-6.6-11.6C14.6 25.3 12 20.2 12 16c0-6.63 5.37-12 12-12Z")
_LOBES = [(20, 11.8, 3.2), (24, 10.8, 3.3), (28, 11.8, 3.2),
          (17.8, 15, 3.2), (30.2, 15, 3.2), (24, 14.8, 3.6),
          (19.8, 18.2, 3.2), (28.2, 18.2, 3.2), (24, 18.8, 3.3)]

MARK = (
    '<svg viewBox="0 0 48 48" aria-hidden="true">'
    '<rect width="48" height="48" rx="11" fill="currentColor"/>'
    '<g class="glyph">'
    '<path d="%s" fill="none" stroke="var(--accent-contrast)" stroke-width="3"/>'
    '<g fill="var(--accent-contrast)">%s</g></g>'
    '<g class="cut">'
    '<path d="M24 8.2V21.8" stroke="currentColor" stroke-width="1.6"/>'
    '<path d="M24 12.6h3.6M24 18.4h3M24 15.4h4.4" fill="none" stroke="currentColor"'
    ' stroke-width="1.5" stroke-linecap="round"/>'
    '<g fill="currentColor"><circle cx="27.6" cy="12.6" r="1.4"/>'
    '<circle cx="28.4" cy="15.4" r="1.4"/><circle cx="27" cy="18.4" r="1.4"/></g></g></svg>'
) % (_PIN, "".join('<circle cx="%s" cy="%s" r="%s"/>' % c for c in _LOBES))

# ---------------------------------------------------------------- icons

I = {
    "web": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm0 0c2.8 2.6 4.2 6 4.2 10S14.8 19.4 12 22c-2.8-2.6-4.2-6-4.2-10S9.2 4.6 12 2ZM2.5 9h19M2.5 15h19" fill="none" stroke="currentColor" stroke-width="1.7"/>',
    "github": '<path d="M12 .5a12 12 0 0 0-3.79 23.4c.6.11.82-.26.82-.58v-2.2c-3.34.72-4.04-1.42-4.04-1.42-.55-1.4-1.34-1.77-1.34-1.77-1.09-.75.08-.73.08-.73 1.2.08 1.84 1.24 1.84 1.24 1.07 1.84 2.81 1.31 3.5 1 .1-.78.42-1.31.76-1.61-2.67-.3-5.47-1.34-5.47-5.96 0-1.32.47-2.39 1.24-3.23-.12-.3-.54-1.53.12-3.18 0 0 1.01-.32 3.3 1.23a11.4 11.4 0 0 1 6.01 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.23 0 4.63-2.81 5.65-5.49 5.95.43.37.82 1.1.82 2.22v3.29c0 .32.21.7.83.58A12 12 0 0 0 12 .5Z"/>',
    "scholar": '<path d="M12 2 1 8.5 12 15l9-5.32V16h2V8.5L12 2Z"/><path d="M5.5 12.1v3.6c0 2.2 2.9 4 6.5 4s6.5-1.8 6.5-4v-3.6L12 16.2l-6.5-4.1Z"/>',
    "amazon": '<path d="M2.6 16.2c3.2 2.3 7.2 3.5 11 3.5 2.6 0 5.4-.55 8.1-1.7.4-.17.74.27.35.57-2.4 1.8-5.9 2.75-8.9 2.75-4.2 0-8-1.55-10.9-4.15-.23-.2-.03-.5.35-.97Zm19.2.9c-.3-.4-2-.2-2.8-.1-.24.03-.28-.18-.06-.34 1.36-.95 3.58-.68 3.84-.36.26.33-.07 2.56-1.34 3.63-.2.16-.38.07-.3-.14.28-.7.9-2.28.66-2.69ZM13.4 10.5c0 1.1.03 2-.53 2.97-.45.78-1.16 1.26-1.96 1.26-1.08 0-1.72-.83-1.72-2.06 0-2.42 2.17-2.86 4.21-2.86v.69Zm2.83 6.85a.58.58 0 0 1-.66.07c-.93-.77-1.1-1.13-1.6-1.86-1.54 1.57-2.63 2.04-4.62 2.04-2.36 0-4.2-1.46-4.2-4.37 0-2.28 1.24-3.83 3-4.59 1.53-.67 3.67-.79 5.3-.97v-.36c0-.67.05-1.46-.34-2.03-.34-.52-1-.73-1.57-.73-1.07 0-2.02.55-2.25 1.68-.05.25-.23.5-.48.51l-2.7-.29c-.23-.05-.48-.23-.41-.58C6.32 2.68 8.94 1.8 11.3 1.8c1.2 0 2.78.32 3.73 1.23 1.2 1.13 1.09 2.63 1.09 4.27v3.86c0 1.16.48 1.67.93 2.3.16.22.2.49-.01.65-.5.42-1.4 1.2-1.9 1.64l-.01-.01Z"/>',
    "arxiv": '<path d="M4 4h4l5.2 7.4L18.6 4H21l-6.6 9 6.8 7h-4.1l-5.4-6-4.5 6H4.6l6-8L4 4Z"/>',
    "linkedin": '<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.6 4.78 6V21h-4v-5.3c0-1.27-.02-2.9-1.8-2.9-1.8 0-2.08 1.38-2.08 2.8V21h-4z"/>',
    "researchgate": '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2Zm-1.1 5.6h2.5c1.9 0 3 .95 3 2.55 0 1.2-.66 2.05-1.7 2.4l2.2 3.85h-1.9l-2-3.6h-1.2v3.6H10.9V7.6Zm1.9 1.35v2.55h.85c.95 0 1.45-.45 1.45-1.3 0-.83-.5-1.25-1.45-1.25h-.85Z"/>',
    "medium": '<path d="M13.54 12a6.8 6.8 0 0 1-6.77 6.82A6.8 6.8 0 0 1 0 12a6.8 6.8 0 0 1 6.77-6.82A6.8 6.8 0 0 1 13.54 12ZM20.96 12c0 3.54-1.51 6.42-3.38 6.42S14.2 15.54 14.2 12s1.51-6.42 3.38-6.42S20.96 8.46 20.96 12ZM24 12c0 3.17-.53 5.75-1.19 5.75-.66 0-1.19-2.58-1.19-5.75s.53-5.75 1.19-5.75C23.47 6.25 24 8.83 24 12Z"/>',
    "youtube": '<path d="M23.5 6.5a3 3 0 0 0-2.1-2.1C19.5 3.9 12 3.9 12 3.9s-7.5 0-9.4.5A3 3 0 0 0 .5 6.5C0 8.4 0 12 0 12s0 3.6.5 5.5a3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1c.5-1.9.5-5.5.5-5.5s0-3.6-.5-5.5ZM9.6 15.6V8.4l6.2 3.6-6.2 3.6Z"/>',
    "email": '<path d="M2 5.5A2.5 2.5 0 0 1 4.5 3h15A2.5 2.5 0 0 1 22 5.5v13a2.5 2.5 0 0 1-2.5 2.5h-15A2.5 2.5 0 0 1 2 18.5v-13Zm2.3-.5 7.7 5.9L19.7 5H4.3ZM20 7.3l-7.4 5.66a1 1 0 0 1-1.2 0L4 7.3V18.5c0 .28.22.5.5.5h15a.5.5 0 0 0 .5-.5V7.3Z"/>',
    "phone": '<path d="M6.6 2h3l1.6 4-2 1.4a13 13 0 0 0 5.4 5.4l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A17.6 17.6 0 0 1 2 6.2 2 2 0 0 1 4 4h2.6Z"/>',
    "pin": '<path d="M12 22s7-6.1 7-11.2A7 7 0 0 0 5 10.8C5 15.9 12 22 12 22Zm0-8.6a2.8 2.8 0 1 1 0-5.6 2.8 2.8 0 0 1 0 5.6Z"/>',
    "slides": '<path d="M3 4h18v11H3zM3 4h18M12 15v3m-4 3h8l-4-3-4 3Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    "users": '<path d="M8.5 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7ZM1.5 20a7 7 0 0 1 14 0zM17 11.2a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM17.2 13c2.9 0 5.3 2.3 5.3 5.2V20h-5.6v-1.4c0-2-.7-3.9-1.9-5.3.7-.2 1.4-.3 2.2-.3Z"/>',
}


def icon(name):
    body = I[name]
    fill = "none" if 'fill="none"' in body else "currentColor"
    return '<svg viewBox="0 0 24 24" fill="%s" aria-hidden="true">%s</svg>' % (fill, body)


ICON_SUN = ('<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
            'stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/>'
            '<path d="M12 2v2.4M12 19.6V22M2 12h2.4M19.6 12H22M4.9 4.9l1.7 1.7M17.4 17.4l1.7 1.7'
            'M19.1 4.9l-1.7 1.7M6.6 17.4l-1.7 1.7"/></svg>')
ICON_MOON = ('<svg class="moon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
             '<path d="M21 13.2A8.6 8.6 0 0 1 10.8 3 8.6 8.6 0 1 0 21 13.2Z"/></svg>')

SOCIAL = [
    ("https://github.com/ai4smlab", "GitHub", "github"),
    ("https://medium.com/ai4sm", "Medium publication", "medium"),
    ("https://www.youtube.com/@AI4SM_lab", "YouTube channel", "youtube"),
    ("mailto:alaa.rashwan@kfupm.edu.sa", "Email", "email"),
]


def social_html():
    out = ['<div class="social">']
    for url, label, ic in SOCIAL:
        ext = "" if url.startswith("mailto:") else ' target="_blank" rel="noopener noreferrer"'
        out.append('<a href="%s"%s aria-label="%s" title="%s">%s</a>' % (url, ext, label, label, icon(ic)))
    out.append("</div>")
    return "\n".join(out)


def nav_html(active):
    items = "\n".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else "", l)
        for h, l in NAV)
    return '<nav class="nav" id="primary-nav" aria-label="Primary">\n%s\n</nav>' % items


def shell(active, title, description, body, head_extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="AI for Smart Mobility, AI4SM, KFUPM, smart mobility, software-defined vehicles, agentic AI, seamless integrated mobility, last-mile delivery, intelligent transportation">
<link rel="canonical" href="{URL}{'' if active == 'index.html' else active}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE} at KFUPM">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{URL}{'' if active == 'index.html' else active}">
<meta property="og:image" content="{URL}images/AV2.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#027e40">
<link rel="icon" href="assets/img/mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
<script>
  // Set the theme before first paint so there is no flash of the wrong colors.
  (function () {{
    try {{
      var t = localStorage.getItem("theme");
      if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
    }} catch (e) {{}}
  }})();
</script>
{head_extra}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar">
  <div class="wrap mono">
    <span>King Fahd University of Petroleum and Minerals</span>
    <span class="topbar__right">
      <a href="https://ri.kfupm.edu.sa/irc-sml" target="_blank" rel="noopener noreferrer">IRC-SML</a>
      <a href="https://ise.kfupm.edu.sa/" target="_blank" rel="noopener noreferrer">ISE Department</a>
      <a href="join.html">We are hiring</a>
    </span>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="brand__mark">{MARK}</span>
      <span class="brand__text">
        <span class="brand__name">AI for Smart Mobility Lab</span>
        <span class="brand__sub">Research Lab</span>
      </span>
    </a>
    {nav_html(active)}
    <button class="icon-btn theme-toggle" type="button" aria-label="Switch theme" aria-pressed="false">{ICON_SUN}{ICON_MOON}</button>
    <button class="icon-btn nav-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false" aria-controls="primary-nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="site-footer__grid">
      <div>
        <div class="site-footer__mark">{MARK}<span>AI for Smart Mobility Lab</span></div>
        <p>Part of the Interdisciplinary Research Center for Smart Mobility and Logistics,
           King Fahd University of Petroleum and Minerals, Dhahran, Saudi Arabia.</p>
        {social_html()}
      </div>
      <div>
        <h4>Explore</h4>
        <ul class="footer-links">
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="facilities.html">Facilities</a></li>
          <li><a href="publications.html">Publications</a></li>
        </ul>
      </div>
      <div>
        <h4>Connect</h4>
        <ul class="footer-links">
          <li><a href="join.html">Open positions</a></li>
          <li><a href="news.html">News and events</a></li>
          <li><a href="contact.html">Contact and resources</a></li>
          <li><a href="https://ri.kfupm.edu.sa/irc-sml" target="_blank" rel="noopener noreferrer">IRC-SML at KFUPM</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      <span>&copy; <span id="year">2026</span> {SITE} at KFUPM</span>
      <span>Directed by <a href="https://alaakhamis.org/" target="_blank" rel="noopener noreferrer">Dr. Alaa Khamis</a></span>
    </div>
  </div>
</footer>

<button class="to-top" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def page_header(title, subtitle="", label="AI4SM Lab"):
    sub = '<p class="page-header__sub">%s</p>' % subtitle if subtitle else ""
    return """<section class="page-header">
  <div class="wrap">
    <div class="section__label">%s</div>
    <h1>%s</h1>
    %s
  </div>
</section>
""" % (label, title, sub)


def section(num, title, body, alt=False, lead="", wrap="wrap", more=None):
    label = '<div class="section__label">%s / %s</div>' % (num, title.upper())
    head = "<div>%s<h2>%s</h2>%s</div>" % (label, title, "<p>%s</p>" % lead if lead else "")
    head += ('<a class="link-more" href="%s">%s</a>' % more) if more else "<div></div>"
    return """<section class="section%s">
  <div class="%s">
    <div class="section__head">%s</div>
%s
  </div>
</section>
""" % (" section--alt" if alt else "", wrap, head, body)


BRITISH = re.compile(
    r"\bhonours?\b|\bcolours?\b|\bprogramme[s]?\b|\bcentre[s]?\b|\bdefence\b|\bmodelling\b|"
    r"\btowards\b|\bwhilst\b|\bamongst\b|\bcatalogue\b|\blicence\b|\bbehaviour[s]?\b|"
    r"\b(?:organis|optimis|recognis|specialis|realis)(?:e|es|ed|ing|ation|ations)\b", re.I)


def write(name, text):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    flags = []
    if "—" in text or "&mdash;" in text:
        flags.append("EM DASH")
    flags += sorted({m.group(0) for m in BRITISH.finditer(text)})
    print("wrote %-20s %6.1f KB %s" % (name, len(text) / 1024.0,
                                       ("!! " + ", ".join(flags)) if flags else ""))


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content  # noqa: E402

if __name__ == "__main__":
    for name, title, desc, body, extra in content.pages(
            page_header=page_header, section=section, icon=icon, social_html=social_html):
        write(name, shell(name, title, desc, body, extra))
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % URL)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
                         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
                         % "\n".join("  <url><loc>%s%s</loc></url>"
                                     % (URL, "" if h == "index.html" else h) for h, _ in NAV))
    print("done")
