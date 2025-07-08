import random
import string

length = int(input("Enter the length of Password You Want: "))
char = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(char) for _ in range(length))
print("Succesfully genrated")
print("Your Genrate Password:", password)