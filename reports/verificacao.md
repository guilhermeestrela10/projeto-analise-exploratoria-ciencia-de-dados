## Entrega das etapas 7 e 8 - 20/11/2026

Responsável informado: Guilherme Estrela. Guia em `docs/entrega_etapas_7_8.md`.
Reaproveitado o painel integrado, sem alterar suas métricas ou reatribuir as etapas anteriores.
Atualizados README, roteiro de apresentação e registro de assistência. Corrigida mensagem fixa do CLI
que declarava pendência autoral sem consultar o estado da revisão; o pipeline não avalia autoria.

Verificações executadas nesta sessão, Windows/Python 3.11:

- `.venv/Scripts/python.exe -m pytest -q`: **34 passed in 47.28s**.
  Inclui quatro páginas, filtro de UF, período, recorte vazio e integração com dados brutos.
- Após a alteração da mensagem do CLI, `-m pytest tests/test_pipeline.py -q`: **3 passed in 15.57s**.
- `scripts/executar_pipeline.py --input work/amostra_bruta --output work/entrega_7_8 --sem-graficos`:
  sucesso; **49 linhas, 41 colunas, 19.416 bytes, 47 despachos elegíveis**, última execução em **1,0 s**.
  A entrada contém 50 pedidos reais e registros relacionados. A saída é separada da base do painel.
- `pip check`: **No broken requirements found**.
- `compileall -q src scripts pages app.py tests`: sem erros; script do CLI recompilado após a mensagem.
- PDF existente conferido: **12 páginas**, nome Guilherme Estrela presente, referência “FINAL BOSS” ausente.
  Todas as páginas renderizadas com Poppler e inspecionadas em imagem de contato; sem cortes ou sobreposição observados.
- GitHub Actions do commit anterior `4aa1972cea1bfbc49472b356d283db893768f4b6`: concluído com sucesso,
  execução `44292660824`. Isso não é o resultado remoto do novo commit desta entrega.

O painel remoto não foi inspecionado visualmente nesta sessão; mantém-se a confirmação anterior do proprietário.
O líder deve reconciliar os arquivos se os colegas substituírem a base das etapas 1 a 6.
As seções seguintes preservam o histórico das revisões anteriores e suas datas.

## Revisão informada pelo solicitante em 18/11/2026

O solicitante confirmou nesta conversa que ele e o grupo revisaram o relatório. A versão do PDF foi
atualizada para refletir essa declaração, sem afirmar que a ferramenta acompanhou a revisão humana.
As indicações de assistência de IA e os registros anteriores foram preservados. A declaração de revisão
não equivale à aprovação da professora nem altera a origem dos textos ou comprova contribuições individuais.
O registro está em reports/revisao_equipe.json.

---

# Complementação dos textos como rascunho IA - 17/11/2026

- Por solicitação do usuário, o documento recebeu texto completo para conclusão técnica, contextualização e oito justificativas.
- A origem assistida por IA foi preservada; não foram inventadas reuniões, revisões ou pesquisas dos integrantes.
- PDF: 12 páginas, com todas as páginas renderizadas e revisadas visualmente; Parte A continua em uma página.
- Não restam os marcadores de campos vazios nas páginas do PDF. O marcador RASCUNHO IA identifica os complementos.
- Suíte completa executada: 34 passed in 36.60s. Verificador de entrega: cinco testes específicos passaram após ajustar as mensagens.
- O verificador mantém código 1 para rascunhos IA: texto preenchido não comprova atendimento às exigências de autoria humana.
- Referências técnicas são atribuídas à ferramenta. Não se afirma que a equipe realizou pesquisa bibliográfica não confirmada.

---

# Confirmação manual do proprietário - 17/11/2026

O proprietário confirmou nesta conversa que o painel abre em janela anônima, sem login, e que as três páginas funcionam. Essa é uma confirmação manual do proprietário; não representa inspeção visual independente da ferramenta nem teste manual de todos os filtros.

As pendências de autoria e validação da equipe permanecem.

---

# Link Community Cloud recebido - 17/11/2026

- URL fornecida pelo proprietário: https://wuevyectn67rbfng9xqssx.streamlit.app/
- Consultas a página inicial e rotas das três páginas responderam HTTP 200, com HTML da interface de carregamento do Community Cloud.
- O endpoint /_stcore/health também retornou HTML, e não a resposta de saúde do aplicativo. Não foi usado como prova de que o código está funcionando remotamente.
- A sessão de execução remota não foi confirmada pelo cliente de verificação. Não se afirma validação externa de indicadores, gráficos ou filtros.
- Confirmação recebida do proprietário: o painel abre em janela anônima, sem login, e as três páginas funcionam. Trata-se de verificação manual relatada pelo usuário; não foi atribuída à ferramenta.
- Os 33 testes locais/remotos do repositório e as demais pendências humanas permanecem conforme o histórico abaixo.

