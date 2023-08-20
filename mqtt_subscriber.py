import paho.mqtt.client as mqtt
import pymongo
import redis
import datetime
from datetime import datetime


broker_address = "192.168.124.41"
broker_port = 1883

client = mqtt.Client()

mongo_host = "localhost"
mongo_port = 27017
mongo_db_name = "sensor_data"

redis_host = "localhost"
redis_port = 6379

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


mongo_client = pymongo.MongoClient(mongo_host, mongo_port)
db = mongo_client[mongo_db_name]


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("sensors/temperature")
        client.subscribe("sensors/humidity")
    else:
        print("Connection to MQTT broker failed with code", rc)


def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")
    print(f"Received message on topic: {topic}\nPayload: {payload}")

    sensor_data = {
        "topic": topic,
        "payload": payload,
        "timestamp": datetime.datetime.now().isoformat(),
    }

    r.lpush("latest_sensor_readings", json.dumps(sensor_data))

    r.ltrim("latest_sensor_readings", 0, 9)


mongo_client = pymongo.MongoClient(mongo_host, mongo_port)
db = mongo_client[mongo_db_name]
collection = db["mqtt_messages"]
