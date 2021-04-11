import random as ran

def checking(a):
    if a.isdigit():
        print("Cannot enter the number in the text")
        return True
    else:
        return False


def checking(a):
    if a.isdigit():
        print("cannot enter the number in the text")
        return True
    else:
        return False

if __name__ == '__main__':
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    plain = input("enter the plain text")
    decri = []
    print(len(plain))
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(c in special_characters for c in plain):
        print("special charater not allowed")
        exit()

    key, cnt = [], 0
    while cnt !=len(plain):
        r = ran.randint(0,24)
        key.append(alpha[r])
        cnt +=1
    print(plain)
    print(key)
    for i in range(len(plain)):
        if checking(plain[i])==True:
            break               # cheching if the char is number
        a = key[i]
        b = plain[i]
        sum = alpha.index(a)+alpha.index(b) # summing two table one by one and storing it in another 
        val= alpha[int(sum%26)]    # takinf vakue from alpha of respective index letter
        decri.append(val)
    print(decri)

        
