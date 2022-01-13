<!-- Use uvicorn to start app -->
uvicorn api.main:app --reload

<!-- Create table on AWS console -->
Go to aws console, select dynamodb and create table named Orders

<!-- Enter api docs -->
http://127.0.0.1:8000/docs