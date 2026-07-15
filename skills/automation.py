"""
automation.py
Developer automation skills for Babo.
"""

import subprocess
import os

# --------------------------------------------------
# Configure these paths for your machine
# --------------------------------------------------

PROJECTS = {
    "automation": r"D:\Automation",
    "framework": r"D:\Automation\Framework",
}

PYTEST_COMMANDS = {
    "smoke": "pytest tests/smoke -v",
    "regression": "pytest tests/regression -v",
    "sanity": "pytest tests/sanity -v",
}

# --------------------------------------------------
# PROJECT
# --------------------------------------------------

def open_project(name):

    name = name.lower()

    if name in PROJECTS:

        os.startfile(PROJECTS[name])

        return f"Opening {name} project."

    return "Project not found."


# --------------------------------------------------
# PYTEST
# --------------------------------------------------

def run_pytest(test_type):

    test_type = test_type.lower()

    if test_type not in PYTEST_COMMANDS:
        return "Unknown test suite."

    subprocess.Popen(
        PYTEST_COMMANDS[test_type],
        shell=True
    )

    return f"Running {test_type} tests."


# --------------------------------------------------
# GIT
# --------------------------------------------------

def git_status():

    subprocess.Popen(
        "git status",
        shell=True
    )

    return "Opening Git Status."


def git_pull():

    subprocess.Popen(
        "git pull",
        shell=True
    )

    return "Pulling latest code."


def git_push():

    subprocess.Popen(
        "git push",
        shell=True
    )

    return "Pushing code."


# --------------------------------------------------
# CMD
# --------------------------------------------------

def open_terminal():

    subprocess.Popen("cmd")

    return "Opening Command Prompt."


def open_powershell():

    subprocess.Popen("powershell")

    return "Opening PowerShell."