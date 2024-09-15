arr_nums = []

while True:
    num = input("Enter a number (Enter 'exit' to break): ")
    if num.lower() == 'exit':
        break
    num = int(num)
    arr_nums.append(num)
print(f"Finally array: {arr_nums}")