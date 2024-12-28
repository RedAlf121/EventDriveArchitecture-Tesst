from models.concrete_models.user import User
from models.db import DB

user1 = User('francisco','francisco@gmail.com')
user2 = User('tomasa','tomasa@gmail.com')

user1.save()
user2.save()

print(DB[User])