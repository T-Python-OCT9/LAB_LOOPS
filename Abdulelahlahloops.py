for i in range (45,210):
    if i == 100:
        continue 
    if i == 205:
        break
    print(i)

user_input = input("what is the product of 7 * 24 ?")
while user_input != "168":
    print("You answered this Question correctly")
    user_input = input("what is the product of 7 * 24 ?") 
    if user_input == "168":
        continue
    else:
        print("You answered this Question correctly")