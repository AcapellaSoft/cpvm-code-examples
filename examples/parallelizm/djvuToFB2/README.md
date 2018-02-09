# convert djvu book to fb2 with text recognition and add image for read original text if text not correct

problem : 

**perfomance** of sequentional convetation and text recognition **are low.** 

**cpvm can scale process of convertation** 

## environment prepare 

```	
	sudo apt-get install python-opencv libopencv-dev python-numpy python-dev

	luarocks install penlight
	luarocks install xml
	sudo apt-get install imagemagick # convert
```

Setup enironment for snapshot : build Dockerfile

TODO 

## main process 

internal main function call example 

```lua
djvuToFB2(	'"/home/pavlov/Загрузки/знай_и_умей_[tfile.ru]/Якуб С.К. - Вспомним забытые игры (Знай и умей) - 1988.djvu"', 
			'Якуб С.К. - Вспомним забытые игры (Знай и умей) - 1988')
```

then loop page by page : 

```lua
		extractPageFromDJVU(djvu, i, image) 
		bookAppendScanedPage(book, i, image)	
```

every page can to be converted independently
