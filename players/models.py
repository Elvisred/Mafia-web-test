from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.club_name


class Player(models.Model):
    nickname = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    club = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname
