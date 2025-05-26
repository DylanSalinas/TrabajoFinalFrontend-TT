fh = open("mbox-short.txt")
fhr = fh.readlines()
print(fhr)
#for line in fhr:
#        if not line.startswith("X-DSPAM-Confidence:"):
#               ly = line.rstrip()
#               print(ly)
#               fhr.close()