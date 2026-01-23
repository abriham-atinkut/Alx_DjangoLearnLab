from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return {self.title , self.author.name}

class Library(models.Model):
    name = models.CharField(100)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.name , self.book.name}"
    
class Librarian(models.Model):
    name = models.CharField(100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name , self.library.name}"