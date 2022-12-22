# Learn Flask Web App Tutorial Step by step

The original study resource is in the main branch, YouTude [Link](https://www.youtube.com/watch?v=dam0GPOAvVI&ab_channel=TechWithTim)


│  main.py                    ##python main.py to set up the local app
│  Readme.md 
│  requirements.txt           ## packages to install
│
├─instance
│      database.db            ## database to store User and Note
│
└─website
    │  auth.py                ## define how to access different pages, such as login, signup, log out
    │  models.py              ## define database structures, there are two tables here
    │  views.py               ## define home page view
    │  __init__.py            ## initiate app, database, login_manager, define the status of being logged in 
    │
    ├─static
    │      index.js           ## Javascript to delete node and return to the current page automatically
    │
    ├─templates
    │      base.html          ## Define the main style of the app
    │      home.html          ## Extension of base.html, home page
    │      login.html         ## Extension of base.html, login page
    │      sign_up.html       ## Extension of base.html, sign up page

## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
