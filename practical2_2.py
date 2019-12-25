a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_a = set(a)
set_b = set(b)

c = [common_value for common_value in set_a if common_value in set_b]

print(c)