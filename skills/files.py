"""
files.py
File management module for the AI Assistant.
"""

from pathlib import Path
import shutil
import os


class FileManager:

    def __init__(self):
        # Default workspace (can be changed later from settings.json)
        self.workspace = Path.home() / "Desktop"

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    def _resolve_path(self, path: str) -> Path:

        if not path:
            raise ValueError("Path cannot be empty.")

        p = Path(os.path.expandvars(os.path.expanduser(path)))

        # If only filename is provided, save in workspace
        if not p.is_absolute():
            p = self.workspace / p

        return p.resolve()

    # --------------------------------------------------
    # Create File
    # --------------------------------------------------

    def create_file(self, filename: str, content: str = ""):

        try:

            path = self._resolve_path(filename)

            if path.exists():
                return f"{path.name} already exists."

            path.parent.mkdir(parents=True, exist_ok=True)

            path.write_text(content, encoding="utf-8")

            return f"Created file '{path.name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Create Folder
    # --------------------------------------------------

    def create_folder(self, foldername: str):

        try:

            path = self._resolve_path(foldername)

            if path.exists():
                return f"{path.name} already exists."

            path.mkdir(parents=True)

            return f"Created folder '{path.name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(self, target: str):

        try:

            path = self._resolve_path(target)

            if not path.exists():
                return "File or folder not found."

            if path.is_dir():

                shutil.rmtree(path)

            else:

                path.unlink()

            return f"Deleted '{path.name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Rename
    # --------------------------------------------------

    def rename(self, source: str, new_name: str):

        try:

            source_path = self._resolve_path(source)

            if not source_path.exists():
                return "File or folder not found."

            destination = source_path.with_name(new_name)

            source_path.rename(destination)

            return f"Renamed to '{new_name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Copy
    # --------------------------------------------------

    def copy(self, source: str, destination: str):

        try:

            src = self._resolve_path(source)

            dst = self._resolve_path(destination)

            if not src.exists():
                return "Source not found."

            dst.parent.mkdir(parents=True, exist_ok=True)

            if src.is_dir():

                shutil.copytree(src, dst)

            else:

                shutil.copy2(src, dst)

            return "Copy completed."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Move
    # --------------------------------------------------

    def move(self, source: str, destination: str):

        try:

            src = self._resolve_path(source)

            dst = self._resolve_path(destination)

            if not src.exists():
                return "Source not found."

            dst.parent.mkdir(parents=True, exist_ok=True)

            shutil.move(str(src), str(dst))

            return "Move completed."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Open
    # --------------------------------------------------

    def open(self, target: str):

        try:

            path = self._resolve_path(target)

            if not path.exists():
                return "File not found."

            os.startfile(path)

            return f"Opening '{path.name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(self, filename: str):

        try:

            for root, _, files in os.walk(self.workspace):

                if filename in files:

                    return str(Path(root) / filename)

            return "File not found."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # List Folder
    # --------------------------------------------------

    def list_folder(self, folder="."):

        try:

            path = self._resolve_path(folder)

            if not path.exists():
                return "Folder not found."

            items = []

            for item in sorted(path.iterdir()):

                if item.is_dir():
                    items.append(f"[DIR] {item.name}")
                else:
                    items.append(item.name)

            if not items:
                return "Folder is empty."

            return "\n".join(items)

        except Exception as e:

            return f"Error: {e}"
    
    # --------------------------------------------------
    # Read File
    # --------------------------------------------------

    def read_file(self, filename: str):

        try:

            path = self._resolve_path(filename)

            if not path.exists():
                return "File not found."

            if path.is_dir():
                return "Cannot read a folder."

            text = path.read_text(encoding="utf-8")

            if not text.strip():
                return "The file is empty."

            return text

        except Exception as e:

            return f"Error: {e}"
  
    # --------------------------------------------------
    # Write File
    # --------------------------------------------------

    def write_file(self, filename: str, text: str):

        try:

            path = self._resolve_path(filename)

            path.parent.mkdir(parents=True, exist_ok=True)

            path.write_text(text, encoding="utf-8")

            return f"Wrote to '{path.name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # Append File
    # --------------------------------------------------

    def append_file(self, filename: str, text: str):

        try:

            path = self._resolve_path(filename)

            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, "a", encoding="utf-8") as file:

                file.write(text + "\n")

            return f"Appended to '{path.name}'."

        except Exception as e:

            return f"Error: {e}"

    # --------------------------------------------------
    # List Folder
    # --------------------------------------------------

    def list_folder(self, folder="."):

        try:

            path = self._resolve_path(folder)

            if not path.exists():
                return "Folder not found."

            items = []

            for item in sorted(path.iterdir()):

                if item.is_dir():

                    items.append(f"[DIR] {item.name}")

                else:

                    items.append(item.name)

            if not items:

                return "Folder is empty."

            return "\n".join(items)

        except Exception as e:

            return f"Error: {e}"

# Singleton instance
file_manager = FileManager()