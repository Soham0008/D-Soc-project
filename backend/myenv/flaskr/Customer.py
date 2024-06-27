class Customer:
    def __init__(self, c_ID, c_name, c_email, c_contact):
        self.c_ID = c_ID
        self.c_name = c_name
        self.c_email = c_email
        self.c_contact = c_contact

    def __repr__(self):
        return f"<Customer {self.c_name}>"
