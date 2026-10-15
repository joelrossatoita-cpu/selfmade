"""Seis artes de 1080x1350, cada uma com identidade e estilo próprios (nada de minimalismo).
Negócios, nomes e textos são fictícios e servem só como exemplo.
Uso: python gerar_identidades.py"""
import os, subprocess, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=DM+Serif+Display&family=Rye&family=Anton&family=Barlow+Condensed:ital,wght@1,700;1,800"
         "&family=Bebas+Neue&family=Bowlby+One+SC&family=Caveat:wght@600;700&family=Chewy&family=Fredoka:wght@500;600;700"
         "&family=Pacifico&family=Playfair+Display:ital,wght@1,500;1,700&family=Rubik:wght@500;700;800&display=swap');")
BASE = FONTS + """*{box-sizing:border-box;margin:0;padding:0}html,body{width:1080px;height:1350px;overflow:hidden}
.p{position:relative;width:1080px;height:1350px;overflow:hidden}.a{position:absolute}"""

D = {}

# ---------------------------------------------------------------- 1 · Brasa Café — minimalista
D["01-cafeteria"] = ("Cafeteria", r"""
<div class="p" style="background:#F5EDE0;color:#3A2417;font-family:'Rubik',sans-serif">
  <div class="a" style="left:92px;top:92px;display:flex;align-items:center;gap:22px">
    <svg width="66" height="66" viewBox="0 0 64 64" fill="none" stroke="#3A2417" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"><path d="M10 24h34v12a15 15 0 0 1-15 15h-4a15 15 0 0 1-15-15z"/><path d="M44 28h3a7 7 0 0 1 0 14h-6"/><path d="M20 8c-3 4 3 5 0 10M28 6c-3 4 3 5 0 10M36 8c-3 4 3 5 0 10"/></svg>
    <div style="font:400 54px 'DM Serif Display';letter-spacing:-.5px">brasa café</div></div>
  <div class="a" style="right:92px;top:112px;font:500 30px 'Rubik';letter-spacing:.14em">07H — 10H</div>
  <div class="a" style="left:92px;right:92px;top:226px;height:2px;background:#3A2417;opacity:.25"></div>
  <div class="a" style="left:92px;top:340px;font:400 196px 'DM Serif Display';line-height:.95;letter-spacing:-5px;white-space:nowrap">Combo<br>da manhã<span style="color:#D9531E">.</span></div>
  <div class="a" style="left:96px;top:800px;font:400 50px 'Rubik';line-height:1.25;max-width:500px;opacity:.82">café + pão de queijo, saindo do forno agora.</div>
  <div class="a" style="right:-110px;bottom:-110px;width:560px;height:560px;border-radius:50%;background:#D9531E"></div>
  <div class="a" style="left:92px;bottom:92px;font:500 32px 'Rubik';line-height:1.4">Rua das Flores, 120<br><span style="color:#D9531E">@brasacafe</span></div>
</div>""")

POLE_TEMPLATE_A = '''<rect x="30" y="0" width="90" height="34" rx="10" fill="#14284B"/><rect x="38" y="30" width="74" height="300" rx="8" fill="#fff" stroke="#14284B" stroke-width="8"/>
    <clipPath id="pole1"><rect x="42" y="34" width="66" height="292" rx="4"/></clipPath>
    <g clip-path="url(#pole1)"><g transform="rotate(-30 75 180)"><rect x="0" y="-60" width="26" height="560" fill="#C8312B"/><rect x="52" y="-60" width="26" height="560" fill="#14284B"/><rect x="104" y="-60" width="26" height="560" fill="#C8312B"/><rect x="156" y="-60" width="26" height="560" fill="#14284B"/><rect x="208" y="-60" width="26" height="560" fill="#C8312B"/></g></g>
    <rect x="30" y="326" width="90" height="34" rx="10" fill="#14284B"/>'''
