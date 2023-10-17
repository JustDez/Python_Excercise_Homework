# 1) Accept two user ages as inputs and give us the difference between them. 
# (The Answer should always be a positive output)

User1 = input("User one, what is your age?")
User2 = input("User two, what is your age?")

if User1 >= User2:
    print(User1 - User2) #figure out how to do one problem or the other
else:
    print(User2 - User1)






# 2) Accept 3 user inputs for variables named noun, verb and adjective. 
# Print out a formatted string using the outputs.
User1 = input("name a noun, a verb, and an adjective")

User2 = input("name a noun, a verb, and an adjective")

User3 = input("name a noun, a verb, and an adjective")

print(User1, User2, User3)




# 3) Take in a users input for their age, if they are younger than 18 print kids, 
#  if they're 18 to 65 print adults, else print seniors
age = input("What is your age?")
if age <= 18:
    print("kids")
elif age >= 65:
    print("adults")
else:
    print("senior")





# 4) Take in a number from a user input, output the number squared.
num = input("pick a number")
    print(num**2)





# 5) Check the below variables' length. If the length of the word is greater than 5 output True, 
#   if it is less than 5, output False

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

length_of_word = len(word1, word2,word3,word4,word5)
print(length_of_word)
print(len(word1, word2, word3, word4, word5))

if len >= 5:
    print(True)
else:
    print(False)


