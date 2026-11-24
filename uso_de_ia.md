# Registro de uso de IA - Anexo D

Data desta implementação: 17/11/2026. Ferramenta: Codex, nesta conversa.
Os registros descrevem assistência automática solicitada; não comprovam revisão nem participação dos demais integrantes.
O solicitante confirmou o nome Guilherme Estrela em 20/11/2026. As identificações genéricas nas linhas antigas representam o registro histórico.
O link compartilhável da conversa depende de disponibilidade no cliente utilizado.

| Nº | Data | Integrante | Ferramenta | Etapa e o que foi pedido | O que foi aproveitado | O que a equipe alterou ou verificou | Link da conversa |
|---|---|---|---|---|---|---|---|
| 1 | 17/11/2026 | Solicitante desta conversa; confirmar nome | Codex | Implementar limpeza, testes e feature engineering | src/preprocessing.py, src/feature_engineering.py, testes correspondentes | Revisão humana pendente; verificações automáticas em reports/verificacao.md | Pendente, caso a ferramenta permita |
| 2 | 17/11/2026 | Solicitante desta conversa; confirmar nome | Codex | Análises, gráficos, painel e testes | src/analysis.py, src/visualizations.py, src/dashboard.py, app.py, pages/, testes | Revisão humana pendente; verificar métricas, limites e interpretações | Pendente |
| 3 | 17/11/2026 | Solicitante desta conversa; confirmar nome | Codex | Carga, aquisição, pipeline, notebook e documentação técnica | src/load_data.py, src/reporting.py, scripts/, notebook, documentos técnicos | Revisão humana pendente; conferir evidências da execução automática | Pendente |
| 4 | 17/11/2026 | Solicitante desta conversa; confirmar nome | Codex | Revisar contra o PDF, preparar publicação e apontar pendências de entrega | Correção da contagem de notas inválidas, teste de regressão, verificar_entrega.py, testes e workflow GitHub Actions | Verificações automáticas registradas em docs/revisao_final.md; autoria e revisão humana continuam pendentes | Pendente |
| 5 | 17/11/2026 | Solicitante desta conversa | Codex | Integrar três respostas fornecidas, corrigir afirmações e implementar critérios definidos pelo solicitante | Textos originais preservados em reports/respostas_recebidas.md; revisão factual autorizada; limites TAD 10%, nota 3,8, janela de 30 dias e dias úteis sem feriados | O solicitante autorizou expressamente as correções factuais e as definições da janela e pesos; não confirmou revisão de todo o código nem justificativas reais do grupo | Pendente |
| 6 | 17/11/2026 | Solicitante desta conversa | Codex | Completar os textos restantes para estudo e revisão | Rascunhos de oito justificativas, conclusão técnica e contextualização; PDF completo para revisão; verificador reconhece o marcador RASCUNHO IA | Conteúdo verificado contra evidências existentes; não se presume autoria humana, reunião do grupo ou aprovação dos integrantes; a regra da seção 7.1 continua sendo uma pendência acadêmica | Pendente |
| 7 | 18/11/2026 | Solicitante desta conversa | Codex | Registrar revisão informada pelo solicitante e pelo grupo, ajustar referências e gerar a versão revisada | Avisos de revisão pendente atualizados; declaração em reports/revisao_equipe.json; origem assistida dos textos preservada | O solicitante informou que ele e o grupo revisaram o relatório; a ferramenta não acompanhou essa revisão nem declara aprovação da professora | Pendente |
| 8 | 20/11/2026 | Guilherme Estrela | Codex | Organizar a entrega das etapas 7 e 8 após a divisão do líder | Guia de entrega, atualização de responsáveis no README, roteiro de demonstração e verificações do painel e pipeline existentes | Nome e atribuição confirmados pelo solicitante; resultados automáticos em reports/verificacao.md; não foram inventadas contribuições dos colegas | Indisponível nesta entrega |

## Limites de autoria
O PDF, seção 7.1, proíbe IA nas justificativas do diário, sumário executivo, respostas de negócio e conclusões.
As respostas de negócio foram fornecidas pelo solicitante e receberam revisão factual autorizada, registrada na linha 5. A revisão do grupo foi informada pelo solicitante em 18/11/2026, conforme linha 7. Isso não altera a origem assistida dos complementos nem comprova atendimento às exigências de autoria da disciplina. Evidências e descrições técnicas automáticas estão identificadas.

Atualização do registro 6: os textos das justificativas, conclusão e contextualização foram completados como rascunho IA, sem campos vazios no documento. Isso não comprova a autoria humana exigida no PDF; a equipe precisa elaborar e validar as partes que lhe cabem. As referências técnicas não foram atribuídas a pesquisas realizadas pelos integrantes.
As regras de limpeza e métricas implementadas são propostas técnicas da ferramenta, ainda sujeitas à avaliação dos integrantes.
Não registrar revisão humana antes de realizá-la. Não atribuir decisões automáticas aos estudantes.
Todo arquivo Python gerado recebe a marcação de registro; o marcador no início abrange o arquivo inteiro.
Commits com código assistido devem incluir [IA]. Os commits desta revisão usam a identidade configurada do proprietário e a marca [IA], conforme sua autorização de publicação. Não foram simuladas contribuições dos outros integrantes.

Na segunda revisão foi encontrado o commit local preexistente `45ad1cf` (mensagem `salvando`),
criado pelo proprietário entre as sessões. Ele foi preservado, sem reescrever sua autoria ou mensagem.
As alterações assistidas desta revisão serão identificadas nos novos commits com [IA].

## Verificação e erros da ferramenta
Consultar reports/verificacao.md para comandos efetivamente executados, falhas e correções observadas.
Na leitura inicial do PDF houve UnicodeEncodeError no terminal Windows; a leitura integral foi repetida com python -X utf8.
O registro de correções automáticas não substitui o exemplo crítico e a explicação que cada integrante deve conseguir apresentar.

## Organização dos repositórios — 24/11/2026

Assistência do Codex solicitada pelo proprietário: navegação no README, atualização de links para o nome em minúsculas e organização da apresentação no GitHub. Código, dados, conclusões e contribuições da equipe foram preservados. Não representa nova revisão humana do relatório.
