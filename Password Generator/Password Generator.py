import random
print('Welcome to our Password Generator')
print('=================================')
 
chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'

number =input('Amount of Password generate: ')
number =int(number)

length =input('Enter the length of Password Generate: ')
length =int(length)

print('\nhere is your Password')
for pwd in range(number):
    Passwords =''
    for c in range(length):
        Passwords += random.choice(chars)
    print(Passwords)

   
