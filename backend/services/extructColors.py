import cv2
import math
import services.color_definition as colordef
import services.utils as utils
import numpy as np


def extruct():

	bin_range = 16
	bin_size = 256 / bin_range
	channels = 4
	img_path = "./media/test2.jpg"
	img = cv2.imread(img_path)
	K = 5
	bin_idx =np.zeros((bin_range,bin_range,bin_range))
	bins = bin_value_calulate(bin_range,bin_size)
	bins_count = bin_count(bin_range,img)
	Labs,RGBs = kmeans(bin_size,bin_range,bins,bins_count,bin_idx,K)

	outim = generate_color_palette(RGBs)
	cv2.imwrite("./media/output_palette.jpg",outim)


	return outim

def generate_color_palette(RGBs):
	size = (512,512,3)
	res = np.full(size,255,np.uint8)
	rectsize = 512//len(RGBs)


	for i,RGB in enumerate(RGBs):
		cv2.rectangle(res,(rectsize*i,200),(rectsize*(i+1)-10,300),RGB,-1)
		# cv2.rectangle(res,(384,0),(510,128),(0,255,0),3)
	return res




def bin_value_calulate(bin_range,bin_size):
	# bins = [[[[0]*3]* bin_range]*bin_range]*bin_range 
	bins = np.zeros((bin_range,bin_range,bin_range,3))
	# print(bins.shape)
	# bins = [[0]* 3]*bin_range 
	for i in range(bin_range):
		for j in range(bin_range):
				for k in range(bin_range):
					color =(i + 0.5) * bin_size, (j + 0.5) *bin_size, (k + 0.5) * bin_size
					L,a,b = colordef.rgb2lab(color[0],color[1],color[2])
					# print(bins[i][j][k])
					bins[i][j][k] = (L,a,b)
			
	return bins

def bin_count(bin_range,img):
	bin_count =np.zeros((bin_range,bin_range,bin_range))
	height,width,_ = img.shape
	# print(img.shape)
	for i in range(height):
		for j in range(width):
			# print(math.floor(img[i][j]/bin_range))
			b = img[i][j]/bin_range
			b = b.astype(int)
			# print(b[0])
			
			bin_count[b[0]][b[1]][b[2]]+=1
			# print(bin_count)

	return bin_count


def kmeansFirst(bin_size,bin_range,bins_color,bins_count,K):
	centers = []
	centers_lab = []
	centers.append([bin_size / 2,bin_size / 2,bin_size / 2])
	r,g,b=centers[0]
	centers_lab.append(colordef.rgb2lab(r,g,b))
	bins_copy = []

	for p in range(K):
		maxc = -1
		for i in range(bin_range):
			for j in range(bin_range):
				for k in range(bin_range):
					d2 = utils.distance2(bins_color[i][j][k], centers_lab[p])
					fact = 1 - math.exp(-d2 / 6400)
					# print(bins_count[i][j][k])
					bins_count[i][j][k] = fact*bins_count[i][j][k]
					if (bins_count[i][j][k] > maxc):
						maxc = bins_count[i][j][k]
						tmp = []	
						tmp.append(bins_color[i][j][k])
		centers.append(tmp)
		# print(centers)
		r,g,b=tmp[0]

		centers_lab.append(colordef.rgb2lab(r,g,b))
	return centers_lab

def kmeans(bin_size,bin_range,bins,bins_count,bin_idx,K):
	centers = kmeansFirst(bin_size,bin_range,bins,bins_count,K)
	# print(centers)
	centers = np.array(centers)
	no_change = False
	while (not(no_change)):
		no_change = True

		# sum = []
		color =np.zeros((K,3))
		count =np.zeros((K))


		

		for i in range(bin_range):
			for j in range(bin_range):
				for k in range(bin_range):
					if (bins_count[i][j][k] == 0):
						continue

					lab = bins[i][j][k]
					c =bins_count[i][j][k]
					mind = float('inf')
					mini = -1
					for p in range(K):
						d = utils.distance2(centers[p], lab)
						if (mind > d):
							mind = d
							mini = p
					if (mini != bin_idx[i][j][k]):
						bin_idx[i][j][k] = mini
						no_change = False
					m = utils.sca_mul(lab,c)
					# print(m)
					color[mini] = utils.add(color[mini], m)
					count[mini] += c

		# print(color)
		for i in range(K):
			if (count[i]):
				for j  in range(3):
					# print(color[i][j]/count[i], centers[i][j])
					centers[i][j] = color[i][j] /count[i]
	# print(centers)
	# centers = utils.sort(centers)
	centers_rgb = []
	for i in range(K):
		centers_r,centers_g,centers_b=centers[i]
		centers_rgb.append(colordef.lab2rgb(centers_r,centers_g,centers_b))
	
	print(centers)
	return centers,centers_rgb

