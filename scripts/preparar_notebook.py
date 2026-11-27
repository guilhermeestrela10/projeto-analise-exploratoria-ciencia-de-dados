"""Cria e executa o notebook usando o interpretador Python atual."""
# [IA] registro 3
import os
from pathlib import Path
import sys
import nbformat as nbf
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]


def main():
    nb = nbf.v4.new_notebook()
    md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
    nb.cells = [
        md('# Olist Seller Analytics\nAnálise exploratória de vendedores.\n\nNotebook técnico assistido por IA, registro 3. Conclusões e justificativas ficam para autoria humana. Os dados usados são os originais Olist.'),
        code('# [IA] registro 3\nfrom pathlib import Path\nimport sys, json\nroot = Path.cwd()\nif not (root / "src").exists():\n    root = root.parent\nsys.path.insert(0, str(root))\nfrom src.load_data import load_data\nfrom src.preprocessing import preprocessar, profile\nfrom src.analysis import seller_metrics, review_comparison, selection_report\nfrom src.visualizations import ranking_chart, review_chart\nimport pandas as pd\nimport matplotlib.pyplot as plt\nraw = load_data(root / "data/raw")\nnames = ["orders", "items", "products", "sellers", "reviews"]'),
        md('## 1. Compreensão do negócio e dos dados\nObjetivo: fornecer evidências sobre despacho e avaliações. Não há modelagem preditiva. Chaves: pedido, pedido-item, produto, vendedor. Avaliações podem se repetir por pedido.'),
        code('# [IA] registro 3\npd.DataFrame([{ "tabela": n, "linhas": len(d), "colunas": len(d.columns), "duplicatas": int(d.duplicated().sum())} for n,d in zip(names,raw)])'),
        code('# [IA] registro 3\nfor name, frame in zip(names, raw):\n    print(name)\n    display(pd.DataFrame({"tipo_carregado": frame.dtypes.astype(str), "nulos": frame.isna().sum(), "distintos": frame.nunique()}))\ndisplay(raw[1][["price", "freight_value"]].apply(pd.to_numeric).describe())\ndisplay(pd.to_numeric(raw[4].review_score).value_counts().sort_index())'),
        md('## 2. Pipeline de preparação e histórico de merges\n`preprocessar` executa todas as etapas sem células manuais: validação, cópia, duplicatas, chaves, tipos, datas, categorias, textos, agregações, merges e engenharia. Itens-produtos N:1; agregação pedido-vendedor; contagens por pedido N:1; pedidos N:1; vendedores N:1; avaliação única N:1. Textos livres não são exportados.'),
        code('# [IA] registro 1\ntabela = preprocessar(*raw)\naudit = tabela.attrs["audit"]\nprint("Tabela final:", tabela.shape)\nprint("Chave repetida:", tabela.duplicated(["order_id", "seller_id"]).sum())\nprint({k: audit[k] for k in ["reviews_reduced", "orders_without_items", "multi_seller_orders", "invalid_chronology_pairs", "eligible_dispatch", "eligible_review"]})'),
        md('## 3. Limpeza, ausências e impacto\nAs medidas gerenciais preservam extremos. Datas, notas e dinheiro não são imputados. Consultar evidências antes de redigir as justificativas humanas. O CSV antes/depois registra linhas e duplicatas; alternativas_outliers quantifica remoção e clipping.'),
        code('# [IA] registro 3\nprint("Datas inválidas:", audit["invalid_dates"])\ndisplay(pd.DataFrame({"nulos_finais": tabela.isna().sum(), "tipo": tabela.dtypes.astype(str)}))\ndisplay(pd.read_csv(root / "reports/antes_depois.csv"))\ndisplay(pd.read_csv(root / "reports/alternativas_outliers.csv"))'),
        md('## 4. Transformações e seleção\nOne-hot de status com esquema fixo; MinMax e Z-score de sales_value; clipping IQR somente demonstrativo. Atributos originais ficam preservados. Seleção semântica, variância populacional <= 1e-12 e inspeção de correlações >= 0,95 em módulo.'),
        code('# [IA] registro 1\ndisplay(tabela[["sales_value", "demo_sales_minmax", "demo_sales_zscore", "demo_status_delivered", "demo_status_shipped", "demo_status_other"]].head())\nselection, correlations = selection_report(tabela)\nprint(json.dumps(selection, ensure_ascii=False, indent=2))\ndisplay(correlations)'),
        md('## 5. Engenharia de atributos\nTécnicas distintas: diferenças temporais; indicadores condicionais; agregação de itens/pedidos por grupo; extração de mês e dia da semana; razão entre frete e valor. A comparação individual exclui pedidos multivendedor observados.'),
        code('# [IA] registro 1\ndisplay(tabela[["approval_to_carrier_days", "dispatch_delay_days", "dispatch_late", "transport_days", "delivery_late", "item_count", "purchase_month", "purchase_weekday", "freight_share"]].describe(include="all"))'),
        md('## 6. Evidências para as perguntas do escopo\nAs tabelas abaixo são resultados calculados. A equipe deve produzir as respostas de negócio e conclusões; associação não implica causalidade.'),
        code('# [IA] registro 2\nmetrics = seller_metrics(tabela)\ndisplay(metrics[metrics.eligible_orders.ge(30)].head(15))\ncomparison = review_comparison(tabela)\ndisplay(comparison)\ndisplay(tabela[tabela.eligible_dispatch].groupby("purchase_month").dispatch_late.agg(["mean", "count"]))\ndisplay(tabela[tabela.eligible_review].groupby(["dispatch_late", "delivery_late"], dropna=False).review_score.agg(["mean", "count"]))'),
        code('# [IA] registro 2\ndisplay(ranking_chart(metrics[metrics.eligible_orders.ge(30)]))\ndisplay(review_chart(comparison))\nplt.close("all")'),
        md('## 7. Validação da reprodução em recortes reais\nA amostra preserva itens e dimensões dos pedidos sorteados. Um recorte independente pode não possuir correspondência. A cobertura dos itens é indispensável para interpretar vendedor único.'),
        code('# [IA] registro 3\no, i, p, s, r = raw\nosmall = o.sample(20, random_state=4)\nismall = i[i.order_id.isin(osmall.order_id)]\nsmall = preprocessar(osmall, ismall, p[p.product_id.isin(ismall.product_id)], s[s.seller_id.isin(ismall.seller_id)], r[r.order_id.isin(osmall.order_id)])\nassert not small.duplicated(["order_id", "seller_id"]).any()\nassert len(small) == len(ismall[["order_id", "seller_id"]].drop_duplicates())\nprint("Recorte real:", small.shape)\ndisplay(small[["order_id", "seller_id", "eligible_dispatch", "dispatch_late"]].head())'),
        md('## 8. Campos de autoria humana\nRespostas de negócio: preencher no painel e relatório. Justificativas: preencher diário de decisões. Conclusões: escrever pela equipe após validar os resultados. Não atribuir automaticamente estes resultados a revisão dos integrantes.')]
    nb.metadata['kernelspec'] = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
    nb.metadata['language_info'] = {'name': 'python', 'version': sys.version.split()[0]}
    # Kernel temporário local usa o mesmo Python do comando; não instala kernel global.
    kernel = ROOT / 'work/jupyter/kernels/olist-local'
    kernel.mkdir(parents=True, exist_ok=True)
    (kernel / 'kernel.json').write_text(__import__('json').dumps({'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'], 'display_name': 'Olist local', 'language': 'python'}), encoding='utf-8')
    os.environ['JUPYTER_PATH'] = str(ROOT / 'work/jupyter')
    client = NotebookClient(nb, timeout=1200, kernel_name='olist-local', resources={'metadata': {'path': str(ROOT)}})
    client.execute()
    path = ROOT / 'notebooks/analise_exploratoria.ipynb'
    path.parent.mkdir(exist_ok=True)
    nbf.write(nb, path)
    print(f'Notebook executado e salvo: {len(nb.cells)} células.')


if __name__ == '__main__':
    main()
