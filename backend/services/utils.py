import math
import numpy as np 

def distance2(c1, c2):
	res = 0
	# print("c1: ",c1)
	# print("c2: ",c2)
	for i in range(len(c1)):
		res += (c1[i] - c2[i]) * (c1[i] - c2[i])
	return res

def normalize(v):
	d = math.sqrt(distance2(v, [0, 0, 0]))
	res = []
	for i  in range(len(v)):
		res.append(v[i] / d)
	return res

def add(c1, c2):
	res = []
	for i in range(len(c1)):
		res.append(c1[i] + c2[i])
	return res

def sub(c1, c2):
	res = []
	for i in range(len(c1)):
		res.append(c1[i] - c2[i])
	return res

def sca_mul(c, k):
	res = []
	for i  in range(len(c)):
		res.append(c[i] * k)
	return res




def sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j] >= lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def omega(cs1, Lab, i,lambda_value,sigma):
	s = 0
	for j in range(len(cs1)):
		s += lambda_value[j][i] * phi(math.sqrt(distance2(cs1[j], Lab)),sigma)
	return s

def getLambda(cs1,sigma,k):
	s = []
	for p in range(k):
		tmp = []
		for q in range(k):
			tmp.append(phi(math.sqrt(distance2(cs1[p], cs1[q])),sigma))
		s.append(tmp)
	lambda_value = np.linalg.inv(s)
	return lambda_value

def phi(r,sigma):
	return math.exp(-r * r / (2 * sigma * sigma))

def getSigma(colors,K):
	s = 0
	for i  in range(K+1):
		for j  in range(K+1):
			if (i == j):
				continue
			s += math.sqrt(distance2(colors[i], colors[j]))
	return s/ (K * (K + 1))


