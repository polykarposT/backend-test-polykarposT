# backend-test-polykarposT

This is back-end-test-user1 from Polykarpos Tiftikoglou
For this project the database we used is SQLite. The reason is to prevent the reviewer to do extra steps like setup a database locally only for this project.

Python version for this project is 3.10.5

## How to use the application
The first thing you have to do is to clone the repo to your machine. 
When the clone is done, you have to open a terminal or navigate using the terminal to the same directory with the ```manage.py``` file.

Now you have to do two more steps to successfully run the application. The first step is to write to your terminal ```python -m venv virtualenv``` and create a python virtual environment with name ```virtualenv```. First with virtualenv we will avoid to install different versions of the packages that we need to run the application and second the necessary packages will be install only inside the virtual environment. Now write to your terminal ```source virtualenv/bin/activate``` to activate the virtual environment.

You know that you activate the virtual environemnt when you see int the terminal something like this ```(virtualenv) polykarpostiftikoglou@192 backend-test-polykarposT % ```

Now run ```pip install -r requirements.txt``` to install the necessary python packages that we need to run the application

Ok, that's it`! Now you are ready to run the application! Write to the terminal ```python manage.py runserver```

Using SQLite and having the database in the ```db.sqlite3``` you don't need to run ```python manage.py makemigrations``` , ```python manage.py migrate``` and ```python manage.py createsuperuser```. 

Now you are ready to use the application! Open your favourite browser and type ```http://127.0.0.1:8000/```

Probably the application is working (hope so) and you can see that I everything is almost orange!!

Now the only thing you have to do is to press the ```get company info``` button to retrieve tha company information!

Last but not least, you can access the Django admin page at the following url ```http://127.0.0.1:8000/admin/``` and use ```admin``` for username and password.
