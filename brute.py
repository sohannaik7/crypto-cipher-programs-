if __name__ == '__main__':
    text = input("enter the test")
    result=""
    res2=""
    num = 0

    while num <= 26:
        for i in text:
            if 65 <= ord(i) <= 90:
                con = (ord(i) + 1)
                if con > 90:
                    con = con - 26
                result += chr(con)
            elif 48 <= ord(i) <= 57:
                con = (ord(i) + 1)
                if con > 57:
                    con = con - 10
                result += chr(con)
            elif 97 <= ord(i) <= 122:
                con = (ord(i) + 1)
                if con > 122:
                    con = con - 26
                result += chr(con)
        num+=1
        print("key at",num,":",result,"\n")
        text = ""
        text = result
        result = ""