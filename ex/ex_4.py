def get_user_input():
    """_Get user input_

    Returns:
        _num1_: _element in array 1_
        _num2_: _element in array 2_
    """
    num_1 = input("Enter a number for array 1 (Enter 'exit' to break): ")
    num_2 = input("Enter a number for array 2 (Enter 'exit' to break): ")
    return num_1, num_2


def max_min(arr):
    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

def same_numbers(arr1, arr2):
    same_nums = []
    for n in arr1:
        if n in arr2:
            same_nums.append(n)
    return same_nums

def different_numbers(arr1, arr2):
    diff_nums = []
    for n in arr1:
        if n not in arr2:
            diff_nums.append(n)
    for n in arr2:
        if n not in arr1:
            diff_nums.append(n)
    return diff_nums

def main():
    arr_1 = []
    arr_2 = []

    while True:
        num_1, num_2 = get_user_input()
        if num_1.lower() == 'exit' or num_2.lower() == 'exit':
            break
        try:
            arr_1.append(int(num_1))
            arr_2.append(int(num_2))
        except ValueError:
            print("Please enter valid numbers.")
        arr_3 = arr_1 + arr_2
    if arr_1 and arr_2:
        same_number_array = same_numbers(arr_1, arr_2)
        diff_number_array = different_numbers(arr_1, arr_2)        
        max_num, min_num = max_min(arr_3)                
        print(f"Max: {max_num}")
        print(f"Min: {min_num}")
        print(f"Same numbers: {same_number_array}")
        print(f"Different numbers: {diff_number_array}")
    else:
        print("Arrays are empty, no calculations to display.")

if __name__ == "__main__":
    main()
