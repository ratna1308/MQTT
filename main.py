from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import redis

# MongoDB configuration
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["sensor_data"]
mongo_collection = mongo_db["mqtt_messages"]

# Redis configuration
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


app = FastAPI()


class SensorReadingsRequest(BaseModel):
    start_timestamp: str
    end_timestamp: str


class LastTenReadingsRequest(BaseModel):
    sensor_id: str


# MongoDB configuration
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["sensor_data"]
mongo_collection = mongo_db["mqtt_messages"]

# Redis configuration
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


@app.post("/sensor-readings")
async def get_sensor_readings(request: SensorReadingsRequest):
    start_timestamp = request.start_timestamp
    end_timestamp = request.end_timestamp

    query = {"timestamp": {"$gte": start_timestamp, "$lte": end_timestamp}}
    readings = list(mongo_collection.find(query))

    return readings


@app.post("/last-ten-readings")
async def get_last_ten_readings(request: LastTenReadingsRequest):
    sensor_id = request.sensor_id

    last_ten_readings = redis_client.lrange(sensor_id, 0, 9)

    return last_ten_readings
