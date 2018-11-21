#!/usr/bin/env python3.5
import paho.mqtt.client as mqtt
from SampleBase import SampleBase

# --led-rows=32 --led-cols=64 --led-pwm-bits 1 --led-slowdown-gpio 2 --led-no-hardware-pulse LED-NO-HARDWARE-PULSE

array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
client = None


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("array")
    

def on_disconnect(client, userdata, rc):
    print("Disconnect with result code " + str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic.")


def on_message(client, userdata, msg):
    global array
    # print("Receiving.")
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
        client = mqtt.Client(client_id="RaspberryPi", protocol=mqtt.MQTTv31)
        client.username_pw_set("kvvunrvu", "n0nK2Ew4DjCw")
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.connect("m15.cloudmqtt.com", 15406)
        client.loop_start()

    def fill(self, x1, x2, y1, y2, r, g, b):
        for x in range(x1+1, x2-1):
            for y in range(y1, y2):
                self.oc.SetPixel(x, y, r, g, b)
            for y in range(0, y1-1):
                self.oc.SetPixel(x, y, 0, 0, 0)
        self.oc = self.matrix.SwapOnVSync(self.oc)

    def run(self):
        global array
        self.oc = self.matrix.CreateFrameCanvas()
        while True:
            # print("Running.")
            for k in range(16):
                self.fill(4*k, 4*(k+1), max(0, 32-array[k]), 32, self.colors[k][0], self.colors[k][1], self.colors[k][2])
                # self.fill(4*k, 3*(k+1), 0, array[k], 255, 255, 255)


# Main function
if __name__ == "__main__":
    lights = Lights()
    if (not lights.process()):
        lights.print_help()
