

class State:

    def __init__ (self,name,population):
        self.name = name
        self.population = population


    def display (self):
        
        
        print ("{0}            Popltion: {1:,}".format(self.name,self.population))
    def getPopulation(self):
        self.population = population
        return population

def makeAState(line):
    w = line.split("\t")
    state =   w[0]
    popultion = w[1]
    
    popultion=popultion.replace(",","")
   
    
    MyState = State(state,int(popultion))
    return MyState

def usePopulation(aState):
    population = aState.getPopulation()
    return population

def main():
    Newyork = State("NewYork", 19862512)
    Texas = State("Texas", 26424712)
    Newyork.display()
    Texas.display()
    infile = open("states.txt","r")
    file= infile.readlines()
    StatesList  = []
    
    for line in file:
        Objectstate= makeAState(line)
        StatesList.append(Objectstate)
    StatesList[0].display()
    

    infile.close()
main()
        
        


   

