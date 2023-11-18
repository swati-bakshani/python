def even_no_square(list):
    output=[]
    for i in list:
        if i % 2 == 0:
            a = i * i
            output.append(a)
    return output


print(even_no_square(list))