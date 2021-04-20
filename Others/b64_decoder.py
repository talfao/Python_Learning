import base64

with open("base64 text file") as f:
    msg = f.read()
print(msg)

for i in range(50):
    msg = base64.b64decode(msg)

print(msg.decode("utf8"))
