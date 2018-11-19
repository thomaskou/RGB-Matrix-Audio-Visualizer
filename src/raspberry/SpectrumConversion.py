import raspberry.Lights as lightModule


class SpectrumConversion:

    LED_WIDTH = 64
    LED_HEIGHT = 32
    MAX_AMPLITUDE = None

    freqArray = None
    moddedArray = None
    light = lightModule.Lights()

    colors = [
              [255, 51, 51],
              [255, 153, 51],
              [255, 204, 51],
              [255, 255, 51],
              [153, 255, 51],
              [51, 255, 51],
              [51, 255, 153],
              [51, 255, 255],
              [51, 204, 255],
              [51, 153, 255],
              [51, 51, 255],
              [102, 51, 255],
              [153, 51, 255],
              [204, 51, 255],
              [255, 51, 255],
              [255, 51, 153]
    ]

    def set_array(self, freqArray):
        self.freqArray = freqArray

    def convert_array(self):
        self.moddedArray = []
        for i in range(16):
            x2 = min(self.freqArray[i] * 32 / self.MAX_AMPLITUDE, self.MAX_AMPLITUDE)
            self.moddedArray.append(x2)

    def draw(self):
        for k in range(16):
            self.light.fill(4*k, 3*(k+1), 0, self.freqArray[k], self.colors[k][0], self.colors[k][1], self.colors[k][2])

    def set_maxamplitude(self, amplitude):
        self.MAX_AMPLITUDE = amplitude
