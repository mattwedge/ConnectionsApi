from django.db import models

from apps.authentication.models import User


class Board(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="boards"
    )
    name = models.CharField(null=False, default="", blank=False, max_length=255)


class Group(models.Model):
    name = models.CharField(null=False, default="", blank=False, max_length=255)
    board = models.ForeignKey(
        Board, null=True, on_delete=models.SET_NULL, related_name="groups"
    )


class Tile(models.Model):
    name = models.CharField(null=False, default="", blank=False, max_length=255)
    group = models.ForeignKey(
        Group, null=True, on_delete=models.SET_NULL, related_name="tiles"
    )
