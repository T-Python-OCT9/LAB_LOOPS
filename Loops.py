from cgi import print_arguments


#num : int = 210

for num in range(45,210) :
    if num == 100 :
        continue
    if num == 205:
        break

    print(num)

#answer : int = 168
user_input : str = ""

while not user_input == 168  :
    user_input = int(input("what is the product of 7 * 24 ?"))
    if user_input == 168:
        print("You answered this Question correctly")
    else:
        
        print("Your Answer is wrong try again..", user_input)

        

    
    

