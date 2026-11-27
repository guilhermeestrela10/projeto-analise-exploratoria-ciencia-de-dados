# Textos recebidos e complementos para estudo

[TEXTO ASSISTIDO POR IA - REVISÃO INFORMADA]
As respostas e o sumário vieram do solicitante, com revisão factual autorizada. A conclusão técnica e a contextualização abaixo foram redigidas pela ferramenta nesta etapa. Revisão do grupo informada pelo solicitante em 18/11/2026. A informação foi recebida nesta conversa, sem acompanhamento independente da revisão pela ferramenta. A origem assistida dos complementos permanece registrada.

O solicitante enviou as três respostas e autorizou correções factuais e inclusão de números e vendedores.
Os originais estão em respostas_recebidas.md. Revisão do grupo informada pelo solicitante em 18/11/2026.

## Parte A - Sumário executivo (máximo de uma página)

No ranking de vendedores com pelo menos 30 pedidos elegíveis, os maiores percentuais de atraso foram: 48efc9d94a9834137efd9ea76b065a38, com 28 atrasos em 33 pedidos (84,85%); 835f0f7810c76831d6c7d24c7a646d4d, com 31 em 40 (77,50%); e a7f13822ceb966b076af67121f87b063, com 45 em 75 (60,00%). O atraso compara a entrega à transportadora com o prazo-limite dos itens. Esse resultado identifica os maiores percentuais nesse recorte e não comprova que 10% a 15% dos vendedores concentrem os problemas.

Sim, observamos associação entre atraso no despacho e notas piores. Entre os pedidos elegíveis com avaliação, a nota média foi 4,19 sem atraso e 3,68 com atraso. A proporção de notas 1 e 2 foi 11,89% sem atraso e 24,21% com atraso. Essa comparação não prova que o vendedor causou a nota baixa e não permite classificar toda a relação como correlação forte.

Propomos acompanhar três métricas: Taxa de Atraso de Despacho superior a 10%, nota média por pedido nos últimos 30 dias da base filtrada com piso de 3,8, e tempo médio entre aprovação e postagem em dias úteis. Cada pedido elegível com nota tem peso 1. A janela termina na última compra do recorte histórico; dias úteis consideram segunda a sexta, sem feriados. Ainda não definimos um limite para o tempo médio.

## Resposta 1 - Quais vendedores mais atrasam o despacho?

No ranking de vendedores com pelo menos 30 pedidos elegíveis, os maiores percentuais de atraso foram: 48efc9d94a9834137efd9ea76b065a38, com 28 atrasos em 33 pedidos (84,85%); 835f0f7810c76831d6c7d24c7a646d4d, com 31 em 40 (77,50%); e a7f13822ceb966b076af67121f87b063, com 45 em 75 (60,00%). O atraso compara a entrega à transportadora com o prazo-limite dos itens. Esse resultado identifica os maiores percentuais nesse recorte e não comprova que 10% a 15% dos vendedores concentrem os problemas.

## Resposta 2 - Vendedores que atrasam recebem avaliações piores?

Sim, observamos associação entre atraso no despacho e notas piores. Entre os pedidos elegíveis com avaliação, a nota média foi 4,19 sem atraso e 3,68 com atraso. A proporção de notas 1 e 2 foi 11,89% sem atraso e 24,21% com atraso. Essa comparação não prova que o vendedor causou a nota baixa e não permite classificar toda a relação como correlação forte.

## Resposta 3 - Que critérios usar para acompanhar ou advertir vendedores?

Propomos acompanhar três métricas: Taxa de Atraso de Despacho superior a 10%, nota média por pedido nos últimos 30 dias da base filtrada com piso de 3,8, e tempo médio entre aprovação e postagem em dias úteis. Cada pedido elegível com nota tem peso 1. A janela termina na última compra do recorte histórico; dias úteis consideram segunda a sexta, sem feriados. Ainda não definimos um limite para o tempo médio.

## Conclusão técnica

O projeto reuniu os cinco arquivos da Olist em uma tabela de 100.010 registros, com uma linha por pedido e vendedor observado. A agregação dos itens antes dos relacionamentos e a seleção de uma avaliação por pedido impediram que valores e notas fossem contados várias vezes. A comparação individual ficou restrita aos 94.955 pedidos elegíveis, dos quais 94.257 tinham nota válida.

Os resultados indicam associação entre atraso de despacho e avaliações piores: a média passou de 4,19 no grupo sem atraso para 3,68 no grupo com atraso. Isso não comprova que o vendedor causou a avaliação. A data de transportadora pertence ao pedido inteiro, e fatores como transporte e características da compra também podem influenciar a experiência do cliente.

As comparações de tratamento mostram que limpar os dados exige cuidado. Excluir tempos extremos reduziria a taxa de atraso de 9,23% para 5,66%, alterando a percepção dos problemas. Por esse motivo técnico, a implementação preserva os valores originais nos indicadores e separa as transformações demonstrativas. Para os prazos dos itens, a base analisada apresentou os mesmos 8.769 atrasos usando o menor ou o maior prazo entre os pedidos elegíveis; essa equivalência não deve ser presumida para qualquer amostra futura.

O pipeline funciona sem ajustes manuais no notebook e foi testado com a base real e com recortes pequenos. O painel permite explorar o período, a UF e o vendedor usando o CSV final. Os limites TAD acima de 10% e nota abaixo de 3,8 foram propostos pelo solicitante e servem para acompanhamento, sem advertência automática. Eles precisam ser avaliados com volume suficiente e registros conferidos. O principal limite do estudo é medir o despacho individual por uma data disponível no nível do pedido; os dados históricos também não descrevem o desempenho atual dos parceiros.

## Contextualização e referências consultadas pela ferramenta

O problema analisado é o acompanhamento de vendedores: a plataforma precisa acompanhar vendedores que despacham os pedidos, embora a experiência do cliente também envolva transporte e entrega. A análise deve distinguir essas etapas. Um pedido entregue depois do dia prometido não significa, por si só, que o vendedor ultrapassou o prazo de despacho. No projeto, o despacho é comparado com shipping_limit_date, enquanto a entrega ao cliente é comparada com order_estimated_delivery_date.

A fonte empírica é o Brazilian E-Commerce Public Dataset by Olist. Foram utilizados os arquivos de pedidos, itens, produtos, vendedores e avaliações; o arquivo de geolocalização foi excluído do escopo. O período é histórico, e não houve coleta de desempenho atual. A estrutura dos relacionamentos e as contagens apresentadas foram verificadas nos próprios CSVs, cujos hashes estão registrados na proveniência.

O fluxo segue o CRISP-DM: compreensão do problema, exploração dos dados, preparação, avaliação e entrega. Não foram construídos modelos de previsão ou classificação. A documentação de Pandas apoiou o uso de validação nos relacionamentos, a de Scikit-Learn apoiou as transformações demonstrativas, e a de Streamlit apoiou o painel e seus testes. Essas consultas foram feitas pela ferramenta; não se afirma que os integrantes tenham realizado uma pesquisa bibliográfica que não foi confirmada.

Referências: Olist/Kaggle, https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce; Pandas, https://pandas.pydata.org/docs/user_guide/merging.html; Scikit-Learn, https://scikit-learn.org/stable/modules/preprocessing.html; Streamlit, https://docs.streamlit.io/develop/concepts/app-testing. Dados e documentação técnica consultados ao longo da implementação em 17/11/2026.
