from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id"]  # why need to show id, if the instance is picked from the url not including the id doesn't stop the update of the particular instance of todo?
        read_only_fields = ['title', 'memo', 'created', 'completed']

        # Why completed is read-only: This is the key insight - completed is marked as read-only in the serializer to prevent it from being directly modified through the API request payload. Instead of letting clients set any value they want, the toggle logic is controlled by the view's perform_update method.
        # This is a security and design choice - it ensures that clients can only toggle the state(true→false or false→true) rather than setting it to any arbitrary value
