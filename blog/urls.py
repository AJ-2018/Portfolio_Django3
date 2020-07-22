from django.urls import path
from . import views #to import blog app's view file

#declaring app name to access each blog
app_name = 'blog'

urlpatterns = [
    #coming from the main url file the default path goes like 'example.com/blog'
    path('', views.all_blogs, name='all_blogs'),
    #the route takes in a integer as input and shows the blog associated with it as output
    path('<int:blog_id>/', views.detailed_blog, name='detailed_blog'),
]