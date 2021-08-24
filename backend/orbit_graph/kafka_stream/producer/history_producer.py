import logging
from kafka import KafkaProducer
import simplejson as json
from data import get_orbit_json_events
from orbit_graph.kafka_stream.config import TOPIC_NAME, KAFKA_SERVER

log = logging.getLogger("orbit_graph.kafka.history_producer")


def main():
    try:
        data = get_orbit_json_events()
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER], value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        for data_item in data:
            producer.send(TOPIC_NAME, value=data_item)
        log.info("Successfully sent all Orbit historic data.")
    except Exception as e:
        log.error(e)


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)-15s [%(levelname)s] %(name)s: %(message)s", level=logging.INFO)

    main()
