birthday_list = []

birthday = input("What is your birthday? ")
birthday_list.append(birthday)
x = 0

while x <= 3:
    birthday = input("What is your birthday? ")
    birthday_list.append(birthday)
    x = x + 1
    for i in birthday_list:
        for f in birthday_list:
            if i == f:
                print("beaners")
 

