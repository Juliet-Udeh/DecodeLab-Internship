import random

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += str(random.randint(0, 9))

print("Password:", password)