POLE_TEMPLATE_B = '''<rect x="30" y="0" width="90" height="34" rx="10" fill="#14284B"/><rect x="38" y="30" width="74" height="300" rx="8" fill="#fff" stroke="#14284B" stroke-width="8"/>
    <clipPath id="pole2"><rect x="42" y="34" width="66" height="292" rx="4"/></clipPath>
    <g clip-path="url(#pole2)"><g transform="rotate(-30 75 180)"><rect x="0" y="-60" width="26" height="560" fill="#C8312B"/><rect x="52" y="-60" width="26" height="560" fill="#14284B"/><rect x="104" y="-60" width="26" height="560" fill="#C8312B"/><rect x="156" y="-60" width="26" height="560" fill="#14284B"/><rect x="208" y="-60" width="26" height="560" fill="#C8312B"/></g></g>
    <rect x="30" y="326" width="90" height="34" rx="10" fill="#14284B"/>'''

# ---------------------------------------------------------------- 2 · Navalha — old school (tatuagem clássica)
D["02-barbearia"] = ("Barbearia", r"""
<div class="p" style="background:#F2E6C9;color:#14284B;font-family:'Rye',serif">
  <div class="a" style="inset:0;background:radial-gradient(circle,rgba(20,40,75,.16) 3px,transparent 3.5px) 0 0/30px 30px;-webkit-mask-image:linear-gradient(180deg,#000 0,transparent 55%)"></div>
  <div class="a" style="inset:34px;border:10px solid #14284B"></div><div class="a" style="inset:60px;border:3px solid #C8312B"></div>
  <svg class="a" style="left:92px;top:116px" width="150" height="360" viewBox="0 0 150 360">POLE1</svg>
  <svg class="a" style="right:92px;top:116px;transform:scaleX(-1)" width="150" height="360" viewBox="0 0 150 360">POLE2</svg>
  <div class="a" style="left:0;right:0;top:130px;text-align:center">
    <svg width="360" height="200" viewBox="0 0 360 200">
      <g stroke="#14284B" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">
        <rect x="26" y="118" width="190" height="46" rx="23" fill="#C8312B" transform="rotate(-14 120 140)"/>
        <path d="M200 112L318 60c10-4 22 4 20 14-4 22-40 52-112 66z" fill="#fff"/>
        <path d="M232 112L312 78" fill="none" stroke-width="4"/>
        <circle cx="206" cy="128" r="14" fill="#F2E6C9"/>
        <circle cx="206" cy="128" r="4" fill="#14284B" stroke="none"/></g>
      <g fill="#C8312B" stroke="#14284B" stroke-width="5"><circle cx="58" cy="52" r="11"/><circle cx="318" cy="168" r="11"/></g>
      <g fill="#14284B"><polygon points="120,40 126,56 142,56 129,66 134,82 120,72 106,82 111,66 98,56 114,56"/></g></svg>
    <div style="font-size:84px;letter-spacing:6px;line-height:1;margin-top:-6px">NAVALHA</div>
    <div style="font:700 32px 'Rubik';letter-spacing:9px;margin-top:14px;color:#C8312B">BARBEARIA</div></div>
  <div class="a" style="left:72px;right:72px;top:560px;text-align:center">
    <div style="font-size:158px;line-height:1;color:#C8312B;text-shadow:7px 7px 0 #14284B;letter-spacing:2px">AGENDA</div>
    <div style="font-size:158px;line-height:1.02;color:#14284B;text-shadow:7px 7px 0 #C8312B;letter-spacing:2px;margin-top:6px">ABERTA</div></div>
  <svg class="a" style="left:140px;top:905px" width="800" height="130" viewBox="0 0 800 130">
    <polygon points="0,30 90,30 60,65 90,100 0,100 30,65" fill="#C8312B" stroke="#14284B" stroke-width="6" stroke-linejoin="round"/><polygon points="800,30 710,30 740,65 710,100 800,100 770,65" fill="#C8312B" stroke="#14284B" stroke-width="6" stroke-linejoin="round"/>
    <rect x="80" y="10" width="640" height="110" fill="#14284B"/>
    <text x="400" y="86" text-anchor="middle" font-family="Rye" font-size="40" fill="#F2E6C9" letter-spacing="2">CORTE · BARBA · BIGODE</text></svg>
  <div class="a" style="left:110px;right:110px;bottom:130px;background:#C8312B;color:#F2E6C9;border:8px solid #14284B;box-shadow:10px 10px 0 #14284B;padding:24px 38px;display:flex;justify-content:space-between;align-items:center;font-size:40px;letter-spacing:1px;white-space:nowrap"><span>RESERVE SEU HORÁRIO</span><span>→</span></div>
  <div class="a" style="left:0;right:0;bottom:78px;text-align:center;font:700 28px 'Rubik';letter-spacing:5px;color:#14284B">★ @NAVALHABARBEARIA ★</div>
</div>""".replace("POLE1", POLE_TEMPLATE_A).replace("POLE2", POLE_TEMPLATE_B))

