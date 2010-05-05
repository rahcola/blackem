from django.db import models

class Pantry(models.Model):
    name = models.CharField(max_length=100)
    owner = modles.ForeignKey('users.User')

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pantries"

