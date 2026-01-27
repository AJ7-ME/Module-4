low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
Empty_list = []
for num in range(low, high + 1):
    root = num ** 0.5
    if root.is_integer():
        print(f"{num} is a perfect square.")
        Empty_list.append(num)
print("Perfect squares in the given range are:", Empty_list)