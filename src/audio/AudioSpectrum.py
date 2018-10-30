# The class AudioSpectrum is responsible for decoding an audio spectrum from audio data.

''' Functions in class AudioSpectrum:

    set_audio_data(self, data)      Sets the current audio data as a bytes object.
                                    * Use with get_stream_data in class AudioStream.

    data_to_spectrum(self)          Converts the audio data to an audio spectrum.
                                    * Currently, this is done using the FFT algorithm from numpy. Will be changed later.

    get_spectrum(self)              Returns the current audio spectrum.
'''


import numpy as np


class AudioSpectrum:

    data = None
    spec = None

    def set_audio_data(self, data):
        self.data = data

    def data_to_spectrum(self):
        b = list(self.data)  # Converts bytes to bytearray for use with numpy FFT algorithm.
        s = np.fft.fft(b)/len(b)  # Computes the discrete Fourier transform of the bytearray.
        s = s[range(int(len(b)/2))]
        f = [i for i in range(0, int(len(b)/2))]
        self.spec = (s, f)  # Creates a 2-tuple that holds an amplitude array and a frequency array.

    def get_spectrum(self):
        return self.spec
