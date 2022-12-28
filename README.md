# Email_sender_Django_celery
Using celery with Django project.
## How to run this project on your machine!
### The Gmail part 
* now you need to create a Gmail account and then click on Manage your google account
* now click on the Security tab
* make sure to enable two steps verification
* now click on App passwords
* you have to type your password again
* click on select app choose *** other (Custome Name) *** and give a name to you app
* the last step click on generate and Gmail will generate a key or an app password make sure to copy this key or save it in a text file
### Edit your settings.py file

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'<br>
EMAIL_HOST = 'smtp.gmail.com'<br>
EMAIL_HOST_USER = 'yoorusername@gmail.com'<br>
EMAIL_HOST_PASSWORD = 'key' # the key of the app here<br>
EMAIL_PORT = 587<br>
EMAIL_USE_TLS = True<br>
DEFAULT_FROM_EMAIL = 'default from email'<br>


## Using RabbitMQ
* RabbitMQ handles larger messages better than Redis, however if many messages are coming in very quickly, scaling can become a concern
and Redis or SQS should be considered unless RabbitMQ is running at very large scale.

* Installing on Windows https://www.rabbitmq.com/install-windows.html



Create a virtual env<br>
pip install -r requirements.txt

Starting the worker process:
python -m celery -A django_celery worker -l INFO -P eventlet

#### Open another CMD
run: python manage.py runserver





