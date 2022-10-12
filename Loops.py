from tracemalloc import Trace


for i in range (45 , 210) :
    if i == 100 :
        continue 
    elif i == 205 :
        break

    print(i)



user_input = int (input ("What is the product of 7 * 24 ?"))
while user_input == 168 :
    print ("You answered this Question correctly")
    break
else :
    print ("Your Answer is wrong try again..")

  
  