import pytest
from py_cyclo.tools.display import display_exceeded_complexity, display_radon_results

def test_display_exceeded_complexity_no_results(capsys):
    results = {}
    display_exceeded_complexity(results, 10)
    captured = capsys.readouterr()
    assert captured.out == "File\tFunction\tComplexity\tScore\n"

def test_display_exceeded_complexity_no_exceeding(capsys):
    results = {
        "module1": [{"name": "func1", "complexity": 5, "score": 5}]
    }
    display_exceeded_complexity(results, 10)
    captured = capsys.readouterr()
    assert captured.out == "File\tFunction\tComplexity\tScore\n"

def test_display_exceeded_complexity_exceeding(capsys):
    results = {
        "module1": [{"name": "func1", "complexity": 15, "score": 15}]
    }
    display_exceeded_complexity(results, 10)
    captured = capsys.readouterr()
    assert "module1\tfunc1\t15\t15\n" in captured.out

def test_display_exceeded_complexity_multiple_files(capsys):
    results = {
        "module1": [{"name": "func1", "complexity": 5, "score": 5}],
        "module2": [{"name": "func2", "complexity": 20, "score": 20}]
    }
    display_exceeded_complexity(results, 10)
    captured = capsys.readouterr()
    assert "module2\tfunc2\t20\t20\n" in captured.out

def test_display_radon_results_no_results(capsys):
    results = {}
    display_radon_results(results)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_display_radon_results_single_file(capsys):
    results = {
        "module1": [{"name": "func1", "complexity": 5, "score": 5}]
    }
    display_radon_results(results)
    captured = capsys.readouterr()
    assert "File: module1" in captured.out
    assert "Function: func1, Complexity: 5, Score: 5" in captured.out

def test_display_radon_results_multiple_files(capsys):
    results = {
        "module1": [{"name": "func1", "complexity": 5, "score": 5}],
        "module2": [{"name": "func2", "complexity": 10, "score": 10}]
    }
    display_radon_results(results)
    captured = capsys.readouterr()
    assert "File: module1" in captured.out
    assert "Function: func1, Complexity: 5, Score: 5" in captured.out
    assert "File: module2" in captured.out
    assert "Function: func2, Complexity: 10, Score: 10" in captured.out

def test_display_radon_results_empty_functions(capsys):
    results = {
        "module1": []
    }
    display_radon_results(results)
    captured = capsys.readouterr()
    assert "File: module1" in captured.out
    assert "Function:" not in captured.out