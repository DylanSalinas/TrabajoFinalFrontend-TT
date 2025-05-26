def computepay(h, r):
    if h <= 40 :
    	pay = h*r
    elif h > 40 :
        bruto = 40*r
        r = r*1.5
        extra = h-40 
        p = extra*r
        pay = p+bruto
    return pay
hrs = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
p = computepay(hrs, r)
print("Pay", p)