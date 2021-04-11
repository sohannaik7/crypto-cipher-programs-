
def perform(text):
    line1 , line2, newtext = "","", ""
    for index in range(len(text)):
        if index % 2 == 0:
            line1 = line1+text[index]
        else:
            line2 = line2+text[index]

    newtext = line1+line2
    return newtext
        
if __name__ == '__main__':
    plain = input("give the plain input")   #provide the plain text 
    numoflevel = int(input("enter the number of levels you want to perform cipher")) # more the level more the strong
    cnt = 0
    temp = plain

    special_characters = "!@#$%^&*()-+?_=,<>/1234567890"
    # Example: $tackoverflow

    if any(c in special_characters for c in plain):
        print("special charater not allowed")
        exit()



    while cnt != numoflevel:
        temp = perform(temp)  
        cnt +=1
    print(temp)
    dicip = input("would u like to dycript it  Y or N??")
    if dicip == 'Y' or dicip == 'y':
        cnt = 0
        while cnt != numoflevel:
            temp = perform(temp)  
            cnt +=1
        print(temp)
    else:
        exit()
        
