#function starts with def and a function name
#def sayhi( ):
    #print("Hello User")

#sayhi() #need to call/execute the function

#def sayhi(name, age): #parameter gives information
    #print("Hello " + name + ", you are " + age)

#sayhi("Csaba", "33") 


#return statement: get info back from the function and break out of the function

def cube(num):
    return num*num*num

result = cube(3)
print(result)
print(cube(3))
