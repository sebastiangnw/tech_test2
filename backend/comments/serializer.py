"""Rest API serializers for tasks app."""


from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""
    class Meta:
        """Meta class for serializer."""
        model = Comment
        # fields = ("id", "name", "comment", "user", "created")
        fields = "__all__"
        read_only_fields = ("id", "created")
