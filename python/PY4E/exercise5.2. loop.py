largest = None
smallest = None
while True: 
    num = input("Enter a number: ")
    if num == "done" :
            break
    try :
        num = int(num)
        for n in [num]: 
            if largest is None or n > largest :
                largest = n
        for n in [num]: 
            if smallest is None or n < smallest :
                smallest = n
    except : 
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)