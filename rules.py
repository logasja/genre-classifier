rules_json = [
  # Rules for punk rock
  { "conditions": { "all": [
      {
          "name": "distorted",
          "operator": "is_true",
          "value": ""
      }, {
          "name": "perc_emot",
          "operator": "shares_at_least_one_element_with",
          "value": ["angry", "anxious", "determined", "energetic", "tense"]
      }, {
          "name": "instruments",
          "operator": "contains_all",
          "value": ["lead guitar", "bass guitar", "rhythm guitar", "drums", "vocals"]
      }, {
          "name": "performer_count",
          "operator": "less_than_or_equal_to",
          "value": 5
      }, {
          "name": "felt_emot",
          "operator": "shares_no_elements_with",
          "value": ["bored", "content", "hurt", "lost", "loving", "peaceful"]
      },
    ]},
    "actions": [
      {"name":"assign_genre",
        "params":{"genre":"rock"}
      },
    ],
  },

  # Rules for classical score
  { "conditions": {
      "all": [{
          "name": "instruments",
          "operator": "shares_at_least_one_element_with",
          "value": ["piano", "vocals", "horns", "violin"]
      }, {
          "name": "descriptor",
          "operator": "shares_no_elements_with",
          "value": ["sharp", "rough", "chaotic", "hard", "simple", "hurried", "edgy", "grungy", "peppy", "twangy", "bassheavy"]
      }, {
          "name": "perc_emot",
          "operator": "shares_at_least_one_element_with",
          "value": ["angry", "anxious", "content", "happy", "inspired", "lost", "loving", "peaceful"]
      }, {
          "name": "felt_emot",
          "operator": "is_contained_by",
          "value": ["amazed", "angry", "bored", "content", "depressed", "happy", "inspired", "loving", "peaceful", "proud"]
      }, {
          "name": "performer_count",
          "operator": "greater_than_or_equal_to",
          "value": 10
      },
    ]},
    "actions": [
      {"name": "assign_genre",
       "params": {"genre": "classical"}
      },
    ],
  },
]