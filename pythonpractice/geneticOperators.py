import random
import math
from testparser import Parser
from chromosome import Chromosome
def mutate(chromosome):
    newChromosome = Chromosome()
    for c in chromosome.data:
        r = random.randint(0, 100)
        if r < 10:
            if c is '0':
                c = '1'
            elif c is '1':
                c = '0'
        newChromosome.data = newChromosome.data + c
    return newChromosome

def crossover(p1, p2):
    split = math.floor(p1.data.__len__()/2)#random.randint(1, str(p1.data).__len__())
    kid1 = Chromosome()
    kid2 = Chromosome()
    for i in range(0, str(p1.data).__len__()):
        if i < split:
            kid1.data = kid1.data + p1.data[i]
            kid2.data = kid2.data + p2.data[i]
        else:
            kid1.data = kid1.data + p2.data[i]
            kid2.data = kid2.data + p1.data[i]
    return (kid1, kid2)

def fitness(population, cnf):
    p = Parser(cnf);
    p.get_clauses()
    p.get_num_clauses()
    p.get_vars()
    fit_percent = []
    for chromosome in population:
        sol = p.test_solution(chromosome.data)
        score = 0
        for s in sol:
            if s is 1:
                score += 1
        chromosome.fitness = float(score) / float(p.num_clauses)
        fit_percent.append(chromosome.fitness)
    fitness_scores = {}
    total = 0
    for p in fit_percent:
        total += p
    i = 0
    for c in population:
        c.popfitness =(float(fit_percent[i])/float(total))
        i+=1
    return population
        
        
