import bcrypt
import json
import pickle

with open("user_list.json") as json_file:
    user_pw = json.load(json_file)

users = user_pw.keys()
passwords = user_pw.values()
#print(passwords)

passwords_hashed = []
for i in passwords:
    i_hashed = bcrypt.hashpw(i.encode('utf8'), bcrypt.gensalt())
    passwords_hashed.append(i_hashed)

#print(user_pw)

for user, pw in zip(users,passwords_hashed):
    user_pw[user] = pw

#print(user_pw) 

with open("user_list_hashed.pkl", "wb") as pkl_result:
    pickle.dump(user_pw, pkl_result)
