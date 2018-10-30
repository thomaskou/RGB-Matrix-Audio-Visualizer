# The class SpectrumAnalysis includes several functions that involve the analysis of any incoming audio stream.

''' Functions in class SpectrumAnalysis:

    __init__(self, min_freq, max_freq)          Initializes the instance with a specified minimum and maximum frequency.

    set_spectrum(self, spec)                    Sets the current audio spectrum to be analyzed.
                                                * Use with get_spectrum in class AudioSpectrum.

    get_amplitude_in_range(self, freq1, freq2)  Returns an average amplitude within a certain frequency interval.

    get_amplitude_at_index(self, index, size)   Returns an average amplitude given an index and a fixed interval size.
'''


class SpectrumAnalysis:

    min_freq = None
    max_freq = None

    spec = None

    def __init__(self, min_freq, max_freq):
        self.min_freq = min_freq
        self.max_freq = max_freq

    def set_spectrum(self, spec):
        self.spec = spec

    # Unfinished function.
    def get_amplitude_in_range(self, freq1, freq2):
        return 1

    def get_amplitude_at_index(self, index, size):
        interval_size = (self.max_freq - self.min_freq)/size
        freq1 = self.min_freq + (index * interval_size)
        freq2 = self.min_freq + ( (index+1) * interval_size )
        return self.get_amplitude_in_range(freq1, freq2)
