from django.db import models

# Create your models here.
# This is how you implement changes in the database. Everytime you make changes to the database, 
# you have to run the python manage.py makemigrations command. 
# The python manage.py migrate command actually moves the code.

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__ (self):
        return f"{self.first_name} {self.last_name}"
    