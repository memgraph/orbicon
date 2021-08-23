from time import sleep
from kafka import KafkaProducer
import simplejson as json
from data import get_orbit_json_events
from orbit_graph.kafka_stream.config import TOPIC_NAME, KAFKA_SERVER

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER], value_serializer=lambda v: json.dumps(v).encode("utf-8"))

data = get_orbit_json_events()

for data_item in data:
    producer.send(TOPIC_NAME, value=data_item)
    print("Sent 1 item through kafka!")
    print(data_item)
    sleep(1)
