name = input('Enter your name: ')
Lenname = len(name)
if(name.isspace() or (len(name)==0)):
        print('Sorry name cannot be blank')
else:
    if (Lenname < 3):
           print('Sorry name needs to be at least 3 characters')
    else:
        if name.isnumeric():
                print('Name must be alpabetic')

Accnum = input('Enter your account number: ')
Acclenght = len(Accnum)
if(Accnum.isspace() or (len(Accnum) == 0)):
                print('Sorry account number cannot be blank')
else:
    if Accnum.isalpha():
                    print('Account number must be numeric')
    else:
        if (Acclenght < 9) or (Acclenght >9):
                        print('Account number must be nine digits long')
                        
Payamnt = input('Enter Payment amount: ')
Paylenght = len(Payamnt)
if (Payamnt.isspace() or (len(Payamnt) == 0)):
                print('Payment cannot be blank')
else:
    amnt = float(Payamnt)
    if(amnt == 0) or (amnt < 0):
        if amnt == 0:
            print('Amount cannot be zero')
        else:
            print('Amount cannot be negative')
            
if (Lenname > 3) and (name.isalpha()): #Printing starts here 
    print('\n')
    print('Name: ',name,'Valid')
else:
    if (name.isspace() or (len(name)==0)):
        print('\n')
        print('Name: Name cannot be blank')
    else:
        if name.isnumeric():
                  print('\n')
                  print('Name: Name must be alphabetic')
        else:
            if (Lenname <= 3): 
                    print('\n')
                    print('Name: Name must be more than 3 characters')
if (Acclenght == 9) and Accnum.isnumeric():
        print('Account Number: ',Accnum,' Valid')
else:
    if (Accnum.isalpha()):
            print('Account Number: Account number must be numneric')
    else:
        if(Accnum.isspace() or (len(Accnum) == 0)):
                   print('Account Number: Account number cannot be blank')
        else:
           if (Acclenght < 9) or (Acclenght >9):
                        print('Account Number: Account number must be nine digits long')
if Payamnt.isspace() or len(Payamnt) == 0:
    print('Payment: Payment cannot be blank')
else:
    amnt = float(Payamnt)
    if amnt == 0:
        print('Payment: Payment cannot be zero')
    elif amnt < 0:
        print('Payment: Payment cannot be negative')
    else:
        if Paylenght > 0: 
            print('Payment: ', Payamnt, ' Valid')
