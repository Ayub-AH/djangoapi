from django.db import models

# Create your models here.
class Hadith(models.Model):
   title = models.CharField(max_length=100)
   hadith = models.TextField()
   book_taken_from = models.CharField(max_length=100)
   hadith_grading = models.CharField(max_length=100)
