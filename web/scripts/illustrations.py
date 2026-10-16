"""Generates the practice-area illustrations in public/illustrations/.

Style: still-life scenes of legal objects (documents, folders, wax seals,
gavels, scales, law books, court buildings) on a dark card with soft shadows,
in the firm's letterhead palette: near-black, paper white and one red accent.
Run:  python3 scripts/illustrations.py
"""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'public' / 'illustrations'
RED, RED_D = '#EF363A', '#B3141A'
PAPER, PAPER_D, INK = '#F4F3EF', '#DCDBD6', '#B9BBBF'
DARK, DARK2 = '#2A2E34', '#3A3F46'
W = lambda a: f'rgba(255,255,255,{a})'

DEFS = f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1D2025"/><stop offset="1" stop-color="#0B0C0E"/></linearGradient>
<radialGradient id="glow" cx=".82" cy=".12" r=".75"><stop offset="0" stop-color="{RED}" stop-opacity=".2"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></radialGradient>
<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4A4F57"/><stop offset="1" stop-color="#23262B"/></linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F2F2F0"/><stop offset="1" stop-color="#A9ACB1"/></linearGradient>
<linearGradient id="redg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F45155"/><stop offset="1" stop-color="{RED_D}"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="9" stdDeviation="10" flood-color="#000" flood-opacity=".5"/></filter>
</defs>'''


def g(body, x=0, y=0, rot=0, s=1, shadow=True):
    f = ' filter="url(#sh)"' if shadow else ''
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"{f}>{body}</g>'


def paper(w, h, lines=8, heading=True, sign=False, ruled_from=0):
    """A sheet of paper drawn from 0,0."""
    out = f'<rect width="{w}" height="{h}" rx="4" fill="{PAPER}"/>'
    y = 22
    if heading:
        out += f'<rect x="18" y="{y}" width="{w*.5:.0f}" height="8" rx="2" fill="#5B5F66"/>'
        y += 24
    for i in range(lines):
        lw = w - 36 - (30 if i % 3 == 2 else 0)
        out += f'<rect x="18" y="{y + ruled_from}" width="{lw}" height="4" rx="2" fill="{INK}"/>'
        y += 13
    if sign:
        out += f'<path d="M20 {h-26}c8 -12 14 5 22 -6c6 -9 11 3 20 -3" fill="none" stroke="#2C3E66" stroke-width="2.2" stroke-linecap="round"/>'
        out += f'<rect x="18" y="{h-18}" width="70" height="2" fill="{INK}"/>'
    return out


def seal(r=26, emblem='scales'):
    """Red wax seal with a scalloped edge, centred on 0,0."""
    pts = []
    for i in range(36):
        a = i / 36 * 2 * math.pi
        rr = r if i % 2 == 0 else r * .9
        pts.append(f'{rr*math.cos(a):.1f},{rr*math.sin(a):.1f}')
    out = f'<polygon points="{" ".join(pts)}" fill="url(#redg)"/>'
    out += f'<circle r="{r*.66:.1f}" fill="none" stroke="rgba(255,255,255,.45)" stroke-width="1.5"/>'
    if emblem == 'scales':
        k = r / 26
        out += (f'<g transform="scale({k:.2f})" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M0 -10v20M-6 10h12M-10 -6h20M-10 -6l-4 8h8zM10 -6l-4 8h8z"/></g>')
    return out


def gavel(rot=-35):
    """Gavel centred on its head."""
    head = (f'<rect x="-40" y="-17" width="80" height="34" rx="7" fill="url(#wood)"/>'
            f'<rect x="-48" y="-21" width="12" height="42" rx="4" fill="#5A606A"/><rect x="36" y="-21" width="12" height="42" rx="4" fill="#5A606A"/>'
            f'<rect x="-30" y="-17" width="4" height="34" fill="{RED}" opacity=".9"/><rect x="26" y="-17" width="4" height="34" fill="{RED}" opacity=".9"/>'
            f'<rect x="-36" y="-14" width="72" height="5" rx="2" fill="rgba(255,255,255,.12)"/>')
    handle = f'<rect x="-6" y="14" width="12" height="96" rx="6" fill="url(#wood)"/><rect x="-7" y="96" width="14" height="18" rx="7" fill="#5A606A"/>'
    return f'<g transform="rotate({rot})">{handle}{head}</g>'


def block(w=110):
    return (f'<rect x="{-w/2}" y="0" width="{w}" height="18" rx="6" fill="url(#wood)"/>'
            f'<rect x="{-w/2+12}" y="-10" width="{w-24}" height="12" rx="5" fill="#4A4F57"/>'
            f'<rect x="{-w/2+12}" y="-10" width="{w-24}" height="3" rx="1.5" fill="rgba(255,255,255,.15)"/>')


def scales(tilt=0, s=1):
    """Scales of justice, base at 0,0."""
    t = math.radians(tilt)
    lx, ly = -58 * math.cos(t), -96 - 58 * math.sin(t)
    rx, ry = 58 * math.cos(t), -96 + 58 * math.sin(t)
    pan = lambda x, y: (f'<path d="M{x} {y} L{x-22} {y+44} M{x} {y} L{x+22} {y+44}" stroke="url(#metal)" stroke-width="1.6"/>'
                        f'<path d="M{x-30} {y+44} Q{x} {y+72} {x+30} {y+44} Z" fill="url(#metal)"/><rect x="{x-31}" y="{y+42}" width="62" height="4" rx="2" fill="#E8E8E6"/>')
    return (f'<g transform="scale({s})" stroke-linecap="round">'
            f'<rect x="-34" y="-8" width="68" height="10" rx="4" fill="url(#metal)"/>'
            f'<rect x="-4" y="-104" width="8" height="98" rx="3" fill="url(#metal)"/>'
            f'<circle cx="0" cy="-110" r="8" fill="{RED}"/>'
            f'<line x1="{lx:.1f}" y1="{ly:.1f}" x2="{rx:.1f}" y2="{ry:.1f}" stroke="url(#metal)" stroke-width="6"/>'
            f'{pan(lx, ly)}{pan(rx, ry)}</g>')


def books(n=3):
    cols = [RED_D, '#3A3F46', '#E6E3DC', '#25292E']
    out = ''
    for i in range(n):
        y = -i * 22
        w = 150 - i * 14
        c = cols[i % len(cols)]
        out += (f'<rect x="{-w/2 + i*4}" y="{y-20}" width="{w}" height="22" rx="3" fill="{c}"/>'
                f'<rect x="{-w/2 + i*4 + 10}" y="{y-14}" width="{w-20}" height="2" fill="rgba(255,255,255,.35)"/>'
                f'<rect x="{-w/2 + i*4 + 10}" y="{y-6}" width="{w-20}" height="2" fill="rgba(255,255,255,.35)"/>'
                f'<rect x="{w/2 + i*4 - 6}" y="{y-18}" width="5" height="18" fill="{PAPER_D}"/>')
    return out


def folder(w=170, h=120, tab=RED):
    return (f'<path d="M0 12 a8 8 0 0 1 8 -8 h44 l10 10 h{w-70} a8 8 0 0 1 8 8 v{h-22} a8 8 0 0 1 -8 8 h-{w-8} a8 8 0 0 1 -8 -8z" fill="{DARK}"/>'
            f'<rect x="10" y="-8" width="{w-30}" height="{h-20}" rx="3" fill="{PAPER}" transform="rotate(-3)"/>'
            f'<path d="M0 30 h{w} v{h-30} a8 8 0 0 1 -8 8 h-{w-16} a8 8 0 0 1 -8 -8z" fill="{DARK2}"/>'
            f'<rect x="18" y="44" width="70" height="16" rx="3" fill="{tab}"/>'
            f'<rect x="18" y="72" width="{w-60}" height="4" rx="2" fill="rgba(255,255,255,.18)"/>')


def pen(rot=-40, s=1):
    return (f'<g transform="rotate({rot}) scale({s})">'
            f'<rect x="-6" y="-70" width="12" height="96" rx="6" fill="#16181B"/>'
            f'<rect x="-6" y="-70" width="12" height="30" rx="6" fill="#26292E"/>'
            f'<rect x="-6.5" y="-42" width="13" height="5" fill="url(#metal)"/>'
            f'<rect x="4" y="-66" width="3" height="30" rx="1.5" fill="url(#metal)"/>'
            f'<path d="M-6 26 L0 50 L6 26 Z" fill="url(#metal)"/><path d="M0 32v14" stroke="#555" stroke-width="1"/></g>')


def column_bg():
    """Faint court columns in the background."""
    return ''.join(f'<rect x="{x}" y="30" width="22" height="300" rx="3" fill="rgba(255,255,255,.035)"/>' for x in (30, 80, 400, 440)) + \
        '<rect x="20" y="22" width="440" height="10" rx="3" fill="rgba(255,255,255,.035)"/>'


def svg(title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{DEFS}'
            f'<rect width="480" height="360" rx="22" fill="url(#bg)"/><rect width="480" height="360" rx="22" fill="url(#glow)"/>'
            f'{column_bg()}{body}</svg>')


def coins(n=5):
    return ''.join(f'<ellipse cx="0" cy="{-i*10}" rx="34" ry="11" fill="{"#C9CBCF" if i % 2 else "#E8E8E6"}" stroke="#8D9095" stroke-width="1"/>' for i in range(n)) + \
        f'<ellipse cx="0" cy="{-(n-1)*10}" rx="22" ry="6" fill="none" stroke="#8D9095" stroke-width="1"/>'


def house():
    return (f'<path d="M-46 -6 L0 -46 L46 -6 Z" fill="{RED}"/>'
            f'<rect x="-36" y="-8" width="72" height="56" rx="3" fill="{PAPER}"/>'
            f'<rect x="-10" y="18" width="20" height="30" rx="2" fill="{DARK2}"/>'
            f'<rect x="-28" y="4" width="14" height="14" rx="2" fill="{INK}"/><rect x="14" y="4" width="14" height="14" rx="2" fill="{INK}"/>')


def rings():
    return ('<circle cx="-12" cy="0" r="20" fill="none" stroke="url(#metal)" stroke-width="7"/>'
            '<circle cx="12" cy="0" r="20" fill="none" stroke="url(#metal)" stroke-width="7"/>')


def car():
    return (f'<path d="M-62 10 v-12 l14 -26 c4 -7 9 -10 18 -10 h52 c8 0 13 3 18 10 l16 22 l14 4 c6 2 8 6 8 12 v10 z" fill="{PAPER}"/>'
            f'<path d="M-40 -6 l9 -18 h24 v18z M2 -6 v-18 h20 l14 18z" fill="{DARK2}"/>'
            f'<circle cx="-34" cy="20" r="13" fill="#16181B"/><circle cx="-34" cy="20" r="5" fill="#9A9DA2"/>'
            f'<circle cx="44" cy="20" r="13" fill="#16181B"/><circle cx="44" cy="20" r="5" fill="#9A9DA2"/>')


def court():
    cols = ''.join(f'<rect x="{x}" y="-62" width="14" height="62" rx="2" fill="{PAPER}"/>' for x in (-66, -38, -10, 18, 46))
    return (f'<path d="M-84 -66 L0 -110 L84 -66 Z" fill="{PAPER}"/><circle cx="0" cy="-82" r="9" fill="{RED}"/>'
            f'<rect x="-86" y="-70" width="172" height="10" rx="2" fill="{PAPER_D}"/>{cols}'
            f'<rect x="-90" y="0" width="180" height="10" rx="2" fill="{PAPER_D}"/><rect x="-100" y="10" width="200" height="10" rx="2" fill="{PAPER}"/>')


def stethoscope():
    return (f'<path d="M-30 -60 C-30 -10 -10 10 10 10 C30 10 50 -10 50 -60" fill="none" stroke="#C9CBCF" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M10 10 C10 50 40 60 60 50" fill="none" stroke="#C9CBCF" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="72" cy="46" r="16" fill="url(#metal)"/><circle cx="72" cy="46" r="7" fill="#7E8186"/>'
            f'<circle cx="-30" cy="-62" r="5" fill="url(#metal)"/><circle cx="50" cy="-62" r="5" fill="url(#metal)"/>')


def calendar(day=30):
    cells = ''.join(f'<rect x="{12+c*16}" y="{40+r*14}" width="11" height="9" rx="2" fill="{RED if r*7+c+1==day else INK}"/>'
                    for r in range(5) for c in range(7) if r * 7 + c < 31)
    return (f'<rect width="132" height="118" rx="6" fill="{PAPER}"/><rect width="132" height="28" rx="6" fill="{RED}"/><rect y="20" width="132" height="8" fill="{RED}"/>'
            f'<circle cx="28" cy="2" r="5" fill="#16181B"/><circle cx="104" cy="2" r="5" fill="#16181B"/>{cells}')


def binder():
    return (f'<rect width="120" height="150" rx="6" fill="{RED_D}"/><rect x="10" width="110" height="150" rx="6" fill="{RED}"/>'
            f'<rect x="32" y="30" width="70" height="40" rx="4" fill="{PAPER}"/><rect x="42" y="42" width="50" height="4" rx="2" fill="{INK}"/><rect x="42" y="54" width="34" height="4" rx="2" fill="{INK}"/>'
            f'<rect x="-6" y="20" width="12" height="20" rx="3" fill="url(#metal)"/><rect x="-6" y="110" width="12" height="20" rx="3" fill="url(#metal)"/>')


def envelope(w=190, h=120):
    return (f'<rect width="{w}" height="{h}" rx="6" fill="{PAPER}"/>'
            f'<path d="M0 6 L{w/2} {h*.58} L{w} 6" fill="none" stroke="{PAPER_D}" stroke-width="3"/>'
            f'<path d="M0 {h} L{w*.42} {h*.5} M{w} {h} L{w*.58} {h*.5}" stroke="{PAPER_D}" stroke-width="2"/>')


def flag():
    return (f'<rect x="-3" y="-90" width="6" height="96" rx="3" fill="url(#metal)"/>'
            f'<path d="M3 -86 C25 -94 40 -78 64 -86 V-50 C40 -42 25 -58 3 -50 Z" fill="{RED}"/>')


def ribbon_docs():
    return (g(paper(140, 170, 9), 14, -10, 6, shadow=False) + g(paper(140, 170, 9), 0, 0, 0, shadow=False) +
            f'<rect x="-4" y="70" width="148" height="12" fill="{RED}"/><rect x="62" y="0" width="12" height="170" fill="{RED}"/>')


S = {}

S['criminal-litigation'] = ('Gavel striking its block in front of a closed case file',
    g(folder(190, 130), 40, 140, -6) +
    g(paper(150, 190, 10, sign=True), 230, 60, 7) +
    g(block(140), 330, 292) +
    g(gavel(-38), 300, 210))

S['labour-disputes'] = ('Scales weighing an employer briefcase against a worker, beside a 30 day calendar',
    g(paper(140, 180, 9, sign=True), 40, 50, -7) +
    g(scales(-8, 1.05), 230, 318) +
    g(f'<rect x="-28" y="-22" width="56" height="38" rx="6" fill="{RED_D}"/><rect x="-28" y="-6" width="56" height="4" fill="rgba(0,0,0,.25)"/><rect x="-11" y="-30" width="22" height="10" rx="3" fill="none" stroke="{RED_D}" stroke-width="4"/>', 169, 260) +
    g(f'<circle cx="0" cy="-28" r="12" fill="{PAPER}"/><path d="M-19 6 c2 -24 36 -24 38 0z" fill="{PAPER}"/>', 291, 246) +
    g(calendar(30), 322, 70, 6))

S['civil-litigation'] = ('Summons sealed in red wax on a stack of law books',
    g(books(4), 150, 312) +
    g(paper(170, 210, 11, sign=True), 230, 56, 5) +
    g(seal(34), 380, 236) +
    g(gavel(-60), 120, 190, 0, .55))

S['medical-negligence'] = ('Medical file with a red cross beside a stethoscope and the scales of justice',
    g(folder(200, 140, RED), 36, 150, -4) +
    g(f'<rect x="-14" y="-38" width="28" height="76" rx="4" fill="{RED}"/><rect x="-38" y="-14" width="76" height="28" rx="4" fill="{RED}"/>', 136, 100) +
    g(stethoscope(), 290, 160, 8, 1.1) +
    g(scales(4, .6), 400, 330))

S['personal-injury'] = ('Road accident claim form with a car and a warning triangle',
    g(paper(170, 220, 11, sign=True), 44, 52, -6) +
    f'<path d="M190 296 H460" stroke="rgba(255,255,255,.14)" stroke-width="30" stroke-linecap="round"/>' +
    ''.join(f'<rect x="{x}" y="294" width="22" height="4" rx="2" fill="rgba(255,255,255,.45)"/>' for x in (210, 260, 310, 360, 410)) +
    g(car(), 320, 252, 0, 1.25) +
    g(f'<path d="M0 -34 L32 22 L-32 22 Z" fill="{RED}"/><path d="M0 -14 L16 14 L-16 14 Z" fill="none" stroke="#fff" stroke-width="3"/>', 410, 110) +
    g(seal(26), 196, 252))

S['family-and-estates'] = ('Last will with a wax seal, wedding rings and a family home',
    g(paper(170, 220, 10, sign=True), 50, 60, -5) +
    g(seal(30), 190, 250) +
    g(house(), 340, 150, 0, 1.45) +
    g(rings(), 345, 285, -8, 1.5))

S['employment-law'] = ('Workplace policy binder, gavel and a signed disciplinary notice',
    g(binder(), 60, 80, -4) +
    g(paper(150, 190, 9, sign=True), 210, 70, 6) +
    g(block(120), 360, 300) +
    g(gavel(-30), 340, 230, 0, .8))

S['litigation'] = ('Court building with the scales of justice and bound court papers',
    g(court(), 170, 305, 0, 1.1) +
    g(ribbon_docs(), 330, 52, 8, .55) +
    g(scales(0, .82), 395, 318))

S['commercial-law'] = ('Signed contract with a fountain pen and a company seal',
    g(paper(200, 250, 13, sign=True), 60, 50, -4) +
    g(paper(150, 190, 9), 270, 90, 7) +
    g(pen(-50), 330, 200) +
    g(seal(34), 380, 290))

S['debt-recovery'] = ('Letter of demand sealed in red wax beside a stack of coins',
    g(paper(150, 190, 9), 70, 50, -8) +
    g(envelope(200, 126), 150, 160, 4) +
    g(seal(28), 252, 236) +
    g(coins(7), 390, 300))

S['public-sector'] = ('Government building with its flag and tender documents tied with red ribbon',
    g(court(), 160, 300, 0, .9) +
    g(flag(), 160, 196, 0, .8) +
    g(ribbon_docs(), 300, 110, 4))

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, (title, body) in S.items():
        (OUT / f'{slug}.svg').write_text(svg(title, body))
    print(f'wrote {len(S)} illustrations to {OUT}')
