# Organização técnica

O projeto separa carga, preparação, atributos, análise, visualização e interface. O pipeline gera a tabela processada, metadados, evidências e relatórios. O painel consome a tabela final sem executar novamente o processamento bruto.

## Regras de manutenção

Preservar fontes, hashes, contratos de dados e testes. Alterar nomes ou tipos de colunas exige revisar todos os consumidores. Justificativas e conclusões devem manter a origem declarada; saídas automáticas não equivalem a decisões validadas pela equipe.

## Componentes

- `src/`: regras de preparação, métricas, figuras e interface.
- `scripts/`: rotinas de reprodução e verificação.
- `tests/`: verificações do pipeline e do painel.
- `reports/`: resultados, referências e documentos.
- `docs/`: integração, publicação e validação.
