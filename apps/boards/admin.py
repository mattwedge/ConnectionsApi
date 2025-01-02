from django.contrib import admin

from .models import Board, Group, Tile


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    """Tile admin"""

    model = Tile
    list_display = ("name", "group")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Group admin"""

    model = Group


@admin.register(Board)
class Board(admin.ModelAdmin):
    """Board admin"""

    model = Board
