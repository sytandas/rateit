# T - time watcher have
# time - time individual movies have
# rating - movies rating
# n - lenght of (rating)

def knapSack(Time, time, rating, n):
    K = [[0 for x in range(Time+1)] for y in range(2)]
    for i in range(n + 1):
        for w in range(Time + 1):
            if (i == 0 or w == 0):
                K[i % 2][w] = 0
            elif (time[i - 1] <= w):
                K[i % 2][w] = max(
                        rating[i - 1]
                        +K[(i - 1) % 2][w - time[i - 1]],
                        K[(i - 1) % 2][w])
            else:
                K[i % 2][w] = K[(i - 1) % 2][w]
    return K[i % 2][Time]

if __name__ == "__main__":
    rating = [10, 8, 8, 7]
    time = [50, 40, 20, 10]
    Time = 40
    n = len(rating)
    print(knapSack(Time, time, rating, n))
