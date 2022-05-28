from django.db import models
import os

# Create your models here.

def filepath(request, Name):
    old_filename = Name
    filename = old_filename
    return os.path.join('uploads/', filename)

class face_pay(models.Model):
    Name = models.TextField(max_length=191)
    Password = models.IntegerField()
    Picture = models.ImageField(upload_to=filepath, null=True, blank=True)
    class Meta:
       db_table = 'members_face_pay'


