# Olist — análise exploratória de vendedores

Análise exploratória sobre atrasos, avaliações e critérios de acompanhamento de vendedores parceiros. Projeto acadêmico do Grupo 04, com painel Streamlit e uso de IA declarado.

[![Testes](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/actions/workflows/testes.yml/badge.svg?branch=main)](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/actions/workflows/testes.yml)

[Painel](https://wuevyectn67rbfng9xqssx.streamlit.app/) · [Instalação](#instalação-no-vs-code) · [Apresentação](docs/apresentacao.md) · [Registro de IA](uso_de_ia.md)

**Escopo:** análise descritiva. A tabela analítica tem uma linha por pedido-vendedor; avaliações de pedidos multivendedor não são atribuídas individualmente. Limitações, proveniência, conclusões e responsabilidades da equipe estão documentadas abaixo e nos relatórios.

## Contexto acadêmico e autoria

Centro Universitário Santo Agostinho (UNIFSA) - Bacharelado em Engenharia de Software.
Disciplina: Ciência de Dados. Professora: Heloisa Guimarães. Grupo 04, Briefing 5: Gestão de Vendedores Parceiros.

**Versão revisada conforme declaração do solicitante em 18/11/2026:** o solicitante informou que ele e o grupo revisaram o relatório.
Sumário e respostas vieram do solicitante, com revisão factual autorizada. Implementação e complementos
receberam assistência de IA, cuja origem permanece registrada. A revisão informada não constitui
aprovação da professora nem altera as exigências de autoria do documento da disciplina.
O GitHub e o painel estão publicados. O proprietário confirmou acesso anônimo, sem login, e funcionamento das três páginas.

## Integrantes e responsabilidades

| Integrante | Responsabilidade informada nesta conversa |
|---|---|
| Guilherme Estrela | Etapa 7: Streamlit. Etapa 8: documentação, apresentação e verificação integrada |
| David Gabriel | Distribuição das etapas 1 a 6 a alinhar com o líder |
| Carlos Gabriel Raposo | Distribuição das etapas 1 a 6 a alinhar com o líder |
| Roger | Distribuição das etapas 1 a 6 a alinhar com o líder |

Entrega específica de Guilherme: [etapas 7 e 8](docs/entrega_etapas_7_8.md).
O projeto integrado inclui as dependências das etapas anteriores; isso não atribui sua execução a Guilherme.

Todos devem compreender o projeto e fazer contribuições e commits reais. Commits com código assistido devem incluir `[IA]`.

## Briefing e perguntas

"A marca é nossa, mas quem despacha é o vendedor. Desconfio que alguns poucos parceiros estão prejudicando a reputação da plataforma inteira. Preciso de critérios objetivos antes de conversar com eles."

1. Quais vendedores mais atrasam o despacho dos pedidos?
2. Vendedores que atrasam recebem avaliações piores?
3. Que critérios objetivos a empresa poderia usar para acompanhar ou advertir vendedores?

Fonte: [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
Referência de avaliação: `FINAL BOSS - TRABALHO CIENCIA DE DADOS.pdf`, 12 páginas, consultado em 17/11/2026.
Prazo: **30/11/2026, 23h59 de Brasília**. Apresentação: **02/12/2026**, até 10 minutos.

## Instalação no VS Code

Abra esta pasta pelo menu Arquivo > Abrir Pasta. Python recomendado: **3.11**.
O ambiente `.venv` local foi preparado, mas deve ser recriado em outro computador.
No terminal PowerShell, a partir da raiz:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

Não é necessário ativar o ambiente. Selecione `.venv` como interpretador no VS Code.
Linux/macOS: substitua `.\.venv\Scripts\python.exe` por `./.venv/bin/python`.

## Dados e pipeline

São usados somente cinco CSVs: orders, order_items, products, sellers e order_reviews.
O arquivo geolocation não é extraído nem utilizado. Os CSVs originais ficam fora do Git.
O download público foi obtido em 17/11/2026; a proveniência e hashes estão em `data/raw/proveniencia.json`.
Caso precise obter novamente, use uma pasta sem CSVs existentes:

```powershell
.\.venv\Scripts\python.exe scripts/baixar_dados.py
.\.venv\Scripts\python.exe scripts/executar_pipeline.py
```

Se o Kaggle exigir login, baixe os cinco arquivos pelo navegador e coloque-os em `data/raw/`.
O downloader preserva arquivos já presentes e não usa credenciais no código.
O pipeline gera o CSV final e evidências em `reports/`. Campos autorais existentes não são sobrescritos.

Para a amostra bruta fornecida pela professora, coloque **os cinco arquivos com nomes e colunas originais** numa pasta própria:

```powershell
.\.venv\Scripts\python.exe scripts/executar_pipeline.py --input data/amostra_bruta --output work/demonstracao --sem-graficos
```

Uma amostra real de 50 pedidos já foi preparada localmente em work/amostra_bruta/. Para ensaiar agora, use --input work/amostra_bruta no comando acima.

O resultado da demonstração fica separado da base usada pelo painel. Pastas com espaços devem ser colocadas entre aspas.
Dimensões e avaliações podem estar vazias, desde que mantenham os cabeçalhos.
Amostras independentes podem não conter pedidos em comum; nesse caso o CSV fica vazio, sem inventar correspondências.

Interface Python reutilizável:

```python
from src.load_data import load_data
from src.preprocessing import preprocessar
orders, items, products, sellers, reviews = load_data()
tabela = preprocessar(orders, items, products, sellers, reviews)
evidencias = tabela.attrs['audit']
```

## Painel

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Abra o endereço local mostrado no terminal. As quatro páginas usam exclusivamente
`data/processed/tabela_analitica.csv` para dados. `reports/conclusoes_equipe.json` contém apenas textos autorais.
Filtros de UF, vendedor e período afetam indicadores, gráficos e tabelas.
O filtro de volume limita o ranking, não os indicadores gerais da página.
A página de critérios é um simulador exploratório, sem recomendar advertências automaticamente.
Após as definições aprovadas pelo solicitante, essa página também acompanha TAD > 10%, nota média < 3,8
e tempo até despacho em dias úteis (segunda a sexta, sem feriados). Usa a coorte de compras nos últimos
30 dias até a última compra do recorte filtrado. Cada pedido elegível avaliado tem peso 1.
Não foi definido um limite automático para o tempo médio. Valores e parâmetros continuam exigindo avaliação humana.

## Organização

```text
app.py                         Página inicial
pages/                         Três perguntas do briefing
src/load_data.py               Carga dos originais
src/preprocessing.py           Função preprocessar e merges validados
src/feature_engineering.py     Datas, indicadores, codificação e escalas
src/analysis.py                Métricas, filtros e seleção de atributos
src/visualizations.py          Gráficos compartilhados
src/dashboard.py               Interface comum das páginas
src/reporting.py               Evidências, dicionário e saídas
scripts/                       Pipeline, download, notebook e relatório
notebooks/                     Análise exploratória executável
tests/                         Casos sintéticos e recortes reais
data/raw/                      Originais locais; não versionar CSVs
data/processed/                CSV final e metadados para publicar
reports/                       Relatório técnico, evidências e campos humanos
docs/                          Plano, apresentação, publicação e auditoria
uso_de_ia.md                   Registro conforme Anexo D
```

## Tratamentos e limites das métricas

- A chave final é `(order_id, seller_id)`. Itens são agregados antes de juntar as dimensões. Merges usam `validate='many_to_one'`.
- Duplicatas exatas são removidas. Chaves conflitantes geram erro compreensível; não se escolhe uma linha arbitrária.
- Datas inválidas tornam-se `NaT`; valores monetários negativos tornam-se ausentes; notas fora de 1 a 5 ficam ausentes.
- Não se imputam datas, notas ou atrasos. UF inválida vira `SEM_INFORMACAO`; categoria ausente vira `sem_categoria`.
- Valores monetários infinitos também viram ausências. Itens sem vendedor são preservados em grupo desconhecido e ficam fora da comparação individual.
- O menor prazo entre os itens é a referência conservadora. O maior prazo também é preservado. Grupos com algum prazo ausente não são elegíveis.
- `comparacao_prazos.csv` mede o efeito de trocar menor pelo maior prazo. `alternativas_ausencias.csv` mede quantas linhas seriam perdidas ao excluir qualquer nulo por tabela.
- Despacho atrasado: transportadora após o prazo, com precisão de segundos. Dias = segundos / 86400.
- Elegibilidade: um vendedor **observado**, status delivered/shipped, compra <= aprovação <= despacho, prazo >= aprovação e prazo válido em todos os itens.
- A taxa divide atrasos por pedidos elegíveis, sem transformar desconhecidos em pontuais. Pedidos canceled/unavailable ficam preservados, fora dessa taxa.
- Atraso na entrega ao cliente usa dias civis: entregar no dia prometido não conta como atraso.
- Notas negativas são 1 ou 2. Uma avaliação por pedido: última resposta válida no tempo, com desempate determinístico por ID, nota e comprimento do comentário.
- Nota média e taxa negativa individuais usam pedidos elegíveis com nota. O painel compara os dois grupos de atraso e mostra denominadores.
- A data de entrega à transportadora pertence ao pedido, não ao vendedor. Mesmo com vendedor único ela é uma aproximação, sem comprovar responsabilidade.
- Pedidos multivendedor ficam fora da comparação individual. Notas repetidas nessas linhas não podem ser somadas como avaliações independentes.
- Em amostras com itens incompletos, o número de vendedores pode estar subestimado. Nenhum pipeline recupera vendedores que não foram fornecidos.
- Valores comercializados são preços dos itens; não representam faturamento líquido e podem incluir pedidos não concluídos. Consultar status antes de uso financeiro.
- Outliers são sinalizados pelo IQR; medidas originais permanecem nos indicadores. Clipping, MinMax, Z-score e one-hot ficam em colunas `demo_`.
- Escalas e cercas são ajustadas ao lote recebido. Valores normalizados não devem ser comparados entre execuções independentes.
- Seleção por propósito, baixa variância e correlação está em `reports/selecao_atributos.json`. Correlações não provam causalidade.
- As quatro técnicas principais de engenharia são: diferenças de datas, indicadores condicionais, agregações por grupo, extração temporal. Há também razão frete/valor e categoria por frequência.
- Textos de avaliações passam por NFKC, minúsculas e espaços simples; somente seu comprimento é exportado. Não se faz análise de sentimento.

## Verificações e reprodução

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m compileall -q src scripts pages app.py tests
.\.venv\Scripts\python.exe scripts/preparar_notebook.py
.\.venv\Scripts\python.exe scripts/gerar_relatorio.py
```

O primeiro teste integrado lê a base real e cria um recorte coerente de 50 pedidos; o segundo usa um pedido e um recorte sem correspondências.
Os dados sintéticos existem somente em testes unitários. Não são usados no CSV final nem nos gráficos.
Testes do painel requerem o CSV gerado. Evidências da execução: `reports/verificacao.md`.
Dependências principais têm versões fixas; `reports/ambiente.txt` registra todas as instaladas no ambiente testado.

## Conclusões, publicação e entrega

Para conferir os campos autorais ainda vazios, execute:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/verificar_entrega.py
```

Esse comando aponta pendências textuais e retorna código 1 enquanto existirem campos não preenchidos.
Ele não comprova autoria, aprovação humana ou publicação. O detalhamento da segunda revisão está em `docs/revisao_final.md`.
O workflow GitHub Actions executa testes a cada push. Os resultados e suas datas estão em `reports/verificacao.md`.
As próximas alterações feitas pelo assistente devem seguir o fluxo testar, revisar, commit e push registrado em AGENTS.md.

As três respostas foram fornecidas pelo solicitante e receberam revisão factual expressamente autorizada. Os originais estão em `reports/respostas_recebidas.md`; os textos integrados estão no painel e na Parte A. O solicitante informou em 18/11/2026 que ele e o grupo revisaram o relatório. Os complementos assistidos e a declaração de revisão permanecem registrados em `uso_de_ia.md` e `reports/revisao_equipe.json`.
Desafios técnicos: granularidade de itens/avaliações, ausência de despacho por vendedor, múltiplas avaliações, cronologias contraditórias e amostras incompletas.
Consultar `docs/apresentacao.md`, `docs/publicacao.md` e `docs/auditoria_rubrica.md`.

Repositório público: [projeto-analise-exploratoria-ciencia-de-dados](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados). Nome: `projeto-analise-exploratoria-ciencia-de-dados`.
Painel Streamlit Community Cloud: [Abrir painel](https://wuevyectn67rbfng9xqssx.streamlit.app/). O proprietário confirmou abertura sem login em janela anônima e funcionamento das três páginas.
O CSV deve ficar abaixo de 100 MB. O pipeline verifica esse limite e não remove linhas para reduzi-lo.
Para o envio do grupo: conferir a versão consolidada, as contribuições reais dos integrantes e enviar o PDF
e os links do GitHub e do painel pela plataforma A da disciplina. Consultar o roteiro em `docs/apresentacao.md`.

## Referências técnicas consultadas

[Pandas - merges](https://pandas.pydata.org/docs/user_guide/merging.html),
[Streamlit - testes](https://docs.streamlit.io/develop/concepts/app-testing),
[Scikit-Learn - pré-processamento](https://scikit-learn.org/stable/modules/preprocessing.html).
Consultas de APIs de Pandas e Streamlit realizadas com Context7 em 17/11/2026.

Atualização de publicação: repositório público sincronizado. O proprietário informou o painel https://wuevyectn67rbfng9xqssx.streamlit.app/ A consulta HTTP respondeu, mas retornou a interface de carregamento do serviço; indicadores, gráficos e filtros remotos ainda não foram confirmados por esta ferramenta.

## Confirmação manual de publicação

O proprietário confirmou nesta conversa que o painel abre em janela anônima, sem login, e que as três páginas funcionam. Essa é uma confirmação manual do proprietário; não representa inspeção visual independente da ferramenta nem teste manual de todos os filtros.

## Navegação pelo repositório

- `app.py` e `pages/`: entrada e páginas do painel.
- `src/`: carregamento, preparação, análise e visualização.
- `scripts/`: pipeline, notebook, relatório e verificação de entrega.
- `data/`: proveniência e tabela processada.
- `notebooks/`: análise exploratória.
- `reports/`: evidências, gráficos e relatório final.
- `docs/`: apresentação, publicação e revisões.
- `tests/`: testes automatizados.
- `uso_de_ia.md`: registro da assistência, incluindo esta organização.
