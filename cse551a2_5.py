def greedy_interval(sorted_list_of_reals):
    result = []
    X = sorted_list_of_reals
    i = 0
    while i < len(X):
        interval = [X[i], X[i] + 2]
        for j in range(i+1, len(X)):
            if X[i] <= X[j] <= X[i]+2:
                pass
            else:
                i = j-1
                break
            i = j

        result.append(interval)
        i = i + 1

    return result


print(greedy_interval([1.5,2.0,2.1,5.7,8.8,9.1,10.2]))
