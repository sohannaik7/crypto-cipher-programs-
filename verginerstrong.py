def checking(a):
    if a.isdigit():
        print("cannot enter the number in the text")
        return True
    else:
        return False
        

import math
if __name__ == '__main__':
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(len(alpha))
    plain = input("enter the plain text")
    key = input("enter the key")
    k = [1]*len(plain)
    decri = []*len(plain)
    cnt = 0
    incri = 0
    furthercount = 0
    special_characters = "!@#$%^&*()-+?_=,<>/"

    if any(c in special_characters for c in plain):
        print("special charater not allowed")
        exit()

    for i in range(len(plain)):
        if checking(plain[i])==True:
            break
        if len(k)>len(plain):
            break
        if cnt < len(key):
            k[incri] = key[cnt]
            incri+=1
            cnt +=1

        if cnt >= len(key) and cnt <=len(plain):
            m = len(plain)-len(key)
            if furthercount >= m:
                break
            k[incri] = plain[furthercount]
            incri+=1
            cnt +=1
            furthercount +=1

    for i in range(len(plain)):
        
        if checking(plain[i])==True:
            break

        a = k[i]
        b = plain[i]
        sum = alpha.index(a)+alpha.index(b) # summing two table one by one and storing it in another 
        val= alpha[int(sum%26)]    # takinf vakue from alpha of respective index letter
        decri.append(val)
    print(k)
    print(plain)
    print(decri)
