import os
import audio.AudioStream as aus


"""
def get_filepath(filename):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, 'audio', filename)
"""


stream = aus.AudioStream()

# stream.set_wave_path(get_filepath('test_triangle_arpeggio.wav'))
# stream.set_wave_path('./audio/test_triangle_arpeggio.wav')
stream.set_wave_path('./audio/downloaded/IKSON_PARADISE.wav')
stream.init_audio_stream_wav(1024)
stream.play_full_stream_wav()
