import json
import random
import time

import numpy as np
import paho.mqtt.client as mqtt


MQTT_ADDRESS = 'broker.mqttdashboard.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'mex'


client = mqtt.Client()
client.connect(MQTT_ADDRESS, MQTT_PORT)


# Mean and Stdev from sample data of customer
recorded_values = [['t1', 83.85, 2.81],
                   ['t2', 83.85, 2.81],
                   ['t3', 83.85, 2.81],
                   ['t4', 83.85, 2.81],
                   ['t5', 83.85, 2.81],
                   ['t6', 83.85, 2.81],
                   ['t7', 83.85, 2.81],
                   ['t8', 83.85, 2.81],
                   ['t9', 83.85, 2.81],
                   ['t10', 83.85, 2.81],
                   ['t11', 83.85, 2.81],
                   ['pr', 8.07, 2.81]]


# Statuses from sample data of customer
statuses = ['PURE WATER IN',
            'INITIAL H/E EXHAUST',
            'HEAT UP',
            'H/E COOLING EXHAUST',
            'COOLING PHASE'
            ]


def msg_gen():
    measurement = '\'measurement\': \'furnace\''
    tags = '\'tags\': {\'status\': \'' + random.choice(statuses) + '\'}'
    values = ', '.join(map(lambda x: '\'{0}\': \'{1}\''.format(
        x[0], round(np.random.normal(x[1], x[2], 1)[0], 2)), recorded_values))
    fields = '\'fields\': {' + values + '}'

    msg = measurement + ', ' + tags + ', ' + fields

    return eval('json.dumps({' + msg + '})')


for i in range(100):
    mqtt_msg = msg_gen()
    client.publish(
        topic=MQTT_TOPIC, payload=mqtt_msg, qos=1, retain=False)
    print('Message Published: {}'.format(str(i).zfill(3)))
    time.sleep(10)
