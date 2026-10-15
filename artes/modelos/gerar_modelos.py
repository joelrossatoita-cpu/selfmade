"""Gera 8 modelos de post (1080x1350) para negócios diferentes e uma folha comparativa.
Uso: python gerar_modelos.py
Cada modelo mostra o tipo de arte que o sistema da selfmade. ajuda um pequeno negócio a produzir.
Os negócios, nomes e textos são fictícios e servem só como exemplo de design."""
import os, subprocess, pathlib, sys

AQUI = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600"
         "&family=Archivo+Black&family=Poppins:wght@400;500;600;700"
         "&family=Inter+Tight:wght@400;500;600"
         "&family=Space+Grotesk:wght@400;500;700"
         "&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&display=swap');")

BASE = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
.p{position:relative;width:1080px;height:1350px;overflow:hidden;padding:72px}
.abs{position:absolute}
"""

MODELOS = {}

# 1 — cafeteria: círculo de destaque
MODELOS["01-cafeteria"] = ("Cafeteria · promoção do dia", """
<div class="p" style="background:#F4E9DA;color:#3B2314;font-family:'Fraunces',serif">
  <div style="display:flex;justify-content:space-between;align-items:baseline;font-size:44px;font-style:italic">
    <span>brasa café</span><span style="font:500 30px 'Inter Tight';letter-spacing:.04em">07h — 10h</span></div>
  <div class="abs" style="left:-120px;top:230px;width:900px;height:900px;border-radius:50%;border:2px solid #3B2314;opacity:.25"></div>
  <div class="abs" style="left:150px;top:300px;width:780px;height:780px;border-radius:50%;background:#D9531E;color:#F4E9DA;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
    <div style="font:600 30px 'Inter Tight';letter-spacing:.14em;text-transform:uppercase">Hoje</div>
    <div style="font-size:150px;font-weight:600;line-height:.95;letter-spacing:-.03em;margin-top:18px">Combo<br>da manhã</div>
    <div style="font:400 44px 'Inter Tight';margin-top:30px">café + pão de queijo</div>
  </div>
  <div class="abs" style="left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;font:500 32px 'Inter Tight';border-top:2px solid #3B2314;padding-top:28px">
    <span>Rua das Flores, 120</span><span>→</span></div>
</div>""")

# 2 — barbearia: tipografia pesada e moldura
MODELOS["02-barbearia"] = ("Barbearia · agenda aberta", """
<div class="p" style="background:#0E0E0E;color:#F2E8CF;font-family:'Archivo Black',sans-serif">
  <div class="abs" style="inset:40px;border:3px solid #C9A24B"></div>
  <div class="abs" style="inset:56px;border:1px solid #C9A24B;opacity:.6"></div>
  <div style="position:relative;padding:40px 24px;display:flex;flex-direction:column;height:100%">
    <div style="display:flex;justify-content:space-between;font:500 30px 'Inter Tight';letter-spacing:.2em;color:#C9A24B"><span>NAVALHA</span><span>BARBEARIA</span></div>
    <div style="margin-top:70px;font-size:196px;line-height:.9;letter-spacing:-.02em">AGENDA<br><span style="color:#C9A24B">ABERTA</span></div>
    <div style="font:400 50px 'Inter Tight';margin-top:46px;line-height:1.2;max-width:760px">Ainda tem horário esta semana. Corte, barba ou os dois.</div>
    <div style="margin-top:auto;display:inline-block;align-self:flex-start;background:#C9A24B;color:#0E0E0E;font:700 40px 'Inter Tight';padding:30px 48px">Chame no WhatsApp →</div>
  </div>
</div>""")

# 3 — nutrição: lista amigável
MODELOS["03-nutricao"] = ("Nutrição · dica em lista", """
<div class="p" style="background:#DFF0E3;color:#17402A;font-family:'Poppins',sans-serif">
  <div style="display:flex;justify-content:space-between;font:600 32px 'Poppins'"><span>prato leve</span><span style="color:#FF7A59">dica</span></div>
  <div style="margin-top:60px;font-size:128px;font-weight:700;line-height:.98;letter-spacing:-.035em">3 trocas<br>simples<span style="color:#FF7A59">.</span></div>
  <div style="margin-top:56px;display:flex;flex-direction:column;gap:22px">
    <div style="background:#fff;border-radius:60px;padding:30px 44px;display:flex;align-items:center;gap:30px;font:500 44px 'Poppins'"><b style="background:#FF7A59;color:#fff;border-radius:50%;width:76px;height:76px;display:flex;align-items:center;justify-content:center;font-size:38px">1</b>Suco por fruta inteira</div>
    <div style="background:#fff;border-radius:60px;padding:30px 44px;display:flex;align-items:center;gap:30px;font:500 44px 'Poppins'"><b style="background:#FF7A59;color:#fff;border-radius:50%;width:76px;height:76px;display:flex;align-items:center;justify-content:center;font-size:38px">2</b>Pão branco por integral</div>
    <div style="background:#fff;border-radius:60px;padding:30px 44px;display:flex;align-items:center;gap:30px;font:500 44px 'Poppins'"><b style="background:#FF7A59;color:#fff;border-radius:50%;width:76px;height:76px;display:flex;align-items:center;justify-content:center;font-size:38px">3</b>Fritura por forno</div>
  </div>
  <div class="abs" style="left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;font:500 32px 'Poppins'"><span>Salve para consultar depois</span><span>→</span></div>
