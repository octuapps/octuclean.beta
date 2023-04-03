import os

def get_dir_size(path='.'):
    total = 0
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_dir_size(entry.path)
        return total
    except FileNotFoundError:
        return total

def get_file_size(path: str) -> float:
    return os.path.getsize(path) if path is not None else 0

def get_size(path: str):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)