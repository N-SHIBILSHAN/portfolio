from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    demo_link = models.URLField()
    code_link = models.URLField()

    def __str__(self):
        return self.title
