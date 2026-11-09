# Studio La Rocha — contexto do projeto (leia antes de mexer em qualquer coisa)

Este arquivo é a memória do projeto. Quem continuar o trabalho (Claude ou pessoa) deve ler tudo antes de agir e atualizar ao final de cada etapa.

## 1. Quem é quem
- **Kevin Laet** — marido da Amanda. Quem pede e decide. Está sempre atarefado: o objetivo é **economizar o tempo dele**. Fala português do Brasil, simples. Usa o celular (iPhone) e o app Claude.
- **Sandra** — dona do salão, mãe da Amanda, 52 anos, cabeleireira (corte, coloração) e manicure muito requisitada (inclusive desencravar unhas). Agenda lotada. Vai se dedicar 100% ao salão; no começo atendendo, depois só gerenciando. Instagram pessoal: @sandraaparecida5566. Ainda **não deu o e-mail** para o login do painel.
- **Amanda Rocha** — 29 anos, enfermeira (COREN-SP 617675), saúde mental, atende só mulheres (auriculoterapia e limpeza de pele). **Sócia com 50%** do salão **e** profissional solo, com site e marca próprios (amandarochabemestar.com.br). Instagram @amandarochaat.
- Ninguém tem dinheiro: sempre preferir soluções gratuitas/baratas (GitHub Pages, Supabase grátis, ntfy). Ainda faltam móveis, produtos e decoração. Tem 2 cadeiras de cabeleireiro, 1 maca, 1 lavatório, espelhos. Obra e pintura prontas.

## 2. O negócio
- Nome **sempre** "**Studio La Rocha**" ("Studio" sem acento; nunca Stúdio, Estudio, La Rocha Studio). Verificado: nenhum salão com esse nome encontrado.
- Local: **Vila Nova Mauá, Mauá - SP**. Endereço usado no cartão da Amanda: Rua Onivaldo Vanderlei Dionísio, 25 (confirmar com a Sandra antes de usar no salão). Salão com inauguração "em breve" (data não definida).
- Slogan: "Beleza, saúde e bem-estar". Serviços: Cabelo (corte e coloração), Unhas (manicure), Auriculoterapia e Limpeza de pele (Amanda). **Novos serviços em breve** (aparece nos posts).
- Modelo: o salão também **aluga cadeira/maca** para outras profissionais (parceiras). Contrato modelo existe como artifact; falta confirmar modelo de aluguel com a Sandra.
- Instagram do salão: **@studiolarocha** (134 seguidores em 08/11/2026; 3 posts ANTIGOS no ar — versão "Agendar/Saúde/Beleza 1-3 de 3" com "Chame no WhatsApp"; foto de perfil e bio já certas; link da bio já é `studiolarocha.com.br/links/?de=instagram`). Nome do perfil ainda "STUDIO LA ROCHA": trocar para "Studio La Rocha | Salão em Mauá".

## 3. Regras que nunca mudam
1. **Nunca inventar dados do salão** (serviços, preços, horários, endereço, datas, CNPJ). Perguntar.
2. **Nada vai a público/impressão sem aprovação por escrito da Sandra** (WhatsApp vale).
3. **Nunca pedir nem guardar senhas**, nem a Secret key / service_role do Supabase. Só a chave pública (`sb_publishable_…`) pode ficar no código.
4. **Pagamento só no salão.** Nunca Pix/sinal por mensagem (aviso fixo na página de links).
5. **Saúde:** não prometer resultado de procedimento. Anúncio de desencravar unha fica pendente de orientação da Vigilância Sanitária.
6. **Fotos de clientes** só com autorização escrita.
7. Linguagem **simples**, para a cliente mais leiga entender sozinha. Toda página termina com "Desenvolvido por Kevin Laet".
8. Qualidade acima de velocidade: a cliente deve pensar "que fofo, que capricho", mas continuar **fácil de usar**. Conferir no celular (largura ~390px) antes de entregar.
9. Não pedir ao Kevin o que dá para resolver sozinho; quando precisar dele, dar passo a passo curto, valores para copiar **separados**.
10. Não criar PR sem pedido. Não mexer no repo/Pages da Amanda (renomear/apagar quebra o QR dos 100 cartões já pedidos).

- **Textos a evitar:** nada que soe como emagrecer/corpo ("chegar mais leve", "secar", "perder peso"); o Kevin vetou "chegue nas festas mais leve". Preferir cuidado, momento seu, se cuidar.

