"""Gera 8 artes (1080x1350) da Verbena, uma floricultura de bairro fictícia, para o giro 3D da página inicial.
A Verbena tem identidade própria, independente da selfmade.: colagem de papel recortado, serifa itálica macia
(Fraunces), paleta em verdes e creme, a mesma família do site (tinta, verde floresta, lima, menta, sálvia) e sombras de recorte. Cada arte usa um modelo
diferente de apresentar a ideia. Uso: python gerar_verbena.py
A empresa, os preços, horários e textos são fictícios e servem só como exemplo de design."""
import os, math, random, subprocess, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

PAPEL, PLUM, CORAL, SOL, ROSA, LILAS, FOLHA, AGUA, CARTAO = "#F3EFE6", "#13241C", "#1E6B47", "#D2E86C", "#C4EFD2", "#9CD3B0", "#2E8B57", "#0E7C86", "#FAF7EF"

FONTS = "@import url('fonts/fontes.css');"  # Fraunces e DM Sans (OFL), baixadas para fonts/ para o render ser determinístico
BASE = FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#fff}
svg{display:block}
"""
DEFS = ("<defs><filter id='sh' x='-5%' y='-5%' width='115%' height='115%'><feDropShadow dx='6' dy='8' stdDeviation='0' flood-color='#13241C' flood-opacity='.22'/></filter>"
        "<filter id='gr' x='0' y='0' width='100%' height='100%'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' seed='4'/>"
        "<feColorMatrix values='0 0 0 0 .07  0 0 0 0 .14  0 0 0 0 .11  1.3 0 0 0 -.5'/></filter></defs>")


def T(x, y, s, size, fill, fam="f", w=800, anchor="start", ls=-.02):
    est = ("font-family:Fraunces,serif;font-style:italic;font-variation-settings:&quot;SOFT&quot; 100,&quot;opsz&quot; 144" if fam == "f"
           else "font-family:DM Sans,sans-serif")
    return f"<text x='{x}' y='{y}' font-size='{size}' fill='{fill}' font-weight='{w}' text-anchor='{anchor}' style='letter-spacing:{ls}em;{est}'>{s}</text>"


def sh(c):
    return f"<g filter='url(#sh)'>{c}</g>"


def pagina(fundo, corpo):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1350' viewBox='0 0 1080 1350'>{DEFS}"
            f"<rect width='1080' height='1350' fill='{fundo}'/>{corpo}<rect width='1080' height='1350' filter='url(#gr)' opacity='.35'/></svg>")


def selo(fundo=PLUM, texto=PAPEL):
    return f"<rect x='60' y='1244' width='350' height='62' rx='31' fill='{fundo}'/>" + T(235, 1285, "@verbena.flores", 30, texto, "d", 700, "middle", 0)


def blob(cx, cy, r, seed, cor, n=9, var=.24):
    rnd = random.Random(seed)
    pts = [(cx + r * (1 - var / 2 + var * rnd.random()) * math.cos(2 * math.pi * i / n), cy + r * (1 - var / 2 + var * rnd.random()) * math.sin(2 * math.pi * i / n)) for i in range(n)]
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    m0 = mid(pts[-1], pts[0])
    d = f"M{m0[0]:.1f},{m0[1]:.1f}"
    for i in range(n):
        m = mid(pts[i], pts[(i + 1) % n])
        d += f" Q{pts[i][0]:.1f},{pts[i][1]:.1f} {m[0]:.1f},{m[1]:.1f}"
    return f"<path d='{d}Z' fill='{cor}'/>"


def flor(x, y, r, n, c1, c2, rot=0, w=.6, cen=.24):
    W = r * w
    pet = f"<path d='M0,0 C{W:.1f},{-r * .15:.1f} {W:.1f},{-r * .85:.1f} 0,{-r:.1f} C{-W:.1f},{-r * .85:.1f} {-W:.1f},{-r * .15:.1f} 0,0Z' fill='{c1}'/>"
    p = "".join(f"<g transform='rotate({i * 360 / n:.1f})'>{pet}</g>" for i in range(n))
    return f"<g transform='translate({x} {y}) rotate({rot})'>{p}<circle r='{r * cen:.1f}' fill='{c2}'/></g>"


def folha(x, y, L, ang, cor):
    return (f"<g transform='translate({x} {y}) rotate({ang})'><path d='M0,0 C{L * .5:.1f},{-L * .3:.1f} {L * .5:.1f},{-L * .7:.1f} 0,{-L} "
            f"C{-L * .5:.1f},{-L * .7:.1f} {-L * .5:.1f},{-L * .3:.1f} 0,0Z' fill='{cor}'/></g>")


def haste(x1, y1, x2, y2, cor, w=8):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{cor}' stroke-width='{w}' stroke-linecap='round'/>"


def tulipa(x, y, s, cor):
    return (f"<g transform='translate({x} {y}) scale({s})'><path d='M-40,0 C-52,-60 -46,-100 -36,-132 L-12,-96 L0,-138 L12,-96 L36,-132 C46,-100 52,-60 40,0 Z' fill='{cor}'/></g>")


def bez(p, u):
    a, b, c, d = p
    k = lambda i: (1 - u) ** 3 * a[i] + 3 * (1 - u) ** 2 * u * b[i] + 3 * (1 - u) * u * u * c[i] + u ** 3 * d[i]
    dk = lambda i: 3 * (1 - u) ** 2 * (b[i] - a[i]) + 6 * (1 - u) * u * (c[i] - b[i]) + 3 * u * u * (d[i] - c[i])
    return (k(0), k(1)), math.atan2(dk(1), dk(0))


def ramo(p, cor):
    d = f"M{p[0][0]},{p[0][1]} C{p[1][0]},{p[1][1]} {p[2][0]},{p[2][1]} {p[3][0]},{p[3][1]}"
    s = f"<path d='{d}' fill='none' stroke='{cor}' stroke-width='7' stroke-linecap='round'/>"
    for i in range(9):
        (x, y), ang = bez(p, .22 + i * .09)
        for lado in (-1, 1):
            dr = ang + lado * math.radians(62)
            s += f"<ellipse rx='25' ry='12' fill='{cor}' transform='translate({x + 25 * math.cos(dr):.1f} {y + 25 * math.sin(dr):.1f}) rotate({math.degrees(dr):.1f})'/>"
    return s


A = {}

# 1 — apresentação: marca em letras de papel e colagem de flores
def a01():
    s = sh(blob(730, 470, 330, 3, SOL))
    s += f"<g filter='url(#sh)'><rect x='60' y='80' width='500' height='70' rx='35' fill='{PAPEL}'/></g>" + T(310, 128, "floricultura de bairro", 36, PLUM, "d", 700, "middle", 0)
    s += sh(T(50, 585, "verbena", 275, PAPEL, ls=-.045))
    s += T(66, 680, "buquês, plantas e arranjos", 50, PLUM, "d", 700, "start", -.02) + T(66, 742, "feitos à mão.", 50, PLUM, "d", 700, "start", -.02)
    s += "".join(haste(x, 1350, x2, y2, FOLHA, 14) for x, x2, y2 in ((250, 250, 1010), (620, 620, 930), (880, 880, 1060)))
    s += "".join(folha(x, 1350, L, a, FOLHA) for x, L, a in ((400, 300, -22), (520, 240, 24), (760, 300, 16), (130, 230, 32), (980, 250, -26)))
    s += sh(flor(250, 980, 165, 8, ROSA, PLUM, 8) + flor(620, 905, 135, 7, PLUM, SOL, 0) + flor(880, 1040, 150, 9, PAPEL, SOL, 14))
    s += selo()
    return pagina(CORAL, s)


A["01-apresentacao"] = ("Apresentação da Verbena", a01)


# 2 — buquê: esquema anotado com legendas e etiqueta de preço
def girassol(x, y):
    return flor(x, y, 102, 14, SOL, SOL, 0, .3, .01) + flor(x, y, 66, 12, CORAL, PLUM, 12, .36, .5)


def lisianto(x, y):
    return flor(x, y, 40, 5, CORAL, SOL, 0, .7, .26)


def a02():
    s = ramo(((480, 890), (400, 700), (200, 600), (150, 500)), FOLHA) + ramo(((600, 890), (700, 700), (880, 600), (940, 500)), FOLHA)
    flores = [(girassol, 330, 720, 500), (girassol, 540, 640, 540), (girassol, 760, 720, 600),
              (lisianto, 445, 805, 520), (lisianto, 645, 795, 560), (lisianto, 865, 835, 620), (lisianto, 225, 840, 460), (lisianto, 540, 775, 540)]
    s += "".join(haste(ox, 890, x, y, FOLHA, 7) for _, x, y, ox in flores) + "".join(f(x, y) for f, x, y, _ in flores)
    s += f"<polygon points='540,1190 330,880 750,880' fill='{PAPEL}'/><polygon points='540,1190 750,880 640,880' fill='{LILAS}'/>"
    s += f"<polygon points='388,952 692,952 678,990 402,990' fill='{PLUM}'/><polygon points='540,971 500,945 500,997' fill='{PLUM}'/><polygon points='540,971 580,945 580,997' fill='{PLUM}'/>"
    g = sh(f"<g transform='translate(540 1190) scale(.9) translate(-540 -1190)'>{s}</g>")
    ld = lambda x1, y1, x2, y2: f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{PLUM}' stroke-width='3'/><circle cx='{x2}' cy='{y2}' r='7' fill='{PLUM}'/>"
    g += ld(140, 552, 189, 569) + T(72, 505, "eucalipto", 40, PLUM, "f", 800, "start", 0) + T(72, 543, "2 ramos", 30, PLUM, "d", 500, "start", 0)
    g += ld(540, 560, 540, 607) + T(540, 505, "girassol", 40, PLUM, "f", 800, "middle", 0) + T(540, 543, "3 hastes", 30, PLUM, "d", 500, "middle", 0)
    g += ld(832, 870, 930, 1030) + T(1008, 1085, "lisianthus", 40, PLUM, "f", 800, "end", 0) + T(1008, 1123, "5 hastes", 30, PLUM, "d", 500, "end", 0)
    g += T(60, 215, "buquê", 150, PLUM, ls=-.045) + T(60, 355, "da semana", 150, PLUM, ls=-.045)
    tag = (f"<g transform='translate(860 110) rotate(7)'><line x1='0' y1='36' x2='-28' y2='-120' stroke='{PLUM}' stroke-width='4'/>"
           f"<rect x='-130' y='0' width='260' height='220' rx='36' fill='{SOL}'/><circle cx='0' cy='38' r='13' fill='{ROSA}'/>"
           + T(0, 160, "R$ 89", 92, PLUM, ls=-.04, anchor="middle") + "</g>")
    return pagina(ROSA, g + sh(tag) + selo())


A["02-buque"] = ("Buquê da semana", a02)


# 3 — rega: três quadros recortados
def vaso(cx, topo, larg, folhas, corpo):
    r = larg
    s = f"<rect x='{cx - r / 2}' y='{topo}' width='{r}' height='26' rx='5' fill='{corpo}'/>"
    s += f"<polygon points='{cx - r / 2 + 9},{topo + 26} {cx + r / 2 - 9},{topo + 26} {cx + r / 2 - 28},{topo + 26 + r * .62} {cx - r / 2 + 28},{topo + 26 + r * .62}' fill='{corpo}'/>"
    s += f"<rect x='{cx - r / 2 + 12}' y='{topo}' width='{r - 24}' height='12' fill='{PLUM}'/>" + haste(cx, topo, cx, topo - 90, folhas, 7)
    s += folha(cx, topo - 40, 74, -52, folhas) + folha(cx, topo - 40, 74, 52, folhas) + folha(cx, topo - 82, 84, -12, folhas) + folha(cx, topo - 82, 70, 20, folhas)
    return s


def gota(x, y, cor=AGUA, e=1):
    return f"<g transform='translate({x} {y}) scale({e})'><polygon points='0,-15 9,0 -9,0' fill='{cor}'/><circle cy='4' r='9' fill='{cor}'/></g>"


def quadro(i, fundo, rot, ilu, l1, l2, s1, s2):
    x = 72 + i * 320
    g = f"<rect width='296' height='590' rx='26' fill='{fundo}'/><circle cx='52' cy='52' r='32' fill='{CORAL}'/>" + T(52, 66, str(i + 1), 40, PAPEL, anchor="middle")
    g += f"<g transform='translate(4 80)'>{ilu}</g>" + T(22, 448, l1, 46, PLUM, "f", 800, "start", -.01) + T(22, 494, l2, 46, PLUM, "f", 800, "start", -.01)
    g += T(22, 540, s1, 25, PLUM, "d", 500, "start", 0) + T(22, 569, s2, 25, PLUM, "d", 500, "start", 0)
    return sh(f"<g transform='translate({x} 500) rotate({rot} 148 295)'>{g}</g>")


def a03():
    ilu1 = vaso(148, 190, 150, FOLHA, CORAL)
    ilu1 += f"<g transform='translate(198 193) rotate(-8)'><rect x='-15' y='-130' width='30' height='124' rx='15' fill='{ROSA}'/><rect x='-52' y='-190' width='88' height='70' rx='22' fill='{ROSA}'/><rect x='-46' y='-236' width='76' height='64' rx='10' fill='{PLUM}'/></g>"
    ilu1 += f"<path d='M160,204 q-9,10 0,20 M232,204 q9,10 0,20' fill='none' stroke='{PLUM}' stroke-width='4' stroke-linecap='round'/>"
    ilu2 = vaso(190, 190, 150, FOLHA, CORAL)
    ilu2 += (f"<g transform='translate(60 52) rotate(25) scale(.8)'><rect width='96' height='76' rx='10' fill='{PLUM}'/><path d='M0,16 C-44,16 -44,62 0,62' fill='none' stroke='{PLUM}' stroke-width='11'/>"
             f"<polygon points='96,28 156,60 156,74 96,54' fill='{PLUM}'/></g>")
    ilu2 += gota(154, 168) + gota(149, 186, AGUA, .8) + gota(166, 182, AGUA, .7)
    ilu3 = vaso(148, 100, 150, FOLHA, CORAL)
    ilu3 += f"<ellipse cx='148' cy='212' rx='16' ry='5' fill='{PLUM}'/>" + gota(148, 236) + gota(130, 250, AGUA, .75)
    ilu3 += f"<rect x='74' y='268' width='148' height='22' rx='6' fill='{PLUM}'/><rect x='84' y='268' width='128' height='9' fill='{AGUA}'/>"
    g = T(60, 255, "como regar", 175, PLUM, ls=-.045) + T(64, 360, "três gestos para a planta durar.", 46, PLUM, "d", 700, "start", -.02)
    g += quadro(0, PAPEL, -2, ilu1, "toque", "a terra", "só regue se", "ela estiver seca.")
    g += quadro(1, ROSA, 1.5, ilu2, "regue", "na base", "longe das folhas,", "perto da raiz.")
    g += quadro(2, LILAS, -1, ilu3, "escoe", "o excesso", "raiz encharcada", "apodrece.")
    return pagina(SOL, g + selo())


A["03-rega"] = ("Dica de rega", a03)


# 4 — horário: placa na porta e gráfico de horas abertas
def a04():
    x0, ppx = 330, 67.8
    s = T(60, 280, "horário", 175, PAPEL, ls=-.045)
    s += T(64, 430, "passe por aqui.", 54, PAPEL, "d", 700, "start", -.03) + T(64, 495, "a porta está aberta.", 54, PAPEL, "d", 700, "start", -.03)
    placa = (f"<g transform='rotate(7 850 60)'><line x1='850' y1='60' x2='850' y2='214' stroke='{PAPEL}' stroke-width='4'/><rect x='710' y='196' width='280' height='200' rx='28' fill='{SOL}'/>"
             f"<circle cx='850' cy='226' r='12' fill='{PLUM}'/>" + T(850, 322, "aberto", 78, PLUM, "f", 800, "middle", -.04) + T(850, 366, "até 18h", 32, PLUM, "d", 700, "middle", 0) + "</g>")
    s += placa
    for h in range(8, 19, 2):
        x = x0 + (h - 8) * ppx
        s += f"<line x1='{x:.1f}' y1='690' x2='{x:.1f}' y2='1050' stroke='{PAPEL}' stroke-opacity='.25' stroke-width='2'/>" + T(f"{x:.1f}", 668, f"{h}h", 28, ROSA, "d", 700, "middle", 0)
    s += f"<line x1='{x0}' y1='690' x2='1008' y2='690' stroke='{PAPEL}' stroke-width='4'/>"
    for i, (nome, a, b, rot, cor) in enumerate([("seg a sex", 8, 18, "8h – 18h", ROSA), ("sábado", 8, 14, "8h – 14h", SOL), ("domingo", None, None, "fechado", ROSA)]):
        y = 730 + i * 110
        s += T(72, y + 50, nome, 46, PAPEL, "f", 800, "start", 0)
        if a:
            s += f"<rect x='{x0}' y='{y}' width='{(b - a) * ppx:.1f}' height='72' rx='36' fill='{cor}'/>" + T(x0 + 34, y + 48, rot, 34, PLUM, "d", 700, "start", 0)
        else:
            s += f"<rect x='{x0 + 2}' y='{y + 2}' width='{10 * ppx - 4:.1f}' height='68' rx='34' fill='none' stroke='{ROSA}' stroke-width='4' stroke-dasharray='12 10'/>" + T(x0 + 34, y + 48, rot, 34, ROSA, "d", 700, "start", 0)
    s += T(72, 1150, "rua das acácias, 120 · centro", 38, ROSA, "d", 700, "start", 0)
    return pagina(PLUM, s + selo(PAPEL, PLUM))


A["04-horario"] = ("Horário de funcionamento", a04)


# 5 — assinatura: um vaso para cada semana, cada um com sua flor
def girassol_pequeno(x, y):
    return flor(x, y, 52, 12, SOL, SOL, 0, .3, .01) + flor(x, y, 32, 10, CORAL, PLUM, 12, .36, .5)


def a05():
    s = T(60, 235, "flores", 175, PLUM, ls=-.03) + T(60, 395, "toda semana.", 175, PLUM, ls=-.03)
    vasos = [
        # semana 1: tulipa num pote reto
        haste(0, -120, 0, -190, FOLHA, 7) + tulipa(0, -180, .55, CORAL) + f"<rect x='-36' y='-120' width='72' height='120' rx='12' fill='{PLUM}'/>",
        # semana 2: margarida num vaso redondo
        haste(0, -110, 0, -230, FOLHA, 7) + flor(0, -240, 52, 14, PAPEL, SOL, 0, .26, .4) + f"<circle cy='-52' r='58' fill='{SOL}'/><rect x='-18' y='-118' width='36' height='30' fill='{SOL}'/>",
        # semana 3: hortênsia num vaso alto
        haste(0, -150, 0, -215, FOLHA, 7) + "".join(f"<circle cx='{dx}' cy='{-240 + dy}' r='{r}' fill='{c}'/>" for dx, dy, r, c in ((-22, 6, 26, ROSA), (22, 6, 26, ROSA), (0, -22, 28, CORAL), (0, 24, 26, CORAL)))
        + f"<polygon points='-30,-150 30,-150 20,0 -20,0' fill='{CORAL}'/>",
        # semana 4: girassol numa jarra
        haste(0, -130, 0, -200, FOLHA, 7) + girassol_pequeno(0, -235) + f"<path d='M-32,-130 h64 l12,130 h-88 z' fill='{PAPEL}'/>"]
    v = "".join(f"<g transform='translate({189 + i * 234} 880) scale(1.25)'>{c}</g>" for i, c in enumerate(vasos))
    v += f"<rect x='72' y='880' width='936' height='18' rx='9' fill='{PLUM}'/>"
    s += sh(v) + "".join(T(189 + i * 234, 948, f"semana {i + 1}", 30, PLUM, "d", 700, "middle", 0) for i in range(4))
    s += T(66, 1052, "a partir de", 40, PLUM, "d", 700, "start", -.02) + T(60, 1180, "R$ 59", 140, PLUM, ls=-.045) + T(470, 1180, "/mês", 56, PLUM, "d", 700, "start", -.02)
    return pagina(LILAS, s + selo())


A["05-assinatura"] = ("Assinatura mensal", a05)


# 6 — oficina: folha de calendário, tesoura e retalhos
def tesoura(cx, cy, giro, c1, c2, fundo, e=1):
    return (f"<g transform='translate({cx} {cy}) rotate({giro}) scale({e})'>"
            f"<line x1='-70' y1='28' x2='150' y2='-14' stroke='{c1}' stroke-width='13' stroke-linecap='round'/><line x1='-70' y1='-28' x2='150' y2='14' stroke='{c2}' stroke-width='13' stroke-linecap='round'/>"
            f"<circle cx='-102' cy='50' r='34' fill='none' stroke='{c1}' stroke-width='13'/><circle cx='-102' cy='-50' r='34' fill='none' stroke='{c2}' stroke-width='13'/>"
            f"<circle r='11' fill='{fundo}' stroke='{c1}' stroke-width='6'/></g>")


def a06():
    s = f"<rect x='60' y='60' width='440' height='66' rx='33' fill='{PLUM}'/>" + T(280, 104, "oficina de arranjos", 34, PAPEL, "d", 700, "middle", 0)
    cal = f"<rect x='72' y='220' width='560' height='570' rx='16' fill='{CARTAO}'/><path d='M72,236 a16,16 0 0 1 16,-16 h528 a16,16 0 0 1 16,16 v74 h-560 z' fill='{CORAL}'/>"
    cal += T(100, 286, "novembro", 56, PAPEL, ls=-.04) + T(604, 284, "2026", 38, PAPEL, "d", 700, "end", 0)
    cal += "".join(f"<rect x='{x}' y='198' width='22' height='56' rx='11' fill='{PLUM}'/>" for x in (170, 510))
    cal += "".join(T(112 + i * 80, 372, d, 26, CORAL, "d", 700, "middle", 0) for i, d in enumerate("DSTQQSS"))
    dia = 1
    for r in range(5):
        for c in range(7):
            if dia > 30:
                break
            cx, cy = 112 + c * 80, 458 + r * 72
            if dia == 14:
                cal += f"<circle cx='{cx}' cy='{cy}' r='36' fill='{PLUM}'/>" + T(cx, cy + 12, dia, 34, PAPEL, "d", 700, "middle", 0)
            else:
                cal += T(cx, cy + 12, dia, 34, PLUM, "d", 700, "middle", 0)
            dia += 1
    s += sh(cal)
    for i, (a, b) in enumerate([("sábado", "10h às 12h"), ("material", "incluso"), ("valor", "R$ 120")]):
        y = 300 + i * 170
        s += f"<line x1='690' y1='{y - 40}' x2='1008' y2='{y - 40}' stroke='{PLUM}' stroke-width='3'/>" + T(690, y, a, 30, CORAL, "d", 700, "start", 0) + T(690, y + 62, b, 62, PLUM, ls=-.04)
    s += sh(tesoura(800, 790, -18, PLUM, CORAL, PAPEL, .95) + folha(910, 700, 70, 64, FOLHA) + folha(930, 800, 60, 118, FOLHA) + haste(880, 870, 940, 900, FOLHA, 8))
    s += T(60, 985, "aprenda a montar", 104, PLUM, ls=-.045) + T(60, 1095, "o seu buquê.", 104, PLUM, ls=-.045)
    return pagina(PAPEL, s + selo())


A["06-oficina"] = ("Oficina de arranjos", a06)


# 7 — bastidores: degraus que sobem hora a hora, cada um com seu ícone
def ic_colheita():
    s = f"<line x1='0' y1='100' x2='130' y2='100' stroke='{PAPEL}' stroke-width='7' stroke-linecap='round'/>"
    s += "".join(f"<line x1='65' y1='100' x2='{65 + 70 * math.cos(math.radians(a)):.1f}' y2='{100 - 70 * math.sin(math.radians(a)):.1f}' stroke='{SOL}' stroke-width='7' stroke-linecap='round'/>" for a in (25, 55, 90, 125, 155))
    s += f"<path d='M25,100 a40,40 0 0 1 80,0 z' fill='{SOL}'/>"
    s += "".join(haste(x, 100, x, 74, PAPEL, 6) + f"<circle cx='{x}' cy='68' r='9' fill='{ROSA}'/>" for x in (8, 122))
    return s


def ic_caminhao():
    s = f"<rect x='4' y='44' width='80' height='52' rx='6' fill='{PAPEL}'/><polygon points='84,58 108,58 126,78 126,96 84,96' fill='{CORAL}'/>"
    s += "".join(f"<circle cx='{x}' cy='40' r='12' fill='{c}'/>" for x, c in ((22, ROSA), (44, SOL), (66, ROSA)))
    s += "".join(f"<circle cx='{x}' cy='98' r='13' fill='{PLUM}'/><circle cx='{x}' cy='98' r='5' fill='{PAPEL}'/>" for x in (30, 102))
    return s


def ic_tesoura():
    return tesoura(80, 60, -18, PAPEL, ROSA, FOLHA, .6)


def ic_vitrine():
    s = f"<rect x='10' y='50' width='110' height='58' fill='{PAPEL}'/>"
    s += "".join(f"<rect x='{10 + i * 22}' y='12' width='22' height='38' fill='{CORAL if i % 2 == 0 else PAPEL}'/>" for i in range(5))
    s += f"<rect x='28' y='72' width='26' height='36' fill='{PLUM}'/><circle cx='92' cy='80' r='13' fill='{ROSA}'/><rect x='84' y='92' width='16' height='16' fill='{SOL}'/>"
    return s


def a07():
    s = T(60, 235, "do campo", 170, PAPEL, ls=-.045) + T(60, 385, "à vitrine.", 170, SOL, ls=-.045)
    etapas = [("05h", ("colheita", "no sítio"), ic_colheita, ROSA, PLUM, 200), ("07h", ("chegada", "à loja"), ic_caminhao, SOL, PLUM, 320),
              ("09h", ("corte e", "preparo"), ic_tesoura, CORAL, PAPEL, 440), ("10h", ("na", "vitrine"), ic_vitrine, PLUM, PAPEL, 560)]
    for i, (hora, nome, ic, fundo, cor, alt) in enumerate(etapas):
        x, topo = 72 + i * 237, 1170 - alt
        s += sh(f"<rect x='{x}' y='{topo}' width='225' height='{alt}' rx='20' fill='{fundo}'/>")
        s += T(x + 22, topo + 84, hora, 80, cor, ls=-.05) + T(x + 22, topo + 130, nome[0], 30, cor, "d", 700, "start", -.01) + T(x + 22, topo + 164, nome[1], 30, cor, "d", 700, "start", -.01)
        s += f"<g transform='translate({x + 8} {topo - 134})'>{ic()}</g>"
    return pagina("#0F3B26", s + selo(PAPEL, PLUM))


A["07-bastidores"] = ("Bastidores: do campo à vitrine", a07)


# 8 — encomenda: conversa de WhatsApp
def balao(x, y, w, h, cor, texto, cor_t, direita):
    tx = x + w - 22 if direita else x + 22
    cauda = (f"<polygon points='{x + w - 30},{y + h - 30} {x + w + 22},{y + h} {x + w - 70},{y + h}' fill='{cor}'/>" if direita
             else f"<polygon points='{x + 30},{y + h - 30} {x - 22},{y + h} {x + 70},{y + h}' fill='{cor}'/>")
    return sh(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='44' fill='{cor}'/>{cauda}") + T(x + w / 2, y + h / 2 + 14, texto, 40, cor_t, "d", 700, "middle", -.01)


def a08():
    s = sh(blob(930, 250, 270, 9, CORAL))
    s += T(60, 235, "peça", 205, PAPEL, ls=-.04) + T(60, 450, "pelo", 205, PAPEL, ls=-.04) + T(60, 665, "zap.", 205, SOL, ls=-.04)
    s += balao(300, 745, 720, 130, SOL, "quero o buquê da semana!", PLUM, True)
    s += balao(60, 925, 700, 130, PAPEL, "anotado! retira às 10h?", PLUM, False)
    s += balao(660, 1095, 360, 110, SOL, "pode ser!", PLUM, True)
    return pagina(PLUM, s + selo(PAPEL, PLUM))


A["08-encomenda"] = ("Encomenda pelo WhatsApp", a08)


def renderizar(html, png):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=12000", f"--screenshot={png}", pathlib.Path(html).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def main():
    for nome, (rotulo, fn) in A.items():
        h = AQUI / f"{nome}.html"
        h.write_text(f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{rotulo}</title><style>{BASE}</style></head><body>{fn()}</body></html>", encoding="utf-8")
        renderizar(h, AQUI / f"{nome}.png")
        print("ok", nome)


if __name__ == "__main__":
    main()
