def checking(a):
    if a.isdigit():
        print("cannot enter the number in the text")
        return True
    else:
        return False

if __name__ == '__main__':
    text = input("enter the palinm text")
   
    key = int(input("enter the key"))
    data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]
    memo,dememo = [],[]
    data2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
    k,m = 0,0


    special_characters = "!@#$%^&*()-+?_=,<>/"
    # Example: $tackoverflow

    if any(c in special_characters for c in text):
        print("special charater not allowed")
        exit()
        
    for i in text:
        for j in range(len(data)):
            if (i == data[j]):
                m = (j + key) % 26
                memo.append(m)
                break
            if (i == data2[j]):
                m =  (j+key)%26
                memo.append(m)
                break
            
    for mm in range(len(memo)):
        print(data[memo[mm]])
    print("..............decrypt..............")
    for mm in memo:
        m = (mm - key) % 26
        dememo.append(m)
        print(data[m])