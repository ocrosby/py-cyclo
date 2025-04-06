# py_cyclo/controllers/complexity_controller.py
import os
import sys
import click
from py_cyclo.models.complexity_model import ComplexityModel
from py_cyclo.services.complexity_service import ComplexityService
from py_cyclo.views.complexity_view import ComplexityView
from py_cyclo.tools.analysis import get_max_score

class ComplexityController:
    def __init__(self, service: ComplexityService, model: ComplexityModel, view: ComplexityView) -> None:
        self.service = service
        self.model = model
        self.view = view

    def check_complexity(self) -> None:
        # Convert the path to an absolute path
        self.model.path = os.path.abspath(self.model.path)

        click.echo(f"Checking cyclomatic complexity in \"{self.model.path}\"...")

        files_to_analyze = self.service.get_files_to_analyze(
            self.model.path,
            self.model.exclude_dirs
        )
        if not files_to_analyze:
            click.echo("No Python files found to analyze.")
            sys.exit(0)

        results = self.service.analyze_files(files_to_analyze)
        if not results:
            click.echo("No output from radon.")
            sys.exit(1)

        self.view.display_radon_results(results)
        max_score = get_max_score(results)

        if max_score > self.model.max_complexity:
            click.echo(
                f"\nFAILED - Maximum complexity {self.model.max_complexity} "
                f"exceeded by {max_score}\n"
            )
            self.view.display_exceeded_complexity(results, self.model.max_complexity)
            sys.exit(1)

        self.view.display_max_score_not_exceeded(max_score)
        sys.exit(0)