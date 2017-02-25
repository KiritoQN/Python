#!/usr/bin/python
def tinhlaixuat(t,n,k):
    return n + float(0.01*t*n)

if __name__=="__main__":
    while True:
        t = int(input("Nhap lai xuat (%): "))
        if (t > 0 and t < 100):
            break
        else:
            print("Ban nhap sai lai xuat!")
    while True:
        n = int(input("Nhap so tien gui (vnd): "))
        if (n > 0):
            break
        else:
            print("Ban nhap so tien gui!")
    while True:
        k = int(input("Nhap so thang gui: "))
        if (k > 0):
            break
        else:
            print("Ban nhap thang sai!")
    print "Tong tien: ", tinhlaixuat(t,n,k)
