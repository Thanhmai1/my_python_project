phone = ['Nokia', 'Samsung', 'Iphone', 'Redmi']
num = []
index = 0
for i in phone:
    print('for loop')
    print(f"Element [i]")
    
    
while index < len(phone):
    print('while loop')
    print(f"Element: {phone[index]}")
    index += 1
    
while True:
    value = input("Enter a value: ")
    po = int(input("Enter a positi: "))
    ans = input("Do you want exit [y/n]: ")
    if ans.lower() == 'y':
        print('Exitting...')
        break
    num.insert(po, value)
    print(num)