import os

from hill import HillClimbing
from annealing import SimulatedAnnealing
from genetic import GeneticAlgorithm

class RandomError(Exception) :
    pass

class UserInterface :
    def __init__(self) :
        self.__isRunning = True
        self.__keyInput = 0
        self.__hillSYS = HillClimbing()
        self.__annealSYS = SimulatedAnnealing()
        self.__genSYS = GeneticAlgorithm()

        pass

    def sysUI(self) :
        while (self.__isRunning) :
            try :
                os.system('clear')
                
                if (self.__keyInput == 0) :
                    self.__keyInput = self.__mainMenu()
                    pass
                elif (self.__keyInput in [1, 2]) :
                    inisialKotak, inisialEval = self.__hillSYS.inisialKotak()

                    print("PENDAHULUAN")
                    self.__drawBox(inisialKotak)
                    print(inisialEval)
                    print("-----------\n\n\n")

                    self.__hillSYS.eksekusi()
                    hasilKotak, hasilEval = self.__hillSYS.inisialKotak()

                    self.__drawBox(hasilKotak)
                    print(hasilEval)

                    input("Tekan Enter untuk melanjutkan...")

                    self.__hillSYS.theReset()
                    self.__keyInput = 0
                    pass
                elif (self.__keyInput == 2) :
                    inisialKotak, inisialEval = self.__annealSYS.inisialKotak()

                    print("PENDAHULUAN")
                    self.__drawBox(inisialKotak)
                    print(inisialEval)
                    print("-----------\n\n\n")

                    self.__annealSYS.eksekusi()
                    hasilKotak, hasilEval = self.__annealSYS.inisialKotak()

                    self.__drawBox(hasilKotak)
                    print(hasilEval)

                    input("Tekan Enter untuk melanjutkan...")

                    self.__annealSYS.theReset()
                    self.__keyInput = 0
                    pass
                elif (self.__keyInput == 3) :
                    inisialKotak, inisialEval = self.__genSYS.inisialKotak()

                    print("PENDAHULUAN")
                    self.__drawBox(inisialKotak)
                    print(inisialEval)
                    print("-----------\n\n\n")

                    self.__genSYS.eksekusi()
                    hasilKotak, hasilEval = self.__genSYS.inisialKotak()

                    self.__drawBox(hasilKotak)
                    print(hasilEval)

                    input("Tekan Enter untuk melanjutkan...")

                    self.__genSYS.theReset()
                    self.__keyInput = 0
                    pass
                elif (self.__keyInput == 4) :
                    print("Sampai Jumpa!")
                    self.__isRunning = False
                    pass
                else :
                    raise RandomError()

            except:
                self.__keyInput = 0
                pass

            pass

        pass

    def __mainMenu(self) :
        print("MAIN MENU")
        print("1. Hill Climbing")
        print("2. Simulated Annealing")
        print("3. Genetic")
        print("4. Exit")

        return int(input())

        pass

    def __drawBox(self, theBox):
        print(" {} | {} | {} ".format(theBox[0], theBox[1], theBox[2]))
        print("---|---|---")
        print(" {} | {} | {} ".format(theBox[3], theBox[4], theBox[5]))
        print("---|---|---")
        print(" {} | {} | {} ".format(theBox[6], theBox[7], theBox[8]))

        pass
