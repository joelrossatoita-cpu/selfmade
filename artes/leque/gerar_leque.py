"""Três artes 9:16 (1080x1920) para o leque da tela inicial.
Negócios e nomes fictícios, só para exemplo. Paleta: verdes, branco e creme.
Estilos: 1) retrô anos 70 (curvas "groovy"), 2) colagem de papel recortado, 3) xilogravura.
Uso: python gerar_leque.py"""
import os, math, subprocess, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Shrikhand&family=Alfa+Slab+One&family=DM+Serif+Display:ital@0;1"
         "&family=Inter+Tight:wght@400;500;600&family=Fraunces:ital,opsz,wght@1,9..144,600&display=swap');")
BASE = FONTS + """*{box-sizing:border-box;margin:0;padding:0}html,body{width:1080px;height:1920px;overflow:hidden}
.p{position:relative;width:1080px;height:1920px;overflow:hidden}.a{position:absolute}"""

# cores do projeto
CREME, BRANCO = "#F3EFE6", "#FFFFFF"
V0, V1, V2, V3, V4 = "#0F3B27", "#1E6B47", "#3F9F6B", "#7FD1A1", "#CDEBD8"

D = {}

# ------------------------------------------------------------------ 1 · Feira Verde — retrô anos 70
arcos = "".join(
    f'<circle cx="540" cy="800" r="{r}" fill="{c}"/>'
    for r, c in [(470, V0), (390, V1), (310, V2), (230, V3), (150, V4), (70, CREME)])


def onda(y, amp, cor, fase=0):
    pts = []
    for x in range(-40, 1141, 20):
        pts.append(f"{x},{y + amp * math.sin((x / 1080) * 4 * math.pi + fase):.1f}")
    return f'<polygon points="{" ".join(pts)} 1140,1960 -40,1960" fill="{cor}"/>'


ondas = "".join(onda(1580 + i * 62, 34, c, i * .9) for i, c in enumerate([V4, V3, V2, V1, V0]))
D["01-feira"] = ("Feira orgânica · retrô anos 70", f"""
<div class="p" style="background:{CREME};font-family:'Inter Tight',sans-serif;color:{V0}">
  <svg class="a" style="inset:0" width="1080" height="1920" viewBox="0 0 1080 1920">
    <defs><clipPath id="m"><rect x="0" y="330" width="1080" height="470"/></clipPath></defs>
    <g clip-path="url(#m)">{arcos}</g>
    <g fill="{CREME}"><circle cx="150" cy="560" r="16"/><circle cx="930" cy="470" r="22"/><circle cx="880" cy="650" r="12"/><circle cx="210" cy="420" r="10"/></g>
    {ondas}
  </svg>
  <div class="a" style="left:72px;top:250px;border:4px solid {V0};border-radius:999px;padding:12px 30px;font:600 34px 'Inter Tight';background:{CREME}">Todo sábado · 7h às 12h</div>
  <div class="a" style="left:0;right:0;top:845px;text-align:center;font-family:'Shrikhand';line-height:.95;color:{V1}">
    <div style="font-size:230px;text-shadow:9px 9px 0 {V4},18px 18px 0 {V3}">Feira</div>
    <div style="font-size:230px;text-shadow:9px 9px 0 {V4},18px 18px 0 {V3};margin-top:18px">Verde</div></div>
  <div class="a" style="left:80px;right:80px;top:1368px;text-align:center;font:500 41px 'Inter Tight';line-height:1.25;white-space:nowrap">Hortaliças da estação, direto do produtor.</div>
  <div class="a" style="left:150px;right:150px;top:1470px;background:{V0};color:{CREME};border-radius:999px;padding:30px 0;text-align:center;font:600 46px 'Inter Tight';box-shadow:0 10px 0 {V2}">Reserve sua cesta →</div>
  <div class="a" style="left:0;right:0;top:1640px;text-align:center;font:700 36px 'Inter Tight';color:{V0};letter-spacing:.04em;-webkit-text-stroke:7px {CREME};paint-order:stroke fill">@feiraverde</div>
</div>""")

