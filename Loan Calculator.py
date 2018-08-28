#This program is to calculate the number of payments you have to give each month for you to be loan free!
# M = monthly payement
# L = Loan amount
#i = intrest rate(for an intrest of 5%, i = 0.05)

L = input('Enter the loan amount: ')

i = input('Enter intrest rate: ')

n = input('Enter number of years: ')
numberOfmonths = float(n)*12
LoanAmount = float(L)
IntrestRate = float(i)
M = LoanAmount*(IntrestRate*(1+IntrestRate)*numberOfmonths)/((1+IntrestRate)*numberOfmonths - 1)
print('You must give INR {0:.2f} every month'.format(float(M)))
