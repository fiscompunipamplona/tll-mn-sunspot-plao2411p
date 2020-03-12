from pylab import plot, show, xlim, ylim
from numpy import linspace, sin, loadtxt, zeros
b= loadtxt ("sunspots.txt",float)
#print(b[0:1000,0])
print(len(b[0:1000,0]))
#print(b[:,1])
ra=zeros(1005,float)
p=5
for i in range(1000):
    ra[i+5]+=b[p,1]
    for j in range(1,6,1):
        ra[i+5]+=b[p-j,1]+b[p+j,1]
    ra[i+5]=ra[i+5]/11
    p+=1


plot(b[0:1000,0],b[0:1000,1])
plot(b[0:1000,0],ra[5:1005])

show()
