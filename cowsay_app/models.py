from django.db import models


class CowsayInput(models.Model):
    text = models.TextField(default='')
    # output_text = models.TextField()

    def __str__(self):
        return self.text
