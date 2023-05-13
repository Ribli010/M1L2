import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenght = int(input("сколько символов должно быть в пароле: "))

password=''

for i in range(lenght):
    password += random.choice(symbols)

print(password)