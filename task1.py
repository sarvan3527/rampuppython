import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height, shape):
    if shape == "triangle":
        return 0.5 * base * height

try:
    num_args = int(input("Enter the number of arguments (1, 2, or 3): "))

    if num_args == 1:
        radius = float(input("Enter the radius: "))
        if radius > 0:
            print("Circle Area:", calculate_circle_area(radius))
        else:
            print("Radius must be a positive value.")

    elif num_args == 2:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        if length > 0 and width > 0:
            print("Rectangle Area:", calculate_rectangle_area(length, width))
        else:
            print("Length and width must be positive values.")

    elif num_args == 3:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        shape = input("Enter the shape type (triangle): ").lower()
        if shape == "triangle" and base > 0 and height > 0:
            print("Triangle Area:", calculate_triangle_area(base, height, shape))
        elif shape != "triangle":
            print("Invalid shape entered. Please enter 'triangle'.")
        else:
            print("Base and height must be positive values for a triangle.")

    else:
        print("Invalid number of arguments. Please enter 1, 2, or 3.")

except:
    print("Invalid input. Please enter valid numeric values.")
