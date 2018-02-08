#!/usr/bin/python3
## автоматически получить контур изображения

# https://hub.docker.com/r/elenaalexandrovna/opencv-python3/~/dockerfile/
#sudo pip3.4 install matplotlib
#sudo apt-get install python3.4-tk

def internalWork(imagePath):
	import numpy as np
	import cv2
	
	def auto_canny(image, sigma=0.33):
		# compute the median of the single channel pixel intensities
		v = np.median(image)

		# apply automatic Canny edge detection using the computed median
		lower = int(max(0, (1.0 - sigma) * v))
		upper = int(min(255, (1.0 + sigma) * v))
		edged = cv2.Canny(image, lower, upper)

		# return the edged image
		return edged
	
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (3, 3), 0)

	# apply Canny edge detection using a wide threshold, tight
	# threshold, and automatically determined threshold
	wide = cv2.Canny(blurred, 10, 200)
	tight = cv2.Canny(blurred, 225, 250)
	auto = auto_canny(blurred)

	#show the images
	#cv2.imshow("Original", image)
	#cv2.imshow("Edges", np.hstack([wide, tight, auto]))
	#cv2.waitKey(0)

	#SHOW NOW NOT NEED, disable it
	#import matplotlib.pyplot as plt
	##import matplotlib.image as mpimg
	#imgplot = plt.imshow(auto)
	#plt.show()

	# WRITE TO LOCAL paas disk 
	#cv2.imwrite("/tmp/wide.jpg", wide)
	#cv2.imwrite("/tmp/tight.jpg", tight)
	#cv2.imwrite("/tmp/auto.jpg", auto)
	
	return auto, wide, tight
	
def acapella():
	import ap 
	import cv2
	
	#privaryKey = ap.args['imgKV']
	kvUrl='http://api.acapella.ru:5678/acapelladb/v2/kv/keys/pavlovma007:temp:image?&n=3&r=2&w=2'
	       
	imagedataCell=ap.new_io('{"command":"kv"}' , kvUrl)
	print('imagedataCell', imagedataCell)
	print('imagedataCell value=',ap.tvm_get(imagedataCell))
	
	#auto, wide, tigth = internalWork('/tmp/image.png')	

	## WAIT CUSTOM LOGS MERGE 
	##def imagetostream(img,stream):
	##	ret, buf = cv2.imencode('.jpeg', img)
	##	import base64
	##	auto_s = base64.b64encode(buf)
	##	stream.write(auto_s.decode('ascii'))
	##imagetostream(auto, ap.create_log("auto", scope = "transaction") )
	##imagetostream(tight, ap.create_log("tight", scope = "transaction"))
	##imagetostream(wide,  ap.create_log("wide",  scope = "transaction"))
	
	#ret, buf = cv2.imencode('.jpeg', auto)
	#import base64
	#auto_s = base64.b64encode(buf)	
	#print(auto_s.decode('ascii'))
	
	ap.io_commit()
	
acapella()
