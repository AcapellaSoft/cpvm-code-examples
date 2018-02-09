import ap
p=print

# execute command and return cell with result
def exec(command, args):
	r = ap.tvm_new()
	ap.call('exec.py',{"cmd":command,"args":args , "R":r})
	return r
#print( ap.tvm_get( exec('pwd','')))


def extractPageFromDJVU(path, pagenum, image):
	args = ' -format=tiff  -page="'+str(pagenum)+'" '+path+' '+image
	#p('ddjvu',args)
	ok = exec( 'ddjvu',args )
	#p(ok, ap.tvm_get(ok))# cellid , result

def extractTextFromImage(imagepath, lang):
	args = imagepath+' stdout -l '+lang
	text = exec('tesseract', args)
	text = ap.tvm_get(text)
	#print(text)
	return text
	
extractPageFromDJVU('"/home/admin/Erlykin_L.A._Poslushnyy_metall-1974.djvu"', 90, '"/tmp/page090.tiff"')
#p(ap.tvm_get(exec('ls','/tmp/page090.tiff')))
text = extractTextFromImage("/tmp/page090.tiff",'rus')
t=text
print(t.encode().replace(b'\\\\',b'\\').decode('utf-8'))

import binascii
hex_data = binascii.hexlify(text.encode('ascii'))

f=open('/tmp/f','wb')
f.write(text.encode('utf-8'))
f.close()