</div>""")

# 4 — moda: pôster suíço com blocos
MODELOS["04-moda"] = ("Loja de roupas · lançamento", """
<div class="p" style="background:#FAFAFA;color:#111;font-family:'Inter Tight',sans-serif">
  <div class="abs" style="right:0;top:0;width:470px;height:620px;background:#FF3B1F"></div>
  <div class="abs" style="right:110px;top:150px;width:250px;height:250px;border-radius:50%;background:#111"></div>
  <div style="position:relative;display:flex;justify-content:space-between;font:500 32px 'Inter Tight'"><span style="font-weight:600;letter-spacing:-.03em;font-size:42px">linha.</span></div>
  <div style="position:relative;margin-top:300px;font-size:210px;font-weight:600;letter-spacing:-.06em;line-height:.86">Nova<br>coleção</div>
  <div class="abs" style="left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;align-items:flex-end;border-top:3px solid #111;padding-top:28px">
    <div style="font:500 40px 'Inter Tight';line-height:1.2">Chegou na loja.<br><span style="opacity:.6">Peças limitadas.</span></div><div style="font-size:90px;line-height:1">→</div></div>
</div>""")

# 5 — pilates: citação serifada
MODELOS["05-pilates"] = ("Estúdio de pilates · frase", """
<div class="p" style="background:#E9E4F5;color:#2A2350;font-family:'Fraunces',serif">
  <div class="abs" style="right:-260px;top:-260px;width:760px;height:760px;border-radius:50%;background:#7B61FF;opacity:.9"></div>
  <div class="abs" style="right:-120px;top:-120px;width:480px;height:480px;border-radius:50%;background:#E9E4F5"></div>
  <div style="position:relative;font:italic 400 44px 'Fraunces'">eixo</div>
  <div style="position:relative;margin-top:420px;font-size:108px;font-weight:600;line-height:1.02;letter-spacing:-.025em">Movimento é a forma mais gentil de cuidar de si<span style="color:#7B61FF">.</span></div>
  <div class="abs" style="left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;font:500 32px 'Inter Tight';border-top:2px solid #2A2350;padding-top:28px"><span>Estúdio de pilates</span><span>Aulas em grupo e individuais</span></div>
</div>""")

# 6 — confeitaria: produto em destaque
MODELOS["06-confeitaria"] = ("Confeitaria · produto em destaque", """
<div class="p" style="background:#FBD9DF;color:#5A1630;font-family:'Fraunces',serif">
  <div style="display:flex;justify-content:space-between;font:italic 400 44px 'Fraunces'"><span>doce ofício</span><span style="font:600 28px 'Inter Tight';letter-spacing:.12em">ENCOMENDAS</span></div>
  <div class="abs" style="left:190px;top:260px;width:700px;height:700px;border-radius:50%;background:#5A1630"></div>
  <div class="abs" style="left:250px;top:320px;width:580px;height:580px;border-radius:50%;background:#F5B7C3"></div>
  <div class="abs" style="left:330px;top:400px;width:420px;height:420px;border-radius:50%;background:#FBD9DF;display:flex;align-items:center;justify-content:center;text-align:center;font-size:62px;font-weight:600;line-height:1;color:#5A1630">bolo de<br>cenoura</div>
  <div class="abs" style="left:790px;top:230px;width:180px;height:180px;border-radius:50%;background:#FF9F43;color:#5A1630;display:flex;align-items:center;justify-content:center;text-align:center;font:700 32px 'Inter Tight';line-height:1.1;transform:rotate(12deg)">cobertura<br>de chocolate</div>
  <div style="position:absolute;left:72px;right:72px;bottom:72px">
    <div style="font-size:92px;font-weight:600;line-height:1;letter-spacing:-.02em">Feito sob encomenda.</div>
    <div style="font:500 38px 'Inter Tight';margin-top:18px;display:flex;justify-content:space-between"><span>Peça com 2 dias de antecedência</span><span>→</span></div></div>
