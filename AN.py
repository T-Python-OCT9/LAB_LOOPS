for item in range(45, 210):
    print(item)
    if item == 205:
        break
    
product: str = ""
while not product == 168:
    if product == "":
        product = int(input("What is the product of 7 * 24 ? "))
    else:
        print("Your Answer is wrong try again..")
        product = int(input("What is the product of 7 * 24 ? "))
else:
    print("You answered this Question correctly.")



