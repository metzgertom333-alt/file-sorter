
import shutil
from pathlib import Path

# Sort files into categories based on extension


def get_category(suffix):
    suffix = suffix.lower()
    if suffix in (".jpg", ".png", ".gif"):
        return "Images"
    elif suffix in (".pdf", ".docx", ".txt"):
        return "Documents"
    elif suffix in (".mp4", ".mkv"):
        return "Videos"
    else:
        return "Other"


# Return a unique file path by appending _1, _2, etc. if the file already exists
def get_unique_path(path):
    if not path.exists():
        return path

    stem = path.stem  # filename without extension
    suffix = path.suffix  # file extension
    parent = path.parent  # parent directory

    counter = 1  # start numbering from 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        # build new path
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1


folder = Path(r"C:\Users\metzg\Desktop\test_sorter")
for item in folder.iterdir():
    if item.is_file():
        # determine category
        category = get_category(item.suffix)
        # target directory path
        target_dir = folder / category
        # create folder if needed
        target_dir.mkdir(exist_ok=True)
        # final file path
        target_path = target_dir / item.name
        # move file (with duplicate handling)
        target_path = get_unique_path(target_path)
        shutil.move(str(item), str(target_path))
