# Semana de 23/11/2026 · Studio La Rocha · 2 carrosséis (3 telas, 1080x1350) + 7 stories (1080x1920)
# Visual "clínica premium": papel claro, muito respiro, filetes dourados, cartões de vidro, ícones de linha.
# Gera semana-2311.html; exporte com: NODE_PATH=$(npm root -g) node exportar-semana-2311.cjs
# Regras: sem COREN, sem "Vila Nova Mauá", sem "mãe e filha", sem promessa de resultado.

LINK_GERAL = 'studiolarocha.com.br/links/?de=instagram'
LINK_AMANDA = 'studiolarocha.com.br/agenda/?p=amanda'

CSS = r'''
@font-face{font-family:"Cormorant";src:url(cormorant.woff2) format("woff2");font-weight:300 700}
@font-face{font-family:"Cormorant";font-style:italic;src:url(cormorant-italico.woff2) format("woff2");font-weight:300 700}
@font-face{font-family:"Montserrat";src:url(montserrat.woff2) format("woff2");font-weight:100 900}
:root{--creme:#F7F1E8;--papel:#FFFCF7;--ouro:#B08D57;--ouro-c:#D9BC86;--ouro-e:#8E6E3E;--tinta:#2B2622;--tinta-2:#6A6058;--wa:#1FAF5A;
--brilho:linear-gradient(100deg,#8E6E3E 0%,#B08D57 35%,#D9BC86 52%,#B08D57 70%,#8E6E3E 100%)}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#8a857e}
.p{position:relative;overflow:hidden;font-family:Montserrat;color:var(--tinta);background:var(--papel);isolation:isolate;margin:0 0 30px}
.c{width:1080px;height:1350px}
.s{width:1080px;height:1920px}
/* fundo: brilho dourado suave + grade fina (cara de tecnologia) */
.p::before{content:"";position:absolute;inset:0;z-index:-2;background:radial-gradient(70% 45% at 88% 6%,rgba(217,188,134,.28),transparent 70%),radial-gradient(60% 40% at 0% 100%,rgba(217,188,134,.18),transparent 70%)}
.grade{position:absolute;inset:0;z-index:-1;background-image:linear-gradient(rgba(176,141,87,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(176,141,87,.07) 1px,transparent 1px);background-size:54px 54px;-webkit-mask-image:radial-gradient(70% 60% at 50% 40%,#000 20%,transparent 80%);mask-image:radial-gradient(70% 60% at 50% 40%,#000 20%,transparent 80%)}
/* moldura de filete dourado com cantos marcados */
.moldura{position:absolute;inset:34px;border:1px solid rgba(176,141,87,.32);border-radius:30px;pointer-events:none;z-index:5}
.canto{position:absolute;width:22px;height:22px;border-color:var(--ouro);border-style:solid;z-index:6}
.canto.a{top:26px;left:26px;border-width:2px 0 0 2px}.canto.b{top:26px;right:26px;border-width:2px 2px 0 0}
.canto.c2{bottom:26px;left:26px;border-width:0 0 2px 2px}.canto.d{bottom:26px;right:26px;border-width:0 2px 2px 0}
.topo{position:absolute;top:74px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;z-index:7}
.marca{display:flex;align-items:center;gap:14px;font-family:Cormorant;font-weight:600;font-size:24px;letter-spacing:.28em}
.marca img{height:44px}
.etq{font-weight:600;font-size:18px;letter-spacing:.26em;color:var(--ouro-e);text-transform:uppercase}
.s .topo{top:200px}
h1,h2{font-family:Cormorant;font-weight:400;line-height:.98;letter-spacing:-.01em;font-feature-settings:'lnum' 1;font-variant-numeric:lining-nums}
h1 i,h2 i,.it{font-family:Cormorant;font-style:italic;font-weight:500;background:var(--brilho);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.04em}
.rot{font-weight:600;font-size:20px;letter-spacing:.34em;text-transform:uppercase;color:var(--ouro-e)}
.txt{font-size:30px;line-height:1.5;color:var(--tinta-2)}
.txt b{color:var(--tinta);font-weight:700}
.vidro{background:rgba(255,252,247,.58);-webkit-backdrop-filter:blur(22px) saturate(1.25);backdrop-filter:blur(22px) saturate(1.25);border:1px solid rgba(255,255,255,.75);box-shadow:0 30px 70px rgba(43,38,34,.12),inset 0 0 0 1px rgba(176,141,87,.18);border-radius:34px}
.foto{position:absolute;background-size:cover;background-position:center;border-radius:34px;overflow:hidden;box-shadow:0 30px 70px rgba(43,38,34,.16)}
.ico{width:64px;height:64px;flex:none;border-radius:20px;display:grid;place-items:center;background:linear-gradient(145deg,#FFF8EC,#F1E3C8);box-shadow:inset 0 0 0 1px rgba(176,141,87,.3)}
.ico svg{width:34px;height:34px}
.cta{display:flex;align-items:center;gap:18px;padding:26px 30px}
.cta .ico{background:var(--brilho);box-shadow:none}
.cta b{display:block;font-weight:700;font-size:30px}
.cta span{display:block;font-size:22px;color:var(--tinta-2);margin-top:2px}
.chips{display:flex;flex-wrap:wrap;gap:12px}
.chip{padding:12px 22px;border-radius:99px;font-weight:600;font-size:22px;background:rgba(255,252,247,.7);border:1px solid rgba(176,141,87,.35);color:var(--tinta)}
.rodape{position:absolute;left:84px;right:84px;bottom:78px;display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:18px;letter-spacing:.24em;color:var(--ouro-e);text-transform:uppercase;z-index:7}
.rodape .seta{display:flex;align-items:center;gap:12px}
.rodape .seta i{display:block;width:70px;height:1px;background:var(--ouro)}
.rodape .seta svg{width:20px;height:20px;margin-left:-14px}
/* stories: área da figurinha (a instrução some embaixo dela) */
.alvo{position:absolute;left:50%;transform:translateX(-50%);display:grid;place-items:center;text-align:center;border:2px dashed rgba(176,141,87,.5);color:rgba(142,110,62,.62);font-size:21px;line-height:1.45;padding:0 30px}
.alvo em{font-style:normal;font-weight:700}
.alvo.link{bottom:390px;width:760px;height:118px;border-radius:99px}
.toque{position:absolute;left:0;right:0;bottom:526px;text-align:center;font-weight:700;font-size:22px;letter-spacing:.3em;color:var(--ouro-e);text-transform:uppercase}
.s .rodape{bottom:300px;justify-content:center}
.s .conteudo{position:absolute;left:90px;right:90px;top:300px}
.s .txt{font-size:36px}
'''

