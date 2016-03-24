README.md

---------------
Obtaining a token
---------------
curl --data "username=haaroony&password=password123" http://127.0.0.1:8000/api-token-auth/


---------------
Calling a GET requires the following call, no authentication token is specified
---------------
curl -X GET http://127.0.0.1:8000/review/ -H ''


---------------
Posting information
---------------
Authorization: Token 19b1be0667189f0efd2d07b444d9c205ce444c09; 


curl -X POST http://127.0.0.1:8000/review/ -H "Authorization:Token 19b1be0667189f0efd2d07b444d9c205ce444c09" -H "Content-Type: application/json;" -d '
{
    "heading": "example",
    "body": "example2",
    "game": "Cubic Ninja",
    "rating": "0.5"
}' 