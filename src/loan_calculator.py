from pyloan import pyloan

# a pip module that calculate loan details
def loan_summary(Price,Interest_rate,Term,Date):
    loan = pyloan.Loan(loan_amount=Price,interest_rate=Interest_rate,loan_term=Term,start_date=Date)
    
    return loan.get_loan_summary()

