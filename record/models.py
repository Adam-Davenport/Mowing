from django.db import models


class Mowing(models.Model):
    location = models.CharField(max_length=50)
    direction = models.CharField(max_length=2)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '{}: {} on {}'.format(self.location, self.direction, self.date)
