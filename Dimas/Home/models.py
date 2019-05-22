from django.db import models
from django.utils import timezone

class Projects(models.Model):
	Project_name=models.CharField(max_length=70)
	Task=models.CharField(max_length=60)
	def __str__(self):
		return '%s %S' %(self.Project_name,self.Task)

    # def __str__(self):
    #     return '%s %s' %(self.Type ,self.Blog_Title)