# Olist Seller Analytics

Análise exploratória de atrasos, avaliações e indicadores de acompanhamento de vendedores parceiros, com pipeline reproduzível e painel Streamlit.

[![Testes](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/actions/workflows/testes.yml/badge.svg?branch=main)](https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados/actions/workflows/testes.yml)

[Painel](https://wuevyectn67rbfng9xqssx.streamlit.app/) · [Metodologia](reports/relatorio_tecnico.md) · [Relatório](reports/relatorio_final.pdf) · [Proveniência e autoria](uso_de_ia.md)

## Objetivo

Explorar a frequência de atrasos no despacho, sua associação com avaliações e critérios descritivos para acompanhar vendedores. A análise não estima causalidade nem dispara advertências automáticas.

## Funcionalidades

- Pipeline de limpeza, padronização, agregação e validação dos relacionamentos.
- Tabela analítica com uma linha por pedido-vendedor.
- Painel com visão geral, atrasos, avaliações e critérios de acompanhamento.
- Filtros por UF, vendedor, período e volume mínimo de pedidos elegíveis.
- Gráficos, indicadores, CSVs de evidências, notebook e relatório técnico.

## Executar localmente

Use Python 3.11. Na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

A tabela processada está incluída para executar o painel. No Linux/macOS, use `.venv/bin/python`.

### Pipeline e testes

Os CSVs brutos não são versionados. Para preparar uma cópia local, obter os cinco arquivos públicos, executar o pipeline e rodar a suíte:

```powershell
.\.venv\Scripts\python.exe scripts/baixar_dados.py
.\.venv\Scripts\python.exe scripts/executar_pipeline.py
.\.venv\Scripts\python.exe -m pytest -q
```

O download registra a proveniência e os hashes. Não use diretórios com arquivos brutos de outra origem sem conferir a compatibilidade.

## Dados e limites metodológicos

Fonte: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). São usados pedidos, itens, produtos, vendedores e avaliações.

- A data de despacho e a avaliação pertencem ao pedido inteiro.
- A comparação individual considera pedidos com um único vendedor observado; uma amostra incompleta pode esconder outros vendedores.
- Avaliações de pedidos multivendedor não são atribuídas individualmente.
- Ausências e cronologias inválidas usam máscaras de elegibilidade por indicador.
- Atraso, transporte, entrega e composição dos pedidos podem afetar as notas.
- Os dados são históricos e não representam o desempenho atual dos parceiros.

Os limites TAD acima de 10%, nota abaixo de 3,8 e janela de 30 dias são parâmetros de acompanhamento declarados no projeto; não constituem regra universal de decisão.

## Estrutura

| Caminho | Conteúdo |
| --- | --- |
| `app.py`, `pages/` | Entrada e páginas do painel |
| `src/` | Preparação, análise, visualização e interface |
| `scripts/` | Download, pipeline, notebook, relatório e verificação de autoria |
| `data/` | Proveniência e tabela processada |
| `notebooks/` | Análise exploratória |
| `reports/` | Evidências, dicionário, gráficos e relatórios |
| `docs/` | Publicação, arquitetura do painel e validação |
| `tests/` | Testes do pipeline, painel e relatório |

## Autoria e contribuições

Projeto colaborativo de Guilherme Estrela, David Gabriel, Carlos Gabriel Raposo e Roger. A contribuição declarada de Guilherme abrange o painel Streamlit e a documentação integrada. A consolidação não atribui a ele a execução das demais partes.

Textos recebidos, assistência de IA e limites da revisão humana permanecem registrados em [uso_de_ia.md](uso_de_ia.md) e nos documentos de proveniência. Nenhuma contribuição ou aprovação independente é presumida.

## Documentação

- [Painel e documentação](docs/painel-e-documentacao.md)
- [Publicação](docs/publicacao.md)
- [Validação](docs/validacao.md)
- [Decisões](reports/diario_de_decisoes.md)
- [Dicionário de dados](reports/dicionario_de_dados.md)
