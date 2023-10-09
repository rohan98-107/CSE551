from math import sqrt
from random import randint


def euclidean_dist(x, y):
    return sqrt((x[1] - y[1]) ** 2 + (x[0] - y[0]) ** 2)


def closest_pair(points):
    n = len(points)
    if n < 4:  # the reason we do this is because if we have two points or less in each half, those two points may
        # end up being closest to one another, so the only option is to just brute force it
        res = 100000000  # infinity if n = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = euclidean_dist(points[i], points[j])  # find the euclidean distance between points
                if dist < res:  # update resulting min distance if improvement
                    res = dist
        return res
    else:
        sorted_points = sorted(points,
                               key=lambda p: p[0])  # we first sort the points by x-coordinate for easy splitting
        left_half = sorted_points[:int(n / 2)]  # assign left of median to left half
        right_half = sorted_points[int(n / 2):]  # assign right of median to right half
        delta_1 = closest_pair(left_half)  # compute delta_1 from the left half -- recursive call 1
        delta_2 = closest_pair(right_half)  # compute delta_2 from the right half -- recursive call 2
        delta = min(delta_1, delta_2)  # take the minimum of the delta's

        L = (left_half[-1][0] + right_half[0][0]) / 2  # now we recompute the *actual* median to define delta-band
        S = [point for point in points if
             abs(point[0] - L) < delta]  # create the set of points that lie within delta-band
        S = sorted(S, key=lambda p: p[1])  # sort those point by y-coordinate
        i = 0
        for point in S:  # iterate through points in S starting with the 'lowest' y-value
            const = min(8, len(S) - i)  # only need to check EIGHT points after the current point (see problem 2.1)
            for j in range(i + 1, const):  # iterate through the next 8 or less points (less if length(S) is <= 8)
                dist = euclidean_dist(point, S[j])  # compute euclidean distance
                if dist < delta:  # update if resulting distance is an improvement of our previously computed delta
                    delta = dist
            i = i + 1

        return delta  # return the final delta, which is the closest distance between any two points in our set


pts = [(8, 16), (13, 3), (7, 9), (9, 19), (3, 21), (7, 8), (21, 19), (4, 15), (12, 2), (13, 8), (17, 11), (12, 15), (17, 15), (21, 12), (14, 19), (20, 6)]
print(pts)
print("Minimum Distance between two points is: ", closest_pair(pts))
