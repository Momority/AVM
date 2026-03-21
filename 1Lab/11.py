def maxArea(h):
    l = 0
    r = len(h) - 1
    max_water = 0
        
    while l < r:
        w = r - l
        curr_h = min(h[l], h[r])
        
        curr_water = w * curr_h
        max_water = max(max_water, curr_water)

        if h[l] < h[r]:
            l += 1
        else:
            r -= 1
                
    return max_water

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
print(maxArea([1, 1]))                      # 1