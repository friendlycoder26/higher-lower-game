from utilites.logo import photo
from utilites.dictonaries import data
print(photo)
import random
import os

def format_data(account):
    account_name = account["name"]
    account_descr = account['description']

    return f"{account_name},{account_descr}"
   

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game_should_continue = True

# Start with two different accounts
account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

while game_should_continue:

    print(f"Compare A: {format_data(account_a)}\n")
    print("V E R S U S\n")
    print(f"Compare B: {format_data(account_b)}\n")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls' if os.name == 'nt' else 'clear')

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")

        # Correct logic:
        # If the user chose B correctly → B becomes new A
        if guess == "b":
            account_a = account_b  # promote B to A

        # New B
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