# ---------------------------------------------------------------- 3 · Prato Leve — orgânico ilustrado
LEAF = '<path d="M4 76C4 28 38 4 88 4c0 50-24 84-84 72z" /><path d="M10 70C36 50 56 30 80 10" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>'
D["03-nutricao"] = ("Nutrição", r"""
<div class="p" style="background:#E7F1D8;color:#1F5A33;font-family:'Fredoka',sans-serif">
  <svg class="a" style="inset:0" width="1080" height="1350" viewBox="0 0 1080 1350"><path d="M1080 0v520C960 560 840 480 800 360S720 90 600 0z" fill="#FFD9C2"/><path d="M0 1350V880c120-60 260-20 330 100s190 200 330 370z" fill="#BFDDB0"/><circle cx="930" cy="1130" r="130" fill="#FFE9A8"/><circle cx="130" cy="620" r="70" fill="#FFD9C2"/></svg>
  <svg class="a" style="right:40px;bottom:230px;transform:rotate(18deg)" width="190" height="190" viewBox="0 0 92 80" fill="#5FA66B">LEAF</svg>
  <svg class="a" style="left:-30px;top:800px;transform:rotate(-100deg)" width="240" height="240" viewBox="0 0 92 80" fill="#7DB97A">LEAF</svg>
  <svg class="a" style="right:150px;top:30px;transform:rotate(130deg)" width="150" height="150" viewBox="0 0 92 80" fill="#5FA66B">LEAF</svg>

  <div class="a" style="left:72px;top:78px;display:flex;align-items:center;gap:20px">
    <svg width="90" height="90" viewBox="0 0 90 90"><circle cx="45" cy="45" r="43" fill="#1F5A33"/><g fill="#E7F1D8"><path d="M22 58C22 36 38 24 58 24c0 22-10 38-36 34z"/></g><path d="M26 54C38 46 48 38 56 28" stroke="#1F5A33" stroke-width="2.5" fill="none"/><path d="M60 40v24M54 40v10a6 6 0 0 0 12 0V40" stroke="#E7F1D8" stroke-width="3.2" fill="none" stroke-linecap="round" transform="translate(4 4)"/></svg>
    <div style="font-size:50px;font-weight:700;letter-spacing:-.5px">prato leve</div></div>
  <div class="a" style="right:86px;top:96px;background:#FF7A59;color:#fff;font-weight:600;font-size:34px;padding:12px 32px;border-radius:50px;transform:rotate(4deg)">dica da nutri</div>

  <div class="a" style="left:72px;top:260px"><div style="font-size:196px;font-weight:700;line-height:.92;letter-spacing:-5px">3 trocas</div>
    <div style="font-size:196px;font-weight:700;line-height:.92;letter-spacing:-5px;position:relative;display:inline-block">simples<svg style="position:absolute;left:0;bottom:-16px" width="660" height="34" viewBox="0 0 660 34"><path d="M4 18c40-24 80 24 120 0s80-24 120 0 80 24 120 0 80-24 120 0 80 24 120 0" stroke="#FF7A59" stroke-width="9" fill="none" stroke-linecap="round"/></svg></div></div>
  <div class="a" style="right:56px;top:468px;width:190px;height:190px;border-radius:50%;background:#FFE9A8;border:4px dashed #1F5A33;display:flex;align-items:center;justify-content:center;text-align:center;transform:rotate(10deg);font:700 48px 'Caveat';line-height:1;color:#1F5A33">sem<br>sofrer!</div>

  <div class="a" style="left:72px;right:72px;top:690px;display:flex;flex-direction:column;gap:26px">
    <div style="background:#fff;border:5px solid #1F5A33;border-radius:70px;box-shadow:10px 10px 0 #1F5A33;display:flex;align-items:center;gap:30px;padding:20px 44px 20px 24px"><svg width="104" height="104" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#FFD9C2"/><path d="M32 22c-8-8-20-2-18 12 1 12 10 22 18 18 8 4 17-6 18-18 2-14-10-20-18-12z" fill="#E8553E"/><path d="M32 22c0-6 3-10 8-12" stroke="#1F5A33" stroke-width="3.5" fill="none" stroke-linecap="round"/><path d="M34 14c6-4 12 0 12 4-6 2-11 0-12-4z" fill="#5FA66B"/></svg><div><div style="font-size:60px;font-weight:600;line-height:1">Fruta inteira</div><div style="font:700 44px 'Caveat';color:#FF7A59;line-height:1">no lugar do suco</div></div></div>
    <div style="background:#fff;border:5px solid #1F5A33;border-radius:70px;box-shadow:10px 10px 0 #1F5A33;display:flex;align-items:center;gap:30px;padding:20px 44px 20px 24px"><svg width="104" height="104" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#FFE9A8"/><path d="M12 38c-2-12 8-20 20-20s22 8 20 20c0 6-4 8-8 8H20c-4 0-8-2-8-8z" fill="#C98A4B"/><path d="M22 26l5 8M32 24l5 8M42 26l5 8" stroke="#F4D7A8" stroke-width="3.5" stroke-linecap="round"/></svg><div><div style="font-size:60px;font-weight:600;line-height:1">Pão integral</div><div style="font:700 44px 'Caveat';color:#FF7A59;line-height:1">no lugar do branco</div></div></div>
    <div style="background:#fff;border:5px solid #1F5A33;border-radius:70px;box-shadow:10px 10px 0 #1F5A33;display:flex;align-items:center;gap:30px;padding:20px 44px 20px 24px"><svg width="104" height="104" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#BFDDB0"/><rect x="10" y="16" width="44" height="34" rx="6" fill="#1F5A33"/><rect x="16" y="24" width="32" height="20" rx="4" fill="#FFD9C2"/><circle cx="18" cy="20" r="2" fill="#E7F1D8"/><circle cx="26" cy="20" r="2" fill="#E7F1D8"/><path d="M24 40q4-8 8 0t8 0" stroke="#E8553E" stroke-width="3" fill="none" stroke-linecap="round"/></svg><div><div style="font-size:60px;font-weight:600;line-height:1">Forno</div><div style="font:700 44px 'Caveat';color:#FF7A59;line-height:1">no lugar da fritura</div></div></div>
  </div>
  <div class="a" style="left:72px;right:72px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-size:36px;font-weight:600">
    <span style="display:flex;align-items:center;gap:14px"><svg width="34" height="44" viewBox="0 0 34 44"><path d="M4 2h26v40l-13-10L4 42z" fill="#FF7A59"/></svg>Salve para consultar depois</span><span style="color:#FF7A59">@pratoleve</span></div>
</div>""".replace("LEAF", LEAF))

