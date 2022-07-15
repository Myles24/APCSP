import random
from tkinter import *
import tkinter
from tkinter import ttk
 
password = ""
char_list = ["!", ".", "`", "~", "[", "1", "2", "3", "4", "a", "b", "c", "A", "H", "Y"] # list that stores characters that will be used in the password
rand = open("random.txt", "w") # a text file "random.txt" is opened with the variable "rand"
pw_list = []
length = 8
special_characters_list = ["!", ".", "`", "~", "[", "*", "$", "@"]
low_letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
high_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
 
# these 4 functions below add characters to the character list
def special_characters():
    char_list.extend(special_characters_list)
def low_letters():
        char_list.extend(low_letters_list)
def high_letters():
        char_list.extend(high_letters_list)
def numbers2():
        char_list.extend(numbers_list)
 
# this function below asks the user to provide input on which characters they want in their password and executes the respective function(s)
def char_choice():
    global window2
    global char_list
    char_list = []
    window2 = Tk()
    window2.title("Character Choice")
    window2.configure(width=500, height=300)
    label1=Label(window2, text="Click on the characters that you want in the password. \n Multiple clicks on a button set the priority higher.", font=('Calibri 9')).pack(side = "top")
    special_chars = Button(window2, text = 'Special Characters', bd = '5', command = special_characters).pack(side = 'bottom')
    numbers = Button(window2, text = 'Numbers', bd = '5', command = numbers2).pack(side = 'bottom')
    low_letters2 = Button(window2, text = 'Lowercase Letters', bd = '5', command = low_letters).pack(side = 'bottom')
    high_letters2 = Button(window2, text = 'Uppercase Letters', bd = '5', command = high_letters).pack(side = 'bottom')
    done = Button(window2, text = 'Done', bd = '5', command = window2.destroy).pack(side = "right")
    window2.mainloop()
 
 
def GUI(): # main (1st) tkinter window of the GUI
   
    def length(): # this function allows the user to specify the length of the password
        window3 = Tk()
        window3.title("Length")
        label2=Label(window3, text="Enter the # of characters in password", font=('Calibri 9')).pack(side = "left")
        entry = tkinter.Entry(window3)
        entry.pack(side = "left")
        def get_value(): # this function retrieves the integer value using the .get() method
            global length
            length = int(entry.get()) # converts the entry to an integer and assigns it the variable length
            window3.destroy()
        done2 = Button(window3, text = 'Done', bd = '5', command = get_value).pack(side = "right")
        window3.mainloop()
       
    global window
    window = Tk()
    window.title("Password Generator")
    window.configure(width=500, height=300)
    label5=Label(window, text="Default length is 8 with numbers & special characters", font=('Calibri 9')).pack(side = "top")
    length_button = Button(window, text = 'Define length of password', bd = '5', command = length).pack(side = "left")
    character_choice = Button(window, text = 'Choose characters', bd = '5', command = char_choice).pack(side = "right")
    generate = Button(window, text = 'Generate!', bd = '5',
            command=lambda : create_password(password, pw_list, window)).pack(side = "bottom")
    window.mainloop()
 
def create_password(pw, lis, win): # this function creates the password from the characters generated in the text file
    lis = []
    h = 0
    while h < 1000:
        for element in char_list:
            rand.write(str(element) + "\n") # iterates 1000 times appending items in char_list to a respective line in random.txt
        h = h + 1
    i = 0
    while i < length: # iterates the number of times specified by t (length of password)
        lis.append(random.choice(open('random.txt', "r").readlines())) # appends random lines from random.txt to the pw_list. The number of lines depends on the length specified.
        i = i + 1
    lis = list(map(lambda elem: elem.replace("\n", ''), lis)) # for each item in the pw_list, this procedure will remove "/n" from that item - https://stackoverflow.com/questions/71023711/how-to-store-string-with-tabs-in-a-list-in-python
    pw = "".join(lis) # joins all items in the pw_list
    print(pw)
    label1=Label(win, text=pw, font=('Calibri 15')).pack(side = "top")
 
    # PASSWORD CHECKER
    security = 0
    if any(item in lis for item in special_characters_list):
        security = security + 1
    if any(item in lis for item in low_letters_list):
        security = security + 1
    if any(item in lis for item in high_letters_list):
        security = security + 1
    if any(item in lis for item in numbers_list):
        security = security + 1
    if len(lis) > 7:
        security = security + 1
    
    else:
        if len(lis) < 7 and len(lis) >= 5 and security >= 3:
            label5=Label(win, text="Password security is good, but consider making it at least 8 characters long", 
                                    font=('Calibri 10')).pack(side = "bottom")
        else: 
            label5=Label(win, text="Password should be longer for added security", 
                                        font=('Calibri 10')).pack(side = "bottom")
    if security >= 4:
        label5=Label(win, text="Password is secure; meets the length and character requirements", 
                                        font=('Calibri 10')).pack(side = "bottom")
    else:
        label5=Label(win, text="Consider adding more different characters for increased security.", 
                                        font=('Calibri 10')).pack(side = "bottom")
 
 
GUI()
 
 
 
 
 
 
