#Convert Fº to Cº

def convert(s):
    f = float(s)
    c= (f - 32) * 5/9
    return c
    
s = int(input("Temperatura  : "))

print(convert(s))