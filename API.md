# JSON Objects returned by API:

### AuthToken
```JSON
{
    "jwt": "jwt.token.here"
}
```
### User
```JSON
{
    "id": 2,
    "name": "jhon doe",
    "email": "jhon@doe.com",
    "password": "pbkdf2_sha256$260000$bp6e8TMwdGS8k8xNwJ1d30$oWhFen7Ax7xjX0cxeQ5y4ihkEl0f/3vlWNG8P8IQKwE="
}
```
### Address
```JSON
{
    "id": 2,
    "fullname": "Williams B Holloway",
    "company": "",
    "email": "",
    "coutrycode": "",
    "number": "",
    "street": "518 Johnson Street",
    "area": "",
    "city": "Raleigh",
    "state": "North Carolina",
    "country": "US",
    "zip": "27604",
    "fax": "",
    "website": "",
    "author": 2
}
```

### Multiple Address
```JSON
{
    "total pages": "1",
    "page number": 1,
    "page size": 10,
    "result": [
        {
            "id": 1,
            "fullname": "b@b.com",
            "company": "",
            "email": "",
            "coutrycode": "",
            "number": "",
            "street": "bdf",
            "area": "",
            "city": "coudfntry",
            "state": "sfddfs",
            "country": "ciy",
            "zip": "545454",
            "fax": "",
            "website": "",
            "author": 2
        },
        {
            "id": 2,
            "fullname": "Williams B Holloway",
            "company": "",
            "email": "",
            "coutrycode": "",
            "number": "",
            "street": "518 Johnson Street",
            "area": "",
            "city": "Raleigh",
            "state": "North Carolina",
            "country": "US",
            "zip": "27604",
            "fax": "",
            "website": "",
            "author": 2
        }
    ]
}
```

### Postal Codes

```JSON
{
    "zips": [
        "27604",
        "02743"
    ]
}
```

### Deleted Data
```JSON

{"message":"address successfully deleted!"}
```

### Errors
```JSON
{
    "detail": "An address with this id does not exist."
}
```
----

# Endpoints:

### Registration:

```http
POST /api/user
```
Example request body:
```JSON
{
    "name":"jhon doe",
    "email":"jhon@doe.com",
    "password":"12345678"
}
```
`No authentication required`, returns a [AuthToken](#AuthToken)

**Required:** `name`, `email`, `password`

### Login:

```http
POST api/login
```
Example request body:
```JSON
{
    "email":"jhon@doe.com",
    "password":"12345678"
}
```
`authentication required`, returns a [Deleted Data](#deleted-data)

**Required fields:**  `email`, `password`

### logout:

```http
DELETE api/login
```
`No authentication required`, returns a [AuthToken](#AuthToken)

### Get Current User:

```http
get api/user
```
`authentication required`, returns a [User](#user)

### Add Address:

```http
POST api/address
```
Example request body:
```JSON
{
   "fullname":"Williams B Holloway",
   "street":"518 Johnson Street",
   "city":"Raleigh",
   "country":"US",
   "state":"North Carolina",
   "zip":"27604"
}
```
`authentication required`, returns a [Address](#Address)

**Required fields:**  `fullname`, `street`,`city`, `country`,`state`, `zip`

### Get an Address:

```http
Get api/address/:id
```
`authentication required`, returns a [Address](#Address)

**Data Params:** `id`

### Update an Address:

```http
POST api/address
```
Example request body:
```JSON
{
   "fullname":"Williams B Holloway",
   "street":"518 Johnson Street",
   "city":"Raleigh",
   "country":"US",
   "state":"North Carolina",
   "zip":"27604"
}
```
`authentication required`, returns a [Address](#address)

**Required fields:**  `fullname`, `street`,`city`, `country`,`state`, `zip`

### Get Addresses:

```http
DELETE api/address/:id
```
`authentication required`, returns a [Deleted Data](#deleted-data)

**Data Params:** `id`

### Get Postal Addresses:

```http
GET api/postalcodes
```
`authentication required`, returns a [Postal Codes](#postal-codes)

### Get Multiple Addresses:

```http
GET api/address
```
`authentication required`, returns a [Multiple Address](#multiple-address)

| Parameter | default value | Description |
| :--- | :--- | :--- |
| `size` | `10` | set page size |
| `page` | `1` | set current page |
| `search` | `None` | search in every fields of address |

### Delete multiple Addresses:

```http
DELETE api/address
```
`authentication required`, returns a [Deleted Data](#deleted-data)

| Parameter | default value | Description |
| :--- | :--- | :--- |
| `size` | `10` | set page size |
| `page` | `1` | set current page |
| `search` | `None` | search in every fields of address |

---


### Tasks status completion

1. - [x]  User is able to create a new address
     - [x]  User will not be able to add a duplicated address to their account
2.  - [x]  User is able to retrieve all their postal addresses
     - [x]  User is able to retrieve a large number of address entries in a practical way
     - [x]   User is able to filter retrieved addresses using request parameters
3.  - [x]  User is able to update existing addresses
4.  - [x]  User is able to delete one
     - [x]  User is able to delete multiple addresses
     - [x]  User is able to authenticate with a username and a password
5.  - [x]  User can log out
