// Gera o aviso de agenda da Amanda (feed 2160x2700 e story 2160x3840). Uso: node exportar-aviso-agenda.cjs
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'aviso-agenda.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.locator('#agenda-feed').screenshot({ path: path.join(__dirname, '..', 'aviso-agenda-dezembro-feed.png') });
  await page.locator('#agenda-story').screenshot({ path: path.join(__dirname, '..', 'aviso-agenda-dezembro-story.png') });
  await b.close();
})();
