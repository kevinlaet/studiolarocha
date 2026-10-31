// Gera os PNGs do Instagram a partir de posts.html.
// Uso: node exportar.cjs   (salva na pasta acima desta)
const { chromium } = require('playwright');
const path = require('path');

const pecas = [
  ['inauguracao', '1-postar-primeiro-inauguracao.png'],
  ['historia', '2-postar-segundo-nossa-historia.png'],
  ['chegamos', '3-postar-terceiro-chegamos.png'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
  await page.goto('file://' + path.join(__dirname, 'posts.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const [id, arquivo] of pecas) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', arquivo) });
  }
  await browser.close();
})();
