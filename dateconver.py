#DateConver.py

#Reads given number and converts it to month

def main():
    m="JanFebMarAprMayJunJulAugSepOctNovDec"
    
    lm= " ", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    
    d=input("What date in mm-dd-yy : ")
    
    mm=d[:2]
    
    dd=d[3:5]
    
    yy=d[6:8]
    
    n=int(mm)
    
    month= m[n*3-3:n*3]
    
    longmonth= lm[n]
    
    print(month+" "+dd+", 20"+yy)
    
    print(longmonth+" "+dd+", 20"+yy)
    
main()


