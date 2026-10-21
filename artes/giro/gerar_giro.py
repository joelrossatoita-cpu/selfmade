"""Gera 8 artes (1080x1350) para o giro 3D da página inicial, cada uma em um estilo gráfico diferente
e sempre na paleta verde da selfmade. Uso: python gerar_giro.py
Os negócios, nomes e textos são fictícios e servem só como exemplo de design."""
import os, subprocess, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Archivo+Black&family=Josefin+Sans:wght@400;700"
         "&family=Bangers&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,800&family=Press+Start+2P&family=Orbitron:wght@500;900"
         "&family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter+Tight:wght@400;500;700&family=Special+Elite&display=swap');")
BASE = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
.p{position:relative;width:1080px;height:1350px;overflow:hidden}
.abs{position:absolute}
"""
A = {}

# 1 — brutalismo: bordas grossas, sombra dura, mono
A["01-brutalismo"] = ("Brutalismo · feira orgânica", """
<div class="p" style="background:#E4F5D0;font-family:'Space Mono',monospace;color:#0B1F14;padding:60px">
  <div style="border:8px solid #0B1F14;background:#fff;padding:22px 30px;display:flex;justify-content:space-between;font-weight:700;font-size:34px;box-shadow:14px 14px 0 #0B1F14"><span>HORTA BRUTA</span><span>SÁB 7H</span></div>
  <div style="margin-top:56px;border:8px solid #0B1F14;background:#2FA866;padding:44px 40px;box-shadow:18px 18px 0 #0B1F14;transform:rotate(-1.5deg)">
    <div style="font:400 138px/.9 'Archivo Black';letter-spacing:-.04em;color:#0B1F14">FEIRA<br>SEM<br>FRESCURA.</div></div>
  <div style="margin-top:56px;display:flex;gap:28px">
    <div style="flex:1;border:8px solid #0B1F14;background:#B8F2C9;padding:26px;font-weight:700;font-size:38px;line-height:1.2;box-shadow:12px 12px 0 #0B1F14">Alface<br>R$ 4,00</div>
    <div style="flex:1;border:8px solid #0B1F14;background:#fff;padding:26px;font-weight:700;font-size:38px;line-height:1.2;box-shadow:12px 12px 0 #0B1F14">Cesta<br>R$ 35,00</div></div>
  <div class="abs" style="left:60px;right:60px;bottom:60px;background:#0B1F14;color:#B8F2C9;font-weight:700;font-size:36px;padding:26px 32px">RESERVE PELO WHATSAPP →</div>
</div>""")

# 2 — bauhaus: formas geométricas primárias, em verdes
A["02-bauhaus"] = ("Bauhaus · ateliê de cerâmica", """
<div class="p" style="background:#EFE9D6;font-family:'Josefin Sans',sans-serif;color:#0F3B26">
  <div class="abs" style="left:-90px;top:-90px;width:640px;height:640px;border-radius:50%;background:#1E6B47"></div>
  <div class="abs" style="right:70px;top:120px;width:380px;height:380px;background:#7FD1A1"></div>
  <div class="abs" style="right:60px;top:600px;width:0;height:0;border-left:170px solid transparent;border-right:170px solid transparent;border-bottom:300px solid #0F3B26;transform:rotate(12deg)"></div>
  <div class="abs" style="left:90px;top:560px;width:560px;height:30px;background:#0F3B26"></div>
  <div class="abs" style="left:90px;top:80px;color:#EFE9D6;font-weight:700;font-size:36px;letter-spacing:.2em">ATELIÊ BARRO</div>
  <div class="abs" style="left:90px;top:640px;font-weight:700;font-size:190px;line-height:.85;letter-spacing:-.03em;text-transform:uppercase">Forma<br>& uso</div>
  <div class="abs" style="left:90px;bottom:90px;font-size:44px;line-height:1.3">Curso de cerâmica · turma de sábado<br><b>Vagas abertas</b></div>
  <div class="abs" style="right:90px;bottom:90px;width:120px;height:120px;border-radius:50%;background:#2FA866"></div>
