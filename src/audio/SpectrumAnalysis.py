# The class SpectrumAnalysis includes several functions that involve the analysis of audio spectrum data.

''' Functions in class SpectrumAnalysis:

    set_frequencies(self, min_freq, max_freq)   Sets a specified minimum and maximum frequency.

    set_spectrum(self, spec)                    Sets the current audio spectrum to be analyzed.
                                                * If min_freq and max_freq are not already defined, set them based on
                                                  the received audio spectrum.
                                                * Use with get_spectrum in class AudioSpectrum.

    get_amplitude_in_range(self, freq1, freq2)  Returns an average amplitude within a certain frequency interval.

    get_amplitude_at_index(self, index, size)   Returns an average amplitude given an index and a fixed interval size.

    get_amplitude_array(self, size)             Returns an audio spectrum amplitude array of a specified size.

    plot_init(self)                             Initializes a matplotlib plot.

    plot_update(self)                           Updates the matplotlib plot.
                                                * plot_pause is required for the plot to generate.

    plot_pause(self, time)                      Pauses the process to update the matplotlib plot for a specified time.
                                                * Very rudimentary solution that needs to be replaced, since the entire
                                                  process pauses for a certain amount of time before continuing.
                                                * Consider multiple threads? (or something like that)
'''

import math
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt


FREQ_BYTE_MIN = 0
FREQ_BYTE_MAX = 1024


class SpectrumAnalysis:

    min_freq = None
    max_freq = None
    freq_byte_interval = None

    spec = None

    # Initialization.

    def set_frequencies(self, min_freq, max_freq):
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.freq_byte_interval = (max_freq - min_freq) / (FREQ_BYTE_MAX - FREQ_BYTE_MIN)
        # print(self.min_freq)
        # print(self.max_freq)
        # print(self.freq_byte_interval)

    def set_spectrum(self, spec):
        self.spec = spec  # spec is a 2-tuple containing an amplitude array and a frequency array.
        if self.min_freq is None or self.max_freq is None:
            self.min_freq = FREQ_BYTE_MIN
            self.max_freq = FREQ_BYTE_MAX
            self.freq_byte_interval = 1

    # Accessors.

    def get_amplitude_in_range(self, freq1, freq2):
        lower = ((freq1 - self.min_freq) / self.freq_byte_interval) + FREQ_BYTE_MIN
        upper = ((freq2 - self.min_freq) / self.freq_byte_interval) + FREQ_BYTE_MIN
        return math.expm1(np.mean(abs(self.spec[0])[int(lower):int(upper):])/2)

    def get_amplitude_at_index(self, index, size):
        interval_size = (self.max_freq - self.min_freq)/size
        freq1 = self.min_freq + (index * interval_size)
        freq2 = self.min_freq + ( (index+1) * interval_size )
        return self.get_amplitude_in_range(freq1, freq2)

    def get_amplitude_array(self, size):
        s = []
        for i in range(size):
            s.append(self.get_amplitude_at_index(i, size))
        return s

    # Tkinter functions.

    def draw_init(self):
        draw = tk.Tk()
        w = tk.Canvas(draw, width=800, height=400)
        w.pack()
        draw.mainloop()

    # Plot functions.

    def plot_init(self):
        plt.ion()
        plt.show()

    def plot_update(self):
        plt.clf()
        plt.bar(range(16), self.get_amplitude_array(16))
        plt.ylim(top=4)
        plt.draw()

    def plot_pause(self, time):
        plt.pause(time)
