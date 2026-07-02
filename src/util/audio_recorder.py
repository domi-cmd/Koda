"""PyAudio Example: Record a few seconds of audio and save to a wave file."""

import wave
import sys
import pyaudio
import threading, time

class AudioRecorder:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100
    RECORD_SECONDS = 5

    def __init__(self):
        pass

    def recordAudio(self):
        with wave.open('output/output.wav', 'wb') as wf:
            p = pyaudio.PyAudio()
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)

            stream = p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True)

            print('Recording...')
            for _ in range(0, self.RATE // self.CHUNK * self.RECORD_SECONDS):
                wf.writeframes(stream.read(self.CHUNK))
            print('Done')

            stream.close()

            p.terminate()

    def record_live_data(self):
        recThread = threading.Thread(target=self.recordAudio)
        recThread.start()