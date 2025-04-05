# PyCyclo

**py-cyclo** is a general-purpose command-line tool for analyzing and validating cyclomatic complexity in Python code. Designed for developers who want to maintain clean, testable, and maintainable code, `py-cyclo` provides detailed reports and enforcement mechanisms to ensure your codebase doesn't spiral out of control.

![License](https://img.shields.io/github/license/ocrosby/py-cyclo)
![Tests](https://img.shields.io/github/actions/workflow/status/ocrosby/py-cyclo/tests.yml)
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

```bash
# Execute this from within your project directory
cyclo --max-complexity 10
```

### Example Output

```text
example.py:12 - function `process_data` has cyclomatic complexity of 13 (limit: 10)
```

### Options

| Flag               | Description                                        |
|--------------------|----------------------------------------------------|
| `--max-complexity` | Set the maximum allowed complexity per function    |
| `--help`           | Show CLI help                                      |

---

## 🔧 Configuration

At present there are no configuration options.

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

## 📬 Contact

Feel free to reach out via GitHub Issues or submit feature requests and bugs.