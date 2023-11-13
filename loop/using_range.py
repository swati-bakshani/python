for x in range(2,6):
    print(x)


print("###############################")
for x in range(2,30,3):
    print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
    print(x)
else:
    print("finally finished!")

# break the loop when x is 3
for x in range(6):
    if x == 3:
        break
else:
    print("finally finished!")