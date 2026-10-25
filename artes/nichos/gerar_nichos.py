"""Gera 4 artes (1080x1350) de outros nichos para o giro 3D da página inicial, em dois estilos além da colagem da Verbena
e sempre na paleta de verdes e creme do site: neobrutalismo (academia e padaria) e emblema retrô (barbearia e cafeteria).
Uso: python gerar_nichos.py
Os negócios, preços, horários e textos são fictícios e servem só como exemplo de design."""
import os, sys, math, subprocess, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "verbena"))
import gerar_verbena as V  # noqa: E402  (paleta, filtros e a tesoura)

CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
PAPEL, TINTA, VERDE, LIMA, MENTA, SALVIA = V.PAPEL, V.PLUM, V.CORAL, V.SOL, V.ROSA, V.LILAS
FAM = {"sg": "Space Grotesk,sans-serif", "sm": "Space Mono,monospace", "af": "Abril Fatface,serif", "bn": "Bebas Neue,sans-serif"}
BASE = """@import url('../verbena/fonts/fontes.css');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#fff}
svg{display:block}
"""


def X(x, y, s, size, fill, fam, anchor="start", ls=0, rot=0):
    r = f" transform='rotate({rot} {x} {y})'" if rot else ""
    return f"<text x='{x}' y='{y}' font-size='{size}' fill='{fill}' text-anchor='{anchor}'{r} style='letter-spacing:{ls}em;font-family:{FAM[fam]}'>{s}</text>"


def pagina(fundo, corpo, grao=False):
    g = "<rect width='1080' height='1350' filter='url(#gr)' opacity='.3'/>" if grao else ""
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1350' viewBox='0 0 1080 1350'>{V.DEFS}"
            f"<rect width='1080' height='1350' fill='{fundo}'/>{corpo}{g}</svg>")


