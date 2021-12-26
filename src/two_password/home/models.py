from django.db import models

# Create your models here.
class User(models.Model):
    '''
    @field : EmailAddress (Using as Primary Key)
    @field : MasterPassword
    '''
    email_address = models.EmailField(primary_key=True, unique = True)
    master_password = models.CharField(max_length=20)

