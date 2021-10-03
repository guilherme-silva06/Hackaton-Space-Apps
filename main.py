from statistics import mean

#Here we have the lists
#x1 and x2 stands for the coordenates of a place where you took the sample of water
#y stands for the concentration of plastic in a determined amount of water
#The idea is to get a huge database of locations and their respective concentration of plastic, in order to quantify/predict marine debris in water

#You would have to connect this to your database, or Excel spreadcheet, and then the program would calculate and generate 
# a equation to predict, monitor and quantify plastic concentration in water

#if you want to try, you can use this values for tests
#x1 = [3,1,3,1,3,13]
#x2 = [2,3,31,3,13,3]
#y = [0.9,4,3,1,3,2]

x1 = [] #x1 is your array of latitude
x2 = [] #x2 is your array of longitude
y = [] #y is your array of concentration

#Getting the mean of the lists
Mx1 = mean(x1)
Mx2 = mean (x2)
My = mean(y)


def tss(xs):   #Function to define the Total sum of squares
    m = sum(xs) / len(xs)
    return sum((x - m)**2 for x in xs)


n = len(x1) 
o = len(x2)
p = len(y)

#Starting the variables of the sum of products
Spx1x2 = 0 
Spx1y = 0
Spx2y = 0

for i in range(n): #Getting the Sum of products beetween x1 and x2
    Spx1x2 += ((x1[i] - Mx1) * (x2[i] - Mx2))

for i in range(n): #Getting the Sum of products beetween x1 and y
    Spx1y += ((x1[i] - Mx1) * (y[i] - My))

for i in range(n): #Getting the Sum of products beetween x2 and y
    Spx2y += ((x2[i] - Mx2) * (y[i] - My))

Sx1 = (sum(x1)) 
Sx2 = (sum(x2)) # Getting the sum of squares of x2
Sy = (sum(y)) 

Sq1 = tss(x1) # Getting the sum of squares of x1
Sq2 = tss(x2) # Getting the sum of squares of x2

#We'll follow this linear regression with multiple features equation:  y = a1x1 + a2x2 + b

a1 = ((Spx1y * Sq2) - (Spx1x2 *Spx2y)) / ((Sq1*Sq2)-(Spx1x2*Spx1x2)) #Getting the value of a1 based in your dataset
a2 = ((Spx2y * Sq1) - (Spx1x2 *Spx1y)) / ((Sq1*Sq2)-(Spx1x2*Spx1x2)) #Getting the value of b based in your dataset
b = My - (a1*Mx1) - (a2*Mx2) #Getting the value of b

#Printing the equation
print('y =',a1,'*x1 +',a2,'*x2 +', b)
