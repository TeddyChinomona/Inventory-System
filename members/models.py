from django.db import models

class Name(models.Model):
    name = models.CharField(max_length= 20)
    surname = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)
    def __str__(self):
        return (f'{self.name}, {self.gender}')

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    member = models.ManyToManyField(Name)
    def __str__(self):
        member_names  = ','.join([str(member) for member in self.member.all()])
        return (f'{self.name}, {member_names}')