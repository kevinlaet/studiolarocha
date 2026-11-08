// Gera os 3 posts de chamada (2160x2700) a partir de chamadas.html. Uso: node exportar-chamadas.cjs
const { chromium } = require('playwright');
const path = require('path');
const pecas = [['c1','chamada-1-auriculoterapia.png'],['c2','chamada-2-limpeza-de-pele.png'],['c3','chamada-3-manicure-e-pedicure.png']];
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'chamadas.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const [id, f] of pecas) await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', f) });
  await b.close();
})();
