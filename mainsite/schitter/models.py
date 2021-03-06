from django.db import models

# Create your models here.
class Schitt(models.Model):
    name_text = models.CharField(max_length=40)
    schitt_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.schitt_text

    def published(self):
        return self.pub_date

    def name(self):
        return self.name_text

    def text(self):
        return self.schitt_text
