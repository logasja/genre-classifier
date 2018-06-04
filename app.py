from business_rules import run_all
from rules import rules_json
from models import *

rules = rules_json

example = {
    "descriptors": ["grounded", "melodic", "acoustical"],
    "instruments": ["vocals", "horns", "violin"],
    "distortion": False,
    "performers": 20,
    "age": 24,
    "perc_emot": ["content"],
    "felt_emot": ["inspired", "happy"],
    "genre": None,
}

song = example

run_all(rule_list=rules,
    defined_variables=SongVariables(song),
    defined_actions=SongActions(song),
    stop_on_first_trigger=False
    )

print(example["genre"])