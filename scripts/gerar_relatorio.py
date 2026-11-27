"""Gera o relatório com origem dos textos e condição de rascunho explícitas."""
# [IA] registro 3
from pathlib import Path
import json
from xml.sax.saxutils import escape
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'


def main():
    audit = json.loads((REPORTS / 'evidencias.json').read_text(encoding='utf-8'))
    metadata = json.loads((ROOT / 'data/processed/metadados.json').read_text(encoding='utf-8'))
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'Helvetica'
    styles['Normal'].fontSize = 10
    styles['Normal'].leading = 15
    styles['Normal'].spaceAfter = 8
    styles['Heading1'].textColor = colors.HexColor('#142D4E')
    styles['Heading2'].textColor = colors.HexColor('#087F8C')
    styles.add(ParagraphStyle(name='Subtitle', parent=styles['Normal'], fontSize=13, leading=18, spaceAfter=16))
    styles.add(ParagraphStyle(name='SmallCell', fontSize=7.5, leading=10, spaceAfter=0))
    styles.add(ParagraphStyle(name='Cover', parent=styles['Title'], fontSize=25, leading=30, textColor=colors.HexColor('#142D4E'), spaceAfter=24))
    story, technical = [], []

    def paragraph(text, style='Normal'):
        story.append(Paragraph(escape(str(text)), styles[style]))

    def heading(text):
        paragraph(text, 'Heading2')

    def table(data, widths=None):
        cells = [[Paragraph(escape(str(v)), styles['SmallCell']) for v in row] for row in data]
        t = Table(cells, colWidths=widths, repeatRows=1, hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EAF0F6')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('GRID', (0, 0), (-1, -1), .35, colors.HexColor('#CCD6E0')),
            ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7)]))
        story.extend([t, Spacer(1, 12)])

    def section(title, text):
        heading(title)
        paragraph(text)
        technical.extend([f'## {title}', '', text, ''])

    def image(name, caption):
        path = REPORTS / f'graficos/{name}.png'
        if path.exists():
            from PIL import Image as PILImage
            with PILImage.open(path) as im:
                ratio = im.height / im.width
            story.append(KeepTogether([Image(str(path), width=480, height=480*ratio),
                Paragraph(escape(caption), styles['SmallCell']), Spacer(1, 14)]))

    def markdown(text):
        lines = text.splitlines()
        j = 0
        while j < len(lines):
            line = lines[j].strip()
            if line.startswith('|'):
                rows = []
                while j < len(lines) and lines[j].strip().startswith('|'):
                    row = [x.strip() for x in lines[j].strip().strip('|').split('|')]
                    if not all(set(x) <= set('-: ') for x in row):
                        rows.append(row)
                    j += 1
                if rows:
                    widths = [25, 58, 103, 86, 110, 101] if len(rows[0]) == 6 else [483 / len(rows[0])] * len(rows[0])
                    table(rows, widths)
                continue
            if line:
                paragraph(line.lstrip('# '), 'Heading2' if line.startswith('#') else 'Normal')
            j += 1

    paragraph('OLIST SELLER ANALYTICS', 'Subtitle')
    paragraph('Gestão de vendedores parceiros', 'Cover')
    paragraph('Análise descritiva de vendedores no e-commerce com dados públicos da Olist', 'Subtitle')
    paragraph('Guilherme Estrela · David Gabriel · Carlos Gabriel Raposo · Roger')
    story.append(Spacer(1, 24))
    paragraph('RELATÓRIO TÉCNICO - VERSÃO REVISADA', 'Heading2')
    paragraph('Revisão do grupo informada pelo solicitante em 18/11/2026. As respostas e o sumário vieram do solicitante, com revisão factual autorizada. A implementação, evidências e complementos técnicos receberam assistência de IA, documentada em uso_de_ia.md. A revisão informada não altera essa origem nem constitui validação independente.')
    story.append(PageBreak())
    paragraph('Parte A - Sumário executivo', 'Heading1')
    paragraph('Texto fornecido pelo solicitante; revisão factual autorizada.', 'Heading2')
    author_text = (REPORTS / 'secoes_autorais.md').read_text(encoding='utf-8')
    executive = author_text.split('## Parte A - Sumário executivo (máximo de uma página)', 1)[-1].split('## Resposta 1', 1)[0].strip()
    for block in (executive or '[Equipe preencher o sumário executivo.]').split('\n\n'):
        paragraph(block)
    paragraph('Texto integrado a partir das respostas recebidas. Revisão do grupo informada pelo solicitante em 18/11/2026.')
    story.append(PageBreak())
    paragraph('Parte B - Relatório técnico', 'Heading1')
    section('1. Problema e recorte', 'O projeto trata de gestão de vendedores parceiros: identificar atrasos de despacho, investigar a associação com avaliações e apoiar a discussão de critérios objetivos. A data de transportadora existe no nível do pedido. A análise individual usa pedidos com um único vendedor observado; isso não comprova responsabilidade e depende da cobertura dos itens recebidos. A contextualização complementar e as referências consultadas pela ferramenta aparecem na seção 12, sem atribuição de pesquisa aos integrantes.')
    section('2. Dados e relacionamentos', 'Fonte: Olist Brazilian E-Commerce Public Dataset, Kaggle. Cinco arquivos foram obtidos da fonte pública; hashes de cada original estão registrados em data/raw/proveniencia.json. Geolocalização não foi extraída nem utilizada. IDs de clientes e textos livres de avaliações não são incluídos na tabela final.')
    table([['Tabela', 'Linhas brutas', 'Colunas', 'Duplicatas exatas']] + [[k, v['rows'], v['columns'], v['duplicates']] for k, v in audit['before'].items()], [170, 105, 95, 113])
    paragraph('Itens -> produtos: N:1; itens agregados -> contagens por pedido: N:1; grupos -> pedidos: N:1; grupos -> vendedores: N:1; grupos -> avaliação única: N:1. Todas essas relações são validadas no código. A chave final é order_id + seller_id.')
    section('3. Ciclo de vida CRISP-DM', 'Compreensão do negócio: três perguntas do escopo. Compreensão dos dados: perfis, ausências, chaves e estatísticas. Preparação: limpeza, conversões, agregação e engenharia. A etapa de modelagem não inclui modelos de IA, classificação ou previsão, conforme o escopo descritivo adotado. Avaliação: testes, recortes reais e comparação de alternativas. Entrega: CSV, notebook, painel, relatório e repositório público. O proprietário confirmou o acesso público ao painel e informou a revisão do relatório pelo grupo.')
    section('4. Exploração e qualidade', f'Foram observados {audit["orders_without_items"]} pedidos sem itens correspondentes, que não geram linha pedido-vendedor; {audit["reviews_reduced"]} avaliações excedentes foram reduzidas a uma por pedido; {audit["multi_seller_orders"]} pedidos possuem mais de um vendedor observado. Há {audit["invalid_chronology_pairs"]} pares pedido-vendedor com alguma contradição temporal sinalizada. Cada duração possui sua própria máscara de validade; uma entrega ao cliente inconsistente não invalida automaticamente uma medição de despacho que seja coerente.')
    null_rows = [['Coluna de pedidos', 'Ausências originais']] + [[c, v] for c, v in audit['before']['orders']['nulls'].items() if v]
    if len(null_rows) > 1:
        table(null_rows, [350, 133])
    paragraph('Tipos carregados e ausências de todas as colunas: perfil_orders.csv, perfil_items.csv, perfil_products.csv, perfil_sellers.csv e perfil_reviews.csv. Estatísticas numéricas brutas e finais: estatisticas_brutas_*.csv e estatisticas_final.csv. A carga mantém as colunas como texto para preservar IDs; as conversões ocorrem no pipeline.')
    section('5. Limpeza e padronização', 'Duplicatas exatas são removidas; chaves ausentes são contabilizadas; chaves conflitantes interrompem a execução. Datas usam conversão segura e não são imputadas. Preços/fretes negativos ou inválidos viram ausências; somas de grupos incompletos continuam ausentes. Notas fora de 1 a 5 não entram na média. Categorias são normalizadas; UF inválida vira SEM_INFORMACAO. Textos de comentários usam NFKC, minúsculas e espaços simples; somente o comprimento é exportado. São propostas técnicas da ferramenta; suas justificativas autorais devem ser escritas pela equipe.')
    table([['Medida observada', 'Contagem']] + [[k, audit[k]] for k in ['invalid_price', 'invalid_freight_value', 'invalid_review_scores', 'orphan_items', 'missing_products', 'missing_sellers']], [350, 133])
    section('6. Outliers e impacto mensurável', 'O tempo de aprovação até a transportadora usa cercas Q1 - 1,5 IQR e Q3 + 1,5 IQR, ajustadas ao lote de pedidos elegíveis. O valor original é preservado. O clipping fica numa coluna demo_, sem alterar o indicador de atraso. A tabela abaixo compara alternativas; não representa uma justificativa autoral da equipe.')
    alternatives = pd.read_csv(REPORTS / 'alternativas_outliers.csv')
    table([['Alternativa', 'Linhas', 'Média em dias', 'Taxa de atraso']] + [[r.alternativa, r.linhas, f'{r.media_dias:.4f}', f'{r.taxa_atraso:.4%}'] for r in alternatives.itertuples()], [225, 65, 95, 98])
    image('distribuicao', 'Figura 1. Tempo até despacho, sem remover extremos; frequência em escala logarítmica.')
    section('7. Codificação, escalas e seleção', 'O status é codificado em delivered, shipped e other, com três colunas one-hot fixas. MinMaxScaler e StandardScaler são aplicados a sales_value apenas nas observações válidas; constantes viram zero e ausências são preservadas. As escalas são recalculadas para cada lote. IDs, texto livre e escalas redundantes são excluídos da lista de atributos analíticos. Variância populacional <= 1e-12 identifica constantes ou baixa variância; correlação absoluta >= 0,95 gera pares para inspeção, sem eliminar automaticamente medidas gerenciais necessárias. Lista exata e matriz: selecao_atributos.json e correlacoes.csv.')
    image('correlacao', 'Figura 2. Correlação de Pearson em pares completos; associação não estabelece causalidade.')
    section('8. Engenharia de atributos e denominadores', 'Foram aplicadas pelo menos quatro técnicas: diferenças temporais (dias até despacho, excesso, transporte e entrega); indicadores condicionais (atraso, avaliação negativa, elegibilidade); agregações por grupo (itens, valor, vendedores por pedido); extração temporal (mês e dia da semana). Há ainda razão frete/(itens + frete). Atraso de despacho compara timestamps; atraso ao cliente compara dias civis. O menor prazo dos itens é usado como aproximação conservadora e o maior prazo também é preservado. Algum item sem prazo exclui o grupo da taxa individual.')
    paragraph(f'Amostra analítica: {metadata["rows"]} linhas, {metadata["columns"]} colunas e {metadata["bytes"]} bytes. Pedidos elegíveis para despacho: {audit["eligible_dispatch"]}; elegíveis com avaliação: {audit["eligible_review"]}. O dicionário documenta todas as colunas. Uma linha não equivale sempre a um pedido distinto: pedidos multivendedor se repetem.')
    section('9. Evidências descritivas calculadas', 'Os gráficos e tabelas a seguir são saídas numéricas do pipeline, sem resposta autoral às perguntas de negócio. O ranking ilustrativo usa volume mínimo exploratório de 30 pedidos, ajustável no painel. IDs completos e denominadores estão nos CSVs de apoio.')
    image('ranking', 'Figura 3. Taxas por vendedor com pelo menos 30 pedidos elegíveis; IDs abreviados somente no gráfico.')
    image('temporal', 'Figura 4. Evolução mensal; os denominadores de cada mês estão em serie_mensal.csv.')
    comparison = pd.read_csv(REPORTS / 'comparacao_avaliacoes.csv')
    table([['Atraso despacho', 'Notas válidas', 'Nota média', 'Notas 1 ou 2']] + [[int(r.dispatch_late), int(r.review_count), f'{r.mean_score:.4f}', f'{r.negative_rate:.4%}'] for r in comparison.itertuples()], [145, 110, 110, 118])
    image('avaliacoes', 'Figura 5. Médias de avaliação por grupo de atraso; uma nota por pedido elegível.')
    paragraph('Foram disponibilizados cortes por mês e atraso ao cliente em avaliacoes_estratificadas.csv. Categorias, transporte, época e composição dos pedidos podem afetar as notas; não foi estimado efeito causal. O simulador do painel permite discutir parâmetros e não emite recomendação automática de advertência.')
    section('10. Pipeline e reprodutibilidade', 'A função preprocessar recebe cinco DataFrames brutos e retorna a tabela final, com evidências em attrs["audit"]. O comando python scripts/executar_pipeline.py executa todas as etapas. Para demonstração: python scripts/executar_pipeline.py --input data/amostra_bruta --output work/demonstracao --sem-graficos. O segundo comando mantém a base do painel preservada. Dependências, comandos completos e testes estão no README e em reports/verificacao.md.')
    section('11. Limites e validação humana', 'Amostras com itens faltantes podem subestimar o número de vendedores e alterar prazos e valores agregados. O pipeline não recupera dados não fornecidos. Avaliações multivendedor não são atribuídas individualmente na análise principal. A última resposta não garante que a nota se refira apenas ao despacho. Intervalos de Wilson descrevem incerteza da taxa sob aproximação binomial, sem corrigir dependência temporal ou confundimento. Os dados são históricos; não representam o desempenho atual dos parceiros.')
    story.append(PageBreak())
    heading('12. Respostas recebidas e validações da equipe')
    # [IA] registro 6: preservar as indicações de origem dos textos recebidos e dos complementos IA.
    markdown('## Resposta 1' + author_text.split('## Resposta 1', 1)[-1] if '## Resposta 1' in author_text else author_text)
    story.append(PageBreak())
    paragraph('Parte C - Diário de decisões', 'Heading1')
    paragraph('Justificativas técnicas assistidas por IA, com revisão do relatório informada pelo solicitante em 18/11/2026. A origem dos textos permanece registrada em uso_de_ia.md.')
    markdown((REPORTS / 'diario_de_decisoes.md').read_text(encoding='utf-8'))
    heading('Referências e transparência')
    paragraph('Olist: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Documentação técnica: pandas.pydata.org, scikit-learn.org e docs.streamlit.io. Registro de IA: uso_de_ia.md, com revisão técnica automatizada realizada.')
    pdf = REPORTS / 'relatorio_final.pdf'

    def footer(canvas, doc):
        canvas.setStrokeColor(colors.HexColor('#CCD6E0'))
        canvas.line(50, 40, 545, 40)
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#405B80'))
        canvas.drawString(50, 27, 'Equipe do projeto | Gestão de Vendedores Parceiros')
        canvas.drawRightString(545, 27, str(doc.page))

    SimpleDocTemplate(str(pdf), pagesize=A4, rightMargin=50, leftMargin=50, topMargin=48, bottomMargin=55, invariant=1,
        title='Equipe do projeto - Gestão de Vendedores Parceiros', author='Equipe do projeto - conteúdo técnico assistido por IA').build(story, onFirstPage=footer, onLaterPages=footer)
    (REPORTS / 'relatorio_tecnico.md').write_text('# Parte B - Conteúdo técnico automático\n\n' + '\n'.join(technical), encoding='utf-8')
    print(f'PDF técnico gerado: {pdf.name}. Revisão do grupo registrada conforme declaração do solicitante.')


if __name__ == '__main__':
    main()
