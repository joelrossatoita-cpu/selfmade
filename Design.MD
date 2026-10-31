# Design.MD — selfmade.

Guia de design da página de vendas da selfmade. Valores medidos na página (`estilo.css` e `index.html`) em 1280×800 (desktop) e 375×812 (celular). Estilo: minimalista suíço (grade clara, muito espaço em branco, uma só família de fonte, bordas finas).

---

## 1. Briefing

**O que é.** A selfmade é um produto digital de **R$ 500, pagamento único**. Entrega um sistema que cria stories, posts e reels para pequenos negócios, na cara da marca de cada cliente. O cliente conta o que vende e como quer ser visto, pede o conteúdo e recebe a arte pronta, sem precisar saber design.

**Para quem.**
- Pequeno empreendedor, dono do próprio negócio, de **25 a 40 anos**.
- Negócios de serviço local, loja, profissional autônomo ou marca própria.
- **Pouca intimidade com tecnologia.** A maior objeção é achar que não vai saber usar. A ponte: "se você manda mensagem no WhatsApp, consegue usar".
- Usa o celular para tudo.
- **Medo:** gastar dinheiro e continuar com um perfil amador.
- **Desejo:** um perfil que passe credibilidade e pareça de empresa grande.
- **Hoje:** o marketing dele tem design fraco. Contratar agência é caro, e fazer sozinho custa tempo ou fica genérico.
- **Não é o cliente** quem quer passar 100% do trabalho para outra pessoa. A selfmade não é agência, e a página deixa isso claro.

**A virada.** De "meu perfil parece amador" para "minha empresa parece grande, e fui eu que fiz", gastando muito menos do que pagaria a uma agência.

**Como falar.** Linguagem simples, como uma conversa. Tom direto, confiante, frases curtas. Nada de promessa de "viralizar". Sem jargão: dizer "a cara da sua marca", "modelo", "cores", "letras", "mais clientes", e não "identidade visual", "template", "paleta", "tipografia", "engajamento", "conversão". Não citar "Claude" nem "IA" no discurso principal.

**Objetivo da página.** Captar esse público e convencê-lo a usar a selfmade, **sempre conduzindo para a venda**. Cada seção termina em um caminho para o CTA (`#preco`). Estrutura: Início → Como funciona → Exemplos → Preço → FAQ.

**Limites de conteúdo.** Não inventar depoimentos, números, preços de concorrentes, prazos ou escassez. Marcas de exemplo são fictícias e a página declara isso.

---

## 2. Cores

Tema creme com verde-tinta. A seção "Como funciona" inverte (fundo escuro). Nunca usar cor fora desta tabela.

| Cor | Hex | Variável | Onde usa | Onde NÃO usa |
|---|---|---|---|---|
| Creme | `#F3EFE6` | `--bg`, `--cream` | Fundo da página, do cabeçalho e das seções claras. Texto e botão dentro da seção escura. | Não é cor de destaque. Não usar como texto sobre o fundo creme. |
| Verde-tinta | `#13241C` | `--ink`, `--line` | Texto principal, bordas de 1px, bordas do cartão do Preço. Fundo da seção escura. | Não usar em botões de CTA. Não usar como fundo de seções claras. |
| Verde | `#1E6B47` | `--accent` | **Fundo do botão de CTA**, ponto final dos títulos, números "01 —", link ativo do índice, marcador do título, pontos do passo a passo. | **Nunca** fora dos itens listados ao lado. Não usar em textos corridos. Ver "Não fazer". |
| Mostarda | `#D98E04` | `--cta` | **Somente** a sombra dura dos botões (4px 4px; 3px 3px no botão pequeno). | Não usar como fundo, texto ou borda. |
| Cinza-verde | `#5b6a62` | `--muted` | Textos secundários: respostas do FAQ, descrição dos passos, notas, legendas, índice inativo. | Não usar em títulos nem em texto de venda principal. |
| Creme escuro | `#E9E4D8` | `--soft` | Caixa de contato do FAQ e fundo de miniaturas. | Não usar como fundo de seção inteira. |
| Verde-claro | `#7FD1A1` | `--accent` na seção escura | Números e pontos dentro de "Como funciona" (substitui o verde). | Não usar em seções claras (falta contraste). |
| Cinza-claro | `#A9B8AE` | `--muted` na seção escura | Texto secundário dentro de "Como funciona". | Não usar em seções claras. |
| Linha clara | `rgba(243,239,230,.35)` | `--line` na seção escura | Bordas dentro de "Como funciona". | Não usar em seções claras. |

