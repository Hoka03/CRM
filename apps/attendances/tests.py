def add(x, y):
    return x + y


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

added_numbers = map(add, numbers1, numbers2)
added_numbers_list = list(added_numbers)

print(added_numbers_list)