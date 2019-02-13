# This will be the base class for specialized item types to be delcared later.
# The item should have name description attributes.
# The name should be one word for ease in parsing later.


class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
