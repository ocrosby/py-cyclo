# tests/services/test_complexity_service.py
# pylint: disable=redefined-outer-name

from unittest.mock import mock_open

import pytest
from radon.visitors import Function

from py_cyclo.services.complexity_service import ComplexityService


@pytest.fixture
def complexity_service():
    return ComplexityService()


def test_get_files_to_analyze(mocker, complexity_service):
    # Arrange
    mocker.patch(
        "os.walk",
        return_value=[
            ("/path", ["dir1", "dir2"], ["file1.py", "file2.py"]),
            ("/path/dir1", [], ["file3.py"]),
            ("/path/dir2", [], ["file4.py"]),
        ],
    )
    exclude_dirs = {"dir2"}
    expected_files = [
        "/path/file1.py",
        "/path/file2.py",
        "/path/dir1/file3.py",
        "/path/dir2/file4.py",
    ]

    # Act
    files_to_analyze = complexity_service.get_files_to_analyze("/path", exclude_dirs)

    #
    assert files_to_analyze == expected_files


def test_analyze_files(mocker, complexity_service):
    mock_open_instance = mock_open(read_data="def foo(): pass")
    mocker.patch("builtins.open", mock_open_instance)
    mocker.patch(
        "radon.complexity.cc_visit",
        return_value=[
            Function(
                name="foo",
                lineno=1,
                col_offset=0,
                endline=1,
                is_method=False,
                classname=None,
                complexity=1,
                closures=None,
            )
        ],
    )
    files_to_analyze = ["/path/file1.py"]
    results = complexity_service.analyze_files(files_to_analyze)
    assert len(results) == 1
    assert results[0].name == "foo"


def test_get_max_score(complexity_service):
    functions = [
        Function(
            name="foo",
            lineno=1,
            col_offset=0,
            endline=1,
            is_method=False,
            classname=None,
            complexity=5,
            closures=None,
        ),
        Function(
            name="bar",
            lineno=2,
            col_offset=0,
            endline=2,
            is_method=False,
            classname=None,
            complexity=10,
            closures=None,
        ),
    ]
    max_score = complexity_service.get_max_score(functions)
    assert max_score == 10


def test_get_functions_exceeding_complexity(complexity_service):
    functions = [
        Function(
            name="foo",
            lineno=1,
            col_offset=0,
            endline=1,
            is_method=False,
            classname=None,
            complexity=5,
            closures=None,
        ),
        Function(
            name="bar",
            lineno=2,
            col_offset=0,
            endline=2,
            is_method=False,
            classname=None,
            complexity=10,
            closures=None,
        ),
    ]
    exceeding_functions = complexity_service.get_functions_exceeding_complexity(
        functions, 6
    )
    assert len(exceeding_functions) == 1
    assert exceeding_functions[0].name == "bar"


def test_get_functions_within_complexity(complexity_service):
    functions = [
        Function(
            name="foo",
            lineno=1,
            col_offset=0,
            endline=1,
            is_method=False,
            classname=None,
            complexity=5,
            closures=None,
        ),
        Function(
            name="bar",
            lineno=2,
            col_offset=0,
            endline=2,
            is_method=False,
            classname=None,
            complexity=10,
            closures=None,
        ),
    ]
    within_functions = complexity_service.get_functions_within_complexity(functions, 6)
    assert len(within_functions) == 1
    assert within_functions[0].name == "foo"
