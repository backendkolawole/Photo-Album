# django-capture

`django-capture` is a Photo Gallery allowing users to store images in album categories. `django-capture` is built with Python and Django

## Goal

`django-capture` will help you organize your photos and make sure they are arranged and instantly accessible 

## ⚙️ Installation

- Open CMD
  
- Change the current directory to the desktop

  `cd desktop`
   
- Clone this repository

  `git clone git@github.com:backendkolawole/django-capture.git`

- Change the current directory

  `cd django-capture`

- Create a virtual environment

  `python -m venv myvirtualenv`
  
- Activate virtual environment

  `myvirtualenv\Scripts\activate`

- Install all the packages listed in your requirements.txt file

  `pip install -r requirements.txt`

- Install Pillow with pip:

  ```
   python3 -m pip install --upgrade pip
   python3 -m pip install --upgrade Pillow
  ```

- In the same directory as settings.py, create a file called `.env`

  - Generate a secret key and set up the `SECRET_KEY` variable in the `.env` file

> [!WARNING]
> `SECRET_KEY` is the key to securing signed data – you must keep this secure, or attackers could use it to generate their own signed values.


- Apply migrations

  `python manage.py migrate`

- Run the server

  `python manage.py runserver`
