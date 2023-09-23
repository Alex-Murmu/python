# Python operator
"""
operator    name       example
 +         addition      X+y  
 -        subtraction    x-y
 *       multiplication  x*y
 /         division      x/y
 %         modulus       x%y remainder
 **      Exponentiation  x**y  power
 //      Floor Division  x//y  
"""
# Creating variable
x = 5
y = 6
#addition
add =x+y
print("sum of ",(x),"and",(y),"is",add,type(add))
 
#Subtraction
sub =x-y
print("Subtraction of ",x,"AND",y,"is",sub,type(sub))

#multiplication
mul =x*y
print("multiplication of",x,"and",y,"is",mul,type(mul))

#division
div =x/y
print("Div of ",x,"and",y,"is",div,type(div))

 #modulus gives U remainder
modu =x%y
print("Mod of",x,"and",y,"is",modu,type(modu))

#Exponentiation gives u (x pe power y)
Exp =x**y
print("Exponentiation of",x,"and",y,"is",Exp,type(Exp))

#Floor division
fldiv =x//y
print(fldiv)