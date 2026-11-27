"""Interface gerencial; a única fonte numérica é o CSV analítico final."""
# [IA] registro 2
import json
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from .load_data import ROOT
from .analysis import filter_data, seller_metrics, review_comparison, monitoring_metrics
from .visualizations import ranking_chart, review_chart


@st.cache_data
def read_final(path, modified_ns):
    d = pd.read_csv(path, dtype={'order_id': 'string', 'seller_id': 'string'})
    for c in ['eligible_dispatch', 'eligible_review', 'invalid_chronology', 'deadlines_complete', 'dispatch_time_outlier']:
        d[c] = d[c].astype('string').str.lower().eq('true')
    d['order_purchase_timestamp'] = pd.to_datetime(d.order_purchase_timestamp, errors='coerce')
    return d


def conclusion(key):
    path = ROOT / 'reports/conclusoes_equipe.json'
    content = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    text = content.get(key, '').strip()
    st.subheader('Conclusão da equipe')
    if text:
        st.write(text)
    else:
        st.info('Texto de autoria humana pendente. A equipe deve interpretar os dados e escrever sua resposta antes da entrega.')


def show_figure(fig):
    st.pyplot(fig)
    plt.close(fig)


def friendly_metrics(metrics):
    shown = metrics.copy()
    for col in ['late_rate', 'negative_rate', 'late_ci_low', 'late_ci_high']:
        shown[col] = (shown[col] * 100).round(2)
    return shown.round(2).rename(columns={'seller_id': 'Vendedor', 'observed_orders': 'Pedidos observados',
        'sales_value': 'Valor dos itens (R$)', 'eligible_orders': 'Pedidos elegíveis', 'late_orders': 'Pedidos atrasados',
        'late_rate': 'Atrasos (%)', 'mean_delay_days': 'Excesso médio (dias)', 'median_dispatch_days': 'Mediana até despacho (dias)',
        'review_count': 'Pedidos com nota', 'mean_score': 'Nota média', 'negative_count': 'Notas 1 ou 2',
        'negative_rate': 'Notas negativas (%)', 'late_ci_low': 'Limite inferior 95% (%)', 'late_ci_high': 'Limite superior 95% (%)',
        'cenario': 'Resultado do cenário', 'mean_business_days': 'Média até despacho (dias úteis)',
        'above_tad_limit': 'TAD acima de 10%', 'below_score_floor': 'Nota abaixo de 3,8'})


