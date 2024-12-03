screwprice =  .99
pounds = float(input('How many pounds of screws would you like to purchase? '))
Gsales = pounds * screwprice
Discount = 0
if(pounds >= 10) and (pounds <= 99.99):
    Discount = Gsales * .10
    Famount = Gsales - Discount
    print('Number of pounds: ', pounds)
    print('Gross sales: ', Gsales)
    print('Discount: ', Discount)
    print('Final amount: ', Famount)
elif(pounds >= 100) and (pounds <= 999.99):
        Discount = Gsales * .20
        Famount = Gsales - Discount
        print('Number of pounds: ', pounds)
        print('Gross sales: ', Gsales)
        print('Discount: ', Discount)
        print('Final amount: ', Famount)
elif(pounds >= 1000) and (pounds <= 9999.99):
        Discount = Gsales * .30
        Famount = Gsales - Discount
        print('Number of pounds: ', pounds)
        print('Gross sales: ', Gsales)
        print('Discount: ', Discount)
        print('Final amount: ', Famount)
elif(pounds >= 10000):
    Discount = Gsales * .40
    Famount = Gsales - Discount
    print('Number of pounds: ', pounds)
    print('Gross sales: ', Gsales)
    print('Discount: ', Discount)
    print('Final amount: ', Famount)
else:
        print('Number of pounds: ', pounds)
        print('Gross sales: ', Gsales)
        print('Discount: Haha you get nothing buy some more will ya?')
        print('Final amount: ', Gsales)
