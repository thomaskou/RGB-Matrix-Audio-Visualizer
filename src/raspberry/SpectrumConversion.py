import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


class SpectrumConversion:

    MAX_AMPLITUDE = 2.5

    freqArray = None
    moddedArray = None

    client = None

    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect("172.31.237.19")
        self.client.loop_start()

    def set_array(self, freqArray):
        self.freqArray = freqArray

    def convert_array(self):
        self.moddedArray = []
        for i in range(16):
            x2 = min(int(self.freqArray[i] * 32 / self.MAX_AMPLITUDE), 32)
            self.moddedArray.append(x2)

    def send(self):
        publish.single("array", str(self.moddedArray))
        # print(str(self.moddedArray))

    def tick(self, freqArray):
        self.set_array(freqArray)
        self.convert_array()
        self.send()
