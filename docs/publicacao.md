# Publicação e entrega

## GitHub

Repositório público: https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados.
O primeiro envio foi confirmado; a branch local `main` acompanha `origin/main`.
Código, notebook, requirements.txt, documentação, CSV final, metadados e PDF técnico já estão no GitHub.
Não versionar `.venv`, dados brutos, textos livres de avaliações, credenciais, caches ou work/.
O PDF oficial é referência da disciplina; não é necessário redistribuí-lo em repositório público.

Usar mensagens com `[IA]` quando houver código assistido. Cada integrante deve fazer sua própria contribuição real.
Não compartilhar credenciais nem simular commits dos colegas.

Para próximas alterações, revisar os arquivos antes de selecionar o que será enviado:

```powershell
git status --short
git add caminho/do/arquivo
git diff --cached --stat
git commit -m "[IA] descrever a alteração feita"
git push
```

Conferir o conteúdo staged antes do commit: somente os arquivos listados na auditoria devem entrar.
O assistente recebeu instrução para testar, revisar, criar commit e fazer push a cada conjunto de alterações feitas por ele.
Essa regra está em AGENTS.md. Não foi instalado um serviço que envie arquivos editados fora das sessões.
O CSV final ultrapassa o limite comum de upload pelo navegador; usar Git para enviar o arquivo de 38,37 MB.

## Streamlit Community Cloud

1. Entrar com a conta autorizada em https://share.streamlit.io/.
2. Conectar o repositório público e selecionar a branch publicada.
3. Arquivo principal: `app.py`. Versão Python: `3.11` nas configurações avançadas.
4. Manter `requirements.txt` na raiz e `data/processed/tabela_analitica.csv` versionado.
5. Não executar download nem pipeline na inicialização do painel; os dados já devem estar no CSV final.
6. Abrir o link publicado em janela anônima. Visitar quatro páginas e testar UF, vendedor, período e recorte vazio.
7. Inserir links reais no README e manter o painel acessível até a apresentação de 02/12/2026.

## Relatório e envio

O PDF possui texto completo, com indicação de rascunho. A Parte A e as respostas do painel foram integradas
a partir dos textos do solicitante, com correções factuais autorizadas. As justificativas da Parte C,
a conclusão técnica e a contextualização foram completadas pela ferramenta como rascunho IA para estudo.
A autoria humana exigida pelo documento da disciplina e a validação dos demais integrantes continuam pendentes.
Completar `reports/secoes_autorais.md`, `reports/diario_de_decisoes.md` e `reports/conclusoes_equipe.json`.
Gerar novamente o PDF e revisar todas as páginas. A ferramenta incorpora os arquivos humanos existentes.
Na plataforma A da disciplina, enviar PDF, link GitHub e link Streamlit até **30/11/2026, 23h59 de Brasília**.

Não há links fictícios. O estado efetivamente verificado de autenticação/publicação fica em `reports/verificacao.md`.

Referências verificadas: [GitHub CLI - criar repositório](https://cli.github.com/manual/gh_repo_create), [limites de arquivos no GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) e [deploy no Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).

## Link do painel informado pelo proprietário

[Abrir painel](https://wuevyectn67rbfng9xqssx.streamlit.app/). O proprietário confirmou nesta conversa que o painel abre em janela anônima, sem login, e que as três páginas funcionam. Essa é uma confirmação manual do proprietário; não representa inspeção visual independente da ferramenta nem teste manual de todos os filtros.

## Revisão informada pelo solicitante em 18/11/2026

O solicitante confirmou nesta conversa que ele e o grupo revisaram o relatório. A versão do PDF foi
atualizada para refletir essa declaração, sem afirmar que a ferramenta acompanhou a revisão humana.
As indicações de assistência de IA e os registros anteriores foram preservados. A declaração de revisão
não equivale à aprovação da professora nem altera a origem dos textos ou comprova contribuições individuais.
O registro está em reports/revisao_equipe.json.
