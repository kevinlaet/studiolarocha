# Black Friday 2026 · Studio La Rocha · limpeza de pele com a Amanda · carrossel de 5 telas (1080x1350)
# Uso: python3 gerar.py && NODE_PATH=$(npm root -g) node exportar.cjs
# ====== CAMPOS QUE A AMANDA CONFIRMA (troque aqui e gere de novo) ======
PACOTES = None            # ex.: 4 -> "Só 4 pacotes 🖤"  (None = "Pacotes limitados 🖤")
SABADOS = None            # ex.: ["28/11", "12/12"] -> "Sábados: 28/11 e 12/12"  (None = "Atendimento aos sábados")
VALIDADE_2A = None        # ex.: "31/01" -> "2ª sessão até 31/01"  (None = linha some)
PRAZO = "27/11"           # último dia para garantir o pacote
PRECO = "100"             # valor do pacote (2 sessões)
# Regras: sem COREN nas artes (pedido da Amanda), local sempre "Mauá - SP", sem promessa de resultado.
# =======================================================================
import html
def e(x): return html.escape(str(x))
def lista(xs): return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' e ' + xs[-1]
txt_pac = f'Só {PACOTES} pacotes 🖤' if PACOTES else 'Pacotes limitados 🖤'
txt_sab = f'Sábados: {lista(SABADOS)}' if SABADOS else 'Atendimento aos sábados'
cada = int(PRECO) // 2
F = '../../fonte/'
CSS = r'''
@font-face{font-family:"Cormorant";src:url(F/cormorant.woff2) format("woff2");font-weight:300 700}
@font-face{font-family:"Great Vibes";src:url(F/greatvibes.woff2) format("woff2")}
@font-face{font-family:"Montserrat";src:url(F/montserrat.woff2) format("woff2");font-weight:100 900}
:root{--creme:#F7F1E8;--papel:#FFFCF7;--ouro:#B08D57;--ouro-c:#D9BC86;--ouro-e:#8E6E3E;--bronze:#9C7A45;--tinta:#2B2622;--tinta-2:#6A6058;--escuro:#1F1A17;--marfim:#F4EBDD;--wa:#1FAF5A;
--brilho:linear-gradient(100deg,#8E6E3E 0%,#C9A468 30%,#F1DEB4 48%,#C9A468 66%,#8E6E3E 100%)}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#777}
.t{position:relative;width:1080px;height:1350px;overflow:hidden;margin:0 0 30px;padding:96px 96px 0;font-family:Montserrat;isolation:isolate;display:flex;flex-direction:column}
.escura{background:radial-gradient(120% 90% at 85% 0%,#3A2C1B 0%,#1F1A17 55%,#16120F 100%);color:var(--marfim)}
.clara{background:var(--creme);color:var(--tinta)}
.topo{display:flex;align-items:center;justify-content:space-between;flex:none}
.marca{display:flex;align-items:center;gap:16px;font-family:Cormorant;font-weight:500;font-size:27px;letter-spacing:.24em}
.marca img{height:58px}
.pag{font-weight:700;font-size:20px;letter-spacing:.2em;padding:11px 18px;border-radius:99px;border:1.5px solid rgba(176,141,87,.45)}
.escura .pag{color:var(--ouro-c)} .clara .pag{color:var(--bronze)}
.bf{display:inline-flex;align-items:center;gap:14px;align-self:flex-start;background:#0A0908;color:#fff;font-weight:800;font-size:25px;letter-spacing:.28em;padding:16px 28px;border-radius:99px;box-shadow:0 0 0 2px rgba(217,188,134,.6)}
.rot{font-weight:700;font-size:23px;letter-spacing:.32em;text-transform:uppercase}
.escura .rot{color:var(--ouro-c)} .clara .rot{color:var(--bronze)}
h1,h2{font-family:Cormorant;font-weight:500;line-height:.98;letter-spacing:-.005em}
em{font-style:normal;font-family:"Great Vibes";font-weight:400;padding-right:.08em;background:var(--brilho);-webkit-background-clip:text;background-clip:text;color:transparent}
.clara em{background:linear-gradient(100deg,#8E6E3E,#B08D57 45%,#C9A468 60%,#8E6E3E);-webkit-background-clip:text;background-clip:text}
p.lead{font-size:34px;line-height:1.5}
.escura p.lead{color:rgba(244,235,221,.85)} .clara p.lead{color:var(--tinta-2)}
p.lead b{font-weight:700} .escura p.lead b{color:var(--marfim)} .clara p.lead b{color:var(--tinta)}
.v,.rs{font-feature-settings:"lnum" 1;font-variant-numeric:lining-nums}
.foto{position:absolute;z-index:-1;inset:0;background-size:cover;background-position:center}
.rodape{position:absolute;left:96px;right:96px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:20px;letter-spacing:.18em;text-transform:uppercase}
.escura .rodape{color:var(--ouro-c)} .clara .rodape{color:var(--bronze)}
.rodape svg{width:34px;height:34px;vertical-align:middle;margin-left:10px}
.capa .foto{background-image:linear-gradient(180deg,rgba(31,26,23,.88) 0%,rgba(31,26,23,.35) 18%,rgba(31,26,23,.6) 40%,#1F1A17 62%),url(folder-limpeza.jpg);filter:saturate(.75)}
.capa .pag,.res .pag{background:rgba(31,26,23,.5);color:var(--marfim);border-color:rgba(244,235,221,.45)}
.capa .bf{margin-top:110px}
.capa .rot{margin-top:auto}
.capa h1{margin-top:16px;font-size:92px;line-height:1.02}
.preco{display:flex;align-items:flex-end;gap:22px;margin-top:6px}
.preco .rs{font-family:Cormorant;font-weight:600;font-size:96px;line-height:1;color:var(--ouro-c);margin-bottom:34px}
.preco .v{font-family:Cormorant;font-weight:600;font-size:300px;line-height:.8;background:var(--brilho);-webkit-background-clip:text;background-clip:text;color:transparent}
.escassez{margin:40px 0 170px;display:flex;flex-wrap:wrap;gap:14px}
.chip{display:inline-flex;align-items:center;gap:12px;padding:16px 26px;border-radius:99px;font-weight:700;font-size:28px;background:rgba(244,235,221,.08);border:1.5px solid rgba(217,188,134,.45);color:var(--marfim)}
.chip.forte{background:var(--brilho);color:var(--escuro);border-color:transparent}
.inc h2{margin-top:150px;font-size:118px}
.inc p.lead{margin-top:40px;max-width:860px}
.balao{margin-top:54px;display:grid;gap:18px}
.balao div{display:flex;align-items:center;gap:22px;padding:28px 32px;border-radius:30px;background:var(--papel);border:1.5px solid rgba(176,141,87,.3);font-weight:600;font-size:33px;box-shadow:0 18px 40px rgba(142,110,62,.1)}
.balao i{flex:none;width:62px;height:62px;border-radius:20px;background:linear-gradient(145deg,#FFF8EC,#EFDDBC);display:grid;place-items:center}
.balao svg{width:34px;height:34px}
.leve{margin-top:46px;font-weight:700;font-size:30px;color:var(--bronze)}
.res .foto{background-image:linear-gradient(180deg,rgba(247,241,232,.92) 0%,rgba(247,241,232,0) 16%,rgba(247,241,232,.15) 30%,rgba(247,241,232,.93) 52%,#F7F1E8 62%),url(folder-serum.jpg);background-position:center 30%;filter:saturate(.8)}
.res h2{margin-top:auto;font-size:116px}
.res p.lead{margin-top:30px;max-width:880px}
.res .lista{margin:40px 0 170px;display:flex;flex-wrap:wrap;gap:14px}
.res .lista span{padding:16px 26px;border-radius:99px;background:var(--papel);border:1.5px solid rgba(176,141,87,.3);font-weight:600;font-size:28px}
.conf h2{margin-top:auto;font-size:112px}
.conf .itens{margin-top:46px;display:grid;gap:16px}
.conf .itens div{display:flex;align-items:center;gap:24px;padding:26px 30px;border-radius:28px;background:rgba(244,235,221,.06);border:1.5px solid rgba(201,164,104,.3);font-size:31px;line-height:1.3}
.conf .itens b{color:var(--marfim)}
.conf .itens svg{flex:none;width:42px;height:42px}
.conf .frase{margin:40px 0 auto;font-family:"Great Vibes";font-size:56px;color:var(--ouro-c)}
.of .rot{margin-top:auto}
.of h2{margin-top:22px;font-size:112px}
.caixa{margin-top:44px;border-radius:40px;padding:40px 44px;background:rgba(244,235,221,.06);border:2px solid rgba(217,188,134,.5);box-shadow:0 30px 70px rgba(0,0,0,.4)}
.caixa .l1{display:flex;align-items:flex-end;gap:18px}
.caixa .l1 .v{font-family:Cormorant;font-weight:600;font-size:170px;line-height:.8;background:var(--brilho);-webkit-background-clip:text;background-clip:text;color:transparent}
.caixa .l1 .rs{font-family:Cormorant;font-weight:600;font-size:64px;color:var(--ouro-c);margin-bottom:18px}
.caixa .l1 small{margin-left:auto;margin-bottom:14px;font-weight:700;font-size:26px;color:var(--escuro);background:var(--brilho);padding:12px 20px;border-radius:99px;white-space:nowrap}
.caixa ul{list-style:none;margin-top:30px;display:grid;gap:14px}
.caixa li{display:flex;align-items:center;gap:18px;font-size:29px;color:rgba(244,235,221,.9)}
.caixa li svg{flex:none;width:34px;height:34px}
.zap{margin-top:40px;display:flex;align-items:center;justify-content:center;gap:20px;background:var(--wa);color:#fff;font-weight:800;font-size:35px;padding:30px;border-radius:99px;box-shadow:0 24px 50px rgba(31,175,90,.3)}
.zap svg{width:50px;height:50px}
.miudo{margin:22px 0 auto;padding-bottom:40px;text-align:center;font-size:22px;color:rgba(244,235,221,.6)}
'''.replace('F/', F)
def ic(path, cor='#D9BC86', w=1.8): return f'<svg viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'
OK='<path d="M5 12.5l4.5 4.5L19 7.5"/>'; CAL='<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>'
REL='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'; ESC='<path d="M12 3l7 3v5.5c0 4.4-3 8-7 9.5-4-1.5-7-5.1-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>'
PIN='<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'
PES='<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>'
GOTA='<path d="M12 3c3 4 6 7 6 10.5A6 6 0 0 1 6 13.5C6 10 9 7 12 3z"/>'; SOL='<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
CARTAO='<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/>'; SET='<path d="M5 12h14M13 6l6 6-6 6"/>'
WA='<svg viewBox="0 0 32 32"><path fill="#fff" d="M16 4.5a11.5 11.5 0 0 0-9.9 17.3L4.5 27.5l5.9-1.5A11.5 11.5 0 1 0 16 4.5zm6.7 16.1c-.3.8-1.6 1.6-2.3 1.7-1.1.2-1.9.1-4.2-.8-3.5-1.5-5.7-5-5.9-5.3-.2-.2-1.4-1.8-1.4-3.5s.9-2.5 1.2-2.9c.3-.3.7-.4.9-.4h.6c.2 0 .5-.1.8.6l1.1 2.5c.1.2.1.4 0 .6-.6 1.3-1.3 1.2-.9 1.9a9.4 9.4 0 0 0 4.7 4.1c.4.2.6.2.8-.1l1-1.3c.3-.4.5-.3.8-.2l2.3 1.1c.4.2.6.3.7.4.1.2.1.9-.2 1.6z"/></svg>'
def topo(n, cls): 
    logo = F + ('simbolo-claro-transp.svg' if cls=='escura' else 'simbolo-colorido.svg')
    return f'<div class="topo"><div class="marca"><img src="{logo}" alt="">STUDIO LA ROCHA</div><span class="pag">{n:02d} / 05</span></div>'
