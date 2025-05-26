horas =input("Enter Hours: ")
rate =input("Enter Rate: ")
try :
    h = float(horas)
    r = float(rate)
except :
    h = -1
    r = -1
    print("ERROR, please enter Numeric Value: ")

if h <= 40 :
    pay = h*r
    print(pay)
elif h > 40 :
    bruto = 40*r
    r = r*1.5
    extra = h-40
    p = extra*r
    pay = p+bruto
    print(pay)