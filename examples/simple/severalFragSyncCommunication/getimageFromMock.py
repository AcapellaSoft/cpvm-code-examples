def fromapluafrag():
	import ap 
	print( 'ap=', dir(ap) ) # for info 
	
	r1 =   ap.tvm_new() # emul  uniq in transaction value cell id #'r1'
	print(r1)
	
	result = ap.call('_mock_base64Image.lua', {"R":r1}) # cell for result
	result = ap.tvm_get(r1) # read value puted by called frag 
	print('base64\n', result)
fromapluafrag()	
