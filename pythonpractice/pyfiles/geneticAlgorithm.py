import random
import geneticOperators
from cnfParser import Parser
from chromosome import Chromosome

def random_chromosome(size):
    chromosome = Chromosome()
    for i in range(0,size):
        chromosome.data += str(random.randint(0,1))
    return chromosome


def genetic_function(cnf):
    p = Parser(cnf)
    p.get_vars()
    solution = ''
    generation = 1
    population = []
    numOfKids = p.variables.__len__()/2
    print numOfKids
    population.append(random_chromosome(p.variables.__len__()))
    population.append(random_chromosome(p.variables.__len__()))
    print population
    while solution is '':
        population = geneticOperators.fitness(population, cnf)
        population = sorted(population, key=lambda x: x.popfitness, reverse=True)

        if int(population[0].fitness) is 1:
            return population[0]
        #if generation%500 is 0:
        print generation
        #print "Most Fit: " + str(population[0])
        newpop = []
        for i in range(0,numOfKids):
            kids = geneticOperators.crossover(population[0], population[1])
            kid1 = geneticOperators.mutate(kids[0])
            kid2 = geneticOperators.mutate(kids[1])

            newpop.append(kid1)
            newpop.append(kid2)
            i+=1
        population = newpop
        #print population.__len__()
        generation += 1

       # for chromosome in population:
        #    if p.test_solution(chromosome) is 1:
         #       solution = chromosome
          #      break
           # else:

if __name__ == '__main__':
    import main as main
    main.main()
