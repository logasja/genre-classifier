import datetime
from business_rules.variables import BaseVariables, numeric_rule_variable, select_rule_variable, string_rule_variable
from business_rules.actions import BaseActions, rule_action

class ProductVariables(BaseVariables):

    def __init__(self, product):
        self.product = product

    @numeric_rule_variable
    def current_inventory(self):
        return self.product.current_inventory

    @numeric_rule_variable(label='Days until expiration')
    def expiration_days(self):
        last_order = self.product.orders[-1]
        return (last_order.expiration_date - datetime.date.today()).days

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
