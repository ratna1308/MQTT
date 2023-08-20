# Project Structure
- mqtt_publisher.py: Python MQTT client to publish mock sensor readings.
- mqtt_subscriber.py: Python MQTT subscriber to store incoming messages in MongoDB and Redis.
- main.py: FastAPI application with endpoints for data retrieval.
- docker-compose.yml: Docker Compose configuration for services.
- mongodb_data/: Directory for MongoDB data persistence.
- requirements.txt: Python dependencies.

# Usage
- Access the FastAPI documentation at http://localhost:8000/docs to explore and test the available endpoints.
- Monitor sensor readings in MongoDB and retrieve the latest readings from Redis.

# Endpoints
- Fetch Sensor Readings by Timestamp Range
- URL: /sensor-readings

- Method: POST

- Request Body:

    json
    
    {
      "start_timestamp": "YYYY-MM-DDTHH:MM:SSZ",
      "end_timestamp": "YYYY-MM-DDTHH:MM:SSZ"
    }

# Retrieve Last Ten Sensor Readings for a Specific Sensor
- URL: /last-ten-readings

- Method: POST

- Request Body:

    json
    
    {
      "sensor_id": "unique_sensor_id"
    }
- Response: List of the last ten sensor readings for the specified sensor.

# Docker Compose
- The included docker-compose.yml file sets up the necessary services for this project. Use the following command to start the Docker containers:


    docker-compose up -d