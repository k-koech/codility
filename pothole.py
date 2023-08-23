def solution(R):
    N = len(R)
    largest_pothole_indicator = 0
    
    current_group_size = 0
    current_group_depth = 0
    
    for i in range(N):
        if R[i] > 0:
            current_group_size += 1
            current_group_depth = max(current_group_depth, R[i])
        else:
            largest_pothole_indicator = max(largest_pothole_indicator, current_group_size * current_group_depth)
            current_group_size = 0
            current_group_depth = 0
    
    largest_pothole_indicator = max(largest_pothole_indicator, current_group_size * current_group_depth)
    
    return largest_pothole_indicator

# Test cases
print(solution([0, 2, 1, 1, 0, 4, 1])) # Output: 8
print(solution([1, 4, 1, 0, 5, 2, 3, 0, 8])) # Output: 15
print(solution([9, 8, 7, 0, 0, 0, 2, 3, 6, 4])) # Output: 27
print(solution([0, 0, 0])) # Output: 0
