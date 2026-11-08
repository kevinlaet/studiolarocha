// Gera os PNGs (A5, ~300 dpi) e o PDF com os 5 folhetos. Uso: node exportar.cjs (salva na pasta acima).
const { chromium } = require('playwright');
const path = require('path');
const ids = ['auriculoterapia', 'limpeza-de-pele', 'manicure-e-pedicure', 'massagem', 'produtos'];
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 700, height: 900 }, deviceScaleFactor: 3.125 });
  await page.goto('file://' + path.join(__dirname, 'folhetos.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const id of ids) await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', `folheto-${id}.png`) });
  await page.pdf({ path: path.join(__dirname, '..', 'folhetos-a5.pdf'), width: '148mm', height: '210mm', printBackground: true });
  await b.close();
})();
