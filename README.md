# PyCyclo

**py-cyclo** is a general-purpose command-line tool for analyzing and validating cyclomatic complexity in Python code. Designed for developers who want to maintain clean, testable, and maintainable code, `py-cyclo` provides detailed reports and enforcement mechanisms to ensure your codebase doesn't spiral out of control.

![License](https://img.shields.io/github/license/ocrosby/py-cyclo)
[![Continuous Integration](https://github.com/ocrosby/py-cyclo/actions/workflows/ci.yaml/badge.svg)](https://github.com/ocrosby/py-cyclo/actions/workflows/ci.yaml)
[![Release](https://github.com/ocrosby/py-cyclo/actions/workflows/release.yaml/badge.svg)](https://github.com/ocrosby/py-cyclo/actions/workflows/release.yaml)
![PyPI](https://img.shields.io/pypi/v/py-cyclo)

---

## 🚀 Features

- Measure cyclomatic complexity of Python functions and methods  
- Set complexity thresholds and enforce them via CLI  
- Supports per-file, per-function, or project-wide analysis  
- JSON, plain-text, or colorized output formats  
- Integrates easily into CI/CD pipelines  

---

## 📦 Installation

You can install `py-cyclo` via pip:

```bash
pip install py-cyclo
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/ocrosby/py-cyclo.git
```

---

## 🛠️ Usage

```text
Usage: cyclo [OPTIONS] PATH
```

### Example Command

```bash
# Validate the cyclomatic complexity of all Python files in the current directory
# and its subdirectories is less than or equal to 10
cyclo --max-complexity 10 --exclude-dirs .venv,tests .
```

or 

### Example Command

```bash
# Validate the cyclomatic complexity of all Python files in the current directory
# and its subdirectories is less than or equal to 10
cyclo -m 10 -e .venv,tests .
```

### Example Output

```text
Checking cyclomatic complexity in "/path/to/project"...

2 functions exceed the maximum complexity of 4:
+-------------------------------+--------------+-----------+-----------------------------------------------+
| Name                          |   Complexity |   Line No | Filename                                      |
+===============================+==============+===========+===============================================+
| example_function              |            6 |        10 | example_module.py                             |
+-------------------------------+--------------+-----------+-----------------------------------------------+
| another_function              |            5 |        20 | another_module.py                             |
+-------------------------------+--------------+-----------+-----------------------------------------------+

5 functions with a complexity < 4:
+-------------------------------+--------------+-----------+-----------------------------------------------+
| Name                          |   Complexity |   Line No | Filename                                      |
+===============================+==============+===========+===============================================+
| simple_function               |            3 |        15 | simple_module.py                              |
+-------------------------------+--------------+-----------+-----------------------------------------------+
| helper_function               |            2 |        25 | helper_module.py                              |
+-------------------------------+--------------+-----------+-----------------------------------------------+
| utility_function              |            2 |        30 | utility_module.py                             |
+-------------------------------+--------------+-----------+-----------------------------------------------+
| another_helper_function       |            1 |        35 | another_helper_module.py                      |
+-------------------------------+--------------+-----------+-----------------------------------------------+
| yet_another_function          |            1 |        40 | yet_another_module.py                         |
+-------------------------------+--------------+-----------+-----------------------------------------------+

Maximum complexity: 6

FAILED - Maximum complexity 4 exceeded by 2

Functions with complexity greater than the maximum allowed:
example_function: 6
another_function: 5
```

### Options

| Flag                   | Description                                        |
|------------------------|----------------------------------------------------|
| `--max-complexity, -m` | Set the maximum allowed complexity per function    |
| `--exclude-dirs, -e`   | Comma-separated list of directories to exclude    |
| `--help`               | Show CLI help                                      |

---

## 🔧 Configuration

You can use a .cyclo configuration file to set default options for `cyclo`. This file should be
placed in the root directory of your project. Here is an example configuration:

```plaintext
[cyclo]
max_complexity = 10
exclude_dirs = .venv,tests,node_modules
```

You can then run `cyclo` without any options, and it will use the settings from the configuration file:

### Example Command Using Configuration

```bash
# Run py-cyclo using the defaults from the .cyclo file
cyclo .
```

If both the .cyclo file and command-line arguments are provided, the command-line arguments take precedence.

This update ensures that users are aware of the new `exclude_dirs` argument and the `.cyclo` configuration file, and it provides clear examples of how to use them.

---

## 🧪 Testing

To run the test suite:

```bash
pip install --upgrade pip
pip install invoke
pip install ".[dev]"
invoke test
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork this repo  
2. Create a new branch (`git checkout -b feature/my-feature`)  
3. Make your changes  
4. Write tests and ensure everything passes  
5. Submit a pull request  

Please follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- Inspired by tools like [`radon`](https://github.com/rubik/radon)  
- Built with ❤️ using [Click](https://click.palletsprojects.com/) and [ast](https://docs.python.org/3/library/ast.html)  

---

## 🔗 Related Projects

- [Radon](https://github.com/rubik/radon)  
- [Lizard](https://github.com/terryyin/lizard)  
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)  

---

## References

- [Cyclomatic Complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- [Cyclomatic Complexity](https://www.ibm.com/docs/en/raa/6.1.0?topic=metrics-cyclomatic-complexity#:~:text=Cyclomatic%20complexity%20is%20a%20measurement,and%20less%20risky%20to%20modify.)
- [Cyclomatic Complexity Explained with Practical Examples](https://www.youtube.com/watch?v=vmyS_j3Kh8g)

## 📬 Contact

Feel free to reach out via GitHub Issues or submit feature requests and bugs.