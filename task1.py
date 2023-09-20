import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height, shape):
    if shape == "triangle":
        return 0.5 * base * height

try:
    # Get input from the user
    num_args = int(input("Enter the number of arguments (1, 2, or 3): "))

    if num_args == 1:
        radius = float(input("Enter the radius: "))
        print("Circle Area:", calculate_circle_area(radius))

    elif num_args == 2:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("Rectangle Area:", calculate_rectangle_area(length, width))

    elif num_args == 3:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        shape = input("Enter the shape type (triangle): ").lower()
        if shape == "triangle":
            print("Triangle Area:", calculate_triangle_area(base, height, shape))
        else:
            print("Invalid shape entered. Please enter 'triangle'.")

    else:
        print("Invalid number of arguments. Please enter 1, 2, or 3.")

except:
    print("Invalid input. Please enter valid numeric values.")
