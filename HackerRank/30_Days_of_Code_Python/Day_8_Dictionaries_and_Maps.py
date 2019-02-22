# Day 8: Dictionaries and Maps

n = input("")
n = int(n)
friends = dict()

for inp in range(n):
    friend = input("")
    inp = friend.split()
    name = inp[0]
    phone = inp[1]
    friends[name] = phone

for ask in range(n):
    query = input("")
    if query in friends.keys():
        print(query + "=" + friends[query])
    else :
        print("Not found")
