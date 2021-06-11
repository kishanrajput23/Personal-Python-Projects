# Grammar Correction Using Python🔥

## 📌How to use Python for Grammar Correction?

- There are so many applications that help you to correct your grammatical mistakes while writing. Grammarly is one of the best examples of such applications. It can correct every error while writing and helps you to complete your articles, emails, or any piece of writing without any errors.

- So can we use Python for the task of grammar correction? Yes, we can! The Gingerit library in Python is an open-source library that contains all the features that Grammarly provides. You can easily install it by using the pip command; pip install gingerit. In the section below, I will take you through how to use the gingerit library for the task of Grammar correction using Python.


## 📌Grammar Correction With Python

- By using the gingerit library in Python you can eliminate all the grammatical mistakes, fix your spellings and punctuation errors and at the end, it helps you to enhance your text. Now let’s see how to use this library for the task of grammar correction using Python:

### Code:

    from gingerit.gingerit import GingerIt
    
    text = input("Entr your text ")
    
    corrected_text = GingerIt().parse(text)
    
    print(corrected_text['result'])
    
### Output:

    Enter your text: My name are Kishan.
    My name is Kishan.
    
- In the above code, I am first importing the GingerIt function from the gingerit library, then I am storing a sentence as user input in the variable ‘text’. Then I am initializing the GingerIt() function on the input text. This function returns a dictionary of the text and the result, so to print the final output, I have selected ‘result’ to show the corrected text.

## 📌Summary

- So this is how we can use Python to correct grammatical mistakes from any piece of text. The Gingerit library in Python can be used to enhance your writing by correcting all the mistakes in a few lines of code.
