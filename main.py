"""
Babo AI Assistant
Conversation Mode
"""

import time

from core.listener import record_audio
from core.speech import speech_to_text
from core.speaker import speak
from core.executor import execute

WAKE_WORD = "hello"

TIMEOUT = 30  # seconds

EXIT_COMMANDS = {
    "sleep",
    "stop listening",
    "goodbye",
    "bye",
    "exit",
    "that's all",
}

print("=" * 50)
print("Babo AI Assistant")
print("=" * 50)

print("Waiting for wake word...")

while True:

    # ---------------------------
    # Sleep Mode
    # ---------------------------
    wake_audio = record_audio(seconds=3)

    wake_text = speech_to_text(wake_audio).lower()

    print("Wake:", wake_text)

    if WAKE_WORD not in wake_text:
        continue

    speak("Yes Rajesh. I'm listening.")

    last_activity = time.time()

    # ---------------------------
    # Conversation Mode
    # ---------------------------
    while True:

        # Auto sleep after timeout
        if time.time() - last_activity > TIMEOUT:

            speak("Going back to sleep.")

            print("Waiting for wake word...")

            break

        command_audio = record_audio(seconds=5)

        command = speech_to_text(command_audio).lower().strip()

        if command == "":
            continue

        print("Command:", command)

        last_activity = time.time()

        # Exit conversation
        if command in EXIT_COMMANDS:

            speak("Okay Rajesh. Call me whenever you need me.")

            print("Waiting for wake word...")

            break

        # Execute
        response = execute(command)

        speak(response)