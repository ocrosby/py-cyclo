# py_cyclo/models/complexity_model.py
from typing import Optional, Set


class ComplexityModel:
    def __init__(
        self,
        path: Optional[str] = None,
        max_complexity: Optional[int] = 0,
        exclude_dirs: Optional[Set[str]] = None,
    ):
        self.path = path
        self.max_complexity = max_complexity
        self.exclude_dirs = exclude_dirs

    def __str__(self):
        return (
            f"ComplexityModel(path={self.path}, max_complexity={self.max_complexity}, "
            f"exclude_dirs={sorted(list(self.exclude_dirs))})"
        )

    def __repr__(self):
        return self.__str__()
