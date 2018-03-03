from cnfParser import Parser
import geneticOperators
import geneticAlgorithm
from chromosome import Chromosome
import sys
firstarg = sys.argv[0]
def main():
    
        

    p = Parser('(A+B)*(B+!C)')
    p.get_data_from_file('test1.txt')
    p.get_vars()
    
    print "CNF Equation To Solve: " + p.data
    print "\nEXPECTED OUTPUT: a-z + numbers and special characters, all true"
    print "\nNumber of variables: " + str(p.variables.__len__()) + "\n"
    solution =  str(geneticAlgorithm.genetic_function(p.data).data)
    print "\nSolution: " + solution + "\n\n"

    print "------------------------------------------------------------------------------------------------------------"
    print "------------------------------------------------------------------------------------------------------------"

    p.get_data_from_file('test2.txt')
    p.get_vars()
    print "\nCNF Equation To Solve: " + p.data
    print "\nEXPECTED OUTPUT: a-z, first half false second half true"
    print "\nNumber of variables: " + str(p.variables.__len__()) + "\n"
    solution =  str(geneticAlgorithm.genetic_function(p.data).data)
    print "\nSolution: " + solution + "\n\n"

    print "------------------------------------------------------------------------------------------------------------"
    print "------------------------------------------------------------------------------------------------------------"

    p.get_data_from_file('test3.txt')
    p.get_vars()
    
    print "\nCNF Equation To Solve: " + p.data
    print "\nEXPECTED OUTPUT: a-z, all true except the last one"

    print "\nNumber of variables: " + str(p.variables.__len__()) + "\n"
    solution =  str(geneticAlgorithm.genetic_function(p.data).data)
    print "\nSolution: " + solution + "\n\n"

    print "------------------------------------------------------------------------------------------------------------"
    print "------------------------------------------------------------------------------------------------------------"

    p.get_data_from_file('test4.txt')
    p.get_vars()
    
    print "\nCNF Equation To Solve: " + p.data
    print "\nEXPECTED OUTPUT: a-z + special characters, first three false all the rest true"
    print "\nNumber of variables: " + str(p.variables.__len__()) + "\n"
    solution =  str(geneticAlgorithm.genetic_function(p.data).data)
    print "\nSolution: " + solution + "\n\n"
    raw_input()
    
if __name__ == '__main__':
    import main as main
    main.main()
