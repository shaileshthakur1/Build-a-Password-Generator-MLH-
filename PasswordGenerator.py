#this is program implementation of "random password generator" using random method in python.

import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!~@#$%^&*(){}[]:'?><"
length_password = int(input("Enter the length of the password: "))
a = "".join(random.simple(password,length_password))
print("Your Random password is {a}")
