from django.db import models

class Client(models.Model):
	Phone_number=models.IntegerField(max_length=10)
	
