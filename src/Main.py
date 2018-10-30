import os
import audio.AudioStream as astr
import audio.AudioSpectrum as aspec
import audio.SpectrumAnalysis as aspa


# Local functions.

def get_path(filename):
    return './audio/' + filename


# Instantiate variables.
CHUNK = 1024

# Instantiate relevant classes.
audio = astr.AudioStream()
spec = aspec.AudioSpectrum()
# analysis = aspa.SpectrumAnalysis()

# Pick audio file.
audio.set_wave_path(get_path('test_triangle_arpeggio.wav'))
audio.set_wave_path(get_path('downloaded/IKSON_PARADISE.wav'))
audio.set_wave_path(get_path('downloaded/you_already_know_what_it_is.wav'))

# Initialize audio stream.
audio.init_audio_stream_wav(CHUNK)

# Play audio stream.
while not audio.check_stream_data_empty():
    audio.stream.write(audio.data)
    audio.data = audio.wf.readframes(audio.chunk_size)
audio.stop_audio_stream()