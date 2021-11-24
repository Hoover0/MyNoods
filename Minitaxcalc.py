#Asks for the income made for the year
income = float(input('Enter the annual income: '))
tax = 0.0

#If income is not greater than 85,528.0 then tax is equal to %18 of income minus 556.2
if income <= 85528.0:
    tax = float(round((income*.18)-556.02))
    if tax < 0:
        tax = 0
    print('The tax is:', tax, 'thalers')

#If income is greater than 85,528.0 then tax is equal to %32 of the surplus income plus 14,839
if income > 85528.0:
    tax = float(round((income-85528.0)*.32 + 14839.02))
    if tax < 0:
        tax = 0
    print('The tax is:', tax, 'thalers')