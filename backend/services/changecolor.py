import cv2
import math

import services.color_definition as colordef
import services.utils as utils

def translate():
	image = cv2.imread("media/test7.jpg")

	mask = cv2.imread("media/mask7_7.png")
	# lab = colordef.rgb2lab(255,0,0)
	col1 =[[ 2.193387968190372, 0.0002984078976697724, -0.0005904407270940215 ],
		[ 43.28113743863315, 17.010338403243676, -11.203441349943288 ],
		[ 61.023910964714545, 17.312836785774167, -27.031810519097288 ],
		[ 66.62935465662024, 8.017241296791045, -9.420517918338845 ],
		[ 84.30989530835596, 10.160658898221598, -12.533152005355408 ],
		[ 87.02762812118554, 6.802082882229444, 10.202105360212798 ]]


	col2 = col1.copy()
	col2[0] =False
	col2[1]=[ 43.28113743863315, 17.010338403243676, -11.203441349943288 ]
	col2[2]=[ 72.00426057330887, 50.357464261422734, -9.342869183525004 ]
	col2[3]=[72.00426057330887, 8.017241296791045, -9.420517918338845 ]
	col2[4]=[84.30989530835596, 10.160658898221598, -12.533152005355408 ]
	col2[5]=[ 87.02762812118554, 6.802082882229444, 10.202105360212798 ]

	# print(col2)
	K =5

	outim = colorTransform(col1,col2,image,K,mask)
	# outim = colorTransform_test(col1,col2,image,K)
	cv2.imwrite("./media/output_colorch.jpg",outim)
	
	return outim


def colorTransform(colors1, colors2,img,K,mask):
	L1 = [0]
	L2 = [0]
	# print(img.shape)
	for i in range (K):
		L1.append(colors1[i+1][0])
		L2.append(colors2[i+1][0])
	L1.append(100)
	L2.append(100)
	l = img.shape
	out_array = img.copy()

	cs1 = []
	cs2 = []
	k = 0
	for i in range(K + 1):
		# print(colors2[i])
		if (colors2[i] != False):
			cs1.append(colors1[i])
			cs2.append(colors2[i])
			k+=1
	sigma = utils.getSigma(colors1,K)
	lambda_v = utils.getLambda(cs1,sigma,K)
	for i  in range(img.shape[0]):
		for j in range(img.shape[1]):
			m = mask[i][j][0]
			B,G,R= img[i][j]
			Lab = colordef.rgb2lab(R, G, B)
			out_lab = [0, 0, 0]


			L = colorTransformSingleL(Lab[0],L1,L2,m)
			# print(L)

			
			for p in range(k):
				v = colorTransformSingleAB([cs1[p][1], cs1[p][2]], [cs2[p][1], cs2[p][2]], Lab[0], Lab,m)
				v[0] = L

				#ここから調査
				omega = utils.omega(cs1, Lab, p,lambda_v,sigma)
				v = utils.sca_mul(v, omega)

				out_lab = utils.add(out_lab, v)
					
			out_rgb = colordef.lab2rgbInout(out_lab)
			if(colordef.isOutRGB(out_rgb)):
				out_rgb= colordef.cliping(out_rgb)
			out_array[i][j][2] = out_rgb[0]
			out_array[i][j][1] = out_rgb[1]
			out_array[i][j][0] = out_rgb[2]
	return out_array


def colorTransform_test(colors1, colors2,img,K):
	L1 = [0]
	L2 = [0]
	# print(img.shape)
	for i in range (K):
		L1.append(colors1[i+1][0])
		L2.append(colors2[i+1][0])
	L1.append(100)
	L2.append(100)
	l = img.shape
	out_array = img.copy()

	cs1 = []
	cs2 = []
	k = 0
	for i in range(K + 1):
		# print(colors2[i])
		if (colors2[i] != False):
			cs1.append(colors1[i])
			cs2.append(colors2[i])
			k+=1
	sigma = utils.getSigma(colors1,K)
	lambda_v = utils.getLambda(cs1,sigma,K)
	
	B,G,R= img[400][250]
	# B =50
	# G = 30
	# R =18
	Lab = colordef.rgb2lab(R, G, B)
	out_lab = [0, 0, 0]
	L = colorTransformSingleL(Lab[0],L1,L2)
	# print(L)
	for p in range(k):
		v = colorTransformSingleAB([cs1[p][1], cs1[p][2]], [cs2[p][1], cs2[p][2]], Lab[0], Lab)
		v[0] = L
		#ここから調査
		omega = utils.omega(cs1, Lab, p,lambda_v,sigma)
		v = utils.sca_mul(v, omega)
		# print(v)
		out_lab = utils.add(out_lab, v)
		print(out_lab)
	out_rgb = colordef.lab2rgbInout(out_lab)
	print(out_lab)
	print(out_rgb)
	return out_array

def colorTransformSingleL(l,L1,L2,mask):

	for i in range(len(L1)):
		if ((l >= L1[i] )and (l <= L1[i + 1])):
			break
	if (mask==0):
		ratio =1
	else:
		ratio =1
	l1 = L1[i]
	l2 = L1[i + 1]
	if(l1 == l2):
		 s= 1
	else:
		 s = (l - l1) / (l2 - l1)
	L1 = L2[i]
	L2 = L2[i + 1]
	L = (L2 - L1) * s*ratio + L1
	return L


def colorTransformSingleAB(ab1, ab2, L, x,mask):
	if (mask==0):
		ratio=1.0
	else:
		ratio=0.5

	color1 = [L, ab1[0], ab1[1]]
	color2 = [L, ab2[0], ab2[1]]
	
	color2 = vectAdjust(color1,color2,ratio)
	if (utils.distance2(color1, color2) < 0.0001):
		return color1

	
	d = utils.sub(color2, color1)
	# print(d)
	x0 = utils.add(x, d)
	Cb = colordef.labIntersect(color1, color2)

	if (colordef.isOutLab(x0)):
		xb = colordef.labBoundary(color2, x0)
	else: 
		xb = colordef.labIntersect(x, x0)

	dxx = utils.distance2(xb, x)
	dcc = utils.distance2(Cb, color1)
	l2 = min(1, dxx / dcc)
	xbn = utils.normalize(utils.sub(xb, x))
	x_x = math.sqrt(utils.distance2(color1, color2) * l2)
	return utils.add(x, utils.sca_mul(xbn, x_x))

def vectAdjust(vec1,vec2,ratio):
	d = utils.sub(vec2,vec1)
	for i in range(len(d)-1):
		d[i+1] = d[i+1]*ratio
	res_vec = utils.add(vec1,d)

	return res_vec

