##  one fragment call other as *mock*

simple example of sync call and usetvm as buffer between fragments 

1. fragment ```getimageFromMock.py``` prapare tvm cell for comunication
2. fragment ```getimageFromMock.py```  **call** ``_mock_base64Image.lua```  
3. fragment ``_mock_base64Image.lua```  **put to tvm cell** base64 value - encoded image 
4. fragment ```getimageFromMock.py```  **read value from tvm cell**


## how to start 

install acapella_cli - paas command line interface 

and 

just ```./start.sh```


