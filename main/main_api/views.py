from rest_framework.decorators import api_view
from main.models import Contact
from archive.models import Article, Tag
from rest_framework.response import Response
from archive.api.serializers import ArticleSerializer, TagSerializer
from rest_framework import status
from main.main_api.serializer import ContactSerializer


@api_view(['GET'])
def main_home_view(request):
    tag = Tag.objects.all()
    article = Article.objects.order_by('-id')[:3]
    if tag:
        article = article.filter(tags__title__exact=tag)
    serializer = ArticleSerializer(article)
    serializer_tag = TagSerializer(tag, many=True)
    context = {
        "serializer": serializer.data,
        "serializer_tag": serializer_tag.data
    }
    return Response(context)


@api_view(['POST'])
def main_contact_view(request):
    contact = ContactSerializer(data=request.data)
    if contact.is_valid():
        contact.save()
        return Response(contact.data, status=status.HTTP_201_CREATED)
    data = {
        "success": False,
        "message": "xatolik bor"
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)