SV = lambda p, c='#B08D57', w=1.5: f'<svg viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
IC = {
 'link': '<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1 1"/><path d="M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1-1"/>',
 'gota': '<path d="M12 3c3 4 6 7 6 10.5A6 6 0 0 1 6 13.5C6 10 9 7 12 3z"/><path d="M9.5 14.5a2.6 2.6 0 0 0 2.5 2"/>',
 'folha': '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19c3-5 6-8 10-10"/>',
 'lua': '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 'brilho': '<path d="M12 2.5l1.8 5.7 5.7 1.8-5.7 1.8L12 17.5l-1.8-5.7L4.5 10l5.7-1.8z"/>',
 'cal': '<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'tes': '<circle cx="6" cy="7" r="2.6"/><circle cx="6" cy="17" r="2.6"/><path d="M8.2 8.4L20 16M8.2 15.6L20 8"/>',
 'esc': '<path d="M12 3l7 3v5.5c0 4.4-3 8-7 9.5-4-1.5-7-5.1-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>',
 'cora': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 'seta': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'ok': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
}
def ic(k, c='#B08D57', w=1.5): return SV(IC[k], c, w)
def base(cls, n=None, tot=None, etq=None):
    t = etq or (f'{n:02d} / {tot:02d}' if n else '')
    return (f'<div class="grade"></div><div class="moldura"></div><i class="canto a"></i><i class="canto b"></i><i class="canto c2"></i><i class="canto d"></i>'
            f'<div class="topo"><div class="marca"><img src="simbolo-colorido.svg" alt="">STUDIO LA ROCHA</div><span class="etq">{t}</span></div>')
def rod(arrasta=True):
    return ('<div class="rodape"><span>@studiolarocha</span>' + (f'<span class="seta">Arraste<i></i>{ic("seta","#B08D57",1.8)}</span>' if arrasta else '<span>Mauá - SP</span>') + '</div>')
def cta(t='Agende pelo link na bio', sub='Online ou pelo WhatsApp, em poucos toques'):
    return f'<div class="vidro cta"><div class="ico">{ic("link","#FFFCF7",2)}</div><div><b>{t}</b><span>{sub}</span></div></div>'