## 4. Padrão visual (identidade)
- Cores: creme `#F7F1E8`, papel `#FFFCF7`, ouro `#B08D57` (claro `#D9BC86`, escuro `#8E6E3E`), bronze `#9C7A45`, tinta `#2B2622`, escuro `#1F1A17`, marfim `#F4EBDD`. Brilho dourado: `linear-gradient(100deg,#8E6E3E,#C9A468,#F1DEB4,#C9A468,#8E6E3E)`.
- Fontes (locais em `fonts/`): **Cormorant** (títulos, caixa alta com letter-spacing), **Great Vibes** (assinatura), **Montserrat** (texto).
- Logo: símbolo opção C (`img/simbolo.svg`) + nome. Foto de perfil redonda: versão "nome em arco" (já trocada), alternativa "nome reto".
- Estilo: elegante, quente, dourado/creme, vidro translúcido, animações suaves de entrada; ícones de linha em traço ouro; botões grandes.
- Posts Instagram: **2160x2700 (4:5)**, exportados com Playwright (`deviceScaleFactor: 2`). Nunca exportar em 1x.

## 5. Endereços (domínio próprio **studiolarocha.com.br**)
- Links (bio): `https://studiolarocha.com.br/links/?de=instagram`
- Agenda: `https://studiolarocha.com.br/agenda/` (`?p=sandra` ou `?p=amanda` abre direto na profissional)
- Profissionais: `…/profissionais/` (`?modo=online` ou `?modo=whatsapp`)
- Painel do salão: `https://studiolarocha.com.br/painel/`
- Amanda: `https://amandarochabemestar.com.br/` (QR dos cartões dela: `kevinlaet.github.io/AMANDA-ROCHA-AT/?o=cartao#agendar`, que redireciona).
- Origem da cliente via `?de=` (`instagram, facebook, google, cartao, cartaz, folheto, espelho, amanda, whatsapp`), ou detecção pelo navegador do Instagram/Facebook. Site da Amanda usa `?o=`. Os textos de WhatsApp sempre dizem de onde a cliente veio.
- **DNS (Registro.br → GitHub Pages):** A (Nome vazio = raiz) para 185.199.108.153, .109.153, .110.153, .111.153; CNAME `www` → `kevinlaet.github.io`. Nome "@" fica gravado literalmente e está errado. Modo básico trava o modo avançado por horas.
- **Regra:** em bio, cartões, QRs, cartazes e documentos usar SEMPRE o endereço **sem `www`** (`https://studiolarocha.com.br/...`). O `www` só existe para redirecionar quem digitar à mão.
- **Estado (confirmado pelo Kevin no celular):** domínio raiz abre com HTTPS ("Privado"): links, agenda e profissionais OK. O `www` ainda mostra aviso de certificado (GitHub emite sozinho em até algumas horas; se persistir: Settings > Pages > Remove e recolocar o domínio, depois Enforce HTTPS). Não bloqueia nada.
- Teste ao vivo não é possível da sessão (proxy bloqueia github.io e o domínio); pedir ao Kevin para testar no celular.

## 6. Repositórios
- `kevinlaet/studiolarocha` (branch `main`, publicado em GitHub Pages) — este repo. Clone local: `/home/user/studiolarocha`.
  - `links/` página de links; `profissionais/`; `agenda/` (agenda do salão); `painel/` (cópia do painel da Amanda com a marca do salão; **não editar** `index.html`, `painel.js`, manifesto — só `painel/marca.js`); `config.js`; `whatsapp/` (pacote WhatsApp Business); `instagram/` (posts, perfil, destaques, legendas em `LEIA-ME.txt`; `fonte/` gera os PNGs); `ferramentas/painel.mjs` (sincroniza o painel).
- `kevinlaet/AMANDA-ROCHA-AT` — site/painel/banco da Amanda (clone `/home/user/AMANDA-ROCHA-AT`). Banco em `supabase/schema.sql` e `atualizacao.sql` (idempotente). Painel em `admin/`. Testes em `tests/` (`npm test`, PGlite).
  - Trabalho recente está na branch `claude/new-session-gjqujs` (sessão de 24 h + desconexão imediata, cadastro de clientes, story, domínio no SQL, CLAUDE.md ponteiro; último commit e2e25d2). **Falta o Kevin abrir novo PR para `main` e mesclar** com os testes verdes.
