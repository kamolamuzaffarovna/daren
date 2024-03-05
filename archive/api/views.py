from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from archive.models import Article, Tag, Category, Content, Comment
from .serializers import ArticleSerializer, ArticleCommentSerializer, TagSerializer, CategorySerializer, \
    ArticleContentSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def article_list_view(request):
    qs = Article.objects.all()
    tags = Tag.objects.all()
    category = Category.objects.all()
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if q:
        qs = qs.filter(title__icontains=q)
    if cat:
        qs = qs.filter(category__title__exact=cat)
    if tag:
        qs = qs.filter(tags__title__exact=tag)
    serializer = ArticleSerializer(qs, many=True)
    serializer_tags = TagSerializer(tags, many=True)
    serializer_category = CategorySerializer(category, many=True)
    context = {
        "serializer": serializer.data,
        "serializer_tags": serializer_tags.data,
        "serializer_category": serializer_category.data
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_detail_view(request, *args, **kwargs):
    article = get_object_or_404(Article, slug=kwargs['slug'])
    comment = Comment.objects.filter(article_id=article.id).order_by('-id')
    content = Content.objects.filter(article_id=article.id)
    if request.method == 'POST':
        comment = ArticleCommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        data = {
            "success": False,
            "message": "Xatolik bor",
            "detail": "Xatolikni toping"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    serializer = ArticleSerializer(article)
    comment = ArticleCommentSerializer(comment, many=True)
    content = ArticleContentSerializer(content, many=True)
    context = {
        'serializer': serializer.data,
        'comment': comment.data,
        'content': content.data
    }
    return Response(context, status=status.HTTP_200_OK)