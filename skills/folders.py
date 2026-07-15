"""
folders.py
Open common Windows folders.
"""

import os
import subprocess

# User home directory
HOME = os.path.expanduser("~")

FOLDERS = {
    "desktop": os.path.join(HOME, "Desktop"),
    "downloads": os.path.join(HOME, "Downloads"),
    "documents": os.path.join(HOME, "Documents"),
    "pictures": os.path.join(HOME, "Pictures"),
    "videos": os.path.join(HOME, "Videos"),
    "music": os.path.join(HOME, "Music"),

    "c drive": "C:\\",
    "d drive": "D:\\",
    "e drive": "E:\\",
}


def open_folder(folder_name: str):

    folder_name = folder_name.lower().strip()

    if folder_name in FOLDERS:

        path = FOLDERS[folder_name]

        if os.path.exists(path):
            os.startfile(path)
            return f"Opening {folder_name}"

        return f"{folder_name} does not exist."

    return f"I don't know the folder {folder_name}"


def open_custom_folder(path):

    if os.path.exists(path):

        subprocess.Popen(f'explorer "{path}"')

        return f"Opening {path}"

    return "Folder not found."