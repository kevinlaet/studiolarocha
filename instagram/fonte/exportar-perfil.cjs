// Gera as fotos de perfil redondas a partir de perfil.html.
// Uso: node exportar-perfil.cjs   (salva na pasta acima desta)
const { chromium } = require('playwright');
const path = require('path');

const pecas = [
  ['reto-claro', 'perfil-A-nome-reto-claro.png'],
  ['reto-escuro', 'perfil-A-nome-reto-escuro.png'],
  ['arco-claro', 'perfil-B-nome-em-arco-claro.png'],
  ['arco-escuro', 'perfil-B-nome-em-arco-escuro.png'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1200 } });
  await page.goto('file://' + path.join(__dirname, 'perfil.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const [id, arquivo] of pecas) {
    await page.locator('#' + id).screenshot({ path: path.join(__dirname, '..', arquivo) });
  }
  await browser.close();
})();
