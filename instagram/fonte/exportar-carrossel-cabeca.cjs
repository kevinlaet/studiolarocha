// Gera o carrossel "Cabeça a mil" (7 slides 2160x2700). Uso: node exportar-carrossel-cabeca.cjs
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'carrossel-cabeca.html'));
  await page.evaluate(() => document.fonts.ready);
  const d = path.join(__dirname, '..', 'carrossel-cabeca-a-mil'); fs.mkdirSync(d, { recursive: true });
  for (let i = 1; i <= 7; i++) await page.locator('#k' + i).screenshot({ path: path.join(d, `cabeca-a-mil-${i}.png`) });
  await b.close();
})();
