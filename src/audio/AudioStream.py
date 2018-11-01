# The class AudioStream plays an audio stream from a file and returns relevant data.
# Currently, only .wav files can be played.

''' Functions in class AudioStream:

    set_wave_path(self, wave_path)              Sets the file path to the audio file to be played.

    init_audio_stream_wav(self, chunk_size)     Initializes an audio stream from a .wav file using pyaudio and wave.
                                                * chunk_size indicates the size of the chunk of audio data to be read
                                                  each tick.

    tick_audio_stream_wav(self)                 Reads a chunk of audio data from the .wav stream.
                                                * Audio data is written to variable "data" as a bytes object.
                                                * Run only when the stream data is not empty.

    check_stream_data_empty(self)               Checks if there is no longer any audio data in the file to be read.
                                                * Useful for terminating the audio stream when the file is done playing.

    get_stream_data(self)                       Returns the stream's current audio data as a bytes object.
                                                * Use only when the stream data is not empty.

    stop_audio_stream(self)                     Closes and terminates the audio stream.

    play_full_stream_wav(self)                  Plays the entire .wav audio stream.
                                                * Used only for testing audio stream functionality.
'''

import pyaudio
import wave


class AudioStream:

    # Initialize an audio stream using pyaudio and wave.

    p = pyaudio.PyAudio()
    stream = None

    wf = None
    data = None
    chunk_size = None
    wave_path = None
    fr = None

    def set_wave_path(self, wave_path):
        self.wave_path = wave_path

    def init_audio_stream_wav(self, chunk_size):
        self.chunk_size = chunk_size
        self.wf = wave.open(self.wave_path, 'rb')  # wf is set to a "wave_read" object.
        self.fr = self.wf.getframerate()
        self.stream = self.p.open( format = self.p.get_format_from_width( self.wf.getsampwidth() ),
                                   channels = self.wf.getnchannels(),
                                   rate = self.fr,
                                   output = True )
        self.data = self.wf.readframes(self.chunk_size)

    # Audio stream tick.

    def tick_audio_stream_wav(self):
        self.stream.write(self.data)
        self.data = self.wf.readframes(self.chunk_size)  # data becomes a standard Python "bytes" object.

    def check_stream_data_empty(self):
        return self.data == '';

    def get_stream_data(self):
        return self.data

    # Terminate audio stream.

    def stop_audio_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    # Play entire audio file (for testing only).

    def play_full_stream_wav(self):
        while not self.check_stream_data_empty():
            self.stream.write(self.data)
            self.data = self.wf.readframes(self.chunk_size)
        self.stop_audio_stream()

    # Misc functions.

    def get_framerate(self):
        return self.fr
