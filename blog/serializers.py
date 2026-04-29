from rest_framework import serializers
from .models import Post, Comment

# CommentSerializer is defined first so PostSerializer can use it
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']
        read_only_fields = ['created_at'] # Users shouldn't edit the creation date

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)

    class Meta:
        model = Post
        # Add 'author' to this list!
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments']
        read_only_fields = ['created_at']