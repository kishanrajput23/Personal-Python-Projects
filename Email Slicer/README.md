# Email Slicer🔥

- An Email slicer is a very useful program for separating the username and domain name of an email address. I will be explaining you how to write a program to create an Email Slicer with Python.

## 📌Email Slicer with Python
- To create an email slicer with Python, our task is to write a program that can retrieve the username and the domain name of the email. For example, let's take an email like "codingbuddies2021@gmail.com".

Here, **Username :** codingbuddies2021\
      **Domain name :** gmail.com
      
- So we need to divide the email into two strings using ‘@’ as the separator. Let’s see how to separate the email and domain name with Python:

**Code:**
    
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
    
**Output:**

    Enter your email address codingbuddies2021@gmail.com
    
    Your username is codingbuddies2021 and your domain name is gmail.com

- The code above is very simple and easy to understand. We take user input and use the strip function at the same time to remove white space if any. Then we are finding the index of ‘@’ symbol of the user input. Then we store the index into a variable known as domain_name to split the email into two parts; the user name and the domain.

- Finally, we are just formatting to print the output. The above code can be enhanced with more ideas depending on your needs. As a beginner, you must try these types of programs to improve your coding skills. In the long run, it will also help you build your algorithms and increase your ability to think logically.
