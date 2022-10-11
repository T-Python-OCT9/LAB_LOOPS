'''
This is the loop lab
'''

var1: int = 250

for x in range(45,210):
    if x == 100:
        continue
    print(x)
    if x == 205:
        break


user_input = input("What is the product of 7 * 24 ? ")

while user_input != "168":
    print("Your answer is wrong, Try again !")
    user_input = input("What is the product of 7 * 24 ? ")
    
    if user_input == "168":
        continue

else:
    print("You answered this question correctly !")
    

