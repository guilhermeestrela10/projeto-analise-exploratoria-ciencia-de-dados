# Auditoria de escopo - rubrica da professora

Fonte: PDF oficial, página 5; anexos B/C/D nas páginas 11/12. A auditoria não atribui nota.

| Critério | Peso | Evidências preparadas | Pendência que impede considerar a entrega final |
|---|---|---|---|
| Exploração dos dados | 1,5 | Notebook executado, perfis das cinco tabelas, estatísticas, gráficos de distribuição, tempo e relação | Equipe deve estudar e validar leitura dos resultados |
| Limpeza, tratamento e diário | 2,0 | Conversões, validação de chaves, ausências, IQR, comparação de alternativas, evidencias.json e modelo Anexo B | Justificativas e decisões reais do diário devem ser escritas pelos integrantes |
| Codificação, normalização e seleção | 1,5 | One-hot fixo, MinMax, Z-score, correlações, baixa variância e filtro semântico | Equipe deve conseguir explicar propósito e limites |
| Feature engineering, quatro técnicas | 1,0 | Diferenças temporais, indicadores condicionais, agregações e extração temporal; razão frete/valor adicional | Validar definições e limitações da aproximação de despacho |
| Pipeline em função e amostra bruta | 1,5 | preprocessar; CLI; testes com recorte real de 50 pedidos, um pedido, constantes e nenhuma correspondência | Ensaio dos quatro integrantes e execução na amostra desconhecida da professora |
| Painel publicado, funcional e alinhado | 1,5 | Inicial + três páginas; filtros UF/vendedor/período; testes AppTest; CSV final como fonte | Publicar no Streamlit Community Cloud, escrever conclusões humanas, testar link anônimo |
| Respostas de negócio e apresentação | 1,0 | Tabelas numéricas de apoio, espaços autorais e roteiro de dez minutos | Equipe deve escrever sumário, respostas e conclusões e ensaiar apresentação |

## Entregáveis e restrições

- Repositório público com nome `projeto-analise-exploratoria-ciencia-de-dados`: publicado e confirmado na conta guilhermeestrela10; consultar README para o link.
- Código, notebook, função de pipeline, CSV, dicionário, painel e requirements: preparados; execução verificada em reports/verificacao.md.
- CSV final menor que 100 MB: tamanho e hash em data/processed/metadados.json; nenhuma linha foi removida para diminuir tamanho.
- Registro de IA: uso_de_ia.md, seis registros, marcadores nos arquivos Python, sem revisão humana fictícia.
- Cinco tabelas: três obrigatórias e dois complementares; geolocation não utilizada.
- Scikit-Learn exclusivamente pré-processamento; sem modelo de classificação ou previsão.
- Relatório PDF: Partes A/B/C presentes; Parte A e respostas recebidas integradas com revisão autorizada. Justificativas e demais campos humanos continuam sinalizados; ainda não é relatório final para entrega.
- Sumário executivo: seção reservada em uma página; equipe deve respeitar máximo de uma página ao preencher.
- Dicionário Anexo C: todas as 41 colunas, origem, tipo, descrição e tratamento; correspondência de esquema validada pelo teste integrado.
- Diário Anexo B: seis campos exigidos, evidências separadas; ampliar para todas as decisões efetivamente discutidas.
- Histórico de commits de todos os integrantes: precisa ser produzido pelos integrantes, sem simulação.
- Links GitHub e Streamlit: precisam ser reais e entrar no README.
- Plataforma A: enviar PDF e os dois links até 30/11/2026, 23h59 de Brasília.
- Apresentação 02/12/2026: cinco minutos de negócio e cinco minutos técnicos, até dez minutos no total.

## Verificação técnica

Resultados e limitações dos testes estão em reports/verificacao.md. Os testes executam o código;
não substituem autoria, validação crítica e apresentação humana. Não se declara cumprimento integral
dos critérios com partes humanas ou publicação pendentes.

## Link do painel informado pelo proprietário

[Abrir painel](https://wuevyectn67rbfng9xqssx.streamlit.app/). O proprietário confirmou nesta conversa que o painel abre em janela anônima, sem login, e que as três páginas funcionam. Essa é uma confirmação manual do proprietário; não representa inspeção visual independente da ferramenta nem teste manual de todos os filtros.

## Complementação textual para revisão

O PDF de 12 páginas possui conclusão, contextualização e oito justificativas técnicas preenchidas como rascunho IA. A identificação da assistência foi mantida. Os 34 testes passaram. Não se considera atendido o requisito de autoria humana apenas pelo preenchimento automático desses textos.

## Revisão informada pelo solicitante em 18/11/2026

O solicitante confirmou nesta conversa que ele e o grupo revisaram o relatório. A versão do PDF foi
atualizada para refletir essa declaração, sem afirmar que a ferramenta acompanhou a revisão humana.
As indicações de assistência de IA e os registros anteriores foram preservados. A declaração de revisão
não equivale à aprovação da professora nem altera a origem dos textos ou comprova contribuições individuais.
O registro está em reports/revisao_equipe.json.
