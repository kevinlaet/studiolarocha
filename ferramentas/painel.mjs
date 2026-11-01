// Monta o painel do salão (painel/) a partir do painel da Amanda: o mesmo código, com a cara do Studio La Rocha.
// Uso:
//   node ferramentas/painel.mjs [caminho do repositório AMANDA-ROCHA-AT]            -> atualiza painel/
//   node ferramentas/painel.mjs [caminho] --conferir                                -> só confere se painel/ está igual (sai com erro se não)
// O que é só do salão fica em painel/marca.js (escrito à mão, nunca sobrescrito).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const conferir = args.includes('--conferir');
const AMANDA = path.resolve(args.find((a) => !a.startsWith('--')) || path.join(RAIZ, '..', 'AMANDA-ROCHA-AT'));
const ler = (p) => fs.readFileSync(path.join(AMANDA, p), 'utf8');

function troca(texto, de, para) {
  if (!texto.includes(de)) throw new Error('não encontrei no painel da Amanda: ' + de.slice(0, 80));
  return texto.split(de).join(para);
}

let html = ler('admin/index.html');
html = troca(html, '<title>Agenda da Amanda</title>', '<title>Agenda do Studio La Rocha</title>');
html = troca(html, '<meta name="theme-color" content="#0B5F59">', '<meta name="theme-color" content="#1F1A17">');
html = troca(html, '<link rel="icon" href="../img/logo.svg" type="image/svg+xml">', '<link rel="icon" href="../img/simbolo.svg" type="image/svg+xml">');
html = troca(html, '<h1>Amanda Rocha</h1>', '<h1>Studio La Rocha</h1>');
html = troca(html, '<h1 id="cabNome">Amanda Rocha</h1>', '<h1 id="cabNome">Studio La Rocha</h1>');
html = troca(html, '<b>Bem-vinda, Amanda!</b>', '<b>Bem-vinda!</b>');
html = troca(html, '<script src="../agenda.js"></script>', '<script src="marca.js"></script>');
// cores do salão: dourado e marrom quase preto (as variáveis mantêm os nomes do painel da Amanda)
// os tons verde-azulados fixos do painel da Amanda viram os beges do salão (o verde de "confirmado" é de estado e fica)
const BEGES = { '#E9F4F1': '#F1E6D3', '#EEF7F5': '#F7F1E8', '#BFD9D4': '#E3D3BC', '#CFE5E0': '#E8D9C0', '#F1F8F6': '#F7F1E8', '#D5E9E5': '#EADBC3' };
for (const [de, para] of Object.entries(BEGES)) html = html.split(de).join(para);
html = troca(html, '</style>', `/* Studio La Rocha */
:root{--teal:#2B2622;--teal-d:#1F1A17;--peach:#C9A468;--peach-l:#F4EBDD;--cream:#F7F1E8;--sand:#EFE5D6;--ink:#2B2622;--muted:#6A6058;--line:#E3D3BC}
header h1{font-family:Cormorant,Georgia,serif;font-weight:600;font-size:20px;letter-spacing:.16em;text-transform:uppercase;color:var(--peach)}
</style>`);
html = troca(html, '<!doctype html>', '<!doctype html>\n<!-- Gerado por ferramentas/painel.mjs a partir do painel da Amanda. Não edite aqui: rode o script de novo. -->');

const manifesto = JSON.stringify({
  name: 'Agenda do Studio La Rocha', short_name: 'Agenda', start_url: './', scope: './', display: 'standalone',
  background_color: '#F7F1E8', theme_color: '#1F1A17', lang: 'pt-BR',
  icons: [
    { src: '../img/icone-192.png', sizes: '192x192', type: 'image/png', purpose: 'any maskable' },
    { src: '../img/icone-512.png', sizes: '512x512', type: 'image/png', purpose: 'any maskable' },
  ],
}, null, 2) + '\n';

const saida = { 'painel/index.html': html, 'painel/painel.js': ler('admin/painel.js'), 'painel/manifest.webmanifest': manifesto };
let diferentes = [];
for (const [arq, conteudo] of Object.entries(saida)) {
  const destino = path.join(RAIZ, arq);
  const atual = fs.existsSync(destino) ? fs.readFileSync(destino, 'utf8') : null;
  if (atual === conteudo) continue;
  diferentes.push(arq);
  if (!conferir) { fs.mkdirSync(path.dirname(destino), { recursive: true }); fs.writeFileSync(destino, conteudo); }
}
if (conferir) {
  if (diferentes.length) { console.log('Painel do salão desatualizado: ' + diferentes.join(', ') + '. Rode: node ferramentas/painel.mjs'); process.exit(1); }
  console.log('Painel do salão igual ao da Amanda.');
} else console.log(diferentes.length ? 'Atualizado: ' + diferentes.join(', ') : 'Nada mudou.');
