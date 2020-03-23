import math

# because we used import access methods by referencing the module

print("ceil(4.4) = ", math.ceil(4.4))
print("floar(4.4) = ", math.floor(4.4))
print("fabs(4.4) = ", math.fabs(4.4))
#Factorial = 1*2*3*4 = 24
print("factorial(4) = ", math.factorial(4))
#Return remainder of divison
print("fmod(4) = ", math.fmod(5,4))
#Received a float and return a int
print("Trunc(4.5) = ", math.trunc(4.5))
print("pow(4,6) = ", math.pow(4,6))
#Return the square root
print("sqrt(4) = ", math.sqrt(4))
#Special Value
print("math.e(4) = ", math.e)
print("math.pi(4) = ", math.pi)
# Return e^x
print("exp(4) = ", math.factorial(4))
#Return the natural logarithm e*e*e ~= 20 so long()20 tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))
#we can do define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000,10))

#we can also define the base and 10 like this
print("log10(1000,10) = ", math.log10(1000))

# Functions available sin,cos,tan,asin,acos,atan,atan2,asonh,acosh,atanh,sinh,cosh,tanh
#convert radians to degrees and vice versa
print("degrees(1,5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
print("factorial(4) = ", math.factorial(4))

####Decimal Module
from decimal import Decimal as D

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")



