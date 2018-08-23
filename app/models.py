from django.db import models

class Tasklist(models.Model):
    item = models.CharField(max_length=255)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' - ' + str(self.ended)
