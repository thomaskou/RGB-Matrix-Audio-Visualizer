###Audio Visualizer for Arduino  
***Contributors**: Thomas Kou, Hansson Lin*

An audio visualization program and our SE 101 term project. For use with Raspberry Pi and
programmed in Python 3.6 using PyCharm.

The `src` folder contains code that runs on a computer, decoding audio signals and
sending them to an external MQTT server. The `raspberry` folder contains a script
`Lights.py` that runs on the Raspberry Pi, which is responsible for receiving messages
from the MQTT server and displaying them on an attached 32x64 LED board.

***

####Libraries used:

* Computer: `numpy`,  `pyaudio`, `wave`, and `paho-mqtt`.

* Raspberry Pi: `paho-mqtt` and `rgbmatrix`.

* `matplotlib` and `tkinter` are optional and used only for testing purposes. If needed,
these can be commented out.

***

####Additional credits:

`raspberry/SampleBase.py` is sourced from the `rpi-rgb-led-matrix` repository and used
under the GPL v2.0 license. Credits go to *hzeller* and the other contributors of the
repository.