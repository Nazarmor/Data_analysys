import argparse
import os
import shutil
from pathlib import Path

FOLDER_EXTENSIONS = {
    'csv files': ['.csv'],
    'image files': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'txt files': ['.txt'],
    'xlsx files': ['.xlsx'],
    'pdf files': ['.pdf']
}


def sort_files(base_path: Path) -> None:
    """Sort files in *base_path* into folders based on their extension."""
    if not base_path.is_dir():
        raise ValueError(f"{base_path} is not a directory")

    # Create target folders
    for folder in FOLDER_EXTENSIONS:
        (base_path / folder).mkdir(exist_ok=True)
    (base_path / 'others').mkdir(exist_ok=True)

    for item in base_path.iterdir():
        if item.is_file():
            target = base_path / 'others'
            for folder, extensions in FOLDER_EXTENSIONS.items():
                if item.suffix.lower() in extensions:
                    target = base_path / folder
                    break
            shutil.move(str(item), target / item.name)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sort files in a directory by extension")
    parser.add_argument('path', nargs='?', default='.', help="Directory containing files to sort")
    args = parser.parse_args(argv)
    sort_files(Path(args.path))


if __name__ == '__main__':
    main()
