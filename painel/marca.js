// O que é só do Studio La Rocha no painel (o resto é o mesmo código do painel da Amanda).
window.PAINEL = {
  titulo: 'Agenda do Studio La Rocha',
  // onde a cliente agenda: o botão "Visualizar agenda como cliente" e os links enviados levam para cá
  agenda: '../agenda/',
  arquivoImagem: 'horarios-studio-la-rocha.png',
  imagem: {
    logo: '../img/simbolo.svg', titulo: 'Studio La Rocha', sub: 'BELEZA  ·  SAÚDE  ·  BEM-ESTAR', rodape: 'PAGAMENTO SÓ NO SALÃO',
    fundo: ['#3A2F27', '#2B2622', '#1F1A17'], destaque: '#C9A468', claro: '#F4EBDD', papel: '#F7F1E8', tinta: '#2B2622', pilula: '#2B2622',
    linha: 'rgba(201,164,104,.22)', rodapeTxt: 'rgba(244,235,221,.8)'
  }
};
// serviços de reserva (o banco manda os de verdade) e o WhatsApp do salão, para a imagem de horários
window.AGENDA = { servicos: [], whatsapp: (window.SALAO && window.SALAO.whatsapp) || '5511967682546' };
