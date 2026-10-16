**selfmade.**: um produto digital de R$ 500 (pagamento único) que entrega um sistema no Claude para criar stories, posts e reels de pequenos negócios. O deploy é feito automaticamente quando dado git Push.`artes/` é o diretório de exemplos fictícios para o site. IDEALIZACAO.md nao deve ser considerado no commit. O site deve seguir o padrão de Design minimalista suíço. 

`IDEALIZACAO.md` (briefing, público, decisões de marca) existe só localmente e está no `.gitignore`; leia-o antes de mudar posicionamento ou texto de venda. `.claude/` também é ignorado.

- Não inventar depoimentos, números, preços de concorrentes, prazos ou escassez. Nomes e dados das marcas de exemplo são fictícios e a página declara isso.

- .claude/launch.json define a config landing (Node, porta 5173, serve a raiz do projeto). Use preview_start com name: "landing". Acesse o novo preview sempre em /?v=<timestamp>#<id>
- A verificação é visual e por medidas: em 1280×800 todos os .panel devem ter offsetHeight 739 e em 375×812, 751; document.documentElement.scrollWidth deve ser igual a innerWidth (sem rolagem lateral).

Remoto `origin`: `https://github.com/joelrossatoita-cpu/selfmade` (público), branch `main`.
