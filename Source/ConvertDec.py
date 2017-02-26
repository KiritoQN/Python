def DecToBin(n):
    #print("DEC TO BIN")
    # Convert decimal to binary
    x = ""
    while n:
        temp = str(n%2)
        x = temp + x
        n=n/2
    return x
def DecToHex(n):
    #print("DEC TO HEX")
    # Convert decimal to hexa
    x = ""
    while n:
        temp = n%16
        if (temp < 10):
            hex = str(temp)
        else:
            if (temp == 10): hex = ("A")
            if (temp == 11): hex = ("B")
            if (temp == 12): hex = ("C")
            if (temp == 13): hex = ("D")
            if (temp == 14): hex = ("E")
            if (temp == 15): hex = ("F")
        x = hex + x
        n/=16
    return x
def Menu():
    print("CONVERT DEC TO (BIN OR HEX)")
    print("1. DecToBin")
    print("2. DecToHex")
    print("0. Exit")
    choose = int(input("Input choose: "))
    if(choose == 1):
        print("DEC TO BIN")
        n = int(input("Input dec: "))
        print DecToBin(n)
    else:
        if(choose == 2):
            print("DEC TO HEX")
            n = int(input("Input dec: "))
            print DecToHex(n)
        else:
            if(choose == 0):
                exit()
            else:
                print("ERROR! Please choose number (0->2)!")
                Menu()

if __name__ == '__main__':
    Menu()

