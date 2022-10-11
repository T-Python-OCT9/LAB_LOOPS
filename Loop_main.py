from tkinter import RIGHT


for i in range(45,210):
    if i ==100:
         continue
    if i ==205:
        break
    print(i)

while True:
     total =int(input("what is the product of 7 * 24 ?"))
     if total ==168 :
        print("You answered this Question correctly")
        break
     else:
        print(" and show the user the question again")