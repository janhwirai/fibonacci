n= int(input ("Enter number"))  
n_1 = 0  
n_2 = 1  
count = 0  
if n <= 0:  
    print ("Given number is not valid!")  
elif n == 1:  
    print ("The Fibonacci sequence of the numbers up to", n, ": ")  
    print(n_1)   
else:  
    print ("The fibonacci sequence is:")  
    while count < n:  
        print(n_1)  
        nth = n_1 + n_2  
        n_1 = n_2  
        n_2 = nth  
        count += 1  