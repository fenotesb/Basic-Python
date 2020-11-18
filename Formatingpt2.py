
# What does this do?
def snowball():
    s='*'
    print("{0:>11}".format("****"))
    print("{0:>7}{0:>6}".format("**"))
    print("{0:>5}{0:>9}".format(s))
    print("{0:>4}{0:>11}".format(s))
    print("{0:>4}{0:>11}".format(s))
    print("{0:>5}{0:>9}".format(s))
    print("{0:>7}{0:>6}".format("**"))
    print("{0:>11}".format("****"))
    ## end snowball

def hat():
    print("{0:>11}".format("****"))
    print("{0:>7}{0:>6}".format("**"))
    print("{0:>5}{0:>9}".format('*'))
    print("{0:>4}{0:>11}".format('*'))
         


def main():
    hat() 
    snowball()
    hat()
    snowball()
    hat()
    snowball()
main()


def f():
    
    print("{0:>11}".format("********"))
    print("{0:^7}".format("*"))
    print("{0:^7}".format("*"))
    print("{0:>11}".format("********"))
    print("{0:^7}".format("*"))
    print("{0:^7}".format("*"))
    ## this is a F 

def T():
    print("{0:>11}".format("********"))
    print("{0:^15}".format("*"))
    print("{0:^15}".format("*"))
    print("{0:^15}".format("*"))
    print("{0:^15}".format("*"))
    ## this is a T

def H():
    print("{0:^7}{0:>4}".format("*"))
    print("{0:^7}{0:>4}".format("*"))
    print("{0:^15}".format("********"))
    print("{0:^7}{0:>4}".format("*"))
    print("{0:^7}{0:>4}".format("*"))
    ## this is a H

def I():
    print("{0:>11}".format("********"))
    print("{0:^15}".format("*"))
    print("{0:^15}".format("*"))
    print("{0:^15}".format("*"))
    print("{0:>11}".format("********"))
    ## this is a I

def L():
    print("{0:^7}".format("*"))
    print("{0:^7}".format("*"))
    print("{0:^7}".format("*"))
    print("{0:^7}".format("*"))
    print("{0:>11}".format("********"))
    ## this is a L
    
def E():
    print("{0:>11}".format("********"))
   
    print("{0:^7}".format("*"))
    print("{0:>11}".format("********"))
    print("{0:^7}".format("*"))
    print("{0:>11}".format("********"))
    ## this is a E
def main():

    
    T()
    print()
    H()
    print()
    E()
    print()
    
    E()
    print()
    f()
    print()
    L()
    print()
    
    f()
    print()
    I()
    print()
    L()
    print()
    E()
    print()
    
    
main()

