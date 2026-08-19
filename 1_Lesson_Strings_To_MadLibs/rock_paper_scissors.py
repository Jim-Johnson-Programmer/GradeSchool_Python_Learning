import random

print("Welcome to our rock-paper-scissors game!")
print("You will be playing against the computer.")

human_choice = input("Please enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"You chose: {human_choice}")
print(f"The computer chose: {computer_choice}")

if human_choice == computer_choice:
    print("It's a tie!")
elif (human_choice == "rock" and computer_choice == "scissors"):
    print("Rock smashes scissors. You win!")
elif(human_choice == "paper" and computer_choice == "rock"):
     print("Paper covers rock. You win!")
elif(human_choice == "scissors" and computer_choice == "paper"):
    print("Scissors cuts paper. You win!")
else:
    print("You lose! Better luck next time.")
    
    
