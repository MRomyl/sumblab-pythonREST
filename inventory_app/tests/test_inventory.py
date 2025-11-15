# tests/test_inventory.py
import pytest
from app.models import InventoryItem

def test_add_get_item():
    InventoryItem.inventory.clear()
    InventoryItem.add_item("1", "Apple", 10, 1.5)
    item = InventoryItem.get_item("1")
    assert item["name"] == "Apple"
    assert item["quantity"] == 10

def test_update_item():
    InventoryItem.add_item("2", "Banana", 5, 0.5)
    updated = InventoryItem.update_item("2", quantity=8)
    assert updated["quantity"] == 8

def test_delete_item():
    InventoryItem.add_item("3", "Orange", 12, 0.75)
    deleted = InventoryItem.delete_item("3")
    assert deleted["name"] == "Orange"
    assert InventoryItem.get_item("3") is None
