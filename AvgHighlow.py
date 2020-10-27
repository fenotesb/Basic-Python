#ProcessTemps.py
#Compute the average temperature and the high temperature
#for a month  from data stored in a file.
#Record the answers on the console. 

def main():
    #open the input file
    infile=open("Jan05temps.txt","r")

    #initialize some variables for computing the average
    count = 0
    sum = 0
    
    #Read first item from file and process it
    temp = int(infile.readline())  #read the first line
    high = temp    #the highest temperature so far
    count=count+1
    sum=sum+temp

    low = temp
    for line in infile:  #line will be one line of the
                         #infile, treated as a string
        temp=int(line)
        if temp>high:

           high = temp  #the highest temperature so far

        count=count+1
        sum=sum + temp
    
    infile.close()
    
    
    #compute average
    average=sum/count
    
    #print results to screen
    print("Average temperature: {0:.2f}".format(average))
    print("High temperature:", high)
   
    
    infile=open("Jan05temps.txt","r")

    low = int(infile.readline())

  
    
    for i in infile :
        if int(i) < low :
            low = int(i)
    print ("the Lowest temp is {0:.2f}".format(low))
    
        
    infile.close()
    #end of main    
        
      
    
main()    
