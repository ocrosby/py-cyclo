import shutil

from invoke import task


@task(aliases=["c"])
def clean(c):
    """Clean up transient files."""
    patterns = [
        "__pycache__",
        ".pytest_cache",
        "build",
        "dist",
        "*.egg-info",
        ".mypy_cache",
        ".coverage",
        "coverage.xml",
        "*.log",
        "junit.xml",
    ]

    for pattern in patterns:
        c.run(f"rm -rf {pattern}")
        shutil.rmtree(pattern, ignore_errors=True)

    # Recursively remove .coverage directories in the tests package using find
    c.run("find ./tests -type f -name '.coverage' -exec rm -f {} +")
    c.run("find ./tests -type f -name 'junit.xml' -exec rm -f {} +")
    c.run("find ./tests -type f -name 'coverage.xml' -exec rm -f {} +")
    c.run("find ./tests -type d -name '__pycache__' -exec rm -rf {} +")
    c.run("find ./tests -type d -name '.pytest_cache' -exec rm -rf {} +")
    c.run("find ./tests -type d -name 'htmlcov' -exec rm -rf {} +")
    c.run("find ./tests -type d -name '.mypy_cache' -exec rm -rf {} +")


@task(aliases=["i"])
def install(c):
    """Install dependencies."""
    c.run("pip install .[dev]")


@task(aliases=["f"])
def format_code(c):
    """Format code using black."""
    c.run("isort py_cyclo/ tests/ tasks.py")
    c.run("black py_cyclo/ tests/ tasks.py")


@task(aliases=["l"], pre=[format_code])
def lint(c):
    """Lint code using flake8, pylint, and isort."""
    c.run("flake8 py_cyclo/ tests/ tasks.py")
    c.run("pylint py_cyclo/ tests/ tasks.py")
    c.run("isort --check-only py_cyclo/ tests/ tasks.py")


@task(aliases=["t"])
def test(c):
    """Run tests using pytest."""
    c.run("pytest")


@task(aliases=["b"])
def build(c):
    """Build the project."""
    c.run("python -m build")


@task(aliases=["m"])
def mypy(c):
    """Type check using mypy."""
    c.run("mypy .")


@task(aliases=["s"])
def sort_imports(c):
    """Sort imports using isort."""
    c.run("isort .")


@task(aliases=["p"])
def pylint(c):
    """Lint code using pylint."""
    c.run("pylint .")
