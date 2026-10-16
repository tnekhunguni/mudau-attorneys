"""Generates the practice-area illustrations in public/illustrations/.

Style: layered interface-like panels on a dark card (like the SALOUI site),
in the firm's letterhead palette: near-black, translucent whites, one red accent.
Run:  python3 scripts/illustrations.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'public' / 'illustrations'
RED = '#EF363A'
W = lambda a: f'rgba(255,255,255,{a})'

DEFS = f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1B1E23"/><stop offset="1" stop-color="#0B0C0E"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{RED}" stop-opacity=".35"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></linearGradient>
<radialGradient id="glow" cx=".85" cy=".1" r=".7"><stop offset="0" stop-color="{RED}" stop-opacity=".22"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></radialGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".45"/></filter>
</defs>'''


def card(x, y, w, h, fill='#1F2328', r=12, shadow=False, stroke=W(.12)):
    f = ' filter="url(#sh)"' if shadow else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"{f}/>'


def pill(x, y, w, h=7, fill=W(.22)):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}"/>'


def window(x, y, w, h, shadow=False):
    """Panel with a title bar and three dots, like an app window."""
    return (card(x, y, w, h, shadow=shadow) +
            f'<path d="M{x} {y+30}h{w}" stroke="{W(.1)}"/>' +
            ''.join(f'<circle cx="{x+18+i*14}" cy="{y+15}" r="4" fill="{RED if i == 2 else W(.22)}"/>' for i in range(3)) +
            pill(x + 70, y + 11, min(120, w - 90), 8, W(.08)))


def lines(x, y, widths, gap=16, fill=W(.2)):
    return ''.join(pill(x, y + i * gap, w, 7, fill) for i, w in enumerate(widths))


def badge(cx, cy, r, icon, fill=RED):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" filter="url(#sh)"/>' +
            f'<g transform="translate({cx} {cy})" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">{icon}</g>')


def check(x, y, s=1, color=RED):
    return f'<path d="M{x} {y} l{6*s} {6*s} l{11*s} -{12*s}" fill="none" stroke="{color}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'


# Line icons centred on 0,0, roughly 36px across
ICON = {
    'gavel': '<g transform="rotate(-40)"><rect x="-15" y="-16" width="30" height="13" rx="3"/><path d="M0 -3v22"/></g><path d="M-16 17h18"/>',
    'scales': '<path d="M0 -16v32M-10 16h20M-15 -10h30M-15 -10l-6 13h12zM15 -10l-6 13h12z"/>',
    'calendar': '<rect x="-15" y="-12" width="30" height="28" rx="4"/><path d="M-15 -3h30M-8 -17v8M8 -17v8"/>',
    'pulse': '<path d="M-17 0h8l4 -10l7 20l4 -10h11"/>',
    'car': '<path d="M-16 6v-6l5 -9h22l5 9v6zM-12 0h24"/><circle cx="-9" cy="9" r="3"/><circle cx="9" cy="9" r="3"/>',
    'house': '<path d="M-16 -1l16 -14l16 14M-11 -5v19h22v-19"/><path d="M0 9c-5 -4 -6 -7 -4 -9c2 -1 3 0 4 1c1 -1 2 -2 4 -1c2 2 1 5 -4 9z" fill="#fff" stroke="none"/>',
    'people': '<circle cx="-7" cy="-6" r="6"/><circle cx="9" cy="-4" r="5"/><path d="M-18 15c1 -9 21 -9 22 0M3 14c1 -7 14 -7 15 0"/>',
    'court': '<path d="M-17 -7l17 -10l17 10zM-17 15h34M-13 -3v14M-4 -3v14M5 -3v14M13 -3v14"/>',
    'pen': '<path d="M-12 14l4 -12l16 -16l8 8l-16 16z M-8 2l8 8"/>',
    'coins': '<ellipse cx="0" cy="-9" rx="13" ry="5"/><path d="M-13 -9v18c0 3 6 5 13 5s13 -2 13 -5v-18M-13 0c0 3 6 5 13 5s13 -2 13 -5"/>',
    'flag': '<path d="M-10 17v-34M-10 -15h22l-5 7l5 7h-22"/>',
    'pin': '<path d="M0 17s-12 -11 -12 -20a12 12 0 0 1 24 0c0 9 -12 20 -12 20z"/><circle cx="0" cy="-3" r="4"/>',
    'clipboard': '<rect x="-13" y="-13" width="26" height="30" rx="3"/><path d="M-6 -16h12v6h-6z M-6 0h12M-6 8h8"/>',
    'box': '<path d="M-16 -6l16 -9l16 9v16l-16 9l-16 -9zM-16 -6l16 9l16 -9M0 3v16"/>',
}


def svg(title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{DEFS}'
            f'<rect width="480" height="360" rx="22" fill="url(#bg)"/><rect width="480" height="360" rx="22" fill="url(#glow)"/>'
            f'<g stroke-width="1.2">{body}</g></svg>')


def timeline(x, y, steps, active, gap=46):
    out = f'<path d="M{x} {y}v{gap*(steps-1)}" stroke="{W(.15)}" stroke-width="2"/>'
    out += f'<path d="M{x} {y}v{gap*active}" stroke="{RED}" stroke-width="2.5"/>'
    for i in range(steps):
        cy = y + i * gap
        if i < active:
            out += f'<circle cx="{x}" cy="{cy}" r="9" fill="{RED}"/>' + check(x - 5, cy, .55, '#fff')
        elif i == active:
            out += f'<circle cx="{x}" cy="{cy}" r="9" fill="#1F2328" stroke="{RED}" stroke-width="2.5"/><circle cx="{x}" cy="{cy}" r="3.5" fill="{RED}"/>'
        else:
            out += f'<circle cx="{x}" cy="{cy}" r="8" fill="#1F2328" stroke="{W(.25)}" stroke-width="2"/>'
        out += pill(x + 22, cy - 9, [90, 70, 100, 80, 90][i % 5], 7, W(.85) if i == active else W(.25))
        out += pill(x + 22, cy + 3, [60, 80, 50, 70, 60][i % 5], 6, W(.12))
    return out


S = {}

S['criminal-litigation'] = ('Case timeline from arrest to appeal with a gavel badge',
    window(40, 34, 270, 292) + timeline(72, 100, 5, 2) +
    card(270, 70, 170, 96, shadow=True) + pill(290, 92, 70, 7, W(.3)) + pill(290, 110, 110, 12, W(.9)) + pill(290, 134, 80, 7, f'{RED}') +
    card(300, 196, 150, 110, shadow=True) + lines(318, 220, [80, 110, 60]) + check(320, 282, 1) + pill(346, 276, 70, 9, W(.6)) +
    badge(420, 60, 30, ICON['gavel']))

S['labour-disputes'] = ('Referral form with a 30 day calendar countdown',
    window(40, 40, 250, 280) + lines(64, 92, [120, 170, 140]) +
    card(64, 150, 202, 34, '#181B1F', 8) + pill(76, 164, 90, 7, W(.3)) +
    card(64, 194, 202, 34, '#181B1F', 8) + pill(76, 208, 130, 7, W(.3)) +
    card(64, 250, 110, 40, RED, 8, stroke='none') + pill(82, 266, 74, 8, '#fff') +
    card(250, 90, 190, 200, shadow=True) + pill(270, 110, 80, 8, W(.3)) +
    ''.join(f'<rect x="{270+c*24}" y="{136+r*24}" width="18" height="18" rx="4" fill="{RED if (r,c)==(4,1) else W(.14) if r*6+c<25 else W(.05)}"/>' for r in range(5) for c in range(6)) +
    f'<circle cx="303" cy="241" r="15" fill="none" stroke="{RED}" stroke-width="2"/>' +
    badge(420, 70, 28, ICON['calendar']))

S['civil-litigation'] = ('Summons with a court seal and a ten day countdown ring',
    card(70, 46, 210, 270, '#23272D', 10, shadow=True) +
    card(52, 30, 210, 270, shadow=True) + pill(76, 56, 110, 10, W(.85)) + lines(76, 84, [160, 140, 160, 120, 150, 100], 18) +
    pill(76, 210, 70, 7, W(.3)) + f'<path d="M78 254c10 -14 18 6 28 -8c8 -10 14 4 26 -4" fill="none" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>' +
    card(290, 110, 150, 150, shadow=True) +
    f'<circle cx="365" cy="185" r="44" fill="none" stroke="{W(.12)}" stroke-width="10"/>' +
    f'<circle cx="365" cy="185" r="44" fill="none" stroke="{RED}" stroke-width="10" stroke-linecap="round" stroke-dasharray="190 400" transform="rotate(-90 365 185)"/>' +
    pill(343, 175, 44, 12, W(.9)) + pill(350, 195, 30, 6, W(.3)) +
    badge(250, 268, 30, ICON['scales']))

S['medical-negligence'] = ('Medical record with a heartbeat line and a clinic file list',
    window(40, 40, 300, 200) +
    f'<path d="M56 190 L100 190 L116 150 L138 222 L156 170 L176 190 L230 190 L246 130 L262 205 L280 190 L324 190 L324 228 L56 228 Z" fill="url(#area)"/>' +
    f'<path d="M56 190 L100 190 L116 150 L138 222 L156 170 L176 190 L230 190 L246 130 L262 205 L280 190 L324 190" fill="none" stroke="{RED}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>' +
    lines(60, 92, [110, 160]) +
    card(250, 190, 190, 130, shadow=True) +
    ''.join(card(266, 208 + i * 34, 158, 26, '#181B1F', 6) + pill(280, 218 + i * 34, [90, 70, 100][i], 6, W(.3)) +
            f'<circle cx="408" cy="{221 + i*34}" r="4" fill="{RED if i == 0 else W(.3)}"/>' for i in range(3)) +
    badge(400, 70, 30, ICON['pulse']))

S['personal-injury'] = ('Road map with a location pin and a claim progress card',
    window(40, 40, 280, 280) +
    f'<path d="M60 300 C 120 250, 110 170, 190 150 S 290 110, 300 70" fill="none" stroke="{W(.14)}" stroke-width="26" stroke-linecap="round"/>' +
    f'<path d="M60 300 C 120 250, 110 170, 190 150 S 290 110, 300 70" fill="none" stroke="{W(.4)}" stroke-width="2" stroke-dasharray="10 10"/>' +
    badge(190, 150, 24, ICON['pin']) +
    card(250, 196, 190, 120, shadow=True) + pill(270, 216, 90, 8, W(.3)) + pill(270, 234, 130, 12, W(.9)) +
    f'<rect x="270" y="268" width="150" height="10" rx="5" fill="{W(.12)}"/><rect x="270" y="268" width="96" height="10" rx="5" fill="{RED}"/>' +
    pill(270, 290, 60, 6, W(.25)) +
    badge(410, 80, 30, ICON['car']))

S['family-and-estates'] = ('Family members linked to a home and a signed will',
    window(40, 40, 260, 200) +
    ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{W(.14)}" stroke="{W(.25)}"/>' for cx, cy, r in ((110, 120, 26), (190, 120, 26), (150, 196, 20))) +
    f'<path d="M136 120h28M122 142l18 34M178 142l-18 34" stroke="{W(.25)}" stroke-width="2"/>' +
    f'<circle cx="150" cy="196" r="20" fill="{RED}" opacity=".85"/>' +
    card(250, 130, 190, 190, shadow=True) + pill(272, 152, 100, 10, W(.85)) + lines(272, 180, [140, 120, 146, 100], 18) +
    f'<path d="M274 290c10 -14 18 6 28 -8c8 -10 14 4 26 -4" fill="none" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>' + pill(272, 300, 80, 4, W(.3)) +
    badge(410, 80, 30, ICON['house']))

S['employment-law'] = ('Organisation chart beside a disciplinary hearing checklist',
    window(40, 40, 270, 230) +
    card(140, 86, 70, 34, RED, 8, stroke='none') + pill(152, 99, 46, 7, '#fff') +
    f'<path d="M175 120v20M90 140h170M90 140v16M175 140v16M260 140v16" stroke="{W(.3)}" stroke-width="2" fill="none"/>' +
    ''.join(card(x, 156, 64, 30, '#2A2F35', 7) + pill(x + 12, 167, 40, 6, W(.35)) for x in (58, 143, 228)) +
    ''.join(card(x, 206, 52, 26, '#181B1F', 6) for x in (64, 120, 176, 232)) +
    card(260, 170, 180, 150, shadow=True) +
    ''.join(f'<rect x="278" y="{192+i*30}" width="16" height="16" rx="4" fill="{RED if i < 3 else "none"}" stroke="{RED if i < 3 else W(.3)}" stroke-width="1.5"/>' +
            (check(281, 200 + i * 30, .5, '#fff') if i < 3 else '') + pill(304, 196 + i * 30, [100, 80, 110, 70][i], 7, W(.3)) for i in range(4)) +
    badge(410, 80, 30, ICON['clipboard']))

S['litigation'] = ('Court building with a list of matters and their status',
    window(40, 40, 400, 280) +
    f'<g fill="none" stroke="{W(.5)}" stroke-width="2.5" stroke-linejoin="round"><path d="M70 130l60 -36l60 36z"/><path d="M70 214h120M80 136v70M102 136v70M124 136v70M146 136v70M168 136v70"/></g>' +
    f'<circle cx="130" cy="118" r="6" fill="{RED}"/>' +
    ''.join(card(222, 76 + i * 56, 196, 44, '#181B1F', 8) + pill(236, 88 + i * 56, [110, 90, 120, 80][i], 7, W(.35)) + pill(236, 102 + i * 56, 60, 6, W(.15)) +
            pill(360, 92 + i * 56, 44, 12, RED if i == 0 else W(.12)) for i in range(4)) +
    card(64, 236, 140, 64, shadow=True) + pill(80, 252, 60, 7, W(.3)) + pill(80, 268, 100, 12, W(.9)) +
    badge(420, 60, 28, ICON['scales']))

S['commercial-law'] = ('Contract with clauses, two signatories and a red stamp',
    card(40, 34, 240, 292, shadow=True) + pill(64, 58, 120, 10, W(.85)) +
    ''.join(f'<circle cx="70" cy="{98+i*34}" r="5" fill="{RED if i == 0 else W(.3)}"/>' + lines(84, 92 + i * 34, [150, 110], 12) for i in range(5)) +
    f'<path d="M66 290c10 -14 18 6 28 -8c8 -10 14 4 26 -4" fill="none" stroke="{W(.6)}" stroke-width="2.5" stroke-linecap="round"/>' +
    f'<path d="M166 290c10 -14 18 6 28 -8c8 -10 14 4 26 -4" fill="none" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>' +
    card(300, 100, 140, 120, shadow=True) +
    f'<circle cx="345" cy="150" r="20" fill="{W(.18)}"/><circle cx="395" cy="150" r="20" fill="{RED}" opacity=".9"/>' +
    f'<path d="M345 150h50" stroke="#fff" stroke-width="2" stroke-dasharray="4 4"/>' + pill(330, 188, 80, 7, W(.3)) +
    card(310, 240, 120, 70, RED, 10, stroke='none', shadow=True) + pill(330, 262, 80, 8, '#fff') + pill(330, 280, 50, 6, W(.6)) +
    badge(420, 60, 28, ICON['pen']))

S['debt-recovery'] = ('Recovery chart rising as an overdue balance is paid',
    window(40, 40, 300, 220) +
    ''.join(f'<rect x="{70+i*44}" y="{230-h}" width="26" height="{h}" rx="5" fill="{RED if i == 5 else W(.16)}"/>' for i, h in enumerate((40, 62, 80, 104, 124, 150))) +
    f'<path d="M83 186 L127 166 L171 150 L215 126 L259 106 L303 80" fill="none" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>' +
    card(250, 196, 190, 124, shadow=True) + pill(270, 216, 70, 7, W(.3)) + pill(270, 234, 120, 12, W(.9)) +
    pill(270, 262, 70, 18, RED) + pill(280, 268, 50, 6, '#fff') + lines(270, 294, [140], 0) +
    badge(410, 80, 30, ICON['coins']))

S['public-sector'] = ('Government building with tender documents and a compliance checklist',
    window(40, 40, 250, 260) +
    f'<g fill="none" stroke="{W(.5)}" stroke-width="2.5" stroke-linejoin="round"><rect x="80" y="130" width="130" height="120" rx="4"/><path d="M70 130h150M145 130v-56"/></g>' +
    f'<path d="M145 76l36 10l-36 12z" fill="{RED}"/>' +
    ''.join(f'<rect x="{96+c*36}" y="{148+r*34}" width="22" height="20" rx="3" fill="{W(.14)}"/>' for c in range(3) for r in range(2)) +
    f'<rect x="133" y="216" width="24" height="34" rx="3" fill="{W(.3)}"/>' +
    card(286, 150, 150, 160, '#23272D', 10, shadow=True) +
    card(270, 136, 150, 160, shadow=True) +
    ''.join(check(288, 170 + i * 30, .8) + pill(312, 164 + i * 30, [80, 90, 70, 86][i], 7, W(.3)) for i in range(4)) +
    badge(410, 80, 30, ICON['flag']))

S['labour-disputes'] = S['labour-disputes']

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, (title, body) in S.items():
        (OUT / f'{slug}.svg').write_text(svg(title, body))
    print(f'wrote {len(S)} illustrations to {OUT}')
