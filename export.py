from business_rules import export_rule_data
from models import *

json = export_rule_data(SongVariables, SongActions)

print(json)