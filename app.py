from business_rules import run_all
from rules import rules_json
from models import *

rules = rules_json

run_all(rule_list=rules,
        defined_variables=SongVariables(song),
        defined_actions=SongActions(song),
        stop_on_first_trigger=False
        )