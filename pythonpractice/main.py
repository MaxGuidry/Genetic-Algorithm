from testparser import Parser
def main():
    p = Parser('(A+B)*(B+!C)')
    p.get_data_from_file("test.txt")
    print p.get_vars()
    print p.get_clauses()
    print p.get_num_clauses()
if __name__ == '__main__':
    import main as main
    main.main()