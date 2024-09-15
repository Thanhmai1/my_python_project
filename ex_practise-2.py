from ex_practise import area
print("")
while True:
        print('_________________________')
        x = float(input("Enter height: "))
        y = float(input("Enter wight: "))

        if x == y:
            shape_area = area(x, y)
            print("This is a square")
            print(f"Area of square: {shape_area}")
        else:
            shape_area = area(x, y)
            print("This is a rectangle")
            print(f"Area of rectangle: {shape_area}")
