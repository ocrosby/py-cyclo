# tests/views/test_complexity_view.py
# pylint: disable=redefined-outer-name

import pytest

from py_cyclo.views.complexity_view import ComplexityView


@pytest.fixture
def complexity_view():
    return ComplexityView()


def test_display_complexity_table(mocker, capsys, complexity_view):
    mocker.patch("os.path.relpath", side_effect=lambda x: x)
    results = [
        mocker.Mock(name="foo", complexity=10, lineno=1, filename="/path/file1.py"),
        mocker.Mock(name="bar", complexity=5, lineno=2, filename="/path/file2.py"),
    ]
    complexity_view.display_complexity_table(results)
    captured = capsys.readouterr()
    assert "foo" in captured.out
    assert "bar" in captured.out
    assert "10" in captured.out
    assert "5" in captured.out
    assert "/path/file1.py" in captured.out
    assert "/path/file2.py" in captured.out


def test_display_complexity_table_no_results(capsys, complexity_view):
    with pytest.raises(SystemExit):
        complexity_view.display_complexity_table([])
    captured = capsys.readouterr()
    assert "No output from radon." in captured.out


def test_display_radon_results(mocker, capsys, complexity_view):
    result_foo = mocker.Mock(name="foo", complexity=10)
    result_foo.name = "foo"
    result_bar = mocker.Mock(name="bar", complexity=5)
    result_bar.name = "bar"
    results = [result_foo, result_bar]

    complexity_view.display_radon_results(results)
    captured = capsys.readouterr()
    assert "Cyclomatic Complexity Results:" in captured.out
    assert "foo: 10" in captured.out
    assert "bar: 5" in captured.out


def test_display_radon_results_no_results(capsys, complexity_view):
    with pytest.raises(SystemExit):
        complexity_view.display_radon_results([])
    captured = capsys.readouterr()
    assert "No output from radon." in captured.out


def test_display_exceeded_complexity(mocker, capsys, complexity_view):
    result_foo = mocker.Mock(name="foo", complexity=10)
    result_foo.name = "foo"
    result_bar = mocker.Mock(name="bar", complexity=5)
    result_bar.name = "bar"
    results = [result_foo, result_bar]

    complexity_view.display_exceeded_complexity(results, 6)
    captured = capsys.readouterr()
    assert "Functions with complexity greater than the maximum allowed:" in captured.out
    assert "foo: 10" in captured.out
    assert "bar: 5" not in captured.out


def test_display_exceeded_complexity_no_results(capsys, complexity_view):
    with pytest.raises(SystemExit):
        complexity_view.display_exceeded_complexity([], 6)
    captured = capsys.readouterr()
    assert "No output from radon." in captured.out


def test_display_max_score_not_exceeded(capsys, complexity_view):
    complexity_view.display_max_score_not_exceeded(10)
    captured = capsys.readouterr()
    assert "Maximum complexity not exceeded: 10" in captured.out
