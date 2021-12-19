import random

def multiplication(num1, num2):
    guess = int(input(f"{num1} x {num2} = "))
    answer = num1*num2

    if (guess == answer):
        print("Your answer is correct!")
        return True
    else:
        print("You did not get the answer correct!")
        return False

def addition(num1, num2):
    guess = int(input(f"{num1} + {num2} = "))
    answer = num1+num2

    if (guess == answer):
        print("Your answer is correct!")
        return True
    else:
        print("You did not get the answer correct!")
        return False

def subtraction(num1, num2):
    guess = int(input(f"{num1} - {num2} = "))
    answer = num1-num2

    if (guess == answer):
        print("Your answer is correct!")
        return True
    else:
        print("You did not get the answer correct!")
        return False

def app(score): 
    print(f"Your score is {score}")
    numberone = random.randint(2, 12)
    numbertwo = random.randint(2, 12)

    randomsign = random.randint(1, 3)

    if (randomsign == 1):
        if (multiplication(numberone, numbertwo)):
            score = score + 1
            app(score)
    elif (randomsign == 2):
        if (addition(numberone, numbertwo)):
            score = score + 1
            app(score)
    elif (randomsign == 3):
        if (subtraction(numberone, numbertwo)):
            score = score + 1
            app(score)
    

if __name__ == "__main__":
    app(0)