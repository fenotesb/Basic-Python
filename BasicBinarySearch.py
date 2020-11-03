def binarySearch(list,key):
    highI=len(list)-1
    lowI=0
    located=False

    while lowI <= highI or located==False:
        middleI= int((highI+lowI)//2)

        if list[middleI]==key:
            located = True
            value= list.index(key)

        elif list[middleI]>key:
            highI=middleI-1

        else:
            lowI = middleI+1

        if located == True:
            return value
       

def main():
    infile= open("biglist.txt",'r')
    lists=infile.readline()
    number=lists.split()
    num = []
    count = 0 
    for i in number:
        num.append(int(i))
        count = 1 + count
    num.sort()
    key=num[len(num)//2]
    StartLookup= binarySearch(num,key)
    print(StartLookup)
main()
    


