from testparser import Parser
import geneticOperators
import geneticAlgorithm
from chromosome import Chromosome
def main():
    
        

    p = Parser('(A+B)*(B+!C)')
    p.get_data_from_file('cnf.txt')
   
    print 'Solution: '  + str(geneticAlgorithm.genetic_function(p.data))
    
if __name__ == '__main__':
    import main as main
    main.main()
