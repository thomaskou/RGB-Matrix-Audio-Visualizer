# The class AudioSpectrum is responsible for storing information about the decoded audio spectrum.

''' Functions in class AudioSpectrum:

    set_audio_data(self, data)      Sets the current audio data.
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

    # Unfinished function.
    def data_to_spectrum(self):
        spec = np.fft.fft(self.data)

    def get_spectrum(self):
        return self.spec