def render(page):
    st.set_page_config(page_title='Parceiros | Olist Seller Analytics', layout='wide')
    st.sidebar.title('Parceiros Olist')
    for path, label in [('app.py', 'Visão geral'), ('pages/1_Atrasos_no_Despacho.py', 'Atrasos no despacho'),
            ('pages/2_Atrasos_e_Avaliacoes.py', 'Atrasos e avaliações'), ('pages/3_Criterios_para_Vendedores.py', 'Critérios de acompanhamento')]:
        st.sidebar.page_link(path, label=label)
    st.caption('Olist Seller Analytics · Indicadores de vendedores')
    titles = {'inicio': 'Gestão de vendedores parceiros', 'atrasos': 'Quais vendedores mais atrasam o despacho?',
              'avaliacoes': 'Vendedores que atrasam recebem avaliações piores?',
              'criterios': 'Critérios para acompanhar vendedores'}
    st.title(titles[page])
    st.write('Acompanhe prazos e avaliações dos parceiros no período selecionado.')
    path = ROOT / 'data/processed/tabela_analitica.csv'
    if not path.exists():
        st.info('Base analítica ainda indisponível. Execute o pipeline descrito no README.')
        st.stop()
    d = read_final(str(path), path.stat().st_mtime_ns)
    st.sidebar.header('Recorte da análise')
    states = st.sidebar.multiselect('Estado do vendedor', sorted(d.seller_state.dropna().unique()), key='states')
    sellers = st.sidebar.multiselect('Vendedor (ID)', sorted(d.seller_id.dropna().unique()), key='sellers')
    valid_dates = d.order_purchase_timestamp.dropna()
    start = end = None
    if not valid_dates.empty:
        dates = st.sidebar.date_input('Período da compra', value=(valid_dates.min().date(), valid_dates.max().date()),
            min_value=valid_dates.min().date(), max_value=valid_dates.max().date(), key='period')
        if len(dates) != 2:
            st.info('Selecione a data inicial e a data final.')
            st.stop()
        start, end = dates
    d = filter_data(d, states, sellers, start, end)
    if d.empty:
        st.info('Nenhum pedido neste recorte. Ajuste os filtros.')
        st.stop()
    eligible = d[d.eligible_dispatch]
    reviewed = d[d.eligible_review]
    cols = st.columns(4)
    cols[0].metric('Pedidos no recorte', f'{d.order_id.nunique():,}'.replace(',', '.'))
    cols[1].metric('Despachos elegíveis', f'{len(eligible):,}'.replace(',', '.'))
    rate = eligible.dispatch_late.mean()
    cols[2].metric('Taxa de atraso', f'{rate:.1%}'.replace('.', ',') if pd.notna(rate) else 'Sem dados')
    cols[3].metric('Pedidos com nota', f'{len(reviewed):,}'.replace(',', '.'))
    st.caption('Taxa = pedidos com despacho após o prazo / pedidos elegíveis. Um pedido elegível tem um único vendedor observado, datas coerentes e prazo em todos os itens.')
    st.warning('A data de despacho é do pedido inteiro. Pedidos com vários vendedores ficam fora da comparação individual. Em amostras parciais, um vendedor observado não comprova vendedor único na base completa.')
    metrics = seller_metrics(d)
    if page == 'inicio':
        st.subheader('Três perguntas, uma base de evidências')
        st.page_link('pages/1_Atrasos_no_Despacho.py', label='1. Atrasos no despacho')
        st.page_link('pages/2_Atrasos_e_Avaliacoes.py', label='2. Atrasos e avaliações')
        st.page_link('pages/3_Criterios_para_Vendedores.py', label='3. Critérios de acompanhamento')
        st.write('Atraso no despacho compara a entrega à transportadora ao menor prazo dos itens. Atraso ao cliente compara a data de entrega ao dia prometido.')
        st.caption('Base histórica Olist; nenhum modelo de previsão foi utilizado. Dados agregados não demonstram causalidade.')
    elif page == 'atrasos':
        minimum = st.sidebar.number_input('Mínimo de pedidos elegíveis', 1, 10000, 30, key='min_orders')
        ranked = metrics[metrics.eligible_orders.ge(minimum)]
        st.subheader('Frequência e intensidade no recorte')
        if ranked.empty:
            st.info('Nenhum vendedor alcançou o volume mínimo informado.')
        else:
            show_figure(ranking_chart(ranked))
        st.dataframe(friendly_metrics(ranked), hide_index=True)
        st.caption('Excesso médio: max(despacho - prazo, 0) em todos os pedidos elegíveis. Intervalos de Wilson indicam incerteza amostral; o volume mínimo é um filtro exploratório.')
        monthly = eligible.groupby('purchase_month').dispatch_late.agg(['mean', 'count'])
        st.subheader('Evolução mensal')
        st.line_chart((monthly['mean'] * 100).rename('Atrasos (%)').rename_axis('Mês da compra'))
        monthly['mean'] *= 100
        st.dataframe(monthly.round(2).rename(columns={'mean': 'Atrasos (%)', 'count': 'Pedidos elegíveis'}).rename_axis('Mês da compra'))
    elif page == 'avaliacoes':
        comparison = review_comparison(d)
        show_figure(review_chart(comparison))
        displayed = comparison.copy()
        displayed['dispatch_late'] = displayed.dispatch_late.map({0: 'Em prazo', 1: 'Com atraso'})
        displayed['negative_rate'] *= 100
        st.dataframe(displayed.rename(columns={'dispatch_late': 'Despacho', 'review_count': 'Pedidos avaliados',
            'mean_score': 'Nota média', 'negative_rate': 'Notas 1 ou 2 (%)'}), hide_index=True)
        st.caption('Uma avaliação por pedido: última resposta registrada, com desempate determinístico. Notas 1 e 2 são negativas. Ausências ficam fora do denominador.')
        st.subheader('Comparação entre vendedores')
        if not metrics.dropna(subset=['mean_score', 'late_rate']).empty:
            points = friendly_metrics(metrics.dropna(subset=['mean_score', 'late_rate']))
            st.scatter_chart(points, x='Atrasos (%)', y='Nota média', size='Pedidos com nota')
        st.subheader('Controle descritivo por atraso ao cliente')
        strata = reviewed.groupby(['dispatch_late', 'delivery_late'], dropna=False).agg(
            pedidos=('order_id', 'size'), nota_media=('review_score', 'mean')).reset_index()
        for c in ['dispatch_late', 'delivery_late']:
            strata[c] = strata[c].map({0: 'Em prazo', 1: 'Com atraso'}).fillna('Sem informação')
        st.dataframe(strata.rename(columns={'dispatch_late': 'Despacho', 'delivery_late': 'Entrega ao cliente',
            'pedidos': 'Pedidos avaliados', 'nota_media': 'Nota média'}).round(2), hide_index=True)
        st.caption('Associação não implica causalidade. Transporte, categoria, período e perfil do pedido podem afetar as notas. O recorte por atraso ao cliente é descritivo.')
    elif page == 'criterios':
        # [IA] registro 5: definições e limites aprovados pelo solicitante.
        st.subheader('Critérios propostos pela equipe')
        recent, first_day, last_day = monitoring_metrics(d)
        if first_day is not None:
            st.caption(f'Compras de {first_day:%d/%m/%Y} a {last_day:%d/%m/%Y}: últimos 30 dias até a última compra do recorte filtrado, não até a data atual.')
        if not recent.empty:
            st.dataframe(friendly_metrics(recent), hide_index=True)
        st.caption('TAD > 10%; nota média < 3,8. Cada pedido elegível com nota tem peso 1: soma das notas / quantidade de notas. Dias úteis: segunda a sexta no intervalo da aprovação até o despacho, sem feriados. O tempo médio é acompanhado sem limite automático, pois a equipe não definiu esse limite. Volumes e ausências devem ser considerados antes de qualquer advertência.')
        st.subheader('Simulador de critérios para discussão da equipe')
        st.write('Os valores abaixo são parâmetros exploratórios. A equipe deve definir e justificar os critérios finais.')
        minimum = st.number_input('Volume mínimo de pedidos elegíveis', 1, 10000, 30)
        threshold = st.slider('Limiar de atraso do cenário (%)', 0, 100, 10)
        metrics['cenario'] = 'Abaixo do volume informado'
        volume = metrics.eligible_orders.ge(minimum)
        metrics.loc[volume, 'cenario'] = 'Dentro do limiar informado'
        metrics.loc[volume & metrics.late_rate.gt(threshold / 100), 'cenario'] = 'Acima do limiar informado'
        st.dataframe(friendly_metrics(metrics), hide_index=True)
        st.caption('A classificação não é recomendação de advertência. Validar os registros, observar recorrência mensal, comparar mix e ouvir o vendedor antes de decidir.')
    conclusion(page)
    st.download_button('Baixar o recorte analítico (CSV)', d.to_csv(index=False).encode('utf-8'), 'recorte_analitico.csv', 'text/csv')
    st.caption('Fonte: Olist / Kaggle. Implementação assistida por IA declarada no repositório. Conclusões finais: autoria dos integrantes.')
