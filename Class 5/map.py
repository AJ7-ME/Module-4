numbers1 = [1, 2, 3]
numbers2 = [6, 5, 4]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("addition of two lists:", list(result))
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n * n
square = list(map(sq, nums))
print("squares of numbers:", square)