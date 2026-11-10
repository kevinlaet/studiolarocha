// Gera os stories (2160x3840) e o carrossel (2160x2700) a partir de stories-carrossel.html.
// Uso: node exportar-stories-carrossel.cjs  (salva em ../stories e ../carrossel-checklist)
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
const st = ['s1-1','s1-2','s1-3','s2-1','s2-2','s2-3'], car = ['k1','k2','k3','k4','k5','k6'];
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'stories-carrossel.html'));
  await page.evaluate(() => document.fonts.ready);
  const d1 = path.join(__dirname, '..', 'stories'), d2 = path.join(__dirname, '..', 'carrossel-checklist');
  fs.mkdirSync(d1, { recursive: true }); fs.mkdirSync(d2, { recursive: true });
  const nomes = { 's1-1': 'story1-tela1-enquete', 's1-2': 'story1-tela2-auriculoterapia', 's1-3': 'story1-tela3-link-agenda', 's2-1': 'story2-tela1-caixinha', 's2-2': 'story2-tela2-enquete', 's2-3': 'story2-tela3-link-whatsapp' };
  for (const id of st) await page.locator('#' + id).screenshot({ path: path.join(d1, nomes[id] + '.png') });
  for (const [i, id] of car.entries()) await page.locator('#' + id).screenshot({ path: path.join(d2, `checklist-${i + 1}.png`) });
  await b.close();
})();
