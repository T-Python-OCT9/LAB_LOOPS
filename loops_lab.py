
# solve the first part of the qustion
for numbers in range(45, 210):

    if numbers == 100:
        continue
    elif numbers == 205:
        break
    print(numbers)

# solve the second part of the qustion
x : bool = False
while x == False:
    user_input = input("what is the product of 7 * 24 ? ")
    int(user_input)
    if user_input == 168:
        print("You answered this Question correctly")
        break 
    else:
        print("Your Answer is wrong try again..")
    






