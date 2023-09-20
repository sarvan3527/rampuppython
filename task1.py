import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

try:
    # Get input from the user
    shape = input("Enter the shape (rectangle, circle, or triangle): ").lower()

    if shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("Rectangle Area:", calculate_rectangle_area(length, width))
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        print("Circle Area:", calculate_circle_area(radius))
    elif shape == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print("Triangle Area:", calculate_triangle_area(base, height))
    else:
        print("Invalid shape entered. Please enter 'rectangle', 'circle', or 'triangle'.")
except ValueError:
    print("Invalid input. Please enter valid numeric values for the dimensions.")
except Exception as e:
    print("An error occurred:", str(e))