# ------------------------------------------------------------------ 2 · Flora Ateliê — colagem de papel recortado
def folha(cx, cy, w, h, rot, cor):
    return (f'<path transform="translate({cx} {cy}) rotate({rot})" fill="{cor}" '
            f'd="M0 {-h/2} C{w*.62} {-h*.32} {w*.58} {h*.28} 0 {h/2} C{-w*.5} {h*.3} {-w*.66} {-h*.3} 0 {-h/2}Z"/>')


def flor(cx, cy, r, n, pet, mid):
    g = ""
    for i in range(n):
        ang = i * 360 / n
        g += f'<ellipse cx="{cx}" cy="{cy - r}" rx="{r*.42}" ry="{r*.85}" fill="{pet}" transform="rotate({ang} {cx} {cy})"/>'
    return g + f'<circle cx="{cx}" cy="{cy}" r="{r*.42}" fill="{mid}"/>'


fl = "".join([
    folha(190, 520, 230, 560, -28, V2), folha(330, 640, 200, 520, 14, V1), folha(840, 470, 220, 600, 24, V1),
    folha(960, 650, 190, 470, -16, V3), folha(560, 460, 210, 480, 4, V4), folha(110, 790, 170, 380, -52, V3),
    folha(700, 760, 200, 420, 40, V2),
])
flores = (flor(480, 640, 150, 8, BRANCO, V3) + flor(790, 810, 110, 7, V4, V1) + flor(250, 830, 120, 9, BRANCO, V2))
D["02-flora"] = ("Floricultura · colagem de papel", f"""
<div class="p" style="background:{CREME};font-family:'Inter Tight',sans-serif;color:{V0}">
  <svg class="a" style="inset:0;filter:drop-shadow(0 10px 0 rgba(15,59,39,.22))" width="1080" height="1920" viewBox="0 0 1080 1920">
    {fl}{flores}
    <path fill="{V0}" d="M0 1560 C200 1470 330 1640 540 1560 S900 1470 1080 1580 V1920 H0Z"/>
    <path fill="{V1}" d="M0 1640 C220 1560 360 1720 560 1650 S900 1580 1080 1670 V1920 H0Z"/>
  </svg>
  <div class="a" style="left:72px;top:250px;background:{BRANCO};border-radius:14px;padding:12px 28px;font:600 34px 'Inter Tight';transform:rotate(-3deg);box-shadow:0 8px 0 rgba(15,59,39,.18)">Floricultura e ateliê</div>
  <div class="a" style="left:60px;right:60px;top:1030px;text-align:center;font-family:'DM Serif Display';line-height:.92;color:{V0}">
    <div style="font-size:250px;letter-spacing:-4px;text-shadow:8px 8px 0 {V4}">Buquês</div>
    <div style="font-size:110px;font-style:italic;color:{V1};margin-top:6px">da semana</div></div>
  <div class="a" style="left:130px;right:130px;top:1380px;background:{BRANCO};border-radius:20px;padding:26px 0;text-align:center;font:600 44px 'Inter Tight';color:{V0};box-shadow:0 10px 0 {V3}">Encomende pelo WhatsApp →</div>
  <div class="a" style="left:0;right:0;top:1632px;text-align:center;font:600 36px 'Inter Tight';color:{CREME};letter-spacing:.04em">flora ateliê · @floraatelie</div>
</div>""")

# ------------------------------------------------------------------ 3 · Casa Folha — xilogravura
hach = "".join(f'<line x1="{x}" y1="0" x2="{x - 90}" y2="400" />' for x in range(40, 700, 22))
folhas_chá = "".join(
    f'<path transform="translate({x} {y}) rotate({r})" d="M0 -88 Q62 -6 0 78 Q-62 -6 0 -88Z M0 -88 L0 78 M0 78 L0 118" fill="{V0}" stroke="{CREME}" stroke-width="5"/>'
    for x, y, r in [(135, 430, -35), (145, 640, 22), (125, 850, -18), (945, 440, 35), (935, 650, -22), (955, 860, 20), (130, 1040, -12), (950, 1040, 14)])
