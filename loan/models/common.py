from django.db import models


class CommonBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}.{1}".format(self.id, self.title)

    class Meta:
        abstract = True
