print("Welcome to computer quiz")
ans=input("Do you want to play yes/no ")
if ans != "yes":
    quit()
print("okay lets play")
score=0
answer=input("What is the full form of CPU? ")
if answer == "central processing unit":
    print("correct")
    score+=5
else:
    print("Incorrect")
answer=input("What is the full form of GPU? ")
if answer == "graphics processing unit":
    print("correct")
    score+=5
else:
    print("incorrect")
answer=input("What is FTP? ")
if answer == "file transfer protocol":
    print("correct")
    score+=5
else:
    print("incorrect")
print("Your final score is ",score)
 
