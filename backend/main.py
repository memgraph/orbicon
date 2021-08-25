"""
orbit_graph
"""

import json
from flask import Flask, jsonify, request
from kafka import KafkaProducer

from orbit_graph.kafka_stream.config import TOPIC_NAME

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"name": "Orbit Graph API"})


@app.route("/webhook", methods=["POST"])
def webhook():
    # TODO(gitbuda): Orbit will use the secret token (the current tokern is
    # testtesttesttesttest as a HMAC-SHA256 key and generate an HMAC hex digest
    # of the HTTP request body. Read more
    # https://docs.orbit.love/docs/webhooks#headers + check the digest from
    # request.headers.
    producer = KafkaProducer(bootstrap_servers=["kafka:9092"], value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    producer.send(TOPIC_NAME, value=request.get_json())
    producer.flush()
    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