# ---------------------------------------------------------------- 4 · Linha — neobrutalismo pop
STAR = "".join(f"{540+ (330 if i%2==0 else 250)*__import__('math').cos(i*3.14159/12):.0f},{540+(330 if i%2==0 else 250)*__import__('math').sin(i*3.14159/12):.0f} " for i in range(24))
D["04-moda"] = ("Loja de roupas", r"""
<div class="p" style="background:#BBA6FF;color:#111;font-family:'Rubik',sans-serif">
  <div class="a" style="left:0;right:0;top:0;height:86px;background:repeating-conic-gradient(#111 0 25%,#FFE45E 0 50%) 0 0/86px 86px;border-bottom:7px solid #111"></div>
  <div class="a" style="left:0;right:0;bottom:0;height:86px;background:repeating-conic-gradient(#111 0 25%,#FFE45E 0 50%) 0 0/86px 86px;border-top:7px solid #111"></div>
  <svg class="a" style="left:60px;top:150px" width="940" height="1000" viewBox="0 0 940 1000" fill="none" stroke="#111" stroke-width="7" stroke-linecap="round"><path d="M30 480c40-40 80 40 120 0s80 40 120 0" /><path d="M690 940c40-40 80 40 120 0s80 40 120 0"/><path d="M40 60l30 30m0-30L40 90M880 330l30 30m0-30l-30 30M60 930l30 30m0-30l-30 30"/></svg>

  <div class="a" style="left:72px;top:150px;display:flex;align-items:center;gap:20px">
    <div style="width:104px;height:104px;border-radius:50%;background:#FFE45E;border:7px solid #111;box-shadow:7px 7px 0 #111;display:flex;align-items:center;justify-content:center"><svg width="62" height="62" viewBox="0 0 64 64" fill="none" stroke="#111" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18a7 7 0 1 1 7 7c-4 1-7 4-7 8v4L6 54h52L32 37"/></svg></div>
    <div style="font:800 62px 'Rubik';letter-spacing:-2px">linha.</div></div>

  <svg class="a" style="right:30px;top:120px;transform:rotate(14deg)" width="290" height="290" viewBox="0 0 1080 1080"><polygon points="STAR" fill="#FF5C8A" stroke="#111" stroke-width="22" stroke-linejoin="round"/><text x="540" y="590" text-anchor="middle" font-family="Bowlby One SC" font-size="230" fill="#fff" stroke="#111" stroke-width="14" paint-order="stroke">NOVA!</text></svg>

  <div class="a" style="left:72px;top:380px;background:#fff;border:10px solid #111;box-shadow:20px 20px 0 #111;padding:20px 54px 8px;transform:rotate(-3deg)"><div style="font:400 250px 'Bowlby One SC';line-height:1.0;letter-spacing:-6px">NOVA</div></div>
  <div class="a" style="left:96px;top:760px;background:#FFE45E;border:10px solid #111;box-shadow:20px 20px 0 #111;padding:14px 40px 4px;transform:rotate(2.5deg)"><div style="font:400 142px 'Bowlby One SC';line-height:1.0;letter-spacing:-4px">COLEÇÃO</div></div>

  <div class="a" style="left:72px;top:1010px;display:flex;gap:20px;align-items:center">
    <div style="background:#2BD99F;border:7px solid #111;box-shadow:9px 9px 0 #111;border-radius:60px;padding:14px 32px;font:800 38px 'Rubik'">peças limitadas</div>
    <div style="background:#fff;border:7px solid #111;box-shadow:9px 9px 0 #111;border-radius:60px;padding:14px 32px;font:800 38px 'Rubik'">outono/inverno</div></div>
  <div class="a" style="right:72px;bottom:104px;background:#111;color:#fff;border:7px solid #111;box-shadow:12px 12px 0 #FF5C8A;border-radius:24px;padding:26px 48px;font:800 56px 'Rubik'">Chegou na loja →</div>
</div>""".replace("STAR", STAR))

