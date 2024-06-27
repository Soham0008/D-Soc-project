class InventoryItem:
    def __init__(self, Item_SKU, Item_Name, Item_Description, Item_Price, Item_Qty):
        self.Item_SKU = Item_SKU
        self.Item_Name = Item_Name
        self.Item_Description = Item_Description
        self.Item_Price = Item_Price
        self.Item_Qty = Item_Qty

    def __repr__(self):
        return f"<InventoryItem {self.Item_Name}>"
