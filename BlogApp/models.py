from cgitb import text
from pyexpat import model
from tkinter import CASCADE
from turtle import title
from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='author')
    title = models.CharField(max_length=50, verbose_name='title')
    text = models.TextField(verbose_name='main text')

    def __str__(self):
        return self.title