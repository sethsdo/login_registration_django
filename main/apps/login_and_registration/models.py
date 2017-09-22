from __future__ import unicode_literals
import re
from django.db import models

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class userManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        print postData
        for input in postData:
            if len(postData[input]) < 2:
                errors['input'] = "All fields are required"
            elif not postData['first_name'].isalpha():
                errors['first_name'] = "Invalid  first name!"
            elif not postData['last_name'].isalpha():
                errors['last_name'] = "Invalid  last name!"
            elif not emailRegex.match(postData['email']):
                errors['email'] = "Invalid  email!"
            elif postData['password'] < 8:
                errors['password'] = "Invalid password..."
            elif postData['password'] != postData['confirm_password']:
                errors['confirm_password'] = "Passwords dont match!"
            return errors

    def login_validator(self, postData):
        errors = {}
        for input in postData:
            if len(postData[input]) < 2:
                errors['input'] = "All fields are required"
            elif not emailRegex.match(postData['email']):
                errors['email'] = "Invalid  email!"
            elif postData['password'] < 8:
                errors['password'] = "Invalid password..."
            return errors


class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = userManager() 

    def __repr__(self):
        return "<user object: {} {} {}>".format(self.first_name, self.last_name, self.email)
