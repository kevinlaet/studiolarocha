// Exporta a semana de 23/11: carrosséis (2160x2700) e stories (2160x3840), conferindo fontes, imagens e sobreposições.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const out = path.join(__dirname, '..', 'semana-2026-11-23');
const pecas = { a1: 'carrossel-A-depois-da-sessao/1', a2: 'carrossel-A-depois-da-sessao/2', a3: 'carrossel-A-depois-da-sessao/3',
  b1: 'carrossel-B-sua-pele-respira/1', b2: 'carrossel-B-sua-pele-respira/2', b3: 'carrossel-B-sua-pele-respira/3',
  s1: 'stories/1-segunda-quem-cuida', s2: 'stories/2-terca-3-sinais', s3: 'stories/3-quarta-enquete', s4: 'stories/4-quinta-como-e-a-limpeza',
  s5: 'stories/5-sexta-novembro-lotou', s6: 'stories/6-sabado-tem-horario', s7: 'stories/7-domingo-r75' };
(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport: { width: 1200, height: 2100 }, deviceScaleFactor: 2 });
  const falhas = []; page.on('requestfailed', r => falhas.push(r.url()));
  await page.goto('file://' + path.join(__dirname, 'semana-2311.html')); await page.evaluate(() => document.fonts.ready);
  const prob = await page.evaluate(() => {
    const A = [];
    for (const s of document.querySelectorAll('section.p')) {
      const R = s.getBoundingClientRect();
      for (const e of s.querySelectorAll('h1,h2,p,.vidro,.chip,.rot,.foto,.txt')) { if (e.classList.contains('foto') && /left:0/.test(e.getAttribute('style') || '')) continue; const r = e.getBoundingClientRect(); if (r.width && (r.left < R.left + 30 || r.right > R.right - 30)) A.push(s.id + ' fora da moldura: ' + (e.className || e.tagName)); }
      const limite = s.classList.contains('s') ? (s.querySelector('.toque').getBoundingClientRect().top - 24) : (s.querySelector('.rodape').getBoundingClientRect().top - 20);
      const cta = s.querySelector('.cta'); const ctaTop = cta ? cta.getBoundingClientRect().top - 16 : Infinity;
      for (const e of s.querySelectorAll('.conteudo > *, section > div[style] > *')) { if (e.closest('.cta') || e.classList.contains('cta')) continue; const r = e.getBoundingClientRect(); if (r.height && r.bottom > Math.min(limite, ctaTop) && !e.classList.contains('foto')) A.push(s.id + ' encosta embaixo: ' + (e.className || e.tagName) + ' ' + Math.round(r.bottom - R.top)); }
      const alvo = s.querySelector('.alvo[style]'); if (alvo) { const a = alvo.getBoundingClientRect(); for (const e of s.querySelectorAll('.conteudo > *')) { const r = e.getBoundingClientRect(); if (r.bottom > a.top - 10) A.push(s.id + ' encosta na enquete'); } }
    }
    return A;
  });
  for (const [id, nome] of Object.entries(pecas)) { const f = path.join(out, nome + '.png'); fs.mkdirSync(path.dirname(f), { recursive: true }); await page.locator('#' + id).screenshot({ path: f }); }
  await b.close(); console.log(falhas.length || prob.length ? 'PROBLEMAS ' + JSON.stringify({ falhas, prob: [...new Set(prob)] }, null, 1) : 'Tudo certo: 13 peças, nada fora do lugar.');
})();
