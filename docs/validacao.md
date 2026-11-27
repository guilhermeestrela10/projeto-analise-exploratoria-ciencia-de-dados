# Validação técnica

## Integridade e métricas

- Validar chaves, cardinalidades e duplicatas nos relacionamentos.
- Manter uma linha por pedido-vendedor e uma avaliação selecionada por pedido.
- Aplicar máscaras específicas para datas, notas e elegibilidade de despacho.
- Preservar denominadores, dados originais e sinais de cronologia inválida.
- Separar medidas gerenciais de transformações demonstrativas.

## Aplicação e relatórios

Execute a suíte com `python -m pytest -q`. Ela cobre preparação, análise, recortes reais, interface Streamlit, textos de autoria e geração reproduzível do PDF. Testes automáticos não comprovam revisão humana ou causalidade.

Confira as páginas do painel com filtros de UF, vendedor, período, volume mínimo e recorte vazio. Antes de publicar um novo PDF, confira texto, gráficos, tabelas, referências e todas as páginas renderizadas.

O arquivo `reports/verificacao.md` registra evidências e limites das verificações anteriores. As execuções de CI pertencem aos commits correspondentes; não representam validação permanente de serviços externos.
