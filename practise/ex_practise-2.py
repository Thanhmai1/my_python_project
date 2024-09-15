import ex_practise
print("")
while True:
        print('_________________________')
        x = float(input("Enter height: "))
        y = float(input("Enter wight: "))

        if x == y:
            shape_area = ex_practise.area(x, y)
            shape_chu_vi = ex_practise.chu_vi_square(y)
            print("This is a square")
            print(f"Area of square: {shape_area}")
            print(f"Chu vi of square: {shape_chu_vi}")
        else:
            shape_area = ex_practise.area(x, y)
            shape_chu_vi = ex_practise.chu_vi_rectangle(y, x)
            print("This is a rectangle")
            print(f"Area of rectangle: {shape_area}")
            print(f"Chu vi of rectangle: {shape_chu_vi}")
