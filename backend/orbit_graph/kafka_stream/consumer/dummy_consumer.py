from kafka import KafkaConsumer
from orbit_graph.kafka_stream.config import TOPIC_NAME, KAFKA_SERVER

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

for msg in consumer:
  print("Received a message!")
  print(msg)