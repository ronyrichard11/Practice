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
        


better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)