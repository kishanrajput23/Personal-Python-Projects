# Story Generator🔥

Do you think the most complex use of the random module in Python is random sampling? No, we can also generate random stories or anything beyond that using the random module.

## 📌Story Generator with Python
Our task is to generate a random story every time the user runs the program. I will first store the parts of the stories in different lists, then the Random module can be used to select the random parts of the story stored in different lists:

**Code**

    import random
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
    name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
    residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
    went = ['cinema', 'university','seminar', 'school', 'laundry']
    happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

**Output:**

    On 20th Jan, a rabbit that lived in Germany, went to the laundry and made a lot of friends

Here, I first imported the random module and then I created parts of the stories in different lists, then I only selected the parts of the lists at random to generate a random story.

As a beginner, you look for creating software applications more, which is not wrong. But spending more time with programs which required you to think logically will always help you no matter what aspect of programming interests you.

## 📌Summary
There are a few areas where the above code could be improved upon, but at a basic level, it meets many secure password generation requirements by today’s standards. 

As a newbie to Python or any other language, you should keep trying these types of programs as they help you explore more functions and in the long run will help you design your algorithms and doing a great job in coding interviews.
