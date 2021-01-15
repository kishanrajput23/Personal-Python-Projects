import pywhatkit as kt
import getpass as gp

#display welcome msg
print("Let's Automate Whatsapp!")

#capture the target phone number
p_num = gp.getpass(prompt='Phoneumber: ', stream=None) 

#capture the message
msg = "Let's join MLH for Local Hack Day"

# call the method
kt.sendwhatmsg(p_num, msg, 10, 25)