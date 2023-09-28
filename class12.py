



"""Factprial program in python"""
""""""""""""""""""""""""""""""""
fact =1
Enter = int(input("Enter any number to find factorial"))
if Enter<0:
    print("Factorial is not for negative number")
elif Enter==0:
    print("fatorial of ",(Enter),"is",fact)
else:
 for i in range(1,Enter+1):
    fact =fact*i
print(fact)    

 