from django.db import models

# Create your models here.
class Blogger(models.Model):
    """用户的博客"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
    
class BlogPost(models.Model):
    """用户博客的具体博文内容"""
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blogposts'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."

