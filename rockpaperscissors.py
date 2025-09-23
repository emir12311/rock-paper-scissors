import random

randomnum = random.randint(1, 3)

if randomnum == 1:
    computerguess = "Rock"
elif randomnum == 2:
    computerguess = "Paper"
else:
    computerguess = "Scissors"

r = "Rock"
p = "Paper"
s = "Scissors"
w = "You Win!"
l = "You Lost"

humanguess = input("Rock, Paper or Scissors? ").capitalize()

print(f"computers guess was {computerguess}")

#this isnt optimized at all.
if humanguess == computerguess:
    print("its a tie")
elif humanguess == r and computerguess == p:
    print(l)
elif humanguess == r and computerguess == s:
    print(w)
elif humanguess == p and computerguess == s:
    print(l)
elif humanguess == p and computerguess == r:
    print(w)
elif humanguess == s and computerguess == r:
    print(l)
elif humanguess == s and computerguess == p:
    print(w)
else:
    print("error")

