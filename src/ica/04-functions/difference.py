def smallest_diff(x, y, z):
    print('smallest_diff inputs:', x, y, z)
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    print(diff1, diff2, diff3, 'return value:', min_diff)
    return min_diff
'''
Local environment
   x    32
   y    43
   z    90
'''
print(smallest_diff(32, 43, 90))