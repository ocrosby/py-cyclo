# python
import os
import subprocess
import sys
from typing import Set

import click
from radon.complexity import cc_visit

from py_cyclo.controllers.complexity_controller import ComplexityController
from py_cyclo.models.complexity_model import ComplexityModel
from py_cyclo.services.complexity_service import ComplexityService
from py_cyclo.tools.display import handle_results
from py_cyclo.views.complexity_view import ComplexityView


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option(
    "--max-complexity", "-m", default=12, help="The maximum allowed cyclomatic complexity."
)
def check_complexity(path: str, max_complexity: int) -> None:
    """
    Check the cyclomatic complexity of the code.
    Fail if it exceeds the max_complexity.
    """
    main(path, max_complexity)


def main(path: str, max_complexity: int) -> None:
    """
    Main function to run the cyclomatic complexity check.
    """
    view = ComplexityView()
    service = ComplexityService()
    model = ComplexityModel(path, max_complexity, {"node_modules", ".venv", "venv"})
    controller = ComplexityController(service, model, view)

    controller.check_complexity()

if __name__ == "__main__":
    main(".", 12)