def caixa(x, y, w, h, fill, conteudo="", sh=10, r=0, rot=0, borda=8):
    cx, cy = x + w / 2, y + h / 2
    return (f"<g transform='rotate({rot} {cx} {cy})'><rect x='{x + sh}' y='{y + sh}' width='{w}' height='{h}' rx='{r}' fill='{TINTA}'/>"
            f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{r}' fill='{fill}' stroke='{TINTA}' stroke-width='{borda}'/>{conteudo}</g>")


A = {}

# 1 — neobrutalismo: academia
def pesa(c1, c2, trac, dx=0):
    s = f"<rect x='{-150 + dx}' y='-14' width='300' height='28' fill='{c1}' stroke='{trac}' stroke-width='6'/>"
    for lado in (-1, 1):
        s += f"<rect x='{lado * 118 - 18 + dx}' y='-78' width='36' height='156' fill='{c2}' stroke='{trac}' stroke-width='6'/>"
        s += f"<rect x='{lado * 150 - 14 + (14 if lado < 0 else 0) + dx}' y='-52' width='28' height='104' fill='{c1}' stroke='{trac}' stroke-width='6'/>"
    return s


def a_academia():
    s = "<defs><pattern id='grade' width='60' height='60' patternUnits='userSpaceOnUse'><path d='M60 0H0V60' fill='none' stroke='#13241C' stroke-opacity='.13' stroke-width='2'/></pattern></defs>"
    s += "<rect width='1080' height='1350' fill='url(#grade)'/>"
    s += caixa(60, 60, 960, 92, PAPEL, X(92, 123, "PULSO STUDIO", 38, TINTA, "sm") + X(988, 123, "TREINO #03", 38, VERDE, "sm", "end"))
    s += caixa(60, 200, 940, 470, VERDE, X(100, 345, "segunda é", 142, PAPEL, "sg", ls=-.045) + X(100, 475, "dia de", 142, PAPEL, "sg", ls=-.045) + X(100, 605, "perna.", 142, LIMA, "sg", ls=-.045), 14, rot=-1.5)
    linhas = ""
    for i, (nome, rep, ok) in enumerate([("agachamento", "4×12", True), ("afundo", "3×10", True), ("panturrilha", "3×15", False)]):
        y = 880 + i * 92
        linhas += f"<rect x='92' y='{y - 40}' width='46' height='46' fill='{VERDE if ok else PAPEL}' stroke='{TINTA}' stroke-width='6'/>"
        if ok:
            linhas += f"<path d='M102,{y - 17} l10,11 l18,-24' fill='none' stroke='{PAPEL}' stroke-width='7' stroke-linecap='square'/>"
        linhas += X(162, y, nome, 42, TINTA, "sg") + X(668, y, rep, 36, VERDE, "sm", "end")
        if i < 2:
            linhas += f"<line x1='92' y1='{y + 30}' x2='668' y2='{y + 30}' stroke='{TINTA}' stroke-width='3' stroke-dasharray='10 8'/>"
    s += caixa(60, 730, 640, 380, PAPEL, X(92, 800, "treino de hoje", 32, VERDE, "sm") + linhas, 12, rot=1)
    sombra = f"<g transform='translate(870 950) rotate(-22)'>{pesa(TINTA, TINTA, TINTA)}</g>"
    s += f"<g transform='translate(12 12)'>{sombra}</g><g transform='translate(870 950) rotate(-22)'>{pesa(SALVIA, MENTA, TINTA)}</g>"
    s += caixa(830, 640, 150, 150, PAPEL, X(905, 735, "bora!", 54, TINTA, "sg", "middle", -.03, 12), 8, r=75, rot=0)
    s += caixa(60, 1236, 380, 70, PAPEL, X(250, 1283, "@pulsostudio", 34, TINTA, "sm", "middle"), 6)
    return pagina(LIMA, s)


A["09-academia"] = ("Academia Pulso Studio", a_academia)


# 2 — neobrutalismo: padaria
def pao_rustico():
    s = f"<ellipse cx='150' cy='150' rx='112' ry='70' fill='{LIMA}' stroke='{TINTA}' stroke-width='8'/>"
    return s + "".join(f"<line x1='{x}' y1='112' x2='{x + 26}' y2='150' stroke='{TINTA}' stroke-width='7' stroke-linecap='round'/>" for x in (108, 140, 172))


def brioche():
    s = f"<circle cx='150' cy='148' r='82' fill='{SALVIA}' stroke='{TINTA}' stroke-width='8'/><circle cx='150' cy='72' r='24' fill='{SALVIA}' stroke='{TINTA}' stroke-width='8'/>"
    return s + "".join(f"<line x1='{x}' y1='170' x2='{x + 14}' y2='134' stroke='{TINTA}' stroke-width='6' stroke-linecap='round'/>" for x in (112, 143, 174))


def croissant():
    s = f"<path d='M30,200 C10,70 290,70 270,200 C246,214 222,170 150,166 C78,170 54,214 30,200 Z' fill='{MENTA}' stroke='{TINTA}' stroke-width='8' stroke-linejoin='round'/>"
    return s + "".join(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{TINTA}' stroke-width='6' stroke-linecap='round'/>" for x1, y1, x2, y2 in ((96, 124, 112, 160), (150, 106, 150, 138), (204, 124, 188, 160)))


def a_padaria():
    s = "<defs><pattern id='pontos' width='40' height='40' patternUnits='userSpaceOnUse'><circle cx='20' cy='20' r='3.5' fill='#13241C' fill-opacity='.16'/></pattern></defs><rect width='1080' height='1350' fill='url(#pontos)'/>"
    s += caixa(60, 60, 540, 82, LIMA, X(330, 114, "padaria fermento", 36, TINTA, "sm", "middle"), 8, r=41)
    s += caixa(40, 350, 800, 180, LIMA, "", 10, rot=-2)
    s += X(60, 330, "fornada", 200, TINTA, "sg", ls=-.05) + X(70, 505, "saindo.", 180, VERDE, "sg", ls=-.05, rot=-2)
    s += caixa(790, 120, 200, 200, VERDE, X(890, 212, "toda", 40, PAPEL, "sm", "middle", 0, 10) + X(890, 258, "manhã", 40, PAPEL, "sm", "middle", 0, 10), 8, r=100)
    for i, (nome1, nome2, preco, ic) in enumerate([("pão", "rústico", "R$ 16", pao_rustico), ("brioche", "", "R$ 9", brioche), ("croissant", "", "R$ 12", croissant)]):
        x = 60 + i * 320
        c = f"<g transform='translate({x} 640)'>{ic()}</g>"
        c += X(x + 24, 930, nome1, 46, TINTA, "sg", ls=-.03) + (X(x + 24, 978, nome2, 46, TINTA, "sg", ls=-.03) if nome2 else "")
        c += f"<circle cx='{x + 226}' cy='1040' r='52' fill='{VERDE}' stroke='{TINTA}' stroke-width='6'/>" + X(x + 226, 1050, preco, 28, PAPEL, "sm", "middle")
        s += caixa(x, 620, 300, 480, PAPEL, c, 10, rot=(-1.5, 1, -1)[i])
    s += caixa(60, 1236, 380, 70, PAPEL, X(250, 1283, "@padariafermento", 32, TINTA, "sm", "middle"), 6)
    return pagina(PAPEL, s)


A["10-padaria"] = ("Padaria Fermento", a_padaria)


# 3 — emblema retrô: barbearia
def raios(cx, cy, n, cor, r=1500):
    p = ""
    for i in range(0, n, 2):
        a1, a2 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
        p += f"<polygon points='{cx},{cy} {cx + r * math.cos(a1):.1f},{cy + r * math.sin(a1):.1f} {cx + r * math.cos(a2):.1f},{cy + r * math.sin(a2):.1f}' fill='{cor}'/>"
    return p


def poste(x):
    return (f"<defs><pattern id='lista' width='90' height='90' patternUnits='userSpaceOnUse' patternTransform='rotate(35)'><rect width='90' height='30' fill='{PAPEL}'/><rect y='30' width='90' height='30' fill='{MENTA}'/><rect y='60' width='90' height='30' fill='{TINTA}'/></pattern>"
            f"<clipPath id='cap{x}'><rect x='{x}' y='590' width='70' height='520' rx='35'/></clipPath></defs>"
            f"<rect x='{x - 8}' y='570' width='86' height='36' rx='10' fill='{PAPEL}'/><rect x='{x - 8}' y='1094' width='86' height='36' rx='10' fill='{PAPEL}'/>"
            f"<rect x='{x}' y='590' width='70' height='520' rx='35' fill='url(#lista)'/><rect x='{x}' y='590' width='70' height='520' rx='35' fill='none' stroke='{PAPEL}' stroke-width='5'/>")


def moldura(cor):
    return f"<rect x='36' y='36' width='1008' height='1278' fill='none' stroke='{cor}' stroke-width='5'/><rect x='54' y='54' width='972' height='1242' fill='none' stroke='{cor}' stroke-width='2'/>"


def a_barbearia():
    s = raios(540, 350, 56, "#237A52") + moldura(PAPEL)
    s += f"<circle cx='540' cy='350' r='200' fill='{PAPEL}'/><circle cx='540' cy='350' r='186' fill='none' stroke='{VERDE}' stroke-width='3'/><circle cx='540' cy='350' r='112' fill='{VERDE}'/>"
    s += f"<defs><path id='arco' d='M540,350 m-152,0 a152,152 0 1,1 304,0 a152,152 0 1,1 -304,0'/></defs>"
    s += f"<text font-size='50' fill='{VERDE}' style='letter-spacing:.06em;font-family:{FAM['bn']}'><textPath href='#arco' textLength='940' lengthAdjust='spacing'>BARBEARIA DOM BIGODE • CORTE E BARBA • NAVALHA • </textPath></text>"
    s += V.tesoura(548, 352, -35, PAPEL, MENTA, VERDE, .66)
    s += poste(110) + poste(900)
    s += X(540, 705, "corte", 170, PAPEL, "af", "middle", -.01) + X(540, 855, "& barba.", 170, LIMA, "af", "middle", -.01)
    s += f"<line x1='330' y1='925' x2='500' y2='925' stroke='{PAPEL}' stroke-width='3'/><line x1='580' y1='925' x2='750' y2='925' stroke='{PAPEL}' stroke-width='3'/><polygon points='540,908 557,925 540,942 523,925' fill='{LIMA}'/>"
    s += X(540, 1035, "seg a sáb", 96, PAPEL, "bn", "middle", .03) + X(540, 1120, "9h às 19h", 96, LIMA, "bn", "middle", .03) + X(540, 1172, "rua do comércio, 45", 40, MENTA, "bn", "middle", .06)
    s += f"<rect x='355' y='1206' width='370' height='60' rx='30' fill='{PAPEL}'/>" + X(540, 1247, "@dombigode.barbearia", 36, TINTA, "bn", "middle", .04)
    return pagina(VERDE, s, True)


A["11-barbearia"] = ("Barbearia Dom Bigode", a_barbearia)


# 4 — emblema retrô: cafeteria
def a_cafeteria():
    s = raios(540, 830, 48, V.ROSA) + moldura(TINTA)
    s += X(540, 262, "café coado", 160, TINTA, "af", "middle", -.01) + X(540, 412, "na hora.", 160, VERDE, "af", "middle", -.01)
    s += f"<circle cx='765' cy='800' r='70' fill='none' stroke='{VERDE}' stroke-width='36'/>"
    s += f"<ellipse cx='540' cy='1015' rx='270' ry='42' fill='{TINTA}'/><ellipse cx='540' cy='1000' rx='270' ry='42' fill='{SALVIA}' stroke='{TINTA}' stroke-width='6'/>"
    s += f"<path d='M340,700 H740 C740,890 690,985 540,985 C390,985 340,890 340,700 Z' fill='{VERDE}' stroke='{TINTA}' stroke-width='8'/>"
    s += f"<ellipse cx='540' cy='700' rx='200' ry='38' fill='{TINTA}'/><ellipse cx='510' cy='694' rx='90' ry='12' fill='#2C3F34'/>"
    s += X(540, 890, "BULE", 96, PAPEL, "bn", "middle", .1)
    for x, d in ((470, 0), (540, 26), (610, 0)):
        s += f"<path d='M{x},{650 - d} C{x - 36},{600 - d} {x + 36},{560 - d} {x},{510 - d}' fill='none' stroke='{TINTA}' stroke-width='9' stroke-linecap='round'/>"
    s += caixa(790, 540, 190, 190, LIMA, f"<circle cx='885' cy='635' r='78' fill='none' stroke='{TINTA}' stroke-width='3' stroke-dasharray='6 7'/>" + X(885, 628, "TORRA", 46, TINTA, "bn", "middle", .05, 10) + X(885, 674, "ARTESANAL", 36, TINTA, "bn", "middle", .04, 10), 8, r=95, borda=5)
    s += f"<rect x='54' y='1090' width='972' height='84' fill='{TINTA}'/>" + X(540, 1150, "terça a domingo • 8h às 17h", 62, PAPEL, "bn", "middle", .05)
    s += f"<rect x='355' y='1206' width='370' height='60' rx='30' fill='{TINTA}'/>" + X(540, 1247, "@cafebule.coado", 36, PAPEL, "bn", "middle", .05)
    return pagina(PAPEL, s, True)


A["12-cafeteria"] = ("Cafeteria Bule", a_cafeteria)


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
