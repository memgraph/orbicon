import simplejson as json
from pathlib import Path

def get_orbit_json_events():
  data_path = Path("./backend/data/memgraph_orbit_events.json")
  with open(data_path, 'r') as fp:
    data = json.load(fp)
  return data