from Modules.items import Item
import json

def load_json(path):
	with open(path, "r") as f:
		return json.load(f)