- `kevinlaet/IA.RTS-Marketing-inteligente` — repositório irmão de marketing (branch de trabalho `claude/new-session-gjqujs`).
- Branch de trabalho nas sessões do app: `claude/new-session-gjqujs`; no `studiolarocha` o Kevin publica direto em `main`.

## 7. Arquitetura da agenda (resumo)
- **Um banco só** (Supabase da Amanda). Tabelas: `profissionais` (papel `socia`/`parceira`), `recursos` (maca, cadeira-1, cadeira-2, mesa-unhas), `horarios`, `servicos`, `clientes`, `historico`, etc. Colunas `profissional` com padrão `amanda`.
- Sócias (Amanda, Sandra) veem/mexem em tudo; parceiras só no que é delas (garantido por RLS no banco). Chave "Só a minha agenda / Todas as profissionais" no painel.
- **A maca (e cadeiras/mesa) trava** entre profissionais por trigger `checa_recurso` (`recurso_ocupado`).
- **Sessão do painel (decisão do Kevin):** login aberto por **24 horas**, pede a senha **uma vez por dia** (sem opção de 30 dias). Algo estranho **desconecta todos os aparelhos na hora**: (1) programa automático logado com a senha dela; (2) alerta grave novo do guardião de tipo `cancelamentos` ou `intruso` (só os que surgem depois do login; o que já existia não conta). Código em `painel.js` (`alertaNovo`, `acessoEstranho`); testes em `AMANDA-ROCHA-AT/tests`.
- Clientes: autocompletar nome ao enviar horários; cada profissional vê só as suas; depois de cadastrado, só sócias editam/excluem. E-mail lembrado no aparelho (senha pelo Chaveiro/Face ID; nunca guardada).
- A agenda da Sandra é lotada: **ela não vai manter horários livres no painel**. Por isso foi descartada a ideia do story automático "Horários livres" (fica só como código na branch da Amanda).
- Fluxo da página de links (atual): botões **Agendar online** (`profissionais/?modo=online` → "Ver horários" abre `agenda/?p=…`) e **Agendar pelo WhatsApp** (`?modo=whatsapp` → escolhe profissional e serviço → abre WhatsApp com saudação + resumo + origem).
- **Números de WhatsApp:** centralizados no objeto `ZAP` em `profissionais/index.html`. Amanda → (11) 94890-7302 (`5511948907302`). Sandra → número do salão (11) 96768-2546 (`5511967682546`), por enquanto o mesmo. Quando a Sandra tiver número próprio, trocar **só a linha `Sandra`** em `ZAP`; o número do salão também está em `config.js`, `links/index.html` (tiles de Cabelo/Unhas/aluguel, `data-wa`) e `links/studio-la-rocha.vcf`. O número do salão será convertido em WhatsApp Business.

## 8. Instagram do salão — estado
- **Posts refeitos (nov/2026)** porque a Amanda achou "as duas mulheres" sem sentido: agora diretos, sem texto sentimental. Ordem: 1 Apresentação (4 serviços + inauguração em breve), 2 Cabelo (Sandra), 3 Unhas (Sandra), 4 Saúde (Amanda), 5 Em breve (novos serviços e novas profissionais), 6 Agendar. Fonte: `instagram/fonte/feed.html`; gerar com `node exportar-feed.cjs` (2160x2700). Legendas em `instagram/LEIA-ME.txt`. Falta a Sandra e a Amanda aprovarem por escrito, e o Kevin postar. Não citar preço, horário, data, nem "desencravar unha" nos posts.
- **3 posts de chamada** (gancho para prender atenção; a Amanda posta): Auriculoterapia ("Cabeça a mil? Sono leve?"), Limpeza de pele ("Pele cansada?"), Manicure e pedicure. Fonte `instagram/fonte/chamadas.html`, `node exportar-chamadas.cjs`; legendas na seção 3a do LEIA-ME. Saúde: só "pode ajudar" + aviso; sem prometer resultado. Pedicure já é oferecida (sem selo "em breve").
- **Aviso de agenda da Amanda (nov/2026):** destaque em "Dezembro"; sábados 5 e 26 lotados, 12 e 19 com vagas (gatilho de escassez real, sem inventar); feed e story. Fonte `instagram/fonte/aviso-agenda.html` (lista `SABADOS` no topo do gerador, já gravada no HTML).
- **3 posts de dicas** (`dica-1-pele`, `dica-2-unhas`, `dica-3-sono`; fonte `fonte/dicas.html`, `node exportar-dicas.cjs`): conteúdo para salvar/compartilhar. Dicas só gerais; Amanda revisa pele e sono, Sandra revisa unhas.
- **Estratégia de vendas e crescimento:** `instagram/ESTRATEGIA.md` (5 tipos de post, ritmo, crescimento local, medição, o que não fazer). Seguir como guia de todo conteúdo novo.
- Bio: `Studio La Rocha | Salão em Mauá` / "Beleza, saúde e bem-estar ✨ / Cabelo · Unhas · Auriculoterapia · Limpeza de pele / Por @sandraaparecida5566 e @amandarochaat / 📍 Mauá - SP · Agende 👇". Trocar o link da bio e do WhatsApp Business para o domínio (HTTPS).
- Próximo passo estratégico: **dia de fotos** (Sandra + Amanda juntas, retratos individuais, espaço/cadeiras/lavatório/maca, vídeo curto de 10–15s) e então carrossel, Reels e destaques com foto. Perfil só com arte ainda parece "vazio".

