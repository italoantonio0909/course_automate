from django.db import models
from django.db.models.signals import post_save

from automate.users.models import BaseUser
import os


class Course(models.Model):
    title = models.CharField(max_length=1000)
    start = models.CharField(max_length=100)
    end = models.DateField(max_length=100)
    user = models.ManyToManyField(BaseUser)
    days = models.IntegerField()
    hours = models.IntegerField()
    state = models.CharField(max_length=100)
    file_data = models.FileField(upload_to='course_data')

    def __str__(self):
        return self.title


def post_save_course(sender, instance, created, *args, **kwargs):
    if created:
        base_dir = os.getcwd()
        data_dir = os.path.join(base_dir, 'data')

        # Name of data
        course_data = instance.file_data.name
        filename = os.path.join(data_dir, course_data)
        if os.path.exists(filename):
            print('CORRECTO')
        #    with open(filename) as file:
            # print(file)


post_save.connect(post_save_course, sender=Course)
