import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class WaveformDisplay:
    def __init__(self):
        AppFont = 'Any 16'
        sg.theme('DarkTeal2')
         # Timeout in ms for the event loop
        self.TIMEOUT = 10 
        self.layout = [[sg.Canvas(key='figCanvas')],
                [sg.ProgressBar(4000, orientation='h',
                                size=(60, 20), key='-PROG-')],
                [sg.Button('Listen', font=AppFont),
                sg.Button('Stop', font=AppFont, disabled=True),
                sg.Button('Exit', font=AppFont)]]
        
        self.window = sg.Window('Microphone Waveform Pyplot',
                                    self.layout, finalize=True,
                                    location=(400, 100))
        
        CHUNK = 1024

        # Draw empty plot first
        xData = np.linspace(0, CHUNK, num=CHUNK, dtype=int)
        yData = np.zeros(CHUNK)
        self.drawPlot(xData, yData)


    def draw_figure(self, canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    def drawPlot(self, xData, yData):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.line1, = self.ax.plot(xData, yData, '--k')
      
        plt.ylim(-10, 10)
        self.figg_agg = self.draw_figure(
            self.window['figCanvas'].TKCanvas, self.fig)


    def updatePlot(self, data):
        # Incase data has not been initialized yet
        if data is None:
            return

        x = np.arange(len(data))

        self.line1.set_xdata(x)
        self.line1.set_ydata(data)

        pos_ylim = np.max((np.max(data), 30))
        neg_ylim = np.min((np.min(data), -30))
        self.ax.set_ylim(neg_ylim, pos_ylim)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()