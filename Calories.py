ans = 'y'
print('Calorie calculation')
while ans == 'y' or ans == 'Y':
    Calories = 4.9
    Minutes = 0
    Runtime = input('Enter your run time in minutes: ')
    if Runtime.isspace() or Runtime == '':
        print('cannot be blank')
    else:
        Runtime = float(Runtime)
        if Runtime < 5:
            print('Error: Minutes must be greater than 5')
        else:
            while Minutes < Runtime:
                Minutes += 5 
                if Minutes > Runtime:
                    Minutes = Runtime
                Burning = Calories * Minutes
                print('Minutes:', Minutes, 'burns', Burning, 'calories')
    ans = input('\nRun again? y/n -> ')
print('--Done--')
