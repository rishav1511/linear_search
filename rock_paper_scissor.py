import random
item_list = ["Rock","Paper","Scissors"]
user_choice = input("Enter your choice = ")
comp_choice = random.choice(item_list)
print(f"Your choice = {user_choice} and computer choice = {comp_choice} ")
if user_choice == comp_choice :
    print("Both the the choices are same. Hence match is TIED")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = COMPUTER WINS")
    else:
        print("Rock smashes Scissors = YOU WIN")
elif user_choice == "Paper":
    if comp_choice == "Scissors":
        print("Scissors cut paper = COMPUTER WINS ")
    else :
        print("Paper covers rock = YOU WIN")
elif user_choice == "Scissors":
    if comp_choice == "Rock":
        print("Rock smashes Scissors = COMPUTER WINS")
    else:
        print("Scissors cut paper = YOU WIN")