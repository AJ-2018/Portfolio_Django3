from django.shortcuts import render, get_object_or_404

#importing model Blog for accessing its db
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-blog_Date')[:3] #this grabs all the objects from the db in Blog, orders them in recent date order and limits visibility of only 3 blogs at a time
    blogs_count = Blog.objects.count() #to have a count of total number of blogs
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'blogs_count': blogs_count})


def detailed_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #Blog refers to the class created in the model and pk refers to primary key
    return render(request, 'blog/detailed_blog.html', {'blog': blog})
