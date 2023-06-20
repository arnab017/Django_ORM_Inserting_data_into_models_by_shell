from django.db import models as mo

# Create your models here.
class Topic(mo.Model):
    topic_name = mo.CharField(max_length=50, primary_key=True)
    
    def __str__(self):
        return self.topic_name

class Webpage(mo.Model):
    name = mo.CharField(max_length=50, primary_key=True)
    topic_name = mo.ForeignKey(Topic, on_delete=mo.CASCADE)
    url = mo.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Access_Records(mo.Model):
    author = mo.CharField(max_length=50, primary_key=True)
    name = mo.ForeignKey(Webpage, on_delete=mo.CASCADE)
    date = mo.DateField()
    
    def __str__(self):
        return self.author
    