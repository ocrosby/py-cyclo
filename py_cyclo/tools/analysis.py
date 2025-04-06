# python
import sys

import click


def get_max_score(results):
    """
    Get the maximum cyclomatic complexity score from the results.
    """
    if not results:
        click.echo("No output from radon.")
        sys.exit(1)

    max_score = max(result.complexity for result in results)

    return max_score
