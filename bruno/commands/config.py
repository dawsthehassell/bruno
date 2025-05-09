import os

DEFAULT_DATA_PATH = os.path.join(os.path.expanduser("~"), ".bruno", "entry_logs.json")

def ensure_data_dir_exists(data_path=DEFAULT_DATA_PATH):
    dir_path = os.path.dirname(data_path)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory ensured at: {dir_path}")