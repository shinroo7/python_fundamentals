#while loop: until the condition is true. Can be used for log filter

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


#for loop

friends = ["Csaba", "Lena", "Borka"]
for index in range(10):
    print(index) #will print 0~9

for index in range(3, 10):
    print(index) #will print 3~9, the last number won't be printed

for index in range(len(friends)):
    print(friends[index])


#nested loop: to access every elements in the grid (2d list)

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][2]) #it's 3

for row in number_grid:
    for col in row:
        print(col)
