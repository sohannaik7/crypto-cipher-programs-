if __name__ == '__main__':
    text = input("enter the testx")
    key = int(input("enter the key"))
    result=""
    res2=""
    for i in text:
        if 65 <= ord(i) <= 90:
            con = (ord(i)+key)
            if con > 90:
                con = con - 26
            result+=chr(con)
        elif 48 <= ord(i) <= 57:
            con = (ord(i) + key)
            if con > 57:
                con = con - 10
            result+=chr(con)
        elif 97 <= ord(i) <= 122:
            con = (ord(i) + key)
            if con > 122:
                con = con - 26
            result+=chr(con)
    print(result)
    print("===========dicrypt=========")

    for i in result:
        if 65 <= ord(i) <= 90:
            con = (ord(i)-key)
            if con < 65:
                con = con + 26
            res2+=chr(con)
        elif 48 <= ord(i) <= 57:
            con = (ord(i) - key)
            if con < 48:
                con = con + 10
            res2+=chr(con)
        elif 97 <= ord(i) <= 122:
            con = (ord(i) - key)
            if con < 97 :
                con = con + 26
            res2+=chr(con)
    print(res2)