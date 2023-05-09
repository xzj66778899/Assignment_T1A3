from pyloan import pyloan
import math,datetime


now=datetime.datetime.now()
s = now.strftime('20%y-%m-%d')

# a pip module that calculate loan details
def loan_summary(Price,Interest_rate,Term,Date):
    loan = pyloan.Loan(loan_amount=Price,interest_rate=Interest_rate,loan_term=Term,start_date=Date)
    
    return loan.get_loan_summary()



# # a function calculate the monthly payment
# def monthly_payment_calculate(p,i,t):
#      return round(p*(i/12)*math.pow(1+(i/12),t*12)/(math.pow(1+(i/12),t*12)-1))


with open('purchase_order.txt','w') as f:
    print(loan_summary(70000,7,5,s),file=f)

f.close()




offer_date=loan_summary(70000,7,5,s)[0]
payment_amount=loan_summary(70000,7,5,s)[1]
interest_amount=



# f.close()


