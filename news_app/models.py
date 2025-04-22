from django.db import models


class Advertisement(models.Model):
    headline = models.CharField(max_length=255)
    file_url = models.URLField()
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    css_class = models.CharField(max_length=100, blank=True, null=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='ads')  # link to Article
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline} (Ad for: {self.article.headline})"


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True) 
    video_url = models.URLField(blank=True, null=True)  
    image_filename = models.CharField(max_length=255, blank=True, null=True)
    video_filename = models.CharField(max_length=255, blank=True, null=True)
    likes = models.IntegerField(default=0)
    pokemon = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def get_image_url(self):
        if self.image_url:
            return self.image_url
        if self.image_filename:
            return f"https://raw.githubusercontent.com/yuiyeyo/andreaadimiharja_hw4/refs/heads/main/assets/{self.image_filename}"
        return ""


    def __str__(self):
        return self.headline

    
class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, default="Jane Doe") 
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.name}: {self.text[:30]}" 
    

class VisualContent(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_url = models.URLField(blank=True, null=True) 
    file_type = models.CharField(max_length=10, choices=[("image", "Image"), ("video", "Video")])
    css_class = models.CharField(max_length=100, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.name
