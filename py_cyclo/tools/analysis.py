# python
from typing import Any, Dict, Optional


def get_max_score(results: Dict[Optional[str], Any]) -> int:
    max_score = 0
    for _, functions in results.items():
        for function in functions:
            if function["score"] > max_score:
                max_score = function["score"]
    return max_score
