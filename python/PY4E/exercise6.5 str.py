text = "X-DSPAM-Confidence:    0.8475"
number = text.find(":")
n = number+1
final = text[n:]
flotada = float(final.strip(" "))
print(flotada)