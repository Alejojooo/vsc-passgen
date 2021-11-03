import random

char = "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
password = ""
password_lenght: int = 20

for i in range(1, password_lenght + 1):
    nextChar = char[random.randint(0, len(char) - 1)]
    password += nextChar

print("Your password is:", password)
