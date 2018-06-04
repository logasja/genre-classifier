rules_json = [
    # Rules for punk rock
    {
        "conditions": { 
            "all": [
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
            ]
        },
        "actions": [
            {
                "name":"assign_genre",
                "params":{"genre":"rock"}
            },
        ],
    },

    # Rules for classical score
    { 
        "conditions":  {
            "all": [
                {
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
                }, {
                    "name": "distorted",
                    "operator": "is_false",
                    "value": ""
                }
            ]
        },
        "actions": [
            {
                "name": "assign_genre",
                "params": {"genre": "classical"}
            },
        ],
    },

    # Rules for general rock
    {
        "conditions" : {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["sharp", "rough", "chaotic", "steady", "hard", "hurried", "edgy", "grungy"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["lead guitar", "bass guitar", "drums", "vocals"]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 10
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["angry", "determined", "energetic", "tense"]
                }, {
                    "any": []
                }
            ]
        },
        "actions" : [
            {
                "name":"assign_genre",
                "params":{"genre":"rock"}
            }
        ],
    },

    # Rules for blues music
    {
        "conditions" : {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["rough", "steady", "grounded", "melodic"]
                }, {
                    "name": "perc_emot",
                    "operator": "contains_all",
                    "value": ["depressed", "hurt", "lost"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["lead guitar", "bass guitar", "drums", "vocals"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["piano", "rhythm guitar", "saxophone", "horns", "violin"]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 10
                }
            ]
        },
        "actions" : [
            {
                "name": "assign_genre",
                "params": {"genre": "blues"}
            }
        ],
    },

    # Rules for country music
    {
        "conditions" : {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["patriotic", "homey", "twangy"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["energetic", "inspired", "proud"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["bass guitar", "drums", "vocals"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["lead guitar", "rhythm guitar", "steel guitar"]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 10
                }
            ]
        },
        "actions" : [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "country"
                }
            }
        ],
    },

    # Rules for reggae music
    {
        "conditions" : {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "contains_all",
                    "value": ["repetitive"]
                }, {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["round", "simple", "leisurly"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["content", "happy", "loving", "peaceful"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["bass guitar", "drums", "vocals"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["piano", "sythesizer"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["lead guitar", "rhythm guitar"]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 10
                }
            ]
        },
        "actions" : [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "reggae"
                }
            }
        ],
    },

    # Rules for rap music
    {
        "conditions" : {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["steady", "hard", "edgy", "bassheavy"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["angry", "anxious", "determined", "energetic", "tense"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["drums", "vocals"]
                }, {
                    "any": [
                        {
                            "name": "age",
                            "operator": "less_than_or_equal_to",
                            "value": 50
                        }, {
                            "name": "felt_emot",
                            "operator": "contains_all",
                            "value": ["annoyed"]
                        }
                    ]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 5
                }
            ]
        },
        "actions" : [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "rap"
                }
            }
        ],
    },

    # Rules for electronic music
    {
        "conditions": 
        {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "contains_all",
                    "value": ["upbeat"]
                }, {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["hurried", "repetitive", "bassheavy"]
                }, {
                    "name": "perc_emot",
                    "operator": "contains_all",
                    "value": ["energetic"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["amazed", "anxious", "determined", "happy", "inspired", "tense"]
                }, {
                    "any": [{
                        "name": "age",
                        "operator": "less_than_or_equal_to",
                        "value": 50
                    }, {
                        "name": "felt_emot",
                        "operator": "contains_all",
                        "value": ["annoyed"]
                    }]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["bass guitar", "drums", "sythesizer"]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 5
                }
            ]
        },
        "actions": [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "electronic"
                }
            }
        ],
    },

        # Rules for world music
    {
        "conditions": 
        {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["patriotic", "upbeat", "homey", "melodic"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["amazed", "energetic", "happy", "inspired", "loving", "proud"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["bass guitar", "drums", "vocals"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["piano", "lead guitar", "rhythm guitar", "saxophone", "horns", "violin"]
                }, {
                    "name": "performer_count",
                    "operator": "greater_than",
                    "value": 3
                }
            ]
        },
        "actions": [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "world"
                }
            }
        ],
    },

        # Rules for classical music
    {
        "conditions":
        {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["complex", "acoustical", "melodic"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["amazed", "anxious", "depressed", "happy", "inspired", "tense"]
                }, {
                    "name": "distorted",
                    "operator": "is_false",
                    "value": ""
                }, {
                    "any": [{
                        "name": "age",
                        "operator": "greater_than_or_equal_to",
                        "value": 30
                    }, {
                        "name": "felt_emot",
                        "operator": "shares_at_least_one_element_with",
                        "value": ["annoyed", "bored", "confused"]
                    }]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["drums", "horns", "violin"]
                }, {
                    "name": "performer_count",
                    "operator": "greater_than_or_equal_to",
                    "value": 10
                }
            ]
        },
        "actions": [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "classical"
                }
            }
        ],
    },

        # Rules for folk music
    {
        "conditions": {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["soft", "leisurly", "grounded", "acoustical", "homey", "melodic"]
                }, {
                    "name": "distorted",
                    "operator": "is_false",
                    "value": ""
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["inspired", "lost", "loving", "peaceful", "proud"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["drums", "vocals"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["piano", "lead guitar", "bass guitar", "rhythm guitar", "steel guitar", "violin"]
                }
            ]
        },
        "actions": [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "folk"
                }
            }
        ],
    },

        # Rules for pop music
    {
        "conditions": {
            "all": [
                {
                    "name": "descriptor",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["simple", "upbeat", "peppy", "repetitive"]
                }, {
                    "name": "perc_emot",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["energetic", "happy", "loving"]
                }, {
                    "name": "instruments",
                    "operator": "contains_all",
                    "value": ["bass guitar", "drums", "vocals"]
                }, {
                    "name": "instruments",
                    "operator": "shares_at_least_one_element_with",
                    "value": ["piano", "lead guitar", "rhythm guitar", "sythesizer"]
                }, {
                    "name": "performer_count",
                    "operator": "less_than_or_equal_to",
                    "value": 10
                }
            ]
        },
        "actions": [
            {
                "name": "assign_genre",
                "params": {
                    "genre": "pop"
                }
            }
        ],
    },
]