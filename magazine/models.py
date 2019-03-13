from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length = 300)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'media/', default = 'default.jpg')
    description = models.CharField(max_length = 500)
    related = models.CharField(max_length = 10, choices = (
        ("General", "General"),
        ("Technology", "Technology"),
        ("Culture", "Culture"),
        ("Design", "Design"),
        ("Ideas", "Ideas"),
        ("Politics", "Politics"),
        ("Self", "Self"),
        ("Health", "Health"),
        ("Science", "Science"),
        ("Business", "Business")
    ), default = "General")
    content = models.TextField()
    created_at = models.DateTimeField(editable = False)
    updated_at = models.DateTimeField(editable = False)

    def save(self, *args, **kwargs):

        "On save update the timestamp of article object"
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Article, self).save(*args, **kwargs)

    def __str__(self):

        "Return the meaningful string about the article"
        return self.title + " by " + str(self.author)
