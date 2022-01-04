 

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num): #for how many pow_num, loop goes how many times
        result = result * base_num #result saves the number base_num multiplies itself
    return result

print(raise_to_power(2, 10))