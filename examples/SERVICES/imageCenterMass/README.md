## Calculate the cener  mass of figure in cpvm acapella paas cloud 

* Service - source of code fragment , handler registration script , meta of service 
* client - script for request of service by ```curl```


input image : ![](https://n6-img-fp.akamaized.net/free-icon/crescent-moon_318-35328.jpg)
or 
![](https://n6-img-fp.akamaized.net/free-icon/horse-ride_318-104190.jpg)

call the service 

```bash 
#URL="image.freepik.com/free-icon/moon-phase-black-crescent-shape_318-69954.png"
URL="n6-img-fp.akamaized.net/free-icon/crescent-moon_318-35328.jpg"
#URL="n6-img-fp.akamaized.net/free-icon/horse-ride_318-104190.jpg"

curl -v -X POST http://api.acapella.ru:5678/io/pavlovma007/my/imageCenterMass?imagepath=$URL
```


result : 
```bash 
$ ./red_button.sh 
* Hostname was NOT found in DNS cache
*   Trying 188.120.224.221...
* Connected to api.acapella.ru (188.120.224.221) port 5678 (#0)
> POST /io/pavlovma007/my/imageCenterMass?imagepath=n6-img-fp.akamaized.net/free-icon/crescent-moon_318-35328.jpg HTTP/1.1
> User-Agent: curl/7.35.0
> Host: api.acapella.ru:5678
> Accept: */*
> 
< HTTP/1.1 201 Created
< imagepath-v: n6-img-fp.akamaized.net/free-icon/crescent-moon_318-35328.jpg
< Access-Control-Allow-Origin: *
< content-length: 51
< connection: keep-alive
< 
* Connection #0 to host api.acapella.ru left intact
{"cx": 367.97130998571424, "cy": 256.8033542126325}m
```

[link to source](https://github.com/AcapellaSoft/cpvm-code-examples/blob/master/examples/SERVICES/imageCenterMass/service/imageCenterMass.py)
