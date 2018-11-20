import paho.mqtt.client as mqtt


array = None
client = None


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("array")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic.")


def on_message(client, userdata, msg):
    print([int(x) for x in str(msg.payload)[3:-2].split(", ")])


class MqttTest:

    def __init__(self):
        global client
        client = mqtt.Client(client_id="MqttTest")
        client.username_pw_set("se101", "se101")
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.connect("m15.cloudmqtt.com", 15406)
        client.loop_start()
