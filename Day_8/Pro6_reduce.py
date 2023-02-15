# from functools import reduce
#
# def add(x, y):
#     return x + y
#
# list = [2, 4, 7, 3]
# print(reduce(add, list))


from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
