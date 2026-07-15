"""
media.py
Volume and media controls for Babo.
"""

import pyautogui
from pycaw.pycaw import AudioUtilities


class MediaController:

    def __init__(self):
        # In current PyCAW versions GetSpeakers() returns an AudioDevice
        # wrapper. Its EndpointVolume property provides the COM interface.
        speakers = AudioUtilities.GetSpeakers()
        self.volume = speakers.EndpointVolume

    # ------------------------
    # Volume Controls
    # ------------------------

    def volume_up(self, step=0.05):

        current = self.volume.GetMasterVolumeLevelScalar()

        self.volume.SetMasterVolumeLevelScalar(
            min(1.0, current + step),
            None
        )

        return "Volume increased."

    def volume_down(self, step=0.05):

        current = self.volume.GetMasterVolumeLevelScalar()

        self.volume.SetMasterVolumeLevelScalar(
            max(0.0, current - step),
            None
        )

        return "Volume decreased."

    def mute(self):

        self.volume.SetMute(1, None)

        return "Muted."

    def unmute(self):

        self.volume.SetMute(0, None)

        return "Unmuted."

    def get_volume(self):

        current = self.volume.GetMasterVolumeLevelScalar()

        return f"Current volume is {int(current*100)} percent."

    # ------------------------
    # Media Keys
    # ------------------------

    def play_pause(self):

        pyautogui.press("playpause")

        return "Play/Pause."

    def next_song(self):

        pyautogui.press("nexttrack")

        return "Next track."

    def previous_song(self):

        pyautogui.press("prevtrack")

        return "Previous track."


media = MediaController()
