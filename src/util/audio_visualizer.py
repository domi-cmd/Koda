import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import threading, time

class AudioVisualizer:
    path = "output/output.wav"

    def __init__(self):
        pass

    def visualize(self):
        rawFile = wave.open(self.path)

        # Read all frames
        signal = rawFile.readframes(-1)
        signal = np.frombuffer(signal, dtype="int16")

        # Get framerate
        frameRate = rawFile.getframerate()

        # Plot the x-axis in seconds, Time Vector spaced linearly with the size of the audio file
        time = np.linspace(0, len(signal) / frameRate, num=len(signal))

        plt.plot(time, signal)

        plt.show()

    def visualize_live_data(self):
        visThread = threading.Thread(target=self.visualize)
        visThread.start()




