input = "nikhil meghnani"
def count_vowels(list):
    vowel = ["a","e","i","o","u"]
    count = 0
    for letter in list:
        if letter in vowel:
            count = count + 1
    return count

def print_vowels(list):
    output_list = []
    vowel = ["a","e","i","o","u"]
    for letter in list:
        if letter in vowel:
            output_list.append(letter)
    return output_list

print(count_vowels(input))
print(print_vowels(input))