---

# Atualização final da segunda revisão - 17/11/2026

- Repositório público confirmado: https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados.
- Pushes confirmados; o histórico original do proprietário foi preservado.
- Código verificado remotamente no commit 39e54e6: https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/actions/runs/44185881745. Resultado: success.
- Suíte local atual: 33 testes passaram em 34,56 s. Dependências e sintaxe também verificadas.
- O primeiro CI falhou porque work/pytest dependia de um diretório pai ausente no clone; corrigido em pytest.ini para .pytest-tmp. O novo CI concluiu com sucesso em clone Linux limpo.
- O PDF foi estabilizado com invariant=1: entradas iguais geram os mesmos bytes, comprovado por teste de repetição.
- PDF atual: 11 páginas renderizadas e revisadas visualmente, com Parte A em uma página.
- Reprodução integral adicional: pipeline executado em 96,2 s, gerou CSV idêntico byte a byte ao final preservado.
- Amostra real nesta revisão: 49 linhas, 47 elegíveis, 0,2 s.
- As três respostas recebidas do solicitante foram integradas; ele autorizou correções factuais e os critérios TAD > 10%, nota < 3,8 e calendário/janela utilizados.
- Monitoramento: 1.171 vendedores na coorte de 05/08/2018 a 03/09/2018; média das notas únicas por pedido com peso 1; dias úteis de segunda a sexta sem feriados.
- Revisão independente da função de acompanhamento não encontrou bug concreto; cinco testes específicos passaram.
- A automação do navegador foi interrompida pela ferramenta por não conseguir confirmar a URL com segurança. Não houve publicação no Streamlit Community Cloud nem fabricação de link.
- Ainda não pronto para entrega: faltam justificativas reais do diário, conclusão técnica, pesquisas e validação dos demais integrantes, contribuições reais de todos e painel publicado.

---

# Histórico da primeira implementação

# Verificação técnica executada - 17/11/2026

Verificações realizadas automaticamente pelo Codex. **Não representam revisão humana dos integrantes.**
Pasta de trabalho: projeto CIENCIAS DE DADOS, aberto no VS Code e inicialmente vazio.
Documento oficial lido integralmente: 12 páginas, incluindo anexos A/B/C/D, rubrica e restrições de IA.

## Ambiente

- Windows, Python 3.11.9, ambiente virtual `.venv` dentro do projeto.
- Dependências principais fixadas em requirements.txt. Ambiente resolvido em ambiente.txt.
- `python -m pip check`: **No broken requirements found.**
- `python -m compileall -q src scripts pages app.py tests`: saída sem erros, código de saída 0.
- 21 arquivos Python inspecionados; todos possuem marcação `# [IA] registro N` correspondente ao uso_de_ia.md.

## Dados reais e integridade

Cinco CSVs originais obtidos pelo endpoint público Kaggle/Olist. Nenhum CSV fictício foi usado no resultado.
Os cinco hashes SHA-256 dos arquivos conferem com data/raw/proveniencia.json.
Geolocalização não foi extraída nem utilizada.

| Tabela | Linhas |
|---|---|
| orders | 99.441 |
| order_items | 112.650 |
| products | 32.951 |
| sellers | 3.095 |
| order_reviews | 99.224 |

Tabela final: **100.010 linhas, 41 colunas, 38.373.468 bytes**; abaixo do limite de 100 MB do trabalho.
SHA-256 do CSV: `af2422c07a4ddc54be5e687704161c3ba85d3736a4dc6e09f587d8fba50f29c5`.
Foram observados 98.666 pedidos distintos; 94.955 são elegíveis para despacho individual e 94.257 possuem nota elegível.
Essas contagens são evidências técnicas; não são respostas autorais às perguntas de negócio.

Foram executadas assertions na base completa: chave final única, quantidade de pares igual aos pares dos itens,
soma dos item_count igual a 112.650, somas de preço e frete iguais às dos originais, vendedores únicos nos pedidos
elegíveis, valores monetários finitos e intervalo MinMax válido. Todas passaram.
Merges validados por cardinalidade; nenhuma multiplicação indevida da tabela analítica foi observada.

## Pipeline e amostras

Comando completo executado após as correções:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/executar_pipeline.py
```

Última execução completa: **84,1 segundos**, CSV gerado e gráficos/evidências preparados. Tempo depende da máquina e carga.
Execuções anteriores completas: 101,3 e 66,3 segundos, com o mesmo tamanho final do CSV.

Amostra real para ensaio preservada em `work/amostra_bruta/`: 50 pedidos, 55 itens, 49 produtos,
44 vendedores e 51 avaliações. Todas as linhas vieram dos originais.

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/executar_pipeline.py --input work/amostra_bruta --output work/demonstracao --sem-graficos
```

