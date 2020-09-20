actnum = 18
total_guess = 9
guess = 0
print("You have total 9 Guess Availabe")
while guess < 9:
    guess = guess + 1
    usrin = int(input("Plz Enter Your Guessed Number : \n"))
    if usrin < actnum:
        print("Your Guessed Number is lower.")
    elif usrin > actnum:
        print("Your Guessed Number is higher.")
    else:
        print("Congrats, You Guessed Right.")
        print("You Guessed It in ", guess, " Chances")
        break
    print("No. of guess left : ", total_guess - guess)
    if guess == 9:
        print("Game Over")
"""
# Exercise 3 Printing Start Pattern In Python
"""
no_of_star = int(input("Please Enter The nUmber : \n"))
bol = int(input("Please Enter 1 OR 0 : \n"))
for i in range(no_of_star):
    i = i + 1
    if bol == 1:
        print(i * "*")
    elif bol == 0:
        pno_of_star = no_of_star + 1
        print((pno_of_star - i) * "*")
    else:
        print("Invailid Input")
