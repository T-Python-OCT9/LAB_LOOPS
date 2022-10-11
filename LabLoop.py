for num in range(45, 210):
    
    if num == 100:
        continue
    print("the elements", num)
    if num == 205:
        break


result = input("What is the product of 7*24")
while int(result)  == 7*24:
    print("You answered this Question correctly")

    break
else :
    print("Your Answer is wrong try again..")
    result = input("What is the product of 7*24")  



'''while True:
    result = int(input("What is the product of 7*24"))
    if result == 7*24:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")'''