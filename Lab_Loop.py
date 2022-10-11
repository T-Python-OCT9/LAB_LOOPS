# LAB_LOOPS

## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
for x in range(45, 210):
    if x == 100 :
        continue
    print("Elements : ", x)
    if x == 205 :
        break


## 2) Using a while loop and input , do the following :
#Ask the the user : "what is the product of 7 * 24 ?"
user_input :int = int(input("what is the product of 7 * 24 ?"))
#check if the answer is right then exit the loop and print "You answered this Question correctly"
while user_input != 168 :
    print("Your Answer is wrong try again.." )
    user_input :int = int(input("what is the product of 7 * 24 ?"))
    continue
# if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
else:
        print("You answered this Question correctly")
    


# Another Answer 
print("This is the Second Code")
while True:
    _user_input :int = int(input("what is the product of 7 * 24 ?"))
    if _user_input == 7*24:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")


