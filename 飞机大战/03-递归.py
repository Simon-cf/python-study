def  get_sum(n, m):
    if m == n:
        return n
    return get_sum(n, m - 1) + m
print(get_sum(1, 100))