import random
import math

from box import BoxAndRules

class SimulatedAnnealing :
    def __init__(self) :
        self.__BOX = BoxAndRules()
        self.__suhuInit = 1000.0
        self.__coolingRate = 0.95

        pass

    def inisialKotak(self) :
        return self.__BOX.initials.copy(), self.__BOX.evaluate()
    
    def theReset(self) :
        self.__BOX.resetBox()
        self.__suhuInit = 1000.0

    def eksekusi(self) :
        currentKotak = self.__BOX.initials.copy()
        currentEval = self.__BOX.evaluate()

        while self.__suhuInit > 0 :
            self.__BOX.randomize()

            newKotak = self.__BOX.initials.copy()
            newEval = self.__BOX.evaluate()

            deltaEnergy = newEval - currentEval

            if deltaEnergy < 0 or random.random() < math.exp(-deltaEnergy/self.__suhuInit) :
                currentKotak = newKotak.copy()
                currentEval = newEval

            self.__suhuInit *= self.__coolingRate

            pass

        self.__BOX.initials = currentKotak.copy()
        pass