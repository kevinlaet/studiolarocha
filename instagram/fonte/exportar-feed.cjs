// Gera os 6 posts do feed a partir de feed.html (2160x2700).
// Uso: node exportar-feed.cjs   (salva na pasta acima desta)
const { chromium } = require('playwright');
const path = require('path');
const pecas = [
  ['p1', '1-postar-primeiro-apresentacao.png'],
  ['p2', '2-postar-segundo-cabelo.png'],
  ['p3', '3-postar-terceiro-unhas.png'],
  ['p4', '4-postar-quarto-saude.png'],
  ['p5', '5-postar-quinto-em-breve.png'],
  ['p6', '6-postar-por-ultimo-agendar.png'],
];
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'feed.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const [id, arquivo] of pecas) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', arquivo) });
  }
  await browser.close();
})();
