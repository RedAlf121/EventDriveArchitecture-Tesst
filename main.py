from models.concrete_models.user import User
from models.db import DB

user1 = User(username='francisco',email='francisco@gmail.com')
user2 = User(username='tomasa',email='tomasa@gmail.com')

user1.save()
user2.save()

print(DB[User])