D["03-cha"] = ("Casa de chá · xilogravura", f"""
<div class="p" style="background:{CREME};font-family:'Inter Tight',sans-serif;color:{V0}">
  <svg width="0" height="0" class="a"><defs><filter id="r"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="7"/></filter></defs></svg>
  <div class="a" style="inset:0;filter:url(#r)">
    <div class="a" style="inset:36px;border:16px solid {V0}"></div>
    <div class="a" style="inset:76px;border:4px dashed {V0}"></div>
    <svg class="a" style="left:190px;top:330px" width="700" height="700" viewBox="0 0 700 700">
      <defs><clipPath id="lua"><circle cx="350" cy="350" r="330"/></clipPath></defs>
      <circle cx="350" cy="350" r="340" fill="{V0}"/>
      <g clip-path="url(#lua)" fill="none" stroke="{V2}" stroke-width="6"><g transform="translate(0 290)">{hach}</g></g>
      <circle cx="350" cy="350" r="330" fill="none" stroke="{CREME}" stroke-width="8"/>
      <g transform="translate(110 250)">
        <ellipse cx="240" cy="330" rx="250" ry="38" fill="{CREME}" stroke="{V0}" stroke-width="8"/>
        <path d="M30 130 H450 C450 250 380 320 240 320 C100 320 30 250 30 130Z" fill="{CREME}" stroke="{V0}" stroke-width="12"/>
        <path d="M450 160 C540 160 540 280 420 270" fill="none" stroke="{CREME}" stroke-width="30"/>
        <path d="M450 160 C540 160 540 280 420 270" fill="none" stroke="{V0}" stroke-width="10"/>
        <ellipse cx="240" cy="130" rx="210" ry="30" fill="{V1}" stroke="{V0}" stroke-width="10"/>
        <g stroke="{V0}" stroke-width="5"><line x1="300" y1="190" x2="250" y2="300"/><line x1="340" y1="190" x2="290" y2="290"/><line x1="380" y1="190" x2="335" y2="270"/><line x1="420" y1="200" x2="380" y2="250"/></g>
        <g fill="none" stroke="{CREME}" stroke-width="14" stroke-linecap="round"><path d="M160 90 C130 40 200 20 170 -30"/><path d="M250 90 C220 30 290 10 260 -50"/><path d="M340 90 C310 40 380 20 350 -30"/></g>
      </g>
    </svg>
    <svg class="a" style="inset:0" width="1080" height="1920" viewBox="0 0 1080 1920">{folhas_chá}</svg>
  </div>
  <div class="a" style="left:0;right:0;top:250px;text-align:center;font:600 34px 'Inter Tight';letter-spacing:.2em;text-transform:uppercase">Casa Folha · chás e infusões</div>
  <div class="a" style="left:0;right:0;top:1090px;text-align:center;font-family:'Alfa Slab One';line-height:.95;color:{V1};filter:url(#r)">
    <div style="font-size:170px;text-shadow:7px 7px 0 {V0}">Chá da</div>
    <div style="font-size:200px;text-shadow:7px 7px 0 {V0}">tarde</div></div>
  <div class="a" style="left:120px;right:120px;top:1432px;background:{V0};color:{CREME};padding:26px 0;text-align:center;font:600 42px 'Inter Tight';letter-spacing:.02em;transform:rotate(-1.5deg);filter:url(#r)">Peça seu kit de chá pelo WhatsApp</div>
  <div class="a" style="left:0;right:0;top:1632px;text-align:center;font:600 34px 'Inter Tight';letter-spacing:.06em">@casafolha</div>
</div>""")


def renderizar(html, png):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1920", "--virtual-time-budget=14000", f"--screenshot={png}", pathlib.Path(html).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def main():
    for nome, (rotulo, corpo) in D.items():
        h = AQUI / f"{nome}.html"
        h.write_text(f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{rotulo}</title><style>{BASE}</style></head><body>{corpo}</body></html>", encoding="utf-8")
        renderizar(h, AQUI / f"{nome}.png")
        print("ok", nome)


if __name__ == "__main__":
    main()
