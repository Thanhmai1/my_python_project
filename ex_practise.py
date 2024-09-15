def area(height, wight):
    return height * wight


while True:
    print('_________________________')
    x = int(input("Enter height: "))
    y = int(input("Enter wight: "))

    if x == y:
        shape_area = area(x, y)
        print("This is a square")
        print(f"Area of square: {shape_area}")
    else:
        shape_area = area(x, y)
        print("This is a rectangle")
        print(f"Area of rectangle: {shape_area}")
