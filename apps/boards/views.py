from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.boards.models import Board
from apps.boards.serializers import BoardSerializer


class BoardViewSet(ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.AllowAny,)
