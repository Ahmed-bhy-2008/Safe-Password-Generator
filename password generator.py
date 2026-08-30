import random
print("---- Welcome to my safe password generator ----")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
length = int(input("How long should the password be? "))

# 1. Check if the length is too short
if length<8:
    print("Too short! Setting length at least to 8 for security.")
    length=8

# 2. Check if the length is dangerously long
elif length>50:
    print("Too long! Setting length to 50 max.")
    length = 50

# 3. I Used choices() instead of sample() so characters can repeat
password= "".join(random.choices(chars, k=length))

print("Your new password is:", password)