import random

def notEqual(a,b):
  return a == b

# Main Program
n = random.randint (1,100)

def guess(count = 1):
    
    choice = int(input("Enter a number (1 to 100): "))

    if choice < n:
      print("Too low!")
      return guess(count + 1)
    elif choice > n:
      print("Too high!")
      return guess(count + 1)
    else:
      print("You are correct!")
      print("You guessed correctly in " + str(count) + " attempts.")
      return 0

guess()
