"""Três telas de demonstração (1200x960, cantos arredondados, fundo transparente).
Marca e negócio (brasa café) são fictícios. Uso: python gerar_uso.py"""
import os, subprocess, pathlib, math

AQUI = pathlib.Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
W, H = 1200, 960
ARTE = "../identidades/01-cafeteria.png"

CSS = """@import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&display=swap');
:root{--ink:#13241C;--cream:#F3EFE6;--green:#1E6B47;--mint:#7FD1A1;--muted:#5b6a62;--line:rgba(19,36,28,.14);--bub:#DCE8D8}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1200px;height:960px;overflow:hidden;background:transparent}
body{font-family:'Inter Tight',system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.card{position:relative;width:1200px;height:960px;background:var(--cream);border-radius:26px;overflow:hidden;display:flex;flex-direction:column}
.top{height:88px;flex:none;display:flex;align-items:center;gap:16px;padding:0 36px;border-bottom:1.5px solid var(--line)}
.top b{font-size:34px;font-weight:600;letter-spacing:-.02em}
.tit{margin-left:auto;font-size:26px;color:var(--muted);background:#E8E3D6;border-radius:99px;padding:8px 22px}
.sp{width:44px;height:44px;flex:none}
.chat{flex:1;padding:30px 40px 0;display:flex;flex-direction:column;gap:22px;min-height:0}
.ia{display:flex;gap:18px;align-items:flex-start}
.ia .sp{width:42px;height:42px;margin-top:2px}
.ia p{font-size:30px;line-height:1.36;max-width:900px}
.us{align-self:flex-end;background:var(--bub);border-radius:26px 26px 8px 26px;padding:15px 26px;font-size:30px;line-height:1.34;max-width:820px}
.inp{flex:none;margin:0 40px 34px;height:92px;border:2px solid var(--line);border-radius:28px;background:#fff;display:flex;align-items:center;padding:0 22px 0 30px;font-size:28px;color:var(--muted)}
.inp i{margin-left:auto;width:56px;height:56px;border-radius:50%;background:var(--green);display:flex;align-items:center;justify-content:center}
.sw{display:flex;gap:14px;margin-top:14px}.sw span{display:flex;align-items:center;gap:10px;font-size:23px;color:var(--muted);background:#fff;border:1.5px solid var(--line);border-radius:99px;padding:7px 18px 7px 8px}
.sw em{display:block;width:30px;height:30px;border-radius:50%}
.chip{display:inline-flex;align-items:center;gap:10px;font-size:26px;font-weight:500;border-radius:99px;padding:12px 26px;border:2px solid var(--green);color:var(--green);background:transparent}
.chip.f{background:var(--green);color:var(--cream)}
"""

rays = "".join(
    f'<line x1="22" y1="22" x2="{22 + 17 * math.cos(a * math.pi / 6):.1f}" y2="{22 + 17 * math.sin(a * math.pi / 6):.1f}"/>'
    for a in range(12))
SPARK = f'<svg class="sp" viewBox="0 0 44 44"><g stroke="#1E6B47" stroke-width="4.2" stroke-linecap="round">{rays}</g></svg>'
SEND = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F3EFE6" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>'


def topo(t): return f'<div class="top">{SPARK}<b>Claude</b><span class="tit">{t}</span></div>'
def inp(t): return f'<div class="inp">{t}<i>{SEND}</i></div>'
_n = [0]
def prox():
    v = _n[0]; _n[0] += 1; return v
def ia(t, extra=""): return f'<div class="ia" data-s="{prox()}">{SPARK}<div><p>{t}</p>{extra}</div></div>'
def us(t): return f'<div class="us" data-s="{prox()}">{t}</div>'


D = {}
D["uso-1-perguntas"] = f"""<div class="card">{topo("selfmade · brasa café")}
<div class="chat">
{ia("Vamos montar a identidade da sua marca. <b>O que a sua cafeteria vende?</b>")}
{us("Café especial, pão de queijo e doces caseiros.")}
{ia("<b>Quem costuma comprar de você?</b>")}
{us("Gente do bairro, de 25 a 40 anos, que passa de manhã a caminho do trabalho.")}
{ia("<b>Como você quer ser visto?</b>")}
{us("Aconchegante e caseiro, com cara de café de bairro.")}
{ia("Pronto. Sugeri tons de café e brasa, com fonte de serifa. Quer ajustar algo?", '<div class="sw"><span><em style="background:#3A2417"></em>café</span><span><em style="background:#D9531E"></em>brasa</span><span><em style="background:#F5EDE0;border:1.5px solid rgba(0,0,0,.2)"></em>creme</span></div>')}
</div>{inp("Responda aqui…")}</div>"""

_n[0] = 0
D["uso-2-pedido"] = f"""<div class="card">{topo("selfmade · brasa café")}
<div class="chat" style="gap:26px">
{us("Crie um post de feed para o combo da manhã: café + pão de queijo, das 7h às 10h.")}
<div class="ia">{SPARK.replace('<svg ','<svg data-s="1" ',1)}<div style="display:flex;gap:34px;align-items:flex-start"><div data-s="1">
<p style="max-width:520px">Pronto! Post de feed na identidade da <b>brasa café</b>.</p>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:28px;align-items:flex-start"><span class="chip f">Baixar arte</span><span class="chip">Ajustar o texto</span><span class="chip">Criar o story</span></div></div>
<img data-s="2" src="{ARTE}" style="width:420px;height:525px;border-radius:20px;border:2px solid var(--line);display:block;object-fit:cover"></div></div>
</div>{inp("Peça o próximo conteúdo…")}</div>"""


