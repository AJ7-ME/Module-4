def palind(r):
    #return r == r[::-1]
    end = len(r) - 1
    start = 0
    while start < end:
        if r[start] != r[end]:
            return False
        start += 1
        end -= 1
    return True
r = (1,2,3,3,2,1)
if palind(r):
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")
