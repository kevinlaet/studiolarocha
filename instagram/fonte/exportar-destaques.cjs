// Gera as capas dos destaques (1080x1920) a partir de destaques.html.
// Uso: node exportar-destaques.cjs   (salva na pasta acima desta, em capas-destaques/)
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
const capas = [['servicos', '1-Servicos'], ['precos', '2-Precos'], ['chegar', '3-Como-chegar'], ['agendar', '4-Agendar'], ['antes', '5-Antes-e-depois'], ['equipe', '6-Equipe'], ['regras', '7-Regras']];
(async () => {
  const saida = path.join(__dirname, '..', 'capas-destaques'); fs.mkdirSync(saida, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + path.join(__dirname, 'destaques.html'));
  for (const [id, nome] of capas) await p.locator('#' + id).screenshot({ path: path.join(saida, nome + '.png') });
  await b.close();
})();