def rod(cls): return f'<div class="rodape"><span>@studiolarocha</span><span>Arraste{ic(SET, "#D9BC86" if cls=="escura" else "#9C7A45", 2)}</span></div>'
B='#9C7A45'
T = []
T.append(f'''<section class="t escura capa" id="t1"><div class="foto"></div>{topo(1,"escura")}
<span class="bf">BLACK FRIDAY 🖤</span>
<div class="rot">No Studio La Rocha</div>
<h1>2 limpezas de pele por</h1>
<div class="preco"><span class="rs">R$</span><span class="v">{e(PRECO)}</span></div>
<div class="escassez"><span class="chip forte">{e(txt_pac)}</span><span class="chip">Só até {e(PRAZO)}</span></div>
{rod("escura")}</section>''')
T.append(f'''<section class="t clara inc" id="t2">{topo(2,"clara")}
<h2>Sabe aquele <em>cravinho</em> que insiste?</h2>
<p class="lead">E a pele que chega pesada no fim do dia? Acontece com muita gente. 😉</p>
<div class="balao"><div><i>{ic(GOTA, B)}</i>Cravinho que volta sempre</div><div><i>{ic(SOL, B)}</i>Pele pesada e sem brilho</div></div>
<p class="leve">Dá pra cuidar disso com calma →</p>
{rod("clara")}</section>''')
T.append(f'''<section class="t clara res" id="t3"><div class="foto"></div>{topo(3,"clara")}
<h2>Pele <em>leve</em> e com viço</h2>
<p class="lead">A limpeza tira o que pesa: impurezas, cravinhos e células mortas. Você sai com a pele limpinha e um momento só seu.</p>
<div class="lista"><span>Pele mais limpa</span><span>Sensação de leveza</span><span>Mais viço</span></div>
{rod("clara")}</section>''')
T.append(f'''<section class="t escura conf" id="t4">{topo(4,"escura")}
<h2>Feita com <em>cuidado</em></h2>
<div class="itens">
<div>{ic(ESC)}<span>Pela <b>Amanda Rocha</b>, enfermeira</span></div>
<div>{ic(PES)}<span>Atendimento <b>só para mulheres</b></span></div>
<div>{ic(REL)}<span>Sem pressa, com técnica e biossegurança</span></div>
<div>{ic(PIN)}<span>No <b>Studio La Rocha</b>, em Mauá - SP</span></div>
</div>
<div class="frase">um momento só seu</div>
{rod("escura")}</section>''')
itens = [(CAL, txt_sab)] + ([(REL, f'2ª sessão até {VALIDADE_2A}')] if VALIDADE_2A else []) + [(OK, txt_pac.replace(' 🖤','')), (CARTAO, 'Pagamento no salão, no dia')]
lis = ''.join(f'<li>{ic(p)}{e(t)}</li>' for p,t in itens)
T.append(f'''<section class="t escura of" id="t5">{topo(5,"escura")}
<div class="rot">Black Friday · só até {e(PRAZO)}</div>
<h2>Bora cuidar da <em>pele</em>?</h2>
<div class="caixa"><div class="l1"><span class="rs">R$</span><span class="v">{e(PRECO)}</span><small>2 sessões · R$ {cada} cada</small></div><ul>{lis}</ul></div>
<div class="zap">{WA}Chama a Amanda no WhatsApp</div>
<div class="miudo">Toque em “Enviar mensagem” 👇</div>
</section>''')
open('carrossel.html','w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Black Friday · Studio La Rocha</title><style>{CSS}</style></head><body>' + '\n'.join(T) + '</body></html>')
print('ok |', txt_pac, '|', txt_sab, '|', VALIDADE_2A)
