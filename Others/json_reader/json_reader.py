import json
account = {}
with open("data.json") as f: # We need json file
     account = json.load(f)
print(account["username"]) # We work with it as with dictionary
print(account["password"])

account["password"] = "New password"

with open("data.json","w") as f: #w = write
    json.dump(account, f)

print("New password of user {} is {}.".format(account["username"],account["password"]))
