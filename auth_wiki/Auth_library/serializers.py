from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['content', 'author_name']


class AuthLibrarySerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField('get_comments')
    
    def get_comments(self, obj):
        query = obj.comment_set.all()
        comments =CommentSerializer(query, many=True).data
        return comments


    class Meta:
        model = AuthLibrary
        fields = ['created_by', 'functionality', 'code_snippet', 'comments', 'categories', 'created_at']
        