from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(100)

class Book(models.Model):
    title = models.CharField(100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(100)
    book = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)