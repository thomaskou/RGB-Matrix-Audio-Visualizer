#!/usr/bin/env python
from raspberry.SampleBase import SampleBase


class Lights(SampleBase):

    canvas = None
    canvas_Height = None
    canvas_Width = None

    def __init__(self, *args, **kwargs):
        super(Lights, self).__init__(*args, **kwargs)
        self.canvas = self.matrix.CreateFrameCanvas()
        self.canvas_Width = self.canvas.width
        self.canvas_Height = self.canvas.height

    def fill(self, x1, x2, y1, y2, r, g, b):
        y1 = 32 - y1
        y2 = 32 - y2
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.canvas.SetPixel(x, y, r, g, b)
        oc = self.matrix.SwapOnVSync(self.canvas)


# Main function
if __name__ == "__main__":
    lights = Lights()
