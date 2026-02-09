phonebook = {
    'travis': '555-1234',
    'xavier': '555-5678',
    'rakshan': '555-8765',
    'leo': '555-4321',
    'sarah': '555-2468',
    'john': '555-1357',
    'sophia': '555-2468',
    'michael': '555-9876',
    'emma': '555-6543',
    'oliver': '555-3210',
    'bobby': '555-7890',
    'lily': '555-2468',
    'william': '555-4321',
    'ava': '555-2468',
}
name1 = input("Enter a name: ")
name = name1.lower()
print("Number: ", phonebook.get(name, "Not found"))
delname= input("Enter a name to delete: ")
if delname in phonebook:
    del phonebook[delname]
    print(f"{delname} has been deleted from the phonebook.")
else:
    print(f"{delname} not found in the phonebook.")
print("Updated Phonebook:", phonebook)
