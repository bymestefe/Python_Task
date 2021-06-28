import random

users = input("please enter the names of the participants, seperated by a comma.")
users_list = users.split(", ")

# print(users_list)
len_of_users_list = len(users_list)

winner_index = random.randint(0, len_of_users_list - 1)

print(f"winner is {users_list[winner_index]}")



