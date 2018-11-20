#!/usr/bin/env python
import paho.mqtt.client as mqtt
from SampleBase import SampleBase

# --led-rows=32 --led-cols=64 --led-pwm-bits ?? --led-slowdown-gpio 2 --led-no-hardware-pulse LED-NO-HARDWARE-PULSE


class Lights(SampleBase):

    WIDTH = 64
    HEIGHT = 32

    array = []
    colors = [ [255, 51, 51], [255, 153, 51], [255, 204, 51], [255, 255, 51],
               [153, 255, 51], [51, 255, 51], [51, 255, 153], [51, 255, 255],
               [51, 204, 255], [51, 153, 255], [51, 51, 255], [102, 51, 255],
               [153, 51, 255], [204, 51, 255], [255, 51, 255], [255, 51, 153] ]

    client = None

    def __init__(self, *args, **kwargs):
        super(Lights, self).__init__(*args, **kwargs)
        self.client = mqtt.Client()
        self.client.connect("172.31.237.19")
        self.client.loop_start()

    def receive(self):
        return

    def fill(self, oc, x1, x2, y1, y2, r, g, b):
        y1 = 32 - y1
        y2 = 32 - y2
        for x in range(x1, x2):
            for y in range(y1, y2):
                oc.SetPixel(x, y, r, g, b)
        oc = self.matrix.SwapOnVSync(oc)

    def run(self):
        oc = self.matrix.CreateFrameCanvas()
        while True:
            self.receive()
            for k in range(16):
                self.fill(oc, 4*k, 3*(k+1), 0, self.array[k], self.colors[k][0], self.colors[k][1], self.colors[k][2])


# Main function
if __name__ == "__main__":
    lights = Lights()
