# a = "abc def"
# def reverse(a):
#     b = a.split(" ")
#     c = ["".join(i[::-1]) for i in b]

#     return c

# print(reverse(a))

def create_even(start,stop):
    return [i for i in range(start,stop) if i%2 == 0]

print(create_even(1,100))