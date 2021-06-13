# BMI Calculator🔥

## 📌What is Body Mass Index (BMI)?

- BMI is a measure of relative weight based on an individual’s mass and height. Today, Body Mass Index is commonly used to classify people as underweight, overweight, and even with obesity. Also, it is adopted by countries to promote healthy eating.

- BMI can be considered as an alternative for direct measurements of body fat. Besides, BMI is an inexpensive and easy-to-perform method of screening for weight classes that may cause health problems.

## 📌BMI Calculator with Python

- The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, then dividing the answer again by their height. Now let’s see how to create a BMI calculator with Python:

### Code:

    height = float(input("Enter your height in centimeters (cms) "))

    weight = float(input("Enter your weight in kg "))

    height = height / 100

    BMI = weight / (height ** 2)

    print("Your Body Mass Index is ",BMI)

    if BMI > 0:
        if BMI <= 16:
            print("You are severley underweight")

        elif BMI <= 18:
            print("You are underweight")

        elif BMI <= 25:
            print("You are Healthy")

        elif BMI <= 30:
            print("You are overweight")

        else:
            print("You are severley overweight")

    else:
        print("Please enter correct values") 
        
        
### Output:

    Enter your height in centimeters (cms) 170
    Enter your Weight in Kg 67
    Your Body Mass Index is 23.18339100346021
    You are Healthy
