
# Day 1: Create loosly coupled Microservices 
## Hello World Microservice Application

Create a simple "Hello World" microservice application with a frontend using Node.js and a backend using Python that has access to a database. In this example, we'll use Node.js for the frontend, Flask for the backend, and SQLite as the database.

Before we get started, make sure you have Node.js and Python installed on your system.

### Step 1: Set up the project directory

Create a project directory and navigate to it in your terminal:

```bash
mkdir hello-world-microservice
cd hello-world-microservice
```

### Step 2: Set up the Node.js Frontend

Create the frontend using Node.js and Express.js:

```bash
cd frontend
npm init -y
npm install express
```
  
Now, create a file named app.js in the frontend directory:

```javascript

// frontend/app.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello from the frontend!');
});

app.listen(3000, () => {
  console.log('Frontend server is running on http://localhost:3000');
});


```

## Step 3: Set up the Python Backend
  
Create the backend using Python and Flask:

```bash

cd ..
mkdir backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install Flask

```
  
Now, create a file named app.py in the backend directory:

``` python

# backend/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from the backend!'

if __name__ == '__main__':
    app.run()

```


  
## Step 4: Create a SQLite Database
  
Let's set up a simple SQLite database. Create a file named database.py in the backend directory:

```python
# backend/database.py
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                  (id INTEGER PRIMARY KEY, message TEXT)''')

conn.commit()
conn.close()
```
  
Run this script to create the database:
  
```bash
python database.py
```
  
Make sure the db is created, and Access to DB:

```bash
#Lst the DB:
ls mydatabase.db
#access the db 
```bash
sqlite3 mydatabase.db
```
  
Interact with the DB:  
```sql
Copy code
.tables   -- List all tables in the database
SELECT * FROM messages;  -- Retrieve all data from the 'messages' table
```
<!-- Using DBeaver to diplay a db from GUI
If you prefer a graphical user interface (GUI) to interact with the database, you can use an SQLite database client. Some popular options include:

DB Browser for SQLite (DB4S): This is an open-source, user-friendly GUI tool for SQLite. You can download and install it from https://sqlitebrowser.org/. Once installed, open your database file (e.g., mydatabase.db) using DB4S, and you can easily view and query the database.
DBeaver: DBeaver is a free and open-source multi-database SQL client that supports SQLite. You can download it from https://dbeaver.io/, connect to your SQLite database, and use its SQL editor and visual query builder to explore the data.
These tools will provide a more user-friendly interface to check and display the contents of your SQLite database, making it easier to interact with your data.
-->

## Step : Run the Applications
### Run Locally
  
Start the frontend and backend servers:
  
For the frontend:
  
```bash
cd frontend
node app.js
```
    
For the backend:
  
```bash
cd backend
python app.py
```
  
Now, you should have a simple microservice application with a Node.js frontend, a Python backend, and an SQLite database. You can access the frontend at http://localhost:3000 and the backend at http://localhost:5000.




## Contributing

Feel free to contribute to this project by opening issues or pull requests.

## License

This project is licensed under the MIT License.





    


      
<!--Comments

**Flask**: Flask is a micro web framework for Python that is used to develop web applications. You write your application using Flask, and it handles the application's routes, views, and business logic. Flask is a great choice for web application development.
**WSGI Server**: WSGI stands for Web Server Gateway Interface. It's a specification that defines how web servers and web applications should communicate with each other. When deploying a Flask application in production, you need a WSGI server to handle incoming web requests and interact with your Flask application. Common WSGI servers include Gunicorn, uWSGI, and mod_wsgi (for Apache).
So, in production, you use Flask as your web application framework, and you use a WSGI server alongside it to handle the web server responsibilities. The WSGI server is responsible for efficiently handling incoming HTTP requests, load balancing, and managing your Flask application. This setup provides the performance, scalability, and reliability required for a production environment.

In summary, you don't replace Flask with a WSGI server; you use both in combination. Flask handles your application's logic, while the WSGI server handles the web server responsibilities in a production deployment.

-->


# Day 2: Connect the two microservices throught Rest APIs

## Define the API endpoint /api/message

In a microservices architecture, the frontend communicates with the backend through API endpoints. You need to define these endpoints in both the frontend and backend.  
  
Modify app.js in the frontend directory to make an API request to the backend. Here's an updated version of the frontend code:  

Here, we added an API call to the **/api/message** endpoint on the backend.  
  
```javascript

// frontend/app.js
const express = require('express');
const axios = require('axios'); // You'll need to install axios via npm

const app = express();

app.get('/', (req, res) => {
  // Make an API request to the backend
  axios.get('http://localhost:5000/api/message')
    .then(response => {
      res.send('Frontend received this message from the backend: ' + response.data);
    })
    .catch(error => {
      res.status(500).send('Error communicating with the backend.');
    });
});

app.listen(3000, () => {
  console.log('Frontend server is running on http://localhost:3000');
});

```
## Backend

**Update the Backend**: Modify the backend (app.py) to define the API endpoint:  
  
Here, we've created an **/api/message** endpoint that returns a JSON response.  
  
```python
# backend/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/message')
def get_message():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Bind to '0.0.0.0' to listen on all available network interfaces

```

  
**CORS**: You might need to enable Cross-Origin Resource Sharing (CORS) in your backend to allow requests from the frontend. You can do this by adding the flask-cors extension. Install it via pip install flask-cors and update your backend code:  
  

```python
# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/api/message')
def get_message():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```