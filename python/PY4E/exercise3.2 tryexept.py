horas = input("Enter Hours: ")
rate = input("Enter Rate: ")
try :
    h = float(horas)
    r = float(rate)
except :
    h = -1
    r = -1
    if h > 0 :
        print("nice work")
    else:
        print("ERROR, please enter Numeric Value: ")        
if h <= 40 :
    pay = h*r
    print(pay)
elif h > 40 :
    bruto = 40*r
    rates = r*1.5
    extra = h-40
    p = extra*rates
    pay = p+bruto
    print(pay)