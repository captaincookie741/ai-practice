import os
from pathlib import Path

# 将 base_dir 定义为项目根目录 (src 目录的父目录)
base_dir = Path(__file__).resolve().parent.parent


def read_file(name: str) -> str:
    print(f"Reading file: {name}")
    try:
        with open(base_dir / name, "r") as f:
            content: str = f.read()
        return content
    except Exception as e:
        return f"An error occurred: {e}"


def list_files() -> list[str]:
    print("(list_file)")
    file_list: list[str] = []
    for item in base_dir.rglob("*"):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list


def rename_file(name: str, new_name: str) -> str:
    print(f"(renaming_file {name} -> {new_name})")
    try:
        new_path: Path = base_dir / new_name
        if not str(new_path).startswith(str(base_dir)):
            return "Error: New file name must be within the base directory."

        os.makedirs(new_path.parent, exist_ok=True)
        os.rename(base_dir / name, new_path)
        return f"File renamed from {name} to {new_name}"
    except Exception as e:
        return f"An error occurred: {e}"