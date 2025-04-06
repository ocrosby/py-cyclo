# py_cyclo/models/complexity_model.py
import os
from typing import Set, Optional

from radon.complexity import cc_visit

class ComplexityModel:
    def __init__(self,
                 path: Optional[str] = None,
                 max_complexity: Optional[int] = 0,
                 exclude_dirs: Optional[Set[str]] = None
                 ):
        self.path = path
        self.max_complexity = max_complexity
        self.exclude_dirs = exclude_dirs

    def __str__(self):
        return f"ComplexityModel(path={self.path}, max_complexity={self.max_complexity}, exclude_dirs={self.exclude_dirs})"

    def __repr__(self):
        return f"ComplexityModel(path={self.path}, max_complexity={self.max_complexity}, exclude_dirs={self.exclude_dirs})"


class ComplexityAnalyzer:
    def __init__(self, path, exclude_dirs):
        self.path = path
        self.exclude_dirs = exclude_dirs

    def get_files_to_analyze(self):
        files_to_analyze = []
        for root, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            for file in files:
                if file.endswith(".py"):
                    files_to_analyze.append(os.path.join(root, file))
        return files_to_analyze

    def analyze_files(self, files_to_analyze):
        results = []
        for file in files_to_analyze:
            with open(file, "r", encoding="utf-8") as f:
                code = f.read()
                file_results = cc_visit(code)
                for result in file_results:
                    result.filename = file
                results.extend(file_results)
        return results
