#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from SampleBase import SampleBase

# --led-rows=32 --led-cols=64 --led-pwm-bits ?? --led-slowdown-gpio 2 --led-no-hardware-pulse LED-NO-HARDWARE-PULSE

array = None
client = None


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("array")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic.")


def on_message(client, userdata, msg):
    global array
    array = [int(x) for x in str(msg.payload)[3:-2].split(", ")]
    print(array)


class Lights(SampleBase):

    WIDTH = 64
    HEIGHT = 32

    colors = [ [255, 51, 51], [255, 153, 51], [255, 204, 51], [255, 255, 51],
               [153, 255, 51], [51, 255, 51], [51, 255, 153], [51, 255, 255],
               [51, 204, 255], [51, 153, 255], [51, 51, 255], [102, 51, 255],
               [153, 51, 255], [204, 51, 255], [255, 51, 255], [255, 51, 153] ]

    oc = None

    def __init__(self, *args, **kwargs):
        super(Lights, self).__init__(*args, **kwargs)
        global client
        client = mqtt.Client(client_id="RaspberryPi")
        client.username_pw_set("se101", "se101")
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.connect("m15.cloudmqtt.com", 15406)
        client.loop_start()

    def fill(self, x1, x2, y1, y2, r, g, b):
        y1 = 32 - y1
        y2 = 32 - y2
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.oc.SetPixel(x, y, r, g, b)
        self.oc = self.matrix.SwapOnVSync(self.oc)

    def run(self):
        global array
        self.oc = self.matrix.CreateFrameCanvas()
        while True:
            for k in range(16):
                self.fill(4*k, 3*(k+1), 0, array[k], self.colors[k][0], self.colors[k][1], self.colors[k][2])


# Main function
if __name__ == "__main__":
    lights = Lights()
