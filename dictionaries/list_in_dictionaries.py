thisdict={
    "brand":"Kia",
     "electric":"yes",
     "model":"sonnet",
     "year":"2022",
     "colours":["red","green","white"]
}

# print(thisdict)
# print(thisdict["colours"])
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict["colours[0]"])

# for key,value in thisdict.items():
#     # print(key, value)
#     if key == 'colours':
#         print(value[0])

numbers = [3,6,2,4,3,6,8,9]
print(len(numbers))
for i in range(len(numbers)):
    print(f"value of i: {i}")
    for j in range(i+1, len(numbers)):
        print(f"value of j: {j}")
        if numbers[i] == numbers[j]:
            # print(str(numbers[i]) + " is a duplicate")
            print(f"{numbers[i]} is a duplicate")
            break