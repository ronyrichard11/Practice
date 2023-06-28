# June 27th, 2023
# codewars.com/kata/5583090cbe83f4fd8c000051/train/python
# Python

def digitize(n):
    reversed_array = []

    reversed_str = str(n)[::-1]

    reversed_array = [int(char) for char in reversed_str]
    return reversed_array