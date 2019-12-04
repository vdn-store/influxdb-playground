from influxdb import InfluxDBClient
import json
import random
import time
from datetime import datetime

import numpy as np

t_mean = 83.85
t_dev = 2.81577190634672

pr_mean = 5.07
pr_dev = 2.81577190634672


def msg_gen(machine):
    json_body = [
        {
            "measurement": "terumo-1",
            "tags": {
                "machine": "MC-" + machine
            },
            "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "t1": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t2": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t3": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t4": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t5": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t6": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t7": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t8": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t9": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t10": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "t11": round(np.random.normal(t_mean, t_dev, 1)[0], 2),
                "pr": round(np.random.normal(pr_mean, pr_dev, 1)[0], 2),
                "status": random.choice(["PURE WATER IN", "INITIAL H/E EXHAUST", "HEAT UP", "H/E COOLING EXHAUST", "COOLING PHASE"])
            }
        }
    ]

    return json_body


host = 'ec2-13-229-222-208.ap-southeast-1.compute.amazonaws.com'
port = 8086
user = 'admin'
password = 'mex@123'
dbname = 'mex_demo'
client = InfluxDBClient(host, port, user, password, dbname)
client.create_database(dbname)

while(1):
    for i in range(1, 11, 1):
        json_body = msg_gen("{:02d}".format(i))
        print(json_body)
        client.write_points(json_body)
        time.sleep(1)