## 8b. Folhetos A5 (`folhetos/`)
- 5 folhetos (um por destaque): Auriculoterapia, Limpeza de pele, Manicure e Pedicure, Massagem, Produtos. Gerar: `cd folhetos/fonte && python3 gerar.py && NODE_PATH=$(npm root -g) node exportar.cjs`. Saída: PNG A5 600 dpi (3494x4963) + `folhetos-a5.pdf` (feito dos PNGs com `python3 pdf.py`). QR → `studiolarocha.com.br/links/?de=folheto`.
- Itens ainda não confirmados levam selo "em breve" (massagem, produtos); pedicure já existe. Auriculoterapia usa só "pode ajudar" e o aviso "não substitui tratamento médico" (mesmo texto do site da Amanda).
- **Fora dos folhetos de propósito:** sex shop (regras do Meta e público do salão; só com decisão da Sandra, em versão discreta) e **Monjaro/tirzepatida** (medicamento de venda só com receita: proibido anunciar e vender fora de farmácia; risco para o COREN da Amanda).
- Nada vai para a gráfica sem aprovação por escrito da Sandra e da Amanda.

## 8c. Instagram: o que está no ar e o que fazer em seguida
- Estado real (screenshot do Kevin, 08/11): perfil com 3 posts antigos. Decisão recomendada: **arquivar** (não apagar) os 3 antigos e postar os 6 novos na ordem 1→6, no mesmo dia; fixar 1, 6 e 5.
- Arquivos prontos em `instagram/` (todos 2160x2700, exceto story 2160x3840): `1-postar-primeiro-apresentacao` … `6-postar-por-ultimo-agendar`; `chamada-1/2/3-*`; `dica-1-pele`, `dica-2-unhas`, `dica-3-sono`; `aviso-agenda-dezembro-feed` e `-story`. Legendas em `LEIA-ME.txt` (seções 3, 3a, 3c, 3d). Ordem sugerida: bloco 1 (6 posts), depois aviso de dezembro, depois chamadas e dicas alternando (um a cada 2–3 dias).
- Enviar à Sandra/Amanda **como documento** no WhatsApp (foto comprime). Aprovação por escrito antes de postar. Dicas: Amanda revisa pele e sono; Sandra revisa unhas. Aviso de dezembro: conferir que os sábados 12 e 19 estão abertos no painel; story com figurinha de link `https://studiolarocha.com.br/agenda/?p=amanda`.

## 8d. Decisões e preferências do Kevin (aprendidas no chat)
- Quer **qualidade alta** e que a cliente pense "que fofo, que capricho"; imagens sempre em alta resolução (reclamou quando saiu baixa). Prefere receber **imagens soltas** (PNG), enviadas no chat, a PDF.
- Quer respostas **curtas, em português simples**, com "seu lado" (o que ele precisa fazer) separado.
- Amanda não gostou do post "duas mulheres" (sem sentido): textos **diretos**, falando de serviços, novidades e como agendar.
- Vetou "chegue nas festas mais leve" (parece emagrecer). Ver regra em "Textos a evitar".
- Pedicure **já é oferecida** pela Sandra. Massagem e produtos (lingerie, perfumes, skincare) estão **em breve**. Sex shop e Monjaro **fora** de qualquer material (motivos em 8b). Se a Amanda for vender produtos de skincare, depende da decisão dela e de regras sanitárias; nada anunciado ainda.
- Login do painel: **24 h**, pede senha 1x por dia, e **fecha na hora** ao detectar algo estranho (decisão em 09/11/2026).
- Cartões de visita da Amanda (100 un.) já pedidos com QR antigo (`kevinlaet.github.io/AMANDA-ROCHA-AT/?o=cartao#agendar`): não apagar/renomear esse repo.
- O Kevin pode trocar de modelo (Sonnet/Opus) no meio da conversa; o trabalho não depende disso.

