from flask.ext.login import UserMixin


class User(UserMixin):
     def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password
