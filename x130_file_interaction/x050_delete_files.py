from x010_path import path_to_another_file
from x040_json import path_to_json_with_users

if __name__ == "__main__":
    path_to_json_with_users.unlink(missing_ok=True)
    path_to_another_file.unlink()
