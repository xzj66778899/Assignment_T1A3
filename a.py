from mortgage import Loan






def get_loan_information(principle,interest,term):
    loan = Loan(principle,interest,term)
    detail=loan.summarize
    


print(get_loan_information(300000,0.06,30))
