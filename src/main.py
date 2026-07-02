from util.audio_recorder import AudioRecorder
from util.audio_visualizer import AudioVisualizer

import time

def main():
    audioRecorder = AudioRecorder()
    audioRecorder.recordAudio()

    audioVisualizer = AudioVisualizer()
    audioVisualizer.visualize()




if __name__ == "__main__":
    main()