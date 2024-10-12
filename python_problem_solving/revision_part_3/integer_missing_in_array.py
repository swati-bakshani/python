input_list = [1,2,3,4,6,5,7,8,10]
# how to do missing no in 10,11,12,14,15,16.....   ans 13

def missing_integer(input_list):
    n = max(input_list)
    total_sum = sum(input_list)
    actual_sum = n*(n+1)/2
    return(actual_sum - total_sum)

print(missing_integer(input_list))

numbers = [10, 11, 13, 14, 15]

# Iterate over the list to find the missing number
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i - 1] != 1:  # Check for the gap
        missing_number = numbers[i - 1] + 1
        break

print(f"The missing number is: {missing_number}")

def missing_num(input_list):
    for num in range(len(input_list)-1):
        if input_list[num] - input_list[num+1] != 1:
            missing_number = input_list[num]+1
    return missing_number

# print(missing_num(input_list))
print(f"missing number is :{missing_num(input_list)}")

