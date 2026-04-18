# print("hello world")
# response=input("What is your name?")#Ask the user for their name and store it in a variable
# print("Hello"+  response + "!")
# print("*** (awkward silence)")
# age=9
# print ("I am " + str(age) + "years old.")
# word = "Dinosaur"
# if len(word) > 0:
#     print("The word is not empty!")
# else:
#     print("The word is empty!")

user_input = input("Type the word 'silicon volcano': ").lower()
if user_input == "silicon volcano": 
    print("You typed it correctly!")
else:
    print("That's not correct. Try again!")