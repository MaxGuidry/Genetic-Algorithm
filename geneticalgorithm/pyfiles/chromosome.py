class Chromosome(object):
    def __init__(self):
        self.data =''
        self.fitness = 0
        self.popfitness = 0

    def __str__(self):
        return '(' +str(self.data) + ', ' + str(self.fitness) + ', ' + str(self.popfitness)+')'