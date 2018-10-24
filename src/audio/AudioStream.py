# The class AudioStream accesses the current audio stream and returns relevant data through various functions.
# Currently, only .wav files can be played.

import pyaudio
import numpy as np
import wave


class AudioStream:

    # Initialize an audio stream using pyaudio.

    p = pyaudio.PyAudio()
    stream = None

    wf = None
    data = None
    chunk_size = None
    wave_path = None

    def set_wave_path(self, wave_path):
        self.wave_path = wave_path

    def init_audio_stream_wav(self, chunk_size):
        self.chunk_size = chunk_size
        self.wf = wave.open(self.wave_path, 'rb')
        self.stream = self.p.open( format = self.p.get_format_from_width( self.wf.getsampwidth() ),
                                   channels = self.wf.getnchannels,
                                   rate = self.wf.getframerate,
                                   output = True )
        self.data = self.wf.readframes(self.chunk_size)

    # Audio stream tick.

    def tick_audio_stream_wav(self):
        self.stream.write(self.data)
        self.data = self.wf.readframes(self.chunk_size)

    def check_stream_data_empty(self):
        return self.data == '';

    # Terminate audio stream.

    def stop_audio_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    # Play entire audio file.

    def play_full_stream_wav(self):
        while self.check_stream_data_empty() == False:
            self.stream.write(self.data)
            self.data = self.wf.readframes(self.chunk_size)
        self.stop_audio_stream()