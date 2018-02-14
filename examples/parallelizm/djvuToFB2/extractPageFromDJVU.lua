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
	local args = imagepath..' '..imagepath..'.txt '..' -l '..lang
	local text = exec('tesseract', args)
	--local text = ap.tvm_get(text)

	local open = io.open

	local function read_file(path)
		local file = open(path, "rb") -- r read mode and b binary mode
		if not file then return nil end
		local content = file:read "*a" -- *a or *all reads the whole file
		file:close()
		return content
	end
	
	--print(imagepath..'.txt')
	text = read_file(imagepath..'.txt')
	--print(text)
	
	exec('rm', imagepath)
	exec('rm', imagepath..'.txt')
	
	return text
end
	
extractPageFromDJVU('"/home/admin/Erlykin_L.A._Poslushnyy_metall-1974.djvu"', 90, '"/tmp/page090.tiff"')
--p(ap.tvm_get(exec('ls','/tmp/page090.tiff')))

text = extractTextFromImage("/tmp/page090.tiff",'rus')
p(text)


