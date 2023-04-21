from django.db import models


class Club(models.Model):
    DoesNotExist = None
    objects = None
    club_name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.club_name


class Player(models.Model):
    objects = None
    nickname = models.CharField(max_length=30, unique=True, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    club = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nickname
