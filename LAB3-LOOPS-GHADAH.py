# lab three - loops 
for i in range(45,210):
    if i==100:
        continue
    elif i==205:
        break 
    else:
        print(i)
    

from pickle import FALSE, TRUE

user_input=int(input("what is the product of 7 * 24 ?"))

while TRUE:

    if user_input==168:
         print ("You answered this Question correctly")
         break 
    else:
        print("Your Answer is wrong try again..")
        user_input=int(input("what is the product of 7 * 24 ?"))
