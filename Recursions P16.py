def Number(n):
    print(' ', n, end='')
    if n <= 0: 
        return n
    else:
        return n + Number(n-1)
def main():
    ans = 'y'
    while ans == 'y':
        try:
            numb = int(input('enter a number -> '))
            if numb < 0:  
                print('Error: Negative number entered')
            else:
                Sum = Number(numb)
                print(' Total sum is:  ', Sum)
                print('--------------')
        except ValueError:
            print('Invalid input. Please enter a valid number.')      
        ans = input(' Run again? y/n: ')
        print('--Done--')
main()
