from util.audio_recorder import AudioRecorder
from util.audio_visualizer import AudioVisualizer
from gui.sound_display import WaveformDisplay

import time

def main():
    audioRecorder = AudioRecorder()
    #audioRecorder.recordAudio()

    audioVisualizer = AudioVisualizer()
    #audioVisualizer.visualize()

    # Try the gui
    waveformDisplay = WaveformDisplay()
    audioRecorder.startAudioStream()
    audioRecorder.streamToGUI(waveformDisplay)




if __name__ == "__main__":
    main()