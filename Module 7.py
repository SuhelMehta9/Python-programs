#Module 7
country = False
country = input("Please enter your country: ").upper()
purchase = float(input("Please enter the total amount of shopping you did: "))
if country == "CANADA":
    country = True

if country:
    
    province = input('Please enter your province(If not in Alberta or Ontario then please enter "other": ').upper()
    if province == "ALBERTA":
        value = purchase*0.05 + purchase
        print('Tax here is 0.05 hence the total amount is {0:f}'.format(value))
    elif province == "ONTARIO":
        value1 = purchase*0.13 + purchase
        print('Tax here is 0.13 hence the total amount is {0:f}'.format(value1))
    
    elif province == "OTHER":
        value2 = purchase*0.06 + purchase*0.05 + purchase
        print('Tax here is 0.06 and 0.05 hence the total amount is {0:f}'.format(value2))

else:
    print('No tax. Your total amount is {0:f}'.format(purchase))

print('Have a nice day!')
        
