# 10th April 2023
# Link: codewars.com/kata/54ff3102c1bad923760001f3
# Python

def get_count(sentence):
    vowel_count = 0
    vowels = "aeiou"
    for i in sentence:
        if i in vowels:
            vowel_count += 1
    print(vowel_count)
    return vowel_count



