#To determine where the two monkeys should live such that the travel time between them is maximized
def max_travel_time(heights):
    N = len(heights)
    max_time = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            distance = min(abs(j - i), N - abs(j - i)
            travel_time = heights[i] + heights[j] + distance
            max_time = max(max_time, travel_time)
        return max_time
N = int(input().strip())
heights = [int(input().strip()) for _ in range(N)]
result = max_travel_time(heights)
print(result)
