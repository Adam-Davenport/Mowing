from django.db import models


class Mowing(models.Model):
    location = models.CharField(max_length=50)
    direction = models.CharField(max_length=25, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {} on {}'.format(self.location, self.direction, self.date)
