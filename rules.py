rules_json = [
# expiration_days < 5 AND current_inventory > 20
{ "conditions": { "all": [
      { "name": "expiration_days",
        "operator": "less_than",
        "value": 5,
      },
      { "name": "current_inventory",
        "operator": "greater_than",
        "value": 20,
      },
  ]},
  "actions": [
      { "name": "put_on_sale",
        "params": {"sale_percentage": 0.25},
      },
  ],
},

# current_inventory < 5 OR (current_month = "December" AND current_inventory < 20)
{ "conditions": { "any": [
      { "name": "current_inventory",
        "operator": "less_than",
        "value": 5,
      },
    ]},
      { "all": [
        {  "name": "current_month",
          "operator": "equal_to",
          "value": "December",
        },
        { "name": "current_inventory",
          "operator": "less_than",
          "value": 20,
        }
      ]},
  },
  "actions": [
    { "name": "order_more",
      "params":{"number_to_order": 40},
    },
  ],
}]