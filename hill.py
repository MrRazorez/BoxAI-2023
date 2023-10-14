from box import BoxAndRules

class HillClimbing :
    def __init__(self) :
        self.__BOX = BoxAndRules()

        pass

    def inisialKotak(self):
        return self.__BOX.initials.copy(), self.__BOX.evaluate()
    
    def theReset(self):
        self.__BOX.resetBox()

    def eksekusi(self) :
        currentKotak = self.__BOX.initials.copy()
        currentEval = self.__BOX.evaluate()

        while currentEval > 0 :
            self.__BOX.randomize()

            neighborKotak = self.__BOX.initials.copy()
            neighborEval = self.__BOX.evaluate()

            if neighborEval <  currentEval :
                currentKotak = neighborKotak.copy()
                currentEval = neighborEval
                pass

            pass

        self.__BOX.initials = currentKotak.copy()
        pass