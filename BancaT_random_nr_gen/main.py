import random
from itertools import repeat
import unittest


class RandomNumberGenerator:  # random number generator class
    def __init__(self, weights):  # input list set in a class attribute
        self.__weights = weights

    def getInput(self):  # getter/setter for input list attribute
        return self.__weights

    def setInput(self, newInput):
        self.__weights = newInput

    # first solution with an expanded list ( best solution in speed for small sets ) most straigh-forward
    # only for integer weights
    def generate_expanded(self):
        distrib = []  # basically adding the the number in the list how many times it's weight
        for i in range(0, len(self.__weights)):
            distrib.extend(repeat(i, self.__weights[i]))
        return int(random.choice(distrib))

    # generating with python's included library ! ------ tested implementation
    def generate_with_library(self):
        indices = list(range(0, len(self.__weights)))  # just filling the indices list
        return random.choices(indices, self.__weights)[0]  # calling python's random.choice with weights

    # generating in a more iterative
    def generate_iterative(self):
        for i in range(0, len(self.__weights)):
            self.__weights[i] *= 100
            self.__weights[i] = int(self.__weights[i])
        distrib = []  # basically adding the the number in the list how many times it's weight
        for i in range(0, len(self.__weights)):
            distrib.extend(repeat(i, self.__weights[i]))
        return int(random.choice(distrib))


class UnitTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_for_library(self):  # tests for 100.000 calls of method checks if weights are aproximately the same

        # ---------------------------- TEST LOGIC ----------------------------------

        def aux_func(weights, probability):  # inner function to calculate for diffrent data sets
            rng_instance = RandomNumberGenerator(weights)
            newDict = {}
            for i in range(0, 100000):
                cur_nr = rng_instance.generate_with_library()  # save all numbers occurances in a dictionary
                if cur_nr in newDict:
                    newDict[cur_nr] += 1
                else:
                    newDict[cur_nr] = 1

            s = sum(newDict.values())  # tehnically i could just write 100.000 because sum should equal this
            print("Initial weights:", weights)
            for k, v in newDict.items():
                print("Number:", k, "raw value / nr. of occurrences :", v)  # raw value taken from dictionary
                pct = v * 100.0 / s
                print("Number:", k, "with probability:", pct)  # numbers turned into percentages
                pct = round(pct)  # i do a bit of rounding because assert almost equals has a very strict aproximation
                self.assertAlmostEqual(pct, probability[k])  # checking if it's matching with our expected probability

        # -------------------------- TEST DATA SETS ------------------------------

        weights = [1.0, 1.0]  # weights as input
        probability = [50, 50]  # expected probability for each index coresponding in weights here 1/2 and 1/2
        aux_func(weights, probability)

        weights.clear()
        probability.clear()

        weights = [1.0, 1.0, 1.0, 1.0, 1.0]
        probability = [20, 20, 20, 20, 20]  # 1/5 probability for every number
        aux_func(weights, probability)

        weights.clear()
        probability.clear()

        weights = [2.0, 0.0, 2.0]
        probability = [50, 0, 50]  # 1/2  probability except for 1 (second from list) which won't be generated
        aux_func(weights, probability)

        weights.clear()
        probability.clear()

        weights = [1.5, 1.0]
        probability = [60, 40]
        aux_func(weights, probability)

        weights.clear()
        probability.clear()

        weights = [1.0, 9.0]
        probability = [10, 90]
        aux_func(weights, probability)

        weights.clear()
        probability.clear()

        weights = [3.0, 4.5, 2.5]
        probability = [30, 45, 25]
        aux_func(weights, probability)

        weights.clear()
        probability.clear()

        weights = [1.5, 0.5, 1]
        probability = [50, 17, 33]
        aux_func(weights, probability)

        weights.clear()
        probability.clear()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # rng_instance = RandomNumberGenerator([1.0, 1.0])  # imput distributions here
    # # print(rng_instance.generate_expanded())
    # print(rng_instance.generate_with_library())
    unittest.main()

    # -------------- USE CASE ----------------
    # create instance rng_instance = RandomNumberGenerator(weights)
    # and then call method rng_instance.generate_with_library()
