# Entrega das etapas 7 e 8 - Guilherme Estrela

Grupo 04 - Briefing 5: Gestão de Vendedores Parceiros. Responsável confirmado pelo solicitante em 20/11/2026.
Implementação e documentação assistidas conforme o registro 8 de `uso_de_ia.md`.

## O que está sendo entregue

### Etapa 7 - Painel Streamlit

| Parte | Arquivo | Comportamento |
|---|---|---|
| Entrada | `app.py` | Visão geral, navegação e indicadores do recorte |
| Pergunta 1 | `pages/1_Atrasos_no_Despacho.py` | Ranking com volume mínimo e evolução mensal dos atrasos |
| Pergunta 2 | `pages/2_Atrasos_e_Avaliacoes.py` | Notas com e sem atraso, dispersão entre vendedores e recorte por atraso ao cliente |
| Pergunta 3 | `pages/3_Criterios_para_Vendedores.py` | Monitoramento dos últimos 30 dias e simulador de limiar e volume |
| Interface comum | `src/dashboard.py` | Filtros de UF, vendedor e período; tabelas, gráficos e download do recorte |
| Cálculos e figuras | `src/analysis.py`, `src/visualizations.py` | Métricas recalculadas após filtros e gráficos compartilhados |
| Configuração | `.streamlit/config.toml`, `requirements.txt` | Tema, navegação e dependências fixadas |

Os indicadores exibem pedidos distintos, despachos elegíveis, taxa de atraso e pedidos com nota.
O mínimo de pedidos modifica somente o ranking; os demais filtros modificam o recorte inteiro.
Recortes vazios e seleção de período incompleta exibem orientações sem interromper o aplicativo com erro.
O painel usa apenas `data/processed/tabela_analitica.csv` como fonte numérica.
Os textos das respostas ficam em `reports/conclusoes_equipe.json`.

### Etapa 8 - Documentação, apresentação e testes

| Entrega | Arquivo |
|---|---|
| Relatório final do grupo, 12 páginas | `reports/relatorio_final.pdf` |
| Versão textual do relatório | `reports/relatorio_tecnico.md` |
| Diário de decisões | `reports/diario_de_decisoes.md` |
| Dicionário das 41 colunas | `reports/dicionario_de_dados.md` |
| Instalação, execução e limites | `README.md` |
| Roteiro de apresentação e fala de apoio | `docs/apresentacao.md` |
| Evidências das verificações | `reports/verificacao.md` |
| Testes do painel | `tests/test_dashboard.py` |
| Testes de integração com dados brutos | `tests/test_pipeline.py` |
| Histórico da assistência | `uso_de_ia.md` |

O relatório permanece uma entrega do grupo inteiro. A responsabilidade de consolidá-lo não altera a origem das análises e das decisões.

## Execução em outro computador

Baixar e extrair o projeto inteiro. Não copiar somente `app.py`: ele depende de `src/`, `pages/`, configuração e base final.
Abrir um terminal na raiz do projeto e executar:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Usar Python 3.11. Para testar o painel, a base final já está incluída; não é necessário baixar os CSVs brutos.
Para executar a suíte completa, obter antes os cinco CSVs conforme o README.

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Integração com as etapas 1 a 6

A interface recebe uma linha por `(order_id, seller_id)`, com nomes e tipos descritos no dicionário.
As datas devem estar em formato reconhecível pelo Pandas; flags são booleanas; notas válidas vão de 1 a 5.
Não mudar nomes de colunas sem adaptar os cálculos e os testes do painel.
As etapas anteriores já estão disponíveis no projeto como referência de integração, sem nova atribuição de responsáveis.

Ao receber a versão consolidada dos colegas, executar o pipeline em uma pasta de saída separada primeiro:

```powershell
.\.venv\Scripts\python.exe scripts/executar_pipeline.py --input data/amostra_bruta --output work/demonstracao --sem-graficos
```

A pasta de entrada deve conter os cinco CSVs com os nomes originais do Kaggle.
Esse comando não substitui a base publicada do painel.
Só depois de conferir schema, contagens e testes, atualizar a base principal, as evidências e o relatório em conjunto.
No computador usado nesta revisão existe também uma amostra real em `work/amostra_bruta` para ensaio; ela não é incluída no Git.

## Critérios que precisam ser explicados na apresentação

- TAD: despachos após o prazo divididos por despachos elegíveis. O prazo é o menor dos itens do pedido-vendedor.
- Comparação individual: um vendedor observado, datas coerentes e prazo conhecido em todos os itens.
- Uma nota por pedido; pedidos multivendedor não entram na comparação individual.
- TAD acima de 10% e nota abaixo de 3,8 são critérios propostos, não prova de culpa nem advertência automática.
- A janela de 30 dias termina na última compra do recorte histórico filtrado. Cada pedido elegível avaliado tem peso 1.
- Dias úteis consideram segunda a sexta, sem feriados. Não há limite automático definido para esse tempo.
- Associação entre atraso e nota menor não demonstra causalidade; o despacho é uma data do pedido inteiro.

## Links para encaminhar ao líder

- [Painel publicado](https://wuevyectn67rbfng9xqssx.streamlit.app/)
- [Repositório completo](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados)
- [Baixar relatório PDF](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/raw/refs/heads/main/reports/relatorio_final.pdf)
- [Baixar projeto em ZIP](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/archive/refs/heads/main.zip)

## Conferência para a entrega do grupo

As etapas 7 e 8 foram organizadas sobre a base integrada atual. Consultar a execução de 20/11/2026 em `reports/verificacao.md`.
O acesso público ao painel foi confirmado anteriormente pelo proprietário em janela anônima.
Antes do envio final, o líder deve assegurar que o PDF, o painel e a tabela correspondem à mesma versão consolidada dos colegas.
Na apresentação, abrir o painel, mostrar os filtros e executar o pipeline sobre a amostra bruta fornecida pela professora.
