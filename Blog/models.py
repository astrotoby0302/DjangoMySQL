from django.db import models

# Create your models here.
class Blog(models.Model):
    BlogId = models.CharField(max_length=30)
    Title = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=300)
    Start_date = models.DateField()
    End_date = models.DateField()

    class Meta:
        db_table = 'Blog'