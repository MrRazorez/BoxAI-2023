import random

from box import BoxAndRules

class GeneticAlgorithm :
    def __init__(self) :
        self.__BOX = BoxAndRules()
        self.__popSize = 100
        self.__gens = 1000
        self.__mutRate = 0.01

        pass

    def inisialKotak(self) :
        return self.__BOX.initials.copy(), self.__BOX.evaluate()
    
    def theReset(self) :
        self.__BOX.resetBox()
        self.__popSize = 100
        self.__gens = 1000
        self.__mutRate = 0.01

    def __crossover(self, mom, dad) :
        return mom.copy()[:5] + dad.copy()[5:]
    
    def __evolve(self, populasi) :
        popBaru = []

        populasi = sorted(populasi, key=lambda x: self.__BOX.evaluate(x))
        bibitUnggul = populasi[:10]

        while len(popBaru) < len(populasi) :
            mommy, daddy = random.choices(bibitUnggul, k=2)
            child = self.__crossover(mommy, daddy)

            if random.random() < self.__mutRate :
                i, j = random.sample(range(9), 2)
                child[i], child[j] = child[j], child[i]
                pass

            popBaru.append(child)
            pass

        return popBaru

    def eksekusi(self) :
        populasi = []

        for _ in range(self.__popSize) :
            populasi.append(self.__BOX.initials.copy())
            if _ < self.__popSize :
                self.__BOX.randomize()
                pass
            pass

        for _ in range(self.__gens) :
            populasi = self.__evolve(populasi)

            if self.__BOX.evaluate(populasi[0]) == 0 :
                break
            pass

        self.__BOX.initials = populasi[0].copy()
        pass