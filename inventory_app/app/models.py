# app/models.py
class InventoryItem:
    inventory = {}  

    @classmethod
    def add_item(cls, item_id, name, quantity, price):
        cls.inventory[item_id] = {
            "id": item_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }
        return cls.inventory[item_id]

    @classmethod
    def get_item(cls, item_id):
        return cls.inventory.get(item_id)

    @classmethod
    def update_item(cls, item_id, **kwargs):
        if item_id not in cls.inventory:
            return None
        cls.inventory[item_id].update(kwargs)
        return cls.inventory[item_id]

    @classmethod
    def delete_item(cls, item_id):
        return cls.inventory.pop(item_id, None)

    @classmethod
    def list_items(cls):
        return list(cls.inventory.values())
