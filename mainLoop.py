# the first task
for n in range(45, 210):
    if n == 100:
        continue
    print(n)
    if n == 205:
        break
    
    
#the second task
'''answer = "168"
while answer == "168":
    answer = input("what is the product of 7 * 24 ? ")
    if answer == "answer":
        print("You answered this Question correctly")
    elif answer!= "answer":
        print("Your Answer is wrong try again..")'''



while True:
    total = int(input("what is the product of 7 * 24 ? "))
    if total == 7*24:
        print("You answered this Question correctly")
        break
    else:
            print("Your Answer is wrong try again..") 
