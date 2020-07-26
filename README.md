# MovieMaster

### Description

RESTful API for movies (like IMDb)

There are 2 levels of access to APIs:
1. __Admin__: 
    * Add
    * Remove 
    * Edit 
2. __User__: 
    * View
    * Search

### APIs

1. User Credential API

HTTP Method | URI | Action
----------- | --- | ------
POST | https://[hostname]/registration | User registration
POST | https://[hostname]/login | User login
GET | https://[hostname]/users | Get list of all users
DELETE | https://[hostname]/users | Delete all users

2. Movies API

HTTP Method | URI | Action | Access
----------- | --- | ------ | ------
GET | https://[hostname]/movie/search/[name] | Search movie (supports substring) | User, Admin
GET | https://[hostname]/movies | List of all movies | User, Admin
POST | https://[hostname]/movies | Create new movie | Admin
PUT | https://[hostname]/movie/[id] | Update movie details | Admin
DELETE | https://[hostname]/movie/[id] | Remove movie | Admin

### Usage

1. Register a new user using registration API
```
curl --location --request POST 'https://mov1e-master.herokuapp.com/registration' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "user",
    "password": "user",
    "is_admin": false
}'
```

2. Login with registered credentials
```
curl --location --request POST 'https://mov1e-master.herokuapp.com/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "admin"
}'
```

3. Retrieve access_token from response
4. Add access_token as Authorization Header to use mentioned APIs
```
curl --location --request POST 'https://mov1e-master.herokuapp.com/movies' \
--header 'Authorization: Bearer [ACCESS_TOKEN]' \
--header 'Content-Type: application/json' \
--data-raw '{
		"99popularity":68,
		"director":"GeorgeLucas",
		"genre":[
			"Drama",
			"Mystery",
			"Sci-Fi",
			"Thriller"
		],
		"imdb_score":6.8,
		"name":"THX1138"
	}'
```

### Request Payload Body Format

1. User Registration "POST /registration"

```
{
  "username": [string],
  "password": [string],
  "is_admin": [boolean]
}
```

2. User Login "POST /login"

```
{
  "username": [string],
  "password": [string]
}
```

3. Add movie "POST /movies" & Update Movie "PUT /movie/[id]
```
{
  "99popularity": [integer],
  "director": [string],
  "genre": [List[string]],
  "imdb_score": [Decimal],
  "name": [string]
}
```


__URL__: https://mov1e-master.herokuapp.com/
