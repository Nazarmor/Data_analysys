"""Simple wrapper around :mod:`file_sorter_cli` for backward compatibility."""
from pathlib import Path
from file_sorter_cli import sort_files

if __name__ == "__main__":
    target = Path.cwd() / "FilesForSorting"
    print(f"Sorting files in {target}")
    sort_files(target)
