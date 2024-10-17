from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
     name = models.OneToOneField(User, on_delete=models.CASCADE)
     phone = models.CharField(max_length=15)
     bio = models.CharField(max_length=100)
     pic = models.ImageField(upload_to='images/tentimages')

     def __str__(self):
        return self.name.first_name

class Menu(models.Model):
    img = models.ImageField(upload_to='images/tentimages', null=True, blank=True)
    name = models.CharField(max_length=30, default='Enter a name')
    description = models.CharField(max_length=20, default='Describe your product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)
    active_status = models.BooleanField()

    def __str__(self):
        return self.name

class Menusnacks(models.Model):
    img = models.ImageField(upload_to='images/tentimages', null=True, blank=True)
    name = models.CharField(max_length=20, default='Enter a name')
    description = models.CharField(max_length=30, default='Describe your product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)
    active_status = models.BooleanField()

    def __str__(self):
        return self.name


class Menubakery(models.Model):
    img = models.ImageField(upload_to='images/tentimages', null=True, blank=True)
    name = models.CharField(max_length=20, default='Enter a name')
    description = models.CharField(max_length=30, default='Describe your product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)
    active_status = models.BooleanField()

    def __str__(self):
        return self.name

class Menuswallow(models.Model):
    img = models.ImageField(upload_to='images/tentimages', null=True, blank=True)
    name = models.CharField(max_length=20, default='Enter a name')
    description = models.CharField(max_length=30, default='Describe your product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)
    active_status = models.BooleanField()

    def __str__(self):
        return self.name

class Menuforeign(models.Model):
    img = models.ImageField(upload_to='images/tentimages', null=True, blank=True)
    name = models.CharField(max_length=20, default='Enter a name')
    description = models.CharField(max_length=30, default='Describe your product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)
    active_status = models.BooleanField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/tentimages', null=True, blank=True)
    title = models.CharField(max_length=50)
    desc = models.CharField( max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.author.name}'s blog"

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Like(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.name} liked this post"

class Dislike(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    dislike = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.name} disliked this post"


