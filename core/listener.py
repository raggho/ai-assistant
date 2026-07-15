"""Microphone input handling for Nova."""

import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000

def record_audio(filename="audio/input.wav", seconds=3):
    print("Listening...")

    recording = sd.rec(
        int(seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, SAMPLE_RATE, recording)

    return filename