# [Volt Dashboard Flask](https://appseed.us/product/volt-dashboard/flask/)

Open-Source **[Flask Dashboard](https://appseed.us/admin-dashboards/flask/)** generated by the `AppSeed` platform with basic modules, database, authentication, and deployment scripts on top of **Volt Dashboard** (free version). Volt Dashboard is a free and open-source **Bootstrap 5** dashboard template featuring over 100 components, 11 example pages, and 3 plugins with Vanilla JS. There are more than 100 free Bootstrap 5 components included some of them being buttons, alerts, modals, date pickers, and so on.

- 👉 [Volt Dashboard Flask](https://appseed.us/product/volt-dashboard/flask/) - `Product page`
- 👉 [Volt Dashboard Flask](https://flask-volt-dashboard.appseed-srv1.com/) - `LIVE Demo`

<br />

## ✅ Features

- `Up-to-date dependencies`
- `Database`: `SQLite`, MySql
  - Silent fallback to `SQLite`
- `DB Tools`: SQLAlchemy ORM, `Flask-Migrate`
- `Authentication`, Session Based, `OAuth` via **Github**
- Docker, `Flask-Minify` (page compression)
- `Deployment` 
  - `CI/CD` flow via `Render`

![Volt Dashboard - Full-Stack Starter generated by AppSeed.](https://github.com/sanjayengineer121/video_streaming_sharing_project/blob/main/media/Screenshot%202024-01-30%20012647.png)

## ✅ Environment

To use the starter, [Python3](https://www.python.org) should be installed properly in the workstation. If you are not sure if Python is installed, please open a terminal and type `python --version`. Here is the full list with dependencies and tools required to build the app:

- [Python3](https://www.python.org) - the programming language used to code the app
- [GIT](https://git-scm.com) - used to clone the source code from the Github repository
- Basic development tools (g++ compiler, python development libraries ..etc) used by Python to compile the app dependencies in your environment.
- (Optional) `Docker` - a popular virtualization software

## ✅ Start in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/flask-volt-dashboard.git
$ cd flask-volt-dashboard
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.


## ✅ Create `.env` file

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `ASSETS_ROOT`: used in assets management
  - default value: `/static/assets`
- `OAuth` via Github
  - `GITHUB_ID`=<GITHUB_ID_HERE>
  - `GITHUB_SECRET`=<GITHUB_SECRET_HERE> 


## ✅ Manual Build

> Download the code 

```bash
$ git clone https://github.com/app-generator/flask-volt-dashboard.git
$ cd flask-volt-dashboard
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
// OR
$ flask run --cert=adhoc # For HTTPS server
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Start the app

```bash
$ flask run
// OR
$ flask run --cert=adhoc # For HTTPS server
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:5000/register`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:5000/login`

<br />

## ✅ Codebase

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # A simple app that serve HTML files
   |    |    |-- routes.py                  # Define app routes
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />
