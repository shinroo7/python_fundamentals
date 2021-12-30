# Order is important in Python
#print("   /|")
#print("  /  \\")
#print(" /___")
#print(" /____|")

# Variables & Data Type: use underline to connect the variables words (if more than one word). 
# The data types we often use are String, Number and Boolean.
#character_name = "Freya" #string
#character_age = "25" #number
#is_male = "False" #Boolean

#print("There is a girl called " + character_name + ",")
#print("and she is " + character_age + " years old")

#functions: using . , ex: variables.uppercase()
#phrase = "Giraffe Academy"
#print(phrase)

#basic calculator: by default, everything key in in Python is String.
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")

#result = int(num1) + int(num2)
#print(result)

#result2 = float(num1) + float(num2)
#print(result2)


# list => array
#friends = ["Abel", "Lena", "Borka", "Reka", "Istven"]

#print(friends)
#print(friends[2:]) #everything after [2]Borka
#print(friends[1:3]) #doesn't include [3]Reka


#list functions: remove(), 
# pop (delete the last value), 
# clear(clear all values), 
# count(count how many times a value show up), 
# copy(duplicate the values to another variable) 

lucky_numbers = [7, 77, 777, 7777, 77777, 0]
friends = ["Abel", "Lena", "Borka", "Reka", "Istven"]
#friends.extend(lucky_numbers) #combine multiple lists(arrays)
#friends.append("Csaba") #add in the last to the list(array)
#friends.insert(1, "Illona") #insert new value to the list by pointing the index
friends.sort() #alphabeta order
print(friends)
#print(friends.index("Lena"))






