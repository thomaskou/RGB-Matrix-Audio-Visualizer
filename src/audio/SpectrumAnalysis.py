# The class SpectrumAnalysis includes several functions that involve the analysis of any incoming audio stream.


class SpectrumAnalysis:

    def __init__(self, min_freq, max_freq):
        self.min_freq = min_freq
        self.max_freq = max_freq

    # Function that returns an average amplitude within a certain interval of frequencies.
    def get_amplitude_in_range(self, freq1, freq2):
        return 1

    # Function that returns an average amplitude given a fixed frequency interval size and an index.
    def get_amplitude_at_index(self, index, size):
        interval_size = (self.max_freq - self.min_freq)/size
        freq1 = self.min_freq + (index * interval_size)
        freq2 = self.min_freq + ( (index+1) * interval_size )
        return self.get_amplitude_in_range(freq1, freq2)
