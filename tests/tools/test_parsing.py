# tests/tools/test_parsing.py
from py_cyclo.tools.parsing import parse_radon_output


def test_parse_radon_output_empty():
    output = ""
    result = parse_radon_output(output)
    assert not result


def test_parse_radon_output_single_file_single_function():
    output = "module1.py\n  F 1:0 func1 - A (5)"
    result = parse_radon_output(output)
    assert result == {
        "module1.py": [
            {
                "type": "F",
                "location": "1:0",
                "name": "func1",
                "complexity": "A",
                "score": 5,
            }
        ]
    }


def test_parse_radon_output_single_file_multiple_functions():
    output = "module1.py\n  F 1:0 func1 - A (5)\n  M 2:0 func2 - B (10)"
    result = parse_radon_output(output)
    assert result == {
        "module1.py": [
            {
                "type": "F",
                "location": "1:0",
                "name": "func1",
                "complexity": "A",
                "score": 5,
            },
            {
                "type": "M",
                "location": "2:0",
                "name": "func2",
                "complexity": "B",
                "score": 10,
            },
        ]
    }


def test_parse_radon_output_multiple_files():
    output = "module1.py\n  F 1:0 func1 - A (5)\nmodule2.py\n  M 2:0 func2 - B (10)"
    result = parse_radon_output(output)
    assert result == {
        "module1.py": [
            {
                "type": "F",
                "location": "1:0",
                "name": "func1",
                "complexity": "A",
                "score": 5,
            }
        ],
        "module2.py": [
            {
                "type": "M",
                "location": "2:0",
                "name": "func2",
                "complexity": "B",
                "score": 10,
            }
        ],
    }


def test_invalid_line_format():
    invalid_output = "Invalid line format\n"
    result = parse_radon_output(invalid_output)
    assert result == {"Invalid line format": []}


def test_parse_radon_output_invalid_line():
    output = "module1.py\n  F 1:0 func1 - A (5)\ninvalid line"
    result = parse_radon_output(output)
    assert result == {
        "module1.py": [
            {
                "type": "F",
                "location": "1:0",
                "name": "func1",
                "complexity": "A",
                "score": 5,
            }
        ],
        "invalid line": [],
    }


def test_parse_output_single_space():
    result = parse_radon_output(" ")
    assert not result


def test_parse_output_second_line_space():
    output = "\n module1.py\n  F 1:0 func1 - A (5)\n "
    result = parse_radon_output(output)
    assert result == {
        "module1.py": [
            {
                "type": "F",
                "location": "1:0",
                "name": "func1",
                "complexity": "A",
                "score": 5,
            }
        ]
    }


def test_parse_radon_output_ansi_escape_sequences():
    output = "\x1b[0mmodule1.py\n  F 1:0 func1 - A (5)\x1b[0m"
    result = parse_radon_output(output)
    assert result == {
        "module1.py": [
            {
                "type": "F",
                "location": "1:0",
                "name": "func1",
                "complexity": "A",
                "score": 5,
            }
        ]
    }
