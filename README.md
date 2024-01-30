
# Backend Problem Statement : Task Management System


```plaintext
task_main/
│
├── task_app/
│   ├── migrations/
│   ├── admin.py
│   ├── app.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── task_main/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── test.py
├── README.md

```

<h2>Setup :</h2>

Clone the repository to your local machine:
```sh
$ git clone https://github.com/jay-arora31/Task-Management-API.git
$ cd Task-Management-API
```
Install the required dependencies:
```sh
$ virtualenv venv
```
```sh
$ venv\scripts\activate


```
```sh
$ pip install -r requirements.txt


```

Apply database migrations:
```sh
$ python manage.py makemigrations


```
```sh
$ python manage.py migrate


```

Start the development server:
```sh
$ python manage.py runserver


```

## API Endpoints

## 1. Create a new Task

### Endpoint
- **Endpoint**: `/v1/tasks`
- **Method**: POST

### Request Body (JSON)
```json
{
  "title": "Task 1"
}
```
### Output
```json
{
  "id": 1
}
```


## 2. Bulk add tasks

### Endpoint
- **Endpoint**: `/v1/tasks`
- **Method**: POST

### Request Body (JSON)
```json
{
  "tasks": [
    {"title": "Task 1", "is_completed": false},
    {"title": "Task 2", "is_completed": true},
    {"title": "Task 3", "is_completed": false}
  ]
}
```
### Output
```json
{
  "tasks": [
    {"id": 1},
    {"id": 2},
    {"id": 3}
  ]
}

```

## 3. List all Tasks

### Endpoint
- **Endpoint**: `/v1/tasks`
- **Method**: GET


### Output
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Task 1",
      "is_completed": false
    },
    {
      "id": 2,
      "title": "Task 2",
      "is_completed": true
    }
  ]
}


```


## 4. Get a specific Task

### Endpoint
- **Endpoint**: `/v1/tasks/{id}`
- **Method**: GET

### Request URL
Replace {id} with the actual task ID.

### Output
```json
{
  "id": 1,
  "title": "Task 1",
  "is_completed": false
}
```

## 5. Delete a specific Task

### Endpoint
- **Endpoint**: `/v1/tasks/{id}`
- **Method**: DELETE

### Request URL
Replace {id} with the actual task ID.

### Output
(No JSON response; returns a 204 No Content status)



## 2.  Bulk delete tasks

### Endpoint
- **Endpoint**: `/v1/tasks`
- **Method**: DELETE

### Request Body (JSON)
```json
{
  "tasks": [
    {"id": 1},
    {"id": 2},
 
  ]
}
```
### Output
(No JSON response; returns a 204 No Content status)



## 7. Edit the title or completion of a specific Task

### Endpoint
- **Endpoint**: `/v1/tasks/{id}`
- **Method**: PUT

### Request Body (JSON)
```json
{
  "title": "Updated Task Title",
  "is_completed": true
}
```
### Output
(No JSON response; returns a 204 No Content status)








## 

![image](https://github.com/jay-arora31/CareerJunction/assets/68243425/523535ce-e9bf-48f2-b7cd-340998b05814)



