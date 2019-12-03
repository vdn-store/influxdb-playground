import json
import random
import time
from datetime import datetime

import numpy as np
import paho.mqtt.client as mqtt

broker_url = "broker.mqttdashboard.com"
broker_port = 1883


client = mqtt.Client()
client.connect(broker_url, broker_port)


# Mean and Stdev from sample data of customer
tags = [["t1", 83.85, 2.81577190634672], ["t2", 83.85, 2.81577190634672],
        ["t3", 83.85, 2.81577190634672], ["t4", 83.85, 2.81577190634672],
        ["t5", 83.85, 2.81577190634672], ["t6", 83.85, 2.81577190634672],
        ["t7", 83.85, 2.81577190634672], ["t8", 83.85, 2.81577190634672],
        ["t9", 83.85, 2.81577190634672], ["t10", 83.85, 2.81577190634672],
        ["t11", 83.85, 2.81577190634672], ["pr", 5.07, 2.81577190634672]]


# Statuses from sample data of customer
statuses = ["PURE WATER IN",
            "INITIAL H/E EXHAUST",
            "HEAT UP",
            "H/E COOLING EXHAUST",
            "COOLING PHASE"
            ]


def msg_gen():
    timestamp = "\"timestamp\" : \"{}\"".format(
        datetime.now().strftime('%y%m%d-%H%M%S'))
    measures = ", ".join(map(lambda x: "\"{0}\": \"{1}\"".format(
        x[0], round(np.random.normal(x[1], x[2], 1)[0], 2)), tags))
    status = "\"status\" : \"{}\"".format(random.choice(statuses))
    msg = timestamp + ", " + measures + ", " + status

    return eval("json.dumps({" + msg + "})")


for i in range(100):
    mqtt_msg = msg_gen()
    client.publish(
        topic="mex", payload=mqtt_msg, qos=1, retain=False)
    print("Message Published: {}".format(str(i).zfill(3)))
    time.sleep(60)
