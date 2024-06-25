from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    email = models.EmailField()
    team_id = models.ForeignKey(Teams, related_name='members', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
