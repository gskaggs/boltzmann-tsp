import numpy as np
import itertools

MAX_DISTANCE = 250

def distance_matrix():
    return np.matrix([
    [0,  10, 20, 5,  18],
    [10, 0,  15, 32, 10],
    [20, 15, 0,  25, 16],
    [5,  32, 25, 0,  35],
    [18, 10, 16, 35, 0],
    ])

def path(state):
    path = []
    for colIdx in range(state.shape[1]):
        path.append(np.argmax(state[:,colIdx]))
    return path


def path_distance(distanceMatrix, path):
    distance = 0
    for index in range(len(path))[1:]:
        distance += distanceMatrix[path[index - 1], path[index]]
    return distance + distanceMatrix[path[0], path[-1]]


# Check to make sure you visit each city exactly once and that you're at exactly one city at each moment in time.
# Note: state[i, j] is 1 iff you are at city i at time j, and is 0 otherwise.
def isPathValid(state):
    assert(state.shape[0] == state.shape[1])
    N = state.shape[0]
    tours_valid  = not any([sum(state[:, idx]) != 1 for idx in range(N)])
    cities_valid = not any([sum(state[idx])    != 1 for idx in range(N)])
    return cities_valid and tours_valid