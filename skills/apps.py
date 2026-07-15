import subprocess
import psutil

# Application paths
APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "snipping tool": "snippingtool.exe",
    "wordpad": "write.exe"
}

# Process names
PROCESS_NAMES = {
    "chrome": "chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "CalculatorApp.exe",   # Windows 10/11
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe",
    "task manager": "Taskmgr.exe",
    "snipping tool": "SnippingTool.exe",
    "wordpad": "wordpad.exe"
}


def open_app(app):

    app = app.lower()

    if app not in APPS:
        return f"I don't know how to open {app}"

    subprocess.Popen(APPS[app])

    return f"Opening {app}"


def close_app(app):

    app = app.lower()

    if app not in PROCESS_NAMES:
        return f"I don't know how to close {app}"

    process_name = PROCESS_NAMES[app]

    closed = False

    for process in psutil.process_iter(["name"]):

        try:

            if process.info["name"] == process_name:
                process.kill()
                closed = True

        except Exception:
            pass

    if closed:
        return f"Closed {app}"

    return f"{app} is not running"