# ---------------------------------------------------------------- 5 · Treino 40 — esportivo urbano
D["05-personal"] = ("Personal trainer", r"""
<div class="p" style="background:#0B0B0B;color:#fff;font-family:'Barlow Condensed',sans-serif">
  <div class="a" style="right:0;top:0;width:700px;height:760px;background:radial-gradient(circle,#D7FF3A 3.5px,transparent 4px) 0 0/26px 26px;-webkit-mask-image:linear-gradient(225deg,#000 0,transparent 70%);opacity:.55"></div>
  <div class="a" style="left:-120px;top:800px;width:1400px;height:300px;background:#D7FF3A;transform:rotate(-8deg)"></div>
  <div class="a" style="left:0;right:0;bottom:0;height:60px;background:repeating-linear-gradient(135deg,#D7FF3A 0 30px,#0B0B0B 30px 60px)"></div>

  <div class="a" style="left:72px;top:72px;display:flex;align-items:center;gap:22px">
    <div style="width:92px;height:92px;background:#D7FF3A;transform:skewX(-10deg);display:flex;align-items:center;justify-content:center"><svg width="58" height="58" viewBox="0 0 64 64" fill="#0B0B0B"><polygon points="38,2 12,36 28,36 22,62 52,24 34,24"/></svg></div>
    <div style="font:400 72px 'Anton';letter-spacing:3px">TREINO <span style="color:#D7FF3A">40</span></div></div>
  <svg class="a" style="right:72px;top:70px" width="190" height="100" viewBox="0 0 190 100" fill="#D7FF3A"><rect x="0" y="30" width="20" height="40" rx="5"/><rect x="24" y="14" width="22" height="72" rx="6"/><rect x="50" y="42" width="90" height="16" rx="5"/><rect x="144" y="14" width="22" height="72" rx="6"/><rect x="170" y="30" width="20" height="40" rx="5"/></svg>

  <div class="a" style="left:72px;top:310px;font-family:'Anton';font-style:italic;transform:skewX(-8deg);line-height:.92">
    <div style="font-size:200px;color:#fff;letter-spacing:2px">ANTES DE</div>
    <div style="font-size:240px;color:#D7FF3A;letter-spacing:2px;text-shadow:10px 10px 0 #0B0B0B">TREINAR.</div></div>

  <div class="a" style="left:96px;right:60px;top:918px;display:flex;flex-direction:column;gap:12px;font-style:italic">
    <div style="background:#0B0B0B;border:5px solid #D7FF3A;transform:skewX(-8deg);padding:12px 32px;display:flex;align-items:center;gap:28px;font-weight:800;font-size:60px;letter-spacing:2px"><span style="width:54px;height:54px;background:#D7FF3A;color:#0B0B0B;display:flex;align-items:center;justify-content:center"><svg width="42" height="42" viewBox="0 0 40 40" fill="none" stroke="#0B0B0B" stroke-width="7" stroke-linecap="square"><path d="M6 21l9 9 19-21"/></svg></span>HIDRATAÇÃO EM DIA</div>
    <div style="background:#0B0B0B;border:5px solid #D7FF3A;transform:skewX(-8deg);padding:12px 32px;display:flex;align-items:center;gap:28px;font-weight:800;font-size:60px;letter-spacing:2px"><span style="width:54px;height:54px;background:#D7FF3A;color:#0B0B0B;display:flex;align-items:center;justify-content:center"><svg width="42" height="42" viewBox="0 0 40 40" fill="none" stroke="#0B0B0B" stroke-width="7" stroke-linecap="square"><path d="M6 21l9 9 19-21"/></svg></span>AQUECIMENTO 5 MIN</div>
    <div style="background:#0B0B0B;border:5px solid #D7FF3A;transform:skewX(-8deg);padding:12px 32px;display:flex;align-items:center;gap:28px;font-weight:800;font-size:60px;letter-spacing:2px"><span style="width:54px;height:54px;background:#D7FF3A;color:#0B0B0B;display:flex;align-items:center;justify-content:center"><svg width="42" height="42" viewBox="0 0 40 40" fill="none" stroke="#0B0B0B" stroke-width="7" stroke-linecap="square"><path d="M6 21l9 9 19-21"/></svg></span>META DO DIA DEFINIDA</div>
  </div>
  <div class="a" style="right:80px;top:190px;font:400 38px 'Anton';letter-spacing:4px;color:#D7FF3A">@TREINO40</div>
</div>""")

