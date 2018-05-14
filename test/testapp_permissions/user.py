from flask_login import UserMixin


class User(UserMixin):
    def __init__(self):
        pass
    @property
    def roles(self):
        pass


