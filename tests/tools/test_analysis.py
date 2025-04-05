# tests/test_analysis.py
from py_cyclo.tools.analysis import get_max_score


def test_get_max_score_empty():
    results = {}
    assert get_max_score(results) == 0


def test_get_max_score_single_function():
    results = {"module1": [{"name": "func1", "score": 5}]}
    assert get_max_score(results) == 5


def test_get_max_score_multiple_functions():
    results = {
        "module1": [{"name": "func1", "score": 5}, {"name": "func2", "score": 10}],
        "module2": [{"name": "func3", "score": 7}],
    }
    assert get_max_score(results) == 10


def test_get_max_score_tied_scores():
    results = {
        "module1": [{"name": "func1", "score": 10}],
        "module2": [{"name": "func2", "score": 10}],
    }
    assert get_max_score(results) == 10


def test_get_max_score_negative_scores():
    results = {
        "module1": [{"name": "func1", "score": -5}, {"name": "func2", "score": -10}]
    }
    assert get_max_score(results) == 0
