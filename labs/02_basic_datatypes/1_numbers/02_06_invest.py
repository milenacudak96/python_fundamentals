'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
i_amount = float(input('Provide investment amount: '))
interest_rate = float(input('Provide interest rate in percentage: '))
years = float(input('Provide number of years to invest: '))
futureInvestmentValue = i_amount * (1 + interest_rate/100) ** years
print('Feature value is: ' + str(futureInvestmentValue))
