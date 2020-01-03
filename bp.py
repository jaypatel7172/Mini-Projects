import math
#Initialize weight & bias
w=[]
n = int(input("Enter the no. of neuron in hidden layer"))
in1 = int(input("Enter the no. of neuron in Input layer"))
'''for i in range(n):
	inp = int(input("Enter the weights"))
	w.append(inp)'''
w = [-1,1,2]
w0 = [-1]
v = [[2,1,0],[1,2,3],[0,2,1]]
v0 = [0,0,-1]
x = [0.6,0.8,0]

#Calculate net input to hidden layer
zin = []
for i in range(in1):
	sum = v0[i]
	for j in range(n):
		sum = sum + (x[j]*v[i][j])   		 
	zin.append(sum)

z = []
for i in zin:
	t = 1 + math.exp(-i)
	zj = 1/ t
	z.append(zj)

#Calculate net input for output unit

yin = 0
sum = w0[0]
for j in range(n):
	sum = sum + (z[j]*w[j])  
yin = sum 		 
print(sum)
y = 0
t = 1 + math.exp(-i)
zj = 1/ t
z.append(zj)


