"""Localiza campos vazios e rascunhos IA; não comprova autoria ou aprovação humana."""
# [IA] registro 4
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def verificar_autoria(root):
    reports = Path(root) / 'reports'
    pending = []
    try:
        conclusions = json.loads((reports / 'conclusoes_equipe.json').read_text(encoding='utf-8'))
        if not isinstance(conclusions, dict) or any(not isinstance(conclusions.get(k), str) or not conclusions[k].strip() or '[equipe ' in conclusions[k].lower()
                for k in ['inicio', 'atrasos', 'avaliacoes', 'criterios']):
            pending.append('Preencher as conclusões e respostas do painel com texto da equipe.')
    except (OSError, ValueError):
        pending.append('Arquivo de conclusões ausente ou inválido.')
    for name in ['secoes_autorais.md', 'diario_de_decisoes.md']:
        try:
            text = (reports / name).read_text(encoding='utf-8').strip()
        except OSError:
            text = ''
        if not text or '[equipe ' in text.lower() or '[rascunho ia]' in text.lower():
            pending.append(f'Concluir a autoria humana de reports/{name}: campo vazio, marcador ou rascunho IA identificado.')
    return pending


if __name__ == '__main__':
    pending = verificar_autoria(ROOT)
    for item in pending:
        print(f'PENDENTE: {item}')
    if pending:
        print('REVISÃO DE AUTORIA PENDENTE: ainda existem pendências de autoria humana.')
    else:
        print('Nenhum campo textual vazio identificado. Conferir autoria, PDF, commits reais e links publicados antes de publicar.')
    raise SystemExit(1 if pending else 0)
