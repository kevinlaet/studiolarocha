# Studio La Rocha

Página de links do salão (para a bio do Instagram) e materiais de divulgação. Salão da Sandra em Mauá (SP).

| Pasta | O que é |
|---|---|
| `links/` | Página de links da bio: WhatsApp do salão, serviços, profissionais, salvar contato e compartilhar |
| `agenda/` | Agenda do salão: a cliente escolhe a profissional, o serviço, o dia e a hora, e reserva. `?p=sandra` já abre numa profissional; os links que o painel envia (`?dias=…&n=…&s=…`) mostram só os dias escolhidos |
| `painel/` | Painel do salão (Sandra e parceiras). É o painel da Amanda com a cara do salão: **não edite** `index.html`, `painel.js` nem o manifesto; o que é só do salão fica em `painel/marca.js` |
| `config.js` | Endereço do banco (Supabase, só a chave pública) e o WhatsApp do salão |
| `profissionais/` | Página "Nossas profissionais": Sandra e Amanda, com resumo, serviços e botões de agendar. As fotos entram em `img/sandra.jpg` e `img/amanda.jpg` (veja os comentários no HTML) |
| `index.html` | Leva direto para `links/` |
| `img/`, `fonts/` | Símbolo do logo (opção C) e as letras da marca |
| `whatsapp/` | Pacote do WhatsApp Business: perfil, saudação, ausência, respostas rápidas, etiquetas e catálogo (o que falta é preenchido pela Sandra) |
| `instagram/` | Foto de perfil, os 6 primeiros posts, legendas e bio (`LEIA-ME.txt`); a pasta `fonte/` gera os PNGs de novo |

## Agenda única: salão e Amanda no mesmo banco

A agenda do salão usa o **mesmo banco** da agenda da Amanda (Supabase). O que a Amanda muda no painel dela aparece na hora aqui, e vice-versa.

- **Sócias** (Amanda e Sandra) veem e mexem na agenda de todas. No painel, a chave **Só a minha agenda / Todas as profissionais** troca a visão.
- **Parceiras** veem e mexem só na própria agenda, clientes e números. Quem garante isso é o banco, não a tela.
- **A maca trava entre elas:** um serviço marcado como "usa a maca" impede outra profissional de usar a maca no mesmo horário. O mesmo vale para as cadeiras e a mesa de unhas.
- **Visualizar agenda como cliente:** botão no painel que abre a página `agenda/` como a cliente vê.

### Cadastrar uma profissional (a Sandra ou uma parceira)

1. No painel, uma sócia abre **Mais › Profissionais**, escreve o nome e o e-mail e escolhe **Sócia** ou **Parceira**. A Sandra já vem cadastrada; falta só o e-mail dela.
2. No Supabase: Authentication › Users › Add user › Create new user, com **o mesmo e-mail** e uma senha provisória, marcando **Auto Confirm User**.
3. Ela entra em `…/studiolarocha/painel/`, troca a senha em Mais › Minha conta e cadastra os serviços dela em Mais › Serviços e preços (com o que cada um usa do salão).

### Atualizar o painel do salão

O painel é o da Amanda (repositório AMANDA-ROCHA-AT, pasta `admin/`). Depois de mudar o painel lá:

```
node ferramentas/painel.mjs ../AMANDA-ROCHA-AT
```

`node ferramentas/painel.mjs ../AMANDA-ROCHA-AT --conferir` só confere se a cópia está igual.

## Colocar no ar (GitHub Pages)

Settings > Pages > Build and deployment: **Deploy from a branch**, branch `main`, pasta **/ (root)**.
O endereço fica `https://studiolarocha.com.br/links/`.

## De onde a cliente veio

Os botões do WhatsApp já abrem com a mensagem escrita, dizendo a origem ("Vim pelo Instagram do Studio La Rocha..."). A origem sai do endereço:

| Onde o link aparece | Endereço |
|---|---|
| Bio do Instagram | `…/links/?de=instagram` |
| Cartão de visita (QR) | `…/links/?de=cartao` |
| Cartaz (QR) | `…/links/?de=cartaz` |
| Espelho do salão (QR) | `…/links/?de=espelho` |
| Perfil no Google | `…/links/?de=google` |
| Perfil do WhatsApp Business | `…/links/?de=whatsapp` |
| Site da Amanda | `…/links/?de=amanda` |

Sem `?de=`, a página reconhece sozinha quando abre dentro do Instagram ou do Facebook; nos outros casos escreve "Vim pelo site do Studio La Rocha". Novas origens e textos ficam no `<script>` de `links/index.html` (`ORIGENS` e `MENSAGENS`).

## Antes de mudar alguma coisa

- O nome é sempre **Studio La Rocha** ("Studio" sem acento).
- Nada de dados do salão inventados: serviços, preços, horários e endereço só depois da Sandra confirmar.
- Os botões "Como chegar" e "Alugue sua cadeira ou maca" estão prontos e comentados em `links/index.html`: ligar quando o endereço e o contrato estiverem confirmados.
- O número do WhatsApp aparece em `links/index.html` e em `links/studio-la-rocha.vcf`. Se mudar, troque nos dois.

Desenvolvido por Kevin Laet