Resultado executado: **49 linhas, 41 colunas, 19.416 bytes, 47 pedidos elegíveis, 0,4 segundo**.
O resultado ficou separado da base do painel. Um dos 50 pedidos não tinha item correspondente.

## Testes automatizados

Comando da primeira suíte completa documentada:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

**25 passed in 63.99s (0:01:03)**, código de saída 0. Saída preservada em pytest.txt.
Cobertura de comportamento: granularidade e valores agregados, avaliações únicas, multivendedor, datas ausentes/inválidas,
cronologia negativa, amostras vazias e constantes, chaves conflitantes, duplicatas exatas, colunas ausentes,
dimensões sem correspondência, prazo parcialmente ausente, notas/dinheiro inválidos, infinitos, vendedor desconhecido,
denominadores, filtros, zero elegíveis, quatro páginas, datas parciais e recorte vazio,
recortes reais de 50 pedidos/um pedido/nenhuma correspondência, dicionário completo, exportação, sensibilidade
ao menor/maior prazo e geração do PDF com Partes A/B/C.

As páginas foram testadas a partir de app.py, usando switch_page, como na navegação real do Streamlit.
As fixtures artificiais são exclusivas dos testes unitários. Testes integrados usam dados reais.
Temporários de testes futuros ficam em work/pytest, conforme pytest.ini.

## Notebook, painel e PDF

- `scripts/preparar_notebook.py` executou e salvou 19 células: 10 de código, todas com execution_count e sem saída de erro.
- Validação estrutural com nbformat passou. Notebook usa a mesma função preprocessar, não tratamentos manuais.
- Streamlit iniciado em localhost:8501. Endpoint `/_stcore/health`: HTTP **200**, corpo **ok**.
- Inspeção no navegador: inicial, navegação, ranking, avaliações e controles do cenário; indicadores legíveis e textos autorais pendentes visíveis.
- Testes AppTest confirmaram filtros UF/período/vendedor, recortes sem registros e inicialização das quatro páginas.
- PDF técnico gerado com **10 páginas**; todas renderizadas e revisadas visualmente, incluindo gráficos, tabelas, capa e partes autorais.
- Poppler emitiu avisos sobre fontes Symbol/ArialUnicode; a renderização foi produzida e não foram observados glifos faltantes ou sobreposição na revisão visual.
- No Windows, a execução do notebook emitiu RuntimeWarning do zmq/Proactor e utilizou thread seletora adicional; o notebook concluiu sem erros.

## Falhas encontradas e corrigidas

1. Leitura do PDF no terminal cp1252 gerou UnicodeEncodeError. Repetida integralmente com `python -X utf8`.
2. Agregação vazia inferia datetime em flag de prazos. Tipos foram explicitados antes da engenharia; teste vazio passou.
3. ReportLab não possui estilo Subtitle por padrão. Estilo foi criado explicitamente; teste de geração do PDF passou.
4. Valor monetário infinito passava pela validação e falhava no scaler. np.isfinite agora o transforma em ausência; teste passou.
5. Vendedor ausente era descartado pelo groupby e podia aparentar vendedor único. Grupo desconhecido é preservado,
   contagem inclui ausência e elegibilidade exige vendedor identificado. Testes parcial/totalmente desconhecido passaram.
6. Após incluir navegação comum, testes que abriam uma página isoladamente não encontravam app.py.
   O teste passou a usar o ponto de entrada e switch_page, reproduzindo a execução real; suíte completa passou.

Revisão independente somente leitura identificou os itens 4 e 5, e confirmou suas correções com assertions
adicionais para preço/frete infinitos e vendedor parcial/totalmente ausente. Não houve alterações pelo revisor.

## Estado de publicação antes da segunda etapa (histórico)

- Git local inicializado em main, **sem commits nem remoto**. Nenhum histórico de integrantes foi simulado.
- CLI GitHub: `gh auth status` informou ausência de login.
- Conector GitHub identificou conta `guilhermeestrela10`; busca pelo repositório solicitado retornou lista vazia.
  O conector disponível não oferece criação de repositórios. Nenhuma publicação remota foi feita.
- Streamlit Community Cloud aberto no navegador exibiu tela **Sign in**. Login e publicação pelo proprietário continuam pendentes.
- Autoria humana obrigatória: sumário executivo, justificativas do diário, respostas de negócio e conclusões.
- Confirmar frentes dos integrantes, revisar tecnicamente o trabalho, produzir commits reais e ensaiar demonstração.
- Teste em outro sistema operacional e execução remota no Community Cloud **não realizados**.
- Auditoria da rubrica em docs/auditoria_rubrica.md; não se afirma entrega integral enquanto autoria/publicação estiverem pendentes.
