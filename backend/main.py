"""
orbit_graph
"""

import json
import logging
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from kafka import KafkaProducer

from orbit_graph.kafka_stream.config import TOPIC_NAME

from orbit_graph.query import dbUserDetails, dbUsernames, dbUsernamesPrefix, dbActivities, dbMemberGraph, dbLegend
from orbit_graph.database.orbit_models import MemberGraphEdge

# TODO(gitbuda): Huge hack but during hackathon all is allowed!
app = Flask(__name__, template_folder="/frontend", static_folder="/frontend", static_url_path="")

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MemberGraphEdge):
            dic = dict()
            dic["from"] = o.from_edge
            dic["to"] = o.to_edge
            dic["length"] = o.length
            return dic
        return o.__dict__


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/heartbeat")
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
    app.logger.debug("%s", request.get_json())
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


@app.route("/legend")
@cross_origin()
def get_legend():
    return json.dumps(dbLegend(), cls=MyEncoder)


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    app.run(host="0.0.0.0", port=3000)
