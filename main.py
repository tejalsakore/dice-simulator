import random

again = True

while again:
    print(random.randint(1,6))
    repeat = input("Wanna roll dice again? (y/n):")
    if repeat.lower() == "y":
        continue
    else:
        break

        