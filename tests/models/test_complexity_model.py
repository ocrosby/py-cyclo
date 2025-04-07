# tests/models/test_complexity_model.py
from py_cyclo.models.complexity_model import ComplexityModel


def test_complexity_model_initialization():
    model = ComplexityModel(
        path="test_path", max_complexity=10, exclude_dirs={"dir1", "dir2"}
    )
    assert model.path == "test_path"
    assert model.max_complexity == 10
    assert model.exclude_dirs == {"dir1", "dir2"}


def test_complexity_model_default_initialization():
    model = ComplexityModel()
    assert model.path is None
    assert model.max_complexity == 0
    assert model.exclude_dirs is None


def test_complexity_model_str():
    model = ComplexityModel(
        path="test_path", max_complexity=10, exclude_dirs={"dir1", "dir2"}
    )
    expected_str = (
        "ComplexityModel(path=test_path, max_complexity=10, "
        "exclude_dirs=['dir1', 'dir2'])"
    )
    assert str(model) == expected_str


def test_complexity_model_repr():
    model = ComplexityModel(
        path="test_path", max_complexity=10, exclude_dirs={"dir1", "dir2"}
    )
    expected_repr = (
        "ComplexityModel(path=test_path, max_complexity=10, "
        "exclude_dirs=['dir1', 'dir2'])"
    )
    assert repr(model) == expected_repr
