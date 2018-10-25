import os
import audio.AudioStream as aus


def get_filepath(filename):
    return os.path.join('./audio/' + filename)


stream = aus.AudioStream()

# stream.set_wave_path(get_filepath('test_triangle_arpeggio.wav'))
stream.set_wave_path(get_filepath('downloaded/IKSON_PARADISE.wav'))
stream.init_audio_stream_wav(1024)
stream.play_full_stream_wav()
