def UCLN1(a,b):
    if(a < 0): a = -a
    if(b < 0): b = -b
    while(a & b):
        if(a >= b): b=a%b
        else: a = b%a
    return (a+b)
def UCLN(a, b):
    if (a == 0 and b == 0):
        return -1
    else:
        if (b == 0):
               return a
        else:
              return UCLN(b, a % b)

def BCNN(a, b):
    if (a == 0 and b == 0):
        return -1
    else:
        return (a * b / UCLN(a, b))

