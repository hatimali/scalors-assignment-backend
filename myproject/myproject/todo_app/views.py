from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import mixins
from .models import Board, TODO, Reminder
from .serializers import BoardSerializer, TODOSerializer, ReminderSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list(self, request, *args, **kwargs):
        response = super(BoardViewSet, self).list(request, *args, **kwargs)
        for board in response.data:
            board['todo_count'] = len(board.pop('todos'))
        return response

    @detail_route()
    def uncompleted(self, request, *args, **kwargs):
        board = self.get_object()
        uncompleted_todos = board.todos.filter(done=False)
        serializer = TODOSerializer(uncompleted_todos, context={'request': request}, many=True)
        return Response(serializer.data)


class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer


class ReminderViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
