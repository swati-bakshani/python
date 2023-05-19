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

for key,value in thisdict.items():
    # print(key, value)
    if key == 'colours':
        print(value[0])
