input = "Nikhil meghnani"

def count_consonants(list):
    output_list = []
    vowel = ["a","e","i","o","u"]
    count = 0
    for letter in list:
        if letter not in vowel:
            count = count + 1
    return count

print(count_consonants(input))



