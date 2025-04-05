# python
import subprocess
import sys

import click

from py_cyclo.tools.analysis import get_max_score
from py_cyclo.tools.display import (
    display_exceeded_complexity,
    display_radon_results,
)
from py_cyclo.tools.parsing import parse_radon_output


@click.command()
@click.option(
    "--max-complexity", default=12, help="The maximum allowed cyclomatic complexity."
)
def check_complexity(max_complexity: int) -> None:
    """
    Check the cyclomatic complexity of the code.
    Fail if it exceeds the max_complexity.
    """
    try:
        click.echo("Checking cyclomatic complexity ...")
        result = subprocess.run(
            ["radon", "cc", "py_cyclo", "-s"],
            capture_output=True,
            text=True,
            check=True,
        )

        if result is None:
            click.echo("No output from radon.")
            sys.exit(1)

        output = result.stdout
        results = parse_radon_output(output)
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
    except subprocess.CalledProcessError as err:
        click.echo(f"Error occurred while checking complexity: {err}")
        sys.exit(1)