def IG(p):
    return f'<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#13241C" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'


D["uso-3-publicacao"] = f"""<div class="card" style="flex-direction:row">
<img src="{ARTE}" style="width:768px;height:960px;object-fit:cover;display:block;border-right:1.5px solid var(--line)">
<div style="flex:1;display:flex;flex-direction:column;min-width:0">
 <div style="height:100px;flex:none;display:flex;align-items:center;gap:16px;padding:0 24px;border-bottom:1.5px solid var(--line)">
  <div style="width:56px;height:56px;border-radius:50%;background:#F5EDE0;border:3px solid var(--green);display:flex;align-items:center;justify-content:center"><svg width="30" height="30" viewBox="0 0 64 64" fill="none" stroke="#3A2417" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 24h34v12a15 15 0 0 1-15 15h-4a15 15 0 0 1-15-15z"/><path d="M44 28h3a7 7 0 0 1 0 14h-6"/></svg></div>
  <div><div style="font-size:27px;font-weight:600">brasacafe</div><div style="font-size:21px;color:var(--muted)">Rua das Flores, 120</div></div></div>
 <div style="flex:1;padding:26px 24px 0;font-size:26px;line-height:1.4">
  <p><b>brasacafe</b> Combo da manhã: café + pão de queijo, saindo do forno agora. De 7h às 10h.</p>
  <p style="margin-top:14px;color:var(--green);font-weight:500">#cafedobairro #combodamanhã</p>
  <span style="display:inline-flex;margin-top:30px;background:var(--green);color:var(--cream);border-radius:99px;padding:10px 24px;font-size:23px;font-weight:500">Publicado agora</span></div>
 <div style="flex:none;border-top:1.5px solid var(--line);padding:18px 24px 14px;display:flex;gap:22px;align-items:center">{IG('<path d="M12 20s-7-4.6-7-10a4 4 0 0 1 7-2.4A4 4 0 0 1 19 10c0 5.4-7 10-7 10z"/>')}{IG('<path d="M4 5h16v11H9l-5 4z"/>')}{IG('<path d="M21 4L3 11l7 3 3 7z"/><path d="M10 14l11-10"/>')}<span style="margin-left:auto">{IG('<path d="M6 4h12v17l-6-4-6 4z"/>')}</span></div>
 <div style="flex:none;height:84px;border-top:1.5px solid var(--line);display:flex;align-items:center;padding:0 24px;font-size:24px;color:var(--muted)">Adicione um comentário…</div>
</div></div>"""


ANIM = """<script>
(function(){
  if(!/anim/.test(location.search)) return;
  var grupos={}, ordem=[], id=0, PALAVRAS_POR_S=10, PAUSA=300, SEM_TEXTO=500;
  [].forEach.call(document.querySelectorAll('[data-s]'),function(e){ var k=+e.getAttribute('data-s'); (grupos[k]=grupos[k]||[]).push(e); if(ordem.indexOf(k)<0) ordem.push(k); });
  ordem.sort(function(a,b){return a-b;});
  function nos(g){ var r=[]; g.forEach(function(e){ var w=document.createTreeWalker(e,NodeFilter.SHOW_TEXT,null), n; while((n=w.nextNode())){ if(!n.nodeValue.trim()) continue; if(n.parentNode.closest('.chip,.sw')) continue; r.push({n:n,t:n.nodeValue}); } }); return r; }
  var info={}; ordem.forEach(function(k){ info[k]=nos(grupos[k]); });
  function esconder(k){ grupos[k].forEach(function(e){ e.style.visibility='hidden'; e.style.opacity='0'; e.style.transform=''; }); info[k].forEach(function(o){ o.n.nodeValue=''; }); }
  function duracao(k){ var w=info[k].reduce(function(a,o){return a+(o.t.trim().split(/\s+/).length);},0); return w? w/PALAVRAS_POR_S*1000 : SEM_TEXTO; }
  function mostrar(k,meu,DIGITA){
    grupos[k].forEach(function(e){ e.style.transition='opacity .25s ease'; e.style.visibility='visible'; e.style.opacity='1'; });
    var total=info[k].reduce(function(a,o){return a+o.t.length;},0), t0=performance.now();
    function quadro(){
      if(meu!==id) return clearInterval(iv);
      var f=Math.min(1,(performance.now()-t0)/DIGITA), c=Math.round(total*f);
      info[k].forEach(function(o){ var q=Math.min(o.t.length,c); o.n.nodeValue=o.t.slice(0,q); c-=q; if(c<0)c=0; });
      if(f>=1) clearInterval(iv);
    }
    var iv=setInterval(quadro,25); quadro();
  }
  function tocar(){
    id++; var meu=id; ordem.forEach(esconder);
    var t=0; ordem.forEach(function(k){ var d=duracao(k), ini=t; setTimeout(function(){ if(meu===id) mostrar(k,meu,d); }, ini); t+=d+PAUSA; });
  }
  ordem.forEach(esconder);
  window.addEventListener('message',function(e){ if(e.data==='play') tocar(); });
  try{ parent.postMessage('pronto','*'); }catch(x){}
})();
</script>"""


def main():
    for nome, html in D.items():
        f = AQUI / f"{nome}.html"
        f.write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{html}{ANIM}", encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--default-background-color=00000000", "--virtual-time-budget=6000", f"--window-size={W},{H}",
                        f"--screenshot={AQUI / (nome + '.png')}", f.as_uri()],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print(nome)


main()
