__author__ = 'jc446932'
def tax_return(income):
    if income <= 16000:
         return 0



    else:
         return(income-16000)*.3

print(tax_return(1700))



