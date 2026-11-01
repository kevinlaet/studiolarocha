# Studio La Rocha

Página de links do salão (para a bio do Instagram) e materiais de divulgação. Salão da Sandra em Mauá (SP).

| Pasta | O que é |
|---|---|
| `links/` | Página de links da bio: WhatsApp do salão, serviços, profissionais, salvar contato e compartilhar |
| `profissionais/` | Página "Nossas profissionais": Sandra e Amanda, com resumo, serviços e botões de agendar. As fotos entram em `img/sandra.jpg` e `img/amanda.jpg` (veja os comentários no HTML) |
| `index.html` | Leva direto para `links/` |
| `img/`, `fonts/` | Símbolo do logo (opção C) e as letras da marca |
| `instagram/` | Foto de perfil, os 6 primeiros posts, legendas e bio (`LEIA-ME.txt`); a pasta `fonte/` gera os PNGs de novo |

## Colocar no ar (GitHub Pages)

Settings > Pages > Build and deployment: **Deploy from a branch**, branch `main`, pasta **/ (root)**.
O endereço fica `https://kevinlaet.github.io/studiolarocha/links/`.

## De onde a cliente veio

Os botões do WhatsApp já abrem com a mensagem escrita, dizendo a origem ("Vim pelo Instagram do Studio La Rocha..."). A origem sai do endereço:

| Onde o link aparece | Endereço |
|---|---|
| Bio do Instagram | `…/links/?de=instagram` |
| Cartão de visita (QR) | `…/links/?de=cartao` |
| Cartaz (QR) | `…/links/?de=cartaz` |
| Espelho do salão (QR) | `…/links/?de=espelho` |
| Perfil no Google | `…/links/?de=google` |
| Site da Amanda | `…/links/?de=amanda` |

Sem `?de=`, a página reconhece sozinha quando abre dentro do Instagram ou do Facebook; nos outros casos escreve "Vim pelo site do Studio La Rocha". Novas origens e textos ficam no `<script>` de `links/index.html` (`ORIGENS` e `MENSAGENS`).

## Antes de mudar alguma coisa

- O nome é sempre **Studio La Rocha** ("Studio" sem acento).
- Nada de dados do salão inventados: serviços, preços, horários e endereço só depois da Sandra confirmar.
- Os botões "Como chegar" e "Alugue sua cadeira ou maca" estão prontos e comentados em `links/index.html`: ligar quando o endereço e o contrato estiverem confirmados.
- O número do WhatsApp aparece em `links/index.html` e em `links/studio-la-rocha.vcf`. Se mudar, troque nos dois.

Desenvolvido por Kevin Laet
