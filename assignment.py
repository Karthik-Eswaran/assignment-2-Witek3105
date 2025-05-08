import os
import importlib
from typing import Iterator, Any, List

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_files_in_directory(directory_path: str) -> List[str]:
    try:
        entries = os.listdir(directory_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    return [
        f for f in entries
        if os.path.isfile(os.path.join(directory_path, f))
    ]

def generate_numbers(n: int) -> Iterator[int]:
    for i in range(n):
        yield i

def use_function_from_module(module_name: str, function_name: str, *args) -> Any:
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"Module not found: {module_name}")

    if not hasattr(module, function_name):
        raise AttributeError(
            f"Function '{function_name}' not found in module '{module_name}'"
        )

    func = getattr(module, function_name)
    if not callable(func):
        raise TypeError(
            f"'{function_name}' in module '{module_name}' is not callable"
        )

    return func(*args)