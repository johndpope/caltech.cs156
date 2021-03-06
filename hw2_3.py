from numpy import *
from numpy.linalg import *

def sqrnorm(p):
	return [2.*(p[0]-0.5), 2.*(p[1]-0.5)]
def genPoint():
	return sqrnorm([random.random(), random.random()])
def genPoints(n):
	p = [None]*n
	for x in range(0, n):
		p[x] = genPoint()
	
	return p


def tolist(y):
	return array(y).reshape(-1,).tolist()


def lineTwoPoints(a, b):
	slope = (b[1]-a[1])/(b[0]-a[0])
	return [slope, a[1]-slope*a[0]]
def genLine():
	return lineTwoPoints(genPoint(), genPoint())

def evalFunction(l, p):
	if (l[0]*p[0]+l[1]) >= p[1]:
		return 1
	else:
		return -1

def above(w, x):
	if (w * transpose(x)).item() < 0.:
		return 1
	else:
		return -1

def calculateFracDiff(y, e):
	size = len(y)
	diff = 0
	eps = .001
	for i in range(size):
		# if (abs(y[i] - e[i])) > eps:
		# 	diff += 1
		if y[i] != e[i]:
			diff += 1
	return float(diff) / float(size)

def sign(x):
	if (x < 0.):
		return -1
	else:
		return 1


def f(x1, x2):
	#x1 = p[i][0]
	#x2 = p[i][1]
	return sign(x1**2+x2**2-0.6)

#Start Program

E = 100
cumdiff = 0.
for x in range(E):

	N = 1000
	p = genPoints(N)
	randm = random.randint(10)

	y = [None] * N

	#Generating y and Noise
	for i in range(N):
		pp = p[i]
		y[i] = f(pp[0], pp[1])
		if i%10==randm:
			y[i] *= -1

	#Prepend p with 1's
	for i in range(N):
		p[i] = [1] + p[i]

	X = matrix(p)

	w = pinv(X) * transpose(matrix(y))
	#print w
	#w = tolist(w)

	# if x == 0:
	# 	print X
	# 	print w

	diff = 0
	#Calculating Ein
	for i in range(N):
		pp = p[i]
		first = f(pp[1], pp[2])
		second = sign((transpose(w) * transpose(matrix(p[i]))).item())
		#print first
		#print second
		if (first != second):
			diff += 1

	#print diff

	cumdiff += float(diff)/float(N)

print float(cumdiff)/float(E)

#.51565