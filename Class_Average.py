# April 11th, 2023
# codewars.com/kata/5601409514fc93442500010b
# Python

def better_than_average(class_points, your_points):
    dividend = 0
    divisor = 0
    
    for i in class_points:
        dividend += i
        divisor += 1
    print(f"Final Total: {dividend}")
    print(f"Amount of Grades: {divisor}")
    
    
    quotient = dividend / divisor
    print(f"Average Score: {quotient}")
    print(f"Your Score: {your_points}")
    if quotient > your_points:
        print("You are below the Class Average")
        return False
    else:
        print("You are above the Class Average!")
        return True
        
