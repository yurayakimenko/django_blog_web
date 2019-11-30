from django.db import models
from django.utils import timezone
from django.db.models.manager import Manager
from django.contrib.auth.models import User


class Picture(models.Model):
    objects = Manager()
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    created_date = models.DateTimeField(default=timezone.now)
    liked_by = models.ManyToManyField(User)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