## 8e. Problemas conhecidos
- Teste automático `painel em 320px … numeros: quebrado em 2 linhas "1 atendimento · R$ 0"` (AMANDA-ROCHA-AT/tests/ponta-a-ponta.test.mjs) **já falhava antes** e continua: layout do quadro "Seus números" em tela de 320px. Todo o resto passa.
- PDF dos folhetos: o primeiro estava "bugado" para o Kevin; foi refeito a partir dos PNGs (`folhetos/fonte/pdf.py`). Se o Kevin reclamar de novo, mandar só os PNGs.
- `www.studiolarocha.com.br` ainda pode mostrar aviso de certificado (não bloqueia).
- Domínio e github.io não são acessíveis da sessão: sempre pedir teste no celular.

## 9. Pendências (atualizar sempre)
**Com o Kevin**
- DNS do Registro.br já ajustado (salvo com sucesso). Só conferir se o `www` ganhou certificado; trocar link da bio e do WhatsApp Business para o endereço sem `www`.
- Escanear o QR do cartão da Amanda e confirmar o redirecionamento.
- Abrir PR de `claude/new-session-gjqujs` → `main` (AMANDA-ROCHA-AT) e mesclar; rodar `atualizacao.sql` de novo no Supabase se preciso; conferir o painel da Amanda.
- **Instagram:** arquivar os 3 posts antigos, trocar o nome do perfil, postar os 6 novos (depois de aprovação escrita), depois aviso de dezembro, chamadas e dicas; trocar o link do WhatsApp Business para `…/links/?de=whatsapp` (o da bio já está certo).
- Enviar às duas as listas de perguntas; criar o acesso da Sandra quando vier o e-mail; combinar o **dia de fotos**.
- Próximos cartões (reimpressão futura): incluir endereço e o site da Amanda; QR direto no domínio (`amandarochabemestar.com.br/?o=cartao#agendar`; salão: `studiolarocha.com.br/links/?de=cartao`).

**Aguardando a Sandra:** serviços, preços e duração; horários de funcionamento; endereço e ponto de referência; data de inauguração; MEI/CNPJ/alvará/licença sanitária/contador; modelo de aluguel; e-mail do salão; decisão do WhatsApp Business / novo número dela; fotos; aprovação escrita dos posts.

**Aguardando a Amanda:** uso da maca (quais serviços), como usa o espaço, horários de sábado e fim da promoção de R$ 75, contrato/CNPJ, configurar ntfy, foto.

**Backlog do Claude:** consertar o teste de 320px; mensagem curta para o dia de fotos (Kevin ainda não respondeu se quer); cartão de visita e cartaz do salão com QR (ofereci; sem resposta); calendário de 4 semanas de conteúdo (ver `instagram/ESTRATEGIA.md`); fotos na página de profissionais; cartão de visita e cartaz do salão com QR; Google Perfil da Empresa; busca no INPI do nome; vale-presente e fidelidade (Amanda tem cartão de 5 carimbos); roteiros de vídeo; carrossel/Reels/destaques com fotos; follow-ups do contrato.

## 10. Como trabalhar aqui (checklist antes de entregar)
1. Ler este arquivo e o `README.md`.
2. Mudou o painel da Amanda? Rodar `node ferramentas/painel.mjs ../AMANDA-ROCHA-AT` e `--conferir`.
3. Mudou o banco? Atualizar `schema.sql` **e** `atualizacao.sql`, manter idempotente, rodar `npm test`.
4. Testar no navegador (Playwright), em largura de celular, e olhar as capturas.
5. Mudou número, endereço ou link? Procurar em todo o repo (`grep`) e trocar tudo, inclusive `.vcf`, `LEIA-ME.txt`, README.
6. Commit claro em português; push; avisar o Kevin com o que ele precisa fazer (se houver), sem jargão.
7. Atualizar a seção 9 deste arquivo.

Desenvolvido por Kevin Laet
