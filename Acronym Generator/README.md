# Acronym Generator🔥

- An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing.

## 📌Create Acronyms using Python

- To create acronyms using Python, you need to write a python program that generates a short form of a word from a given sentence. You can do this by splitting and indexing to get the first word and then combine it. Let’s see how to create an acronym using Python:

**Code:**

    user_input = input("Enter your sentence: ")

    text = user_input.split()

    acronym = ""

    for i in text:
        acronym += i[0].upper()

    print(acronym)
    
**Output:**

    Enter your sentence: artificial intelligence
    
    AI
    
    Enter your sentence: natural language processing
    
    NLP
    
- In the above code, I am first taking a string user input, then I am using the split() function in Python for splitting the sentence. Then I declared a new variable ‘acronym’ to store the actual acronym of a phrase.

- Then at the end, I am running a for loop over the variable ‘text’ which represents the split of user input. While running the for loop we are storing the index value of i[0] of every word after a split and turning it into an uppercase format by using the upper() function.


## 📌Summary

- This is a great python program to test your logical skills. These types of programs contribute a lot to your coding interviews. So you should keep trying such programs to develop a good understanding of creating algorithms to perform well in your coding interviews.
