import random

# print(random.random())
# print(random.randint(10,20))
# print(random.choice(["apple", "banana", "cherry"]))


# a=["hello", "world", "python", "programming"]
# print(random.choice(a))


# # Game ( Guess the number. Counting the number of attempts )
# number = random.randint(1, 10)
# attempts = 0
# while True:
#     print("Enter your guess:")
#     guess = int(input())
#     attempts = attempts + 1

#     if guess == number:
#         print(" You guessed the number.")
#         break
#     else:
#         print("Try again.")
# print("Number of attempts:", attempts)


# # Game ( Guess the number. )
# number = random.randint(1, 10)

# while True:
#     print("Enter your guess:")
#     guess = int(input())

#     if guess == number:
#         print(" You guessed the number.")
#         break
#     else:
#         print("Try again.")


# number = random.randint(1, 100)
# attempts = 0
# while True:
#     print("Enter your guess:")
#     guess = int(input())
#     attempts = attempts + 1

#     if guess == number:
#         print(" You guessed it.")
#         break
#     elif guess < number:
#         print("Number is Higher. Try again.")
#     else:
#         print("Number is Lower. Try again.")

# print("Number of attempts:", attempts)


# # Same game but play again and again until user wants to quit
# while True:
#     number = random.randint(1, 100)
#     attempts = 0
#     while True:
#         print("Enter your guess:")
#         guess = int(input())
#         attempts = attempts + 1

#         if guess == number:
#             print(" You guessed it.")
#             break
#         elif guess < number:
#             print("Number is Higher. Try again.")
#         else:
#             print("Number is Lower. Try again.")

#     print("Number of attempts:", attempts)
#     print("Do you want to play again? (yes/no)")
#     play_again = input()
#     if play_again.lower() != "yes":
#         print("Thank you for playing!")
#         break


# Same game but play again and again until user wants to quit. with Limited attempts

# while True:
#     number = random.randint(1, 10)
#     attempts = 0
#     max_attempts = 5
#     while attempts < max_attempts:
#         print("Enter your guess:")
#         guess = int(input())
#         attempts = attempts + 1
#         print( max_attempts - attempts,"Attempts left.")


#         if guess == number:
#             print(" You guessed it.")
#             break
#         elif guess < number:
#             print("Number is Higher. Try again.")
#         else:
#             print("Number is Lower. Try again.")

#     if attempts == max_attempts:
#         print("Sorry, you have used all your attempts. The number was:", number)

#     print("Do you want to play again? (yes/no)")
#     play_again = input()
#     if play_again.lower() != "yes":
#         print("Thank you for playing!")
#         break


#Question:
    # using ledger board
    # score of player vs the score of computer



# # Game of rock, paper, scissors
# options = ["rock", "paper", "scissors"]
# while True:
#     print("Enter your choice (rock/paper/scissors):")
#     user_choice = input().lower()
#     computer_choice = random.choice(options)
#     print("Computer chose:", computer_choice)

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win!")
#     else:
#         print("Computer wins!")
#     print("Do you want to play again? (yes/no)")
#     play_again = input()
#     if play_again.lower() != "yes":
#         print("Thank you for playing!")
#         break




games_data={"r","p","s"}
data= random.choice(games_data)
print(data)

while True:
        user_data=input("Enter your choice (r/p/s): ")
        if user_data not in games_data:
            print("Invalid choice.")
            continue
        print("Correct input.")
        if data==user_data:
            print("It's a Draw!")


            



        