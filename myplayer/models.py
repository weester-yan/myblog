from django.db import models

# Create your models here.
class Myplayer(models.Model):
    title = models.CharField(max_length = 100)
    date_time = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['-date_time']
