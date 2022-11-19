# Time - time watcher have
# time - time individual movies have
# rating - movies rating
# n - lenght of (rating)
# using 2-D array with 2 rows O(2W)
# Time coplexity O(N*W)


def knapSack(time, rating, Time, n):
    # K = [[0 for x in range(Time+1)] for y in range(2)]
    # base condtions 
    table = [[-1 for i in range(Time + 1)] for j in range(n + 1)]
    if (n == 0 or Time == 0):
        return 0
    if table[n][Time] != -1:
        return table[n][Time]
    # choices
    if time[n - 1] <= Time:
        table[n][Time] = max(rating[n - 1] + knapSack(time, rating, Time - time[n - 1], n - 1),
                                                      knapSack(time, rating, Time, n - 1))
        return table[n][Time]
    elif time[n - 1] > Time:
        table[n][Time] = knapSack(time, rating, Time, n - 1)
        return table[n][Time]
if __name__ == "__main__":
    rating = [10, 8, 8, 7]
    time = [50, 40, 20, 10]
    Time = 40
    n = len(rating)
    print(knapSack(time, rating, Time, n))
