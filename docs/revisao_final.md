# Segunda revisão do trabalho - Grupo 04, Briefing 5

Referência: as 12 páginas de FINAL BOSS - TRABALHO CIENCIA DE DADOS.pdf, relidas nesta revisão.
Data: 17/11/2026. Conteúdo técnico assistido por IA, registro 4.

## Situação da entrega

**AINDA NÃO PRONTO PARA ENVIAR À PROFESSORA.** A implementação técnica foi revisada e testada,
mas as partes de autoria humana, os commits reais dos demais integrantes e a publicação ainda precisam ser concluídos.
O pedido de aparência e linguagem de alunos do quarto período não altera a autoria real dos textos e do código.
O registro de IA deve continuar visível e cada integrante deve conseguir explicar o trabalho.

## Confronto com a rubrica

| Exigência do documento | O que existe | Estado |
|---|---|---|
| Briefing 5 e três perguntas corretas | Páginas de despacho, avaliações e critérios; fontes adequadas | Implementação alinhada |
| Três datasets obrigatórios e até dois complementares | orders, order_items, products, sellers, order_reviews | Atendido; geolocation não utilizada |
| EDA: estrutura, tipos, estatísticas, distribuições e relações | Notebook executado, perfis, estatísticas e cinco gráficos | Parte técnica preparada |
| Limpeza: duplicatas, inconsistências, ausências e outliers | Pipeline, flags, auditoria e comparações de alternativas | Parte técnica preparada; justificativas humanas pendentes |
| Datas, categorias e textos | Conversões seguras; UF/categoria padronizadas; limpeza de texto sem publicar comentários livres | Atendido tecnicamente |
| Codificação, MinMax e Z-score | Colunas demonstrativas separadas das métricas gerenciais | Atendido; constantes e ausências testadas |
| Seleção: correlação, baixa variância e filtros simples | selecao_atributos.json, correlacoes.csv e filtros por propósito/elegibilidade | Atendido tecnicamente |
| Quatro técnicas de feature engineering | Diferenças temporais, indicadores, agregações e extração temporal; razão adicional | Atendido |
| Função sobre DataFrames originais e amostras novas | preprocessar e CLI; recortes reais, vazios, constantes e sem correspondência | Testado; ensaio humano ainda necessário |
| CSV abaixo de 100 MB e dicionário completo | 100.010 linhas, 41 colunas, 38.373.468 bytes; Anexo C completo | Atendido |
| Multipage, dois filtros e fonte CSV final | Inicial e três páginas; UF, vendedor e período; fonte única | Testado localmente |
| Conclusão de negócio em cada página | Respostas fornecidas pelo solicitante, revisadas com autorização e inseridas no painel | Revisão dos demais integrantes pendente |
| PDF A/B/C; Parte A até uma página | PDF técnico de dez páginas com campos humanos destacados | Parte B preparada; A e justificativas de C pendentes |
| README com principais conclusões e link do painel | Instalação, métricas, briefing e responsáveis propostos | Conclusões, confirmação de responsáveis e links finais pendentes |
| IA registrada, marcas no código e nos commits | uso_de_ia.md; código marcado; novos commits assistidos com [IA] | Registro mantido; revisão humana não foi presumida |
| Commits de todos os quatro integrantes | Commit preexistente do proprietário preservado | Faltam contribuições reais dos demais integrantes |
| Repositório público e Streamlit Community Cloud | GitHub público criado e primeiro push confirmado | Community Cloud pendente |

## O que foi corrigido nesta revisão

1. A auditoria de avaliações contava notas numéricas fora de 1 a 5, mas não textos inválidos.
   Agora conta os dois casos. A medição da base original continua reproduzível; não foram inventadas notas.
2. Foi acrescentada uma checagem de campos autorais pendentes, com testes para arquivos ausentes,
   JSON inválido, campos vazios e placeholders. Essa checagem não autentica autoria nem garante aprovação acadêmica.
3. O Git passa a tratar PDF e PNG como binários, com texto normalizado em LF. Isso evita conversão de fim de linha em PDFs.
4. Foi preparado um workflow GitHub Actions para verificar dependências, sintaxe e testes a cada push.
   Ele obtém os cinco CSVs públicos somente no ambiente de testes, sem versionar os brutos e sem permissão de escrita.
5. AGENTS.md registra o fluxo pedido pelo proprietário: alterações do assistente devem ser testadas, revisadas,
   commitadas e enviadas ao remoto. Não foi instalado monitor de arquivos nem inventada sincronização fora de uma sessão.

## Verificações desta revisão

Resultados finais, hash e estado de publicação são registrados também em reports/verificacao.md.
Foram executados pytest, compileall, pip check, leitura do PDF gerado e o pipeline sobre a amostra real preparada.
A amostra tem 50 pedidos, 55 itens, 49 produtos, 44 vendedores e 51 avaliações originais.
Gerou 49 linhas analíticas, 47 pedidos elegíveis e o mesmo esquema de 41 colunas.
A checagem de autoria retorna código 1 no estado atual, apontando pendências reais; isso é o comportamento esperado.

## O que precisa ser feito por pessoas

1. Escrever o sumário executivo, as respostas às três perguntas, as conclusões e as justificativas do diário.
   A seção 7.1 do PDF não permite gerar esses textos com IA. A ferramenta pode revisar o português de texto fornecido.
2. Validar os resultados, explicar as regras de tratamento e confirmar as frentes dos integrantes.
3. Fazer contribuições e commits reais dos quatro participantes. Não há substituto automático para esse requisito.
4. Autorizar a GitHub CLI e concluir a publicação pública; depois publicar e testar o painel no Community Cloud.
5. Conferir o nome do repositório: o proprietário pediu “ciencia de dados”, enquanto o PDF exige o padrão
   Projeto-Analise-Exploratoria-<NomeDaEquipe>. A divergência foi apresentada para escolha do proprietário.
6. Regenerar e revisar o PDF após preencher os textos humanos. Enviar PDF e os dois links reais pela plataforma A.

Prazo: 30/11/2026, 23h59 de Brasília. Apresentação: 02/12/2026, até dez minutos, sendo cinco de negócio e cinco técnicos.

## Atualização após respostas do solicitante

- Nome confirmado: projeto-analise-exploratoria-ciencia-de-dados.
- Repositório público criado e push confirmado: https://github.com/guilhermeestrela10/projeto-analise-exploratoria-ciencia-de-dados.
- As três respostas foram recebidas; as correções factuais e definições dos critérios foram aprovadas expressamente pelo solicitante. Não se presume revisão dos outros integrantes.
- Monitoramento implementado: TAD > 10%, nota < 3,8, coorte dos últimos 30 dias da base filtrada, peso 1 por pedido avaliado e dias úteis sem feriados. Nenhum limite de tempo médio foi inventado.
- O diário recebeu contagens e operações implementadas, mantendo justificativas humanas pendentes. Não foram fabricadas decisões de reuniões do grupo.
- A automação do navegador foi interrompida porque não conseguiu determinar a URL com segurança. Community Cloud continua pendente; nenhum link de aplicativo publicado foi inventado.

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
