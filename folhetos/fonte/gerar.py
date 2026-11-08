# Gera folhetos.html (5 folhetos A5) a partir dos textos abaixo.
# Uso: python3 gerar.py && NODE_PATH=$(npm root -g) node exportar.cjs
# Textos de saúde: nada de prometer resultado. Itens "em breve" ainda não foram confirmados pela Sandra.
import segno
segno.make('https://studiolarocha.com.br/links/?de=folheto', error='h').save('qr-folheto.svg', scale=10, border=0, dark='#2B2622', light=None)

CSS = open('folhetos.css').read()
SP = '<span class="faisca" style="width:16px;height:16px;top:218px;right:74px"><svg viewBox="0 0 10 10"><path fill="currentColor" d="M5 0l1.2 3.8L10 5 6.2 6.2 5 10 3.8 6.2 0 5l3.8-1.2z"/></svg></span><span class="faisca" style="width:10px;height:10px;top:258px;right:118px;opacity:.6"><svg viewBox="0 0 10 10"><path fill="currentColor" d="M5 0l1.2 3.8L10 5 6.2 6.2 5 10 3.8 6.2 0 5l3.8-1.2z"/></svg></span>'
I = {
 'orelha': '<path d="M8 18c-2-2-3-4-3-7a7 7 0 0 1 14 0c0 3-2.5 4.5-4 6.5S13.5 21 11 21c-1.5 0-2.5-1-3-3z"/><path d="M9 11a3 3 0 0 1 6 0c0 2-2 2.5-2 4"/>',
 'gota': '<path d="M12 3c3 4 6 7 6 10.5A6 6 0 0 1 6 13.5C6 10 9 7 12 3z"/><path d="M9.5 14.5a2.6 2.6 0 0 0 2.5 2"/>',
 'lua': '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 'folha': '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19c3-5 6-8 10-10"/>',
 'faisca': '<path d="M12 2.5l1.8 5.7 5.7 1.8-5.7 1.8L12 17.5l-1.8-5.7L4.5 10l5.7-1.8z"/><path d="M19 15.5l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/>',
 'escudo': '<path d="M12 3l7 3v5.5c0 4.4-3 8-7 9.5-4-1.5-7-5.1-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>',
 'coracao': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 'esmalte': '<path d="M10 2.5h4v5h-4z"/><path d="M8.5 7.5h7a1 1 0 0 1 1 1V11h-9V8.5a1 1 0 0 1 1-1z"/><path d="M7 11h10l.6 8.2a2 2 0 0 1-2 2.3H8.4a2 2 0 0 1-2-2.3z"/>',
 'pe': '<path d="M9 3c2 0 3 1.5 3 4 0 2-1 3-1 5 0 2 1 3 1 6 0 2-1 3-3 3s-3-1.5-3-4c0-2 1-4 1-7 0-4 .5-7 2-7z"/><circle cx="15" cy="5" r="1.2"/><circle cx="17.5" cy="8" r="1.1"/><circle cx="18.5" cy="11.5" r="1"/>',
 'perfume': '<path d="M9 2.5h6v3H9z"/><path d="M7 8.5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2V19a2.5 2.5 0 0 1-2.5 2.5h-5A2.5 2.5 0 0 1 7 19z"/><path d="M10 12h4"/>',
 'laco': '<path d="M12 11c-3-4-8-4-8 0s5 4 8 0z"/><path d="M12 11c3-4 8-4 8 0s-5 4-8 0z"/><path d="M12 11l-3 9M12 11l3 9"/>',
 'sino': '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0"/>',
}
def ic(k, tema):
    c = '#E3C88F' if tema == 'escuro' else '#9C7A45'
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{I[k]}</svg>'
def item(k, t, h, p, tag=''):
    return f'<div class="item"><div class="ico">{ic(k,t)}</div><div><h3>{h}{tag}</h3><p>{p}</p></div></div>'
BREVE = '<em class="breve">em breve</em>'

