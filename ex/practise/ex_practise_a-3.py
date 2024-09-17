phones = [
    {
        "name": "Samsung Galaxy",
        "create_At": "16-9-2024"
    },
    {
        "name": "Nokia",
        "create_At": "10-9-2024"
    },
]
while True:
    print("------Menu-------")
    print("1. Create new phone")
    print("2. Display all elements")
    print("3. Sort by create day")
    choice = int(input("Enter a choice: "))

    if choice == 1:    
            name = input("Enter a name of phone: ")
            create_at = input("Enter day : ")     
            phones.append((name, create_at))
            print(phones)
    elif choice == 2:
        ans = input("Do you want sort list by create at[y/n]")
        if ans.lower() == 'y' or 'yes':
                phones.sort(key=lambda x: x["create_At"])
                print(phones)
        else:
            print('OK. Bye')
    elif choice == 3:
        print(f"{phones}")
        print("")
    elif choice == "4":
        break