# py_cyclo/views/complexity_view.py
import sys
import click

class ComplexityView:
    def display_radon_results(self, results) -> None:
        if not results:
            click.echo("No output from radon.")
            sys.exit(1)

        click.echo("\nCyclomatic Complexity Results:")
        click.echo("-------------------------------")
        for result in results:
            click.echo(f"{result.name}: {result.complexity}")

    def display_exceeded_complexity(self, results, max_complexity) -> None:
        if not results:
            click.echo("No output from radon.")
            sys.exit(1)

        click.echo("\nFunctions with complexity greater than the maximum allowed:")
        for result in results:
            if result.complexity > max_complexity:
                click.echo(f"{result.name}: {result.complexity}")

    def display_max_score_not_exceeded(self, max_score) -> None:
        click.echo(f"\nMaximum complexity not exceeded: {max_score}\n")