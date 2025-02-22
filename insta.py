import os
import json
import zipfile
import tempfile

DEBUG = False
INPUT_FOLDER = "in"
TMP_DIR = tempfile.mkdtemp()
SEARCH_DIR = os.path.join(TMP_DIR, "connections", "followers_and_following")

def main():
    # Locate the ZIP file
    zip_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.zip')]
    if len(zip_files) != 1:
        raise ValueError("Expected exactly one ZIP file in the input folder")
    zip_path = os.path.join(INPUT_FOLDER, zip_files[0])

    # Unzip the file
    debug(f"Extracting {zip_path} to {TMP_DIR}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TMP_DIR)

    # Locate the JSON files
    followers_file = None
    following_file = None
    debug(f"Looking for JSON files inside {SEARCH_DIR}")
    for f in os.listdir(SEARCH_DIR):
        if f == "following.json":
            following_file = os.path.join(SEARCH_DIR, f)
        elif f == "followers_1.json":
            followers_file = os.path.join(SEARCH_DIR, f)

    # Ensure both files were found
    if followers_file is None or following_file is None:
        cleanup()
        raise FileNotFoundError("Required JSON files not found inside the ZIP")

    # Load and parse following
    debug(f"Loading {following_file}")
    with open(following_file, 'r') as f:
        following_data = json.load(f)["relationships_following"]
    following = {entry["string_list_data"][0]["value"] for entry in following_data}

    debug(f"Loading {followers_file}")
    with open(followers_file, 'r') as f:
        followers_data = json.load(f)
    followers = {entry["string_list_data"][0]["value"] for entry in followers_data}

    diff = following - followers
    print("\nIt is time. I will teach these trespassers the redemptive power of my Janus key.")
    print(diff)
    cleanup()

def debug(msg):
    if DEBUG:
        print(msg)

def cleanup():
    for root, dirs, files in os.walk(TMP_DIR, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(TMP_DIR)

if __name__ == "__main__":
    main()