"""
coding_buddies2021@gmail.com

user name = coding_buddies2021

domain name = gmail.com
"""

#taking email id from the user
emailId = input("Enter your email address ").strip()

#getting username from the email id
user_name = emailId[:emailId.index("@")]

#getting domain name from the email id
domain_name = emailId[emailId.index("@")+1:]

#storing username and domain name in final output variable
final_output = f"Your username is {user_name} and your domain name is {domain_name}"

#printing final output
print(final_output)