---

## 3. Fonte

**Família única: Inter Tight** (pesos 400, 500, 600; fallback `system-ui, sans-serif`). Peso **500** é o padrão da página; 600 só em destaques pontuais (logo e valores em negrito); 400 só em texto de apoio.

### Os três tamanhos

| Papel | Desktop | Celular | Peso | Entrelinha | Espaçamento entre letras |
|---|---|---|---|---|---|
| **Título** (h1 do Início) | 62 px (teto 68 px) | 35 px | 500 | .94 | -.045em |
| **Título** (h2 das demais seções) | 64 px | 34 px | 500 | .98 | -.04em |
| **Subtítulo** (lead) | 19 px | 17 px (15 px no Início) | 400 | 1,5 | normal |
| **Texto corrido** (body) | 17 px | 17 px | 400 | 1,5 | normal |

Apoio (não são um dos três níveis): rótulo de seção "01 — …" 14 px / 500; legendas e notas 12 a 15 px; pergunta do FAQ 19 px (desktop) / 17 px (celular), peso 500.

### Proporção título : subtítulo : texto

- **Desktop:** 64 : 19 : 17, ou seja, **≈ 3,4 : 1,1 : 1**. O título tem **3,4 vezes** o tamanho do subtítulo.
- **Celular:** 34 : 17 : 17, ou seja, **2 : 1 : 1**. O título tem **2 vezes** o do subtítulo.
- **Regra:** o título nunca fica abaixo de **2× o subtítulo** (celular) nem de **3,4× o subtítulo** (desktop).

### Quando usar cada um

- **Título:** uma ideia por seção, em no máximo 15 caracteres de largura por linha, terminando em ponto verde (`.`). É a primeira coisa que o olho lê.
- **Subtítulo:** logo abaixo do título, explica o ganho em uma ou duas frases curtas. Largura máxima 520 px.
- **Texto corrido:** detalhes, respostas do FAQ, descrições. Nunca como primeira informação de uma seção.

---

## 4. Espaçamento

Toda medida vem de poucas variáveis, definidas em um só lugar (`:root`). Não criar valores soltos.

### 4.1 Variáveis-base

| Variável | Celular | Desktop | Uso |
|---|---|---|---|
| `--gut` | 20 px | 40 px | Margem lateral da página |
| `--pt` | 24 px | 40 px | Espaço do topo da seção até o conteúdo |
| `--pb` | 76 px | 40 px | Espaço do conteúdo até o fim da seção |
| `--r1` | 12 px | 16 px | Ritmo curto: rótulo → título → subtítulo |
| `--r2` | 24 px | 32 px | Ritmo longo: título → conteúdo, conteúdo → CTA |
| largura máx. | 1240 px | 1240 px | Largura do conteúdo, centralizado |

No celular, o `--pb` de 76 px reserva espaço para a barra fixa de compra (R$ 500 + botão) no rodapé. Não reduzir.

### 4.2 Altura

| Elemento | Desktop | Celular |
|---|---|---|
| **Cabeçalho** | 61 px (60 + 1 de borda) | 61 px |
| **Cada seção** (`.panel`) | 739 px | 751 px |
| Regra da seção | altura da tela − 61 px, no mínimo | idem |

- A altura das 5 seções é igual. Conferir sempre: 739 px em 1280×800 e 751 px em 375×812.
- Sem rolagem lateral: `scrollWidth` igual a `innerWidth`.

### 4.3 Páginas de conteúdo (Como funciona, Exemplos, FAQ)

Padrão a seguir em qualquer seção nova:

| Trecho | Desktop | Celular |
|---|---|---|
| Topo da seção → rótulo "0X —" | 40 px | 24 px |
| Rótulo → título | 16 px | 12 px |
| Título → subtítulo | 16 px | 12 px |
| Título/subtítulo → conteúdo | 32 px | 24 px |
| Conteúdo → fim da seção | 40 px | 76 px |
| Linha de separação entre seções | 1 px | 1 px |

