def KilometersC(): 
    try:
        Miles = input('How many miles? ')
        if Miles == '':
            print("Input cannot be blank. Please enter a valid number.")
            return KilometersC()  
        Miles = float(Miles)
        Kilometers = Miles * 1.609344
        print('Miles is: ', Kilometers, 'Kilometers')
        return Kilometers
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return KilometersC()  
def CelciusC():
    try:
        Farenheit = input('How many degrees? ')
        if Farenheit == '':
            print("Input cannot be blank. Please enter a valid number.")
            return CelciusC()
        Farenheit = float(Farenheit)
        Celcius = (Farenheit - 32) * 5/9
        print('Farenheit is: ', Celcius, 'Celcius')
        return Celcius
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return CelciusC()
    except:
        print('General error')
def KilogramsC():
    try:
        pounds = input('How many pounds? ')
        if pounds == '':
            print("Input cannot be blank. Please enter a valid number.")
            return KilogramsC()  
        pounds = float(pounds)
        Kilograms = pounds * 0.45359237
        print('Pounds is: ', Kilograms, 'Kilograms')
        return pounds
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return KilogramsC()  
def main():
    ans = 'y'
    while ans == 'y':
        KilometersC()
        CelciusC()
        KilogramsC()
        ans = input('Run again? y/n: ')
        if ans != 'y':
            print("---DONE---")        

main()
