from django.db import models

class Project(models.Model):
    project_Title = models.CharField(max_length=100)
    project_Description = models.CharField(max_length=350)
    project_Image = models.ImageField(upload_to='portfolio/images')
    project_URL = models.URLField(blank=True) #blank attribute gives an option to the user to whether include a url or not

    #this shows the project's actual title instead of default title in the admin dashboard
    def __str__(self):
        return self.project_Title

