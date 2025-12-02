# HW 8.3. Унікальне число.

def find_unique_value(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    for x, c in freq.items():
        if c == 1:
            return x


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 5, 5, 0.5]))

print(' ')
print('===========================')
print(' ')

from collections import Counter


def find_unique_value(nums):
    # Припускаємо, що в списку рівно одне унікальне число
    counts = Counter(nums)
    for num, cnt in counts.items():
        if cnt == 1:
            return num


print(find_unique_value([1, 2, 2, 5, 3, 3]))  # 1
print(find_unique_value([4, 4, 7, 8, 5, 5]))  # 7
