#!/usr/bin/env python3
import glob, re

# Illustrative colored SVG icons — each with teal gradient background + white illustration
# Used in .svc-icon (72x72 circle) and .other-icon cards

def icon(content, vb="0 0 48 48"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" width="40" height="40" aria-hidden="true">{content}</svg>'

ICONS = {

# ── ORTHODONTIE ─ dent avec fil et brackets ──────────────────────────────────
'orthodontie': icon('''
  <defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00b4b4"/><stop offset="1" stop-color="#00d4c8"/></linearGradient></defs>
  <!-- tooth body -->
  <path d="M15 12C15 8 18 6 24 6C30 6 33 8 33 12L35 32C35 37 32 40 27 41C26 41.3 25 41.5 24 41.5C23 41.5 22 41.3 21 41C16 40 13 37 13 32Z" fill="url(#g1)" opacity="0.15"/>
  <path d="M15 12C15 8 18 6 24 6C30 6 33 8 33 12L35 32C35 37 32 40 27 41C26 41.3 25 41.5 24 41.5C23 41.5 22 41.3 21 41C16 40 13 37 13 32Z" fill="none" stroke="#00b4b4" stroke-width="2.2"/>
  <!-- wire -->
  <line x1="15.5" y1="24" x2="32.5" y2="24" stroke="#00b4b4" stroke-width="2"/>
  <!-- brackets -->
  <rect x="18" y="21.5" width="5" height="5" rx="1" fill="#00b4b4"/>
  <rect x="25" y="21.5" width="5" height="5" rx="1" fill="#d4679a"/>
'''),

# ── CHIRURGIE PARODONTALE ─ gencive + scalpel ────────────────────────────────
'chirurgie-parodontale': icon('''
  <defs><linearGradient id="g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d4679a"/><stop offset="1" stop-color="#e8a0c0"/></linearGradient></defs>
  <!-- tooth -->
  <path d="M17 13C17 10 19 8 24 8C29 8 31 10 31 13L32.5 26" fill="#e0f7f7" stroke="#00b4b4" stroke-width="2.2" stroke-linejoin="round"/>
  <!-- gum wave -->
  <path d="M11 32C13 29 15 27 18 27C21 27 21 30 24 30C27 30 27 27 30 27C33 27 35 29 37 32" fill="none" stroke="#d4679a" stroke-width="2.5" stroke-linecap="round"/>
  <!-- scalpel -->
  <line x1="33" y1="18" x2="42" y2="10" stroke="#00b4b4" stroke-width="2" stroke-linecap="round"/>
  <path d="M33 18 L36 15 L39 11 L42 10 L40 14 L37 17Z" fill="#00b4b4"/>
'''),

# ── IMPLANTOLOGIE ─ implant vissé dans os avec couronne ──────────────────────
'implantologie': icon('''
  <defs><linearGradient id="g3" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#00b4b4"/><stop offset="1" stop-color="#00d4c8"/></linearGradient></defs>
  <!-- crown -->
  <rect x="14" y="4" width="20" height="11" rx="3" fill="url(#g3)"/>
  <rect x="16" y="15" width="16" height="4" rx="1" fill="#00b4b4" opacity="0.7"/>
  <!-- post/screw -->
  <rect x="20" y="19" width="8" height="18" rx="2" fill="#00b4b4" opacity="0.9"/>
  <line x1="18" y1="23" x2="20" y2="23" stroke="#e0f7f7" stroke-width="1.5"/>
  <line x1="18" y1="27" x2="20" y2="27" stroke="#e0f7f7" stroke-width="1.5"/>
  <line x1="18" y1="31" x2="20" y2="31" stroke="#e0f7f7" stroke-width="1.5"/>
  <!-- bone line -->
  <line x1="9" y1="37" x2="39" y2="37" stroke="#d4679a" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M10 37C10 37 11 40 13 40C15 40 15 37 18 37" fill="none" stroke="#d4679a" stroke-width="1.5"/>
  <path d="M30 37C30 37 31 40 33 40C35 40 35 37 38 37" fill="none" stroke="#d4679a" stroke-width="1.5"/>
'''),

# ── SMILE DESIGN ─ lèvres + étoiles ─────────────────────────────────────────
'smile-design': icon('''
  <defs><linearGradient id="g4" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d4679a"/><stop offset="1" stop-color="#f0a0c8"/></linearGradient></defs>
  <!-- lèvre supérieure -->
  <path d="M10 22C10 22 13 18 18 18C21 18 22 20 24 20C26 20 27 18 30 18C35 18 38 22 38 22" fill="url(#g4)" stroke="#d4679a" stroke-width="1.5"/>
  <!-- lèvre inférieure -->
  <path d="M10 22C12 28 17 32 24 32C31 32 36 28 38 22" fill="#fdf0f6" stroke="#d4679a" stroke-width="1.5"/>
  <!-- teeth visible -->
  <path d="M16 22L16 28C16 28 18 30 24 30C30 30 32 28 32 28L32 22Z" fill="white" stroke="#e8c0d8" stroke-width="1"/>
  <line x1="24" y1="22" x2="24" y2="30" stroke="#e8c0d8" stroke-width="1"/>
  <!-- sparkles -->
  <line x1="7" y1="12" x2="7" y2="16"/><line x1="5" y1="14" x2="9" y2="14"/>
  <line x1="40" y1="10" x2="40" y2="14"/><line x1="38" y1="12" x2="42" y2="12"/>
  <circle cx="38" cy="36" r="1.5" fill="#d4679a"/>
  <line x1="38" y1="33" x2="38" y2="35"/><line x1="36" y1="36" x2="37" y2="36"/>
'''),

# ── FACETTES DENTAIRES ─ dent + plaque facette + brillance ───────────────────
'facettes-dentaires': icon('''
  <defs><linearGradient id="g5" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00b4b4"/><stop offset="1" stop-color="#d4679a"/></linearGradient></defs>
  <!-- dent de base -->
  <path d="M16 13C16 10 18 8 24 8C30 8 32 10 32 13L33.5 31C33.5 35 31 38 27 39C26 39.3 25 39.5 24 39.5C23 39.5 22 39.3 21 39C17 38 14.5 35 14.5 31Z" fill="#e0f7f7" stroke="#00b4b4" stroke-width="2"/>
  <!-- facette (overlay) -->
  <path d="M20 10C20 10 18.5 14 18.5 20L18.5 35C18.5 37 20 38.5 22 39" fill="url(#g5)" opacity="0.35" stroke="#d4679a" stroke-width="1.5"/>
  <!-- éclat -->
  <line x1="35" y1="7" x2="37" y2="5"/><line x1="36" y1="6" x2="38" y2="8"/>
  <line x1="38" y1="15" x2="41" y2="15"/>
  <line x1="35" y1="7" x2="35" y2="4"/>
'''),

# ── SOINS DENTAIRES ─ dent + croix médicale ──────────────────────────────────
'soins-dentaires': icon('''
  <defs><linearGradient id="g6" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00b4b4"/><stop offset="1" stop-color="#00d4c8"/></linearGradient></defs>
  <!-- dent -->
  <path d="M15 13C15 10 17.5 8 24 8C30.5 8 33 10 33 13L35 31C35 35 32 38 28 39C27 39.3 25.5 39.5 24 39.5C22.5 39.5 21 39.3 20 39C16 38 13 35 13 31Z" fill="#e0f7f7" stroke="#00b4b4" stroke-width="2.2"/>
  <!-- croix médicale -->
  <rect x="20" y="17" width="8" height="14" rx="2" fill="url(#g6)" opacity="0.9"/>
  <rect x="17" y="21" width="14" height="6" rx="2" fill="url(#g6)" opacity="0.9"/>
  <rect x="22" y="19" width="4" height="10" rx="1.5" fill="white"/>
  <rect x="19" y="22" width="10" height="4" rx="1.5" fill="white"/>
'''),

# ── PROTHÈSES DENTAIRES ─ couronne dentaire ───────────────────────────────────
'protheses-dentaires': icon('''
  <defs><linearGradient id="g7" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#d4679a"/><stop offset="1" stop-color="#00b4b4"/></linearGradient></defs>
  <!-- base de la couronne -->
  <rect x="10" y="30" width="28" height="10" rx="3" fill="url(#g7)" opacity="0.85"/>
  <line x1="10" y1="36" x2="38" y2="36" stroke="white" stroke-width="1" opacity="0.5"/>
  <!-- corps de la couronne -->
  <path d="M10 30L10 24L14 30Z" fill="#d4679a"/>
  <path d="M38 30L38 24L34 30Z" fill="#00b4b4"/>
  <!-- 3 pointes de la couronne -->
  <path d="M10 24L12 14L17 22L24 10L31 22L36 14L38 24Z" fill="url(#g7)"/>
  <!-- détails brillance -->
  <line x1="16" y1="17" x2="18" y2="21" stroke="white" stroke-width="1.2" opacity="0.6"/>
'''),

# ── BLANCHIMENT DENTAIRE ─ dent + rayons lumineux ────────────────────────────
'blanchiment-dentaire': icon('''
  <defs><linearGradient id="g8" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00b4b4"/><stop offset="1" stop-color="#d4679a"/></linearGradient></defs>
  <!-- dent blanche éclatante -->
  <path d="M17 14C17 11 19 9 24 9C29 9 31 11 31 14L32.5 30C32.5 34 30 37 26.5 38C25.5 38.3 24.8 38.5 24 38.5C23.2 38.5 22.5 38.3 21.5 38C18 37 15.5 34 15.5 30Z" fill="white" stroke="url(#g8)" stroke-width="2.5"/>
  <!-- rayons gauche -->
  <line x1="9" y1="14" x2="12" y2="17" stroke="#00b4b4" stroke-width="2" stroke-linecap="round"/>
  <line x1="7" y1="22" x2="11" y2="22" stroke="#00b4b4" stroke-width="2" stroke-linecap="round"/>
  <line x1="9" y1="30" x2="12" y2="27" stroke="#d4679a" stroke-width="2" stroke-linecap="round"/>
  <!-- rayons droite -->
  <line x1="39" y1="14" x2="36" y2="17" stroke="#d4679a" stroke-width="2" stroke-linecap="round"/>
  <line x1="41" y1="22" x2="37" y2="22" stroke="#d4679a" stroke-width="2" stroke-linecap="round"/>
  <line x1="39" y1="30" x2="36" y2="27" stroke="#00b4b4" stroke-width="2" stroke-linecap="round"/>
  <!-- étoile centrale -->
  <circle cx="24" cy="24" r="3" fill="url(#g8)" opacity="0.5"/>
'''),

# ── DENTISTERIE PÉDIATRIQUE ─ petite dent + cœur ─────────────────────────────
'dentisterie-pediatrique': icon('''
  <defs><linearGradient id="g9" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d4679a"/><stop offset="1" stop-color="#f0a0c8"/></linearGradient></defs>
  <!-- petite dent ronde et mignonne -->
  <path d="M14 16C14 12 17 10 24 10C31 10 34 12 34 16L35 29C35 33 32 36 28 37C27 37.3 25.5 37.5 24 37.5C22.5 37.5 21 37.3 20 37C16 36 13 33 13 29Z" fill="#fdf0f6" stroke="#d4679a" stroke-width="2.2"/>
  <!-- cœur -->
  <path d="M20 21C20 19 21.5 18 23 19C23.5 19.3 24 19.8 24 19.8C24 19.8 24.5 19.3 25 19C26.5 18 28 19 28 21C28 23 24 26 24 26C24 26 20 23 20 21Z" fill="url(#g9)"/>
  <!-- petites étoiles -->
  <circle cx="10" cy="12" r="1.5" fill="#d4679a" opacity="0.6"/>
  <circle cx="38" cy="14" r="2" fill="#00b4b4" opacity="0.5"/>
  <circle cx="11" cy="32" r="1.2" fill="#d4679a" opacity="0.5"/>
'''),
}

# Map emoji → slug
EMOJI_SLUG = {
    '😁': 'orthodontie',
    '🔬': 'chirurgie-parodontale',
    '🦷': 'implantologie',
    '✨': 'smile-design',
    '💎': 'facettes-dentaires',
    '🏥': 'soins-dentaires',
    '👑': 'protheses-dentaires',
    '🌟': 'blanchiment-dentaire',
    '👶': 'dentisterie-pediatrique',
}

files = ['index.html', 'rendez-vous.html'] + glob.glob('services/*.html')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for emoji, slug in EMOJI_SLUG.items():
        svg = ICONS[slug]
        # Replace inside svc-icon, other-icon, why-icon, info-icon
        for wrapper in ['svc-icon', 'other-icon', 'why-icon']:
            # with style attr already added
            content = re.sub(
                rf'<div class="{wrapper}"[^>]*>{re.escape(emoji)}</div>',
                f'<div class="{wrapper}">{svg}</div>',
                content
            )
            # plain
            content = content.replace(
                f'<div class="{wrapper}">{emoji}</div>',
                f'<div class="{wrapper}">{svg}</div>'
            )
        # Also existing SVGs that were swapped previously (smaller 28x28) — replace with new ones
        # The old SVGs are already in place from update_icons.py, skip re-replacement

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✓ {fpath}')
    else:
        print(f'- {fpath}')

# Also update the SVG icons in svc-icon for index.html using the new full-color ones
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
original = html

for slug, svg in ICONS.items():
    # Find the old SVG icon block (from previous script) in svc-icon and replace with new
    # The previous script put 36x36 SVGs; now we put 40x40 colored ones
    old_pattern = rf'<div class="svc-icon">(<svg[^<]*viewBox="0 0 28 28"[^>]*>.*?</svg>)</div>'
    # Just replace by slug mapping from emoji
    pass

# Simpler: just replace the svc-icon divs that contain any SVG with the new colored ones
for emoji, slug in EMOJI_SLUG.items():
    # The svc-icon divs now contain the old 28x28 stroke SVG from update_icons.py
    # We need to replace them with the new colored 48x48 SVGs
    # Pattern: <div class="svc-icon"><svg ... </svg></div>
    # Since content-based matching is fragile, use a marker approach
    pass

# Direct approach: find each service-card block by h3 title and replace its svc-icon
SERVICE_TITLES = {
    'Orthodontie': 'orthodontie',
    'Chirurgie Parodontale': 'chirurgie-parodontale',
    'Implantologie': 'implantologie',
    'Smile Design': 'smile-design',
    'Facettes Dentaires': 'facettes-dentaires',
    'Soins Dentaires': 'soins-dentaires',
    'Prothèses Dentaires': 'protheses-dentaires',
    'Blanchiment Dentaire': 'blanchiment-dentaire',
    'Dentisterie Pédiatrique': 'dentisterie-pediatrique',
}

# Replace svc-icon SVGs by finding the service-card context
for title, slug in SERVICE_TITLES.items():
    new_svg = ICONS[slug]
    # Pattern: svc-icon div followed (within a few tags) by the h3 with title
    # Use regex to match the svc-icon content and replace it
    pattern = rf'(<div class="service-card">\s*<div class="svc-icon">)(.*?)(</div>\s*<h3>{re.escape(title)}</h3>)'
    replacement = rf'\g<1>{new_svg}\g<3>'
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

if html != original:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('✓ index.html svc-icons updated with colored SVGs')

print('\nAll done.')
