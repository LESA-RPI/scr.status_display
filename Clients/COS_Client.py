from Client_util import *

## Dummy code for reading raw color sensor data and converting the 
#  RGB values to sRGB gammets for the status screen

def getRGB():
	all_data = cos_control.read_all()
	
	sRGB = []
	for r in range(53):
		RGB = all_data[r][0:3]
		XYZ = Calibrate_r(RGB)
		sRGB_temp = makeRow(XYZ2sRGB(XYZ))
		sRGB_temp = [min(1, x/200) for x in sRGB_temp]
		sRGB.append(sRGB_temp)
	
	return send_COS_status(sRGB)

##############################################

def Calibrate_r(RGB):

	C5 = [[ 0.0687,  0.0101, -0.0136],
		  [ 0.0308,  0.0583, -0.0268],
		  [-0.0023, -0.0130,  0.0620]]

	XYZ = (np.matmul(C5, makeColumn(RGB))).tolist()
	return XYZ

##############################################

def xy2XYZ(xyL):

	x = xyL[1]
	y = xyL[2]
	L = xyL[3]

	Y = L
	Z = L * ((1-x-y) / y)
	X = (x / (1-x)) * (L+Z)
	XYZ = [X, Y, Z]

	return XYZ

##############################################

def XYZ2sRGB(XYZ):

	M = [[ 3.2410, -1.5374, -0.4986],
		 [-0.9692,  1.8760,  0.0416],
		 [ 0.0556, -0.2040,  1.0570]]

	sRGB = (np.matmul(M, XYZ)).tolist()
	sRGB = [max(0, x) for x in sRGB]

	return sRGB

##############################################

def XYZ2xy(XYZ):

	x = XYZ[1] / sum(XYZ)
	y = XYZ[2] / sum(XYZ)
	xy = [x, y]

	return xy

##############################################
def send_COS_status(input):

	A, B, C = [], [], []
	for i in range(3):
		A.append(np.zeros(70))
		B.append(np.zeros(53))
		C.append(np.zeros((5,14)))
	data = np.zeros((5,14,3))

	for i in range(53):
		for j in range(3):
			B[j][i] = input[i][j]

	I = [7,9,17,18,19,27,29,37,38,39,42,44,53,57,59,62,64] 
	k, j = 0, 0
	while(k < 70):
		if not k in I:
			for i in range(3):
				A[i][k] = B[i][j]
			j = j+1
		k = k+1

	for i in range(3):
		A[i] = np.reshape(A[i], [5, 14], 'F')
	
	for i in range(5):
		for j in range(3):
			zx, zy = [], []
			for x in range(len(A[j][i])):
				if A[j][i][x] != 0:
					zx.append(x)
					zy.append(A[j][i][x])
			C[j][i] = np.interp(range(14), zx, zy)
	

	for i in range(5):
		for j in range(14):
			for k in range(3):
				data[i][j][k] = C[k][i][j]

	# Organize Rows
	data = data.tolist()
	data.append(data[0])
	data.pop(0)
	return data

##############################################

def makeColumn(m):
	out = []
	for i in m:
		out.append([i])
	return out

def makeRow(m):
	out = []
	for i in m:
		out.append(i[0])
	return out

if __name__ == "__main__":
    while True:
    	post_request('Status_COS', {"data": getRGB()})
        time.sleep(1)