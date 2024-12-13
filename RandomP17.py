import random

def generateNumbers(highestNumber, numToGenerate):
    numbers = []
    while len(numbers) < numToGenerate:
        num = random.randint(1, highestNumber)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()  
    return numbers
def powerball():
    highestNumber = 69
    numToGenerate = 5
    numbers = generateNumbers(highestNumber, numToGenerate)
    print("Powerball: ")
    for number in numbers:
        print(number)
    print()
def megaMillion():
    highestNumber = 70
    numToGenerate = 5
    numbers = generateNumbers(highestNumber, numToGenerate)
    print("Mega Million: ")
    for number in numbers:
        print(number)
    print()
def luckyDayLotto():
    highestNumber = 45
    numToGenerate = 5
    numbers = generateNumbers(highestNumber, numToGenerate)
    print("Lucky Day Lotto: ")
    for number in numbers:
        print(number)
    print()
def lotto():
    highestNumber = 52
    numToGenerate = 6
    numbers = generateNumbers(highestNumber, numToGenerate)
    print("Lotto: ")
    for number in numbers:
        print(number)
    print()
def displayMenu():
    print("\n1. Powerball")
    print("2. Mega Million")
    print("3. Lucky Day Lotto")
    print("4. Lotto")
    print("5. Quit")
def main():
    continueProgram = "y"  
    while continueProgram == "y":
        displayMenu()
        choice = input("Please select a game (1-5): ")
        if choice == '1':
            powerball()
        elif choice == '2':
            megaMillion()
        elif choice == '3':
            luckyDayLotto()
        elif choice == '4':
            lotto()
        elif choice == '5':
            print("Exiting the program.")
            continueProgram = "n"  
        else:
            print("Invalid selection, please choose a number between 1 and 5.")

        if continueProgram != "n":  
            continueProgram = input("Run again? (y/n): ")
main()
