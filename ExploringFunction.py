#exploringFunctions.py
# <your name>
# <your section>
# Study RETURN VALUES and
# FORMAL PARAMETERS/ ARGUMENTS in functions.

def main():
    #divAndMod(89,5)
    # Part B
   
    
    # comment 2
    #rewriter('w')
    # comment 3
    #triple(2.33)
    
    # Part C
    # comment 4
     #x = triple(1.1)
    #print("x = {0:2f}".format(x))
    
    # comment 5
    #a = rewriter('w')
    #print("\na= ",a)
    # commeng 6
    #r=divAndMod( 89, 5 )
    #print("r = {0:2f}".format(r))
    
    # Part D
    # comment 7
    
    #y= 2.1
    #x= triple(y)
    #print("x = {0:.2f}.".format(x))
    #print("y = {0:.2f}.".format(y))
    # comment 8
    #n = 23
    #d = 10
    #r = divAndMod(n,d)
    #print("r=", r)
    #print("n=" , n , "d = ", d)
    
    # comment 9
    #S = "a"
    #rewriter(S)
    #print("\nS= ",S)
    
    # Part E
    
    rewriter("*")
    rewriter("$")
    rewriter("N")
    
    n = 13
    d = 5
    print("\nDividing ", n, "by",d,": ", end="")
    r = divAndMod(n,d)
    print("                    The remainder is {0}".format(r))
    
    
    
    f = 15
    g = 5
    print("Dividing ", f, "by",g,": ", end="")
    j = divAndMod(f,g)
    
    print("                    The remainder is {0}".format(j))
    print("\n", end="")
    rewriter("+-")
    rewriter("+-")
    
    a = 11
    q=triple(a)
    print("\nWhen I triple some number 1 get ",q,".")
    
    print("\n", end="")
    rewriter("e")
    print("\n ", end="")
    rewriter("c")
    print("\n  ",end="")
    rewriter("s")
    print("\n   ",end="")
    
    
   
    

# Print the parameter 5 times.
# Does not advance to the next line.
# let is the formal parameter
# let is a string
def rewriter( let):
    print(let*5, end="")


# triple the number n.
# n is the formal parameter.
# Note, no printed output.
def triple(n):
    answer = 3.0 * n
    return answer
# end triple


# print num // den
# returns num % den
# num and den are formal parameters, should be int
def divAndMod( num, den ):
    quotient = num // den
    remainder = num % den
    print("The quotient is {0}".format(quotient))
    return remainder
# end divAndMod
main()



    