</div>""")

# 3 — pop art: pontos de retícula, contorno grosso, explosão
A["03-pop-art"] = ("Pop art · sucos", """
<div class="p" style="background:#C6F135;font-family:'Bangers',cursive;color:#0B2A1B">
  <div class="abs" style="inset:0;background-image:radial-gradient(#2FA866 9px,transparent 10px);background-size:44px 44px;opacity:.55"></div>
  <div class="abs" style="left:90px;top:110px;width:900px;height:760px;background:#fff;filter:drop-shadow(0 0 0 #0B2A1B);clip-path:polygon(50% 0,60% 12%,78% 3%,80% 20%,98% 22%,90% 38%,100% 52%,84% 60%,90% 80%,72% 78%,62% 98%,50% 84%,36% 100%,30% 80%,10% 84%,16% 62%,0 50%,14% 38%,6% 20%,26% 20%,30% 4%,42% 14%)"></div>
  <div class="abs" style="left:90px;top:230px;width:900px;text-align:center;font-size:250px;line-height:.85;color:#1E6B47;-webkit-text-stroke:8px #0B2A1B;text-shadow:12px 12px 0 #0B2A1B">POW!</div>
  <div class="abs" style="left:90px;top:590px;width:900px;text-align:center;font-size:96px;color:#0B2A1B">SUCO VERDE NA HORA</div>
  <div class="abs" style="left:70px;right:70px;bottom:80px;background:#0B2A1B;color:#C6F135;padding:34px;font-size:84px;text-align:center;transform:rotate(-2deg);border:8px solid #fff;outline:8px solid #0B2A1B">2 POR 1 ATÉ SEXTA!</div>
  <div class="abs" style="right:60px;top:70px;font:400 40px 'Bangers';background:#fff;border:6px solid #0B2A1B;padding:8px 22px;border-radius:50%">fruta &amp; folha</div>
</div>""")

# 4 — risografia: duas tintas sobrepostas, grão
A["04-risografia"] = ("Risografia · feira de plantas", """
<div class="p" style="background:#F2EEDF;font-family:'Bricolage Grotesque',sans-serif;color:#1E6B47">
  <div class="abs" style="inset:0;background-image:radial-gradient(rgba(30,107,71,.22) 1.4px,transparent 1.8px);background-size:9px 9px"></div>
  <div class="abs" style="left:110px;top:200px;width:620px;height:620px;border-radius:50%;background:#37C27A;mix-blend-mode:multiply"></div>
  <div class="abs" style="left:300px;top:330px;width:620px;height:620px;border-radius:50%;background:#0E7C86;mix-blend-mode:multiply;opacity:.9"></div>
  <div class="abs" style="left:420px;top:240px;width:300px;height:300px;border-radius:50%;background:#B8F2C9;mix-blend-mode:multiply"></div>
  <div class="abs" style="left:80px;top:70px;font-weight:800;font-size:60px;letter-spacing:-.03em;mix-blend-mode:multiply">folha &amp; raiz</div>
  <div class="abs" style="right:80px;top:80px;font-size:34px;font-weight:400;text-align:right;line-height:1.3">feira de plantas<br>dom · 9h–16h</div>
  <div class="abs" style="left:80px;bottom:90px;font-weight:800;font-size:190px;line-height:.82;letter-spacing:-.05em;mix-blend-mode:multiply;color:#0E5B52">verde<br>demais.</div>
