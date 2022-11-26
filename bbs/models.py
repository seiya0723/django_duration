from django.db import models

class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    time        = models.DurationField(verbose_name="時間")




