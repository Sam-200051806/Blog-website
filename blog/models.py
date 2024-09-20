from django.db import models
# from django.core.validators import 
# Create your models 
class Tag(models.Model):
    caption = models.CharField(max_length=100)
    def full_name(self):
        return f"{self.caption} "
        # return 
    
    def __str__(self):
        return self.full_name()
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        # return 
    
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField() 
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tag  = models.ManyToManyField(Tag)
    def full_name(self):
        return f"{self.title}"
        # return 
    
    def __str__(self):
        return self.full_name()

