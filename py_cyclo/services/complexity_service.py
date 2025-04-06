# py_cyclo/services/complexity_service.py
import os
from typing import List, Set, Any
from radon.complexity import cc_visit

class ComplexityService:
    def __init__(self):
        pass

    def get_files_to_analyze(self, path: str, exclude_dirs: Set[str]) -> List[str]:
        files_to_analyze = []
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if file.endswith(".py"):
                    files_to_analyze.append(os.path.join(root, file))

        return files_to_analyze

    def analyze_files(self, files_to_analyze: List[str]) -> List[Any]:
        results: List[Any] = []

        for file in files_to_analyze:
            with open(file, "r", encoding="utf-8") as f:
                code = f.read()
                file_results = cc_visit(code)
                for result in file_results:
                    result.filename = file
                results.extend(file_results)

        return results
