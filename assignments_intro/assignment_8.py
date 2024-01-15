loanAmount = 100000
monthlyInterestRate = 0.01
noyears = 7
monthlypayment = (loanAmount*monthlyInterestRate)/(1-1/(1+monthlyInterestRate)**(noyears*12))
totalpayment = monthlypayment*noyears*12
print(monthlypayment)
print(totalpayment)