</div>""")

# 5 — glass morphism: manchas de cor e cartão de vidro
A["05-glass-morphism"] = ("Glass morphism · spa botânico", """
<div class="p" style="background:linear-gradient(160deg,#0B3D2B,#13241C 60%);font-family:'Inter Tight',sans-serif;color:#fff">
  <div class="abs" style="left:-120px;top:-60px;width:620px;height:620px;border-radius:50%;background:#2FA866;filter:blur(40px)"></div>
  <div class="abs" style="right:-140px;top:380px;width:600px;height:600px;border-radius:50%;background:#7FD1A1;filter:blur(50px);opacity:.85"></div>
  <div class="abs" style="left:120px;bottom:-120px;width:520px;height:520px;border-radius:50%;background:#0E7C86;filter:blur(50px)"></div>
  <div class="abs" style="left:90px;top:170px;right:90px;bottom:170px;border-radius:64px;background:linear-gradient(145deg,rgba(255,255,255,.32),rgba(255,255,255,.08));backdrop-filter:blur(28px);border:2px solid rgba(255,255,255,.55);box-shadow:inset 0 2px 2px rgba(255,255,255,.7),0 40px 80px rgba(0,0,0,.35);padding:80px 70px">
    <div style="font-size:34px;letter-spacing:.3em;font-weight:500;opacity:.9">SPA BOTÂNICO</div>
    <div style="margin-top:90px;font:700 150px/.95 'Inter Tight';letter-spacing:-.05em">Respire<br>fundo.</div>
    <div style="margin-top:50px;font-size:44px;line-height:1.35;opacity:.92">Massagem com ervas e<br>banho de folhas, 60 min.</div>
    <div style="position:absolute;left:70px;bottom:70px;background:rgba(255,255,255,.9);color:#0B3D2B;font-weight:700;font-size:38px;padding:24px 44px;border-radius:60px">Agendar →</div></div>
</div>""")


# 6 — pixel art: fonte e planta em pixels
def pixel_planta():
    g = ["....GG....", "...GLLG...", "..GLLLLG..", ".GLLDLLLG.", "GLLLDLLLLG", ".GLLDLLLG.", "..GLDLLG..", "...GDLG...", "....DD....", "....DD....", "...BBBB...", "..BBRRBB..", "..BRRRRB..", "...BBBB..."]
    cores = {"G": "#0B3D2B", "L": "#2FA866", "D": "#1E6B47", "B": "#7A4B2A", "R": "#B8793F"}
    s, out = 34, []
    for y, row in enumerate(g):
        for x, c in enumerate(row):
            if c in cores:
                out.append(f"<div class='abs' style='left:{x*s}px;top:{y*s}px;width:{s}px;height:{s}px;background:{cores[c]}'></div>")
    return "".join(out)


A["06-pixel-art"] = ("Pixel art · plant shop", f"""
<div class="p" style="background:#0B2A1B;font-family:'Press Start 2P',monospace;color:#B8F2C9">
  <div class="abs" style="inset:0;background-image:linear-gradient(rgba(127,209,161,.09) 2px,transparent 2px),linear-gradient(90deg,rgba(127,209,161,.09) 2px,transparent 2px);background-size:34px 34px"></div>
  <div class="abs" style="left:70px;top:70px;font-size:30px;color:#7FD1A1">PLANT SHOP ▮ 1UP</div>
  <div class="abs" style="left:70px;top:150px;font-size:76px;line-height:1.25;color:#fff;text-shadow:8px 8px 0 #1E6B47">NOVA<br>FASE:<br>JARDIM</div>
  <div class="abs" style="left:370px;top:560px;width:340px;height:476px">{pixel_planta()}</div>
  <div class="abs" style="left:70px;right:70px;bottom:70px;border:8px solid #7FD1A1;padding:34px;font-size:30px;line-height:1.7;background:#13241C">&gt; MUDAS A PARTIR DE R$ 12<br>&gt; APERTE START ▮</div>
