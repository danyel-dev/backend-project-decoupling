from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuário')
    name = models.CharField('nome', max_length=100)


    def __str__(self):
        return self.name


class Item(models.Model):
    List = models.ForeignKey(List, on_delete=models.CASCADE, verbose_name='lista')
    name = models.CharField('nome', max_length=100)
    done = models.BooleanField('feito', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
