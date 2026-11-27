# [IA] registro 4
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from verificar_autoria import verificar_autoria


def test_reports_unfilled_authorial_sections(tmp_path):
    reports = tmp_path / 'reports'
    reports.mkdir()
    (reports / 'conclusoes_equipe.json').write_text(json.dumps({'inicio': '', 'atrasos': '', 'avaliacoes': '', 'criterios': ''}))
    (reports / 'secoes_autorais.md').write_text('[Equipe escrever o texto.]', encoding='utf-8')
    (reports / 'diario_de_decisoes.md').write_text('| [Equipe redigir] |', encoding='utf-8')
    pending = verificar_autoria(tmp_path)
    assert any('conclusões' in p for p in pending)
    assert any('secoes_autorais' in p for p in pending)
    assert any('diario_de_decisoes' in p for p in pending)


def test_missing_or_broken_authorial_files_are_pending(tmp_path):
    assert verificar_autoria(tmp_path)
    (tmp_path / 'reports').mkdir()
    (tmp_path / 'reports/conclusoes_equipe.json').write_text('{ quebrado')
    assert any('inválido' in p for p in verificar_autoria(tmp_path))


def test_returns_no_textual_pending_for_completed_fixture(tmp_path):
    # Conteúdo de teste; não é texto de entrega nem conclusão de produção.
    reports = tmp_path / 'reports'
    reports.mkdir()
    (reports / 'conclusoes_equipe.json').write_text(json.dumps(dict.fromkeys(['inicio','atrasos','avaliacoes','criterios'], 'Texto de teste')))
    for name in ['secoes_autorais.md', 'diario_de_decisoes.md']:
        (reports / name).write_text('Texto de teste preenchido.', encoding='utf-8')
    assert verificar_autoria(tmp_path) == []


def test_json_placeholders_are_pending_even_when_not_empty(tmp_path):
    reports = tmp_path / 'reports'
    reports.mkdir()
    (reports / 'conclusoes_equipe.json').write_text(json.dumps(dict.fromkeys(
        ['inicio', 'atrasos', 'avaliacoes', 'criterios'], '[Equipe escrever]')))
    for name in ['secoes_autorais.md', 'diario_de_decisoes.md']:
        (reports / name).write_text('Texto de teste preenchido.', encoding='utf-8')
    assert any('conclusões' in p for p in verificar_autoria(tmp_path))


def test_complete_ai_drafts_still_require_human_authorship(tmp_path):
    reports = tmp_path / 'reports'
    reports.mkdir()
    (reports / 'conclusoes_equipe.json').write_text(json.dumps(dict.fromkeys(
        ['inicio', 'atrasos', 'avaliacoes', 'criterios'], 'Texto fornecido no teste')))
    for name in ['secoes_autorais.md', 'diario_de_decisoes.md']:
        (reports / name).write_text('[RASCUNHO IA]\nTexto completo para revisão.', encoding='utf-8')
    pending = verificar_autoria(tmp_path)
    assert any('secoes_autorais' in p for p in pending)
    assert any('diario_de_decisoes' in p for p in pending)
