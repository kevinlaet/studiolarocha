// Gera o lote de 15/11: 6 stories (2160x3840) e 3 carrosséis de 3 slides (2160x2700). Uso: node exportar-lote-1511.cjs
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
const out = path.join(__dirname, '..', 'lote-2026-11-15');
const st = { s1: 'story-1-esmalte', s2: 'story-2-mito-pergunta', s3: 'story-3-mito-resposta', s4: 'story-4-dia-so-seu', s5: 'story-5-quiz-auriculo', s6: 'story-6-sabados-amanda' };
const car = { a: 'carrossel-unhas-festas', b: 'carrossel-cuidados-cor', c: 'carrossel-sabado-amanda' };
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'lote-1511.html'));
  await page.evaluate(() => document.fonts.ready);
  fs.mkdirSync(path.join(out, 'stories'), { recursive: true });
  for (const [id, nome] of Object.entries(st)) await page.locator('#' + id).screenshot({ path: path.join(out, 'stories', nome + '.png') });
  for (const [k, nome] of Object.entries(car)) {
    fs.mkdirSync(path.join(out, nome), { recursive: true });
    for (let i = 1; i <= 3; i++) await page.locator('#' + k + i).screenshot({ path: path.join(out, nome, `${i}.png`) });
  }
  await b.close();
})();
