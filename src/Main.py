import keyboard
import audio.AudioStream as aStr
import audio.InputStream as aInp
import audio.AudioSpectrum as aSpec
import audio.SpectrumAnalysis as aSpa


INPUT = True
TIMED = False
SECONDS = 10

FILE = 'test_triangle_arpeggio.wav'
# FILE = 'downloaded/IKSON_PARADISE.wav'
# FILE = 'downloaded/you_already_know_what_it_is.wav'

CHUNK = 2048


# Local functions.

def get_path(filename):
    return './audio/' + filename


def play_file():

    # Instantiate relevant classes.
    audio = aStr.AudioStream()
    spec = aSpec.AudioSpectrum()
    span = aSpa.SpectrumAnalysis()

    # Initialize class stuff.
    audio.set_wave_path(get_path(FILE))
    audio.init_audio_stream_wav(CHUNK)
    span.set_frequencies(0, audio.get_framerate())

    # Initialize drawing (for testing only).
    # span.plot_init()
    # span.draw_init()

    # Work through entire audio stream.
    while not audio.check_stream_data_empty():              # Run the loop while there is still audio data in the file.
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
    audio.stop_audio_stream()                               # Stops the stream once there is no longer any audio data.


def input_seconds():

    # Instantiate relevant classes.
    inp = aInp.InputStream()
    spec = aSpec.AudioSpectrum()
    span = aSpa.SpectrumAnalysis()

    # Initialize class stuff.
    inp.init_input_stream(CHUNK)
    span.set_frequencies(0, inp.get_framerate())

    # Initialize drawing (for testing only).
    # span.plot_init()
    # span.draw_init()

    # Work through entire audio stream.
    for i in range(0, int(inp.get_framerate() / CHUNK * SECONDS)):
        inp.tick_input_stream()
        try:
            spec.set_audio_data(inp.get_input_data())
            spec.data_to_spectrum()
            # print(abs(spec.get_spectrum()[0]))
            # print(spec.get_spectrum()[1])
            span.set_spectrum(spec.get_spectrum())
            # print(span.get_amplitude_array(16))
            span.plot_update()
            span.plot_pause(0.000000001)
        except ValueError:
            break
    inp.stop_input_stream()


def input_indefinite():

    # Instantiate relevant classes.
    inp = aInp.InputStream()
    spec = aSpec.AudioSpectrum()
    span = aSpa.SpectrumAnalysis()

    # Initialize class stuff.
    inp.init_input_stream(CHUNK)
    span.set_frequencies(0, inp.get_framerate())

    # Initialize drawing (for testing only).
    # span.plot_init()
    # span.draw_init()

    # Work through entire audio stream.
    while True:
        inp.tick_input_stream()
        try:
            spec.set_audio_data(inp.get_input_data())
            spec.data_to_spectrum()
            # print(abs(spec.get_spectrum()[0]))
            # print(spec.get_spectrum()[1])
            span.set_spectrum(spec.get_spectrum())
            # print(span.get_amplitude_array(16))
            span.plot_update()
            span.plot_pause(0.000000001)
        except ValueError:
            break
    inp.stop_input_stream()


if INPUT:
    if TIMED:
        input_seconds()
    else:
        input_indefinite()
else:
    play_file()
