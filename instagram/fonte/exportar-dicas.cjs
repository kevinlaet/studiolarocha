// Gera os 3 posts de dicas (2160x2700) a partir de dicas.html. Uso: node exportar-dicas.cjs
const { chromium } = require('playwright');
const path = require('path');
const pecas = [['d1','dica-1-pele.png'],['d2','dica-2-unhas.png'],['d3','dica-3-sono.png']];
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'dicas.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const [id, f] of pecas) await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', f) });
  await b.close();
})();
