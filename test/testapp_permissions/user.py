from flask_login import UserMixin


class User(UserMixin):
    def __init__(self):
        self.roles = ["admin"]

    def get_roles(self):
        return self.roles

    def get_id(self):
        return "admin"