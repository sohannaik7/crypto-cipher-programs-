def checking(a):
    if a.isdigit():
        print("cannot enter the number in the text")
        return True
    else:
        return False

import math


if __name__ == '__main__':
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plain = input("enter the plain text")
    key = input("enter the key")
    k = [1]*len(plain)              #rather give emplty val 
    decri = []*len(plain)
    cnt = 0
    incri = 0

    special_characters = "!@#$%^&*()-+?_=,<>/"
    # Example: $tackoverflow

    if any(c in special_characters for c in plain):
        print("special charater not allowed")
        exit()

    for i in range(len(plain)):
        if checking(plain[i])==True:                #checking for number in char
            break
        if len(k)>len(plain):           # the program must terminat if it is more then the lenth of plain text
            break
        if cnt == len(key):         #after key is added in new K, the key must start again from first and go so on--> sohan sohan sohan 

            cnt = 0
        k[incri] = key[cnt]     #get the value of key to K repeatedly
        incri+=1
        cnt +=1
    for i in range(len(plain)):
        if checking(plain[i])==True:
            break               # cheching if the char is number
        a = k[i]
        b = plain[i]
        sum = alpha.index(a)+alpha.index(b) # summing two table one by one and storing it in another 
        val= alpha[int(sum%26)]    # takinf vakue from alpha of respective index letter
        decri.append(val)
    print(k)
    print(plain)
    print(decri)