Itens de lista (FAQ, passos): 13 a 15 px acima e abaixo de cada item no desktop; 11 a 13 px no celular, com filete de 1 px entre eles.

### 4.4 Páginas de CTA (Início e Preço) — espaçamento próprio

As duas têm a mesma margem lateral e a mesma altura de seção das outras, mas o miolo é diferente.

**Início (landing)**
- **Sem rótulo numérico.** O bloco de texto fica centralizado na vertical (começa a ~213 px do topo no desktop).
- Título (h1) → subtítulo: 16 px (desktop) / 12 px (celular).
- Subtítulo → linha de botões: **32 px** (desktop) / **24 px** (celular).
- Entre os dois botões: 16 px.
- Padding de baixo no celular: **24 px** (não 76 px), porque o leque 3D ocupa o rodapé.
- Texto limitado a 600 px de largura. O leque 3D fica à direita.

**Preço** (vitrine + cartão)
- Rótulo "03 — Preço", título (h2, uma linha no desktop), subtítulo e, abaixo, duas colunas.
- Desktop: **11 fr : 9 fr** com **40 px** entre elas. Esquerda: grade de **8 artes de exemplo** (4 por linha, 8 px entre elas, proporção 4:5) e a legenda "Marcas de exemplo, todas fictícias.". Direita: cartão com borda de 1 px (`--line`), sem fundo, padding `--r2`.
- Celular: uma coluna com **18 px** entre vitrine e cartão. A vitrine mostra **3 artes** (as demais ficam ocultas) e o cartão tem padding de 16 px.
- Cartão: preço "R$ 500" no tamanho do título + "pagamento único" (19 px desktop / 15 px celular, cinza-verde) → lista de 3 respostas com filete de 1 px (sem mensalidade e sem renovação; 7 dias de garantia; "se você manda mensagem no WhatsApp, consegue usar") → botão de CTA, com `--r2` (desktop) / `--r1` (celular) de espaço acima.
- Lista: 14 px acima e abaixo de cada item no desktop, 8 px no celular.
- Sem calculadora, sem slider e sem barras. Nenhum verde no cartão além do botão e do ponto do título.

### 4.5 Botão de CTA — altura de referência

A **landing (Início)** define a altura do botão de CTA.

| Botão | Altura | Padding | Fonte |
|---|---|---|---|
| **CTA da landing (referência), desktop** | **59,5 px** | 16 px × 28 px | 17 px, peso 500 |
| CTA da landing, celular | 56,5 px | 16 px × 14 px | 15 px, peso 500 |
| CTA pequeno (cabeçalho e barra fixa) | 42,5 px | 9 px × 16 px | 15 px |

Sombra dura de 4 px 4 px em mostarda (3 px no botão pequeno). Sem cantos arredondados.

---

## 5. Não fazer

1. **Nunca use a cor do botão de CTA (`#1E6B47`, verde) para outras atividades que não sejam o CTA.** Ela já aparece em detalhes menores (ponto dos títulos, números, marcador), e esses usos não podem crescer. Nenhum botão secundário, aviso ou fundo de bloco em verde. Para ações secundárias, usar o botão "ghost" (texto cinza-verde, sem fundo).
2. **O título nunca deve ficar menor que a proporção dada:** no mínimo 2× o subtítulo no celular e 3,4× no desktop (64 px contra 19 px). Não reduzir o título para "caber" mais texto; cortar o texto.
3. **Nunca deixe o botão de CTA fora da altura que está na landing page:** 59,5 px no desktop e 56,5 px no celular, com o mesmo padding e a mesma fonte.
4. **Nunca mude a fonte utilizada.** A família é sempre a Inter Tight, nos pesos 400, 500 e 600, em toda a página. Não adicionar outra família, nem para títulos, botões ou detalhes.

Regras de apoio, vindas do projeto:
- Não usar a mostarda fora da sombra do botão.
- Não inserir valores de espaçamento fora das variáveis da seção 4.1.
- Não usar jargão, nem prometer "viralizar" (ver briefing).
- Não inventar depoimentos, números, prazos ou escassez.
