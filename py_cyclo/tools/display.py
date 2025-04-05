# python
from typing import Any, Dict, Optional


def display_exceeded_complexity(
    results: Dict[Optional[str], Any], max_complexity: int
) -> None:
    print("File\tFunction\tComplexity\tScore")
    for file, functions in results.items():
        for function in functions:
            if function["score"] > max_complexity:
                print(
                    f"{file}\t{function['name']}\t{function['complexity']}\t"
                    f"{function['score']}"
                )


def display_radon_results(results: Dict[Optional[str], Any]) -> None:
    for file, functions in results.items():
        print(f"\nFile: {file}")
        for function in functions:
            print(
                f"\tFunction: {function['name']}, "
                f"Complexity: {function['complexity']}, "
                f"Score: {function['score']}"
            )
