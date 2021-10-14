from django.db import models


class Group(models.Model):
    cod = models.SmallIntegerField(blank=True, unique=True, null=True)
    description = models.CharField(max_length=255)  

    def __str__(self):
        return "%s (%s)" %(self.description, self.cod)

class Certificado(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    groups = models.ManyToManyField(Group)
    expiration = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s (%s)" %(self.name, self.description)
