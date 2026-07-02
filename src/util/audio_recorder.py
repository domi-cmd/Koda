"""PyAudio Example: Record a few seconds of audio and save to a wave file."""

import wave
import sys
import pyaudio
import threading, time
import numpy as np

class AudioRecorder:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1 if sys.platform == 'darwin' else 2
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.audioStream = None
        self.pyAud = pyaudio.PyAudio()
        self.audioData = None

    def recordAudio(self):
        with wave.open('output/output.wav', 'wb') as wf:
            p = self.pyAud
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


    def callback(self, in_data, frame_count, time_info, status):
        self.audioData = np.frombuffer(in_data, dtype=np.int16)
        return (in_data, pyaudio.paContinue)
    

    def startAudioStream(self):
        self.audioStream = self.pyAud.open(rate = self.RATE,
                              channels = self.CHANNELS,
                              format = self.FORMAT,
                              input = True,
                              frames_per_buffer = self.CHUNK,
                              stream_callback = self.callback)
        self.audioStream.start_stream()


    def stopAudioStream(self):
        if(self.audioStream):
            self.audioStream.stop_stream()
            self.audioStream.close()

    
    def streamToGUI(self, gui):
        while True:
                print(self.audioData)
                gui.updatePlot(self.audioData)


    #def record_live_data(self):
    #    recThread = threading.Thread(target=self.recordAudio)
    #    recThread.start()
    