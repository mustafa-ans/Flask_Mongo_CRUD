# CRUD Application

This is a CRUD (Create, Read, Update, Delete) application built using Flask and MongoDB. It allows users to create, read, update, and delete user data.

# Setup

    Install MongoDB on your device

    Install Python 3 on your device

    Install the required Python libraries using the following command:

pip install pymongo flask

Run the app.py file using the following command:

    python app.py

    Open a web browser and go to http://localhost/users to view all the users in the database.

# Usage

    To create a new user, send a POST request to http://localhost/users with the following parameters in the request body:
        name (required)
        email (required)
        password (required)

    To update a user, send a PATCH request to http://localhost/users/<id> with the user ID in the URL parameter and the following parameters in the request body:
        name (optional)
        email (optional)
        password (optional)

    To delete a user, send a DELETE request to http://localhost/users/<id> with the user ID in the URL parameter.

    To retrieve a specific user, send a GET request to http://localhost/users/<id> with the user ID in the URL parameter.

    To retrieve all users, send a GET request to http://localhost/users.

# Intructions to setup this application on your device

Requirements:

    MongoDB installed on your device
    Python 3 installed on your device
    pymongo and flask Python libraries installed

Setup:

    Clone the repository to your device or download the project files.

    Start the MongoDB server on your device.

    Navigate to the project directory in your terminal or command prompt.

    Install the required Python libraries using the following command:

pip install pymongo flask

Run the app.py file using the following command:

python app.py

If everything is set up correctly, you should see the following message in your terminal:

csharp

    Running on http://127.0.0.1:80/ (Press CTRL+C to quit)

    Open a web browser and go to http://localhost/users. This should display a JSON array of all the users in the database.

Usage:

    To create a new user, send a POST request to http://localhost/users with the following parameters in the request body:
        name (required)
        email (required)
        password (required)

    To update a user, send a PATCH request to http://localhost/users/<id> with the user ID in the URL parameter and the following parameters in the request body:
        name (optional)
        email (optional)
        password (optional)

    To delete a user, send a DELETE request to http://localhost/users/<id> with the user ID in the URL parameter.

    To retrieve a specific user, send a GET request to http://localhost/users/<id> with the user ID in the URL parameter.

    To retrieve all users, send a GET request to http://localhost/users.

Note:

    The default port for the app is 80. If you need to change it, modify the app.run() method in the app.py file accordingly.
    You can modify the database name and collection name in the mongo and db variables in the app.py file, respectively. By default, the database name is user_db and the collection name is users.

# Dependencies

    Flask
    pymongo

# License

This project is licensed under the MIT License. See the LICENSE file for more information.
