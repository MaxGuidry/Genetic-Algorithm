import os
class Parser(object):
    def __init__(self, string):
        self.data = string
        self.num_clauses = 0
        self.variables = []
        self.clauses = []
        self.grammar = ['*','(','+',')','!']
        
    def get_clauses(self):
        self.clauses = []
        copy = False
        string_to_add = ''
        for d in self.data:
            if d is '(':
                copy = True
            if copy:
                string_to_add += d
            if d is ')':
                copy = False
                self.clauses.append(string_to_add)
                string_to_add = ''
        return self.clauses

    def get_num_clauses(self):
        self.num_clauses = 0
        for d in self.data:
            if d is '(':
                self.num_clauses += 1
        return self.num_clauses
    
    def get_vars(self):
        #i=0
        # for d in self.data:
        #    if d is '(' or d is '+':
        #        if(self.data[i+1] is '!'):
        #            if (self.data[i+2],) not in self.variables:
        #                self.variables.append((self.data[i+2],))
        #        elif (self.data[i+1],) not in self.variables:
        #            self.variables.append((self.data[i+1],))
        #    i+=1
        self.variables = self.data
        characters = []
        for g in self.grammar:
            self.variables = self.variables.replace(g,'')
        for d in self.variables:
             if d not in characters:
                 characters.append(d)
        self.variables = sorted(characters,key = lambda x: x)
        #self.variables = characters.sort(key = lambda x: x,reverse = False)
        return self.variables   

    def get_data_from_file(self,filename):
        filedata = open(filename,'r')
        self.data = filedata.read()
    

if __name__ == '__main__':
    import main as main
    main.main()