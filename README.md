README.md

------------
Registration 
------------

Login 	 : haaroony	
Password : password123 

---------------
Obtaining an authorization token
---------------
curl --data "username=haaroony&password=password123" http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/api-token-auth/

---------------
Calling a GET requires the following call, 
no authentication token is required
---------------
curl -X GET http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/users/ -H ''
curl -X GET http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/review/ -H ''
curl -X GET http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/videogames/ -H ''
curl -X GET http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/genres/ -H ''
curl -X GET http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/platform/ -H ''
curl -X GET http://videogames-haaroony.apps.devcloud.eecs.qmul.ac.uk/developer/ -H ''

---------------
Calling a POST requets requires an authorization token
---------------
e.g. posting a review

curl -H "Authorization:Token fa3893f7bda91ae3dff7dbd4acfae4ed9f1a18d2" -H "Content-Type:son" -X POST -d '{"heading":"test","body":"test","game":{"title":"Cubic Ninja"},"rating":"2"}' http://127.0.0.1:8000/review/


Different renderes installed
XML renderer  - 	pip install djangorestframework-xml
YAML renderer - 	pip install djangorestframework-yaml
JSONP Renderer - 	pip install djangorestframework-jsonp
CSV Renderer - 		pip install djangorestframework-csv
Swagger api - 		pip install django-rest-swagger

