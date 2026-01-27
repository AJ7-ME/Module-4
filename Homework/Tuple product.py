t1 = (4, 3, 2, 2, -1, 18)
t2 = (2, 4, 8, 8, 3, 2, 9)

def nums_only(t):
    for x in t:
        try:
            x + 1
        except TypeError:
            return False
    return True

def prod(t):
    p = 1
    for x in t:
        p *= x
    return p

if nums_only(t1):
    print("Product of t1:", prod(t1))
else:
    print("Error: t1 has non-numbers")

if nums_only(t2):
    print("Product of t2:", prod(t2))
else:
    print("Error: t2 has non-numbers")
