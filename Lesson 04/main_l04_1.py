lst = [0, 1, 0, 12, 3]
result = [x for x in lst if x != 0] + [0] * lst.count(0)
print(result)

lst = [0]
result = [x for x in lst if x != 0] + [0] * lst.count(0)
print(result)

lst = [1, 0, 13, 0, 0, 0, 5]
result = [x for x in lst if x != 0] + [0] * lst.count(0)
print(result)

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = [x for x in lst if x != 0] + [0] * lst.count(0)
print(result)
