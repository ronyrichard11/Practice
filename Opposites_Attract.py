# 10th April, 2023
# codewars.com/kata/555086d53eac039a2a000083
# Python

def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 1 or flower1 % 2 == 1 and flower2 % 2 != 0:
        print("InCompatible")
        return False
    else:
        print("Compatible")
        return True
