"""
This script updates the version in `pyproject.toml`, `VERSION` file, `docs/source/conf.py`, `package.json`, and `package-lock.json`.

Usage:
    python update_version.py <version>
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Callable

import toml

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def update_file(
    file_path: Path,
    read_func: Callable[[Any], Any],
    write_func: Callable[[Any, Any], None],
) -> None:
    """
    Reads the content of a file, updates it, and writes it back.

    Args:
        file_path (Path): The path to the file to be updated.
        read_func (Callable[[Any], Any]): A function to read the file content.
        write_func (Callable[[Any, Any], None]): A function to write the updated content back to the file.

    Returns:
        None
    """
    try:
        with file_path.open("r", encoding="utf-8") as file:
            content = read_func(file)
        with file_path.open("w", encoding="utf-8") as file:
            write_func(file, content)
        logging.info(f"Successfully updated {file_path}")
    except Exception as e:
        logging.error(f"Error updating {file_path}: {e}")


def update_version_in_pyproject_toml(version: str) -> None:
    """
    Updates the version in `pyproject.toml`.

    Args:
        version (str): The new version to set.

    Returns:
        None
    """

    def read_func(file):
        return toml.load(file)

    def write_func(file, content):
        content["project"]["version"] = version
        toml.dump(content, file)

    update_file(Path("pyproject.toml"), read_func, write_func)


def update_version_in_version_txt(version: str) -> None:
    """
    Updates the version in the `VERSION` file.

    Args:
        version (str): The new version to set.

    Returns:
        None
    """

    def read_func(file):
        return file.read()

    def write_func(file, content):
        file.write(version)

    update_file(Path("VERSION"), read_func, write_func)


def update_version_in_conf_py(version: str) -> None:
    """
    Updates the version in `docs/source/conf.py`.

    Args:
        version (str): The new version to set.

    Returns:
        None
    """

    def read_func(file):
        return file.readlines()

    def write_func(file, content):
        for line in content:
            if line.startswith("release = "):
                file.write(f'release = "{version}"\n')
            else:
                file.write(line)

    update_file(Path("docs/source/conf.py"), read_func, write_func)


def update_version_in_json(file_path: Path, version: str) -> None:
    """
    Updates the version in a JSON file.

    Args:
        file_path (Path): The path to the JSON file to be updated.
        version (str): The new version to set.

    Returns:
        None
    """

    def read_func(file):
        return json.load(file)

    def write_func(file, content):
        content["version"] = version
        json.dump(content, file, indent=2)
        file.write("\n")  # Ensure a newline at the end of the file

    update_file(file_path, read_func, write_func)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update version in various files.")
    parser.add_argument("version", type=str, help="The new version to set")
    args = parser.parse_args()

    files_to_update = {
        Path("pyproject.toml"): update_version_in_pyproject_toml,
        Path("VERSION"): update_version_in_version_txt,
        Path("docs/source/conf.py"): update_version_in_conf_py,
        Path("package.json"): lambda v: update_version_in_json(Path("package.json"), v),
        Path("package-lock.json"): lambda v: update_version_in_json(
            Path("package-lock.json"), v
        ),
    }

    for file_path, update_func in files_to_update.items():
        update_func(args.version)
