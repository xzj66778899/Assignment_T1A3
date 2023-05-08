from mortgage import Loan
import math

# a pip module that calculate loan details
def get_loan_information(principle,interest_rate,term,):
    loan = Loan(principle,interest_rate,term)
    loan.summarize
    
get_loan_information(10000,.07,5)




# a function calculate the monthly payment
def monthly_payment_calculate(p,i,t):
     return round(p*(i/12)*math.pow(1+(i/12),t*12)/(math.pow(1+(i/12),t*12)-1))


print(monthly_payment_calculate(10000,.07,5))

