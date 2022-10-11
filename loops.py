#loops

phrase : str = "I love python!"

for character in phrase:
    print(character.upper())
    if character == "p" : 
        break



for i in range(1, 50, 2):
    if i == 5:
        continue
    print(i)


items : int = 50

while items <= 50 and items >= 1:
    items = items-1
    if items == 40:
        break
    print("looping", items)

else:
    print("the loop finished successfully")

print(items)


for c in character:
    pass


user_input = input("What is your name ? ")

print("Hello ", user_input)