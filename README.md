# Event Manager Project

Winter of Code 4.0 Project

# Main Files and Directories

Here is a short description of what each directory is doing:

1. Event_Manager : This is the main project file. Every URL request passes through this, and gets transferred to specified App.
2. registration : This is a Django app, which is the centre of this project.
3. venv : This is a virtual enviornment, like a sandbox, it provides all necessary tools for running our app. So, if anyone has to try this app, he/she can activate the virutal environment and then start using it, without having to worrying about installing django and python.
4. static : A directory for storing all the static files like javascript, css, images.
5. db.sqlite3 : This is the database where our events and participant detatils will be stored.
6. manage.py : This file does the management with its built-in features, like creating apps, starting the server, etc.

# Getting Started

1. To start using this project, download the whole folder or clone it on your local disk.
2. Open up a terminal window in that directory.
3. Start a virtual environement by typing the following command :

```
.\venv\Scripts\activate
```

4. Now, you are inside your virutal environment. Start the server by running the following command :

```
py manage.py runserver
```

5. You can visit `localhost:8000/events` or `127.0.0.1:8000/events`, and you'll be good to go.

# You'r Everything

1. You'r the Admin : To see the database and make changes, you need to have one "Super User" as django says it.
   a. To create one (its okay if you keep your server running), open up a new terminal window in the same directory where you have downloaded the project files, and write the following command :

```
py manage.py createsuperuser
```

    b. Upon hitting enter you will be asked to provide username, email, and password (it's okay if you provide very small username and password, just make something which you can remember). Then head to this URL, `localhost:8000/admin`. Sign with your username and password, and you will be taken to admin site. Here, you can make any changes to the database like create entries, delete, modify and all.