F = [
 dict(id='auriculoterapia', tema='escuro', rotulo='Cuidado com a Amanda', h2='Auriculoterapia', script='com a enfermeira Amanda',
      lead='Técnica complementar feita em pontos da orelha, com o cuidado de quem é da área da saúde.',
      sub='Pode ajudar com', itens=[('lua','Sono','Mais tranquilidade para descansar.'),('folha','Ansiedade e estresse','Apoio para desacelerar a mente.'),('coracao','Dores e tensões do dia a dia','Um cuidado para o corpo relaxar.')],
      nota='Os resultados variam de pessoa para pessoa. A auriculoterapia não substitui tratamento médico.',
      assina='Só para mulheres · COREN-SP 617675'),
 dict(id='limpeza-de-pele', tema='claro', rotulo='Cuidado com a Amanda', h2='Limpeza de pele', script='um momento só seu',
      lead='Cuidado com a sua pele, com técnica, higiene e a atenção de uma enfermeira.',
      sub='Como é', itens=[('gota','Feita com técnica','Passo a passo com cuidado e sem pressa.'),('escudo','Biossegurança','Higiene e materiais de enfermagem.'),('coracao','Atendimento acolhedor','Para você sair mais leve e cuidada.')],
      nota='Atendimento com horário marcado. Pagamento só no salão.',
      assina='Só para mulheres · COREN-SP 617675'),
 dict(id='manicure-e-pedicure', tema='escuro', rotulo='Cuidado com a Sandra', h2='Manicure e Pedicure', script='caprichadas, do seu jeito',
      lead='Acabamento caprichado e atenção a cada detalhe, das mãos aos pés.',
      sub='O que você encontra', itens=[('esmalte','Manicure','Acabamento impecável, do jeitinho que você gosta.'),('pe','Pedicure','Cuidado e carinho para os seus pés.'),('faisca','Atenção em cada detalhe','Do começo ao fim do atendimento.')],
      nota='Para agendar, escaneie o QR code e escolha com quem e como.',
      assina='Com a Sandra · Studio La Rocha'),
 dict(id='massagem', tema='claro', rotulo='Novidade no Studio', h2='Massagem', script='para desacelerar',
      lead='Um espaço pensado para você parar um pouquinho e cuidar do corpo e da mente.',
      sub='Vem aí', itens=[('faisca','Um momento para você','Tempo de descanso, sem pressa.',''),('folha','Ambiente acolhedor','Um lugar feito com carinho.',''),('sino','Fique por dentro','Siga o perfil e ative o sininho.','')],
      nota='Em breve: horários e valores. Acompanhe no Instagram @studiolarocha.',
      assina='Novos serviços em breve', breve_h2=True),
 dict(id='produtos', tema='escuro', rotulo='Novidade no Studio', h2='Produtos', script='cuidados e mimos',
      lead='Além dos serviços, o Studio La Rocha vai ter produtos selecionados para você.',
      sub='Vem aí', itens=[('laco','Lingerie','Delicadeza e conforto no dia a dia.',''),('perfume','Perfumes','Para deixar a sua marca por onde passar.',''),('gota','Skincare','Produtos para cuidar da pele em casa.','')],
      nota='Em breve: lista e valores. Acompanhe no Instagram @studiolarocha.',
      assina='Novos produtos em breve'),
]
def pagina(n, f):
    t = f['tema']; mini = 'simbolo-claro-transp.svg' if t == 'escuro' else 'simbolo-colorido.svg'
    itens = ''.join(item(i[0], t, i[1], i[2], i[3] if len(i) > 3 else '') for i in f['itens'])
    selo = '<div class="selo"><i></i>Em breve</div>' if f['id'] in ('massagem','produtos') else ''
    return f'''<section class="folheto {t}" id="{f['id']}">
<i class="luz a"></i><i class="luz b"></i><div class="pontos"></div><div class="arco um"></div><div class="arco dois"></div>{SP}
<div class="topo"><div class="mini"><img src="{mini}" alt="">STUDIO LA ROCHA</div>{selo}</div>
<div class="rotulo">{f['rotulo']}</div>
<h2{' class="longo"' if len(f['h2'])>16 else ''}>{f['h2']}</h2>
<div class="script">{f['script']}</div>
<p class="lead">{f['lead']}</p>
<div class="sub">{f['sub']}</div>
<div class="itens">{itens}</div>
<p class="nota">{f['nota']}</p>
<div class="base">
  <div class="qr"><img src="qr-folheto.svg" alt=""></div>
  <div class="agende"><b>{'Fique por dentro' if f['id'] in ('massagem','produtos') else 'Agende pelo celular'}</b><span>{'Aponte a câmera para o QR code, siga o perfil e veja o que já está disponível para agendar.' if f['id'] in ('massagem','produtos') else 'Aponte a câmera para o QR code. Escolha com quem e como: online ou pelo WhatsApp.'}</span><small>Pagamento só no salão.</small></div>
</div>
<div class="rodape"><span>{f['assina']}</span><span>@STUDIOLAROCHA · MAUÁ - SP</span></div>
</section>'''
html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Studio La Rocha · Folhetos A5</title><style>{CSS}</style></head><body>' + '\n'.join(pagina(i, f) for i, f in enumerate(F)) + '</body></html>'
open('folhetos.html', 'w').write(html)
