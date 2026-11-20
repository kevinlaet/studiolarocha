// Story "Último horário do ano" (2160x3840). Uso: node exportar-story-ultimo-horario.cjs
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  const erros = []; page.on('requestfailed', r => erros.push(r.url()));
  await page.goto('file://' + path.join(__dirname, 'story-ultimo-horario.html'));
  await page.evaluate(() => document.fonts.ready);
  const fora = await page.evaluate(() => { const s = document.getElementById('ult').getBoundingClientRect();
    return [...document.querySelectorAll('#ult *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && (r.left < s.left - 1 || r.right > s.right + 1) && !e.classList.contains('luz') && !e.classList.contains('arco') && !e.classList.contains('pontos'); }).map(e => e.className || e.tagName); });
  const d = path.join(__dirname, '..', 'stories'); fs.mkdirSync(d, { recursive: true });
  await page.locator('#ult').screenshot({ path: path.join(d, 'story-ultimo-horario-12-12.png') });
  await b.close(); console.log(erros.length || fora.length ? 'PROBLEMA ' + JSON.stringify({ erros, fora }) : 'ok');
})();
