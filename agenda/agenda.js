// Agenda do Studio La Rocha: a cliente escolhe a profissional, o serviço, o dia e o horário, e reserva.
// O banco confere tudo de novo (horário livre, duração, maca ocupada, limites): a tela só ajuda a escolher.
(function(){
  var C=window.SUPABASE||{},Z=(window.SALAO&&SALAO.whatsapp)||'5511967682546',$=function(i){return document.getElementById(i)};
  var q=new URLSearchParams(location.search);
  var ORIGENS={instagram:'Instagram do Studio La Rocha',facebook:'Facebook do Studio La Rocha',google:'perfil do Studio La Rocha no Google',whatsapp:'perfil do Studio La Rocha no WhatsApp',cartao:'cartão do Studio La Rocha',cartaz:'cartaz do Studio La Rocha',espelho:'QR code do espelho do Studio La Rocha',amanda:'site da Amanda Rocha'};
  var de=(q.get('de')||'').toLowerCase(),ua=navigator.userAgent;
  var chave=ORIGENS[de]?de:/Instagram/i.test(ua)?'instagram':/FBAN|FBAV/.test(ua)?'facebook':'';
  var origem=ORIGENS[chave]||'site do Studio La Rocha';
  // link enviado pela profissional: só estes dias, nome e serviço já escolhidos
  var DIAS=(q.get('dias')||'').split(',').filter(function(d){return /^\d{4}-\d\d-\d\d$/.test(d)});
  var S={prof:q.get('p')||null,serv:q.get('s')||null,dia:null,hora:null};
  var profs=[],servs=[],slots=[],estado='carregando',aviso='',feito=null,enviando=false;
  var SEM=['domingo','segunda','terça','quarta','quinta','sexta','sábado'];

  function esc(t){return String(t==null?'':t).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function cab(){return {apikey:C.anonKey,'Content-Type':'application/json'}}
  function rpc(f,corpo){return fetch(C.url+'/rest/v1/rpc/'+f,{method:'POST',headers:cab(),body:JSON.stringify(corpo||{})}).then(function(r){if(!r.ok)throw 0;return r.json()})}
  function dd(n){return (n<10?'0':'')+n}
  function hh(h){return (+h.slice(0,2))+(h.slice(3,5)==='00'?'h':'h'+h.slice(3,5))}
  function utc(d){var p=d.split('-');return new Date(Date.UTC(+p[0],+p[1]-1,+p[2]))}
  function diaTxt(d){var x=utc(d);return SEM[x.getUTCDay()]+', '+dd(x.getUTCDate())+'/'+dd(x.getUTCMonth()+1)}
  function minDe(h){return (+h.slice(0,2))*60+(+h.slice(3,5))}
  function ts(d,h){return utc(d).getTime()+minDe(h)*60000}
  function tsIso(s){var m=/^(\d{4})-(\d\d)-(\d\d)[T ](\d\d):(\d\d)/.exec(s||'');return m?Date.UTC(+m[1],+m[2]-1,+m[3],+m[4],+m[5]):0}
  function preco(v){var n=+v;return 'R$ '+(n%1?n.toFixed(2).replace('.',','):n)}
  function dur(m){m=+m||60;var h=Math.floor(m/60),r=m%60;return h?h+'h'+(r?dd(r):''):r+' min'}
  function primeiro(n){return String(n||'').trim().split(/\s+/)[0]}
  function prof(){return profs.filter(function(p){return p.id===S.prof})[0]}
  function servico(){return servs.filter(function(s){return s.id===S.serv&&s.profissional===S.prof})[0]}
  function zap(t){return 'https://wa.me/'+Z+'?text='+encodeURIComponent(t)}

  // o horário cabe o serviço sem encostar em outro atendimento dela, nem usar a maca de outra
  function cabe(x,sv){
    if(x.status!=='livre'||x.profissional!==S.prof)return false;
    if(sv.desde&&x.data<sv.desde)return false;
    var a=ts(x.data,x.hora),b=a+(+sv.duracao||60)*60000;
    return !slots.some(function(o){
      if(o.status==='livre'||o.id===x.id)return false;
      if(o.profissional!==S.prof&&!(sv.recurso&&o.recurso===sv.recurso))return false;
      var c=ts(o.data,o.hora);return c<b&&tsIso(o.ate)>a});
  }
  function livres(){var sv=servico();if(!sv)return [];return slots.filter(function(x){return cabe(x,sv)&&(!DIAS.length||DIAS.indexOf(x.data)>=0)})}
  function dias(){var m={},o=[];livres().forEach(function(x){if(!m[x.data]){m[x.data]=[];o.push(x.data)}m[x.data].push(x)});return o.map(function(d){return {data:d,itens:m[d]}})}

  function carregar(){
    if(!C.url||!C.anonKey){estado='sem';render();return Promise.resolve()}
    return Promise.all([rpc('profissionais_publicas'),rpc('servicos_publicos'),rpc('agenda_publica')])
      .then(function(r){profs=r[0]||[];servs=r[1]||[];slots=r[2]||[];estado='ok';
        if(S.prof&&!prof())S.prof=null;
        if(!S.prof&&profs.length===1)S.prof=profs[0].id;
        if(S.serv&&!servico())S.serv=null;
        var ds=dias();if(S.dia&&!ds.some(function(d){return d.data===S.dia}))S.dia=null;
        if(S.hora&&!livres().some(function(x){return x.id===S.hora}))S.hora=null;
        render()})
      .catch(function(){estado='falhou';render()});
  }

  function passo(n,t,feitoTxt,corpo){return '<section class="passo'+(feitoTxt?' ok':'')+'"><div class="pt"><span class="pn">'+n+'</span><h2>'+t+'</h2>'+(feitoTxt?'<span class="pf">'+feitoTxt+'</span>':'')+'</div>'+corpo+'</section>'}
  function render(){
    var el=$('app'),h='';
    if(estado==='carregando'){el.innerHTML='<p class="vazio">Carregando os horários…</p>';return}
    if(feito){el.innerHTML=telaFeito();return}
    if(estado!=='ok'){el.innerHTML='<div class="cartao-msg"><b>Não consegui carregar os horários agora.</b><p>Fale com a gente pelo WhatsApp, que a gente marca para você.</p><a class="btn forte" href="'+esc(zap('Oi! 🤍 Vim pelo '+origem+' e gostaria de agendar um horário. Quais dias você tem disponíveis?'))+'">Agendar pelo WhatsApp</a></div>';return}
    var p=prof(),sv=servico();
    h+=passo(1,'Com quem?',p?esc(primeiro(p.nome)):'','<div class="opcoes profs">'+profs.map(function(x){
      return '<button type="button" class="op'+(x.id===S.prof?' sel':'')+'" data-prof="'+esc(x.id)+'" aria-pressed="'+(x.id===S.prof)+'"><span class="ini">'+esc(x.nome.charAt(0))+'</span><b>'+esc(x.nome)+'</b></button>'}).join('')+'</div>');
    if(p){var lista=servs.filter(function(s){return s.profissional===S.prof});
      h+=passo(2,'Qual serviço?',sv?esc(sv.nome):'',lista.length?'<div class="opcoes servs">'+lista.map(function(s){
        return '<button type="button" class="op serv'+(s.id===S.serv?' sel':'')+'" data-serv="'+esc(s.id)+'" aria-pressed="'+(s.id===S.serv)+'"><b>'+esc(s.nome)+'</b><span>'+
          (s.preco!=null?(s.preco_antes!=null?'<s>'+preco(s.preco_antes)+'</s> ':'')+preco(s.preco)+' · ':'')+dur(s.duracao)+'</span>'+(s.detalhe?'<small>'+esc(s.detalhe)+'</small>':'')+'</button>'}).join('')+'</div>':
        '<p class="vazio">A '+esc(primeiro(p.nome))+' ainda está montando a agenda online. <a href="'+esc(zap('Oi, '+primeiro(p.nome)+'! 🤍 Vim pelo '+origem+' e gostaria de agendar um horário com você.'))+'">Chame no WhatsApp</a>.</p>')}
    if(sv){var ds=dias();
      h+=passo(3,'Qual dia?',S.dia?esc(diaTxt(S.dia)):'',ds.length?'<div class="chips">'+ds.map(function(d){
        return '<button type="button" class="chip dia'+(d.data===S.dia?' sel':'')+'" data-dia="'+d.data+'" aria-pressed="'+(d.data===S.dia)+'"><b>'+esc(diaTxt(d.data))+'</b><small>'+d.itens.length+(d.itens.length>1?' horários':' horário')+'</small></button>'}).join('')+'</div>'+
        (DIAS.length?'<button type="button" class="link" data-todos>Ver todos os dias</button>':''):
        '<p class="vazio">Sem horários livres para '+esc(sv.nome.toLowerCase())+' agora. <a href="'+esc(zap('Oi! 🤍 Vim pelo '+origem+' e queria um horário de '+sv.nome.toLowerCase()+' com a '+primeiro(p.nome)+'. Quais dias você tem?'))+'">Peça um horário no WhatsApp</a>.</p>')}
    if(sv&&S.dia){var hs=livres().filter(function(x){return x.data===S.dia});
      h+=passo(4,'Qual horário?',S.hora?esc(hh(hs.filter(function(x){return x.id===S.hora})[0].hora)):'','<div class="chips">'+hs.map(function(x){
        return '<button type="button" class="chip'+(x.id===S.hora?' sel':'')+'" data-hora="'+esc(x.id)+'" aria-pressed="'+(x.id===S.hora)+'">'+hh(x.hora)+'</button>'}).join('')+'</div>')}
    if(S.hora){var n0=q.get('n')||'';
      h+=passo(5,'Seus dados','','<form id="fReserva" novalidate><label for="fNome">Seu nome</label><input id="fNome" autocomplete="name" maxlength="60" value="'+esc(n0)+'" placeholder="Ex.: Maria Silva">'+
        '<label for="fTel">Seu WhatsApp</label><input id="fTel" type="tel" inputmode="tel" autocomplete="tel" placeholder="(11) 90000-0000">'+
        (aviso?'<div class="aviso">'+aviso+'</div>':'')+
        '<button class="btn forte" type="submit"'+(enviando?' disabled':'')+'>'+(enviando?'Reservando…':'Reservar meu horário')+'</button>'+
        '<p class="nota">O pagamento é feito no salão, no dia. Nunca pedimos Pix ou sinal por mensagem.</p></form>')}
    else if(aviso)h+='<div class="aviso">'+aviso+'</div>';
    el.innerHTML=h;
  }
  function telaFeito(){var f=feito;
    var t='Oi'+(f.prof?', '+primeiro(f.prof):'')+'! 🤍 Vim pelo '+origem+' e acabei de pedir '+f.serv.toLowerCase()+' para '+f.quando+'. Meu nome é '+f.nome+'.';
    return '<div class="cartao-msg ok"><span class="selo-ok">✓</span><b>Pedido enviado!</b><p>'+esc(f.serv)+' com a '+esc(primeiro(f.prof))+', <b>'+esc(f.quando)+'</b>.</p><p>A '+esc(primeiro(f.prof))+' confirma com você pelo WhatsApp. Se quiser, já mande uma mensagem:</p>'+
      '<a class="btn forte" href="'+esc(zap(t))+'">Avisar pelo WhatsApp</a><p class="nota">O pagamento é feito no salão, no dia.</p><a class="link" href="./'+(chave?'?de='+chave:'')+'">Marcar outro horário</a></div>';
  }

  document.addEventListener('click',function(e){
    var b=e.target.closest('[data-prof],[data-serv],[data-dia],[data-hora],[data-todos]');if(!b)return;aviso='';
    if(b.hasAttribute('data-prof')){var np=b.getAttribute('data-prof');if(np!==S.prof){S.prof=np;S.serv=null;S.dia=null;S.hora=null}}
    else if(b.hasAttribute('data-serv')){S.serv=b.getAttribute('data-serv');S.dia=null;S.hora=null}
    else if(b.hasAttribute('data-dia')){S.dia=b.getAttribute('data-dia');S.hora=null}
    else if(b.hasAttribute('data-hora'))S.hora=b.getAttribute('data-hora');
    else if(b.hasAttribute('data-todos')){DIAS=[];S.dia=null;S.hora=null}
    render();
    var alvo=document.querySelector('.passo:last-of-type');if(alvo&&alvo.scrollIntoView)alvo.scrollIntoView({behavior:'smooth',block:'start'});
  });
  document.addEventListener('submit',function(e){
    if(e.target.id!=='fReserva')return;e.preventDefault();if(enviando)return;
    var nome=$('fNome').value.trim().replace(/\s+/g,' '),tel=$('fTel').value.replace(/\D/g,'').replace(/^55(?=\d{10,11}$)/,'');
    var x=slots.filter(function(s){return s.id===S.hora})[0],sv=servico(),p=prof();
    if(nome.length<2){aviso='Escreva o seu nome.';render();return}
    if(tel.length<10||tel.length>11){aviso='Confira o WhatsApp: use o número com DDD.';render();$('fNome').value=nome;return}
    enviando=true;aviso='';render();$('fNome').value=nome;$('fTel').value=tel;
    rpc('pedir_horario',{p_id:x.id,p_servico:sv.nome,p_nome:nome,p_telefone:tel}).then(function(r){
      enviando=false;
      if(r==='ok'){feito={nome:nome,serv:sv.nome,prof:p.nome,quando:diaTxt(x.data)+' às '+hh(x.hora)};render();window.scrollTo(0,0);return}
      var M={indisponivel:'<b>Esse horário acabou de ser pego.</b> Escolha outro, por favor.',conflito:'<b>Esse horário ficou apertado.</b> Ele encosta em outro atendimento. Escolha outro, por favor.',
        limite:'<b>Você já tem 2 horários reservados.</b> Para marcar mais, fale com a gente no WhatsApp.',dados:'Confira o seu nome e o WhatsApp.',servico:'Esse serviço não está disponível agora. Escolha outro.',
        pausado:'<b>Agora estamos confirmando os horários pelo WhatsApp.</b> <a href="'+esc(zap('Oi! 🤍 Vim pelo '+origem+' e queria '+sv.nome.toLowerCase()+' com a '+primeiro(p.nome)+' '+diaTxt(x.data)+' às '+hh(x.hora)+'. Meu nome é '+nome+'.'))+'">Toque aqui para mandar o pedido</a>.'};
      aviso=M[r]||'Não deu certo agora. Tente de novo.';
      if(r==='indisponivel'||r==='conflito'){S.hora=null;return carregar()}
      render();if($('fNome')){$('fNome').value=nome;$('fTel').value=tel}
    }).catch(function(){enviando=false;aviso='Sem conexão. Confira a internet e tente de novo.';render();if($('fNome')){$('fNome').value=nome;$('fTel').value=tel}});
  });
  if(chave&&$('voltar'))$('voltar').href='../links/?de='+chave;
  carregar();
})();
