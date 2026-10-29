(function(){
  var root=document.documentElement;
  root.classList.add('js');
  var panels=[].slice.call(document.querySelectorAll('.panel'));
  var bar=document.querySelector('#tabs div');
  var links=[];
  panels.forEach(function(p,i){
    var a=document.createElement('a');
    a.href='#'+p.id;
    a.textContent=p.getAttribute('data-label');
    bar.appendChild(a);
    links.push(a);
  });
  function setCurrent(idx){
    links.forEach(function(a,i){
      if(i===idx){
        if(a.getAttribute('aria-current')!=='page'){
          a.setAttribute('aria-current','page');
          var l=bar.scrollLeft+(a.getBoundingClientRect().left-bar.getBoundingClientRect().left)-(bar.clientWidth-a.offsetWidth)/2;
          bar.scrollTo({left:l,behavior:'smooth'});
        }
      } else a.removeAttribute('aria-current');
    });
  }
  setCurrent(0);
  panels[0].classList.add('in');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        var idx=panels.indexOf(en.target);
        if(en.isIntersecting){
          en.target.classList.add('in');
          setCurrent(idx);
          try{ history.replaceState(null,'','#'+en.target.id); }catch(err){}
        } else {
          en.target.classList.remove('in');
        }
      });
    },{threshold:0.55,rootMargin:'-61px 0px 0px 0px'});
    panels.forEach(function(p){ io.observe(p); });
  } else {
    panels.forEach(function(p){ p.classList.add('in'); });
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href^="#"]');
    if(!a) return;
    var target=document.getElementById(a.getAttribute('href').slice(1));
    if(!target||panels.indexOf(target)<0) return;
    e.preventDefault();
    target.scrollIntoView({behavior:'smooth',block:'start'});
  });
  (function(){
    var fan=document.getElementById('fan'); if(!fan) return;
    var alvo=fan.querySelector('.float img'), atual=alvo.getAttribute('src'), t;
    function destaque(g){
      var im=g.querySelector('img'); if(!im) return;
      var src=im.getAttribute('src'); if(src===atual) return;
      atual=src; clearTimeout(t);
      alvo.classList.add('troca');
      t=setTimeout(function(){
        alvo.setAttribute('src',src); alvo.setAttribute('alt',im.getAttribute('alt')||'');
        alvo.classList.remove('troca');
      },180);
    }
    fan.addEventListener('mouseover',function(e){
      var g=e.target.closest&&e.target.closest('.glass'); if(g) destaque(g);
    });
  })();
  (function(){
    var car=document.getElementById('carrossel'); if(!car) return;
    var items=[].slice.call(car.querySelectorAll('.item')), n=items.length, cur=0;
    var nome=document.getElementById('car-nome'), tipo=document.getElementById('car-tipo');
    function layout(){
      items.forEach(function(it,i){
        var off=((i-cur)%n+n)%n; if(off>n/2) off-=n;
        var a=Math.abs(off), vis=a<=2;
        it.style.transform='translateX('+(off*66)+'%) scale('+(1-a*.14)+')';
        it.style.opacity=vis?[1,.5,.22][a]:0;
        it.style.zIndex=10-a;
        it.style.pointerEvents=vis?'auto':'none';
        it.setAttribute('aria-hidden',a===0?'false':'true');
      });
      nome.textContent=items[cur].getAttribute('data-nome');
      tipo.textContent=items[cur].getAttribute('data-tipo');
    }
    function go(d){ cur=((cur+d)%n+n)%n; layout(); }
    items.forEach(function(it,i){ it.addEventListener('click',function(){ if(i!==cur){ var off=((i-cur)%n+n)%n; go(off>n/2?off-n:off); } }); });
    document.getElementById('car-prev').addEventListener('click',function(){ go(-1); });
    document.getElementById('car-next').addEventListener('click',function(){ go(1); });
    var x0=null;
    car.addEventListener('pointerdown',function(e){ x0=e.clientX; });
    window.addEventListener('pointerup',function(e){ if(x0===null) return; var d=e.clientX-x0; x0=null; if(Math.abs(d)>45) go(d<0?1:-1); });
    window.addEventListener('keydown',function(e){
      var p=document.getElementById('resultados'); if(!p||!p.classList.contains('in')) return;
      if(e.key==='ArrowRight'){ go(1); } else if(e.key==='ArrowLeft'){ go(-1); }
    });
    layout();
  })();
  (function(){
    var n=document.getElementById('mens'), r=document.getElementById('mens-r'), out=document.getElementById('calc-out');
    if(!n||!r||!out) return;
    var PRODUTO=500, CLAUDE=120, ANO=12;
    var bA=document.getElementById('bar-ag'), bS=document.getElementById('bar-sm'), vA=document.getElementById('val-ag'), vS=document.getElementById('val-sm');
    function brl(v){ return 'R$ '+Math.round(v).toLocaleString('pt-BR'); }
    function calc(){
      var m=parseFloat(r.value); n.textContent=m.toLocaleString('pt-BR');
      var ag=m*ANO, sm=PRODUTO+CLAUDE*ANO, mx=Math.max(ag,sm);
      if(bA){ bA.style.width=(ag/mx*100)+'%'; bS.style.width=(sm/mx*100)+'%'; vA.textContent=brl(ag); vS.textContent=brl(sm); }
      if(!(m>CLAUDE)){ out.innerHTML='Com esse valor, a agência sai <b>mais barata</b> que a selfmade.'; return; }
      var mes=Math.floor(PRODUTO/(m-CLAUDE))+1;
      var t=mes<=1 ? 'A selfmade já é <b>mais barata no 1º mês</b>.' : 'A partir do <b>mês '+mes+'</b> a agência fica mais cara que a selfmade.';
      if(ag>sm) t+=' Em um ano, são <b>'+brl(ag-sm)+' a menos</b>.';
      out.innerHTML=t;
    }
    r.addEventListener('input',calc);
    calc();
  })();
  (function(){
    var P=document.getElementById('preco'), E=document.getElementById('resultados'); if(!P||!E) return;
    var W=P.querySelector('.wrap'), nP=P.querySelector('.num'), nE=E.querySelector('.num');
    function alinhar(){
      W.style.paddingTop='';
      var h0=P.offsetHeight, base=parseFloat(getComputedStyle(W).paddingTop);
      var pad=Math.max(0,base+(nE.offsetTop-E.offsetTop)-(nP.offsetTop-P.offsetTop));
      W.style.paddingTop=pad+'px';
      var exc=P.offsetHeight-h0; if(exc>0) W.style.paddingTop=Math.max(0,pad-exc)+'px';
    }
    window.addEventListener('resize',alinhar); window.addEventListener('load',alinhar); if(document.fonts&&document.fonts.ready) document.fonts.ready.then(alinhar); alinhar();
  })();
  (function(){
    var ds=[].slice.call(document.querySelectorAll('#faq details'));
    ds.forEach(function(d){ d.addEventListener('toggle',function(){ if(d.open) ds.forEach(function(o){ if(o!==d) o.open=false; }); }); });
  })();
  (function(){
    var box=document.getElementById('passos'); if(!box) return;
    var ims=[].slice.call(document.querySelectorAll('.passo-img img, .passo-img iframe')), pi=document.querySelector('.passo-img'), vis=false, ps=[].slice.call(box.querySelectorAll('.p3')), dots=[].slice.call(document.querySelectorAll('#passo-pontos i')), cur=0, n=ps.length;
    function pintar(){
      ps.forEach(function(p,i){ var rel=(i-cur+n)%n; p.classList.toggle('ativo',rel===0); p.classList.toggle('saiu',rel===n-1); p.setAttribute('aria-hidden',rel===0?'false':'true'); });
      ims.forEach(function(m,i){ var rel=(i-cur+n)%n; m.classList.toggle('ativo',rel===0); m.classList.toggle('saiu',rel===n-1); });
      dots.forEach(function(d,i){ d.classList.toggle('on',i===cur); });
      box.setAttribute('data-passo',String(cur+1));
    }
    function escala(){
      var P=document.getElementById('como'), mob=window.innerWidth<760;
      P.style.minHeight='';
      if(!mob){ pi.style.top=pi.style.height=pi.style.width=pi.style.left=pi.style.right=''; }
      else {
        var G=14, MIN=210, pr=P.getBoundingClientRect(), t=box.getBoundingClientRect(), c=document.querySelector('.passo-ctl').getBoundingClientRect();
        var topo=t.bottom-pr.top+G, livre=c.top-pr.top-G-topo, gut=20, larg=window.innerWidth-2*gut;
        if(livre<MIN){ P.style.minHeight=Math.ceil(P.offsetHeight+MIN-livre)+'px'; pr=P.getBoundingClientRect(); c=document.querySelector('.passo-ctl').getBoundingClientRect(); livre=c.top-pr.top-G-topo; }
        var h=Math.max(60,Math.min(larg/1.25,livre)), w=h*1.25;
        pi.style.top=Math.round(topo)+'px'; pi.style.height=Math.round(h)+'px'; pi.style.width=Math.round(w)+'px'; pi.style.left=Math.round((window.innerWidth-w)/2)+'px'; pi.style.right='auto';
      }
      pi.style.setProperty('--k',(pi.clientWidth/1200).toFixed(4));
    }
    function tocar(){ var f=ims[cur]; if(vis && f && f.tagName==='IFRAME' && f.contentWindow) f.contentWindow.postMessage('play','*'); }
    window.addEventListener('message',function(e){ if(e.data==='pronto') tocar(); });
    window.addEventListener('resize',escala); window.addEventListener('load',escala); if(document.fonts&&document.fonts.ready) document.fonts.ready.then(escala); escala(); requestAnimationFrame(function(){ requestAnimationFrame(function(){ pi.classList.add('pronto'); }); });
    if('IntersectionObserver' in window){ new IntersectionObserver(function(en){ var v=en[0].intersectionRatio>=.6; if(v&&!vis){ vis=true; tocar(); } else if(!v){ vis=false; } },{threshold:.6}).observe(document.getElementById('como')); } else { vis=true; }
    function proximo(){ cur=(cur+1)%n; pintar(); tocar(); }
    document.getElementById('como').addEventListener('click',function(e){ if(e.target.closest('a,button,summary')) return; proximo(); });
    box.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); proximo(); } });
    pintar();
  })();
  var HH=61, lockUntil=0;
  function currentIndex(){
    var idx=0;
    panels.forEach(function(p,i){ if(p.getBoundingClientRect().top<=HH+40) idx=i; });
    return idx;
  }
  window.addEventListener('wheel',function(e){
    if(e.ctrlKey||Math.abs(e.deltaY)<4||Math.abs(e.deltaX)>Math.abs(e.deltaY)) return;
    var now=Date.now();
    var i=currentIndex(), p=panels[i];
    var r=p.getBoundingClientRect();
    var fits=p.offsetHeight<=innerHeight-HH+2;
    if(!fits) return;
    e.preventDefault();
    if(now<lockUntil){ lockUntil=Math.max(lockUntil,now+120); return; }
    var next=panels[i+(e.deltaY>0?1:-1)];
    if(!next) return;
    lockUntil=now+850;
    next.scrollIntoView({behavior:'smooth',block:'start'});
  },{passive:false});
  var h=location.hash.slice(1), t=h&&document.getElementById(h);
  if(t&&panels.indexOf(t)>=0) setTimeout(function(){ t.scrollIntoView({block:'start'}); },0);
})();