</div>""")

# 7 — personal: checklist enérgico
MODELOS["07-personal"] = ("Personal trainer · checklist", """
<div class="p" style="background:#E8FF3A;color:#0B0B0B;font-family:'Space Grotesk',sans-serif">
  <div class="abs" style="left:-200px;top:520px;width:1500px;height:150px;background:#0B0B0B;transform:rotate(-8deg);opacity:.08"></div>
  <div style="display:flex;justify-content:space-between;font:700 34px 'Space Grotesk'"><span>TREINO 40</span><span>CHECKLIST</span></div>
  <div style="margin-top:50px;font-size:150px;font-weight:700;line-height:.9;letter-spacing:-.05em">Antes de<br>treinar.</div>
  <div style="margin-top:56px;border-top:4px solid #0B0B0B">
    <div style="display:flex;align-items:center;gap:36px;padding:30px 0;border-bottom:4px solid #0B0B0B;font:500 54px 'Space Grotesk'"><span style="width:64px;height:64px;background:#0B0B0B;color:#E8FF3A;display:flex;align-items:center;justify-content:center;font-size:44px">✓</span>Hidratação em dia</div>
    <div style="display:flex;align-items:center;gap:36px;padding:30px 0;border-bottom:4px solid #0B0B0B;font:500 54px 'Space Grotesk'"><span style="width:64px;height:64px;background:#0B0B0B;color:#E8FF3A;display:flex;align-items:center;justify-content:center;font-size:44px">✓</span>Aquecimento de 5 minutos</div>
    <div style="display:flex;align-items:center;gap:36px;padding:30px 0;border-bottom:4px solid #0B0B0B;font:500 54px 'Space Grotesk'"><span style="width:64px;height:64px;background:#0B0B0B;color:#E8FF3A;display:flex;align-items:center;justify-content:center;font-size:44px">✓</span>Meta do dia definida</div>
  </div>
  <div class="abs" style="left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;font:700 34px 'Space Grotesk'"><span>Treino começa aqui</span><span>→</span></div>
</div>""")

# 8 — pet shop: aviso com forma gráfica
MODELOS["08-petshop"] = ("Pet shop · aviso de serviço", """
<div class="p" style="background:#1F4FFF;color:#fff;font-family:'Bricolage Grotesque',sans-serif">
  <div style="display:flex;justify-content:space-between;font:800 40px 'Bricolage Grotesque'"><span>patinha</span><span style="background:#FFD23F;color:#1F4FFF;padding:6px 22px;border-radius:40px;font-size:30px">pet shop</span></div>
  <div class="abs" style="left:620px;top:330px;width:360px;height:260px;border-radius:50%;background:#FFD23F;transform:rotate(-10deg)"></div>
  <div class="abs" style="left:560px;top:190px;width:130px;height:170px;border-radius:50%;background:#FFD23F;transform:rotate(-30deg)"></div>
  <div class="abs" style="left:705px;top:130px;width:130px;height:170px;border-radius:50%;background:#FFD23F;transform:rotate(-8deg)"></div>
  <div class="abs" style="left:850px;top:170px;width:130px;height:170px;border-radius:50%;background:#FFD23F;transform:rotate(18deg)"></div>
  <div class="abs" style="left:955px;top:310px;width:110px;height:150px;border-radius:50%;background:#FFD23F;transform:rotate(40deg)"></div>
  <div style="position:absolute;left:72px;top:640px;font-size:176px;font-weight:800;line-height:.92;letter-spacing:-.045em">Banho<br>e tosa</div>
  <div style="position:absolute;left:72px;right:72px;bottom:72px">
    <div style="font:500 48px 'Bricolage Grotesque';line-height:1.2;max-width:800px">Agende hoje e deixe o seu pet pronto para o fim de semana.</div>
    <div style="margin-top:36px;display:inline-block;background:#FFD23F;color:#1F4FFF;font:800 40px 'Bricolage Grotesque';padding:26px 44px;border-radius:70px">Agendar agora →</div></div>
</div>""")


def renderizar(html_path, png_path, w, h):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=12000",
                    f"--screenshot={png_path}", pathlib.Path(html_path).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def main():
    for nome, (rotulo, corpo) in MODELOS.items():
        html = AQUI / f"{nome}.html"
        html.write_text(f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{rotulo}</title><style>{BASE}</style></head><body>{corpo}</body></html>", encoding="utf-8")
        renderizar(html, AQUI / f"{nome}.png", 1080, 1350)
        print("ok", nome)
    # folha comparativa
    tiles = "".join(
        f"<figure><img src='{n}.png'><figcaption><b>{i+1:02d}</b> {r}</figcaption></figure>"
        for i, (n, (r, _)) in enumerate(MODELOS.items()))
    folha = ("<!doctype html><html><head><meta charset='utf-8'><style>"
             "@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&display=swap');"
             "*{margin:0;padding:0;box-sizing:border-box}body{width:2000px;background:#EDE9DF;font-family:'Inter Tight',sans-serif;padding:48px}"
             "h1{font-size:44px;font-weight:600;letter-spacing:-.03em;margin-bottom:6px}p{font-size:24px;color:#4a574f;margin-bottom:36px}"
             ".g{display:grid;grid-template-columns:repeat(4,1fr);gap:36px 32px}figure img{width:100%;display:block;box-shadow:0 18px 40px -20px rgba(19,36,28,.5)}"
             "figcaption{margin-top:14px;font-size:24px;font-weight:500;color:#13241C}figcaption b{color:#1E6B47;margin-right:8px}"
             "</style></head><body><h1>Modelos de design para Instagram</h1><p>Exemplos fictícios do tipo de arte que o sistema ajuda cada negócio a produzir.</p>"
             f"<div class='g'>{tiles}</div></body></html>")
    f = AQUI / "folha.html"
    f.write_text(folha, encoding="utf-8")
    renderizar(f, AQUI / "folha.png", 2000, 1500)
    print("ok folha")


if __name__ == "__main__":
    main()
