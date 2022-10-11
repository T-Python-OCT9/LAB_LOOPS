
for i in range(45,210):
    if i == 100:
        continue
    elif i == 205:
        break
    print(i)

x = 1
while x == 1:
    total = int(input("what is the product of 7 * 24 ?"))
    
    if total == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")