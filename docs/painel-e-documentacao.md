# Painel e documentação

Contribuição de Guilherme Estrela: interface Streamlit e documentação integrada. Implementação assistida conforme uso_de_ia.md. Esta consolidação não altera a autoria das demais partes do projeto.

## Componentes

| Componente | Caminho |
| --- | --- |
| Entrada e visão geral | `app.py` |
| Atrasos, avaliações e acompanhamento | `pages/` |
| Interface comum e filtros | `src/dashboard.py` |
| Cálculos | `src/analysis.py` |
| Figuras | `src/visualizations.py` |
| Conclusões fornecidas pela equipe | `reports/conclusoes_equipe.json` |

O painel lê `data/processed/tabela_analitica.csv`. Os filtros de UF, vendedor e período afetam os cálculos do recorte. O volume mínimo modifica o ranking. Recortes vazios e períodos incompletos recebem mensagens de orientação.

## Contrato de dados

Uma linha por `(order_id, seller_id)`. As colunas, tipos e elegibilidade estão no dicionário. Mudanças de esquema precisam acompanhar cálculos e testes. Não atribuir avaliações multivendedor a vendedores individuais.

## Verificação

Execute `python -m pytest -q` com o ambiente preparado conforme o README. Ao alterar o pipeline, use uma saída separada para comparar os resultados antes de substituir a tabela do painel. A revisão de métricas e textos continua sendo uma responsabilidade humana.
