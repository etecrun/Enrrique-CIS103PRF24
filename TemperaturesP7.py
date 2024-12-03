def KilometersC():
    Miles = float(input('How many miles?')) 
    Kilometers = Miles * 1.609344
    print('Miles is: ',Kilometers, 'Kilometers')
    return Kilometers  
def  CelciusC():
    Farenheit = float(input('How many degrees?'))
    Celcius = (Farenheit - 32) * 5/9
    print('Farenheit is: ',Celcius, 'Celcius')
    return Celcius
def KilogramsC():
    pounds = float(input('How many pounds?'))
    Kilograms = pounds * 0.45359237
    print('Pounds is: ',Kilograms, 'Kilograms')
    return pounds
def  main():
    KilometersC()
    CelciusC()
    KilogramsC()
main() 


