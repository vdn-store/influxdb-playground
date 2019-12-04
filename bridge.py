import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import json

INFLUXDB_ADDRESS = 'localhost'
INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DATABASE = 'mex'

MQTT_ADDRESS = 'broker.mqttdashboard.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'mex'

influxdb_client = InfluxDBClient(
    INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC, qos=1)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    print("Message Recieved: " + msg.payload.decode())
    gateway_msg = json.loads(msg.payload.decode())
    if gateway_msg is not None:
        mqtt_to_influxdb(gateway_msg)


def mqtt_to_influxdb(gateway_msg):
    influxdb_client.write_points([gateway_msg])


def init_influxdb():
    databases = influxdb_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)


def main():
    init_influxdb()

    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_ADDRESS, MQTT_PORT)

    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()
