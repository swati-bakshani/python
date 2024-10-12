given_str = "geekcodders in raipur"
# output_result = geekcoders in the city of raipur

def insert_new_string(given_str):
    return given_str.replace("in" , "in the city of")

print(insert_new_string(given_str))