# ---------------------------------------------------------------- 6 · Patinha — kawaii adesivo
D["06-petshop"] = ("Pet shop", r"""
<div class="p" style="background:#79C7FF;color:#fff;font-family:'Fredoka',sans-serif">
  <svg class="a" style="inset:0" width="1080" height="1350" viewBox="0 0 1080 1350"><g fill="#fff" opacity=".9"><circle cx="560" cy="130" r="40"/><circle cx="610" cy="108" r="52"/><circle cx="665" cy="132" r="38"/><rect x="560" y="130" width="105" height="40"/><circle cx="820" cy="1060" r="55"/><circle cx="880" cy="1030" r="70"/><circle cx="950" cy="1062" r="52"/><rect x="820" y="1060" width="130" height="52"/></g>
    <g fill="none" stroke="#fff" stroke-width="5" opacity=".9"><circle cx="90" cy="650" r="34"/><circle cx="140" cy="720" r="18"/><circle cx="990" cy="560" r="44"/><circle cx="930" cy="640" r="20"/><circle cx="60" cy="1100" r="26"/></g>
    <g fill="#FFD23F" stroke="#fff" stroke-width="5" stroke-linejoin="round"><polygon points="900,150 915,190 958,190 923,214 936,255 900,230 864,255 877,214 842,190 885,190"/><polygon points="120,900 130,926 158,926 136,942 144,968 120,952 96,968 104,942 82,926 110,926"/></g></svg>

  <div class="a" style="left:72px;top:72px;display:flex;align-items:center;gap:20px">
    <div style="width:104px;height:104px;border-radius:50%;background:#FFD23F;border:8px solid #fff;box-shadow:0 8px 0 #1F4FFF;display:flex;align-items:center;justify-content:center"><svg width="62" height="62" viewBox="0 0 64 64" fill="#1F4FFF"><ellipse cx="32" cy="42" rx="14" ry="11"/><ellipse cx="14" cy="28" rx="6" ry="8" transform="rotate(-20 14 28)"/><ellipse cx="25" cy="16" rx="6" ry="8" transform="rotate(-6 25 16)"/><ellipse cx="39" cy="16" rx="6" ry="8" transform="rotate(6 39 16)"/><ellipse cx="50" cy="28" rx="6" ry="8" transform="rotate(20 50 28)"/></svg></div>
    <div style="line-height:1"><div style="font:700 62px 'Fredoka';color:#1F4FFF">patinha</div><div style="font:600 30px 'Fredoka';color:#fff;letter-spacing:5px;margin-top:2px">PET SHOP</div></div></div>

  <svg class="a" style="right:50px;top:200px;transform:rotate(14deg)" width="300" height="300" viewBox="0 0 64 64"><g fill="#FFD23F" stroke="#fff" stroke-width="7" stroke-linejoin="round" paint-order="stroke"><ellipse cx="32" cy="42" rx="15" ry="12"/><ellipse cx="13" cy="28" rx="6.5" ry="8.5" transform="rotate(-20 13 28)"/><ellipse cx="24" cy="15" rx="6.5" ry="8.5" transform="rotate(-6 24 15)"/><ellipse cx="40" cy="15" rx="6.5" ry="8.5" transform="rotate(6 40 15)"/><ellipse cx="51" cy="28" rx="6.5" ry="8.5" transform="rotate(20 51 28)"/></g></svg>

  <div class="a" style="left:60px;top:370px;font-family:'Chewy';line-height:.86;transform:rotate(-4deg)">
    <div style="font-size:290px;color:#fff;-webkit-text-stroke:16px #1F4FFF;paint-order:stroke fill;text-shadow:0 14px 0 #1F4FFF">Banho</div>
    <div style="font-size:220px;color:#FFD23F;-webkit-text-stroke:16px #1F4FFF;paint-order:stroke fill;text-shadow:0 14px 0 #1F4FFF;margin-left:90px;margin-top:18px">e tosa</div></div>

  <svg class="a" style="left:80px;top:950px;transform:rotate(-24deg)" width="170" height="80" viewBox="0 0 170 80"><g fill="#fff" stroke="#1F4FFF" stroke-width="6" stroke-linejoin="round"><rect x="26" y="26" width="118" height="28" rx="14"/><circle cx="26" cy="24" r="16"/><circle cx="26" cy="56" r="16"/><circle cx="144" cy="24" r="16"/><circle cx="144" cy="56" r="16"/></g><rect x="30" y="30" width="110" height="20" fill="#fff"/></svg>
  <svg class="a" style="right:110px;top:950px;transform:rotate(-12deg)" width="110" height="100" viewBox="0 0 64 60"><path d="M32 56C8 38 8 14 24 12c7-1 8 5 8 8 0-3 1-9 8-8 16 2 16 26-8 44z" fill="#FF5C8A" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke"/></svg>

  <div class="a" style="left:72px;right:72px;bottom:70px;background:#fff;color:#1F4FFF;border:8px dashed #1F4FFF;border-radius:70px;padding:34px 44px;box-shadow:0 12px 0 #1F4FFF;display:flex;align-items:center;justify-content:space-between;gap:30px">
    <div style="font-size:48px;font-weight:600;line-height:1.1">Agende hoje e deixe seu pet <span style="background:#FFD23F;padding:0 12px;border-radius:14px">cheirosinho!</span></div>
    <div style="background:#1F4FFF;color:#fff;border-radius:50px;padding:24px 38px;font-size:44px;font-weight:700;white-space:nowrap;box-shadow:0 8px 0 #0A2FB5">Agendar →</div></div>
</div>""")


