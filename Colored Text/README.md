# Print Colored Text with Python🔥

In Python the Colorama module allows us to easily create colored terminal text and I will take you through a tutorial on how to print Colored Text with Python by using the Colorama module in Python.

## 📌What is Colorama in Python?
Using the Colorama module we can print colored text with Python. We can use it and call its built-in variables which are aliases for the desired ANSI codes. This makes our code more readable and works better with Windows command prompts after calling colorama.init() at the start of your script.

The Colorama module offers three main formatting options: Fore, Back, and Style. These allow us to change the foreground or background text color and style. The colors available for the foreground and background are black, red, green, yellow, blue, magenta, cyan, and white.

## 📌Print Colored Text with Python
Traditionally, printing full-colour text to the terminal is accomplished by a series of escape characters on Linux or OS X systems. However, this will not work for Windows operating systems. Now let’s see how to print coloured text with Python using the Colorama module:

**Code**

    import colorama
    from colorama import Fore,Back,Style
    colorama.init()
    print(Fore.GREEN+"HELLO FRIENDS WELCOME TO OUR CODING BUDDIES CHANNEL")
    print(Back.BLUE+"Hi Friends my name Kishan")
    print(Fore.RED+Back.GREEN+"This Is Our Coding Buddies Channel")
    print(Style.BRIGHT+"Do Like Share And Subscribe")
**Output**

<img src="https://github.com/kishanrajput23/Personal-Python-Projects/blob/master/Colored%20Text/Colorama.png" alt="">

It is also possible to change other text properties using ANSI escape characters, for example, if we wanted to make the text darker or lighter. You can try ut out.

