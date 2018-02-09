p = print

local body = ap.args["body"]
local notes = ap.args["notes"]
local images=ap.args["images"]

local index = ap.tvm_get(ap.args["index"])
--local index=100
local text = 'abc' -- test
local base64 = 'abcdef'

local newSection_x= [[<section><title>$title</title>
	<p><a l:href="#n_$index" type="note">original of page (Image scaned )</a></p>
	<p>$text</p>
</section>
]]
newSection_x = string.gsub(newSection_x, '$title', tostring('page #'..index) )
newSection_x = string.gsub(newSection_x, '$index', tostring(index) )
newSection_x = string.gsub(newSection_x, '$text',  text )
--p(newSection_x)

local newNote_x=[[<section id="n_$index"><p><image l:ref="$iid"></image></p>
</section>
]]
newNote_x = string.gsub(newNote_x, '$index', tostring(index))
newNote_x = string.gsub(newNote_x, '$iid', string.format("#i_%03d.jpg",index)  )
--p(newNote_x)

--image with id 
local newImage={xml='binary', id=string.format("i_%03d.jpg", index), ['content-type']="image/jpeg", base64}
local newImage_x=[[<binary id="$id" content-type="image/jpeg">
$base64
</binary>
]]
newImage_x = string.gsub(newImage_x, '$id', string.format("i_%03d.jpg", index)  )
newImage_x = string.gsub(newImage_x, '$base64', base64  )
--p(newImage_x)

body[index] 	= newSection_x
notes[index] 	= newNote_x
images[index] 	= newImage_x

