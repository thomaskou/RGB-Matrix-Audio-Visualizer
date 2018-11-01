# import os
# import numpy as np
import audio.AudioStream as aStr
import audio.AudioSpectrum as aSpec
import audio.SpectrumAnalysis as aSpa


# Local functions.

def get_path(filename):
    return './audio/' + filename


# Instantiate variables.
CHUNK = 2048

# Instantiate relevant classes.
audio = aStr.AudioStream()
spec = aSpec.AudioSpectrum()
span = aSpa.SpectrumAnalysis()

# Pick audio file.
audio.set_wave_path(get_path('test_triangle_arpeggio.wav'))
# audio.set_wave_path(get_path('downloaded/IKSON_PARADISE.wav'))
# audio.set_wave_path(get_path('downloaded/you_already_know_what_it_is.wav'))

# Initialize audio stream.
audio.init_audio_stream_wav(CHUNK)

# Initialize audio plot (for testing only).
span.plot_init()

# Work through entire audio stream.
counter = 0
while not audio.check_stream_data_empty():              # Run the loop while there is still audio data in the file.
    # print("Tick!")
    counter += 1
    audio.tick_audio_stream_wav()                       # Plays the chunk of audio data then gets the next chunk.
    try:
        spec.set_audio_data(audio.get_stream_data())    # Passes audio chunk data to AudioSpectrum for conversion.
        spec.data_to_spectrum()                         # Converts audio chunk data to spectrum data.
        # print(abs(spec.get_spectrum()[0]))
        # print(spec.get_spectrum()[1])
        span.set_spectrum(spec.get_spectrum())          # Passes spectrum data to SpectrumAnalysis.
        print(span.get_amplitude_array(16))
        # span.plot_update()
        # span.plot_pause(0.000000001)
    except ValueError:
        break
audio.stop_audio_stream()                               # Stops the audio stream once there is no longer any audio data.
