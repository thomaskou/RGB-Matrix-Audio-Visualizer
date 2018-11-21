import paho.mqtt.publish as publish
import raspberry.MqttTest as MT
import threading


class SendThread(threading.Thread):

    threadArray = None

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.send()

    def send(self):
        publish.single("array", payload=str(self.threadArray), hostname="m15.cloudmqtt.com", port=15406,
                       auth={'username':"se101", 'password':"se101"}, tls=None)

    def set_array(self, array):
        self.threadArray = array


class SpectrumConversion:

    MAX_AMPLITUDE = 1

    freqArray = None
    moddedArray = None

    client = None
    # mtest = None

    thread = None

    def __init__(self):
        # self.mtest = MT.MqttTest()
        self.thread = SendThread()
        self.thread.start()

    def set_array(self, freqArray):
        self.freqArray = freqArray

    def convert_array(self):
        self.moddedArray = []
        for i in range(16):
            x1 = self.freqArray[i] - 0.9
            x2 = int(min(min(int(x1 * 32 / self.MAX_AMPLITUDE), 32) * 2.2, 32))
            self.moddedArray.append(x2)
        self.moddedArray[0] = int((self.moddedArray[0] + self.moddedArray[1]) / 2)

    def tick(self, freqArray):
        self.set_array(freqArray)
        self.convert_array()
        self.thread.set_array(self.moddedArray)
