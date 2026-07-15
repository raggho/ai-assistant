"""
executor.py
Routes voice commands to the appropriate skill.
"""

from skills.apps import open_app, close_app
from skills.browser import (
    open_website,
    google_search,
    youtube_search,
)
from skills.folders import open_folder
from skills.system import (
    shutdown,
    restart,
    cancel_shutdown,
    lock_pc,
    logoff,
    sleep,
    take_screenshot,
)
from skills.media import media
from skills.automation import (
    open_project,
    run_pytest,
    git_status,
    git_pull,
    git_push,
    open_terminal,
    open_powershell,
)

# Websites that should open in a browser
WEBSITES = {
    "google",
    "youtube",
    "gmail",
    "chatgpt",
    "github",
    "linkedin",
    "facebook",
    "instagram",
    "spotify",
    "amazon",
    "flipkart",
    "netflix",
}

# Common folders
FOLDERS = {
    "desktop",
    "downloads",
    "documents",
    "pictures",
    "videos",
    "music",
    "c drive",
    "d drive",
    "e drive",
}


def execute(command):

    command = command.lower().strip()

    # ------------------------------------------------
    # OPEN
    # ------------------------------------------------
    if command.startswith("open"):

        target = command.replace("open", "", 1).strip()

        # Browser
        if target in WEBSITES or "." in target:
            return open_website(target)

        # Folder
        if target in FOLDERS:
            return open_folder(target)

        # Project
        if "project" in target:
            project = target.replace("project", "").strip()
            return open_project(project)

        # Application
        return open_app(target)

    # ------------------------------------------------
    # CLOSE
    # ------------------------------------------------
    elif command.startswith("close"):

        target = command.replace("close", "", 1).strip()

        return close_app(target)

    # ------------------------------------------------
    # GOOGLE SEARCH
    # ------------------------------------------------
    elif command.startswith("search google"):

        query = command.replace("search google", "", 1).strip()

        return google_search(query)

    # ------------------------------------------------
    # YOUTUBE SEARCH
    # ------------------------------------------------
    elif command.startswith("search youtube"):

        query = command.replace("search youtube", "", 1).strip()

        return youtube_search(query)

    # ------------------------------------------------
    # SCREENSHOT
    # ------------------------------------------------
    elif "screenshot" in command:
        return take_screenshot()

    # ------------------------------------------------
    # SHUTDOWN
    # ------------------------------------------------
    elif "shutdown" in command:
        return shutdown()

    elif "cancel shutdown" in command:
        return cancel_shutdown()

    # ------------------------------------------------
    # RESTART
    # ------------------------------------------------
    elif "restart" in command:
        return restart()

    # ------------------------------------------------
    # LOCK
    # ------------------------------------------------
    elif "lock" in command:
        return lock_pc()

    # ------------------------------------------------
    # LOGOUT
    # ------------------------------------------------
    elif "log off" in command or "logout" in command:
        return logoff()

    # ------------------------------------------------
    # SLEEP
    # ------------------------------------------------
    elif "sleep" in command:
        return sleep()

    # ------------------------------------------------
    # MEDIA
    # ------------------------------------------------
    elif "volume up" in command:
        return media.volume_up()

    elif "volume down" in command:
        return media.volume_down()

    elif command == "mute":
        return media.mute()

    elif "unmute" in command:
        return media.unmute()

    elif "current volume" in command:
        return media.get_volume()

    elif "play music" in command:
        return media.play_pause()

    elif "pause music" in command:
        return media.play_pause()

    elif "next song" in command:
        return media.next_song()

    elif "previous song" in command:
        return media.previous_song()

    # ------------------------------------------------
    # AUTOMATION
    # ------------------------------------------------
    elif "run smoke" in command:
        return run_pytest("smoke")

    elif "run regression" in command:
        return run_pytest("regression")

    elif "run sanity" in command:
        return run_pytest("sanity")

    elif "git status" in command:
        return git_status()

    elif "git pull" in command:
        return git_pull()

    elif "git push" in command:
        return git_push()

    elif "open terminal" in command:
        return open_terminal()

    elif "open powershell" in command:
        return open_powershell()

    # ------------------------------------------------
    # UNKNOWN
    # ------------------------------------------------
    return "Sorry Rajesh, I don't understand that command yet."