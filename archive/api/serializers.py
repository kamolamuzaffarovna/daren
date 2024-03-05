from rest_framework import serializers
from archive.models import Article, Tag, Category, Comment, Content
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_login', 'date_joined']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'slug', 'category', 'image', 'title', 'tags', 'modified_date', 'created_date']


class ArticleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'name', 'image', 'message', 'email', 'parent', 'top_level_parent_id', 'author', 'article']


class ArticleContentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Content
        fields = ['article', 'content', 'is_quota']