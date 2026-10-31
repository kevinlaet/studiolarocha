// Gera os 3 posts do que o salão oferece a partir de servicos.html.
// Uso: node exportar-servicos.cjs   (salva na pasta acima desta)
const { chromium } = require('playwright');
const path = require('path');

const pecas = [
  ['agendar', '4-postar-quarto-agendar.png'],
  ['saude', '5-postar-quinto-saude.png'],
  ['beleza', '6-postar-por-ultimo-beleza.png'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
  await page.goto('file://' + path.join(__dirname, 'servicos.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const [id, arquivo] of pecas) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', arquivo) });
  }
  await browser.close();
})();
