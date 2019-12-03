from influxdb import InfluxDBClient
import random

# Statuses from sample data of customer
statuses = ["PURE WATER IN",
            "INITIAL H/E EXHAUST",
            "HEAT UP",
            "H/E COOLING EXHAUST",
            "COOLING PHASE"
            ]

# Mean and Stdev from sample data of customer
tags = [["t1", 83.85, 2.81577190634672], ["t2", 83.85, 2.81577190634672],
        ["t3", 83.85, 2.81577190634672], ["t4", 83.85, 2.81577190634672],
        ["t5", 83.85, 2.81577190634672], ["t6", 83.85, 2.81577190634672],
        ["t7", 83.85, 2.81577190634672], ["t8", 83.85, 2.81577190634672],
        ["t9", 83.85, 2.81577190634672], ["t10", 83.85, 2.81577190634672],
        ["t11", 83.85, 2.81577190634672], ["pr", 5.07, 2.81577190634672]]

json_body = [
    {
        "measurement": "PLC-"+{0},
        "tags": {
            "status": random.choice(statuses)
        },
        "time": {2},
        "fields": {
            "t1": {2},
            "t2": {3},
            "t3": {4},
            "t4": {5},
            "t5": {6},
            "t6": {7},
            "t7": {8},
            "t8": {9},
            "t9": {10},
            "t10": {11},
            "t12": {12},
            "pr": {13}
        }
    }
]
def msg_gen():
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')



    
   