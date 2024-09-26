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
    # image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts",null=True)
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

class Comments(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    posts = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    def full_name(self):
        return f"{self.user_name} {self.user_email} {self.text} {self.posts}"
        # return 
    
    def __str__(self):
        return self.full_name()
    
class Comm(models.Model):
    user_name = models.CharField(max_length=100)
    def full_name(self):
        return f"{self.user_name} "
        # return 
    
    def __str__(self):
        return self.full_name()