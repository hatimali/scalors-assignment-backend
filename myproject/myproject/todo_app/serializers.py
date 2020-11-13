from rest_framework import serializers
from .models import Board, TODO, Reminder


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        view_name='todo-detail',
        many=True,
        read_only=True,
    )
    uncompleted = serializers.HyperlinkedIdentityField(
        view_name='board-uncompleted'
    )

    class Meta:
        model = Board
        fields = ('url', 'name', 'todos', 'uncompleted')


class TODOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = ('url', 'title', 'done', 'board', 'created_at', 'updated_at')


class ReminderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reminder
        fields = ('url', 'post_url', 'text', 'delay')


class ReminderSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('__all__')
