# python
import sys
from typing import Any, Dict, Optional

import click

from py_cyclo.tools.analysis import get_max_score


def display_exceeded_complexity(results, max_complexity):
    """
    Display functions that exceed the maximum cyclomatic complexity.
    """
    if not results:
        click.echo("No output from radon.")
        sys.exit(1)

    click.echo("\nFunctions with complexity greater than the maximum allowed:")
    for result in results:
        if result["complexity"] > max_complexity:
            click.echo(f"{result['name']}: {result['complexity']}")



def display_radon_results(results: Dict[Optional[str], Any]) -> None:
    for file, functions in results.items():
        print(f"\nFile: {file}")
        for function in functions:
            print(
                f"\tFunction: {function['name']}, "
                f"Complexity: {function['complexity']}, "
                f"Score: {function['score']}"
            )


def handle_results(results, max_complexity):
    """
    Handle the results of the analysis, displaying them and checking for exceeded complexity.
    """
    display_radon_results(results)
    max_score = get_max_score(results)

    if max_score > max_complexity:
        click.echo(
            f"\nFAILED - Maximum complexity {max_complexity} "
            f"exceeded by {max_score}\n"
        )
        click.echo("\nFunctions with complexity greater than the maximum allowed:")
        display_exceeded_complexity(results, max_complexity)
        sys.exit(1)

    click.echo(f"\nMaximum complexity not exceeded: {max_score}\n")
    sys.exit(0)
