class Staff:
    def __init__(self, s_ID, s_name, s_email, s_isAdmin, s_contact):
        self.s_ID = s_ID
        self.s_name = s_name
        self.s_email = s_email
        self.s_isAdmin = s_isAdmin
        self.s_contact = s_contact

    def __repr__(self):
        return f"<Staff {self.s_name}>"