P = []
# ===================== CARROSSEL A: "Depois da sessão eu…" =====================
P.append(f'''<section class="p c" id="a1">{base('c',1,3)}
<div class="foto" style="left:84px;right:84px;top:150px;height:690px;background-image:url(amb/folder-limpeza.jpg);background-position:center 60%"></div>
<div class="vidro" style="position:absolute;left:120px;top:186px;padding:14px 26px;border-radius:99px;font-weight:600;font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:var(--ouro-e)">Sessão no Studio</div>
<div style="position:absolute;left:96px;right:96px;top:890px">
<h1 style="font-size:150px">Depois da<br>sessão <i>eu…</i></h1>
</div>
{rod()}</section>''')
def linha(icone, frase, rotulo):
    return f'<div class="vidro" style="display:flex;align-items:center;gap:28px;padding:36px 38px"><div class="ico">{ic(icone)}</div><div><div style="font-family:Cormorant;font-style:italic;font-weight:500;font-size:68px;line-height:1.05">{frase}</div><div class="rot" style="font-size:17px;margin-top:8px">{rotulo}</div></div></div>'
P.append(f'''<section class="p c" id="a2">{base('c',2,3)}
<div class="foto" style="left:0;right:0;top:0;bottom:0;border-radius:0;box-shadow:none;background-image:url(amb/folder-serum.jpg);opacity:.22;filter:blur(3px) saturate(.8)"></div>
<div style="position:absolute;left:96px;right:96px;top:230px">
<div class="rot">Depois da sessão eu…</div>
<div style="display:grid;gap:26px;margin-top:48px">
{linha('gota','…senti a pele leve.','Limpeza de pele')}
{linha('folha','…fiquei mais tranquila.','Auriculoterapia')}
{linha('lua','…dormi melhor.','Auriculoterapia')}
</div>
<p class="txt" style="margin-top:46px;font-size:28px">Sensações que muitas clientes contam depois de um momento de cuidado.</p>
</div>
{rod()}</section>''')
P.append(f'''<section class="p c" id="a3">{base('c',3,3)}
<div style="position:absolute;left:96px;right:96px;top:250px;text-align:center">
<div class="rot">Studio La Rocha</div>
<h2 style="font-size:132px;margin-top:30px">Não foi sorte.<br>Foi <i>cuidado.</i></h2>
<div style="width:120px;height:1px;background:var(--ouro);margin:56px auto 0"></div>
<p class="txt" style="margin-top:44px">Limpeza de pele e auriculoterapia com a Amanda, aos sábados, só para mulheres.</p>
</div>
<div style="position:absolute;left:120px;right:120px;bottom:170px">{cta()}</div>
{rod(False)}</section>''')

# ===================== CARROSSEL B: "Sua pele / respira / de novo" =====================
P.append(f'''<section class="p c" id="b1">{base('c',1,3,'Limpeza de pele')}
<div class="foto" style="left:84px;right:84px;top:150px;height:760px;background-image:url(amb/folder-serum.jpg);background-position:center 40%"></div>
<div style="position:absolute;left:96px;right:96px;top:960px">
<h1 style="font-size:210px">Sua <i>pele</i></h1>
</div>
{rod()}</section>''')
def fato(icone, t):
    return f'<div class="vidro" style="display:flex;align-items:center;gap:22px;padding:22px 28px;border-radius:26px"><div class="ico" style="width:56px;height:56px;border-radius:16px">{ic(icone)}</div><span style="font-weight:600;font-size:28px">{t}</span></div>'
P.append(f'''<section class="p c" id="b2">{base('c',2,3,'Limpeza de pele')}
<div style="position:absolute;left:96px;right:96px;top:200px">
<h1 style="font-size:220px"><i>respira</i></h1>
<p class="txt" style="margin-top:34px;max-width:820px">A limpeza tira o que pesa no dia a dia, com calma e técnica.</p>
<div style="display:grid;gap:16px;margin-top:44px;max-width:600px">
{fato('gota','Impurezas e cravinhos')}
{fato('brilho','Células mortas')}
{fato('cora','Um momento só seu')}
</div>
</div>
<div class="foto" style="right:96px;width:300px;bottom:160px;height:300px;border-radius:50%;background-image:url(amb/folder-limpeza.jpg)"></div>
{rod()}</section>''')
P.append(f'''<section class="p c" id="b3">{base('c',3,3,'Limpeza de pele')}
<div style="position:absolute;left:96px;right:96px;top:230px">
<h1 style="font-size:220px">de <i>novo.</i></h1>
<div class="vidro" style="margin-top:60px;padding:34px 38px;display:flex;align-items:center;justify-content:space-between;gap:20px">
<div><div class="rot" style="font-size:17px">Valor de inauguração</div><div style="font-family:Cormorant;font-weight:600;font-size:96px;line-height:1;margin-top:6px;font-feature-settings:'lnum' 1">R$ 75</div></div>
<div style="text-align:right;font-size:24px;line-height:1.5;color:var(--tinta-2)">até 19/12<br>depois, R$ 85</div>
</div>
<p class="txt" style="margin-top:40px">Pele limpinha, sensação de leveza e um momento só seu.</p>
<div class="chips" style="margin-top:28px"><span class="chip">Com a Amanda</span><span class="chip">Aos sábados</span><span class="chip">Só para mulheres</span></div>
</div>
<div style="position:absolute;left:120px;right:120px;bottom:170px">{cta()}</div>
{rod(False)}</section>''')

