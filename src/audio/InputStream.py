# The class InputStream reads data from live microphone input.

import pyaudio


class InputStream:

    p = pyaudio.PyAudio()
    stream = None
    data = None

    format = pyaudio.paInt16
    chunk_size = None
    fr = 44100

    def init_input_stream(self, chunk_size):
        self.chunk_size = chunk_size
        self.stream = self.p.open( format = self.format,
                                   channels = 2,
                                   rate = self.fr,
                                   input = True,
                                   frames_per_buffer = self.chunk_size )
        self.data = self.stream.read(self.chunk_size)

    def tick_input_stream(self):
        self.data = self.stream.read(self.chunk_size)

    def get_input_data(self):
        return self.data

    def stop_input_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def record_input_seconds(self, seconds):
        for i in range(0, int(self.fr / self.chunk_size * seconds)):
            self.tick_input_stream()

    def get_framerate(self):
        return self.fr
