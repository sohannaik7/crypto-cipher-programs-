import random
import pyautogui

chr = "JNU1OO1TR"
chr_list = list(chr)

password = pyautogui.passowrd("enter the password") 

guess_pass = ""


while(guess_pass != password):
    guess_pass = random.choices(chr_list, k=len(password))
    print(".................."+str(guess_pass)+"..............")
    if(guess_pass == list(password)):

        print("yue pass code","".join(guess_pass))
        break