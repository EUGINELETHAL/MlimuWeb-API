E-LEARNING-PLATFORM
This is a fullstack application built with Django and ReactJS. 



live heroku link 
 User Stories

Demo


Screenshots
 Screenshot

Requirements
Python 3.6
Django 2.2
Node 7.9.0 or greater
ReactJS 16+

Getting Started
git clone https://github.com/EUGINELETHAL/E-LEARNING-PLATFORM
.

Set up  and Activate your virtual env

You will then go ahead and activate the Virtual environment and install the Python packages using Pip.

source venv/bin/activate
cd LMS
pip install -R requirements.txt
Next we will update the Django Settings.py to reflect your own database credentials and migrate the models.

python manage.py migrate
For the Front-End, we'll go ahead and install the JavaScript packages using NPM (this may take a while).

npm install
Finally, you can start the development server for both the Back-End and the Front-End and being rolling out your own LMS.

python manage.py runserver
npm run start
License
GNU/GPL 3.0