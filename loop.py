
#problem 1
for i in range(45,210):
    if i == 100:
        continue
    elif i == 205:
        break
    print(i)


#problem 2
answer :int = 168

while answer == 168 or answer != 168: 
    user_input = input("what is the product of 7 * 24 ? ")
    if user_input == "168":
     print("You answered this Question correctly")
     break
    else:    
     print("Your Answer is wrong try again..")