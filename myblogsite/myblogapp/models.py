from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    date_created = models.DateField()
    tags = models.CharField(max_length=200)
    body = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-id"]

    
    class Admin:
		pass


#register my models
admin.site.register((Post))
