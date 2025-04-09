# py_cyclo/controllers/complexity_controller.py
# pylint: disable=too-few-public-methods
import os
import sys
from typing import List

import click
from radon.visitors import Function

from py_cyclo.models.complexity_model import ComplexityModel
from py_cyclo.services.complexity_service import ComplexityService
from py_cyclo.views.complexity_view import ComplexityView


class ComplexityController:
    def __init__(
        self, service: ComplexityService, model: ComplexityModel, view: ComplexityView
    ) -> None:
        self.service = service
        self.model = model
        self.view = view

    def check_complexity(self) -> None:
        # Convert the path to an absolute path
        self.model.path = os.path.abspath(self.model.path)

        exclude_dirs = self.model.exclude_dirs or []  # Default to an empty list if None

        click.echo(f'Checking cyclomatic complexity in "{self.model.path}"...')
        click.echo(f"Maximum complexity: {self.model.max_complexity}")
        click.echo(f'Excluding directories: {", ".join(exclude_dirs)}')

        files_to_analyze = self.service.get_files_to_analyze(
            self.model.path, exclude_dirs
        )
        if not files_to_analyze:
            click.echo("No Python files found to analyze.")
            sys.exit(0)

        results: List[Function] = self.service.analyze_files(files_to_analyze)
        if not results:
            click.echo("No output from radon.")
            sys.exit(1)

        exceeding = self.service.get_functions_exceeding_complexity(
            results, self.model.max_complexity
        )

        count = len(exceeding)
        if count > 0:
            click.echo(
                f"\n{count} functions exceed the maximum complexity "
                f"of {self.model.max_complexity}:"
            )
            self.view.display_complexity_table(exceeding)
        else:
            click.echo(
                f"There are no functions exceeding the maximum complexity "
                f"of {self.model.max_complexity}."
            )

        click.echo()

        within = self.service.get_functions_within_complexity(
            results, self.model.max_complexity
        )

        count = len(within)
        if count > 0:
            click.echo(
                f"\n{count} functions with a complexity < {self.model.max_complexity}:"
            )
            self.view.display_complexity_table(within)
        else:
            click.echo("There are no functions within the maximum complexity.")

        click.echo()

        max_score = self.service.get_max_score(results)
        click.echo(f"\nMaximum complexity: {max_score}\n")

        if max_score > self.model.max_complexity:
            click.echo(
                f"\nFAILED - Maximum complexity {self.model.max_complexity} "
                f"exceeded by {max_score}\n"
            )
            self.view.display_exceeded_complexity(results, self.model.max_complexity)
            sys.exit(1)

        self.view.display_max_score_not_exceeded(max_score)
        sys.exit(0)
