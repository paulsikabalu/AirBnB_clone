#!/usr/bin/env python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Paul"
my_user.last_name = "Sikabalu"
my_user.email = "4929210@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

