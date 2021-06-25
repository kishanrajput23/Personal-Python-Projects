# Password Generator🔥

- To create a password with Python, we need to create a program that takes the length of the password and generates a random password of the same length apart from this our program also generates as many passwords as we want with same length.

## 📌Python Program to Generate Password

- To write a Python program to create a password, declare a string of numbers + uppercase + lowercase + special characters. Take a random sample of the string of a length given by the user

**Code:**

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
        
**Output:**

    Welcome to our Password Generator
    =================================
    Amount of Password generate: 5
    Enter the length of Password Generate: 8

    here is your Password
    ag#ZmCmM
    0Kf?z*nl
    *&U31t6W
    0fyIC&#b
    JFkDnOU^

- In the above code, I first imported the random module in Python, then I asked for user input for the amount of the password he/she want. After that I asked for user input for the length of the password. Then I use a for loop here which should run as many times as many times we want amount of password generated.

- Then in the for loop I created a variable named as "Passwords" and define it with blank string. Then again I'm using a for loop here which should run as many times as length of password we want. After that I stored the letters, numbers and special characters that I want to be considered while generating a password which will finally generate a random password and prints it.

## 📌Summary
- There are a few areas where the above code could be improved upon, but at a basic level, it meets many secure password generation requirements by today’s standards. As a newbie to Python or any other language, you should keep trying these types of programs as they help you explore more functions and in the long run will help you design your algorithms.
