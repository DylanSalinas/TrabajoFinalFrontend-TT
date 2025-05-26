horas =input("Enter Hours: ")
h = float(horas)
rate =input("Enter Rate: ")
r = float(rate)
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
