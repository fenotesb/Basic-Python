def func1():
    print("{0:>5}".format("-----"))
1
def func2(turn):
    if turn == 1:
        BorW= "W"
    elif turn == -1:
        BorW= "B"
    print("{0}----".format(BorW))
    
def func3(turn):
    if turn == 1:
        BorW= "W"
    elif turn == -1:
        BorW= "B"
    print("----{0}".format(BorW))
def func4():
    print("|   |")
    print("|   |")
def bord (player,corner):

    if corner == "A":
        func2(player)
        func4()
        func1()
    elif corner == "B":
        func3(player*-1)
        func4()
        func1()
    elif corner == "C":
        func1()
        func4()
        func2(player)
    else:
        func1()
        func4()
        func3(player*-1)
    print()
def main():
    player= eval(input("choice 1 or -1: "))
    c= input("choice a corner (A,B,C,D): ")
    corner = c.upper()
    bord(player,corner)
    player= eval(input("choice 1 or -1: "))
    c= input("choice a corner (A,B,C,D): ")
    corner = c.upper()
    bord(player,corner)
    player= eval(input("choice 1 or -1: "))
    c= input("choice a corner (A,B,C,D): ")
    corner = c.upper()
    bord(player,corner)
    player= eval(input("choice 1 or -1: "))
    c= input("choice a corner (A,B,C,D): ")
    corner = c.upper()
    bord(player,corner)
  
    
main()
