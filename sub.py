import paho.mqtt.client as mqtt


MQTT_ADDRESS = 'broker.mqttdashboard.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'mex'


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)


def on_message(client, userdata, message):
    print("Message Recieved: " + message.payload.decode())


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_ADDRESS, MQTT_PORT)

    client.subscribe(MQTT_TOPIC, qos=1)

    client.loop_forever()
