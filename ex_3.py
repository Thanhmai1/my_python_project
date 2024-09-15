arr = []

max_num = None
min_num = None

sum_odd = 0
sum_even = 0

while True:
    numbers = input("Enter a number (Enter 'exit' to break): ")
    if numbers.lower() == 'exit':
        break
    numbers = int(numbers)
    arr.append(numbers)

    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    sum_odd = sum(num for num in arr if num % 2 != 0)
    sum_even = sum(num for num in arr if num % 2 == 0)

print(f'Length of array: {len(arr)}')
print("")
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
print("")
print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