# ===================== STORIES =====================
def story(id, dia, corpo, link, txt_link, extra=''):
    return f'''<section class="p s" id="{id}">{base('s',etq=dia)}<div class="conteudo">{corpo}</div>{extra}
<div class="toque">Agende pelo link ↓</div>
<div class="alvo link"><span>Cole aqui a figurinha <em>LINK</em> (texto “{txt_link}”)<br>{link}</span></div>
</section>'''
def pessoa(ini, nome, servs, extra):
    return f'''<div class="vidro" style="display:flex;gap:26px;align-items:center;padding:34px 36px">
<div style="width:110px;height:110px;flex:none;border-radius:50%;display:grid;place-items:center;background:var(--brilho);color:var(--papel);font-family:Cormorant;font-weight:600;font-size:58px">{ini}</div>
<div><div style="font-family:Cormorant;font-weight:600;font-size:56px;line-height:1">{nome}</div><div style="font-weight:700;font-size:30px;margin-top:10px">{servs}</div><div style="font-size:27px;color:var(--tinta-2);margin-top:4px">{extra}</div></div></div>'''
S = []
S.append(story('s1', 'Segunda', f'''<div class="rot">Quem cuida de você</div>
<h1 style="font-size:140px;margin-top:26px">Prazer, <i>somos nós</i></h1>
<div style="display:grid;gap:22px;margin-top:60px">
{pessoa('S','Sandra','Cabelo · Unhas · Sobrancelhas','Corte, cor e acabamento caprichado')}
{pessoa('A','Amanda','Limpeza de pele · Auriculoterapia','Enfermeira · aos sábados · só para mulheres')}
</div>
<p class="txt" style="margin-top:44px">Beleza, saúde e bem-estar no mesmo lugar, aqui em Mauá.</p>''', LINK_GERAL, 'Agendar'))
def sinal(n, t, d):
    return f'<div class="vidro" style="display:flex;gap:24px;align-items:center;padding:28px 32px"><div class="ico" style="font-family:Cormorant;font-weight:600;font-size:40px;color:var(--ouro-e);font-feature-settings:\'lnum\' 1">{n}</div><div><div style="font-weight:700;font-size:36px">{t}</div><div style="font-size:28px;color:var(--tinta-2);margin-top:4px">{d}</div></div></div>'
S.append(story('s2', 'Terça', f'''<div class="rot">Dica rápida</div>
<h1 style="font-size:122px;margin-top:26px">3 sinais de que a pele <i>pede uma pausa</i></h1>
<div style="display:grid;gap:18px;margin-top:54px">
{sinal(1,'Cravinhos que insistem','principalmente no nariz e no queixo')}
{sinal(2,'Brilho no meio do dia','aquela oleosidade que aparece fácil')}
{sinal(3,'Maquiagem que não assenta','a base parece não “pegar” bem')}
</div>''', LINK_AMANDA, 'Agendar limpeza de pele'))
S.append(story('s3', 'Quarta', f'''<div class="rot">Enquete</div>
<h1 style="font-size:140px;margin-top:26px">Seu sábado <i>ideal</i></h1>
<p class="txt" style="margin-top:30px">Cabelo novo ou pele renovada? Vote aqui embaixo. 💛</p>''', LINK_GERAL, 'Agendar',
 extra='<div class="alvo" style="top:820px;width:860px;height:420px;border-radius:40px"><span>Cole aqui a figurinha <em>ENQUETE</em><br>Opções: “Cabelo novo 💇‍♀️” e “Pele renovada ✨”</span></div>'))
