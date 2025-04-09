# python
import configparser
import os
from typing import Set

import click

from py_cyclo.controllers.complexity_controller import ComplexityController
from py_cyclo.models.complexity_model import ComplexityModel
from py_cyclo.services.complexity_service import ComplexityService
from py_cyclo.views.complexity_view import ComplexityView

CONFIG_FILE = ".cyclo"


def load_config():
    """
    Load the configuration file.
    """
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)

    return config


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option(
    "--max-complexity",
    "-m",
    default=12,
    help="The maximum allowed cyclomatic complexity.",
)
@click.option(
    "--exclude-dirs",
    "-e",
    default=None,
    help="Comma-separated list of directories to exclude.",
)
def check_complexity(path: str, max_complexity: int, exclude_dirs: str) -> None:
    """
    Check the cyclomatic complexity of the code.
    Fail if it exceeds the max_complexity.
    """
    config = load_config()
    max_complexity = max_complexity or int(
        config.get("cyclo", "max_complexity", fallback=12)
    )
    exclude_dirs = (
        set(exclude_dirs.split(","))
        if exclude_dirs
        else set(
            config.get(
                "cyclo", "exclude_dirs", fallback=".venv,node_modules,venv"
            ).split(",")
        )
    )
    main(path, max_complexity, exclude_dirs)


def main(path: str, max_complexity: int, exclude_dirs: Set[str]) -> None:
    """
    Main function to run the cyclomatic complexity check.
    """
    view = ComplexityView()
    service = ComplexityService()
    model = ComplexityModel(path, max_complexity, exclude_dirs)
    controller = ComplexityController(service, model, view)

    controller.check_complexity()


if __name__ == "__main__":
    main(".", 12, set())
