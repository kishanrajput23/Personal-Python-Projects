# Take Screenshot Using Pyhton🔥

## 📌Introduction

- Screenshot, also known as screen capture, is a digital image that shows the contents of a computer display. A common screenshot is created by the operating system or software running on the device. Taking, saving, and sharing screenshots can be extremely helpful.

## 📌Steps to Take a Screenshot using Python

- **👉Step 1: Install the pyautogui package**

To start, you’ll need to install the [pyautogui](https://pyautogui.readthedocs.io/en/latest/) package using the following command (under Windows):

    pip install pyautogui
    
**🔸What is PyAutoGUI**

PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.

**✨Features**

**(a)** Moving the mouse and clicking or typing in the windows of other applications.

**(b)** Sending keystrokes to applications (for example, to fill out forms).

**(c)** Take screenshots, and given an image (for example, of a button or checkbox), find it on the screen.

**(d)** Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently)

**(e)** Display message boxes for user interaction while your GUI automation script runs.


- **👉Step 2: Capture the path to save the screenshot**

Next, capture the full path where the screenshot will be saved on your computer.

In my case, I decided to save the screenshot under the following path:

    C:\Users\KISHAN\Desktop\screenshot1.png

Here, the file name is screenshot1, while the file type is png (alternatively, you can set the file type to jpg).

- **👉Step 3: Take the screenshot using Python**

For the final step, you’ll need to use the template below in order to take the screenshot using Python:

    import pyautogui
    
    myscreenshot = pyautogui.screenshot()
    
    myscreenshot.save("Enter your location")

Now, when you run the code the screenshot will automatically save at your provided location with the name of you provided in the code.

That’s it! simple, isn’t it?

