import math

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1


if __name__ == '__main__':
    m = 0
    key = []
    p = []
    for i in range(0,3):
        roww = [0]*3
        for j in range(0,3):
            roww[j]=(input("val"))
        key.append(roww)
    print(key)
    plaintetxt = str(input("enter the plain text"))
    locater = 0
    pointer = True
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    plaintetxt = Convert(plaintetxt)
    while pointer == True:
        for i in range(0,3):
            roww = [0]*3
            for j in range(0,3):
                a = plaintetxt[locater]
                roww[j]= alpha.index(a)
                locater +=1
            p.append(roww)
        pointer  = False
    print(p)
        



    