# Age Categorization Program
# print("Welcome to the age checker!")
# age = int(input("Please enter your age: "))

# if age < 14:
#     print("You are a child")
# elif age < 20:
#     print("You are an Teenager.")
# elif age < 60:
#     print("You are an Adult.")
# else:
#     print("You are a senior.")  


# Movie Ticket Pricing and 2$ discount on wednesday
# from datetime import datetime;

# print("Welcome to the movie ticket pricing system!")
# age = int(input("Please enter your age: "))
# day = datetime.now().strftime("%A").lower() 

# price = 12 if age >= 18 else 8

# if day == "wednesday":
#     price -= 2
# print(f"Your ticket price is: ${price}")


# Grade Calculator
# print("Welcome to the grade calculator!")
# score = int(input("Please enter your score (0-100): "))

# if score > 100 or score < 0:
#     print("Invalid score!")
#     exit()
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:    grade = "F"
# print(f"Your grade is: {grade}")


# Fruit Ripeness Checker
# print("Welcome to the fruit ripeness checker!")
# colour = input("Please enter the colour of the fruit (green, yellow, orange): ").lower()
# if colour == "green":
#     print("The fruit is unripe.")
# elif colour == "yellow":
#     print("The fruit is ripe.")
# elif colour == "orange":
#     print("The fruit is overripe.")


# weather activity suggestion
# print("Welcome to the weather activity suggestion system!")
# weatherType = input("Please enter the weather type (sunny, rainy, snowy): ").lower()

# if weatherType == "sunny":
#     print("It's a great day go for a walk!")
# elif weatherType == "rainy":
#     print("It's a perfect day to stay indoors and read a book!")
# elif weatherType == "snowy":
#     print("It's a great day to build a snowman!")
# else:    print("Invalid weather type!")


# Transportation Mode Suggestion
# print("Welcome to the transportation mode suggestion system!")
# distance = float(input("Please enter the distance you want to travel (in km): "))
# if distance < 4:
#     print("You can walk to your destination.")
# elif distance < 16:
#     print("You can bike to your destination.")
# else:
#     print("You can drive car to your destination.")


# coffee customization
# print("Welcome to the coffee customization system!")
# size = input("Please enter the size of your coffee (small, medium, large): ").lower()
# isExtraShot = bool(input("Do you want an extra shot of espresso? (yes/no): ").lower() == "yes")

# if isExtraShot:
#     print(f"You have ordered a {size} coffee with an extra shot of espresso.")
# else:   
#     print(f"You have ordered a {size} coffee without an extra shot of espresso.")


# password strength checker
# print("Welcome to the password strength checker!")
# password = input("Please enter your password: ")
# if len(password) <= 6:
#     print("Your password is weak. It should be at least 6 characters long.")
# elif len(password) <= 10:
#     print("Your password is medium. Consider adding more characters for better security.")
# else:    print("Your password is strong. Good job!")    


# Leap Year Checker
# print("Welcome to the leap year checker!")
# year = int(input("Please enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# Pet Food Recommendation
# print("Welcome to the pet food recommendation system!")
# petType = input("Please enter your pet type (dog, cat, bird): ").lower()
# petAge = int(input("Please enter your pet's age: "))

# if petType == "dog":
#     if petAge < 2:
#         print("We recommend puppy food for your dog.")
#     elif petAge < 7:
#         print("We recommend adult dog food for your dog.")
#     else:
#         print("We recommend senior dog food for your dog.")
# elif petType == "cat":
#     if petAge < 1:
#         print("We recommend kitten food for your cat.")
#     elif petAge < 10:
#         print("We recommend adult cat food for your cat.")
#     else:
#         print("We recommend senior cat food for your cat.")
# elif petType == "bird":
#     if petAge < 1:
#         print("We recommend baby bird food for your bird.")
#     elif petAge < 5:
#         print("We recommend juvenile bird food for your bird.")
#     else:
#         print("We recommend adult bird food for your bird.")
# else:
#     print("Wrong pet type! We currently only support dogs, cats, and birds.")
