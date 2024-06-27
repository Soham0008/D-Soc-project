class Transaction:
    def __init__(self, t_ID, c_ID, s_ID, Item_SKU, t_date, t_amount, t_category):
        self.t_ID = t_ID
        self.c_ID = c_ID
        self.s_ID = s_ID
        self.Item_SKU = Item_SKU
        self.t_date = t_date
        self.t_amount = t_amount
        self.t_category = t_category

    def __repr__(self):
        return f"<Transaction {self.t_ID}>"