def passo(n, t, d):
    return f'<div style="display:grid;grid-template-columns:70px 1fr;gap:22px;align-items:start"><div style="width:70px;height:70px;border-radius:50%;border:1.5px solid var(--ouro);display:grid;place-items:center;font-family:Cormorant;font-weight:600;font-size:36px;color:var(--ouro-e);font-feature-settings:\'lnum\' 1">{n}</div><div><div style="font-weight:700;font-size:36px">{t}</div><div style="font-size:28px;color:var(--tinta-2);margin-top:2px">{d}</div></div></div>'
S.append(story('s4', 'Quinta', f'''<div class="rot">Por dentro da sessão</div>
<h1 style="font-size:122px;margin-top:26px">Como é uma <i>limpeza de pele</i></h1>
<div class="vidro" style="display:grid;gap:26px;padding:40px 38px;margin-top:50px">
{passo(1,'Higienização','a pele é limpa com suavidade')}
{passo(2,'Esfoliação','tira as células mortas')}
{passo(3,'Extração com cuidado','dos cravinhos, sem pressa')}
{passo(4,'Finalização','máscara calmante e proteção')}
</div>''', LINK_AMANDA, 'Agendar limpeza de pele'))
def sab(d, st, on):
    return f'<div style="flex:1;text-align:center;padding:26px 8px;border-radius:26px;{"background:var(--brilho);color:var(--papel);box-shadow:0 20px 50px rgba(142,110,62,.3)" if on else "border:1.5px dashed rgba(176,141,87,.4);color:rgba(43,38,34,.45)"}"><div style="font-weight:700;font-size:18px;letter-spacing:.2em">SÁB</div><div style="font-family:Cormorant;font-weight:600;font-size:{88 if on else 64}px;line-height:1.05;font-feature-settings:\'lnum\' 1;{"" if on else "text-decoration:line-through"}">{d}</div><div style="font-weight:700;font-size:17px;letter-spacing:.12em">{st}</div></div>'
S.append(story('s5', 'Sexta', f'''<div class="rot">Obrigada pelo carinho</div>
<h1 style="font-size:130px;margin-top:26px">Novembro <i>lotou.</i></h1>
<p class="txt" style="margin-top:30px">E dezembro já está quase cheio na agenda da Amanda.</p>
<div style="display:flex;gap:14px;margin-top:56px">{sab('05','LOTADO',False)}{sab('12','1 HORÁRIO',True)}{sab('19','LOTADO',False)}</div>''', LINK_AMANDA, 'Ver horários'))
def hor(d, h):
    return f'<div class="vidro" style="display:flex;justify-content:space-between;align-items:center;padding:28px 34px"><div><div class="rot" style="font-size:16px">Sábado</div><div style="font-family:Cormorant;font-weight:600;font-size:64px;line-height:1.05;font-feature-settings:\'lnum\' 1">{d}</div></div><div style="font-weight:700;font-size:30px;color:var(--ouro-e);text-align:right">{h}</div></div>'
S.append(story('s6', 'Sábado', f'''<div class="rot">Lembrete</div>
<h1 style="font-size:132px;margin-top:26px">Sábado <i>tem horário</i></h1>
<p class="txt" style="margin-top:30px">Os próximos livres com a Amanda:</p>
<div style="display:grid;gap:18px;margin-top:40px">{hor('12/12','18h20')}{hor('09/01','15h · 17h · 19h')}</div>''', LINK_AMANDA, 'Quero um horário'))
S.append(story('s7', 'Domingo', f'''<div class="foto" style="position:relative;height:520px;background-image:url(amb/folder-limpeza.jpg)"></div>
<div class="vidro" style="margin:-120px 40px 0;position:relative;padding:40px 40px 36px;text-align:center">
<div class="rot">Limpeza de pele</div>
<div style="font-family:Cormorant;font-weight:600;font-size:150px;line-height:1;margin-top:14px;font-feature-settings:'lnum' 1">R$ 75</div>
<div style="font-size:30px;color:var(--tinta-2);margin-top:8px">valor de inauguração até <b style="color:var(--tinta)">19/12</b></div>
</div>
<p class="txt" style="margin-top:40px;text-align:center">Comece a semana já pensando no seu sábado. 🤍</p>''', LINK_AMANDA, 'Agendar limpeza de pele'))

html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Semana 23/11 · Studio La Rocha</title><style>{CSS}</style></head><body>' + '\n'.join(P + S) + '</body></html>'
open('semana-2311.html', 'w').write(html)
print('ok')
