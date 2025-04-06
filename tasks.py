import shutil

from invoke import Context, task


@task(aliases=["c"])
def clean(c: Context) -> None:
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


@task(
    pre=[clean],
    aliases=["i"],
    help={"prod": "Install production dependencies."},
)
def install(c: Context, prod: bool = False) -> None:
    """Install dependencies."""
    c.run('pip install --upgrade "pip>=21.3"')
    c.run("pip install flit")
    c.run("pip install build")

    if prod:
        print("Installing production dependencies ...")
        c.run("flit install --deps production")
    else:
        print("Installing development dependencies...")
        c.run("flit install --symlink")  # install package in editable mode


@task(aliases=["f"])
def format_code(c: Context) -> None:
    """Format code using black."""
    c.run("isort py_cyclo/ tests/ tasks.py update_version.py")
    c.run("black py_cyclo/ tests/ tasks.py update_version.py")


@task(aliases=["l"], pre=[format_code])
def lint(c: Context) -> None:
    """Lint code using flake8, pylint, and isort."""
    c.run("flake8 py_cyclo/ tests/ tasks.py update_version.py")
    c.run("pylint py_cyclo/ tests/ tasks.py update_version.py")
    c.run("isort --check-only py_cyclo/ tests/ tasks.py update_version.py")


@task(aliases=["t"])
def test(c: Context) -> None:
    """Run tests using pytest."""
    c.run("pytest")


@task(aliases=["b"])
def build(c: Context) -> None:
    """Build the project."""
    c.run("python -m build")


@task(aliases=["m"])
def mypy(c: Context) -> None:
    """Type check using mypy."""
    c.run("mypy .")


@task(aliases=["s"])
def sort_imports(c: Context) -> None:
    """Sort imports using isort."""
    c.run("isort .")


@task(aliases=["p"])
def pylint(c: Context) -> None:
    """Lint code using pylint."""
    c.run("pylint .")
