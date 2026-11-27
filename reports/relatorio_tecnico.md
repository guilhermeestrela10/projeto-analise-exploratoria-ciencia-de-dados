# Parte B - Conteúdo técnico automático

## 1. Problema e recorte

O projeto trata de gestão de vendedores parceiros: identificar atrasos de despacho, investigar a associação com avaliações e apoiar a discussão de critérios objetivos. A data de transportadora existe no nível do pedido. A análise individual usa pedidos com um único vendedor observado; isso não comprova responsabilidade e depende da cobertura dos itens recebidos. A contextualização complementar e as referências consultadas pela ferramenta aparecem na seção 12, sem atribuição de pesquisa aos integrantes.

## 2. Dados e relacionamentos

Fonte: Olist Brazilian E-Commerce Public Dataset, Kaggle. Cinco arquivos foram obtidos da fonte pública; hashes de cada original estão registrados em data/raw/proveniencia.json. Geolocalização não foi extraída nem utilizada. IDs de clientes e textos livres de avaliações não são incluídos na tabela final.

## 3. Ciclo de vida CRISP-DM

Compreensão do negócio: três perguntas do escopo. Compreensão dos dados: perfis, ausências, chaves e estatísticas. Preparação: limpeza, conversões, agregação e engenharia. A etapa de modelagem não inclui modelos de IA, classificação ou previsão, conforme o escopo descritivo adotado. Avaliação: testes, recortes reais e comparação de alternativas. Entrega: CSV, notebook, painel, relatório e repositório público. O proprietário confirmou o acesso público ao painel e informou a revisão do relatório pelo grupo.

## 4. Exploração e qualidade

Foram observados 775 pedidos sem itens correspondentes, que não geram linha pedido-vendedor; 551 avaliações excedentes foram reduzidas a uma por pedido; 1278 pedidos possuem mais de um vendedor observado. Há 1451 pares pedido-vendedor com alguma contradição temporal sinalizada. Cada duração possui sua própria máscara de validade; uma entrega ao cliente inconsistente não invalida automaticamente uma medição de despacho que seja coerente.

## 5. Limpeza e padronização

Duplicatas exatas são removidas; chaves ausentes são contabilizadas; chaves conflitantes interrompem a execução. Datas usam conversão segura e não são imputadas. Preços/fretes negativos ou inválidos viram ausências; somas de grupos incompletos continuam ausentes. Notas fora de 1 a 5 não entram na média. Categorias são normalizadas; UF inválida vira SEM_INFORMACAO. Textos de comentários usam NFKC, minúsculas e espaços simples; somente o comprimento é exportado. São propostas técnicas da ferramenta; suas justificativas autorais devem ser escritas pela equipe.

## 6. Outliers e impacto mensurável

O tempo de aprovação até a transportadora usa cercas Q1 - 1,5 IQR e Q3 + 1,5 IQR, ajustadas ao lote de pedidos elegíveis. O valor original é preservado. O clipping fica numa coluna demo_, sem alterar o indicador de atraso. A tabela abaixo compara alternativas; não representa uma justificativa autoral da equipe.

## 7. Codificação, escalas e seleção

O status é codificado em delivered, shipped e other, com três colunas one-hot fixas. MinMaxScaler e StandardScaler são aplicados a sales_value apenas nas observações válidas; constantes viram zero e ausências são preservadas. As escalas são recalculadas para cada lote. IDs, texto livre e escalas redundantes são excluídos da lista de atributos analíticos. Variância populacional <= 1e-12 identifica constantes ou baixa variância; correlação absoluta >= 0,95 gera pares para inspeção, sem eliminar automaticamente medidas gerenciais necessárias. Lista exata e matriz: selecao_atributos.json e correlacoes.csv.

## 8. Engenharia de atributos e denominadores

Foram aplicadas pelo menos quatro técnicas: diferenças temporais (dias até despacho, excesso, transporte e entrega); indicadores condicionais (atraso, avaliação negativa, elegibilidade); agregações por grupo (itens, valor, vendedores por pedido); extração temporal (mês e dia da semana). Há ainda razão frete/(itens + frete). Atraso de despacho compara timestamps; atraso ao cliente compara dias civis. O menor prazo dos itens é usado como aproximação conservadora e o maior prazo também é preservado. Algum item sem prazo exclui o grupo da taxa individual.

## 9. Evidências descritivas calculadas

Os gráficos e tabelas a seguir são saídas numéricas do pipeline, sem resposta autoral às perguntas de negócio. O ranking ilustrativo usa volume mínimo exploratório de 30 pedidos, ajustável no painel. IDs completos e denominadores estão nos CSVs de apoio.

## 10. Pipeline e reprodutibilidade

A função preprocessar recebe cinco DataFrames brutos e retorna a tabela final, com evidências em attrs["audit"]. O comando python scripts/executar_pipeline.py executa todas as etapas. Para demonstração: python scripts/executar_pipeline.py --input data/amostra_bruta --output work/demonstracao --sem-graficos. O segundo comando mantém a base do painel preservada. Dependências, comandos completos e testes estão no README e em reports/verificacao.md.

## 11. Limites e validação humana

Amostras com itens faltantes podem subestimar o número de vendedores e alterar prazos e valores agregados. O pipeline não recupera dados não fornecidos. Avaliações multivendedor não são atribuídas individualmente na análise principal. A última resposta não garante que a nota se refira apenas ao despacho. Intervalos de Wilson descrevem incerteza da taxa sob aproximação binomial, sem corrigir dependência temporal ou confundimento. Os dados são históricos; não representam o desempenho atual dos parceiros.
