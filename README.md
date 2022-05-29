# PAY-BY-FACE
“NO CARD, NO CASH, and NO PHONE for Payment:  Do hustle free shopping with enhanced Security using FACIAL RECOGNITION “ 

/******************install django and set it up in your device.**************/

create virtual environment
->py -m venv myproject
->myproject\Scripts\activate.bat

install Django
->py -m pip install Django

Create django project 
->django-admin startproject myworld

To run the program 
->py manage.py runserver

/************************DATABASE*********************/

I have used mysql as a database running on local host.
->'USER': 'root',
->'PASSWORD': '',

to connect database with django after creating model in model.py run command:
->python manage.py makemigration
->python manage.py migrate

/***************PYTHON FILE FOR FACE RECOGNITION**************/
->python get-pip.py

install python libraries 
->pip install numpy
->pip install csv
->pip install face recognition
->pip install pickle-mixin
