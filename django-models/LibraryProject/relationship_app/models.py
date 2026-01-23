from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    



class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# 🔹 Signal to auto-create profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
