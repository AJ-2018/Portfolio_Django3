from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_Title = models.CharField(max_length=150)
    blog_Description = models.TextField()
    blog_Date = models.DateField()

    #this shows the blog's actual title instead of default title in the admin dashboard
    def __str__(self):
        return self.blog_Title