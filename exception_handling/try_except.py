try:
    x = 1
    y = "hello"
    print(x)
    if type(y) is not int:
        raise Exception
except:
    print("something went wrong")

finally:
    print("remove your card")

# Raise a TypeError if x is not an integer:

x = "hello"
print(type(x))
if not type(x) is int:
  raise TypeError("Only integers are allowed")