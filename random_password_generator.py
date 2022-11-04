import random
from turtle import*
import time
def a():
    print('You password is generating.....')
    time.sleep(1)
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    number = '1234567890'
    symbol = '@#&'
    everything = lower + upper + number + symbol
    password = ''.join(random.sample(everything, length))
    print(f'It is your password: {password}')
while True:
    length=int(input("Please Give The Length Of Password You Want\n"))
    if (length>4 and length<30):
        a()
        time.sleep(2)
        print("Need Another Password ?")
        time.sleep(1)
    else:
         print('Please Provide The Length Grater Than 3 Or Lesser Than 30...')
         break
    Mas=(input("[Yes/No]"))
    if Mas=="Yes":
        continue
    elif Mas=="No":
        break
    else:
        print("Please Give Proper Answer! ")
        break