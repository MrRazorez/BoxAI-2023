import random

class BoxAndRules :
    def __init__(self) :
        self.initials = [1,2,3,4,5,6,7,8,9]
        self.resetBox()

        pass

    def resetBox(self) :
        random.shuffle(self.initials)
        
        pass

    def randomize(self) :
        i, j = random.sample(range(9), 2)

        self.initials[i], self.initials[j] = self.initials[j], self.initials[i]

        pass

    def evaluate(self, *args) :
        data1, data2 = 0, 0

        if args == () :
            data1 = self.initials[1] + self.initials[4] + self.initials[7]
            data2 = self.initials[3] + self.initials[4] + self.initials[5]
        else :
            data1 = args[0][1] + args[0][4] + args[0][7]
            data2 = args[0][3] + args[0][4] + args[0][5]
            
        return abs((data1) - (data2))