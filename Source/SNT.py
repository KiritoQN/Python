def SNT(n):
    if(n<2): return 0
    if(n==2): return 1
    l = range(n)
    for i in l[2:]:
        if(n%i==0): return 0
        else: return 1

if __name__ == "__main__":
    n = int(raw_input("Input number: "))
    if (SNT(n)==1):
        print n,"la so nguyen to!"
    else:
        print n,"khong la so nguyen to!"
