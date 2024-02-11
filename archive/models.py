from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    message = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='contents')
    content = RichTextField(null=True, blank=True)
    is_quote = models.BooleanField(default=False)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    top_level_parent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/comments/')
    message = models.TextField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def getReplies(instance, *args, **kwargs):
        # return Comment.objects.filter(parent=self).reverse()
        if not instance.top_level_parent_id:
            replies = Comment.objects.filter(top_level_parent_id=instance.id)
            return replies
        else:
            return None

def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + '-' + str(timezone.now().date()))


pre_save.connect(article_pre_save, sender=Article)


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_parent_id:
            instance.top_level_parent_id = instance.parent.top_level_parent_id
        else:
            instance.top_level_parent_id = instance.parent.id


pre_save.connect(comment_pre_save, sender=Comment)