def renderizar(html, png):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=14000", f"--screenshot={png}", pathlib.Path(html).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def main():
    for nome, (rotulo, corpo) in D.items():
        h = AQUI / f"{nome}.html"
        h.write_text(f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{rotulo}</title><style>{BASE}</style></head><body>{corpo}</body></html>", encoding="utf-8")
        renderizar(h, AQUI / f"{nome}.png")
        print("ok", nome)
    tiles = "".join(f"<figure><img src='{n}.png'><figcaption><b>{i+1:02d}</b> {r}</figcaption></figure>" for i, (n, (r, _)) in enumerate(D.items()))
    f = AQUI / "folha.html"
    f.write_text("<!doctype html><html><head><meta charset='utf-8'><style>*{margin:0;padding:0;box-sizing:border-box}body{width:2000px;background:#EDE9DF;font-family:sans-serif;padding:40px}"
                 ".g{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}figure img{width:100%;display:block;border-radius:16px;box-shadow:0 14px 30px -14px rgba(0,0,0,.5)}"
                 "figcaption{margin-top:10px;font-size:26px;font-weight:600}</style></head><body><div class='g'>" + tiles + "</div></body></html>", encoding="utf-8")
    renderizar_folha(f)


def renderizar_folha(f):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=2000,1920", "--virtual-time-budget=6000", f"--screenshot={AQUI / 'folha.png'}", pathlib.Path(f).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    print("ok folha")


if __name__ == "__main__":
    main()
