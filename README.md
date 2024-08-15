# Backend clone of social media app by using FastAPI 

This repository contains a code for simple backend actions we perform in social media like sign up, password authentication, posting posts, etc.

## Routes It has

## 1 Auth Route
This route is responsible for registration and authentication of users.

## 2. Posts Route
This route is responsible for creatting a post, deleting a post, updating a post, getting a post by id.

## 3. Users Route
This route is responsible for creating a user and getting a user by id.

## 4. Votes Route
This route is responsible for upvoting and downvoting 


# To run locally
clone this repo first on your local machine
```

git clone https://github.com/N-ADITHYA/fastapi-project.git

```
then move to fastapi-project
```

cd fastapi-project

```
Then install fastapi library using the following command, It installs everything you might potentially need to work with FastAPI

```

pip install fastapi[all]

```
then run the following command to run it on your local machine

```

uvicorn main:app --reload

```

Then you can use this by going to your localhost

```

http://127.0.0.1:8000

```

add /docs to the url you got to see the fastpi swagger to actually work on it

```

http://127.0.0.1:8000/docs

```

# To proceed ahead you need to set up postgres on your machine
Create a database on postgres on your local machine. 

After this create a file called **.env** in your folder.
This should contain the following information

```

DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = passward_that_you_set
DATABASE_NAME = name_of_your_database
DATABASE_USERNAME = user_name
SECRET_KEY = f384a2c9d765431b8e0f92d3456789ab 
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 60(base)

```
### NOTE: The above SECRET_KEY is a pseudo key, Refer FastAPI documentation to generate your new SECRET_KEY.

