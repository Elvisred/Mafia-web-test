from django.db import models


class Player(models.Model):
    nickname = models.CharField(max_length = 100, unique = True)
    club = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.nickname
