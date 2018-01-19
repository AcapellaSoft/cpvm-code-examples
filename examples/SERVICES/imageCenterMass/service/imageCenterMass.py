
def internalWork(URL): 
	
	from PIL import Image   # sudo pip3 install image
	import numpy as np

	im = None
	#im = Image.open('image.jpg')
	# OR 
	def pilImageFromURL(url):
		import urllib, requests
		from io import BytesIO
		response = requests.get(url)
		im = Image.open(BytesIO(response.content))
		return im
	# OR 
	def pilImageFromBase64(imageb64):
		import base64 
		decoded = base64.decodebytes(imageb64.encode('ascii'))
		print(decoded)
		import io
		im = Image.open(io.BytesIO(decoded))
		print(im)
		return im

	im = pilImageFromURL(URL)

	immat = im.load()
	(X, Y) = im.size
	m = np.zeros((X, Y))

	for x in range(X):
		for y in range(Y):
			m[x, y] = immat[(x, y)] > (250, 250, 250)
	m = m / np.sum(np.sum(m))

	# marginal distributions
	dx = np.sum(m, 1)
	dy = np.sum(m, 0)

	# expected values
	cx = np.sum(dx * np.arange(X))
	cy = np.sum(dy * np.arange(Y))

	# result of calulation
	print(cx,cy)
	return [cx,cy]

def http_response():
	import ap 
	import json
	url = 'https://'+ap.args['imagepath']
	print('DEBUG imagepath=', url )
	Ra = internalWork(url)
	obj_s = json.dumps({'cx':Ra[0], 'cy':Ra[1]})
	headers = {
		"imagepath-v": ap.args['imagepath']
	}
	ap.http.respond(201, obj_s, headers)

# uncomment before make it handler 
http_response()
