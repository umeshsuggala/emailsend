from django.db import models

# Create your models here.
class Email(models.Model):
	email=models.EmailField(max_length=50,null=True)
	pwd=models.CharField(max_length=20)
	new=models.CharField(max_length=20,null=True)



