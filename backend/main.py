"""
orbit_graph
"""

import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from kafka import KafkaProducer

from orbit_graph.kafka_stream.config import TOPIC_NAME

from data.mocks import usernames, userDetails, memberGraph, activities
from orbit_graph.query import dbUserDetails, dbUsernames, dbUsernamesPrefix, dbActivities, dbMemberGraph
from orbit_graph.database.orbit_models import MemberGraphEdge

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MemberGraphEdge):
            dic = dict()
            dic["from"] = o.from_edge
            dic["to"] = o.to_edge
            return dic
        return o.__dict__


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


@app.route("/memberGraph")
@cross_origin()
def get_member_graph():
    response = dbMemberGraph()
    return json.dumps(response, cls=MyEncoder)


@app.route("/activities")
@cross_origin()
def get_activities():
    return json.dumps(dbActivities(), cls=MyEncoder)


@app.route("/userDetails/<username>")
@cross_origin()
def get_user_details(username):
    return json.dumps(dbUserDetails(username), cls=MyEncoder)


@app.route("/usernames")
@cross_origin()
def get_usernames():
    return json.dumps(dbUsernames(), cls=MyEncoder)


@app.route("/usernamesWithPrefix/<prefix>")
@cross_origin()
def get_usernames_with_prefix(prefix):
    return json.dumps(dbUsernamesPrefix(prefix), cls=MyEncoder)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
