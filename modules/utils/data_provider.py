import os
import simplejson as json

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_orbit_json_events():
    data_path = os.path.join(SCRIPT_DIR, "..", "data", "memgraph_orbit_events.json")
    with open(data_path, "r") as fp:
        data = json.load(fp)
    return data
