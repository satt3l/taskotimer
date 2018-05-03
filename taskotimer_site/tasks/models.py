from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField('date created')
    due_to = models.DateTimeField('due to date')
    status = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    completness = models.IntegerField(default=0)

    def __str__(self):
        return ("name is: %s, description: %s" % (self.name, self.description))
