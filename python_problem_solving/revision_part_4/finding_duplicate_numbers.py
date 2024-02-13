data_list_1 = [1,2,3,4,8]
data_list_2 = [1,2,8,3,7,9]

def find_duplicates(data_list_1,data_list_2):
    duplicate_records = []
    for num in data_list_1:
        if num in data_list_2:
            duplicate_records.append(num)

    return duplicate_records

print(find_duplicates(data_list_1,data_list_2))