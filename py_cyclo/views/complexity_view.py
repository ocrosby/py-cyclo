# py_cyclo/views/complexity_view.py
import os
import sys

import click
from tabulate import tabulate


class ComplexityView:
    def display_complexity_table(self, results) -> None:
        if not results:
            click.echo("No output from radon.")
            sys.exit(1)

        # Sort results by decreasing complexity
        sorted_results = sorted(results, key=lambda x: x.complexity, reverse=True)

        # Prepare data for tabulate
        table_data = [
            [
                result.name,
                result.complexity,
                result.lineno,
                os.path.relpath(result.filename),
            ]
            for result in sorted_results
        ]

        # Define table headers
        headers = ["Name", "Complexity", "Line No", "Filename"]

        # Print the table
        click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))

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
