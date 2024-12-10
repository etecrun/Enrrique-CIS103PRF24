def main():  
    Numerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX', 21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV'}
    print("Roman Numeral Dictionary:")
    print(Numerals)
    ans = 'y'
    while ans == 'y':
        TheInput = input('What number would you like to display as a Roman numeral? ')
        try:
            Num = int(TheInput)  
        except ValueError:
            print("Input must be a valid integer. Please try again.")
        else:
            if Num <= 0:
                print("--done--")
                ans = 'n'
            elif Num not in Numerals:  
                print("Number", Num, "not found in the dictionary.")
                AddEntry = input("Would you like to add " + str(Num) + " to the dictionary? (y/n): ")
                if AddEntry == 'y':
                    RomanNumeral = input("Enter the Roman numeral for " + str(Num) + ": ")
                    if RomanNumeral.isalpha():
                        Numerals[Num] = RomanNumeral
                        print("Adding", Num, ":", RomanNumeral, "to the dictionary.")
                    else:
                        print("Roman numeral must be alphabetic. Entry not added.")
                else:
                    print("Number not added to the dictionary.")
            else:
                print("The Roman numeral for", Num, "is", Numerals[Num] + ".")
        ans = input("Would you like to input another number? (y/n): ")
        if ans != 'y':
            print("--done--")
    print("\nFinal Roman Numeral Dictionary:")
    print(Numerals)
main()
