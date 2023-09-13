# Task description
# There are N blocks, numbered from 0 to N-1, arranged in a row. A couple of frogs were sitting together on one block when they had a terrible quarrel. Now they want to jump away from one another so that the distance between them will be as large as possible. The distance between blocks numbered J and K, where J ≤ K, is computed as K − J + 1. The frogs can only jump up, meaning that they can move from one block to another only if the two blocks are adjacent and the second block is of the same or greater height as the first. What is the longest distance that they can possibly create between each other, if they also chose to sit on the optimal starting block initially?

# Write a function:

# def solution(blocks)

# that, given an array blocks consisting of N integers denoting the heights of the blocks, returns the longest possible distance that two frogs can make between each other starting from one of the blocks.

# Examples:

# 1. Given blocks = [2, 6, 8, 5], the function should return 3. If starting from blocks[0], the first frog can stay where it is and the second frog can jump to blocks[2] (but not to blocks[3]).

# "Graphical representation of example 1."

# 2. Given blocks = [1, 5, 5, 2, 6], the function should return 4. If starting from blocks[3], the first frog can jump to blocks[1], but not blocks[0], and the second frog can jump to blocks[4].

# "Graphical representation of example 2."

# 3. Given blocks = [1, 1], the function should return 2. If starting from blocks[1], the first frog can jump to blocks[0] and the second frog can stay where it is. Starting from blocks[0] would result in the same distance.

# "Graphical representation of example 3."

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..200,000];
# each element of array blocks is an integer within the range [1..1,000,000,000].



def solution(blocks):
    N = len(blocks)

    # Create an array to store the maximum distances for each starting block
    max_distances = [0] * N

    # Calculate the maximum distance for each starting block
    for i in range(N):
        max_left = i
        max_right = i

        # Extend left
        while max_left > 0 and blocks[max_left - 1] >= blocks[max_left]:
            max_left -= 1

        # Extend right
        while max_right < N - 1 and blocks[max_right + 1] >= blocks[max_right]:
            max_right += 1

        # Calculate the maximum distance for this starting block
        max_distances[i] = max_right - max_left + 1

    # Return the maximum value in the max_distances array
    return max(max_distances)

# Test cases
blocks1 = [2, 6, 8, 5]
blocks2 = [1, 5, 5, 2, 6]
blocks3 = [1, 1]

print(solution(blocks1))  # Output: 3
print(solution(blocks2))  # Output: 4
print(solution(blocks3))  # Output: 2
