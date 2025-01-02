from rest_framework import serializers

from apps.boards.models import Board, Group, Tile


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    tiles = TileSerializer(many=True)

    class Meta:
        model = Group
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = Board
        fields = "__all__"
