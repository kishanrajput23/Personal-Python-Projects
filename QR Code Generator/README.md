# QR Code Generator Using Python🔥

QR is short for Quick Response, and they are named so because they can be read quickly by a cell phone. They are used to take information from transitory media and put it on your cell phone.

## 📌What is a QR code?

- QR codes are used to encode and decode the data into a machine-readable form. The use of camera phones to read two-dimensional barcodes for various purposes is currently a popular topic in both types of research and practical applications. 

- It contains a grid of black squares on a white background, which can be read by any imaging device such as a camera, and processed to extract the required data from the patterns that are present in the horizontal components of the image.

## 📌QR Codes with Python

- In this section, I will take you through a tutorial on how to generate QR codes with Python. To generate QR Codes with Python you need to install only one Python library for this task:
    
      pip install pyqrcode
      
Now let’s see how to create a QR Code with Python programming language:

**Code**

    import qrcode
    
    url='Coding Buddies'    # String which represent the QR code
    
    code_image =qrcode.make(url)    # Generate QR code
    
    code_image.save('Enter your Location')    # Create and save the png file at given location
    

**Generated QR-Code**
    
<img src="https://github.com/kishanrajput23/Personal-Python-Projects/blob/master/QR%20Code%20Generator/youtube.svg" alt="">
    
Now we finally built it.👍
