from business_rules import export_rule_data
from models import *
import json
import os

json_data = export_rule_data(SongVariables, SongActions)

mode = 'r+' if os.path.exists('model.json') else 'w'
with open('model.json', mode) as a_file:
    if mode == 'r+':
        a_file.read()
        a_file.seek(0)
    json.dump(json_data, a_file)
    a_file.truncate()