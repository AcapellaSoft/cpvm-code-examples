p=print

-- execute command and return cell with result
local function exec(command, args)
	local r = ap.tvm_new()
	ap.call('exec.py',{cmd=command,args=args , R=r})
	return r
end
--print( ap.tvm_get( exec('pwd', '')))


local function extractPageFromDJVU(path, pagenum, image)
	local args = ' -format=tiff  -page="'..tostring(pagenum)..'" '..path..' '..image
	--p('ddjvu',args)
	local ok = exec( 'ddjvu',args )
	--p(ok, ap.tvm_get(ok))# cellid , result
end 

local function extractTextFromImage(imagepath, lang)
	local args = imagepath..' stdout -l '..lang
	local text = exec('tesseract', args)
	local text = ap.tvm_get(text)
	--print(text)
	return text
end
	
extractPageFromDJVU('"/home/admin/Erlykin_L.A._Poslushnyy_metall-1974.djvu"', 90, '"/tmp/page090.tiff"')
--p(ap.tvm_get(exec('ls','/tmp/page090.tiff')))

text = extractTextFromImage("/tmp/page090.tiff",'rus')
p(text)

