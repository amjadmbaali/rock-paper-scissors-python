import random

print("Welcome to Rock, Paper, Scissors!")

total_user_wins = 0
total_comp_wins = 0

while True:
    rounds = 0
    print("\nStarting 3 rounds...")

    while rounds < 3:
        print("\nChoose your move:")
        print("1) Rock")
        print("2) Paper")
        print("3) Scissors")
        print("4) Exit")
        user = input("Enter your choice (1-4): ")

        if user == "4":
            print("Goodbye!")
            exit()

        if user == "1":
            user1 = "rock"
        elif user == "2":
            user1 = "paper"
        elif user == "3":
            user1 = "scissors"
        else:
            print("Invalid choice, try again.")
            continue

        comp = random.randint(1, 3)
        if comp == 1:
            comp1 = "rock"
        elif comp == 2:
            comp1 = "paper"
        else:
            comp1 = "scissors"

        print("\nYou chose: %s" % user1)
        print("Computer chose: %s" % comp1)

        if user1 == comp1:
            print("Result: It's a tie!")
        elif user1 == "rock" and comp1 == "scissors":
            print("Result: You win!")
            total_user_wins += 1
        elif user1 == "paper" and comp1 == "rock":
            print("Result: You win!")
            total_user_wins += 1
        elif user1 == "scissors" and comp1 == "paper":
            print("Result: You win!")
            total_user_wins += 1
        else:
            print("Result: Computer wins!")
            total_comp_wins += 1

        rounds += 1

    print("\n==== TOTAL RESULT ====")
    print("Your total wins: %d" % total_user_wins)
    print("Computer total wins: %d" % total_comp_wins)

    print("\nWhat do you want to do?")
    print("1) Continue and keep the total score")
    print("2) Delete total score and start from zero")
    print("3) Exit game")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "2":
        total_user_wins = 0
        total_comp_wins = 0
        print("Score deleted! Starting from zero.")
    elif choice == "3":
        print("Goodbye!")
        break
