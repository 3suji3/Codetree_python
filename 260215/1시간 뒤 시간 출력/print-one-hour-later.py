a = input()
h, m = a.split(":")

if int(h) > 22:
    h = 0
else:
    h = int(h) + 1

print(f"{h}:{m}")
