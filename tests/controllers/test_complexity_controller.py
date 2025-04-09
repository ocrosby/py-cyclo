# tests/controllers/test_complexity_controller.py
# pylint: disable=redefined-outer-name

import pytest
from radon.visitors import Function

from py_cyclo.controllers.complexity_controller import ComplexityController


@pytest.fixture
def mock_service(mocker):
    return mocker.Mock()


@pytest.fixture
def mock_model(mocker):
    return mocker.Mock()


@pytest.fixture
def mock_view(mocker):
    return mocker.Mock()


@pytest.fixture
def complexity_controller(mock_service, mock_model, mock_view):
    return ComplexityController(mock_service, mock_model, mock_view)


def test_check_complexity_no_files_to_analyze(
    mocker, complexity_controller, mock_model, mock_service, mock_view
):
    # Arrange
    mock_model.path = "/path"
    mock_model.exclude_dirs = {".venv", "tests", "node_modules"}
    mock_service.get_files_to_analyze.return_value = []
    mocker.patch("os.path.abspath", return_value="/path")

    # Act
    with pytest.raises(SystemExit) as e:
        complexity_controller.check_complexity()

    # Assert
    assert e.value.code == 0
    mock_view.display_complexity_table.assert_not_called()


def test_check_complexity_no_results(
    mocker, complexity_controller, mock_model, mock_service, mock_view
):
    # Arrange
    mock_model.path = "/path"
    mock_model.exclude_dirs = {".venv", "tests", "node_modules"}
    mock_service.get_files_to_analyze.return_value = ["/path/file1.py"]
    mock_service.analyze_files.return_value = []
    mocker.patch("os.path.abspath", return_value="/path")

    # Act
    with pytest.raises(SystemExit) as e:
        complexity_controller.check_complexity()

    # Assert
    assert e.value.code == 1
    mock_view.display_complexity_table.assert_not_called()


def test_check_complexity_exceeding_functions(
    mocker, complexity_controller, mock_model, mock_service, mock_view
):
    # Arrange
    mock_model.path = "/path"
    mock_model.exclude_dirs = {".venv", "tests", "node_modules"}
    mock_model.max_complexity = 5
    mock_service.get_files_to_analyze.return_value = ["/path/file1.py"]
    results = [
        Function(
            name="foo",
            lineno=1,
            col_offset=0,
            endline=1,
            is_method=False,
            classname=None,
            complexity=10,
            closures=None,
        ),
        Function(
            name="bar",
            lineno=2,
            col_offset=0,
            endline=2,
            is_method=False,
            classname=None,
            complexity=3,
            closures=None,
        ),
    ]
    mock_service.analyze_files.return_value = results
    mock_service.get_functions_exceeding_complexity.return_value = [results[1]]
    mock_service.get_functions_within_complexity.return_value = [results[0]]
    mock_service.get_max_score.return_value = 10
    mocker.patch("os.path.abspath", return_value="/path")

    # Act
    with pytest.raises(SystemExit) as e:
        complexity_controller.check_complexity()

    # Assert
    assert e.value.code == 1
    mock_view.display_complexity_table.assert_called_with([results[0]])
    mock_view.display_exceeded_complexity.assert_called_with(results, 5)


def test_check_complexity_within_functions(
    mocker, complexity_controller, mock_model, mock_service, mock_view
):
    # Arrange
    mock_model.path = "/path"
    mock_model.exclude_dirs = {".venv", "tests", "node_modules"}
    mock_model.max_complexity = 10
    mock_service.get_files_to_analyze.return_value = ["/path/file1.py"]
    results = [
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
            complexity=3,
            closures=None,
        ),
    ]
    mock_service.analyze_files.return_value = results
    mock_service.get_functions_exceeding_complexity.return_value = []
    mock_service.get_functions_within_complexity.return_value = results
    mock_service.get_max_score.return_value = 5
    mocker.patch("os.path.abspath", return_value="/path")

    # Act
    with pytest.raises(SystemExit) as e:
        complexity_controller.check_complexity()

    # Assert
    assert e.value.code == 0
    mock_view.display_complexity_table.assert_called_with(results)
    mock_view.display_max_score_not_exceeded.assert_called_with(5)


def test_check_complexity_no_functions_within_max(
    mocker, complexity_controller, mock_model, mock_service, mock_view
):
    # Arrange
    mock_model.path = "/path"
    mock_model.exclude_dirs = {".venv", "tests", "node_modules"}
    mock_model.max_complexity = 5
    mock_service.get_files_to_analyze.return_value = ["/path/file1.py"]
    results = [
        Function(
            name="foo",
            lineno=1,
            col_offset=0,
            endline=1,
            is_method=False,
            classname=None,
            complexity=10,
            closures=None,
        ),
        Function(
            name="bar",
            lineno=2,
            col_offset=0,
            endline=2,
            is_method=False,
            classname=None,
            complexity=8,
            closures=None,
        ),
    ]
    mock_service.analyze_files.return_value = results
    mock_service.get_functions_exceeding_complexity.return_value = results
    mock_service.get_functions_within_complexity.return_value = []
    mock_service.get_max_score.return_value = 10
    mocker.patch("os.path.abspath", return_value="/path")

    # Act
    with pytest.raises(SystemExit) as e:
        complexity_controller.check_complexity()

    # Assert
    assert e.value.code == 1
    mock_view.display_complexity_table.assert_called_with(results)
    mock_view.display_exceeded_complexity.assert_called_with(results, 5)
