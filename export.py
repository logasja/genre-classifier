from business_rules import export_rule_data
from models import *
import json

json_data = export_rule_data(SongVariables, SongActions)

with open('model.json', 'r+') as a_file:
    a_file.read()
    a_file.seek(0)
    json.dump(json_data, a_file)
    a_file.truncate()