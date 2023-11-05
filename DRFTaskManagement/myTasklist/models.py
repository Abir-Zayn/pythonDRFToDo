from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    Due_Date = models.DateTimeField()
     
    tags_choice = [
        ('emergency', 'EMERGENCY'),
        ('study', 'STUDY'),
        ('coding', 'CODING'),
        ('meditation', 'MEDITATION'),
        ('journal', 'JOURNAL'),
        ('dailytask','DAILY TASK'),
        ('other','OTHER')
    ]
    
    priority_choices = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ]
    
    tag = models.CharField(max_length=100,choices=tags_choice)
    priority = models.CharField(max_length=100,choices=priority_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)