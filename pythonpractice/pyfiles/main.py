from cnfParser import Parser
import geneticOperators
import geneticAlgorithm
from chromosome import Chromosome
import sys
firstarg = sys.argv[0]
def main():
    
        

    p = Parser('(A+B)*(B+!C)')
    p.get_data_from_file('cnf.txt')
    p.get_vars()
    solution =  str(geneticAlgorithm.genetic_function(p.data))
    print "CNF Equation Solved: " + p.data
    print "Number of variables: " + str(p.variables.__len__())
    print "Solution: " + solution
    raw_input()
    
if __name__ == '__main__':
    import main as main
    main.main()
