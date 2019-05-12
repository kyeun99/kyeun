from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to ="images/", blank=True)
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text