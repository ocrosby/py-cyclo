# python
import re
from typing import Any, Dict, Optional


def parse_radon_output(output: str) -> Dict[Optional[str], Any]:
    output = output.replace("\x1b[0m", "")
    pattern = re.compile(r"^\s*(\w)\s(\d+:\d+)\s([\w_]+)\s-\s([A-F])\s\((\d+)\)$")
    results: Dict[Optional[str], Any] = {}
    output = output.strip()
    lines = output.splitlines()
    current_file = None
    for line in lines:
        if not line.startswith(" "):
            current_file = line.strip()
            results[current_file] = []
        else:
            match = pattern.match(line)
            if match:
                function_info = {
                    "type": match.group(1),
                    "location": match.group(2),
                    "name": match.group(3),
                    "complexity": match.group(4),
                    "score": int(match.group(5)),
                }
                results[current_file].append(function_info)
    return results
