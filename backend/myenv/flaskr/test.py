from .InventoryItem import InventoryItem 

def test_inventory_item_fields():
    item = InventoryItem(
        Item_SKU='SKU123',
        Item_Name='Sample Item',
        Item_Description='sample description',
        Item_Price=10,
        Item_Qty=100
    )

    assert item.Item_SKU == 'SKU123'
    assert item.Item_Name == 'Sample Item'
    assert item.Item_Description == 'sample description'
    assert item.Item_Price == 10
    assert item.Item_Qty == 100

def test_inventory_item_constraints():
    try:
        invalid_item = InventoryItem(Item_SKU='SKU123')
        assert False, "Expected exception not raised"
    except ValueError:
        # Expected behavior
        pass
