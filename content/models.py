from django.db import models

class Dimension(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Nature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    img_url = models.URLField(null=True, blank=True)
    health = models.IntegerField(default=1)
    version = models.CharField(max_length=10,default="1.0")
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE,related_name="articles", default=1)
    nature = models.ForeignKey(Nature, on_delete=models.CASCADE,related_name="articles", default=1)

    def __str__(self):
        return self.title
    