</div>""")

# 7 — Y2K: cromado, estrelas, brilho
A["07-y2k"] = ("Y2K · loja de acessórios", """
<div class="p" style="background:radial-gradient(circle at 30% 20%,#E8FFD0,#7FD1A1 45%,#1E6B47 100%);font-family:'Orbitron',sans-serif;color:#0B2A1B">
  <div class="abs" style="left:60px;top:70px;font-size:34px;font-weight:500;letter-spacing:.2em">★ MINT.CORE ★</div>
  <div class="abs" style="left:-30px;top:200px;width:1140px;text-align:center;font-weight:900;font-size:230px;line-height:.9;letter-spacing:-.03em;background:linear-gradient(180deg,#fff 0%,#d5ffe6 30%,#2FA866 52%,#fff 56%,#7FD1A1 100%);-webkit-background-clip:text;color:transparent;-webkit-text-stroke:5px #0B2A1B;filter:drop-shadow(0 14px 0 rgba(11,42,27,.35))">NEW<br>DROP</div>
  <div class="abs" style="left:150px;top:760px;width:780px;height:300px;border-radius:150px;background:linear-gradient(180deg,rgba(255,255,255,.85),rgba(255,255,255,.2));border:5px solid #0B2A1B;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:58px;box-shadow:inset 0 12px 20px rgba(255,255,255,.9),0 20px 0 rgba(11,42,27,.3);text-align:center;line-height:1.2">ACESSÓRIOS<br>COLECIONÁVEIS</div>
  <div class="abs" style="left:70px;top:610px;font-size:150px;color:#fff;-webkit-text-stroke:4px #0B2A1B">✦</div>
  <div class="abs" style="right:80px;top:140px;font-size:110px;color:#fff;-webkit-text-stroke:4px #0B2A1B">✦</div>
  <div class="abs" style="right:90px;bottom:200px;font-size:80px;color:#0B2A1B">✧</div>
  <div class="abs" style="left:0;right:0;bottom:70px;text-align:center;font-weight:900;font-size:44px;letter-spacing:.12em">SÓ ESTA SEMANA @mintcore</div>
</div>""")

# 8 — colagem: recortes de papel, fita e carimbos
A["08-colagem"] = ("Colagem · livraria", """
<div class="p" style="background:#D9E6C8;font-family:'Playfair Display',serif;color:#0B2A1B">
  <div class="abs" style="left:-60px;top:80px;width:900px;height:540px;background:#1E6B47;transform:rotate(-6deg);clip-path:polygon(0 4%,12% 0,40% 3%,70% 0,100% 5%,97% 40%,100% 70%,96% 100%,60% 96%,30% 100%,3% 96%,0 60%)"></div>
  <div class="abs" style="right:-40px;top:640px;width:560px;height:480px;background:#F3EFE6;transform:rotate(7deg);border:2px solid rgba(11,42,27,.2);box-shadow:10px 14px 0 rgba(11,42,27,.18)"></div>
  <div class="abs" style="left:170px;top:960px;width:620px;height:260px;background:#7FD1A1;transform:rotate(-3deg);clip-path:polygon(0 8%,25% 0,55% 6%,100% 0,98% 50%,100% 100%,60% 94%,20% 100%,0 92%)"></div>
  <div class="abs" style="left:70px;top:150px;color:#F3EFE6;font-weight:900;font-size:200px;line-height:.85;transform:rotate(-6deg);font-style:italic">Livros<br>& café</div>
  <div class="abs" style="right:90px;top:720px;width:400px;transform:rotate(7deg);font:400 44px/1.3 'Special Elite';color:#0B2A1B">Clube de leitura<br>toda quinta,<br>às 19h.<br><b style="font-size:38px">— Sebo Folha Viva</b></div>
  <div class="abs" style="left:210px;top:1010px;font:400 64px 'Special Elite';transform:rotate(-3deg)">ENTRADA LIVRE</div>
  <div class="abs" style="left:580px;top:60px;width:240px;height:70px;background:rgba(255,236,150,.8);transform:rotate(8deg)"></div>
  <div class="abs" style="left:80px;bottom:80px;width:180px;height:180px;border-radius:50%;border:8px solid #1E6B47;color:#1E6B47;display:flex;align-items:center;justify-content:center;text-align:center;font:700 30px/1.1 'Special Elite';transform:rotate(-14deg)">DESDE<br>1998</div>
</div>""")


def renderizar(html, png):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=12000", f"--screenshot={png}", pathlib.Path(html).as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def main():
    for nome, (rotulo, corpo) in A.items():
        h = AQUI / f"{nome}.html"
        h.write_text(f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{rotulo}</title><style>{BASE}</style></head><body>{corpo}</body></html>", encoding="utf-8")
        renderizar(h, AQUI / f"{nome}.png")
        print("ok", nome)


if __name__ == "__main__":
    main()
