import paho.mqtt.client as mqtt
import random
import time


broker_address = "192.168.124.41"
broker_port = 1883

client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection to MQTT broker failed")


def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")
    print(f"Received message on topic: {topic}\nPayload: {payload}")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_start()

topic_to_subscribe = "sensors/temperature"
client.subscribe(topic_to_subscribe)

topic_to_publish = "sensors/humidity"
message_to_publish = "50%"  # Replace with your actual message
client.publish(topic_to_publish, message_to_publish)

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Disconnecting...")
    client.loop_stop()
    client.disconnect()


def generate_sensor_data():
    sensor_id = "sensor_" + str(random.randint(1, 10))
    temperature = round(random.uniform(15, 35), 2)
    humidity = round(random.uniform(30, 70), 2)
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return {
        "sensor_id": sensor_id,
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": timestamp,
    }


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection to MQTT broker failed with code", rc)


client.on_connect = on_connect

client.connect(broker_address, broker_port, 60)

while True:
    sensor_data = generate_sensor_data()
    temperature_topic = "sensors/temperature"
    humidity_topic = "sensors/humidity"
    client.publish(temperature_topic, payload=str(sensor_data["temperature"]), qos=1)
    client.publish(humidity_topic, payload=str(sensor_data["humidity"]), qos=1)
    time.sleep(5)
