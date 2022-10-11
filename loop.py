

for i in range(45, 210):
    if i != 100 :
        print (i)
        if i == 205 :
            break


num : int = 1
while num != 168:
    user_input = input("what is the product of 7 * 24 ?")
    if int(user_input) == 168 :
        print("You answered this Question correctly")
        num =168
    elif int(user_input) != 168 :
        print("Your Answer is wrong try again..")
    