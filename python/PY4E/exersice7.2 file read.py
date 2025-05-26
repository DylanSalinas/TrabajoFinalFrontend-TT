fname = input("Enter file name: ")
count = 0
variable = 0
try: 
    fh = open(fname)
    fhr = fh.readlines()    
    for line in fhr:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        elif line.startswith("X-DSPAM-Confidence:"):
            count += 1
            ls = line.rstrip()           
            number = line.find(":")
            n = number+1
            final = line[n:]
            flotada = float(final.strip(" "))
            variable = variable + flotada
    laverage = variable / count
    print("Average spam confidence: ",laverage)
except:
    print("file cant be open")
    quit()