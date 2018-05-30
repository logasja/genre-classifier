import datetime
from business_rules.variables import BaseVariables, numeric_rule_variable, select_rule_variable, string_rule_variable
from business_rules.actions import BaseActions, rule_action

class SongVariables(BaseVariables):

    def __init__(self, song):
        self.song = song

    @numeric_rule_variable(label='Numeric representation of song energy.')
    def energy(self):
        return self.song['energy']

    @numeric_rule_variable(label='Major key the song is in.')
    def song_key(self):
        return self.song['key']

    @numeric_rule_variable(label='Song tempo.')
    def tempo(self):
        return self.song['tempo']

    @numeric_rule_variable(label=)

    @string_rule_variable()
    def current_month(self):
        return datetime.datetime.now().strftime("%B")

    @select_rule_variable(options=Products.top_holiday_items())
    def goes_well_with(self):
        return products.related_products


class ProductActions(BaseActions):

    def __init__(self, product):
        self.product = product

    @rule_action(params={"sale_percentage": FIELD_NUMERIC})
    def put_on_sale(self, sale_percentage):
        self.product.price = (1.0 - sale_percentage) * self.product.price
        self.product.save()

    @rule_action(params={"number_to_order": FIELD_NUMERIC})
    def order_more(self, number_to_order):
        ProductOrder.objects.create(product_id=self.product.id,
                                    quantity=number_to_order)
