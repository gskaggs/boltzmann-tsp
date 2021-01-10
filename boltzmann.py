import utils
import numpy as np
import random

class TSP:
    def __init__(self, distMat):
        self.distMat = distMat
        self.numCities = distMat.shape[0]
        self.numStates = self.numCities ** 2

        self.states = np.eye(self.numCities)

        # a guiding constraint: penalty > bias >= 2 * longestDistance
        bias = 2 * np.max(self.distMat)
        penalty = 2 * bias  # arbitrary

        self.weights = self.__init_weights(penalty, bias)
        self.temperature = self.__init_temp(penalty, bias)

    def __init_weights(self, penalty, bias):
        N = self.numCities
        weights = np.zeros((N, N, N, N))

        for city in range(N):
            dist = self.distMat[city, :] 
            for tour in range(N):
                cur = weights[city, tour]

                pre, nxt = (tour - 1) % N, (tour + 1) % N
                cur[:, pre] = dist
                cur[:, nxt] = dist

                cur[:, tour] = penalty
                cur[city, :] = penalty
                cur[city, tour] = -bias
        
        return weights

    def __init_temp(self, penalty, bias):
        # should be generally proportional to the number of steps and total cities to visit, but also
        # ensure that the temperature starts off significantly higher than highest change in consensus that can occur
        return ((penalty * self.numCities * (self.numCities+1)) - bias) * 100


    def __prob_on(self, city, tour, temp):
        state = self.states[city, tour]
        states = self.states.copy()
        states[city, tour] = 1
        
        # Energy with state (city, tour) being on - Energy with state (city, tour) off
        deltaEnergy = np.sum(states * self.weights[city, tour]) 
        exponential = np.exp(deltaEnergy / temp)
        return 1 / (1 + exponential) # Bigger delta energy => smaller probability of being on


    def solve(self):
        lastValidState = self.states.copy()
        lowest_temp = 0.2
        num_states = self.numCities
        while self.temperature > lowest_temp:
            for _ in range(self.numStates ** 2):
                city = random.randint(0, self.numCities-1)
                tour = random.randint(0, self.numCities-1)

                prob_on = self.__prob_on(city, tour, self.temperature)
                prob_flip = prob_on if self.states[city, tour] == 0 else 1 - prob_on
                
                if np.random.binomial(1, prob_flip):
                    self.states[city, tour] = 1 - self.states[city, tour]

                    if utils.isPathValid(self.states):
                        lastValidState = self.states.copy()

            # cooling...
            self.temperature *= 0.985
        
        # by this point the last valid state variable should hold the results of the simulated annealing
        return utils.path(lastValidState)
