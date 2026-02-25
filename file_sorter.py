
import shutil
from pathlib import Path

# rozmístění do určitých karegoríí


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
#


def get_unique_path(path):
    if not path.exists():
        return path

    stem = path.stem  # název bez přípony
    suffix = path.suffix  # přípona
    parent = path.parent  # cesta ke složce

    counter = 1  # číslovaní od jedničky

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        # nová cesta k souboru
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1


folder = Path(r"C:\Users\metzg\Desktop\test_sorter")
for item in folder.iterdir():
    if item.is_file():
        # zjistit kategorii
        category = get_category(item.suffix)
        # cesta bez jména
        target_dir = folder / category
        # složka
        target_dir.mkdir(exist_ok=True)
        # finální cesta
        target_path = target_dir / item.name
        # přesun
        target_path = get_unique_path(target_path)
        shutil.move(str(item), str(target_path))
